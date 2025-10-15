# ReplicationRule

Specifies which S3 on Outposts objects to replicate and where to store the
 replicas.


## Contents





**Bucket** 


The Amazon Resource Name (ARN) of the access point for the source Outposts bucket that you want
 S3 on Outposts to replicate the objects from.


Type: String


Required: Yes




**Destination** 


A container for information about the replication destination and its
 configurations.


Type: [Destination](API_control_Destination.md "API_control_Destination.md") data type


Required: Yes




**Status** 


Specifies whether the rule is enabled.


Type: String


Valid Values: `Enabled | Disabled`



Required: Yes




**DeleteMarkerReplication** 


Specifies whether S3 on Outposts replicates delete markers. If you specify a
 `Filter` element in your replication configuration, you must also include a
 `DeleteMarkerReplication` element. If your `Filter` includes a
 `Tag` element, the `DeleteMarkerReplication` element's
 `Status` child element must be set to `Disabled`, because
 S3 on Outposts doesn't support replicating delete markers for tag-based rules.


For more information about delete marker replication, see [How delete operations affect replication](../userguide/S3OutpostsReplication.md#outposts-replication-what-is-replicated "../userguide/S3OutpostsReplication.md#outposts-replication-what-is-replicated") in the
 *Amazon S3 User Guide*. 


Type: [DeleteMarkerReplication](API_control_DeleteMarkerReplication.md "API_control_DeleteMarkerReplication.md") data type


Required: No




**ExistingObjectReplication** 


An optional configuration to replicate existing source bucket objects. 


###### Note

This is not supported by Amazon S3 on Outposts buckets.


Type: [ExistingObjectReplication](API_control_ExistingObjectReplication.md "API_control_ExistingObjectReplication.md") data type


Required: No




**Filter** 


A filter that identifies the subset of objects to which the replication rule applies. A
 `Filter` element must specify exactly one `Prefix`,
 `Tag`, or `And` child element.


Type: [ReplicationRuleFilter](API_control_ReplicationRuleFilter.md "API_control_ReplicationRuleFilter.md") data type


Required: No




**ID** 


A unique identifier for the rule. The maximum value is 255 characters.


Type: String


Required: No




**Prefix** 



*This member has been deprecated.*



An object key name prefix that identifies the object or objects to which the rule
 applies. The maximum prefix length is 1,024 characters. To include all objects in an
 Outposts bucket, specify an empty string.


###### Important

When you're using XML requests, you must 
replace special characters (such as carriage returns) in object keys with their equivalent XML entity codes. 
For more information, see [XML-related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints") in the *Amazon S3 User Guide*.


Type: String


Required: No




**Priority** 


The priority indicates which rule has precedence whenever two or more replication rules
 conflict. S3 on Outposts attempts to replicate objects according to all replication rules.
 However, if there are two or more rules with the same destination Outposts bucket, then
 objects will be replicated according to the rule with the highest priority. The higher the
 number, the higher the priority. 


For more information, see [Creating replication
 rules on Outposts](../userguide/replication-between-outposts.md "../userguide/replication-between-outposts.md") in the *Amazon S3 User Guide*.


Type: Integer


Required: No




**SourceSelectionCriteria** 


A container that describes additional filters for identifying the source Outposts
 objects that you want to replicate. You can choose to enable or disable the replication of
 these objects.


Type: [SourceSelectionCriteria](API_control_SourceSelectionCriteria.md "API_control_SourceSelectionCriteria.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ReplicationRule "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ReplicationRule")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ReplicationRule "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ReplicationRule")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ReplicationRule "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ReplicationRule")
