

# Batch evaluation encryption
<a name="batch-evaluations-encryption"></a>

When you specify a `kmsKeyArn` on a batch evaluation, the service encrypts all output artifacts stored in S3 using S3 server-side encryption with KMS (SSE-KMS). This includes the data source configuration, session metadata, evaluation results, and insight results (for example from `Builtin.FailureAnalysis`).

The `kmsKeyArn` is specified at creation time via `StartBatchEvaluation`.

## How it works
<a name="batch-evaluations-encryption-how-it-works"></a>

Batch evaluation encryption uses S3 SSE-KMS. When the service writes or reads batch evaluation output in S3, S3 calls KMS on behalf of the service to encrypt or decrypt the data. The service principal (`bedrock-agentcore.amazonaws.com`) must have KMS permissions in the key policy.

At API time, the service validates that the caller has KMS permissions using a dry-run check (Forward Access Sessions). This catches permission issues immediately rather than failing asynchronously during the batch evaluation workflow.

The service also validates that it can perform `kms:GenerateDataKey` with its own credentials to ensure the key policy grants the service principal the required permissions for writing encrypted output.

When you call `GetBatchEvaluation` on a batch evaluation that uses a customer managed key, the service checks with your credentials (Forward Access Sessions) that you can still use the key. The service calls `kms:DescribeKey` and a dry-run `kms:Decrypt` with the encryption context of the batch evaluation. If either call is denied, `GetBatchEvaluation` returns `AccessDeniedException` and no results.

AgentCore Evaluations supports only symmetric encryption KMS keys. The KMS key must be in the same AWS Region as the batch evaluation.

### Configuring permissions to use a customer managed KMS key
<a name="batch-evaluations-encryption-key-policy"></a>

The following key policy provides the minimum permissions required for batch evaluation encryption. The policy has three statements:
+  **AllowCallerAccess** – Allows the IAM user or role to validate the key via `DescribeKey`.
+  **AllowCallerCryptoOps** – Allows the IAM user or role to encrypt and decrypt, scoped by encryption context.
+  **AllowServicePrincipalAccess** – Allows the AgentCore service principal to encrypt and decrypt batch evaluation data, scoped by source account, source ARN, and encryption context.

```
{
"Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowCallerAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyBatchEvaluationRole"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*"
    },
    {
      "Sid": "AllowCallerCryptoOps",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyBatchEvaluationRole"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:bedrock-agentcore:batchEvaluationArn": "arn:aws:bedrock-agentcore:us-east-1:111122223333:batch-evaluate/*"
        }
      }
    },
    {
      "Sid": "AllowServicePrincipalAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock-agentcore.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:bedrock-agentcore:us-east-1:111122223333:batch-evaluate/*"
        },
        "StringLike": {
          "kms:EncryptionContext:aws:bedrock-agentcore:batchEvaluationArn": "arn:aws:bedrock-agentcore:us-east-1:111122223333:batch-evaluate/*"
        }
      }
    }
  ]
}
```

The policy contains the following statements:
+  **AllowCallerAccess** – Grants the IAM role `kms:DescribeKey` permission for key validation when you start a batch evaluation and when you call `GetBatchEvaluation`. Replace {{111122223333}} with your account ID and {{MyBatchEvaluationRole}} with the IAM role or user that starts batch evaluations.
+  **AllowCallerCryptoOps** – Grants the IAM role `kms:GenerateDataKey` and `kms:Decrypt` permissions, scoped by the `aws:bedrock-agentcore:batchEvaluationArn` encryption context. Replace {{111122223333}}, {{MyBatchEvaluationRole}}, and {{us-east-1}} with your values. To allow access to all batch evaluations in your account, use a wildcard with `StringLike`: `arn:aws:bedrock-agentcore:us-east-1:111122223333:batch-evaluate/*`.
+  **AllowServicePrincipalAccess** – Grants the AgentCore service principal `kms:GenerateDataKey` and `kms:Decrypt` permissions for encrypting and decrypting batch evaluation data. Scoped by source account (`aws:SourceAccount`) and source ARN (`aws:SourceArn`) to prevent confused deputy attacks, and by the `aws:bedrock-agentcore:batchEvaluationArn` encryption context. Replace {{us-east-1}} and {{111122223333}} with your region and account ID.

### Scoping down access to the customer managed KMS key
<a name="batch-evaluations-encryption-scoping"></a>

You can use the encryption context to scope down access to the customer managed key. AgentCore Evaluations includes the following encryption context in all KMS operations:

