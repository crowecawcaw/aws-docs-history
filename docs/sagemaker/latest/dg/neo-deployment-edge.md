# Deploy Models

You can deploy the compute module to resource-constrained edge devices
by: downloading the compiled model from Amazon S3 to your device and using
[DLR](https://github.com/neo-ai/neo-ai-dlr "https://github.com/neo-ai/neo-ai-dlr"), or
you can use [AWS IoT Greengrass](../../../greengrass/latest/developerguide/what-is-gg.md "../../../greengrass/latest/developerguide/what-is-gg.md").

Before moving on, make sure your edge device must be supported by
SageMaker Neo. See,
[Supported Frameworks, Devices, Systems, and Architectures](neo-supported-devices-edge.md "neo-supported-devices-edge.md")
to find out what edge devices are supported. Make sure that you specified your
target edge device when you submitted the
compilation job, see
[Use Neo
to Compile a Model](neo-job-compilation.md "neo-job-compilation.md").

## Deploy a Compiled Model (DLR)

[DLR](https://github.com/neo-ai/neo-ai-dlr "https://github.com/neo-ai/neo-ai-dlr") is a compact,
common runtime for deep learning models and decision tree models. DLR uses the
[TVM](https://github.com/neo-ai/tvm "https://github.com/neo-ai/tvm") runtime,
[Treelite](https://treelite.readthedocs.io/en/latest/install.html "https://treelite.readthedocs.io/en/latest/install.html")
runtime, NVIDIA TensorRT™, and can include other
hardware-specific runtimes. DLR provides unified Python/C++ APIs for
loading and running compiled models on various devices.

You can install latest release of DLR package using the following pip command:

```
pip install dlr
```

For installation of DLR on GPU targets or non-x86 edge devices, please refer
to [Releases](https://github.com/neo-ai/neo-ai-dlr/releases "https://github.com/neo-ai/neo-ai-dlr/releases")
for prebuilt binaries, or [Installing
DLR](https://neo-ai-dlr.readthedocs.io/en/latest/install.html "https://neo-ai-dlr.readthedocs.io/en/latest/install.html") for building DLR from source. For example, to install DLR for
Raspberry Pi 3, you can use:

```
pip install https://neo-ai-dlr-release.s3-us-west-2.amazonaws.com/v1.3.0/pi-armv7l-raspbian4.14.71-glibc2_24-libstdcpp3_4/dlr-1.3.0-py3-none-any.whl
```

## Deploy a Model (AWS

IoT Greengrass)

[AWS IoT Greengrass](../../../greengrass/latest/developerguide/what-is-gg.md "../../../greengrass/latest/developerguide/what-is-gg.md") extends cloud capabilities to local devices. It
enables devices to collect and analyze data closer to the source of information,
react autonomously to local events, and communicate securely with each other on
local networks. With AWS IoT Greengrass, you can perform machine learning inference
at the edge on locally generated data using cloud-trained models. Currently, you can
deploy models on to all AWS IoT Greengrass devices based on ARM Cortex-A, Intel
Atom, and Nvidia Jetson series processors. For more information on deploying a
Lambda inference application to perform machine learning inferences with AWS IoT
Greengrass, see [How to configure optimized machine learning inference using the AWS Management Console](../../../greengrass/latest/developerguide/ml-dlc-console.md "../../../greengrass/latest/developerguide/ml-dlc-console.md").
