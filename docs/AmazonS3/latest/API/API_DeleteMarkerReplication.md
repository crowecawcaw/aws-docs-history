# DeleteMarkerReplication

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


## Contents





**Status** 


Indicates whether to replicate delete markers.


###### Note

Indicates whether to replicate delete markers.


Type: String


Valid Values: `Enabled | Disabled`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteMarkerReplication "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteMarkerReplication")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteMarkerReplication "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteMarkerReplication")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteMarkerReplication "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteMarkerReplication")
