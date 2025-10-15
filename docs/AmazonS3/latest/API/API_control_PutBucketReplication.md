# PutBucketReplication

###### Note

This action creates an Amazon S3 on Outposts bucket's replication configuration. To create
 an S3 bucket's replication configuration, see [PutBucketReplication](API_PutBucketReplication.md "API_PutBucketReplication.md")
 in the *Amazon S3 API Reference*. 

Creates a replication configuration or replaces an existing one. For information about
 S3 replication on Outposts configuration, see [Replicating objects for
 S3 on Outposts](../userguide/S3OutpostsReplication.md "../userguide/S3OutpostsReplication.md") in the *Amazon S3 User Guide*.

###### Note

It can take a while to propagate `PUT` or `DELETE` requests for
 a replication configuration to all S3 on Outposts systems. Therefore, the replication
 configuration that's returned by a `GET` request soon after a
 `PUT` or `DELETE` request might return a more recent result
 than what's on the Outpost. If an Outpost is offline, the delay in updating the
 replication configuration on that Outpost can be significant.

Specify the replication configuration in the request body. In the replication
 configuration, you provide the following information:


* The name of the destination bucket or buckets where you want S3 on Outposts to
 replicate objects
* The AWS Identity and Access Management (IAM) role that S3 on Outposts can assume to replicate objects on
 your behalf
* Other relevant information, such as replication rules
A replication configuration must include at least one rule and can contain a maximum of
 100. Each rule identifies a subset of objects to replicate by filtering the objects in the
 source Outposts bucket. To choose additional subsets of objects to replicate, add a rule
 for each subset.

To specify a subset of the objects in the source Outposts bucket to apply a replication
 rule to, add the `Filter` element as a child of the `Rule` element.
 You can filter objects based on an object key prefix, one or more object tags, or both.
 When you add the `Filter` element in the configuration, you must also add the
 following elements: `DeleteMarkerReplication`, `Status`, and
 `Priority`.

Using `PutBucketReplication` on Outposts requires that both the source and
 destination buckets must have versioning enabled. For information about enabling versioning
 on a bucket, see [Managing S3 Versioning
 for your S3 on Outposts bucket](../userguide/S3OutpostsManagingVersioning.md "../userguide/S3OutpostsManagingVersioning.md").

