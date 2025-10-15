# S3ManifestOutputLocation

Location details for where the generated manifest should be written.


## Contents





**Bucket** 


The bucket ARN the generated manifest should be written to.


###### Note


**Directory buckets** - Directory buckets
 aren't supported as the buckets to store the generated manifest.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `arn:[^:]+:s3:.*`



Required: Yes




**ManifestFormat** 


The format of the generated manifest.


Type: String


Valid Values: `S3InventoryReport_CSV_20211130`



Required: Yes




**ExpectedManifestBucketOwner** 


The Account ID that owns the bucket the generated manifest is written to.


Type: String


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: No




**ManifestEncryption** 


Specifies what encryption should be used when the generated manifest objects are
 written.


Type: [GeneratedManifestEncryption](API_control_GeneratedManifestEncryption.md "API_control_GeneratedManifestEncryption.md") data type


Required: No




**ManifestPrefix** 


Prefix identifying one or more objects to which the manifest applies.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 512.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3ManifestOutputLocation "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3ManifestOutputLocation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3ManifestOutputLocation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3ManifestOutputLocation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3ManifestOutputLocation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3ManifestOutputLocation")
