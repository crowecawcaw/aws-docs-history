

# Validating disaster recovery: checklist, go-live ramp, and failback
<a name="disaster-recovery-validate"></a>

Before you rely on the standby Region of the [warm standby architecture](disaster-recovery-resiliency.md#architecture-warm-standby), set it up, prove failover with a 14-day go-live ramp, and plan failback.

## Disaster recovery checklist
<a name="dr-checklist"></a>

Settings such as Memory IDs, gateway URLs, workload identities, private endpoints, IAM resource ARNs, and Kinesis streams contain Region-specific identifiers. A standby that copies the primary’s values points back at the primary, so give it its own.

### Setup (do once)
<a name="_setup_do_once"></a>

Complete the following setup tasks before you begin the go-live ramp. You only need to complete this setup once.
+  **Deployment.** Deploy the same agent runtime version to both Regions from the same IaC. For container images, enable Amazon ECR cross-Region replication, re-push existing images, and compare digests. For direct code, upload the ZIP archive to S3 in each Region and pin the object version.
+  **Routing.** Create the Route 53 failover records and an Amazon Application Recovery Controller (ARC) [Region switch](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.html) plan with a Route 53 health check step for those records. Attach the health check that the plan creates for each Region to that Region’s record. Give the plan an execution role, and decide who can execute it. Keep a copy of the active-Region record (a small versioned record that names the Region serving production) in each Region, so that promotion (making the standby the Region that serves production) can write it and each agent invoker (the request layer you build between clients and AgentCore) can read it without the primary.
+  **Public entry point.** Route 53 hosted zones get AWS Shield Standard DDoS protection automatically. Put each Region’s invoker behind an entry point that AWS WAF supports, such as an Application Load Balancer or an API Gateway REST API, because a web ACL doesn’t attach to a Lambda function or an ECS service directly. Deploy the same rules in both Regions from the same IaC, because a regional web ACL protects only resources in its own Region.
+  **Workload identities.** AgentCore Runtime and AgentCore Gateway each create a workload identity when you deploy them, so the standby has its own. Read its ARN from `workloadIdentityDetails`, and use it wherever the primary’s appears.
+  **Credential providers.** Create OAuth2 and API key credential providers in the standby. Each new OAuth2 provider gets its own callback URL, which `GetOauth2CredentialProvider` returns. Register it at your identity provider **before** an incident, because you can’t make that change during a failover. If you use the authorization code grant with session binding, also register your application’s callback endpoint on the standby workload identity with `UpdateWorkloadIdentity`.
+  **Inbound authorizers.** Make the standby’s whole [custom JWT authorizer configuration](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CustomJWTAuthorizerConfiguration.html) match the primary’s, not only the discovery URL. Give Region-specific fields, such as `allowedWorkloadConfiguration`, the standby’s values. A mismatch shows up after failover as a 401 error on every call.
+  **Token vault.** The token vault is Region-scoped, and no AgentCore API copies it, so users' stored consent doesn’t carry over. Decide in advance what a user sees after failover when a feature needs a token that the standby’s vault doesn’t have: a reauthorization prompt in the flow, or the feature blocked for that user until they reauthorize. If you encrypt the vault with a customer managed key, create a separate single-Region key in the standby, and set it on the standby’s token vault as [Configure with API operations or an AWS SDK](api-configuration-encryption.md) describes.
+  **Gateways and policy engines.** Re-create each gateway with its targets and rate limits in the standby, and confirm that each target’s backend is reachable from there. If a gateway references a policy engine, create an equivalent engine and policies in the standby.
+  **Observability.** In each Region, complete the Transaction Search setup, configure log delivery, and deploy the canary (a synthetic probe that invokes a lightweight canary agent once a minute) and the `SystemErrors` alarms from the same IaC. Set each runtime’s trace destination explicitly, because agents created at different times can default to different log groups.
+  **Quotas.** Request increases for the [quotas that limit a failover](disaster-recovery-resiliency.md#dr-service-limits) before you need them.
+  **Memory and file systems.** Set up the replication that you chose so that it meets the [requirements for any implementation](disaster-recovery-memory.md#memory-replication-requirements). For session state and file systems, see [Session storage and file systems](disaster-recovery-resiliency.md#dr-session-storage).

### Pre-flight (before each ramp phase, through the Days 11–13 drill)
<a name="_pre_flight_before_each_ramp_phase_through_the_days_1113_drill"></a>
+ Each failover record carries its Region’s health check, non-alias records use a TTL of 60 seconds or less, and plan evaluation reports no warnings.
+ The active-Region record names the primary, and invokers in both Regions read it.
+ Memory replication to the standby is running, and capture of standby writes for failback is ready but off.
+ Canaries have been healthy in both Regions for at least 24 hours, and the standby alarms read OK.
+ Artifacts and authorizer configurations match, apart from Region-specific fields, which hold the standby’s own values.
+ Replication lag is within your target recovery point objective (RPO), and no short-term memory (STM) turn was abandoned.
+ A new standby session retrieves replicated memory.
+ Standby quotas are at or above the primary’s.
+ A test authorization completes end to end in the standby.
+ The on-call team has read the [incident runbook](disaster-recovery-operate.md#incident-runbook).

## Validate: a 14-day go-live ramp
<a name="validate-go-live-ramp"></a>

Before you rely on the standby, prove it with synthetic load, then with one full production failover drill. Don’t split production traffic between Regions by weight. That would need two safeguards: routing that always sends a conversation to the same Region, and conflict resolution. Without them, the Regions end up with different versions of a conversation.
+  **Days 1–3, dark launch.** Run canaries in both Regions, and confirm that alarms trigger and resolve correctly and that artifacts match.
+  **Days 4–7, synthetic continuity.** Create test actors and sessions in the primary, then confirm that new standby sessions see what you replicate. For long-term memory (LTM), include creates, updates, and deletes. For STM, rebuild a conversation with `ListEvents`.
+  **Days 8–10, quota stress.** Ramp synthetic sessions in the standby to your expected reconnect rate and concurrency. Don’t reuse production actor or session IDs.
+  **Days 11–13, DR drill.** In a maintenance window, run the promotion steps of the [incident runbook](disaster-recovery-operate.md#incident-runbook) in order, running the Region switch plan in ungraceful mode (the execution mode for when the primary is impaired). Fail the primary at a layer that you own, because AWS Fault Injection Service has no AgentCore-specific action. For example, apply `aws:network:disrupt-vpc-endpoint` to the primary AgentCore interface endpoint. For this to work, route the canary and the runbook’s direct-invoke check through that endpoint. Confirm continuity, tool idempotency (a retried tool call doesn’t repeat its action), quota headroom, and recovery notifications.
+  **Day 14, fail back and freeze.** Fail back until every [failback outcome](#fail-back-outcomes) holds. Then freeze features for a week and record latency baselines.

### Stop triggers
<a name="dr-stop-triggers"></a>

Stop the current phase if any of these occurs, and find the root cause before you advance:
+ The error rate exceeds 1% over five minutes.
+ p95 latency exceeds your SLO for two consecutive evaluation periods.
+ A canary is unhealthy for more than three minutes in a Region you didn’t deliberately fail. During the drill, that’s the standby.
+ Replication falls behind your target RPO, or an STM turn is abandoned.
+ A continuity or idempotency check fails.

If production has already moved and the standby is the problem, stop the fault injection experiment, set the active-Region record to the primary, and execute the Region switch plan back. Until you reconcile the drill window, the primary lacks the changes that the standby accepted during the drill.

## Fail back: required outcomes
<a name="fail-back-outcomes"></a>

Failback is a promotion in the other direction, after the primary recovers. The steps depend on your implementation, so build a procedure that meets each of the following outcomes, and prove it on Day 14.

1.  **Nothing the standby accepted is lost.** Every LTM change and STM turn that the standby accepted reaches the primary. Changes that the standby accepts before traffic switches back reach the primary before it takes traffic. Changes accepted while traffic switches back reach it before you stop capturing standby writes. If you copy STM turns with `ListEvents`, note that it returns no `clientToken` (the token that keeps a retried `CreateEvent` call from writing a duplicate turn). Derive one for each event, for example from a hash of the standby `eventId`. Also reuse each event’s `eventTimestamp`, and add `extractionMode=SKIP` if you also replicate LTM, so that the primary doesn’t extract the same LTM records again.

1.  **Conflicts are resolved deliberately.** Where a record changed in both Regions, the newer change wins. Queue a record for manual review when the order of its changes is unclear. For example, a primary edit from just before the incident never replicated, so a standby edit made after failover didn’t account for it, and the two edits conflict.

1.  **No change loops back.** Keep the primary-to-standby copy stopped until the standby’s changes have reached the primary, and write each replication consumer (the program that reads one Memory’s change stream and writes to the other Memory) so that it skips changes that the other consumer wrote.

1.  **The primary is current and writable before traffic returns.** Copy what the standby wrote to file systems, such as EFS, back to the primary, and restore anything that you made read-only or redirected at promotion.

1.  **Ownership moves cleanly.** Set the active-Region record to the primary, then execute the Region switch plan back.

1.  **Both directions are protected again.** Stop capturing standby writes, including any STM writes to the primary, and leave that capture ready but off. Then restart the primary-to-standby copy, and any replication that you removed at promotion, such as EFS, from the primary to the standby.

## Clean up resources
<a name="clean-up-resources"></a>

If you deployed this architecture to try it, delete the following, standby first:
+ The canaries, their alarms and SNS topics, and the canary agent runtime, in both Regions.
+ The standby agent runtime and endpoints, gateway and targets, policy engine, and credential providers. Remove the standby callback URL from your identity provider, and schedule deletion of the standby KMS keys.
+ Memory streaming on both Memories, the Kinesis streams and their consumers, and, after you retain any records that you need, the standby Memory.
+ The active-Region record, replication state, and deduplication records (the stored request IDs that keep a retried tool call from acting twice), according to their retention requirements.
+ The ECR replication rules, the replicated images, and any export buckets.
+ The Region switch plan, which bills monthly while it exists, and then the Route 53 failover records and health checks.