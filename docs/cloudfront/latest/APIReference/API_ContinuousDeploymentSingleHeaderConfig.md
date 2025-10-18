# ContinuousDeploymentSingleHeaderConfig

This configuration determines which HTTP requests are sent to the staging
 distribution. If the HTTP request contains a header and value that matches what you
 specify here, the request is sent to the staging distribution. Otherwise the request is
 sent to the primary distribution.


## Contents





**Header** 


The request header name that you want CloudFront to send to your staging
 distribution. The header must contain the prefix `aws-cf-cd-`.


Type: String


Required: Yes




**Value** 


The request header value.


Type: String


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContinuousDeploymentSingleHeaderConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContinuousDeploymentSingleHeaderConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContinuousDeploymentSingleHeaderConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContinuousDeploymentSingleHeaderConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContinuousDeploymentSingleHeaderConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContinuousDeploymentSingleHeaderConfig")
