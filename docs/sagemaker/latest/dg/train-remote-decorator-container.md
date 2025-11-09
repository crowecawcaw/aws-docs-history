# Container image compatibility

The following table shows a list of SageMaker training images that are compatible with the
@remote decorator.

| Name                                         | Python Version | Image URI<br>• CPU                                                                                                                                                                                                                 | Image URI<br>• GPU                                                                                                                                             |
| -------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Science                                 | 3.7(py37)      | For SageMaker Studio Classic Notebooks only. Python SDK automatically<br>selects the image URI when used as SageMaker Studio Classic Notebook kernel<br>image.                                                                     | For SageMaker Studio Classic Notebooks only. Python SDK automatically<br>selects the image URI when used as SageMaker Studio Classic Notebook kernel<br>image. |
| Data Science 2.0                             | 3.8(py38)      | For SageMaker Studio Classic Notebooks only. Python SDK automatically<br>selects the image URI when used as SageMaker Studio Classic Notebook kernel<br>image.                                                                     | For SageMaker Studio Classic Notebooks only. Python SDK automatically<br>selects the image URI when used as SageMaker Studio Classic Notebook kernel<br>image. |
| Data Science 3.0                             | 3.10(py310)    | For SageMaker Studio Classic Notebooks only. Python SDK automatically<br>selects the image URI when used as SageMaker Studio Classic Notebook kernel<br>image.                                                                     | For SageMaker Studio Classic Notebooks only. Python SDK automatically<br>selects the image URI when used as SageMaker Studio Classic Notebook kernel<br>image. |
| Base Python 2.0                              | 3.8(py38)      | Python SDK selects this image when it detects that development<br>environment is using Python 3.8 runtime. Otherwise Python SDK<br>automatically selects this image when used as SageMaker Studio Classic<br>Notebook kernel image | For SageMaker Studio Classic Notebooks only. Python SDK automatically<br>selects the image URI when used as SageMaker Studio Classic Notebook kernel<br>image. |
| Base Python 3.0                              | 3.10(py310)    | Python SDK selects this image when it detects that development<br>environment is using Python 3.8 runtime. Otherwise Python SDK<br>automatically selects this image when used as SageMaker Studio Classic<br>Notebook kernel image | For SageMaker Studio Classic Notebooks only. Python SDK automatically<br>selects the image URI when used as Studio Classic Notebook kernel<br>image.           |
| DLC-TensorFlow 2.12.0 for SageMaker Training | 3.10(py310)    | 763104351884.dkr.ecr.<region>.amazonaws.com/tensorflow-training:2.12.0-cpu-py310-ubuntu20.04-sagemaker                                                                                                                             | 763104351884.dkr.ecr.<region>.amazonaws.com/tensorflow-training:2.12.0-gpu-py310-cu118-ubuntu20.04-sagemaker                                                   |
| DLC-Tensorflow 2.11.0 for SageMaker training | 3.9(py39)      | 763104351884.dkr.ecr.<region>.amazonaws.com/tensorflow-training:2.11.0-cpu-py39-ubuntu20.04-sagemaker                                                                                                                              | 763104351884.dkr.ecr.<region>.amazonaws.com/tensorflow-training:2.11.0-gpu-py39-cu112-ubuntu20.04-sagemaker                                                    |
| DLC-TensorFlow 2.10.1 for SageMaker training | 3.9(py39)      | 763104351884.dkr.ecr.<region>.amazonaws.com/tensorflow-training:2.10.1-cpu-py39-ubuntu20.04-sagemaker                                                                                                                              | 763104351884.dkr.ecr.<region>.amazonaws.com/tensorflow-training:2.10.1-gpu-py39-cu112-ubuntu20.04-sagemaker                                                    |
| DLC-TensorFlow 2.9.2 for SageMaker training  | 3.9(py39)      | 763104351884.dkr.ecr.<region>.amazonaws.com/tensorflow-training:2.9.2-cpu-py39-ubuntu20.04-sagemaker                                                                                                                               | 763104351884.dkr.ecr.<region>.amazonaws.com/tensorflow-training:2.9.2-gpu-py39-cu112-ubuntu20.04-sagemaker                                                     |
| DLC-TensorFlow 2.8.3 for SageMaker training  | 3.9(py39)      | 763104351884.dkr.ecr.<region>.amazonaws.com/tensorflow-training:2.8.3-cpu-py39-ubuntu20.04-sagemaker                                                                                                                               | 763104351884.dkr.ecr.<region>.amazonaws.com/tensorflow-training:2.8.3-gpu-py39-cu112-ubuntu20.04-sagemaker                                                     |
| DLC-PyTorch 2.0.0 for SageMaker training     | 3.10(py310)    | 763104351884.dkr.ecr.<region>.amazonaws.com/pytorch-training:2.0.0-cpu-py310-ubuntu20.04-sagemaker                                                                                                                                 | 763104351884.dkr.ecr.<region>.amazonaws.com/pytorch-training:2.0.0-gpu-py310-cu118-ubuntu20.04-sagemaker                                                       |
| DLC-PyTorch 1.13.1 for SageMaker training    | 3.9(py39)      | 763104351884.dkr.ecr.<region>.amazonaws.com/pytorch-training:1.13.1-cpu-py39-ubuntu20.04-sagemaker                                                                                                                                 | 763104351884.dkr.ecr.<region>.amazonaws.com/pytorch-training:1.13.1-gpu-py39-cu117-ubuntu20.04-sagemaker                                                       |
| DLC-PyTorch 1.12.1 for SageMaker training    | 3.8(py38)      | 763104351884.dkr.ecr.<region>.amazonaws.com/pytorch-training:1.12.1-cpu-py38-ubuntu20.04-sagemaker                                                                                                                                 | 763104351884.dkr.ecr.<region>.amazonaws.com/pytorch-training:1.12.1-gpu-py38-cu113-ubuntu20.04-sagemaker                                                       |
| DLC-PyTorch 1.11.0 for SageMaker training    | 3.8(py38)      | 763104351884.dkr.ecr.<region>.amazonaws.com/pytorch-training:1.11.0-cpu-py38-ubuntu20.04-sagemaker                                                                                                                                 | 763104351884.dkr.ecr.<region>.amazonaws.com/pytorch-training:1.11.0-gpu-py38-cu113-ubuntu20.04-sagemaker                                                       |
| DLC-MXNet 1.9.0 for SageMaker training       | 3.8(py38)      | 763104351884.dkr.ecr.<region>.amazonaws.com/mxnet-training:1.9.0-cpu-py38-ubuntu20.04-sagemaker                                                                                                                                    | 763104351884.dkr.ecr.<region>.amazonaws.com/mxnet-training:1.9.0-gpu-py38-cu112-ubuntu20.04-sagemaker                                                          |

