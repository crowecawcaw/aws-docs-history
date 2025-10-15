# DeleteMarkerReplication

Specifies whether S3 on Outposts replicates delete markers. If you specify a
 `Filter` element in your replication configuration, you must also include a
 `DeleteMarkerReplication` element. If your `Filter` includes a
 `Tag` element, the `DeleteMarkerReplication` element's
 `Status` child element must be set to `Disabled`, because
 S3 on Outposts does not support replicating delete markers for tag-based rules.

For more information about delete marker replication, see [How delete operations affect replication](../userguide/S3OutpostsReplication.md#outposts-replication-what-is-replicated "../userguide/S3OutpostsReplication.md#outposts-replication-what-is-replicated") in the
 *Amazon S3 User Guide*. 


## Contents





**Status** 


Indicates whether to replicate delete markers.


Type: String


Valid Values: `Enabled | Disabled`



Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteMarkerReplication "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteMarkerReplication")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteMarkerReplication "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteMarkerReplication")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteMarkerReplication "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteMarkerReplication")
