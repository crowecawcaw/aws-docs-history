# LicenseEndpointSummary

The details for a license endpoint.


## Contents





**licenseEndpointId** 


The license endpoint ID.


Type: String


Pattern: `le-[0-9a-f]{32}`



Required: No




**status** 


The status of the license endpoint.


Type: String


Valid Values: `CREATE_IN_PROGRESS | DELETE_IN_PROGRESS | READY | NOT_READY`



Required: No




**statusMessage** 


The status message of the license endpoint.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1024.


Required: No




**vpcId** 


The VPC (virtual private cloud) ID associated with the license endpoint.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 32.


Pattern: `vpc-[\w]{1,120}`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/LicenseEndpointSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/LicenseEndpointSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/LicenseEndpointSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/LicenseEndpointSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/LicenseEndpointSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/LicenseEndpointSummary")
