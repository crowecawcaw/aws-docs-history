# DomainConflict

Contains information about the domain conflict. Use this information to determine the affected domain, the related resource, and the affected AWS account.


## Contents





**AccountId** 


The ID of the AWS account for the domain conflict.


Type: String


Required: Yes




**Domain** 


The domain used to find existing conflicts for domain configurations.


Type: String


Required: Yes




**ResourceId** 


The ID of the resource that has a domain conflict.


Type: String


Required: Yes




**ResourceType** 


The CloudFront resource type that has a domain conflict.


Type: String


Valid Values: `distribution | distribution-tenant`



Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DomainConflict "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DomainConflict")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DomainConflict "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DomainConflict")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DomainConflict "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DomainConflict")
