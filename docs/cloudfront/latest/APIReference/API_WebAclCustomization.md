# WebAclCustomization

The AWS WAF web ACL customization specified for the distribution tenant.


## Contents





**Action** 


The action for the AWS WAF web ACL customization. You can specify `override` to specify a separate AWS WAF web ACL for the distribution tenant. If you specify `disable`, the distribution tenant won't have AWS WAF web ACL protections and won't inherit from the multi-tenant distribution.


Type: String


Valid Values: `override | disable`



Required: Yes




**Arn** 


The Amazon Resource Name (ARN) of the AWS WAF web ACL.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/WebAclCustomization "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/WebAclCustomization")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/WebAclCustomization "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/WebAclCustomization")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/WebAclCustomization "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/WebAclCustomization")
