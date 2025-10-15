# IntelligentTieringConfiguration

Specifies the S3 Intelligent-Tiering configuration for an Amazon S3 bucket.

For information about the S3 Intelligent-Tiering storage class, see [Storage class for
 automatically optimizing frequently and infrequently accessed objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html#sc-dynamic-data-access "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html#sc-dynamic-data-access").


## Contents





**Id** 


The ID used to identify the S3 Intelligent-Tiering configuration.


Type: String


Required: Yes




**Status** 


Specifies the status of the configuration.


Type: String


Valid Values: `Enabled | Disabled`



Required: Yes




**Tierings** 


Specifies the S3 Intelligent-Tiering storage class tier of the configuration.


Type: Array of [Tiering](API_Tiering.md "API_Tiering.md") data types


Required: Yes




**Filter** 


Specifies a bucket filter. The configuration only includes objects that meet the filter's
 criteria.


Type: [IntelligentTieringFilter](API_IntelligentTieringFilter.md "API_IntelligentTieringFilter.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/IntelligentTieringConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/IntelligentTieringConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/IntelligentTieringConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/IntelligentTieringConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/IntelligentTieringConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/IntelligentTieringConfiguration")
