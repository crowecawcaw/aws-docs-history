# ObjectLambdaConfiguration

###### Note

Amazon S3 Object Lambda will no longer be open to new customers starting on 11/7/2025. If you would like to use the service, please sign up prior to 11/7/2025. For capabilities similar to S3 Object Lambda, learn more here - [Amazon S3 Object Lambda availability change](../userguide/amazons3-ol-change.md "../userguide/amazons3-ol-change.md").

A configuration used when creating an Object Lambda Access Point.


## Contents





**SupportingAccessPoint** 


Standard access point associated with the Object Lambda Access Point.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[^:]+:s3:[^:]*:\d{12}:accesspoint/.*`



Required: Yes




**TransformationConfigurations** 


A container for transformation configurations for an Object Lambda Access Point.


Type: Array of [ObjectLambdaTransformationConfiguration](API_control_ObjectLambdaTransformationConfiguration.md "API_control_ObjectLambdaTransformationConfiguration.md") data types


Required: Yes




**AllowedFeatures** 


A container for allowed features. Valid inputs are `GetObject-Range`,
 `GetObject-PartNumber`, `HeadObject-Range`, and
 `HeadObject-PartNumber`.


Type: Array of strings


Valid Values: `GetObject-Range | GetObject-PartNumber | HeadObject-Range | HeadObject-PartNumber`



Required: No




**CloudWatchMetricsEnabled** 


A container for whether the CloudWatch metrics configuration is enabled.


Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ObjectLambdaConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ObjectLambdaConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ObjectLambdaConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ObjectLambdaConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ObjectLambdaConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ObjectLambdaConfiguration")
