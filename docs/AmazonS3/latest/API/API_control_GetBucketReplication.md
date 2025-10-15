# GetBucketReplication

###### Note

This operation gets an Amazon S3 on Outposts bucket's replication configuration. To get an
 S3 bucket's replication configuration, see [GetBucketReplication](API_GetBucketReplication.md "API_GetBucketReplication.md")
 in the *Amazon S3 API Reference*. 

Returns the replication configuration of an S3 on Outposts bucket. For more information
 about S3 on Outposts, see [Using Amazon S3 on Outposts](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the
 *Amazon S3 User Guide*. For information about S3 replication on Outposts
 configuration, see [Replicating objects for
 S3 on Outposts](../userguide/S3OutpostsReplication.md "../userguide/S3OutpostsReplication.md") in the *Amazon S3 User Guide*.

###### Note

It can take a while to propagate `PUT` or `DELETE` requests for
 a replication configuration to all S3 on Outposts systems. Therefore, the replication
 configuration that's returned by a `GET` request soon after a
 `PUT` or `DELETE` request might return a more recent result
 than what's on the Outpost. If an Outpost is offline, the delay in updating the
 replication configuration on that Outpost can be significant.

This action requires permissions for the
 `s3-outposts:GetReplicationConfiguration` action. The Outposts bucket owner
 has this permission by default and can grant it to others. For more information about
 permissions, see [Setting up IAM with
 S3 on Outposts](../userguide/S3OutpostsIAM.md "../userguide/S3OutpostsIAM.md") and [Managing access to
 S3 on Outposts bucket](../userguide/S3OutpostsBucketPolicy.md "../userguide/S3OutpostsBucketPolicy.md") in the *Amazon S3 User Guide*.

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_GetBucketReplication.md#API_control_GetBucketReplication_Examples "API_control_GetBucketReplication.md#API_control_GetBucketReplication_Examples") section.

If you include the `Filter` element in a replication configuration, you must
 also include the `DeleteMarkerReplication`, `Status`, and
 `Priority` elements. The response also returns those elements.

For information about S3 on Outposts replication failure reasons, see [Replication failure reasons](../userguide/outposts-replication-eventbridge.md#outposts-replication-failure-codes "../userguide/outposts-replication-eventbridge.md#outposts-replication-failure-codes") in the *Amazon S3 User Guide*.

The following operations are related to `GetBucketReplication`:


* [PutBucketReplication](API_control_PutBucketReplication.md "API_control_PutBucketReplication.md")
* [DeleteBucketReplication](API_control_DeleteBucketReplication.md "API_control_DeleteBucketReplication.md")

## Request Syntax



```
GET /v20180820/bucket/`name`/replication HTTP/1.1
Host: `Bucket`.s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetBucketReplication_RequestSyntax "#API_control_GetBucketReplication_RequestSyntax")**


Specifies the bucket to get the replication information for.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded. 


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_GetBucketReplication_RequestSyntax "#API_control_GetBucketReplication_RequestSyntax")**


The AWS account ID of the Outposts bucket.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetBucketReplicationResult](#AmazonS3-control_GetBucketReplication-response-GetBucketReplicationResult "#AmazonS3-control_GetBucketReplication-response-GetBucketReplicationResult")>
   <[ReplicationConfiguration](#AmazonS3-control_GetBucketReplication-response-ReplicationConfiguration "#AmazonS3-control_GetBucketReplication-response-ReplicationConfiguration")>
      <[Role](API_control_ReplicationConfiguration.md#AmazonS3-Type-control_ReplicationConfiguration-Role "API_control_ReplicationConfiguration.md#AmazonS3-Type-control_ReplicationConfiguration-Role")>***string***</[Role](API_control_ReplicationConfiguration.md#AmazonS3-Type-control_ReplicationConfiguration-Role "API_control_ReplicationConfiguration.md#AmazonS3-Type-control_ReplicationConfiguration-Role")>
      <[Rules](API_control_ReplicationConfiguration.md#AmazonS3-Type-control_ReplicationConfiguration-Rules "API_control_ReplicationConfiguration.md#AmazonS3-Type-control_ReplicationConfiguration-Rules")>
         <Rule>
            <[Bucket](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Bucket "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Bucket")>***string***</[Bucket](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Bucket "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Bucket")>
            <[DeleteMarkerReplication](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-DeleteMarkerReplication "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-DeleteMarkerReplication")>
               <[Status](API_control_DeleteMarkerReplication.md#AmazonS3-Type-control_DeleteMarkerReplication-Status "API_control_DeleteMarkerReplication.md#AmazonS3-Type-control_DeleteMarkerReplication-Status")>***string***</[Status](API_control_DeleteMarkerReplication.md#AmazonS3-Type-control_DeleteMarkerReplication-Status "API_control_DeleteMarkerReplication.md#AmazonS3-Type-control_DeleteMarkerReplication-Status")>
            </[DeleteMarkerReplication](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-DeleteMarkerReplication "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-DeleteMarkerReplication")>
            <[Destination](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Destination "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Destination")>
               <[AccessControlTranslation](API_control_Destination.md#AmazonS3-Type-control_Destination-AccessControlTranslation "API_control_Destination.md#AmazonS3-Type-control_Destination-AccessControlTranslation")>
                  <[Owner](API_control_AccessControlTranslation.md#AmazonS3-Type-control_AccessControlTranslation-Owner "API_control_AccessControlTranslation.md#AmazonS3-Type-control_AccessControlTranslation-Owner")>***string***</[Owner](API_control_AccessControlTranslation.md#AmazonS3-Type-control_AccessControlTranslation-Owner "API_control_AccessControlTranslation.md#AmazonS3-Type-control_AccessControlTranslation-Owner")>
               </[AccessControlTranslation](API_control_Destination.md#AmazonS3-Type-control_Destination-AccessControlTranslation "API_control_Destination.md#AmazonS3-Type-control_Destination-AccessControlTranslation")>
               <[Account](API_control_Destination.md#AmazonS3-Type-control_Destination-Account "API_control_Destination.md#AmazonS3-Type-control_Destination-Account")>***string***</[Account](API_control_Destination.md#AmazonS3-Type-control_Destination-Account "API_control_Destination.md#AmazonS3-Type-control_Destination-Account")>
               <[Bucket](API_control_Destination.md#AmazonS3-Type-control_Destination-Bucket "API_control_Destination.md#AmazonS3-Type-control_Destination-Bucket")>***string***</[Bucket](API_control_Destination.md#AmazonS3-Type-control_Destination-Bucket "API_control_Destination.md#AmazonS3-Type-control_Destination-Bucket")>
               <[EncryptionConfiguration](API_control_Destination.md#AmazonS3-Type-control_Destination-EncryptionConfiguration "API_control_Destination.md#AmazonS3-Type-control_Destination-EncryptionConfiguration")>
                  <[ReplicaKmsKeyID](API_control_EncryptionConfiguration.md#AmazonS3-Type-control_EncryptionConfiguration-ReplicaKmsKeyID "API_control_EncryptionConfiguration.md#AmazonS3-Type-control_EncryptionConfiguration-ReplicaKmsKeyID")>***string***</[ReplicaKmsKeyID](API_control_EncryptionConfiguration.md#AmazonS3-Type-control_EncryptionConfiguration-ReplicaKmsKeyID "API_control_EncryptionConfiguration.md#AmazonS3-Type-control_EncryptionConfiguration-ReplicaKmsKeyID")>
               </[EncryptionConfiguration](API_control_Destination.md#AmazonS3-Type-control_Destination-EncryptionConfiguration "API_control_Destination.md#AmazonS3-Type-control_Destination-EncryptionConfiguration")>
               <[Metrics](API_control_Destination.md#AmazonS3-Type-control_Destination-Metrics "API_control_Destination.md#AmazonS3-Type-control_Destination-Metrics")>
                  <[EventThreshold](API_control_Metrics.md#AmazonS3-Type-control_Metrics-EventThreshold "API_control_Metrics.md#AmazonS3-Type-control_Metrics-EventThreshold")>
                     <[Minutes](API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes "API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes")>***integer***</[Minutes](API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes "API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes")>
                  </[EventThreshold](API_control_Metrics.md#AmazonS3-Type-control_Metrics-EventThreshold "API_control_Metrics.md#AmazonS3-Type-control_Metrics-EventThreshold")>
                  <[Status](API_control_Metrics.md#AmazonS3-Type-control_Metrics-Status "API_control_Metrics.md#AmazonS3-Type-control_Metrics-Status")>***string***</[Status](API_control_Metrics.md#AmazonS3-Type-control_Metrics-Status "API_control_Metrics.md#AmazonS3-Type-control_Metrics-Status")>
               </[Metrics](API_control_Destination.md#AmazonS3-Type-control_Destination-Metrics "API_control_Destination.md#AmazonS3-Type-control_Destination-Metrics")>
               <[ReplicationTime](API_control_Destination.md#AmazonS3-Type-control_Destination-ReplicationTime "API_control_Destination.md#AmazonS3-Type-control_Destination-ReplicationTime")>
                  <[Status](API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Status "API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Status")>***string***</[Status](API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Status "API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Status")>
                  <[Time](API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Time "API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Time")>
                     <[Minutes](API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes "API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes")>***integer***</[Minutes](API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes "API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes")>
                  </[Time](API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Time "API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Time")>
               </[ReplicationTime](API_control_Destination.md#AmazonS3-Type-control_Destination-ReplicationTime "API_control_Destination.md#AmazonS3-Type-control_Destination-ReplicationTime")>
               <[StorageClass](API_control_Destination.md#AmazonS3-Type-control_Destination-StorageClass "API_control_Destination.md#AmazonS3-Type-control_Destination-StorageClass")>***string***</[StorageClass](API_control_Destination.md#AmazonS3-Type-control_Destination-StorageClass "API_control_Destination.md#AmazonS3-Type-control_Destination-StorageClass")>
            </[Destination](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Destination "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Destination")>
            <[ExistingObjectReplication](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ExistingObjectReplication "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ExistingObjectReplication")>
               <[Status](API_control_ExistingObjectReplication.md#AmazonS3-Type-control_ExistingObjectReplication-Status "API_control_ExistingObjectReplication.md#AmazonS3-Type-control_ExistingObjectReplication-Status")>***string***</[Status](API_control_ExistingObjectReplication.md#AmazonS3-Type-control_ExistingObjectReplication-Status "API_control_ExistingObjectReplication.md#AmazonS3-Type-control_ExistingObjectReplication-Status")>
            </[ExistingObjectReplication](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ExistingObjectReplication "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ExistingObjectReplication")>
            <[Filter](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Filter "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Filter")>
               <[And](API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-And "API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-And")>
                  <[Prefix](API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Prefix "API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Prefix")>***string***</[Prefix](API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Prefix "API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Prefix")>
                  <[Tags](API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Tags "API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Tags")>
                     <S3Tag>
                        <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>***string***</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
                        <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>***string***</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
                     </S3Tag>
                  </[Tags](API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Tags "API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Tags")>
               </[And](API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-And "API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-And")>
               <[Prefix](API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Prefix "API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Prefix")>***string***</[Prefix](API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Prefix "API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Prefix")>
               <[Tag](API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Tag "API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Tag")>
                  <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>***string***</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
                  <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>***string***</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
               </[Tag](API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Tag "API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Tag")>
            </[Filter](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Filter "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Filter")>
            <[ID](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ID "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ID")>***string***</[ID](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ID "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ID")>
            <[Prefix](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Prefix "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Prefix")>***string***</[Prefix](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Prefix "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Prefix")>
            <[Priority](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Priority "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Priority")>***integer***</[Priority](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Priority "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Priority")>
            <[SourceSelectionCriteria](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-SourceSelectionCriteria "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-SourceSelectionCriteria")>
               <[ReplicaModifications](API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-ReplicaModifications "API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-ReplicaModifications")>
                  <[Status](API_control_ReplicaModifications.md#AmazonS3-Type-control_ReplicaModifications-Status "API_control_ReplicaModifications.md#AmazonS3-Type-control_ReplicaModifications-Status")>***string***</[Status](API_control_ReplicaModifications.md#AmazonS3-Type-control_ReplicaModifications-Status "API_control_ReplicaModifications.md#AmazonS3-Type-control_ReplicaModifications-Status")>
               </[ReplicaModifications](API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-ReplicaModifications "API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-ReplicaModifications")>
               <[SseKmsEncryptedObjects](API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-SseKmsEncryptedObjects "API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-SseKmsEncryptedObjects")>
                  <[Status](API_control_SseKmsEncryptedObjects.md#AmazonS3-Type-control_SseKmsEncryptedObjects-Status "API_control_SseKmsEncryptedObjects.md#AmazonS3-Type-control_SseKmsEncryptedObjects-Status")>***string***</[Status](API_control_SseKmsEncryptedObjects.md#AmazonS3-Type-control_SseKmsEncryptedObjects-Status "API_control_SseKmsEncryptedObjects.md#AmazonS3-Type-control_SseKmsEncryptedObjects-Status")>
               </[SseKmsEncryptedObjects](API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-SseKmsEncryptedObjects "API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-SseKmsEncryptedObjects")>
            </[SourceSelectionCriteria](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-SourceSelectionCriteria "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-SourceSelectionCriteria")>
            <[Status](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Status "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Status")>***string***</[Status](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Status "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Status")>
         </Rule>
      </[Rules](API_control_ReplicationConfiguration.md#AmazonS3-Type-control_ReplicationConfiguration-Rules "API_control_ReplicationConfiguration.md#AmazonS3-Type-control_ReplicationConfiguration-Rules")>
   </[ReplicationConfiguration](#AmazonS3-control_GetBucketReplication-response-ReplicationConfiguration "#AmazonS3-control_GetBucketReplication-response-ReplicationConfiguration")>
</[GetBucketReplicationResult](#AmazonS3-control_GetBucketReplication-response-GetBucketReplicationResult "#AmazonS3-control_GetBucketReplication-response-GetBucketReplicationResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetBucketReplicationResult](#API_control_GetBucketReplication_ResponseSyntax "#API_control_GetBucketReplication_ResponseSyntax")**


Root level tag for the GetBucketReplicationResult parameters.


Required: Yes




**[ReplicationConfiguration](#API_control_GetBucketReplication_ResponseSyntax "#API_control_GetBucketReplication_ResponseSyntax")**


A container for one or more replication rules. A replication configuration must have at
 least one rule and you can add up to 100 rules. The maximum size of a replication
 configuration is 128 KB.


Type: [ReplicationConfiguration](API_control_ReplicationConfiguration.md "API_control_ReplicationConfiguration.md") data type




## Examples


### Sample request to get the replication configuration of an Amazon S3 on Outposts bucket


The following example shows how to get the replication configuration of an
 Outposts bucket.



```

GET /v20180820/bucket/example-outpost-bucket/replication HTTP/1.1
Host: s3-outposts.<Region>.amazonaws.com 
x-amz-account-id: example-account-id
x-amz-outpost-id: op-01ac5d28a6a232904
Authorization: signatureValue
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetBucketReplication "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetBucketReplication")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetBucketReplication "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetBucketReplication")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetBucketReplication")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetBucketReplication")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetBucketReplication")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetBucketReplication")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetBucketReplication")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetBucketReplication")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetBucketReplication "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetBucketReplication")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetBucketReplication")
