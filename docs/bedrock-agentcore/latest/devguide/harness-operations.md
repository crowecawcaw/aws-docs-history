# Observability and cost controls

This page covers monitoring your harness, controlling execution costs, and managing resource tags.

## Observability

Every harness invocation automatically generates traces, logs, and metrics through [AgentCore Observability](observability.md "observability.md") in CloudWatch. Model calls, tool invocations, memory operations, shell commands: each step appears with timing and payload details. No extra configuration. Traces are available from the first invocation.

###### Example

AgentCore CLI

```
# Stream logs
agentcore logs --harness research-agent

# Filter
agentcore logs --harness research-agent --since 1h --level error

# List recent traces
agentcore traces list --harness research-agent

# Get a specific trace
agentcore traces get <trace-id> --harness research-agent
```

AWS CLI/boto3
Traces, logs, and metrics flow to CloudWatch through the harness execution role. View them in the [AgentCore Observability dashboard](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#/gen-ai-observability/agent-core/agents "https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#/gen-ai-observability/agent-core/agents"), or query programmatically through the CloudWatch Logs and X-Ray APIs.

Before you see traces, [enable Transaction Search in CloudWatch](../../../AmazonCloudWatch/latest/monitoring/Enable-Lambda-TransactionSearch.md "../../../AmazonCloudWatch/latest/monitoring/Enable-Lambda-TransactionSearch.md") (one-time per account). See [AgentCore Observability getting started](observability-get-started.md "observability-get-started.md") for setup details.

Learn more: [Observability overview](observability.md "observability.md") · [metrics](observability-runtime-metrics.md "observability-runtime-metrics.md") · [telemetry](observability-telemetry.md "observability-telemetry.md")

## CloudTrail

Harness operations are logged to AWS CloudTrail as management events (control plane) and data events (data plane). In CloudTrail, harness resources appear under the `AWS::BedrockAgentCore::Runtime` resource type rather than a harness-specific type. Harness is a managed abstraction over AgentCore Runtime, and CloudTrail events reflect the underlying runtime resource for consistency.

All harness CloudTrail events use `resources.type` = `AWS::BedrockAgentCore::Runtime`. The event names are:

- `CreateHarness`, `UpdateHarness`, `DeleteHarness`, `GetHarness`, `ListHarnesses` (management events)
- `InvokeAgentRuntime`, `InvokeAgentRuntimeCommand` (data events)

###### Note

Data plane operations appear as `InvokeAgentRuntime` and `InvokeAgentRuntimeCommand` in CloudTrail, matching the underlying Runtime API. The `resources.ARN` field contains the harness ARN for control plane events and the runtime ARN for data plane events.

## Control cost with limits

Set hard caps so a runaway agent can’t burn through resources:

- **`maxIterations`** - reasoning/action cycles per invocation. Default 75.
- **`timeoutSeconds`** - wall-clock timeout for a single invocation. Default 3600.
- **`maxTokens`** - token budget per invocation. Default N/A.
- **`idleRuntimeSessionTimeout`** - how long an idle microVM stays warm. Default 900.
- **`maxLifetime`** - maximum lifetime of a microVM session. Default 28800.

All limits are optional; omit them to use service defaults. Because harness is backed by AgentCore Runtime, harness invocations are also subject to Runtime service quotas. For more information, see [AgentCore harness Service Quotas](bedrock-agentcore-limits.md#harness-service-limits "bedrock-agentcore-limits.md#harness-service-limits") and [AgentCore Runtime Service Quotas](bedrock-agentcore-limits.md#runtime-service-limits "bedrock-agentcore-limits.md#runtime-service-limits").

###### Example

AgentCore CLI
Set defaults:

```
agentcore add harness --name bounded-agent \
  --max-iterations 50 --timeout 1800 --max-tokens 8192 \
  --truncation-strategy sliding_window \
  --idle-timeout 600 --max-lifetime 14400
agentcore deploy
```

The `--truncation-strategy` flag accepts `sliding_window` or `summarization`. The `--idle-timeout` and `--max-lifetime` flags set lifecycle limits in seconds.

Override on a single call:

```
agentcore invoke --harness bounded-agent --max-iterations 20 --harness-timeout 600 \
  "Quick lookup: what's the weather in Seattle?"
```

AWS CLI/boto3

```
aws bedrock-agentcore-control update-harness \
  --harness-id "MyHarness-UuFdkQoXSL" \
  --max-iterations 50 \
  --timeout-seconds 1800 \
  --max-tokens 8192
```

Or override on a single invocation by passing `maxIterations`, `timeoutSeconds`, or `maxTokens` in `invoke_harness`.

## Tags

Apply tags to your harness for cost allocation and access control.

###### Example

AgentCore CLI
Set tags in `harness.json`:

```
{
  "tags": {
    "team": "platform",
    "environment": "staging"
  }
}
```

Run `agentcore deploy` to apply.

AWS CLI/boto3

```
aws bedrock-agentcore-control create-harness \
  --harness-name "MyHarness" \
  --execution-role-arn "arn:aws:iam::123456789012:role/MyHarnessRole" \
  --tags '{"team": "platform", "environment": "staging"}'
```

Tags flow through to deployed CloudFormation resources.

### Related topics

- [Persist memory and filesystem](harness-memory.md "harness-memory.md") - memory persists conversation context across sessions
- [Environment and Skills](harness-environment.md "harness-environment.md") - environment variables and custom containers
- [Security and access controls](harness-security.md "harness-security.md") - execution role policy and IAM permissions
- [API Documentation](harness-get-started.md#api-documentation "harness-get-started.md#api-documentation")
