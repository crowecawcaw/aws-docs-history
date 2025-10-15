# ObjectLambdaTransformationConfiguration

###### Note

Amazon S3 Object Lambda will no longer be open to new customers starting on 11/7/2025. If you would like to use the service, please sign up prior to 11/7/2025. For capabilities similar to S3 Object Lambda, learn more here - [Amazon S3 Object Lambda availability change](../userguide/amazons3-ol-change.md "../userguide/amazons3-ol-change.md").

A configuration used when creating an Object Lambda Access Point transformation.


## Contents





**Actions** 


A container for the action of an Object Lambda Access Point configuration. Valid inputs are
 `GetObject`, `ListObjects`, `HeadObject`, and
 `ListObjectsV2`.


Type: Array of strings


Valid Values: `GetObject | HeadObject | ListObjects | ListObjectsV2`



Required: Yes




**ContentTransformation** 


A container for the content transformation of an Object Lambda Access Point configuration.


Type: [ObjectLambdaContentTransformation](API_control_ObjectLambdaContentTransformation.md "API_control_ObjectLambdaContentTransformation.md") data type



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ObjectLambdaTransformationConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ObjectLambdaTransformationConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ObjectLambdaTransformationConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ObjectLambdaTransformationConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ObjectLambdaTransformationConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ObjectLambdaTransformationConfiguration")
