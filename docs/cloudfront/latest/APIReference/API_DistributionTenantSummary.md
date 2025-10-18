# DistributionTenantSummary

A summary of the information about a distribution tenant.


## Contents





**Arn** 


The Amazon Resource Name (ARN) of the distribution tenant.


Type: String


Required: Yes




**CreatedTime** 


The date and time when the distribution tenant was created.


Type: Timestamp


Required: Yes




**DistributionId** 


The identifier for the multi-tenant distribution. For example: `EDFDVBD632BHDS5`.


Type: String


Required: Yes




**Domains** 


The domains associated with the distribution tenant.


Type: Array of [DomainResult](API_DomainResult.md "API_DomainResult.md") objects


Required: Yes




**ETag** 


The current version of the distribution tenant.


Type: String


Required: Yes




**Id** 


The ID of the distribution tenant.


Type: String


Required: Yes




**LastModifiedTime** 


The date and time when the distribution tenant was updated.


Type: Timestamp


Required: Yes




**Name** 


The name of the distribution tenant.


Type: String


Required: Yes




**ConnectionGroupId** 


The ID of the connection group ID for the distribution tenant. If you don't specify a connection group, CloudFront uses the default connection group.


Type: String


Required: No




**Customizations** 


Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and AWS WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.


Type: [Customizations](API_Customizations.md "API_Customizations.md") object


Required: No




**Enabled** 


Indicates whether the distribution tenants are in an enabled state. If disabled, the distribution tenant won't service traffic.


Type: Boolean


Required: No




**Status** 


The status of the distribution tenant.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DistributionTenantSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DistributionTenantSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DistributionTenantSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DistributionTenantSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DistributionTenantSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DistributionTenantSummary")
