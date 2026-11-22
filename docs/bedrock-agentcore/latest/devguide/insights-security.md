

# Encryption at rest for Agent Insights

Amazon Bedrock AgentCore encrypts Agent Insights in transit and at rest. This topic describes encryption-at-rest options, key permissions, key-unavailability behavior, and AWS KMS activity logging for Agent Insights.

## Options for encryption at rest
<a name="insights-security-options"></a>

By default, AgentCore transparently encrypts Agent Insight data on the server side at rest with an AWS owned key. You don’t need to configure encryption, and you can’t view, manage, or audit the use of the AWS owned key.

You can instead configure the Agent Insight Store with a customer managed AWS KMS key. AgentCore uses the customer managed key to protect customer-derived Agent Insight content, including names, descriptions, sample session references, and detailed Insight content. AgentCore continues to encrypt all Store data at rest.

The Store encryption setting applies to Agent Insights generated from both online and batch evaluations. It doesn’t configure encryption for online evaluation logs or batch evaluation results. For information about batch evaluation result encryption, see [Encrypt batch evaluation results](batch-evaluations-encryption.md).

## Encrypt Agent Insights with a customer managed KMS key
<a name="insights-security-kms"></a>

### How AgentCore uses your customer managed key
<a name="insights-security-how-kms-is-used"></a>

AgentCore uses envelope encryption with the AWS Encryption SDK before it stores protected Agent Insight content. The service calls `kms:GenerateDataKey` to encrypt content and `kms:Decrypt` to decrypt it.

AgentCore doesn’t create AWS KMS grants or cache data keys for the Agent Insight Store. Access is controlled by the permissions of the caller that configures the Store and by the key policy permissions granted to the `bedrock-agentcore.amazonaws.com` service principal.

AgentCore uses the encryption context key `aws:bedrock-agentcore:agentInsightStoreArn`, with the Store ARN as its value, for `GenerateDataKey` and `Decrypt` operations. The encryption context doesn’t contain Agent Insight content.

### Customer managed key requirements
<a name="insights-security-key-requirements"></a>

The customer managed key must meet the following requirements:
+ The key spec is `SYMMETRIC_DEFAULT`.
+ The key usage is `ENCRYPT_DECRYPT`.
+ The key is enabled.
+ The key is in the same AWS Region as the Store.
+ You specify the full key ARN, not a key ID or alias ARN.

### Customer managed key permissions
<a name="insights-security-kms-permissions"></a>

The principal that calls `UpdateAgentInsightStore` needs the following permissions on the key:
+  `kms:DescribeKey` 
+  `kms:GenerateDataKey` 
+  `kms:Decrypt` 

The key policy must also allow the `bedrock-agentcore.amazonaws.com` service principal to use:
+  `kms:GenerateDataKey` 
+  `kms:Decrypt` 

Principals that read Agent Insights also need `kms:Decrypt` permission on every customer managed key that protects the requested content.

