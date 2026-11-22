

# Data protection in Amazon OpenSearch Memory

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Amazon OpenSearch Memory. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/). For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/).

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For more information, see [Monitoring Amazon OpenSearch Memory with AWS CloudTrail](memory-cloudtrail.md).
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with OpenSearch Memory or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. For OpenSearch Memory, this applies to space names, strategy names and descriptions, actor and session IDs, and metadata keys and values. The content of events and memories is customer data and is protected as described in this topic.

**Topics**
+ [Encryption at rest](#memory-encryption-at-rest)
+ [Key management](#memory-key-management)
+ [Encryption in transit](#memory-encryption-in-transit)
+ [Data location](#memory-data-location)
+ [Deleting data](#memory-data-deletion)

## Encryption at rest
<a name="memory-encryption-at-rest"></a>

OpenSearch Memory encrypts the events and memories in every space at rest. By default, it uses an AWS owned key. AWS owned keys are not stored in your account. You can't view, manage, or audit their use, and there is no charge for them.

If you want to control the key, choose a customer managed key in AWS Key Management Service (AWS KMS) when you create the space. You own the key, set its policy, can audit its use in CloudTrail, and can revoke OpenSearch Memory's access to it. You pay AWS KMS charges for a customer managed key.

## Key management
<a name="memory-key-management"></a>

To use a customer managed key, specify its ARN in `encryptionConfiguration.kmsKeyArn` when you create the space. The key must be a symmetric encryption key that is enabled and in the same AWS Region as the space. You can't change a space's key after you create it.

**Topics**
+ [Permissions required for a customer managed key](#memory-encryption-permissions)
+ [How OpenSearch Memory uses grants](#memory-encryption-grants)
+ [If the key becomes unavailable](#memory-encryption-key-unavailable)

### Permissions required for a customer managed key
<a name="memory-encryption-permissions"></a>

OpenSearch Memory uses your key with the permissions of the principal that makes the request. A principal that calls an OpenSearch Memory operation on a space with a customer managed key therefore needs permission to use the key, in addition to permission for the OpenSearch Memory action. The following table lists the AWS KMS actions that each operation requires.


| Operation | AWS KMS actions | 
| --- | --- | 
| [CreateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateSpace.html) | kms:CreateGrant | 
| [CreateEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateEvent.html), [CreateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemory.html) | kms:Decrypt, kms:GenerateDataKey, kms:GenerateDataKeyWithoutPlaintext, kms:ReEncryptFrom, kms:ReEncryptTo | 
| [UpdateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateMemory.html) | kms:Decrypt, kms:GenerateDataKey | 
| [GetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetEvent.html), [BatchGetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BatchGetEvent.html), [ListEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListEvents.html), [SearchEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html), [DeleteEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteEvent.html), [GetMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetMemory.html), [ListMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html), [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html), [DeleteMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteMemory.html) | kms:Decrypt | 

You can grant these permissions in the key policy, in an IAM policy, or both. The following example key policy statement lets one role use the key for all OpenSearch Memory operations, and only through OpenSearch Memory.

```json
{
    "Sid": "Allow use of the key through OpenSearch Memory",
    "Effect": "Allow",
    "Principal": { "AWS": "arn:aws:iam::111122223333:role/my-memory-app-role" },
    "Action": [
        "kms:CreateGrant",
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:ReEncryptFrom",
        "kms:ReEncryptTo"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": { "kms:ViaService": "osm.us-east-1.amazonaws.com" }
    }
}
```

Replace `111122223333` with your account ID, `my-memory-app-role` with the role that calls OpenSearch Memory, and `us-east-1` with the Region of the space. The `kms:ViaService` condition means the role can use the key only from OpenSearch Memory, not directly.

If a principal can access a space but can't use its key, the principal's requests fail with `AccessDeniedException`.

### How OpenSearch Memory uses grants
<a name="memory-encryption-grants"></a>

Extraction, consolidation, and retention run after your request returns, so OpenSearch Memory needs to use your key when no request from you is in progress. When you create a space with a customer managed key, OpenSearch Memory creates [grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) on the key with your permissions. The grants allow OpenSearch Memory to encrypt and decrypt the space's data for this background work. You can see the grants with the AWS KMS [ListGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListGrants.html) operation. OpenSearch Memory retires them when you delete the space.

You can limit the grants that OpenSearch Memory can create with the `kms:GrantIsForAWSResource` and `kms:GrantOperations` condition keys on the `kms:CreateGrant` permission.

### If the key becomes unavailable
<a name="memory-encryption-key-unavailable"></a>

If you disable the key, schedule it for deletion, revoke the grants, or remove a principal's access to it, OpenSearch Memory can no longer read or write the space's data:
+ Requests from a principal that can't use the key fail with `AccessDeniedException`.
+ Requests on a space whose key is disabled, pending deletion, or deleted fail with `ValidationException`.
+ Extraction and consolidation for the space stop until the key is available again.

Re-enable the key or cancel its deletion to restore access. If AWS KMS throttles OpenSearch Memory's use of the key, requests fail with `ThrottlingException`; retry with backoff or request a higher AWS KMS quota.

## Encryption in transit
<a name="memory-encryption-in-transit"></a>

All requests to OpenSearch Memory use Transport Layer Security (TLS). OpenSearch Memory requires TLS 1.2 and supports TLS 1.3.

## Data location
<a name="memory-data-location"></a>

Your spaces, and the events and memories stored in them, stay in the AWS Region where you created the space.

To extract memories, OpenSearch Memory calls a foundation model. Model calls may be processed in another AWS Region within the same geography as your space, for example within the United States for a space in US East (N. Virginia). The data sent to the model is used only to produce the memories and is not stored outside the space's Region. For the Regions in each geography, see [Geographic cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html) in the *Amazon Bedrock User Guide*.

## Deleting data
<a name="memory-data-deletion"></a>

The following operations delete data from a space:
+ [DeleteEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteEvent.html) – Deletes the event. It doesn't delete memories already extracted from the event. To delete those, use `DeleteMemory`.
+ [DeleteMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteMemory.html) – Permanently deletes the memory. You can't restore a deleted memory.
+ [DeleteSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteSpace.html) – Deletes the space and all of its memories. The space's events are removed when they reach the end of their retention period.

Expired events and memories are removed automatically according to the space's retention settings. For more information, see [Configuring retention](memory-spaces.md#memory-spaces-retention).

A deleted event or memory can appear in search results for a short time after the delete call returns.