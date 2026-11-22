

# Using customer managed keys with your knowledge base

If you encrypt your knowledge base with a customer managed key, you must tell Connect Customer agent assist which key to use in the replica Region. A KMS key is a Regional resource, so the key that protects your data in the source Region can't be used in the replica Region. The key that you nominate for the replica Region is called the *replica key*.

How you nominate the replica key depends on whether you're creating a knowledge base or already have one.

**Important**  
A knowledge base that's encrypted with a customer managed key doesn't replicate until you register a replica key for the replica Region. Register the replica key before the knowledge base replicates.

## Providing a replica key when you create a knowledge base
<a name="global-resiliency-quick-responses-cmk-new"></a>

When you create a knowledge base, include the Amazon Resource Name (ARN) of the replica key in the `replicaKmsKeys` member of `serverSideEncryptionConfiguration`. The member is a list of objects, each with an `arn` field, and takes at most one key for each Region. This member is available on the [CreateKnowledgeBase](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_CreateKnowledgeBase.html) API.

The following example shows `serverSideEncryptionConfiguration` with a replica key:

```json
"serverSideEncryptionConfiguration": {
    "kmsKeyId": "arn:aws:kms:{{source-region}}:{{123456789012}}:key/{{source-key-id}}",
    "replicaKmsKeys": [
        {
            "arn": "arn:aws:kms:{{replica-region}}:{{123456789012}}:key/{{replica-key-id}}"
        }
    ]
}
```

In the example, replace the following values:

{{source-region}}  
The Region of the key that encrypts the knowledge base.

{{source-key-id}}  
The ID of the key that encrypts the knowledge base.

{{replica-region}}  
The Region of the replica key.

{{replica-key-id}}  
The ID of the replica key.

{{123456789012}}  
Your AWS account ID.

In the response, check that `replicaKmsKeys` includes the replica key. If you don't see it, register the key as described in [Registering a replica key for an existing knowledge base](#global-resiliency-quick-responses-cmk-existing).

## Registering a replica key for an existing knowledge base
<a name="global-resiliency-quick-responses-cmk-existing"></a>

If you already encrypted a knowledge base with a customer managed key, you don't need to create it again. Replicating your instance doesn't register a replica key for you, so register one for each knowledge base that doesn't have one.

To register a replica key, you need `kms:GenerateDataKey` permission on the replica key, and `kms:CreateGrant` permission on the key that encrypts the knowledge base. For more information, see [register-knowledge-base-replica-key](https://docs.aws.amazon.com/cli/latest/reference/qconnect/register-knowledge-base-replica-key.html) in the *AWS CLI Command Reference*.

**To register replica keys for existing knowledge bases**

1. In the source Region, call the `RegisterKnowledgeBaseReplicaKey` API with the ARN of the replica key. The following AWS CLI command registers a replica key:

   ```bash
   aws qconnect register-knowledge-base-replica-key \
       --region {{source-region}} \
       --knowledge-base-id {{knowledge-base-id}} \
       --replica-kms-key arn=arn:aws:kms:{{replica-region}}:{{123456789012}}:key/{{replica-key-id}}
   ```

   In the command, replace the following values:  
{{source-region}}  
The Region where you created the knowledge base.  
{{knowledge-base-id}}  
The ID of the knowledge base.  
{{replica-region}}  
The Region of the replica key.  
{{replica-key-id}}  
The ID of the replica key.  
{{123456789012}}  
Your AWS account ID.

   Make sure that you have the permissions listed earlier in this section and that the replica key exists in the replica Region before you call the API. If the replica key doesn't exist, or you don't have `kms:GenerateDataKey` permission on it, the call returns a `ValidationException`.

1. In the response, check that the `replicaKmsKeys` member of `serverSideEncryptionConfiguration` includes the replica key.

**Note**  
`RegisterKnowledgeBaseReplicaKey` uses the replica key in the replica Region to validate it, so update the key policy before you make the call. For more information, see [Updating the KMS key policy](#global-resiliency-quick-responses-key-policy).

**Important**  
You can register a replica key only once for each Region. After you register a replica key, you can't change it. A request with a different key fails with a `ConflictException`. To use a different key, delete the knowledge base and create it again with the key that you want.

## Encrypting the knowledge base in the replica Region
<a name="global-resiliency-quick-responses-cmk-replica"></a>

The replicated knowledge base is encrypted with the key in its own Region. When you call the [GetKnowledgeBase](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_GetKnowledgeBase.html) API in the replica Region, the `serverSideEncryptionConfiguration` reports the replica Region key as `kmsKeyId`, and the source Region key as the replica key. Your data is never protected by a key from another Region.

**Note**  
You can use a single-Region key in each Region, or a multi-Region key. If you use a multi-Region key, you must nominate the related multi-Region key in the replica Region as the replica key. Connect Customer agent assist doesn't detect it automatically. Specify it in `replicaKmsKeys` when you create the knowledge base, or register it later by calling the `RegisterKnowledgeBaseReplicaKey` API. The knowledge base doesn't replicate until you do.  
Related multi-Region keys have separate key policies, so update the key policy in both Regions. For more information, see [Multi-Region keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *AWS Key Management Service Developer Guide*.

## Updating the KMS key policy
<a name="global-resiliency-quick-responses-key-policy"></a>

The Connect Customer managed synchronization service-linked role (SLR) performs replication on your behalf. If you encrypt your knowledge base with a customer managed key, you must update the key policy of the keys in *both* Regions to allow that role to use the key.

**Important**  
Without these permissions, replication of the encrypted knowledge base fails.

In each Region, add the following JSON statement to the key policy of your customer managed key. Replace {{123456789012}} with the ID of the AWS account that contains your Connect Customer instance.

```json
{
    "Sid": "AllowConnectSynchronization",
    "Effect": "Allow",
    "Principal": {
        "AWS": "*"
    },
    "Action": [
        "kms:CreateGrant",
        "kms:DescribeKey",
        "kms:Decrypt",
        "kms:GenerateDataKey*"
    ],
    "Resource": "*",
    "Condition": {
        "ArnLike": {
            "aws:PrincipalArn": "arn:aws:iam::{{123456789012}}:role/aws-service-role/synchronization.connect.amazonaws.com/AWSServiceRoleForAmazonConnectSynchronization_*"
        }
    }
}
```

The name of the role ends with a unique suffix, which the wildcard matches. For more information about the role, see [Using service-linked roles for Connect Customer Managed Synchronization](managed-synchronization-slr.md).

In a key policy, `"Resource": "*"` refers to the KMS key that you attach the policy to. You can't use a wildcard in a principal to match part of a role name, so the statement sets the principal to `"*"` and uses the `aws:PrincipalArn` condition to limit it to the managed synchronization SLR. For more information, see [Creating a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-overview.html) in the *AWS Key Management Service Developer Guide*.

Your key policy must also grant Connect Customer agent assist itself permission to use the key. If you already use a customer managed key with your knowledge base, these permissions are in place on the key in the source Region. Add the same permissions to the key policy of the replica key. For the full set of permissions, see [(Optional) Create AWS KMS keys to encrypt the domain and the content](ai-agent-initial-setup.md#enable-awsmanagedkey-ai-agents).

**Note**  
Connect Customer agent assist sets an encryption context on the grants that it creates, which includes `aws:wisdom:knowledgeBase:arn` for a knowledge base. If you use condition keys such as `kms:EncryptionContextKeys` to restrict your key policy, allow this context key.

Consider also allowing `kms:RetireGrant` so that grants can be retired when you delete a replicated knowledge base. For information about how to change a key policy, see [Changing a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html) in the *AWS Key Management Service Developer Guide*.