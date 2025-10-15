# GetBucketReplication

###### Note

This operation is not supported for directory buckets.

Returns the replication configuration of a bucket.

###### Note

 It can take a while to propagate the put or delete a replication configuration to all Amazon S3
 systems. Therefore, a get request soon after put or delete can return a wrong result. 

 For information about replication configuration, see [Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html") in the
 *Amazon S3 User Guide*.

This action requires permissions for the `s3:GetReplicationConfiguration` action. For
 more information about permissions, see [Using Bucket Policies and User
 Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html").

If you include the `Filter` element in a replication configuration, you must also include
 the `DeleteMarkerReplication` and `Priority` elements. The response also returns
 those elements.

For information about `GetBucketReplication` errors, see [List of replication-related
 error codes](ErrorResponses.md#ReplicationErrorCodeList "ErrorResponses.md#ReplicationErrorCodeList")


The following operations are related to `GetBucketReplication`:


* [PutBucketReplication](API_PutBucketReplication.md "API_PutBucketReplication.md")
* [DeleteBucketReplication](API_DeleteBucketReplication.md "API_DeleteBucketReplication.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?replication HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketReplication_RequestSyntax "#API_GetBucketReplication_RequestSyntax")**


The bucket name for which to get the replication information.


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketReplication_RequestSyntax "#API_GetBucketReplication_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[ReplicationConfiguration](#AmazonS3-GetBucketReplication-response-ReplicationConfiguration "#AmazonS3-GetBucketReplication-response-ReplicationConfiguration")>
   <[Role](#AmazonS3-GetBucketReplication-response-Role "#AmazonS3-GetBucketReplication-response-Role")>***string***</[Role](#AmazonS3-GetBucketReplication-response-Role "#AmazonS3-GetBucketReplication-response-Role")>
   <[Rule](#AmazonS3-GetBucketReplication-response-Rules "#AmazonS3-GetBucketReplication-response-Rules")>
      <[DeleteMarkerReplication](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-DeleteMarkerReplication "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-DeleteMarkerReplication")>
         <[Status](API_DeleteMarkerReplication.md#AmazonS3-Type-DeleteMarkerReplication-Status "API_DeleteMarkerReplication.md#AmazonS3-Type-DeleteMarkerReplication-Status")>***string***</[Status](API_DeleteMarkerReplication.md#AmazonS3-Type-DeleteMarkerReplication-Status "API_DeleteMarkerReplication.md#AmazonS3-Type-DeleteMarkerReplication-Status")>
      </[DeleteMarkerReplication](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-DeleteMarkerReplication "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-DeleteMarkerReplication")>
      <[Destination](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Destination "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Destination")>
         <[AccessControlTranslation](API_Destination.md#AmazonS3-Type-Destination-AccessControlTranslation "API_Destination.md#AmazonS3-Type-Destination-AccessControlTranslation")>
            <[Owner](API_AccessControlTranslation.md#AmazonS3-Type-AccessControlTranslation-Owner "API_AccessControlTranslation.md#AmazonS3-Type-AccessControlTranslation-Owner")>***string***</[Owner](API_AccessControlTranslation.md#AmazonS3-Type-AccessControlTranslation-Owner "API_AccessControlTranslation.md#AmazonS3-Type-AccessControlTranslation-Owner")>
         </[AccessControlTranslation](API_Destination.md#AmazonS3-Type-Destination-AccessControlTranslation "API_Destination.md#AmazonS3-Type-Destination-AccessControlTranslation")>
         <[Account](API_Destination.md#AmazonS3-Type-Destination-Account "API_Destination.md#AmazonS3-Type-Destination-Account")>***string***</[Account](API_Destination.md#AmazonS3-Type-Destination-Account "API_Destination.md#AmazonS3-Type-Destination-Account")>
         <[Bucket](API_Destination.md#AmazonS3-Type-Destination-Bucket "API_Destination.md#AmazonS3-Type-Destination-Bucket")>***string***</[Bucket](API_Destination.md#AmazonS3-Type-Destination-Bucket "API_Destination.md#AmazonS3-Type-Destination-Bucket")>
         <[EncryptionConfiguration](API_Destination.md#AmazonS3-Type-Destination-EncryptionConfiguration "API_Destination.md#AmazonS3-Type-Destination-EncryptionConfiguration")>
            <[ReplicaKmsKeyID](API_EncryptionConfiguration.md#AmazonS3-Type-EncryptionConfiguration-ReplicaKmsKeyID "API_EncryptionConfiguration.md#AmazonS3-Type-EncryptionConfiguration-ReplicaKmsKeyID")>***string***</[ReplicaKmsKeyID](API_EncryptionConfiguration.md#AmazonS3-Type-EncryptionConfiguration-ReplicaKmsKeyID "API_EncryptionConfiguration.md#AmazonS3-Type-EncryptionConfiguration-ReplicaKmsKeyID")>
         </[EncryptionConfiguration](API_Destination.md#AmazonS3-Type-Destination-EncryptionConfiguration "API_Destination.md#AmazonS3-Type-Destination-EncryptionConfiguration")>
         <[Metrics](API_Destination.md#AmazonS3-Type-Destination-Metrics "API_Destination.md#AmazonS3-Type-Destination-Metrics")>
            <[EventThreshold](API_Metrics.md#AmazonS3-Type-Metrics-EventThreshold "API_Metrics.md#AmazonS3-Type-Metrics-EventThreshold")>
               <[Minutes](API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes "API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes")>***integer***</[Minutes](API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes "API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes")>
            </[EventThreshold](API_Metrics.md#AmazonS3-Type-Metrics-EventThreshold "API_Metrics.md#AmazonS3-Type-Metrics-EventThreshold")>
            <[Status](API_Metrics.md#AmazonS3-Type-Metrics-Status "API_Metrics.md#AmazonS3-Type-Metrics-Status")>***string***</[Status](API_Metrics.md#AmazonS3-Type-Metrics-Status "API_Metrics.md#AmazonS3-Type-Metrics-Status")>
         </[Metrics](API_Destination.md#AmazonS3-Type-Destination-Metrics "API_Destination.md#AmazonS3-Type-Destination-Metrics")>
         <[ReplicationTime](API_Destination.md#AmazonS3-Type-Destination-ReplicationTime "API_Destination.md#AmazonS3-Type-Destination-ReplicationTime")>
            <[Status](API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Status "API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Status")>***string***</[Status](API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Status "API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Status")>
            <[Time](API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Time "API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Time")>
               <[Minutes](API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes "API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes")>***integer***</[Minutes](API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes "API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes")>
            </[Time](API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Time "API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Time")>
         </[ReplicationTime](API_Destination.md#AmazonS3-Type-Destination-ReplicationTime "API_Destination.md#AmazonS3-Type-Destination-ReplicationTime")>
         <[StorageClass](API_Destination.md#AmazonS3-Type-Destination-StorageClass "API_Destination.md#AmazonS3-Type-Destination-StorageClass")>***string***</[StorageClass](API_Destination.md#AmazonS3-Type-Destination-StorageClass "API_Destination.md#AmazonS3-Type-Destination-StorageClass")>
      </[Destination](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Destination "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Destination")>
      <[ExistingObjectReplication](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ExistingObjectReplication "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ExistingObjectReplication")>
         <[Status](API_ExistingObjectReplication.md#AmazonS3-Type-ExistingObjectReplication-Status "API_ExistingObjectReplication.md#AmazonS3-Type-ExistingObjectReplication-Status")>***string***</[Status](API_ExistingObjectReplication.md#AmazonS3-Type-ExistingObjectReplication-Status "API_ExistingObjectReplication.md#AmazonS3-Type-ExistingObjectReplication-Status")>
      </[ExistingObjectReplication](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ExistingObjectReplication "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ExistingObjectReplication")>
      <[Filter](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Filter "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Filter")>
         <[And](API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-And "API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-And")>
            <[Prefix](API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Prefix "API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Prefix")>***string***</[Prefix](API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Prefix "API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Prefix")>
            <[Tag](API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Tags "API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Tags")>
               <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>***string***</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
               <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>***string***</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
            </[Tag](API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Tags "API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Tags")>
            ...
         </[And](API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-And "API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-And")>
         <[Prefix](API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Prefix "API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Prefix")>***string***</[Prefix](API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Prefix "API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Prefix")>
         <[Tag](API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Tag "API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Tag")>
            <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>***string***</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
            <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>***string***</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
         </[Tag](API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Tag "API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Tag")>
      </[Filter](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Filter "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Filter")>
      <[ID](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ID "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ID")>***string***</[ID](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ID "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ID")>
      <[Prefix](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Prefix "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Prefix")>***string***</[Prefix](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Prefix "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Prefix")>
      <[Priority](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Priority "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Priority")>***integer***</[Priority](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Priority "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Priority")>
      <[SourceSelectionCriteria](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-SourceSelectionCriteria "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-SourceSelectionCriteria")>
         <[ReplicaModifications](API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-ReplicaModifications "API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-ReplicaModifications")>
            <[Status](API_ReplicaModifications.md#AmazonS3-Type-ReplicaModifications-Status "API_ReplicaModifications.md#AmazonS3-Type-ReplicaModifications-Status")>***string***</[Status](API_ReplicaModifications.md#AmazonS3-Type-ReplicaModifications-Status "API_ReplicaModifications.md#AmazonS3-Type-ReplicaModifications-Status")>
         </[ReplicaModifications](API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-ReplicaModifications "API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-ReplicaModifications")>
         <[SseKmsEncryptedObjects](API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-SseKmsEncryptedObjects "API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-SseKmsEncryptedObjects")>
            <[Status](API_SseKmsEncryptedObjects.md#AmazonS3-Type-SseKmsEncryptedObjects-Status "API_SseKmsEncryptedObjects.md#AmazonS3-Type-SseKmsEncryptedObjects-Status")>***string***</[Status](API_SseKmsEncryptedObjects.md#AmazonS3-Type-SseKmsEncryptedObjects-Status "API_SseKmsEncryptedObjects.md#AmazonS3-Type-SseKmsEncryptedObjects-Status")>
         </[SseKmsEncryptedObjects](API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-SseKmsEncryptedObjects "API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-SseKmsEncryptedObjects")>
      </[SourceSelectionCriteria](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-SourceSelectionCriteria "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-SourceSelectionCriteria")>
      <[Status](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Status "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Status")>***string***</[Status](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Status "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Status")>
   </[Rule](#AmazonS3-GetBucketReplication-response-Rules "#AmazonS3-GetBucketReplication-response-Rules")>
   ...
</[ReplicationConfiguration](#AmazonS3-GetBucketReplication-response-ReplicationConfiguration "#AmazonS3-GetBucketReplication-response-ReplicationConfiguration")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ReplicationConfiguration](#API_GetBucketReplication_ResponseSyntax "#API_GetBucketReplication_ResponseSyntax")**


Root level tag for the ReplicationConfiguration parameters.


Required: Yes




**[Role](#API_GetBucketReplication_ResponseSyntax "#API_GetBucketReplication_ResponseSyntax")**


The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that Amazon S3 assumes when replicating
 objects. For more information, see [How to Set Up Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html") in the
 *Amazon S3 User Guide*.


Type: String




**[Rule](#API_GetBucketReplication_ResponseSyntax "#API_GetBucketReplication_ResponseSyntax")**


A container for one or more replication rules. A replication configuration must have at least one
 rule and can contain a maximum of 1,000 rules. 


Type: Array of [ReplicationRule](API_ReplicationRule.md "API_ReplicationRule.md") data types




## Examples


### Sample Request: Retrieve replication configuration information


The following GET request retrieves information about the replication configuration set for the
 `amzn-s3-demo-bucket` bucket:



```

            GET /?replication HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Tue, 10 Feb 2015 00:17:21 GMT
            Authorization: authorization string
         
```

### Sample Response


The following response shows that replication is enabled on the bucket. The empty prefix
 indicates that Amazon S3 will replicate all objects that are created in the
 `amzn-s3-demo-bucket` bucket. The `Destination` element identifies the
 target bucket where Amazon S3 creates the object replicas, and the storage class (STANDARD\_IA) that Amazon S3
 uses when creating replicas.


 Amazon S3 assumes the specified IAM role to replicate objects on behalf of the bucket owner, which
 is the AWS account that created the bucket.



```

            HTTP/1.1 200 OK
            x-amz-id-2: ITnGT1y4RyTmXa3rPi4hklTXouTf0hccUjo0iCPjz6FnfIutBj3M7fPGlWO2SEWp
            x-amz-request-id: 51991C342example
            Date: Tue, 10 Feb 2015 00:17:23 GMT
            Server: AmazonS3
            Content-Length: contentlength

            <?xml version="1.0" encoding="UTF-8"?>
            <ReplicationConfiguration>
              <Role>arn:aws:iam::35667example:role/CrossRegionReplicationRoleForS3</Role>
             <Rule>
               <ID>rule1</ID>
               <Status>Enabled</Status>
               <Priority>1</Priority>
               <DeleteMarkerReplication>
                   <Status>Disabled</Status>
               </DeleteMarkerReplication>
               <Filter>
                  <And>
                       <Prefix>TaxDocs</Prefix>
                       <Tag>
                         <Key>key1</Key>
                         <Value>value1</Value>
                       </Tag>
                       <Tag>
                         <Key>key1</Key>
                        <Value>value1</Value>
                      </Tag>
                  </And>
                </Filter>
               <Destination>
                  <Bucket>arn:aws:s3:::exampletargetbucket</Bucket>
               </Destination>
              </Rule>
            </ReplicationConfiguration>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketReplication "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketReplication")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketReplication "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketReplication")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketReplication")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketReplication")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketReplication")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketReplication")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketReplication")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketReplication")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketReplication "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketReplication")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketReplication "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketReplication")
