

# Operating disaster recovery: detection, response, and recovery
<a name="disaster-recovery-operate"></a>

An incident in the [warm standby architecture](disaster-recovery-resiliency.md#architecture-warm-standby) unfolds in three stages. A canary detects the problem. The agent invoker, the request layer you build between clients and AgentCore, contains it. Then you promote the standby with the incident runbook, making it the Region that serves production.

## Detection: synthetic canary
<a name="detection-synthetic-canary"></a>

AgentCore’s default CloudWatch metrics don’t prove that your agent works end to end, and the internal `/ping` route checks only your container’s readiness. For failover decisions, add a synthetic canary that exercises the full invocation path in each Runtime Region.

Design the canary to report unhealthy when in doubt:
+  **Probe the real path.** Once a minute, a Lambda function or a [CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) canary calls `InvokeAgentRuntime` on a lightweight canary agent. The canary agent returns a fixed value, such as `{"status":"CANARY_OK"}`, only after the expected application path completes. A 200 response proves only that the endpoint answered.
+  **Pin the endpoints.** Invoke the canary agent through a named endpoint pinned to a version, and serve production from a named endpoint too. `DEFAULT` moves to each new version automatically, but a named endpoint keeps its version until you update that endpoint, so updating the runtime doesn’t move the canary endpoint to the new version. Changes to shared dependencies, such as the gateway, can still fail the probe. To release a version, wait until the runtime is `READY`, which can take several minutes, test it through `DEFAULT` with a new session, then update the production endpoint, which happens without downtime, and test again through the production endpoint. Don’t update the canary agent and the production agent in the same window, so that a canary failure points to one change.
+  **Read the whole response.** For a streamed response, fail on any error event, and accept the fixed value only after the stream ends. Fail on any content type that you don’t recognize.
+  **Always publish a value.** Publish a custom metric, `CanaryHealthy`, as 1 or 0. Keep the SDK’s connect and read timeouts inside the function timeout, turn off SDK retries, and publish 0 on any exception.
+  **Alarm on three periods.** Alarm when the `Minimum` of `CanaryHealthy` is below 1 for three consecutive 60-second periods, with `TreatMissingData` set to `breaching`, so that a canary that stops reporting also raises the alarm. Send the ALARM and OK transitions to the same Amazon SNS topic, so that you also hear about recovery.

The following diagram shows the resulting pipeline in one Region. An Amazon EventBridge schedule runs a canary Lambda function that invokes the canary agent every minute. The function publishes `CanaryHealthy` to CloudWatch. A CloudWatch alarm on that metric goes to ALARM after three consecutive failed periods, and it sends both its ALARM and OK notifications to the same Amazon SNS topic, which notifies on-call.

![Canary pipeline: EventBridge runs a canary Lambda every minute, and a CloudWatch alarm notifies SNS on ALARM and OK](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/canary-detection-pipeline.png)


## Response: agent invoker layer
<a name="response-agent-invoker-layer"></a>

Clients call AgentCore only through an agent invoker that you own, such as a Lambda function, an Amazon ECS service, or a shared SDK library. Build it to meet these requirements:
+  **Route to one active Region.** The active-Region record is a small versioned record that names the Region serving production. Send every request to the Region that it names, and never to the other Region, even when the active Region fails. A turn that the standby served before promotion would be saved only in the standby Memory. Read the record in both Regions, use the copy with the higher version, and cache it briefly. When you promote the standby, every invoker switches within that cache time.
+  **Authenticate at both hops.** Authenticate and authorize clients at your application’s entry point, which is the invoker or whatever sits in front of it. Then the invoker authenticates its own call to Runtime. If the runtime version uses IAM inbound auth, it signs with SigV4 from the Lambda execution role or the ECS task role, and that role needs `InvokeAgentRuntime` on the runtime and endpoint ARNs in both Regions. If the version uses a JWT authorizer, the invoker forwards a bearer token that the standby’s authorizer also accepts, and Runtime validates it. A runtime version uses one inbound mode, not both. If your invoker is a shared SDK library, the call to Runtime uses the client’s own credentials or token.
+  **Retry within a deadline, in the active Region only.** Retry with exponential backoff and jitter, inside one deadline for all attempts. Turn off SDK retries, so that only the invoker retries. If the retries fail, serve a fallback, such as a cached response or a human handoff, not the standby.
+  **Use the canary as the fleet-wide signal.** If your invoker uses a circuit breaker (logic that stops sending requests to a failing target for a while), open it in every instance while the active Region’s canary alarm is in `ALARM`, not on a single failed probe, and treat a canary data point older than three canary periods as unhealthy.
+  **Let operators override the canary.** An invoker that follows the canary stops sending requests to the active Region while the canary alarm is in `ALARM`, and it never tries the other Region. So if the canary itself malfunctions, every request goes to the fallback. Give operators a flag, such as an AWS AppConfig flag, that makes invokers ignore the canary.
+  **Preserve the session ID.** Pass the client’s session ID on every call. For HTTP, A2A, and AG-UI agents, that’s the `runtimeSessionId` parameter, sent as the `X-Amzn-Bedrock-AgentCore-Runtime-Session-Id` header. For MCP agents, it’s the `Mcp-Session-Id` header. If you omit `runtimeSessionId`, the SDK generates a new one, which starts a new session.
+  **Make side-effecting tools idempotent.** Retries are safe only when each tool checks a durable record of request IDs before it acts, and skips IDs that it has already handled. That must hold across promotion, because a client that retries after promotion reaches the standby with the same ID. If the stored IDs reach the standby with a delay, a retry right after promotion can still run twice, so also run a check that finds and reverses duplicate actions by request ID.

## Know which errors to retry
<a name="know-which-errors-to-retry"></a>

The following table lists the Runtime errors that matter most in a failover. The Retry? column is a recommendation. For each error’s definition, see the [InvokeAgentRuntime API reference](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeAgentRuntime.html), the [common errors](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/CommonErrors.html), and the [Runtime HTTP protocol contract](runtime-http-protocol-contract.md).


| Code | Error | Retry? | What to do | 
| --- | --- | --- | --- | 
|  **500**, **503**  | InternalServerException, ServiceUnavailable | Yes | Back off exponentially. Count toward any circuit breaker. | 
|  **429**  | ThrottlingException | Yes | Back off longer. Don’t count toward any circuit breaker. If it’s sustained, you might need a [quota increase](bedrock-agentcore-limits.md). | 
|  **409**  | RetryableConflictException | Yes | A session operation is in progress. Retry with short backoff. Not every 409 is retryable, so check the exception name. | 
|  **402**  | ServiceQuotaExceededException | No |  [Request a quota increase](bedrock-agentcore-limits.md). | 
|  **424**  | RuntimeClientError | No | Your agent container returned an error. Check its CloudWatch logs. | 
|  **401**  | UnauthorizedException | No | For agents with inbound OAuth. After failover, it means the standby’s inbound authorizer rejects the caller’s token, often because a setting differs from the primary’s. | 
|  **403**  | AccessDeniedException | No | After failover, a common cause is an IAM policy that scopes `Resource` to primary-Region ARNs. | 

Connection errors and client timeouts also count toward any circuit breaker. Don’t promote the standby for a non-retryable error, which switching Regions doesn’t fix, or for quota pressure.

 [MCP](runtime-mcp-protocol-contract.md) returns most errors inside an HTTP 200 response, as JSON-RPC codes:
+ -32603 for internal errors.
+ -32005 for both `RetryableConflictException`, which you retry, and `ConflictException`, a resource conflict that you don’t retry. Only the message tells them apart.
+ -32003 for both throttling and exceeded quotas, with the same message. [A2A](runtime-a2a-protocol-contract.md) also uses one code, -32053, for both. Retry -32003 and -32053 as throttling. If either persists, you might have exceeded a quota: stop retrying, escalate, and check whether you need a [quota increase](bedrock-agentcore-limits.md).

Map MCP and A2A error codes to the error names in the table before you decide whether to retry. Because SDK retries are off, retry `RetryableConflictException` in your invoker.

## Set up the right alerts
<a name="dr-alerts"></a>

AgentCore publishes [Runtime metrics](observability-runtime-metrics.md) to CloudWatch by default. For DR, these matter most:
+ Alarm on **SystemErrors**, which counts HTTP 500 errors. Don’t base failover decisions on **UserErrors**, which usually indicate a bug on the caller’s side. After promotion, however, build your invoker to alert on a rise in 401 or 403 responses, which points to authorizer or IAM settings that differ in the standby.
+  **Throttles** counts 429 responses. Errors from exceeding quotas (402) are counted with throttling errors, so check the error type to tell them apart.
+ Use `ActiveSessionCount` to watch session quota in either Region.
+ Don’t base failover decisions on the resource-utilization metrics, which can lag by up to an hour.

The canary catches a near-total regional failure. Because each session runs in its own microVM, one probe a minute can miss degradation in part of a Region’s capacity. `SystemErrors` is measured across real traffic, so it catches that.

Complete the one-time CloudWatch Transaction Search setup in each Region. Only Gateway and Payments send trace spans by default. Turn tracing on for the other resources that you use. An alarm can’t evaluate a metric in another Region, so each Region needs its own alarms.

## Incident runbook: the first 30 minutes
<a name="incident-runbook"></a>

When the canary alarm triggers, follow these steps, and investigate only after users are protected.

 **T\+0 to T\+5: Detect and confirm.** The canary alarm notifies you. In CloudWatch, look for a `SystemErrors` spike, rising latency, or throttling. If a direct `InvokeAgentRuntime` call to your production agent succeeds while the canary fails, the canary itself might be faulty. Also check whether a deployment or endpoint update is in progress in that Region. Repeat the call from where the canary runs, through the same endpoint. If that call also succeeds, set the operator override and fix the canary instead of failing over. Clear the override once the canary is fixed. Open an incident tagged with the Region and agent ID, and open an AWS Support case.

 **T\+5 to T\+15: Mitigate.** If errors are sustained, set a feature flag that sends all users to the fallback, without waiting for each request to fail. This flag is separate from the operator override, which only makes invokers ignore the canary. Turn the flag off once test requests that bypass it succeed, whether or not you fail over.

 **T\+15 to T\+30: Fail over.** If the canary is still failing after 15 minutes, confirm that the standby canary is healthy, that a standby session retrieves replicated memory, and that standby quotas have headroom. Then promote the standby. Run these steps from the standby Region, in order:

1.  **Reverse Memory ownership.** Stop copying Memory from the primary to the standby, and start capturing the standby’s writes for failback, as requirements 3 and 5 in [Requirements for any implementation](disaster-recovery-memory.md#memory-replication-requirements) describe. Do this first, so that every change the standby accepts after the switch is captured.

1.  **Make standby file systems writable.** If you use EFS replication, delete the replication configuration.

1.  **Set the active-Region record to the standby.** This moves every invoker. Write the record yourself, as its own step. Your Amazon Application Recovery Controller (ARC) Region switch plan moves DNS by flipping Route 53 health checks. It can also include custom action Lambda steps, but when the primary is impaired you run the plan in ungraceful mode, which skips them.

1.  **Execute the Region switch plan.** The plan flips the Route 53 health checks, which moves DNS to the standby. Confirm in the [failover drill (Days 11–13 of the go-live ramp)](disaster-recovery-validate.md#validate-go-live-ramp) that an ungraceful execution flips the health checks.

 **T\+30 onward: Stabilize.** Verify that new standby sessions retrieve replicated memory, and watch standby session creation against its quota. Stopping sessions in the primary frees no quota in the standby. Then turn off the fallback flag, and confirm that real requests succeed. Keep the primary’s infrastructure running and configured so that you can [fail back](disaster-recovery-validate.md#fail-back-outcomes).

The following timeline summarizes the four stages: detect and confirm (T\+0 to T\+5), mitigate (T\+5 to T\+15), fail over (T\+15 to T\+30), and stabilize (T\+30 onward), with an AWS Support case open in parallel.

![Incident timeline: detect, mitigate, fail over from T+15 to T+30, then stabilize, with a support case in parallel](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/disaster-recovery-incident-timeline.png)
