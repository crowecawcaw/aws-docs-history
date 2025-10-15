# AccessPoint

An access point used to access a bucket.


## Contents





**Bucket** 


The name of the bucket associated with this access point.


Type: String


Length Constraints: Maximum length of 255.


Required: Yes




**Name** 


The name of this access point.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**NetworkOrigin** 


Indicates whether this access point allows access from the public internet. If
 `VpcConfiguration` is specified for this access point, then
 `NetworkOrigin` is `VPC`, and the access point doesn't allow access from
 the public internet. Otherwise, `NetworkOrigin` is `Internet`, and
 the access point allows access from the public internet, subject to the access point and bucket access
 policies.


Type: String


Valid Values: `Internet | VPC`



Required: Yes




**AccessPointArn** 


The ARN for the access point.


Type: String


Length Constraints: Minimum length of 4. Maximum length of 128.


Required: No




**Alias** 


The name or alias of the access point.


Type: String


Length Constraints: Maximum length of 63.


Pattern: `^[0-9a-z\\-]{63}`



Required: No




**BucketAccountId** 


The AWS account ID associated with the S3 bucket associated with this access point.


Type: String


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: No




**DataSourceId** 


A unique identifier for the data source of the access point.


Type: String


Length Constraints: Maximum length of 191.


Required: No




**DataSourceType** 


The type of the data source that the access point is attached to.


Type: String


Required: No




**VpcConfiguration** 


The virtual private cloud (VPC) configuration for this access point, if one exists.


###### Note

This element is empty if this access point is an Amazon S3 on Outposts access point that is used by other
 AWS services.


Type: [VpcConfiguration](API_control_VpcConfiguration.md "API_control_VpcConfiguration.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/AccessPoint "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/AccessPoint")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/AccessPoint "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/AccessPoint")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/AccessPoint "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/AccessPoint")
