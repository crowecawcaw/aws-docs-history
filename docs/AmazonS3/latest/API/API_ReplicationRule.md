# ReplicationRule

Specifies which Amazon S3 objects to replicate and where to store the replicas.


## Contents





**Destination** 


A container for information about the replication destination and its configurations including
 enabling the S3 Replication Time Control (S3 RTC).


Type: [Destination](API_Destination.md "API_Destination.md") data type


Required: Yes




**Status** 


Specifies whether the rule is enabled.


Type: String


Valid Values: `Enabled | Disabled`



Required: Yes




**DeleteMarkerReplication** 


Specifies whether Amazon S3 replicates delete markers. If you specify a `Filter` in your
 replication configuration, you must also include a `DeleteMarkerReplication` element. If your
 `Filter` includes a `Tag` element, the `DeleteMarkerReplication`
`Status` must be set to Disabled, because Amazon S3 does not support replicating delete markers
 for tag-based rules. For an example configuration, see [Basic Rule
 Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-config-min-rule-config "https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-config-min-rule-config"). 


For more information about delete marker replication, see [Basic Rule Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/delete-marker-replication.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/delete-marker-replication.html"). 


###### Note

If you are using an earlier version of the replication configuration, Amazon S3 handles replication of
 delete markers differently. For more information, see [Backward Compatibility](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-backward-compat-considerations "https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-backward-compat-considerations").


Type: [DeleteMarkerReplication](API_DeleteMarkerReplication.md "API_DeleteMarkerReplication.md") data type


Required: No




**ExistingObjectReplication** 


Optional configuration to replicate existing source bucket objects. 


###### Note

This parameter is no longer supported. To replicate existing objects, see [Replicating
 existing objects with S3 Batch Replication](../userguide/s3-batch-replication-batch.md "../userguide/s3-batch-replication-batch.md") in the
 *Amazon S3 User Guide*.


Type: [ExistingObjectReplication](API_ExistingObjectReplication.md "API_ExistingObjectReplication.md") data type


Required: No




**Filter** 


A filter that identifies the subset of objects to which the replication rule applies. A
 `Filter` must specify exactly one `Prefix`, `Tag`, or an
 `And` child element.


Type: [ReplicationRuleFilter](API_ReplicationRuleFilter.md "API_ReplicationRuleFilter.md") data type


Required: No




**ID** 


A unique identifier for the rule. The maximum value is 255 characters.


Type: String


Required: No




**Prefix** 



*This member has been deprecated.*



An object key name prefix that identifies the object or objects to which the rule applies. The
 maximum prefix length is 1,024 characters. To include all objects in a bucket, specify an empty string.
 


###### Important

Replacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").


Type: String


Required: No




**Priority** 


The priority indicates which rule has precedence whenever two or more replication rules conflict.
 Amazon S3 will attempt to replicate objects according to all replication rules. However, if there are two or
 more rules with the same destination bucket, then objects will be replicated according to the rule with
 the highest priority. The higher the number, the higher the priority. 


For more information, see [Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html") in the *Amazon S3 User Guide*.


Type: Integer


Required: No




**SourceSelectionCriteria** 


A container that describes additional filters for identifying the source objects that you want to
 replicate. You can choose to enable or disable the replication of these objects. Currently, Amazon S3
 supports only the filter that you can specify for objects created with server-side encryption using a
 customer managed key stored in AWS Key Management Service (SSE-KMS).


Type: [SourceSelectionCriteria](API_SourceSelectionCriteria.md "API_SourceSelectionCriteria.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ReplicationRule "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ReplicationRule")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ReplicationRule "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ReplicationRule")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ReplicationRule "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ReplicationRule")
