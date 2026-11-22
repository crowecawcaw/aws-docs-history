

# Prerequisites

Before you start a generation, make sure the following are in place:
+ The permissions for dataset generation. For the policy and what each statement grants, see [IAM permissions](#dataset-generation-prereqs-iam).
+ The target dataset already exists and is `ACTIVE`.
+ Your agent’s traces are in Amazon CloudWatch Logs. Dataset generation reads the traces that your agent delivers through AgentCore Observability. For more information, see [AgentCore Observability](observability.md) and [Telemetry setup and delivery](supported-frameworks-telemetry.md).

Dataset generation reads your traces with a forward access session made from your own credentials. There is no execution role. When you start a generation, the service checks that you can run CloudWatch Logs Insights queries on each log group that the source reads, including the results log group of an online evaluation or batch evaluation source, and, for a dataset encrypted with a customer managed key, that you can use that key.

## IAM permissions
<a name="dataset-generation-prereqs-iam"></a>

The following IAM policy grants the permissions needed to run and manage dataset generations.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "DatasetGeneration",
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:StartDatasetGeneration",
                "bedrock-agentcore:GetDatasetGeneration",
                "bedrock-agentcore:ListDatasetGenerations",
                "bedrock-agentcore:DeleteDatasetGeneration"
            ],
            "Resource": "arn:aws:bedrock-agentcore:*:*:dataset/*"
        },
        {
            "Sid": "ReadAgentTraces",
            "Effect": "Allow",
            "Action": [
                "logs:StartQuery",
                "logs:GetQueryResults"
            ],
            "Resource": [
                "arn:aws:logs:us-east-1:111122223333:log-group:/aws/bedrock-agentcore/runtimes/*",
                "arn:aws:logs:us-east-1:111122223333:log-group:/aws/bedrock-agentcore/evaluations/*"
            ]
        },
        {
            "Sid": "BatchEvaluationSource",
            "Effect": "Allow",
            "Action": "bedrock-agentcore:GetBatchEvaluation",
            "Resource": "arn:aws:bedrock-agentcore:*:*:batch-evaluate/*"
        },
        {
            "Sid": "OnlineEvaluationSource",
            "Effect": "Allow",
            "Action": "bedrock-agentcore:GetOnlineEvaluationConfig",
            "Resource": "arn:aws:bedrock-agentcore:*:*:online-evaluation-config/*"
        },
        {
            "Sid": "DatasetKmsKey",
            "Effect": "Allow",
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ]
}
```

The policy includes the following statements:
+  **DatasetGeneration** - Allows the four dataset-generation operations (`StartDatasetGeneration`, `GetDatasetGeneration`, `ListDatasetGenerations`, and `DeleteDatasetGeneration`) on the target dataset.
+  **ReadAgentTraces** - Dataset generation reads your agent’s traces with your own credentials, not an execution role, so you need `logs:StartQuery` and `logs:GetQueryResults` on the log groups that hold your agent’s traces. For an online evaluation or batch evaluation source, you also need them on the log group where that evaluation writes its results, unless it writes results to the source log group. Replace {{111122223333}} with your account ID, {{us-east-1}} with your AWS Region, and the log-group path with the path of your own log groups.
+  **BatchEvaluationSource** - Include this statement only when your source is a batch evaluation. It allows `bedrock-agentcore:GetBatchEvaluation` on the batch evaluation.
+  **OnlineEvaluationSource** - Include this statement only when your source is an online evaluation configuration. It allows `bedrock-agentcore:GetOnlineEvaluationConfig` on the configuration.
+  **DatasetKmsKey** - Include this statement only when the dataset uses a customer managed key. It allows `kms:GenerateDataKey` and `kms:Decrypt` on that key. Replace the example key ARN with your key’s ARN. For the key-policy requirements, see [Dataset encryption](datasets-encryption.md).