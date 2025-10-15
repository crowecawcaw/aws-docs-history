# ReplicationConfiguration

A container for one or more replication rules. A replication configuration must have at
 least one rule and you can add up to 100 rules. The maximum size of a replication
 configuration is 128 KB.


## Contents





**Role** 


The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that S3 on Outposts assumes
 when replicating objects. For information about S3 replication on Outposts configuration,
 see [Setting up
 replication](../userguide/outposts-replication-how-setup.md "../userguide/outposts-replication-how-setup.md") in the *Amazon S3 User Guide*.


Type: String


Required: Yes




**Rules** 


A container for one or more replication rules. A replication configuration must have at
 least one rule and can contain an array of 100 rules at the most. 


Type: Array of [ReplicationRule](API_control_ReplicationRule.md "API_control_ReplicationRule.md") data types


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ReplicationConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ReplicationConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ReplicationConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ReplicationConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ReplicationConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ReplicationConfiguration")
