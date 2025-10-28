End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Setting up your AWS IoT Greengrass Version 2 core device

Amazon Lookout for Vision uses AWS IoT Greengrass Version 2 to simplify the deployment of the model component, Amazon Lookout for Vision Edge Agent component, and client application component
to your AWS IoT Greengrass V2 core device. For information about the devices and hardware that you can use, see [AWS IoT Greengrass Version 2 core device requirements](models-devices-setup-requirements.md "models-devices-setup-requirements.md").

## Setting up your core device

Use the following information to set up your core device.

###### To set up your core device

1. Set up your GPU libraries. Don't do this step if you aren't using GPU accelerated inference.
   1. Verify that you have a GPU that supports CUDA. For more information, see [Verify You Have a CUDA-Capable GPU](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#verify-you-have-cuda-enabled-system "https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#verify-you-have-cuda-enabled-system").
   2. Setup CUDA, cuDNN, and TensorRT on your device by doing one of the following:
      - If you are using a Jetson device, install JetPack version 4.4 - 4.6.1. For more information, see
        [JetPack Archive](https://developer.nvidia.com/embedded/jetpack-archive "https://developer.nvidia.com/embedded/jetpack-archive").
      - If you are using x86 based hardware, and your NVIDIA GPU microarchitecture is prior to Ampere (compute capability is less than 8.0),
        do the following:
        1. Set up CUDA version 10.2 by following the instructions at [NVIDIA CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/archive/10.2/cuda-installation-guide-linux/index.html " https://docs.nvidia.com/cuda/archive/10.2/cuda-installation-guide-linux/index.html").
        2. Install cuDNN, by following the instructions at [NVIDIA cuDNN Documentation](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html "https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html").
        3. Set up TensorRT (version 7.1.3 or later, but earlier than 8.0.0) by following the instructions at [NVIDIA TENSORRT DOCUMENTATION](https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html "https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html").

      - If you are using x86 based hardware, and your NVIDIA GPU microarchitecture is Ampere (compute capability is 8.0), do the following:
        1. Set up CUDA (version 11.2) by following the instructions at [NVIDIA CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/archive/11.2.0/cuda-installation-guide-linux/index.html "https://docs.nvidia.com/cuda/archive/11.2.0/cuda-installation-guide-linux/index.html").
        2. Install cuDNN, by following the instructions at [NVIDIA cuDNN Documentation](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html "https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html").
        3. Set up TensorRT (version 8.2.0) by following the instructions at [NVIDIA TENSORRT DOCUMENTATION](https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html "https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html").

2. Install the AWS IoT Greengrass Version 2 core software on your core device. For more information, see
   [Install the AWS IoT Greengrass Core software](../../../greengrass/v2/developerguide/getting-started.md#install-greengrass-v2 "../../../greengrass/v2/developerguide/getting-started.md#install-greengrass-v2") in the _AWS IoT Greengrass Version 2 Developer Guide_.
3. To read from the Amazon S3 bucket that stores the model, attach permission to the IAM role (token
   exchange role) that you create during AWS IoT Greengrass Version 2 setup. For more
   information, see [Allow access to S3 buckets for component artifacts](../../../greengrass/v2/developerguide/device-service-role.md#device-service-role-access-s3-bucket "../../../greengrass/v2/developerguide/device-service-role.md#device-service-role-access-s3-bucket").
4. At the command prompt, enter the folllowing command to install Python and a Python virtual environment onto the core device.

```
sudo apt install python3.8 python3-venv python3.8-venv
```

5. Use the following command to add the Greengrass user to the video group. This lets Greengrass deployed components access the GPU:

```
sudo usermod -a -G video ggc_user
```

6. (Optional) If you want to call Lookout for Vision Edge Agent API from a different user, add the required user to the
   `ggc_group`. This lets the user communicate with the Lookout for Vision Edge Agent over the Unix Domain socket:

```
sudo usermod -a -G ggc_group $(whoami)
```