```
{
  "aws:bedrock-agentcore:batchEvaluationArn": "arn:aws:bedrock-agentcore:us-east-1:111122223333:batch-evaluate/batch-evaluation-id"
}
```

You can use this encryption context in key policy conditions to restrict KMS operations to specific batch evaluations, as shown in the caller and service principal statements in the example key policy above. Both statements are scoped by the encryption context. The service principal statement is additionally scoped by `aws:SourceAccount` and `aws:SourceArn`.

## Starting a batch evaluation with a customer managed KMS key
<a name="batch-evaluations-encryption-creating"></a>

Specify the `kmsKeyArn` parameter when calling `StartBatchEvaluation`:

**Example**  
With the AgentCore CLI, use `--kms-key-arn` to specify a KMS key for encrypting batch evaluation results.  

```
agentcore eval batch-evaluation evaluate \
  --agent <AGENT_ID> \
  --evaluators Builtin.Correctness \
  --name my_encrypted_eval \
  --kms-key-arn arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
```

```
aws bedrock-agentcore start-batch-evaluation \
  --batch-evaluation-name "MyEncryptedBatchEval" \
  --kms-key-arn "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab" \
  --evaluators '[{"evaluatorId": "Builtin.Helpfulness"}]' \
  --data-source-config '{
    "cloudWatchLogs": {
      "logGroupNames": ["/aws/bedrock-agentcore/runtimes/my-agent-abc123-DEFAULT"],
      "serviceNames": ["my-agent.DEFAULT"],
      "filterConfig": {
        "timeRange": {
          "startTime": "2025-01-01T00:00:00Z",
          "endTime": "2025-01-02T00:00:00Z"
        }
      }
    }
  }'
```

```
import boto3

client = boto3.client('bedrock-agentcore')

response = client.start_batch_evaluation(
    batchEvaluationName='MyEncryptedBatchEval',
    kmsKeyArn='arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
    evaluators=[{'evaluatorId': 'Builtin.Helpfulness'}],
    dataSourceConfig={
        'cloudWatchLogs': {
            'logGroupNames': ['/aws/bedrock-agentcore/runtimes/my-agent-abc123-DEFAULT'],
            'serviceNames': ['my-agent.DEFAULT'],
            'filterConfig': {
                'timeRange': {
                    'startTime': '2025-01-01T00:00:00Z',
                    'endTime': '2025-01-02T00:00:00Z'
                }
            }
        }
    }
)

print(f"Batch Evaluation ID: {response['batchEvaluationId']}")
```

## Monitoring KMS usage for batch evaluations
<a name="batch-evaluations-encryption-monitoring"></a>

The following CloudTrail event names appear for batch evaluation KMS operations:
+  `GenerateDataKey` — When writing encrypted batch evaluation output to S3 (data source config, session metadata, evaluation results, insight results). The `encryptionContext` field contains `aws:bedrock-agentcore:batchEvaluationArn`.
+  `Decrypt` — When reading encrypted batch evaluation output from S3. Decrypt events also include a dry-run `Decrypt` made with the caller’s credentials on `GetBatchEvaluation`, which carries the `aws:bedrock-agentcore:batchEvaluationArn` encryption context.
+  `DescribeKey` — When validating the key at batch evaluation creation time and on `GetBatchEvaluation`.

For more information about monitoring KMS usage, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html) in the * AWS Key Management Service Developer Guide*.

## Behavior when a key becomes unavailable
<a name="batch-evaluations-encryption-unavailable"></a>

If you disable or delete the customer managed KMS key used by a batch evaluation:
+  **StartBatchEvaluation**: Fails at validation with `ValidationException`.
+  **GetBatchEvaluation**: Returns metadata (name, status, timestamps), but the service cannot read evaluation results stored in encrypted S3 objects.
+  **ListBatchEvaluations**: Succeeds because listing returns metadata only and does not require KMS operations.
+  **StopBatchEvaluation**: Succeeds because stopping does not require decrypting data.
+  **DeleteBatchEvaluation**: Succeeds because S3 object deletion does not require KMS decryption.

To restore access, re-enable the key or update the key policy to grant the required permissions.

The AgentCore CLI maps these lifecycle operations as follows:
+  **StartBatchEvaluation**: `agentcore eval batch-evaluation evaluate` 
+  **GetBatchEvaluation**: `agentcore eval batch-evaluation get --id <id>` 
+  **ListBatchEvaluations**: `agentcore eval batch-evaluation list` 
+  **StopBatchEvaluation**: `agentcore eval batch-evaluation stop --id <id>` 

To call `DeleteBatchEvaluation`, use the AWS SDK.