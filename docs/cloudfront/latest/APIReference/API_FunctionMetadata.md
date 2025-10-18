# FunctionMetadata

Contains metadata about a CloudFront function.


## Contents





**FunctionARN** 


The Amazon Resource Name (ARN) of the function. The ARN uniquely identifies the
 function.


Type: String


Required: Yes




**LastModifiedTime** 


The date and time when the function was most recently updated.


Type: Timestamp


Required: Yes




**CreatedTime** 


The date and time when the function was created.


Type: Timestamp


Required: No




**Stage** 


The stage that the function is in, either `DEVELOPMENT` or
 `LIVE`.


When a function is in the `DEVELOPMENT` stage, you can test the function
 with `TestFunction`, and update it with `UpdateFunction`.


When a function is in the `LIVE` stage, you can attach the function to a
 distribution's cache behavior, using the function's ARN.


Type: String


Valid Values: `DEVELOPMENT | LIVE`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FunctionMetadata "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FunctionMetadata")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FunctionMetadata "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FunctionMetadata")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FunctionMetadata "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FunctionMetadata")
