# AnycastIpListSummary

An abbreviated version of the [AnycastIpList](API_AnycastIpList.md "API_AnycastIpList.md") structure. Omits the allocated static IP addresses ([AnycastIpList:AnycastIps](API_AnycastIpList.md#cloudfront-Type-AnycastIpList-AnycastIps "API_AnycastIpList.md#cloudfront-Type-AnycastIpList-AnycastIps")).


## Contents





**Arn** 


The Amazon Resource Name (ARN) of the Anycast static IP list.


Type: String


Required: Yes




**Id** 


The ID of the Anycast static IP list.


Type: String


Required: Yes




**IpCount** 


The number of IP addresses in the Anycast static IP list.


Type: Integer


Required: Yes




**LastModifiedTime** 


The last time the Anycast static IP list was modified.


Type: Timestamp


Required: Yes




**Name** 


The name of the Anycast static IP list.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9-_]{1,64}`



Required: Yes




**Status** 


The deployment status of the Anycast static IP list. Valid values: Deployed, Deploying, or Failed.


Type: String


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AnycastIpListSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AnycastIpListSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AnycastIpListSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AnycastIpListSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AnycastIpListSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AnycastIpListSummary")
