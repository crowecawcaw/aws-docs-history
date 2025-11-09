# Supported Devices, Chip Architectures, and Systems

Amazon SageMaker Neo supports the following devices, chip architectures, and operating systems.

## Devices

You can select a device using the dropdown list in the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker") or by
specifying the `TargetDevice` in the output configuration of the
[`CreateCompilationJob`](../APIReference/API_CreateCompilationJob.md "../APIReference/API_CreateCompilationJob.md") API.

You can choose from one of the following edge devices:

| Device List    | System on a Chip (SoC) | Operating System | Architecture | Accelerator         | Compiler Options Example                                                                                                               |
| -------------- | ---------------------- | ---------------- | ------------ | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| aisage         | _None_                 | Linux            | ARM64        | Mali                | _None_                                                                                                                                 |
| amba_cv2       | CV2                    | Arch Linux       | ARM64        | cvflow              | _None_                                                                                                                                 |
| amba_cv22      | CV22                   | Arch Linux       | ARM64        | cvflow              | _None_                                                                                                                                 |
| amba_cv25      | CV25                   | Arch Linux       | ARM64        | cvflow              | _None_                                                                                                                                 |
| coreml         | _None_                 | iOS, macOS       | _None_       | _None_              | `{"class_labels": "imagenet_labels_1000.txt"}`                                                                                         |
| imx8qm         | NXP imx8               | Linux            | ARM64        | _None_              | _None_                                                                                                                                 |
| imx8mplus      | i.MX 8M Plus           | Linux            | ARM64        | NPU                 | _None_                                                                                                                                 |
| jacinto_tda4vm | TDA4VM                 | Linux            | ARM          | TDA4VM              | _None_                                                                                                                                 |
| jetson_nano    | _None_                 | Linux            | ARM64        | NVIDIA              | `{'gpu-code': 'sm_53', 'trt-ver': '5.0.6', 'cuda-ver':<br>'10.0'}`For `TensorFlow2`, `{'JETPACK_VERSION': '4.6', 'gpu_code': 'sm_72'}` |
| jetson_tx1     | _None_                 | Linux            | ARM64        | NVIDIA              | `{'gpu-code': 'sm_53', 'trt-ver': '6.0.1', 'cuda-ver': '10.0'}`                                                                        |
| jetson_tx2     | _None_                 | Linux            | ARM64        | NVIDIA              | `{'gpu-code': 'sm_62', 'trt-ver': '6.0.1', 'cuda-ver': '10.0'}`                                                                        |
| jetson_xavier  | _None_                 | Linux            | ARM64        | NVIDIA              | `{'gpu-code': 'sm_72', 'trt-ver': '5.1.6', 'cuda-ver': '10.0'}`                                                                        |
| qcs605         | _None_                 | Android          | ARM64        | Mali                | `{'ANDROID_PLATFORM': 27}`                                                                                                             |
| qcs603         | _None_                 | Android          | ARM64        | Mali                | `{'ANDROID_PLATFORM': 27}`                                                                                                             |
| rasp3b         | ARM A56                | Linux            | ARM_EABIHF   | _None_              | `{'mattr': ['+neon']}`                                                                                                                 |
| rasp4b         | ARM A72                | _None_           | _None_       | _None_              | _None_                                                                                                                                 |
| rk3288         | _None_                 | Linux            | ARM_EABIHF   | Mali                | _None_                                                                                                                                 |
| rk3399         | _None_                 | Linux            | ARM64        | Mali                | _None_                                                                                                                                 |
| sbe_c          | _None_                 | Linux            | x86_64       | _None_              | `{'mcpu': 'core-avx2'}`                                                                                                                |
| sitara_am57x   | AM57X                  | Linux            | ARM64        | EVE and/or C66x DSP | _None_                                                                                                                                 |
| x86_win32      | _None_                 | Windows 10       | X86_32       | _None_              | _None_                                                                                                                                 |
| x86_win64      | _None_                 | Windows 10       | X86_32       | _None_              | _None_                                                                                                                                 |

For more information about JSON key-value compiler options for
each target device, see the `CompilerOptions` field in the [`OutputConfig` API](../APIReference/API_OutputConfig.md "../APIReference/API_OutputConfig.md") data type.

## Systems and Chip Architectures

The following look-up tables provide information regarding available operating
systems and architectures for Neo model compilation jobs.

Linux

| Accelerator          | X86_64 | X86 | ARM64 | ARM_EABIHF | ARM_EABI |
| -------------------- | ------ | --- | ----- | ---------- | -------- |
| No accelerator (CPU) | Yes    | No  | Yes   | Yes        | Yes      |
| Nvidia GPU           | Yes    | No  | Yes   | No         | No       |
| Intel_Graphics       | Yes    | No  | No    | No         | No       |
| ARM Mali             | No     | No  | Yes   | Yes        | Yes      |

Android

| Accelerator          | X86_64 | X86 | ARM64 | ARM_EABIHF | ARM_EABI |
| -------------------- | ------ | --- | ----- | ---------- | -------- |
| No accelerator (CPU) | Yes    | Yes | Yes   | No         | Yes      |
| Nvidia GPU           | No     | No  | No    | No         | No       |
| Intel_Graphics       | Yes    | Yes | No    | No         | No       |
| ARM Mali             | No     | No  | Yes   | No         | Yes      |

Windows

| Accelerator          | X86_64 | X86 | ARM64 | ARM_EABIHF | ARM_EABI |
| -------------------- | ------ | --- | ----- | ---------- | -------- |
| No accelerator (CPU) | Yes    | Yes | No    | No         | No       |
