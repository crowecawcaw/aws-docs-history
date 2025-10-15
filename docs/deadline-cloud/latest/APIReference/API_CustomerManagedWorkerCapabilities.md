# CustomerManagedWorkerCapabilities

The worker capabilities for a customer managed workflow.


## Contents





**cpuArchitectureType** 


The CPU architecture type for the customer managed worker capabilities.


Type: String


Valid Values: `x86_64 | arm64`



Required: Yes




**memoryMiB** 


The memory (MiB).


Type: [MemoryMiBRange](API_MemoryMiBRange.md "API_MemoryMiBRange.md") object


Required: Yes




**osFamily** 


The operating system (OS) family.


Type: String


Valid Values: `WINDOWS | LINUX | MACOS`



Required: Yes




**vCpuCount** 


The vCPU count for the customer manged worker capabilities.


Type: [VCpuCountRange](API_VCpuCountRange.md "API_VCpuCountRange.md") object


Required: Yes




**acceleratorCount** 


The range of the accelerator.


Type: [AcceleratorCountRange](API_AcceleratorCountRange.md "API_AcceleratorCountRange.md") object


Required: No




**acceleratorTotalMemoryMiB** 


The total memory (MiB) for the customer managed worker capabilities.


Type: [AcceleratorTotalMemoryMiBRange](API_AcceleratorTotalMemoryMiBRange.md "API_AcceleratorTotalMemoryMiBRange.md") object


Required: No




**acceleratorTypes** 


The accelerator types for the customer managed worker capabilities.


Type: Array of strings


Valid Values: `gpu`



Required: No




**customAmounts** 


Custom requirement ranges for customer managed worker capabilities.


Type: Array of [FleetAmountCapability](API_FleetAmountCapability.md "API_FleetAmountCapability.md") objects


Array Members: Minimum number of 1 item. Maximum number of 15 items.


Required: No




**customAttributes** 


Custom attributes for the customer manged worker capabilities.


Type: Array of [FleetAttributeCapability](API_FleetAttributeCapability.md "API_FleetAttributeCapability.md") objects


Array Members: Minimum number of 1 item. Maximum number of 15 items.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CustomerManagedWorkerCapabilities "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CustomerManagedWorkerCapabilities")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CustomerManagedWorkerCapabilities "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CustomerManagedWorkerCapabilities")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CustomerManagedWorkerCapabilities "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CustomerManagedWorkerCapabilities")
