# ServiceManagedEc2InstanceCapabilities

The Amazon EC2 instance capabilities.


## Contents





**cpuArchitectureType** 


The CPU architecture type.


Type: String


Valid Values: `x86_64 | arm64`



Required: Yes




**memoryMiB** 


The memory, as MiB, for the Amazon EC2 instance type.


Type: [MemoryMiBRange](API_MemoryMiBRange.md "API_MemoryMiBRange.md") object


Required: Yes




**osFamily** 


The operating system (OS) family.


Type: String


Valid Values: `WINDOWS | LINUX`



Required: Yes




**vCpuCount** 


The amount of vCPU to require for instances in this fleet.


Type: [VCpuCountRange](API_VCpuCountRange.md "API_VCpuCountRange.md") object


Required: Yes




**acceleratorCapabilities** 


Describes the GPU accelerator capabilities required for worker host instances in this
 fleet.


Type: [AcceleratorCapabilities](API_AcceleratorCapabilities.md "API_AcceleratorCapabilities.md") object


Required: No




**allowedInstanceTypes** 


The allowable Amazon EC2 instance types.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 100 items.


Pattern: `[a-zA-Z0-9]+\.[a-zA-Z0-9]+`



Required: No




**customAmounts** 


The custom capability amounts to require for instances in this fleet.


Type: Array of [FleetAmountCapability](API_FleetAmountCapability.md "API_FleetAmountCapability.md") objects


Array Members: Minimum number of 1 item. Maximum number of 15 items.


Required: No




**customAttributes** 


The custom capability attributes to require for instances in this fleet.


Type: Array of [FleetAttributeCapability](API_FleetAttributeCapability.md "API_FleetAttributeCapability.md") objects


Array Members: Minimum number of 1 item. Maximum number of 15 items.


Required: No




**excludedInstanceTypes** 


The instance types to exclude from the fleet.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 100 items.


Pattern: `[a-zA-Z0-9]+\.[a-zA-Z0-9]+`



Required: No




**rootEbsVolume** 


The root EBS volume.


Type: [Ec2EbsVolume](API_Ec2EbsVolume.md "API_Ec2EbsVolume.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ServiceManagedEc2InstanceCapabilities "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ServiceManagedEc2InstanceCapabilities")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ServiceManagedEc2InstanceCapabilities "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ServiceManagedEc2InstanceCapabilities")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ServiceManagedEc2InstanceCapabilities "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ServiceManagedEc2InstanceCapabilities")
