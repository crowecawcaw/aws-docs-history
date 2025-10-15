# ReplicationConfiguration

A container for replication rules. You can add up to 1,000 rules. The maximum size of a replication
 configuration is 2 MB.


## Contents





**Role** 


The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that Amazon S3 assumes when replicating
 objects. For more information, see [How to Set Up Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html") in the
 *Amazon S3 User Guide*.


Type: String


Required: Yes




**Rules** 


A container for one or more replication rules. A replication configuration must have at least one
 rule and can contain a maximum of 1,000 rules. 


Type: Array of [ReplicationRule](API_ReplicationRule.md "API_ReplicationRule.md") data types


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ReplicationConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ReplicationConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ReplicationConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ReplicationConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ReplicationConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ReplicationConfiguration")
