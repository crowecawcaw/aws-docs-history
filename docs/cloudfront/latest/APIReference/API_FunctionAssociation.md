# FunctionAssociation

A CloudFront function that is associated with a cache behavior in a CloudFront
 distribution.


## Contents





**EventType** 


The event type of the function, either `viewer-request` or
 `viewer-response`. You cannot use origin-facing event types
 (`origin-request` and `origin-response`) with a CloudFront
 function.


Type: String


Valid Values: `viewer-request | viewer-response | origin-request | origin-response`



Required: Yes




**FunctionARN** 


The Amazon Resource Name (ARN) of the function.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 108.


Pattern: `arn:aws:cloudfront::[0-9]{12}:function\/[a-zA-Z0-9-_]{1,64}`



Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FunctionAssociation "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FunctionAssociation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FunctionAssociation "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FunctionAssociation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FunctionAssociation "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FunctionAssociation")
