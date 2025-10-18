# OrganizationStatus

The status of an Amazon Web Services Organization and the accounts within that organization.


## Contents





**AccountStatusList** 


The current service-linked role (SLR) deployment status for an Amazon Web Services Organization's accounts. This will be either `SUCCEEDED` or `IN_PROGRESS`.


Type: Array of [AccountStatus](API_AccountStatus.md "API_AccountStatus.md") objects


Required: No




**OrganizationAwsServiceAccessStatus** 


The status of the organization's AWS service access. This will be `ENABLED` or `DISABLED`.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Required: No




**OrganizationId** 


The ID of an Amazon Web Services Organization.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^o-([0-9a-f]{8,17})$`



Required: No




**SLRDeploymentStatus** 


The status of the SLR deployment for the account. This will be either `SUCCEEDED` or `IN_PROGRESS`.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/OrganizationStatus "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/OrganizationStatus")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/OrganizationStatus "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/OrganizationStatus")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/OrganizationStatus "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/OrganizationStatus")