###### Note

To run jobs locally using AWS Deep Learning Containers (DLC) images, use the
image URIs found in the [DLC documentation](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md"). The DLC images do not support the
`auto_capture` value for dependencies.

Jobs with [SageMaker AI
Distribution in SageMaker Studio](https://github.com/aws/sagemaker-distribution#amazon-sagemaker-studio "https://github.com/aws/sagemaker-distribution#amazon-sagemaker-studio") run in a container as a non-root user
named `sagemaker-user`. This user needs full permission
to access `/opt/ml` and `/tmp`. Grant this
permission by adding `sudo chmod -R 777 /opt/ml /tmp` to the `pre_execution_commands` list,
as shown in the following snippet:

```
@remote(pre_execution_commands=["sudo chmod -R 777 /opt/ml /tmp"])
def func():
    pass
```

You can also run remote functions with your custom images. For compatibility with
remote functions, custom images should be built with Python version 3.7.x-3.10.x. The
following is a minimal Dockerfile example showing you how to use a Docker image with
Python 3.10.

```
FROM python:3.10

#... Rest of the Dockerfile
```

To create `conda` environments in your image and use it to run jobs, set
the environment variable `SAGEMAKER_JOB_CONDA_ENV` to the `conda`
environment name. If your image has the `SAGEMAKER_JOB_CONDA_ENV` value set,
the remote function cannot create a new conda environment during the training job
runtime. Refer to the following Dockerfile example that uses a `conda`
environment with Python version 3.10.

```
FROM continuumio/miniconda3:4.12.0

ENV SHELL=/bin/bash \
    CONDA_DIR=/opt/conda \
    SAGEMAKER_JOB_CONDA_ENV=`sagemaker-job-env`

RUN conda create -n $SAGEMAKER_JOB_CONDA_ENV \
   && conda install -n $SAGEMAKER_JOB_CONDA_ENV python=3.10 -y \
   && conda clean --all -f -y \
```

For SageMaker AI to use [mamba](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html "https://mamba.readthedocs.io/en/latest/user_guide/mamba.html") to
manage your Python virtual environment in the container image, install the [mamba toolkit from miniforge](https://github.com/conda-forge/miniforge "https://github.com/conda-forge/miniforge").
To use mamba, add the following code example to your Dockerfile. Then, SageMaker AI will detect
the `mamba` availability at runtime and use it instead of
`conda`.

```
#Mamba Installation
RUN curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh" \
    && bash Mambaforge-Linux-x86_64.sh -b -p "/opt/conda"  \
    && /opt/conda/bin/conda init bash
```

Using a custom conda channel on an Amazon S3 bucket is not compatible with mamba when using
a remote function. If you choose to use mamba, make sure you are not using a custom
conda channel on Amazon S3. For more information, see the **Prerequisites** section under **Custom conda
repository using Amazon S3**.

The following is a complete Dockerfile example showing how to create a compatible
Docker image.

```
FROM python:3.10

RUN apt-get update -y \
    # Needed for awscli to work
    # See: https://github.com/aws/aws-cli/issues/1957#issuecomment-687455928
    && apt-get install -y groff unzip curl \
    && pip install --upgrade \
        'boto3>1.0<2' \
        'awscli>1.0<2' \
        'ipykernel>6.0.0<7.0.0' \
#Use ipykernel with --sys-prefix flag, so that the absolute path to
    #/usr/local/share/jupyter/kernels/python3/kernel.json python is used
    # in kernelspec.json file
    && python -m ipykernel install --sys-prefix

#Install Mamba
RUN curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh" \
    && bash Mambaforge-Linux-x86_64.sh -b -p "/opt/conda"  \
    && /opt/conda/bin/conda init bash

#cleanup
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf ${HOME}/.cache/pip \
    && rm Mambaforge-Linux-x86_64.sh

ENV SHELL=/bin/bash \
    PATH=$PATH:/opt/conda/bin
```

The resulting image from running the previous Dockerfile example can also be used as
a [SageMaker Studio Classic
kernel image](studio-byoi.md "studio-byoi.md").
