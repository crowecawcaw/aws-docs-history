# Use the SageMaker AI generic estimator to extend

pre-built DLC containers

You can customize SageMaker AI prebuilt containers or extend them to handle any additional
functional requirements for your algorithm or model that the prebuilt SageMaker AI Docker image
doesn't support. For an example of how you can extend a pre-built container, see [Extend a
Prebuilt Container](prebuilt-containers-extend.md "prebuilt-containers-extend.md").

To extend a prebuilt container or adapt your own container to use the library, you must
use one of the images listed in [Supported frameworks](distributed-data-parallel-support.md#distributed-data-parallel-supported-frameworks "distributed-data-parallel-support.md#distributed-data-parallel-supported-frameworks").

###### Note

From TensorFlow 2.4.1 and PyTorch 1.8.1, SageMaker AI framework DLCs supports EFA-enabled
instance types. We recommend that you use the DLC images that contain TensorFlow 2.4.1 or
later and PyTorch 1.8.1 or later.

For example, if you use PyTorch, your Dockerfile should contain a `FROM`
statement similar to the following:

```
# SageMaker AI PyTorch image
FROM 763104351884.dkr.ecr.`<aws-region>`.amazonaws.com/pytorch-training:`<image-tag>`

ENV PATH="/opt/ml/code:${PATH}"

# this environment variable is used by the SageMaker AI PyTorch container to determine our user code directory.
ENV SAGEMAKER_SUBMIT_DIRECTORY /opt/ml/code

# /opt/ml and all subdirectories are utilized by SageMaker AI, use the /code subdirectory to store your user code.
COPY `train.py` /opt/ml/code/train.py

# Defines cifar10.py as script entrypoint
ENV SAGEMAKER_PROGRAM `train.py`
```

You can further customize your own Docker container to work with SageMaker AI using the [SageMaker Training toolkit](https://github.com/aws/sagemaker-training-toolkit "https://github.com/aws/sagemaker-training-toolkit") and
the binary file of the SageMaker AI distributed data parallel library. To learn more, see the
instructions in the following section.
