

# Prerequisites for Insights

Before you use Insights, complete the following prerequisites.

## Configure agent telemetry
<a name="insights-prereqs-telemetry"></a>

Your agent must emit supported OpenTelemetry or OpenInference traces to Amazon CloudWatch Logs, and CloudWatch Transaction Search must be enabled. For setup instructions, see [Observe agent applications](observability.md) and [Supported agent frameworks](supported-frameworks.md).

For online evaluation insights, AgentCore uses the `service.name` resource attribute, configured as `serviceName` in the online evaluation data source, as the Agent Insight `applicationName`. Use a consistent service name for traffic that belongs to the same agent.

## Configure an evaluation
<a name="insights-prereqs-evaluation"></a>

Include `Builtin.FailureAnalysis` in one of the following:
+ An online evaluation configuration, to generate Agent Insights from sampled live traffic and update them as new evidence arrives.
+ A batch evaluation, to generate point-in-time insights from a selected set or time range of sessions.

An online evaluation requires `evaluationExecutionRoleArn`. The role must be able to read the selected CloudWatch log groups and perform the other evaluation operations described in [Prerequisites for AgentCore Evaluations](evaluations-prerequisites.md). The Agent Insight Store itself doesn’t use a customer-provided execution role.

## Enable the Agent Insight Store
<a name="insights-prereqs-store"></a>

Each account has one default Store per supported Region. The Store starts with `enablementStatus` set to `DISABLED`. Enable it, then use `ListAgentInsightStores` or `GetAgentInsightStore` to confirm that:
+  `enablementStatus` is `ENABLED`.
+  `status` is `ACTIVE`.

If the Store is `INACTIVE`, enable it. If it is `UPDATING`, wait for the current update to finish. If it is `ERROR`, read `failureReason` and correct the reported encryption or cleanup problem. Insight Evaluators can’t write Agent Insights until the Store is enabled and active. For instructions, see [Manage the Agent Insight Store](insights-store.md).

## Grant caller permissions
<a name="insights-prereqs-iam"></a>

The following example grants a principal the Agent Insights API permissions and the evaluation permissions used in the examples in this section. Scope the resources and conditions for your environment where the actions support resource-level permissions.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:GetAgentInsightStore",
                "bedrock-agentcore:ListAgentInsightStores",
                "bedrock-agentcore:UpdateAgentInsightStore",
                "bedrock-agentcore:GetAgentInsight",
                "bedrock-agentcore:ListAgentInsights",
                "bedrock-agentcore:UpdateAgentInsight",
                "bedrock-agentcore:CreateOnlineEvaluationConfig",
                "bedrock-agentcore:DeleteOnlineEvaluationConfig",
                "bedrock-agentcore:GetOnlineEvaluationConfig",
                "bedrock-agentcore:UpdateOnlineEvaluationConfig",
                "bedrock-agentcore:StartBatchEvaluation",
                "bedrock-agentcore:GetBatchEvaluation"
            ],
            "Resource": "*"
        }
    ]
}
```

To pass an online evaluation execution role, you also need `iam:PassRole` for that role.

If you configure the Store with a customer managed AWS KMS key, you need additional KMS permissions, and the key policy must allow the service principal. See [Encryption at rest for Agent Insights](insights-security.md).

The example policy covers the Agent Insights and evaluation operations in this section. To use an Agent Insight to guide a recommendation, also grant the recommendation permissions described in [IAM permissions](optimization-prereqs.md#optimization-prereqs-iam) for AgentCore optimization.