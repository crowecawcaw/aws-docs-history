# AcceleratorSelection

Describes a specific GPU accelerator required for an Amazon Elastic Compute Cloud worker host.


## Contents





**name** 


The name of the chip used by the GPU accelerator.


If you specify `l4` as the name of the accelerator, you must specify
 `latest` or `grid:r570` as the runtime.


The available GPU accelerators are:



* `t4` - NVIDIA T4 Tensor Core GPU
* `a10g` - NVIDIA A10G Tensor Core GPU
* `l4` - NVIDIA L4 Tensor Core GPU
* `l40s` - NVIDIA L40S Tensor Core GPU

Type: String


Valid Values: `t4 | a10g | l4 | l40s`



Required: Yes




**runtime** 


Specifies the runtime driver to use for the GPU accelerator. You must use the same
 runtime for all GPUs. 


You can choose from the following runtimes:



* `latest` - Use the latest runtime available for the chip. If you
 specify `latest` and a new version of the runtime is released, the new
 version of the runtime is used.
* `grid:r570` - [NVIDIA vGPU software 18](https://docs.nvidia.com/vgpu/18.0/index.html "https://docs.nvidia.com/vgpu/18.0/index.html")
* `grid:r535` - [NVIDIA vGPU software 16](https://docs.nvidia.com/vgpu/16.0/index.html "https://docs.nvidia.com/vgpu/16.0/index.html")

If you don't specify a runtime, Deadline Cloud uses `latest` as the default. However,
 if you have multiple accelerators and specify `latest` for some and leave others
 blank, Deadline Cloud raises an exception.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AcceleratorSelection "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AcceleratorSelection")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AcceleratorSelection "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AcceleratorSelection")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AcceleratorSelection "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AcceleratorSelection")
