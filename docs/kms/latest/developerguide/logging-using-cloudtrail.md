

# Logging AWS KMS API calls with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS KMS is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/), a service that records all calls to AWS KMS by users, roles, and other AWS services. CloudTrail captures all API calls to AWS KMS as events, including calls from the AWS KMS console, AWS KMS APIs, CloudFormation templates, the AWS Command Line Interface (AWS CLI), and AWS Tools for PowerShell.

CloudTrail logs all AWS KMS operations, including read-only operations, such as [ListAliases](ct-listaliases.md) and [GetKeyRotationStatus](ct-getkeyrotationstatus.md), operations that manage KMS keys, such as [CreateKey](ct-createkey.md) and [PutKeyPolicy](ct-put-key-policy.md), and [cryptographic operations](kms-cryptography.md#cryptographic-operations), such as [GenerateDataKey](ct-generatedatakey.md) and [Decrypt](ct-decrypt.md). It also logs internal operations that AWS KMS calls for you, such as [DeleteExpiredKeyMaterial](ct-deleteexpiredkeymaterial.md), [DeleteKey](ct-delete-key.md), [SynchronizeMultiRegionKey](ct-synchronize-multi-region-key.md), and [RotateKey](ct-rotatekey.md).

CloudTrail logs all successful operations and, in some scenarios, attempted calls that failed, such as when the caller is denied access to a resource. [Cross-account operations on KMS keys](key-policy-modifying-external-accounts.md) are logged in both the caller account and the KMS key owner account. However, cross-account AWS KMS requests that are rejected because access is denied are logged only in the caller's account.

For security reasons, some fields are omitted from AWS KMS log entries, such as the `Plaintext` parameter of an [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) request, and the response to [GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyPolicy.html) or any cryptographic operation. To make it easier to search for CloudTrail log entries for particular KMS keys, AWS KMS adds the [key ARN](concepts.md#key-id-key-ARN) of the affected KMS key to the `responseElements` field in the log entries for some AWS KMS key management operations, even when the API operation doesn't return the key ARN.

Although by default, all AWS KMS actions are logged as CloudTrail events, you can exclude AWS KMS actions from a CloudTrail trail. For details, see [Excluding AWS KMS events from a trail](#filtering-kms-events).

**Learn more**: 
+ For CloudTrail log examples of AWS KMS operations for attested platforms, see [Monitoring attested requests](ct-attestation.md).

**Topics**
+ [Finding AWS KMS log entries in CloudTrail](#searching-kms-ct)
+ [Excluding AWS KMS events from a trail](#filtering-kms-events)
+ [Examples of AWS KMS log entries](understanding-kms-entries.md)

## Finding AWS KMS log entries in CloudTrail
<a name="searching-kms-ct"></a>

To search CloudTrail log entries, use the [CloudTrail console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html) or the [CloudTrail LookupEvents](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html) operation. CloudTrail supports numerous [attribute values](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html#filtering-cloudtrail-events) for filtering your search, including event name, user name, and event source. 

To help you search for AWS KMS log entries in CloudTrail, AWS KMS populates the following CloudTrail log entry fields.

**Note**  
Beginning in December 2022, AWS KMS populates the **Resource type** and **Resource name** attributes in all management operations that change a particular KMS key. These attribute values might be null in older CloudTrail entries for the following operations: [CreateAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateAlias.html), [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html), [DeleteAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteAlias.html), [DeleteImportedKeyMaterial](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteImportedKeyMaterial.html), [ImportKeyMaterial](https://docs.aws.amazon.com/kms/latest/APIReference/API_ImportKeyMaterial.html), [ReplicateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReplicateKey.html), [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html), [RevokeGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html), [UpdateAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateAlias.html), and [UpdatePrimaryRegion](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdatePrimaryRegion.html).


| Attribute | Value | Log entries | 
| --- | --- | --- | 
| Event source (EventSource) | kms.amazonaws.com | All operations. | 
| Resource type (ResourceType) | AWS::KMS::Key | Management operations that change a particular KMS key, such as CreateKey and EnableKey, but not ListKeys. | 
| Resource name (ResourceName) | Key ARN (or key ID and key ARN) | Management operations that change a particular KMS key, such as CreateKey and EnableKey, but not ListKeys. | 

To help you find log entries for management operations on particular KMS keys, AWS KMS records the key ARN of the affected KMS key in the `responseElements.keyId` element of the log entry, even when the AWS KMS API operation doesn't return the key ARN.

For example, a successful call to the [DisableKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html) operation doesn't return any values in the response, but instead of a null value, the `responseElements.keyId` value in the [DisableKey log entry](ct-disablekey.md) includes the key ARN of the disabled KMS key.

This feature was added in December 2022 and affects the following CloudTrail log entries: [CreateAlias](ct-createalias.md), [CreateGrant](ct-creategrant.md), [DeleteAlias](ct-deletealias.md), [DeleteKey](ct-delete-key.md), [DisableKey](ct-disablekey.md), [EnableKey](ct-enablekey.md), [EnableKeyRotation](ct-enablekeyrotation.md), [ImportKeyMaterial](ct-importkeymaterial.md), [RotateKey](ct-rotatekey.md), [SynchronizeMultiRegionKey](ct-synchronize-multi-region-key.md), [TagResource](ct-tagresource.md), [UntagResource](ct-untagresource.md), [UpdateAlias](ct-updatealias.md), and [UpdatePrimaryRegion](ct-update-primary-region.md).

## Excluding AWS KMS events from a trail
<a name="filtering-kms-events"></a>

To provide a record of the use and management of their AWS KMS resources, most AWS KMS users rely on the events in a CloudTrail trail. The trail can be an valuable source of data for auditing critical events, such as creating, disabling, and deleting AWS KMS keys, changing key policy, and the use of your KMS keys by AWS services on your behalf. In some cases, the metadata in a CloudTrail log entry, such as the [encryption context](encrypt_context.md) in an encryption operation, can help you to avoid or resolve errors.

However, because AWS KMS can generate a large number of events, AWS CloudTrail lets you exclude AWS KMS events from a trail. This per-trail setting excludes all AWS KMS events; you cannot exclude particular AWS KMS events.

**Warning**  
Excluding AWS KMS events from a CloudTrail Log can obscure actions that use your KMS keys. Be cautious when giving principals the `cloudtrail:PutEventSelectors` permission that is required to perform this operation.

To exclude AWS KMS events from a trail: 
+ In the CloudTrail console, use the **Log Key Management Service events** setting when you [create a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) or [update a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-update-a-trail-console.html). For instructions, see [Logging Management Events with the AWS Management Console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html) in the AWS CloudTrail User Guide.
+ In the CloudTrail API, use the [PutEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PutEventSelectors.html) operation. Add the `ExcludeManagementEventSources` attribute to your event selectors with a value of `kms.amazonaws.com`. For an example, see [Example: A trail that does not log AWS Key Management Service events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-additional-cli-commands.html#configuring-event-selector-example-kms) in the AWS CloudTrail User Guide.

You can disable this exclusion at any time by changing the console setting or the event selectors for a trail. The trail will then start recording AWS KMS events. However, it cannot recover AWS KMS events that occurred while the exclusion was effective.

When you exclude AWS KMS events by using the console or API, the resulting CloudTrail `PutEventSelectors` API operation is also logged in your CloudTrail Logs. If AWS KMS events don't appear in your CloudTrail Logs, look for a `PutEventSelectors` event with the `ExcludeManagementEventSources` attribute set to `kms.amazonaws.com`.