The following example shows least-privilege statements to add to the key’s existing policy. Keep the policy statements that administer the key. Replace the account ID, Region, and example principal ARNs with values for your account. The example `InsightsAdmin` and `InsightsReader` roles are caller identities; AgentCore doesn’t assume these roles.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowInsightsAdminDescribeKeyViaAgentCore",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/InsightsAdmin"
            },
            "Action": "kms:DescribeKey",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "bedrock-agentcore.us-west-2.amazonaws.com"
                }
            }
        },
        {
            "Sid": "AllowInsightsAdminSetKeyViaAgentCore",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/InsightsAdmin"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "bedrock-agentcore.us-west-2.amazonaws.com",
                    "kms:EncryptionContext:aws:bedrock-agentcore:agentInsightStoreArn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:agent-insight-store/default-insight-store"
                }
            }
        },
        {
            "Sid": "AllowInsightsReaderReadInsightsViaAgentCore",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/InsightsReader"
            },
            "Action": "kms:Decrypt",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "bedrock-agentcore.us-west-2.amazonaws.com",
                    "kms:EncryptionContext:aws:bedrock-agentcore:agentInsightStoreArn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:agent-insight-store/default-insight-store"
                }
            }
        },
        {
            "Sid": "AllowAgentCoreWriteInsightsForThisStore",
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
                    "aws:SourceAccount": "111122223333",
                    "kms:EncryptionContext:aws:bedrock-agentcore:agentInsightStoreArn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:agent-insight-store/default-insight-store"
                },
                "ArnEquals": {
                    "aws:SourceArn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:agent-insight-store/default-insight-store"
                }
            }
        }
    ]
}
```

Each statement grants only the permissions needed for the following purpose:
+  `AllowInsightsAdminDescribeKeyViaAgentCore` – Allows the caller that configures Store encryption to validate the key’s properties through AgentCore.
+  `AllowInsightsAdminSetKeyViaAgentCore` – Allows AgentCore to verify, using the caller’s identity, that the key can generate data keys and decrypt data. The caller also needs `kms:Decrypt` on an outgoing key while AgentCore changes the Store key.
+  `AllowInsightsReaderReadInsightsViaAgentCore` – Allows a caller to decrypt Agent Insight content that the caller retrieves through AgentCore.
+  `AllowAgentCoreWriteInsightsForThisStore` – Allows the AgentCore service principal to encrypt, decrypt, and re-encrypt content for the specified Store. The `aws:SourceAccount` and `aws:SourceArn` conditions help prevent a confused deputy.

The caller statements use `kms:ViaService` to restrict key use to requests that AgentCore makes in a [forward access session](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). The service-principal statement doesn’t use `kms:ViaService` because AgentCore uses its own service identity for those requests.

Before it accepts an update to a customer managed key, AgentCore verifies that the caller and service principal can generate data keys and decrypt with the key. Provide the full key ARN from the Store’s Region, not a key ID or alias ARN. Keep the applicable caller and service-principal statements on each customer managed key that the Store still uses.

### Configure and change the Store key
<a name="insights-security-configure-key"></a>

Set `encryptionConfiguration.mode` to `CUSTOMER_MANAGED_KMS` and provide `encryptionConfiguration.kmsKeyArn` when you call [UpdateAgentInsightStore](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateAgentInsightStore.html). You can change from the AWS owned key to a customer managed key, from one customer managed key to another, or from a customer managed key back to the AWS owned key.

When AgentCore accepts an encryption change, the Store enters `UPDATING`. New Agent Insight content uses the new encryption configuration while AgentCore re-encrypts existing Agent Insight content and grouping data in the background. Existing content remains readable during the update because its encryption metadata identifies the key that protects it.

Keep the previous and new customer managed keys enabled and preserve the required permissions until the Store returns to `ACTIVE`. After the update completes, the current Agent Insight content and grouping data use the new encryption configuration. Older storage versions and backups can remain encrypted under a previous customer managed key until their normal retention periods expire. Disabling or deleting that key can prevent recovery of those copies.

Automatic rotation of a customer managed AWS KMS key doesn’t require an Agent Insight Store update because its key ARN doesn’t change.

For commands and Store state behavior, see [Change Store encryption](insights-store.md#insights-store-encryption-update).

### Scope access to the Store
<a name="insights-security-scope-key-access"></a>

Use the following policy conditions together to restrict use of the customer managed key:
+  `kms:EncryptionContext:aws:bedrock-agentcore:agentInsightStoreArn` – Restricts `GenerateDataKey` and `Decrypt` operations to the exact Store ARN. AgentCore supplies this encryption context for protected Agent Insight content.
+  `aws:SourceAccount` and `aws:SourceArn` – Restrict service-principal access to the account and exact Store that made the request. Use these conditions in statements for `bedrock-agentcore.amazonaws.com`.
+  `kms:ViaService` – Restricts caller permissions to requests that AgentCore makes on the caller’s behalf. Specify `bedrock-agentcore.<region>.amazonaws.com`, replacing `<region>` with the Store’s Region, as shown in the policy example.

### If a customer managed key becomes unavailable
<a name="insights-security-key-unavailable"></a>

**Warning**  
Don’t disable or schedule deletion of a key, or revoke access to it, while the Store or any of its Agent Insights still uses it. New writes can fail, and deleting the key can permanently prevent access to encrypted Agent Insight content.

If AgentCore can’t use the key:
+ Generated Agent Insight content can report `customerMetadataStatus` as `CUSTOMER_KEY_UNAVAILABLE`.
+ New writes or an encryption update can fail.
+ The Store can enter `ERROR` during re-encryption.

Restore the key and its permissions, then retry the operation. During an encryption change, keep all old and new keys usable until the Store returns to `ACTIVE`.

## Monitor AgentCore interaction with AWS KMS
<a name="insights-security-kms-cloudtrail"></a>

 AWS CloudTrail records the AWS KMS API calls made against your customer managed key. The following events can appear:


| Event name | When it occurs | 
| --- | --- | 
|  `DescribeKey`  | When AgentCore validates the key’s properties for a Store update. | 
|  `GenerateDataKey`  | When AgentCore validates key access or encrypts Agent Insight content. | 
|  `Decrypt`  | When AgentCore validates key access, decrypts Agent Insight content, or re-encrypts content during a key change. | 

For `GenerateDataKey` and `Decrypt` events, `requestParameters.encryptionContext` includes `aws:bedrock-agentcore:agentInsightStoreArn` with the Store ARN as its value.

For more information, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html#searching-kms-ct) in the * AWS Key Management Service Developer Guide*.

## Log Agent Insights API activity with AWS CloudTrail
<a name="insights-security-cloudtrail"></a>

Agent Insight data-plane operations are CloudTrail data events and aren’t recorded in Event history by default:
+  `ListAgentInsights` 
+  `GetAgentInsight` 
+  `UpdateAgentInsight` 

To record the data events, configure a trail or CloudTrail Lake event data store for the `AWS::BedrockAgentCore::AgentInsightStore` resource type.

CloudTrail can also emit service events:
+  `CreateAgentInsightStore` when AgentCore provisions the default Store’s backing state.
+  `CreateAgentInsight` when AgentCore adds an Agent Insight.
+  `DeleteAgentInsight` when AgentCore removes an Agent Insight.

Agent Insights don’t have individual ARNs. The Insight service events identify the parent Agent Insight Store as the resource and include `agentInsightId` and `applicationName` in the event details.

**Important**  
Additional charges apply for logging CloudTrail data events. For more information, see [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/).