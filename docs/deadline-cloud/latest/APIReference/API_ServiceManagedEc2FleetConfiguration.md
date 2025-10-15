# ServiceManagedEc2FleetConfiguration

The configuration details for a service managed Amazon EC2 fleet.


## Contents





**instanceCapabilities** 


The Amazon EC2 instance capabilities.


Type: [ServiceManagedEc2InstanceCapabilities](API_ServiceManagedEc2InstanceCapabilities.md "API_ServiceManagedEc2InstanceCapabilities.md") object


Required: Yes




**instanceMarketOptions** 


The Amazon EC2 market type.


Type: [ServiceManagedEc2InstanceMarketOptions](API_ServiceManagedEc2InstanceMarketOptions.md "API_ServiceManagedEc2InstanceMarketOptions.md") object


Required: Yes




**storageProfileId** 


The storage profile ID.


Type: String


Pattern: `sp-[0-9a-f]{32}`



Required: No




**vpcConfiguration** 


The VPC configuration details for a service managed Amazon EC2 fleet.


Type: [VpcConfiguration](API_VpcConfiguration.md "API_VpcConfiguration.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ServiceManagedEc2FleetConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ServiceManagedEc2FleetConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ServiceManagedEc2FleetConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ServiceManagedEc2FleetConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ServiceManagedEc2FleetConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ServiceManagedEc2FleetConfiguration")
