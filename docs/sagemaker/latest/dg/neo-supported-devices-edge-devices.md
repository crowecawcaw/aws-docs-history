

# Supported Devices, Chip Architectures, and Systems
<a name="neo-supported-devices-edge-devices"></a>

Amazon SageMaker Neo supports the following devices, chip architectures, and operating systems.

## Devices
<a name="neo-supported-edge-devices"></a>

You can select a device using the dropdown list in the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker) or by specifying the `TargetDevice` in the output configuration of the [`CreateCompilationJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCompilationJob.html) API.

You can choose from one of the following edge devices: 


| Device List | System on a Chip (SoC) | Operating System | Architecture | Accelerator | Compiler Options Example | 
| --- | --- | --- | --- | --- | --- | 
| aisage | None | Linux | ARM64 | Mali | None | 
| amba\_cv2 | CV2 | Arch Linux | ARM64 | cvflow | None | 
| amba\_cv22 | CV22 | Arch Linux | ARM64 | cvflow | None | 
| amba\_cv25 | CV25 | Arch Linux | ARM64 | cvflow | None | 
| coreml | None | iOS, macOS | None | None | {"class\_labels": "imagenet\_labels\_1000.txt"} | 
| imx8qm | NXP imx8 | Linux | ARM64 | None | None | 
| imx8mplus | i.MX 8M Plus | Linux | ARM64 | NPU | None | 
| jacinto\_tda4vm | TDA4VM | Linux | ARM | TDA4VM | None | 
| jetson\_nano | None | Linux | ARM64 | NVIDIA | {'gpu-code': 'sm\_53', 'trt-ver': '5.0.6', 'cuda-ver': '10.0'}For `TensorFlow2`, `{'JETPACK_VERSION': '4.6', 'gpu_code': 'sm_72'}` | 
| jetson\_tx1 | None | Linux | ARM64 | NVIDIA | {'gpu-code': 'sm\_53', 'trt-ver': '6.0.1', 'cuda-ver': '10.0'} | 
| jetson\_tx2 | None | Linux | ARM64 | NVIDIA | {'gpu-code': 'sm\_62', 'trt-ver': '6.0.1', 'cuda-ver': '10.0'} | 
| jetson\_xavier | None | Linux | ARM64 | NVIDIA | {'gpu-code': 'sm\_72', 'trt-ver': '5.1.6', 'cuda-ver': '10.0'} | 
| qcs605 | None | Android | ARM64 | Mali | {'ANDROID\_PLATFORM': 27} | 
| qcs603 | None | Android | ARM64 | Mali | {'ANDROID\_PLATFORM': 27} | 
| rasp3b | ARM A56 | Linux | ARM\_EABIHF | None | {'mattr': ['\+neon']} | 
| rasp4b | ARM A72 | None | None | None | None | 
| rk3288 | None | Linux | ARM\_EABIHF | Mali | None | 
| rk3399 | None | Linux | ARM64 | Mali | None | 
| sbe\_c | None | Linux | x86\_64 | None | {'mcpu': 'core-avx2'} | 
| sitara\_am57x | AM57X | Linux | ARM64 | EVE and/or C66x DSP | None | 
| x86\_win32 | None | Windows 10 | X86\_32 | None | None | 
| x86\_win64 | None | Windows 10 | X86\_32 | None | None | 

For more information about JSON key-value compiler options for each target device, see the `CompilerOptions` field in the [`OutputConfig` API](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OutputConfig.html) data type.

## Systems and Chip Architectures
<a name="neo-supported-edge-granular"></a>

The following look-up tables provide information regarding available operating systems and architectures for Neo model compilation jobs. 

------
#### [ Linux ]


| Accelerator | X86\_64 | X86 | ARM64 | ARM\_EABIHF | ARM\_EABI | 
| --- | --- | --- | --- | --- | --- | 
| No accelerator (CPU) | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | 
| Nvidia GPU | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | 
| Intel\_Graphics | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | 
| ARM Mali | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | 

------
#### [ Android ]


| Accelerator | X86\_64 | X86 | ARM64 | ARM\_EABIHF | ARM\_EABI | 
| --- | --- | --- | --- | --- | --- | 
| No accelerator (CPU) | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | 
| Nvidia GPU | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | 
| Intel\_Graphics | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | 
| ARM Mali | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | 

------
#### [ Windows ]


| Accelerator | X86\_64 | X86 | ARM64 | ARM\_EABIHF | ARM\_EABI | 
| --- | --- | --- | --- | --- | --- | 
| No accelerator (CPU) | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/negative_icon.png) No | 

------