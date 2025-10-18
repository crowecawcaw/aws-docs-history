# DistributionTenant

The distribution tenant.


## Contents





**Arn** 


The Amazon Resource Name (ARN) of the distribution tenant.


Type: String


Required: No




**ConnectionGroupId** 


The ID of the connection group for the distribution tenant. If you don't specify a connection group, CloudFront uses the default connection group.


Type: String


Required: No




**CreatedTime** 


The date and time when the distribution tenant was created.


Type: Timestamp


Required: No




**Customizations** 


Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and AWS WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.


Type: [Customizations](API_Customizations.md "API_Customizations.md") object


Required: No




**DistributionId** 


The ID of the multi-tenant distribution.


Type: String


Required: No




**Domains** 


The domains associated with the distribution tenant.


Type: Array of [DomainResult](API_DomainResult.md "API_DomainResult.md") objects


Required: No




**Enabled** 


Indicates whether the distribution tenant is in an enabled state. If disabled, the distribution tenant won't serve traffic.


Type: Boolean


Required: No




**Id** 


The ID of the distribution tenant.


Type: String


Required: No




**LastModifiedTime** 


The date and time when the distribution tenant was updated.


Type: Timestamp


Required: No




**Name** 


The name of the distribution tenant.


Type: String


Required: No




**Parameters** 


A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects


Required: No




**Status** 


The status of the distribution tenant.


Type: String


Required: No




**Tags** 


A complex type that contains zero or more `Tag` elements.


Type: [Tags](API_Tags.md "API_Tags.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DistributionTenant "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DistributionTenant")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DistributionTenant "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DistributionTenant")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DistributionTenant "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DistributionTenant")