For information about S3 on Outposts replication failure reasons, see [Replication failure reasons](../userguide/outposts-replication-eventbridge.md#outposts-replication-failure-codes "../userguide/outposts-replication-eventbridge.md#outposts-replication-failure-codes") in the *Amazon S3 User Guide*.


**Handling Replication of Encrypted Objects**


Outposts buckets are encrypted at all times. All the objects in the source Outposts
 bucket are encrypted and can be replicated. Also, all the replicas in the destination
 Outposts bucket are encrypted with the same encryption key as the objects in the source
 Outposts bucket.


**Permissions**


To create a `PutBucketReplication` request, you must have
 `s3-outposts:PutReplicationConfiguration` permissions for the bucket. The
 Outposts bucket owner has this permission by default and can grant it to others. For more
 information about permissions, see [Setting up IAM with
 S3 on Outposts](../userguide/S3OutpostsIAM.md "../userguide/S3OutpostsIAM.md") and [Managing access to
 S3 on Outposts buckets](../userguide/S3OutpostsBucketPolicy.md "../userguide/S3OutpostsBucketPolicy.md"). 

###### Note

To perform this operation, the user or role must also have the
 `iam:CreateRole` and `iam:PassRole` permissions. For more
 information, see [Granting a user permissions to
 pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html").

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_PutBucketReplication.md#API_control_PutBucketReplication_Examples "API_control_PutBucketReplication.md#API_control_PutBucketReplication_Examples") section.

The following operations are related to `PutBucketReplication`:


* [GetBucketReplication](API_control_GetBucketReplication.md "API_control_GetBucketReplication.md")
* [DeleteBucketReplication](API_control_DeleteBucketReplication.md "API_control_DeleteBucketReplication.md")

## Request Syntax



```
PUT /v20180820/bucket/`name`/replication HTTP/1.1
Host: `Bucket`.s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[ReplicationConfiguration](#AmazonS3-control_PutBucketReplication-request-ReplicationConfiguration "#AmazonS3-control_PutBucketReplication-request-ReplicationConfiguration") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[Role](#AmazonS3-control_PutBucketReplication-request-Role "#AmazonS3-control_PutBucketReplication-request-Role")>`string`</[Role](#AmazonS3-control_PutBucketReplication-request-Role "#AmazonS3-control_PutBucketReplication-request-Role")>
   <[Rules](#AmazonS3-control_PutBucketReplication-request-Rules "#AmazonS3-control_PutBucketReplication-request-Rules")>
      <Rule>
         <[Bucket](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Bucket "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Bucket")>`string`</[Bucket](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Bucket "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Bucket")>
         <[DeleteMarkerReplication](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-DeleteMarkerReplication "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-DeleteMarkerReplication")>
            <[Status](API_control_DeleteMarkerReplication.md#AmazonS3-Type-control_DeleteMarkerReplication-Status "API_control_DeleteMarkerReplication.md#AmazonS3-Type-control_DeleteMarkerReplication-Status")>`string`</[Status](API_control_DeleteMarkerReplication.md#AmazonS3-Type-control_DeleteMarkerReplication-Status "API_control_DeleteMarkerReplication.md#AmazonS3-Type-control_DeleteMarkerReplication-Status")>
         </[DeleteMarkerReplication](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-DeleteMarkerReplication "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-DeleteMarkerReplication")>
         <[Destination](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Destination "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Destination")>
            <[AccessControlTranslation](API_control_Destination.md#AmazonS3-Type-control_Destination-AccessControlTranslation "API_control_Destination.md#AmazonS3-Type-control_Destination-AccessControlTranslation")>
               <[Owner](API_control_AccessControlTranslation.md#AmazonS3-Type-control_AccessControlTranslation-Owner "API_control_AccessControlTranslation.md#AmazonS3-Type-control_AccessControlTranslation-Owner")>`string`</[Owner](API_control_AccessControlTranslation.md#AmazonS3-Type-control_AccessControlTranslation-Owner "API_control_AccessControlTranslation.md#AmazonS3-Type-control_AccessControlTranslation-Owner")>
            </[AccessControlTranslation](API_control_Destination.md#AmazonS3-Type-control_Destination-AccessControlTranslation "API_control_Destination.md#AmazonS3-Type-control_Destination-AccessControlTranslation")>
            <[Account](API_control_Destination.md#AmazonS3-Type-control_Destination-Account "API_control_Destination.md#AmazonS3-Type-control_Destination-Account")>`string`</[Account](API_control_Destination.md#AmazonS3-Type-control_Destination-Account "API_control_Destination.md#AmazonS3-Type-control_Destination-Account")>
            <[Bucket](API_control_Destination.md#AmazonS3-Type-control_Destination-Bucket "API_control_Destination.md#AmazonS3-Type-control_Destination-Bucket")>`string`</[Bucket](API_control_Destination.md#AmazonS3-Type-control_Destination-Bucket "API_control_Destination.md#AmazonS3-Type-control_Destination-Bucket")>
            <[EncryptionConfiguration](API_control_Destination.md#AmazonS3-Type-control_Destination-EncryptionConfiguration "API_control_Destination.md#AmazonS3-Type-control_Destination-EncryptionConfiguration")>
               <[ReplicaKmsKeyID](API_control_EncryptionConfiguration.md#AmazonS3-Type-control_EncryptionConfiguration-ReplicaKmsKeyID "API_control_EncryptionConfiguration.md#AmazonS3-Type-control_EncryptionConfiguration-ReplicaKmsKeyID")>`string`</[ReplicaKmsKeyID](API_control_EncryptionConfiguration.md#AmazonS3-Type-control_EncryptionConfiguration-ReplicaKmsKeyID "API_control_EncryptionConfiguration.md#AmazonS3-Type-control_EncryptionConfiguration-ReplicaKmsKeyID")>
            </[EncryptionConfiguration](API_control_Destination.md#AmazonS3-Type-control_Destination-EncryptionConfiguration "API_control_Destination.md#AmazonS3-Type-control_Destination-EncryptionConfiguration")>
            <[Metrics](API_control_Destination.md#AmazonS3-Type-control_Destination-Metrics "API_control_Destination.md#AmazonS3-Type-control_Destination-Metrics")>
               <[EventThreshold](API_control_Metrics.md#AmazonS3-Type-control_Metrics-EventThreshold "API_control_Metrics.md#AmazonS3-Type-control_Metrics-EventThreshold")>
                  <[Minutes](API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes "API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes")>`integer`</[Minutes](API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes "API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes")>
               </[EventThreshold](API_control_Metrics.md#AmazonS3-Type-control_Metrics-EventThreshold "API_control_Metrics.md#AmazonS3-Type-control_Metrics-EventThreshold")>
               <[Status](API_control_Metrics.md#AmazonS3-Type-control_Metrics-Status "API_control_Metrics.md#AmazonS3-Type-control_Metrics-Status")>`string`</[Status](API_control_Metrics.md#AmazonS3-Type-control_Metrics-Status "API_control_Metrics.md#AmazonS3-Type-control_Metrics-Status")>
            </[Metrics](API_control_Destination.md#AmazonS3-Type-control_Destination-Metrics "API_control_Destination.md#AmazonS3-Type-control_Destination-Metrics")>
            <[ReplicationTime](API_control_Destination.md#AmazonS3-Type-control_Destination-ReplicationTime "API_control_Destination.md#AmazonS3-Type-control_Destination-ReplicationTime")>
               <[Status](API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Status "API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Status")>`string`</[Status](API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Status "API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Status")>
               <[Time](API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Time "API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Time")>
                  <[Minutes](API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes "API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes")>`integer`</[Minutes](API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes "API_control_ReplicationTimeValue.md#AmazonS3-Type-control_ReplicationTimeValue-Minutes")>
               </[Time](API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Time "API_control_ReplicationTime.md#AmazonS3-Type-control_ReplicationTime-Time")>
            </[ReplicationTime](API_control_Destination.md#AmazonS3-Type-control_Destination-ReplicationTime "API_control_Destination.md#AmazonS3-Type-control_Destination-ReplicationTime")>
            <[StorageClass](API_control_Destination.md#AmazonS3-Type-control_Destination-StorageClass "API_control_Destination.md#AmazonS3-Type-control_Destination-StorageClass")>`string`</[StorageClass](API_control_Destination.md#AmazonS3-Type-control_Destination-StorageClass "API_control_Destination.md#AmazonS3-Type-control_Destination-StorageClass")>
         </[Destination](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Destination "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Destination")>
         <[ExistingObjectReplication](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ExistingObjectReplication "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ExistingObjectReplication")>
            <[Status](API_control_ExistingObjectReplication.md#AmazonS3-Type-control_ExistingObjectReplication-Status "API_control_ExistingObjectReplication.md#AmazonS3-Type-control_ExistingObjectReplication-Status")>`string`</[Status](API_control_ExistingObjectReplication.md#AmazonS3-Type-control_ExistingObjectReplication-Status "API_control_ExistingObjectReplication.md#AmazonS3-Type-control_ExistingObjectReplication-Status")>
         </[ExistingObjectReplication](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ExistingObjectReplication "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ExistingObjectReplication")>
         <[Filter](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Filter "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Filter")>
            <[And](API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-And "API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-And")>
               <[Prefix](API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Prefix "API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Prefix")>`string`</[Prefix](API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Prefix "API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Prefix")>
               <[Tags](API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Tags "API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Tags")>
                  <S3Tag>
                     <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>`string`</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
                     <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>`string`</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
                  </S3Tag>
               </[Tags](API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Tags "API_control_ReplicationRuleAndOperator.md#AmazonS3-Type-control_ReplicationRuleAndOperator-Tags")>
            </[And](API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-And "API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-And")>
            <[Prefix](API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Prefix "API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Prefix")>`string`</[Prefix](API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Prefix "API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Prefix")>
            <[Tag](API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Tag "API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Tag")>
               <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>`string`</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
               <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>`string`</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
            </[Tag](API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Tag "API_control_ReplicationRuleFilter.md#AmazonS3-Type-control_ReplicationRuleFilter-Tag")>
         </[Filter](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Filter "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Filter")>
         <[ID](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ID "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ID")>`string`</[ID](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ID "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-ID")>
         <[Prefix](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Prefix "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Prefix")>`string`</[Prefix](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Prefix "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Prefix")>
         <[Priority](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Priority "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Priority")>`integer`</[Priority](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Priority "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Priority")>
         <[SourceSelectionCriteria](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-SourceSelectionCriteria "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-SourceSelectionCriteria")>
            <[ReplicaModifications](API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-ReplicaModifications "API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-ReplicaModifications")>
               <[Status](API_control_ReplicaModifications.md#AmazonS3-Type-control_ReplicaModifications-Status "API_control_ReplicaModifications.md#AmazonS3-Type-control_ReplicaModifications-Status")>`string`</[Status](API_control_ReplicaModifications.md#AmazonS3-Type-control_ReplicaModifications-Status "API_control_ReplicaModifications.md#AmazonS3-Type-control_ReplicaModifications-Status")>
            </[ReplicaModifications](API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-ReplicaModifications "API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-ReplicaModifications")>
            <[SseKmsEncryptedObjects](API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-SseKmsEncryptedObjects "API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-SseKmsEncryptedObjects")>
               <[Status](API_control_SseKmsEncryptedObjects.md#AmazonS3-Type-control_SseKmsEncryptedObjects-Status "API_control_SseKmsEncryptedObjects.md#AmazonS3-Type-control_SseKmsEncryptedObjects-Status")>`string`</[Status](API_control_SseKmsEncryptedObjects.md#AmazonS3-Type-control_SseKmsEncryptedObjects-Status "API_control_SseKmsEncryptedObjects.md#AmazonS3-Type-control_SseKmsEncryptedObjects-Status")>
            </[SseKmsEncryptedObjects](API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-SseKmsEncryptedObjects "API_control_SourceSelectionCriteria.md#AmazonS3-Type-control_SourceSelectionCriteria-SseKmsEncryptedObjects")>
         </[SourceSelectionCriteria](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-SourceSelectionCriteria "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-SourceSelectionCriteria")>
         <[Status](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Status "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Status")>`string`</[Status](API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Status "API_control_ReplicationRule.md#AmazonS3-Type-control_ReplicationRule-Status")>
      </Rule>
   </[Rules](#AmazonS3-control_PutBucketReplication-request-Rules "#AmazonS3-control_PutBucketReplication-request-Rules")>
</[ReplicationConfiguration](#AmazonS3-control_PutBucketReplication-request-ReplicationConfiguration "#AmazonS3-control_PutBucketReplication-request-ReplicationConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_PutBucketReplication_RequestSyntax "#API_control_PutBucketReplication_RequestSyntax")**


Specifies the S3 on Outposts bucket to set the configuration for.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded. 


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_PutBucketReplication_RequestSyntax "#API_control_PutBucketReplication_RequestSyntax")**


The AWS account ID of the Outposts bucket.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[ReplicationConfiguration](#API_control_PutBucketReplication_RequestSyntax "#API_control_PutBucketReplication_RequestSyntax")**


Root level tag for the ReplicationConfiguration parameters.


Required: Yes




**[Role](#API_control_PutBucketReplication_RequestSyntax "#API_control_PutBucketReplication_RequestSyntax")**


The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that S3 on Outposts assumes
 when replicating objects. For information about S3 replication on Outposts configuration,
 see [Setting up
 replication](../userguide/outposts-replication-how-setup.md "../userguide/outposts-replication-how-setup.md") in the *Amazon S3 User Guide*.


Type: String


Required: Yes




**[Rules](#API_control_PutBucketReplication_RequestSyntax "#API_control_PutBucketReplication_RequestSyntax")**


A container for one or more replication rules. A replication configuration must have at
 least one rule and can contain an array of 100 rules at the most. 


Type: Array of [ReplicationRule](API_control_ReplicationRule.md "API_control_ReplicationRule.md") data types


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample Request: Add a replication configuration to an Amazon S3 on Outposts
 bucket


The following sample `PUT` request creates a replication subresource on
 the specified Outposts bucket named `example-outpost-bucket` and saves
 the replication configuration in it. The replication configuration specifies a rule
 to replicate objects to the `example-outpost-bucket` bucket. The rule
 includes a filter to replicate only the objects that are created with the key name
 prefix `TaxDocs` and that have two specific tags.


After you add a replication configuration to your Outposts bucket, S3 on Outposts
 assumes the AWS Identity and Access Management (IAM) role that's specified in the configuration to replicate
 objects on behalf of the Outposts bucket owner. The bucket owner is the
 AWS account that created the Outposts bucket.


Filtering by using the `Filter` element is supported in the latest XML
 configuration. The earlier version of the XML configuration isn't supported.


For more examples of S3 replication on Outposts configuration, see [Creating
 replication rules on Outposts](../userguide/replication-between-outposts.md "../userguide/replication-between-outposts.md") in the
 *Amazon S3 User Guide*.



```

PUT /v20180820/bucket/example-outpost-bucket/replication HTTP/1.1
Host:s3-outposts.<Region>.amazonaws.com
x-amz-account-id: example-account-id
x-amz-outpost-id: op-01ac5d28a6a232904
Authorization: authorization string


<ReplicationConfiguration>
  <Role>arn:aws:iam::35667example:role/ReplicationRoleForS3Outposts</Role>
  <Rules>
   <Rule>
      <Bucket>arn:aws:s3-outposts:us-east-1:example-account-id:outpost/SOURCE-OUTPOST-ID/accesspoint/SOURCE-OUTPOSTS-BUCKET-ACCESS-POINT</Bucket>
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
               <Key>key2</Key>
               <Value>value2</Value>
            </Tag>
         </And>
      </Filter>
      <Destination>
         <Bucket>arn:aws:s3-outposts:us-east-1:example-account-id:outpost/DESTINATION-OUTPOST-ID/accesspoint/DESTINATION-OUTPOSTS-BUCKET-ACCESS-POINT</Bucket>
      </Destination>
   </Rule>
  </Rules> 
</ReplicationConfiguration>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutBucketReplication "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutBucketReplication")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutBucketReplication "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutBucketReplication")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutBucketReplication")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutBucketReplication")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutBucketReplication")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutBucketReplication")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutBucketReplication")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutBucketReplication")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutBucketReplication "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutBucketReplication")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutBucketReplication "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutBucketReplication")
