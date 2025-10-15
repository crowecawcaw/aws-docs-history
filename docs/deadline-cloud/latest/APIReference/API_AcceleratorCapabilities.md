# AcceleratorCapabilities

Provides information about the GPU accelerators used for jobs processed by a
 fleet.


## Contents





**selections** 


A list of accelerator capabilities requested for this fleet. Only Amazon Elastic Compute Cloud instances
 that provide these capabilities will be used. For example, if you specify both L4 and T4
 chips, Deadline Cloud will use Amazon EC2 instances that have either the L4 or the T4 chip
 installed.


Type: Array of [AcceleratorSelection](API_AcceleratorSelection.md "API_AcceleratorSelection.md") objects


Required: Yes




**count** 


The number of GPU accelerators specified for worker hosts in this fleet. 


Type: [AcceleratorCountRange](API_AcceleratorCountRange.md "API_AcceleratorCountRange.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AcceleratorCapabilities "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AcceleratorCapabilities")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AcceleratorCapabilities "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AcceleratorCapabilities")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AcceleratorCapabilities "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AcceleratorCapabilities")
