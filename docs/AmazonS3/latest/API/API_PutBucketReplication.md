# PutBucketReplication

###### Note

This operation is not supported for directory buckets.

 Creates a replication configuration or replaces an existing one. For more information, see [Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html") in the
 *Amazon S3 User Guide*. 

Specify the replication configuration in the request body. In the replication configuration, you
 provide the name of the destination bucket or buckets where you want Amazon S3 to replicate objects, the
 IAM role that Amazon S3 can assume to replicate objects on your behalf, and other relevant information. You
 can invoke this request for a specific AWS Region by using the [`aws:RequestedRegion`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requestedregion "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requestedregion") condition key.

A replication configuration must include at least one rule, and can contain a maximum of 1,000. Each
 rule identifies a subset of objects to replicate by filtering the objects in the source bucket. To
 choose additional subsets of objects to replicate, add a rule for each subset.

To specify a subset of the objects in the source bucket to apply a replication rule to, add the
 Filter element as a child of the Rule element. You can filter objects based on an object key prefix, one
 or more object tags, or both. When you add the Filter element in the configuration, you must also add
 the following elements: `DeleteMarkerReplication`, `Status`, and
 `Priority`.

###### Note

If you are using an earlier version of the replication configuration, Amazon S3 handles replication of
 delete markers differently. For more information, see [Backward Compatibility](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-backward-compat-considerations "https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-backward-compat-considerations").

For information about enabling versioning on a bucket, see [Using Versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html").



Handling Replication of Encrypted Objects

By default, Amazon S3 doesn't replicate objects that are stored at rest using server-side
 encryption with KMS keys. To replicate AWS KMS-encrypted objects, add the following:
 `SourceSelectionCriteria`, `SseKmsEncryptedObjects`, `Status`,
 `EncryptionConfiguration`, and `ReplicaKmsKeyID`. For information about
 replication configuration, see [Replicating Objects Created
 with SSE Using KMS keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-config-for-kms-objects.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-config-for-kms-objects.html").


For information on `PutBucketReplication` errors, see [List of
 replication-related error codes](ErrorResponses.md#ReplicationErrorCodeList "ErrorResponses.md#ReplicationErrorCodeList")




Permissions

To create a `PutBucketReplication` request, you must have
 `s3:PutReplicationConfiguration` permissions for the bucket.
 
 


By default, a resource owner, in this case the AWS account that created the bucket, can
 perform this operation. The resource owner can also grant others permissions to perform the
 operation. For more information about permissions, see [Specifying Permissions in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html")
 and [Managing
 Access Permissions to Your Amazon S3 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").


###### Note

To perform this operation, the user or role performing the action must have the [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html") permission.



The following operations are related to `PutBucketReplication`:


* [GetBucketReplication](API_GetBucketReplication.md "API_GetBucketReplication.md")
* [DeleteBucketReplication](API_DeleteBucketReplication.md "API_DeleteBucketReplication.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?replication HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-bucket-object-lock-token: `Token`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[ReplicationConfiguration](#AmazonS3-PutBucketReplication-request-ReplicationConfiguration "#AmazonS3-PutBucketReplication-request-ReplicationConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[Role](#AmazonS3-PutBucketReplication-request-Role "#AmazonS3-PutBucketReplication-request-Role")>`string`</[Role](#AmazonS3-PutBucketReplication-request-Role "#AmazonS3-PutBucketReplication-request-Role")>
   <[Rule](#AmazonS3-PutBucketReplication-request-Rules "#AmazonS3-PutBucketReplication-request-Rules")>
      <[DeleteMarkerReplication](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-DeleteMarkerReplication "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-DeleteMarkerReplication")>
         <[Status](API_DeleteMarkerReplication.md#AmazonS3-Type-DeleteMarkerReplication-Status "API_DeleteMarkerReplication.md#AmazonS3-Type-DeleteMarkerReplication-Status")>`string`</[Status](API_DeleteMarkerReplication.md#AmazonS3-Type-DeleteMarkerReplication-Status "API_DeleteMarkerReplication.md#AmazonS3-Type-DeleteMarkerReplication-Status")>
      </[DeleteMarkerReplication](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-DeleteMarkerReplication "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-DeleteMarkerReplication")>
      <[Destination](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Destination "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Destination")>
         <[AccessControlTranslation](API_Destination.md#AmazonS3-Type-Destination-AccessControlTranslation "API_Destination.md#AmazonS3-Type-Destination-AccessControlTranslation")>
            <[Owner](API_AccessControlTranslation.md#AmazonS3-Type-AccessControlTranslation-Owner "API_AccessControlTranslation.md#AmazonS3-Type-AccessControlTranslation-Owner")>`string`</[Owner](API_AccessControlTranslation.md#AmazonS3-Type-AccessControlTranslation-Owner "API_AccessControlTranslation.md#AmazonS3-Type-AccessControlTranslation-Owner")>
         </[AccessControlTranslation](API_Destination.md#AmazonS3-Type-Destination-AccessControlTranslation "API_Destination.md#AmazonS3-Type-Destination-AccessControlTranslation")>
         <[Account](API_Destination.md#AmazonS3-Type-Destination-Account "API_Destination.md#AmazonS3-Type-Destination-Account")>`string`</[Account](API_Destination.md#AmazonS3-Type-Destination-Account "API_Destination.md#AmazonS3-Type-Destination-Account")>
         <[Bucket](API_Destination.md#AmazonS3-Type-Destination-Bucket "API_Destination.md#AmazonS3-Type-Destination-Bucket")>`string`</[Bucket](API_Destination.md#AmazonS3-Type-Destination-Bucket "API_Destination.md#AmazonS3-Type-Destination-Bucket")>
         <[EncryptionConfiguration](API_Destination.md#AmazonS3-Type-Destination-EncryptionConfiguration "API_Destination.md#AmazonS3-Type-Destination-EncryptionConfiguration")>
            <[ReplicaKmsKeyID](API_EncryptionConfiguration.md#AmazonS3-Type-EncryptionConfiguration-ReplicaKmsKeyID "API_EncryptionConfiguration.md#AmazonS3-Type-EncryptionConfiguration-ReplicaKmsKeyID")>`string`</[ReplicaKmsKeyID](API_EncryptionConfiguration.md#AmazonS3-Type-EncryptionConfiguration-ReplicaKmsKeyID "API_EncryptionConfiguration.md#AmazonS3-Type-EncryptionConfiguration-ReplicaKmsKeyID")>
         </[EncryptionConfiguration](API_Destination.md#AmazonS3-Type-Destination-EncryptionConfiguration "API_Destination.md#AmazonS3-Type-Destination-EncryptionConfiguration")>
         <[Metrics](API_Destination.md#AmazonS3-Type-Destination-Metrics "API_Destination.md#AmazonS3-Type-Destination-Metrics")>
            <[EventThreshold](API_Metrics.md#AmazonS3-Type-Metrics-EventThreshold "API_Metrics.md#AmazonS3-Type-Metrics-EventThreshold")>
               <[Minutes](API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes "API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes")>`integer`</[Minutes](API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes "API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes")>
            </[EventThreshold](API_Metrics.md#AmazonS3-Type-Metrics-EventThreshold "API_Metrics.md#AmazonS3-Type-Metrics-EventThreshold")>
            <[Status](API_Metrics.md#AmazonS3-Type-Metrics-Status "API_Metrics.md#AmazonS3-Type-Metrics-Status")>`string`</[Status](API_Metrics.md#AmazonS3-Type-Metrics-Status "API_Metrics.md#AmazonS3-Type-Metrics-Status")>
         </[Metrics](API_Destination.md#AmazonS3-Type-Destination-Metrics "API_Destination.md#AmazonS3-Type-Destination-Metrics")>
         <[ReplicationTime](API_Destination.md#AmazonS3-Type-Destination-ReplicationTime "API_Destination.md#AmazonS3-Type-Destination-ReplicationTime")>
            <[Status](API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Status "API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Status")>`string`</[Status](API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Status "API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Status")>
            <[Time](API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Time "API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Time")>
               <[Minutes](API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes "API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes")>`integer`</[Minutes](API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes "API_ReplicationTimeValue.md#AmazonS3-Type-ReplicationTimeValue-Minutes")>
            </[Time](API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Time "API_ReplicationTime.md#AmazonS3-Type-ReplicationTime-Time")>
         </[ReplicationTime](API_Destination.md#AmazonS3-Type-Destination-ReplicationTime "API_Destination.md#AmazonS3-Type-Destination-ReplicationTime")>
         <[StorageClass](API_Destination.md#AmazonS3-Type-Destination-StorageClass "API_Destination.md#AmazonS3-Type-Destination-StorageClass")>`string`</[StorageClass](API_Destination.md#AmazonS3-Type-Destination-StorageClass "API_Destination.md#AmazonS3-Type-Destination-StorageClass")>
      </[Destination](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Destination "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Destination")>
      <[ExistingObjectReplication](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ExistingObjectReplication "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ExistingObjectReplication")>
         <[Status](API_ExistingObjectReplication.md#AmazonS3-Type-ExistingObjectReplication-Status "API_ExistingObjectReplication.md#AmazonS3-Type-ExistingObjectReplication-Status")>`string`</[Status](API_ExistingObjectReplication.md#AmazonS3-Type-ExistingObjectReplication-Status "API_ExistingObjectReplication.md#AmazonS3-Type-ExistingObjectReplication-Status")>
      </[ExistingObjectReplication](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ExistingObjectReplication "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ExistingObjectReplication")>
      <[Filter](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Filter "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Filter")>
         <[And](API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-And "API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-And")>
            <[Prefix](API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Prefix "API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Prefix")>`string`</[Prefix](API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Prefix "API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Prefix")>
            <[Tag](API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Tags "API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Tags")>
               <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>`string`</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
               <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>`string`</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
            </[Tag](API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Tags "API_ReplicationRuleAndOperator.md#AmazonS3-Type-ReplicationRuleAndOperator-Tags")>
            ...
         </[And](API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-And "API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-And")>
         <[Prefix](API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Prefix "API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Prefix")>`string`</[Prefix](API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Prefix "API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Prefix")>
         <[Tag](API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Tag "API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Tag")>
            <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>`string`</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
            <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>`string`</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
         </[Tag](API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Tag "API_ReplicationRuleFilter.md#AmazonS3-Type-ReplicationRuleFilter-Tag")>
      </[Filter](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Filter "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Filter")>
      <[ID](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ID "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ID")>`string`</[ID](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ID "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-ID")>
      <[Prefix](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Prefix "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Prefix")>`string`</[Prefix](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Prefix "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Prefix")>
      <[Priority](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Priority "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Priority")>`integer`</[Priority](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Priority "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Priority")>
      <[SourceSelectionCriteria](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-SourceSelectionCriteria "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-SourceSelectionCriteria")>
         <[ReplicaModifications](API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-ReplicaModifications "API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-ReplicaModifications")>
            <[Status](API_ReplicaModifications.md#AmazonS3-Type-ReplicaModifications-Status "API_ReplicaModifications.md#AmazonS3-Type-ReplicaModifications-Status")>`string`</[Status](API_ReplicaModifications.md#AmazonS3-Type-ReplicaModifications-Status "API_ReplicaModifications.md#AmazonS3-Type-ReplicaModifications-Status")>
         </[ReplicaModifications](API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-ReplicaModifications "API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-ReplicaModifications")>
         <[SseKmsEncryptedObjects](API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-SseKmsEncryptedObjects "API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-SseKmsEncryptedObjects")>
            <[Status](API_SseKmsEncryptedObjects.md#AmazonS3-Type-SseKmsEncryptedObjects-Status "API_SseKmsEncryptedObjects.md#AmazonS3-Type-SseKmsEncryptedObjects-Status")>`string`</[Status](API_SseKmsEncryptedObjects.md#AmazonS3-Type-SseKmsEncryptedObjects-Status "API_SseKmsEncryptedObjects.md#AmazonS3-Type-SseKmsEncryptedObjects-Status")>
         </[SseKmsEncryptedObjects](API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-SseKmsEncryptedObjects "API_SourceSelectionCriteria.md#AmazonS3-Type-SourceSelectionCriteria-SseKmsEncryptedObjects")>
      </[SourceSelectionCriteria](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-SourceSelectionCriteria "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-SourceSelectionCriteria")>
      <[Status](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Status "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Status")>`string`</[Status](API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Status "API_ReplicationRule.md#AmazonS3-Type-ReplicationRule-Status")>
   </[Rule](#AmazonS3-PutBucketReplication-request-Rules "#AmazonS3-PutBucketReplication-request-Rules")>
   ...
</[ReplicationConfiguration](#AmazonS3-PutBucketReplication-request-ReplicationConfiguration "#AmazonS3-PutBucketReplication-request-ReplicationConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketReplication_RequestSyntax "#API_PutBucketReplication_RequestSyntax")**


The name of the bucket


Required: Yes




**[Content-MD5](#API_PutBucketReplication_RequestSyntax "#API_PutBucketReplication_RequestSyntax")**


The Base64 encoded 128-bit `MD5` digest of the data. You must use this header as a
 message integrity check to verify that the request body was not corrupted in transit. For more
 information, see [RFC 1864](http://www.ietf.org/rfc/rfc1864.txt "http://www.ietf.org/rfc/rfc1864.txt").


For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[x-amz-bucket-object-lock-token](#API_PutBucketReplication_RequestSyntax "#API_PutBucketReplication_RequestSyntax")**


A token to allow Object Lock to be enabled for an existing bucket.




**[x-amz-expected-bucket-owner](#API_PutBucketReplication_RequestSyntax "#API_PutBucketReplication_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-sdk-checksum-algorithm](#API_PutBucketReplication_RequestSyntax "#API_PutBucketReplication_RequestSyntax")**


Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
 additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
 `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
 information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
 parameter.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[ReplicationConfiguration](#API_PutBucketReplication_RequestSyntax "#API_PutBucketReplication_RequestSyntax")**


Root level tag for the ReplicationConfiguration parameters.


Required: Yes




**[Role](#API_PutBucketReplication_RequestSyntax "#API_PutBucketReplication_RequestSyntax")**


The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that Amazon S3 assumes when replicating
 objects. For more information, see [How to Set Up Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html") in the
 *Amazon S3 User Guide*.


Type: String


Required: Yes




**[Rule](#API_PutBucketReplication_RequestSyntax "#API_PutBucketReplication_RequestSyntax")**


A container for one or more replication rules. A replication configuration must have at least one
 rule and can contain a maximum of 1,000 rules. 


Type: Array of [ReplicationRule](API_ReplicationRule.md "API_ReplicationRule.md") data types


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample Request: Add a replication configuration


The following is a sample `PUT` request that creates a replication subresource on the
 specified bucket and saves the replication configuration in it. The replication configuration
 specifies a rule to replicate objects to the `DOC-EXAMPLE-BUCKET` bucket. The rule
 includes a filter to replicate only the objects created with the key name prefix TaxDocs and that
 have two specific tags.


After you add a replication configuration to your bucket, Amazon S3 assumes the AWS Identity and Access Management (IAM)
 role specified in the configuration to replicate objects on behalf of the bucket owner. The bucket
 owner is the AWS account that created the bucket.


Filtering using the <Filter> element is supported in the latest XML configuration. If you
 are using an earlier version of the XML configuration, you can filter only on key prefix. In that
 case, you add the <Prefix> element as a child of the <Rule>.


For more examples of replication configuration, see [Replication Configuration Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-config-example-configs "https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-config-example-configs") in the *Amazon S3 User Guide.*




```

PUT /?replication HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com 
Date: Wed, 11 Feb 2015 02:11:21 GMT
Content-MD5: q6yJDlIkcBaGGfb3QLY69A==
Authorization: authorization string
Content-Length: length

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
      <Bucket>arn:aws:s3:::DOC-EXAMPLE-BUCKET</Bucket>
    </Destination>
  </Rule>
</ReplicationConfiguration>
         
```

### Sample Response


This example illustrates one usage of PutBucketReplication.



```

HTTP/1.1 200 OK
x-amz-id-2: r+qR7+nhXtJDDIJ0JJYcd+1j5nM/rUFiiiZ/fNbDOsd3JUE8NWMLNHXmvPfwMpdc
x-amz-request-id: 9E26D08072A8EF9E
Date: Wed, 11 Feb 2015 02:11:22 GMT
Content-Length: 0
Server: AmazonS3
         
```

### Sample Request: Add a Replication Configuration with Amazon S3 Replication Time Control
 Enabled


You can use S3 Replication Time Control (S3 RTC) to replicate your data in the same AWS Region or across different
 AWS Regions in a predictable time frame. S3 RTC replicates 99.99 percent of new objects stored in
 Amazon S3 within 15 minutes. For more information, see [Replicating objects using Replication Time
 Control](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-time-control.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-time-control.html").



```

PUT /?replication HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com 
Date: Wed, 11 Feb 2015 02:11:21 GMT
Content-MD5: q6yJDlIkcBaGGfb3QLY69A==
Authorization: authorization string
Content-Length: length
x-amz-bucket-object-lock-token: Token
<?xml version="1.0" encoding="UTF-8"?>

<ReplicationConfiguration>
  <Role>arn:aws:iam::35667example:role/CrossRegionReplicationRoleForS3</Role>
  <Rule>
    <ID>rule1</ID>
    <Status>Enabled</Status>
    <Priority>1</Priority>
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
      <Bucket>arn:aws:s3:::DOC-EXAMPLE-BUCKET</Bucket>
      <Metrics>
         <Status>Enabled</Status>
         <EventThreshold>
            <Minutes>15</Minutes>
         </EventThreshold>
      </Metrics>
      <ReplicationTime>
         <Status>Enabled</Status>
         <Time>
            <Minutes>15</Minutes>
         </Time>
      </ReplicationTime>           
    </Destination>
  </Rule>
</ReplicationConfiguration>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketReplication "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketReplication")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketReplication "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketReplication")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketReplication")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketReplication")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketReplication")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketReplication")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketReplication")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketReplication")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketReplication "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketReplication")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketReplication")
