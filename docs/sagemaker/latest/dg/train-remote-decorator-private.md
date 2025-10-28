# Private repository for runtime

dependencies

You can use pre-execution commands or script to configure a dependency manager like
pip or conda in your job environment. To achieve network isolation, use either of these
options to redirect your dependency managers to access your private repositories and run
remote functions within a VPC. The pre-execution commands or script will run before your
remote function runs. You can define them with the @remote decorator, the
`RemoteExecutor` API, or within a configuration file.

The following sections show you how to access a private Python Package Index (PyPI)
repository managed with AWS CodeArtifact. The sections also show how to access a custom conda
channel hosted on Amazon Simple Storage Service (Amazon S3).

## How to use a custom PyPI

repository managed with AWS CodeArtifact

To use CodeArtifact to manage a custom PyPI repository, the following prerequisites are
required:

- Your private PyPI repository should already have been created. You can
  utilize AWS CodeArtifact to create and manage your private package repositories. To
  learn more about CodeArtifact, see the [CodeArtifact User
  Guide](../../../codeartifact/latest/ug/welcome.md "../../../codeartifact/latest/ug/welcome.md").
- Your VPC should have access to your CodeArtifact repository. To allow a
  connection from your VPC to your CodeArtifact repository, you must do the
  following:
  - [Create
    VPC endpoints for CodeArtifact](../../../codeartifact/latest/ug/create-vpc-endpoints.md "../../../codeartifact/latest/ug/create-vpc-endpoints.md").
  - [Create an Amazon S3 gateway endpoint](../../../codeartifact/latest/ug/create-s3-gateway-endpoint.md "../../../codeartifact/latest/ug/create-s3-gateway-endpoint.md") for your VPC, which
    allows CodeArtifact to store package assets.

The following pre-execution command example shows how to configure pip in the SageMaker AI
training job to point to your CodeArtifact repository. For more information, see [Configure and use pip with CodeArtifact](../../../codeartifact/latest/ug/python-configure-pip.md "../../../codeartifact/latest/ug/python-configure-pip.md").

```
# use a requirements.txt file to import dependencies
@remote(
    instance_type="`ml.m5.large`"
    image_uri = "`my_base_python:latest`",
    dependencies = './requirements.txt',
    pre_execution_commands=[
        "aws codeartifact login --tool pip --domain `my-org` --domain-owner <`000000000000`> --repository `my-codeartifact-python-repo` --endpoint-url `https://vpce-xxxxx.api.codeartifact.us-east-1.vpce.amazonaws.com`"
    ]
)
def matrix_multiply(a, b):
    return np.matmul(a, b)
```

## How to use a custom conda

channel hosted on Amazon S3

To use Amazon S3 to manage a custom conda repository, the following prerequisites are
required:

- Your private conda channel must already be set up in your Amazon S3 bucket, and
  all dependent packages must be indexed and uploaded to your Amazon S3 bucket. For
  instructions on how to index your conda packages, see [Creating custom channels](https://conda.io/projects/conda/en/latest/user-guide/tasks/create-custom-channels.html "https://conda.io/projects/conda/en/latest/user-guide/tasks/create-custom-channels.html").
- Your VPC should have access to the Amazon S3 bucket. For more information, see
  [Endpoints for
  Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md "../../../vpc/latest/userguide/vpc-endpoints-s3.md").
- The base conda environment in your job image should have
  `boto3` installed. To check your environment, enter the
  following in your Anaconda prompt to check that `boto3` appears
  in the resulting generated list.

```
conda list -n base
```

- You job image should be installed with conda, not [mamba](https://mamba.readthedocs.io/en/latest/installation.html "https://mamba.readthedocs.io/en/latest/installation.html"). To check your environment, ensure that the previous code
  prompt does not return `mamba`.

The following pre-execution commands example shows how to configure conda in the
SageMaker training job to point to your private channel on Amazon S3 The pre-execution
commands removes the defaults channel and adds custom channels to a
`.condarc` conda configuration file.

```
# specify your dependencies inside a conda yaml file
@remote(
    instance_type="`ml.m5.large`"
    image_uri = "`my_base_python:latest`",
    dependencies = "./environment.yml",
    pre_execution_commands=[
        "conda config --remove channels 'defaults'"
        "conda config --add channels 's3://my_bucket/my-conda-repository/conda-forge/'",
        "conda config --add channels 's3://my_bucket/my-conda-repository/main/'"
    ]
)
def matrix_multiply(a, b):
    return np.matmul(a, b)
```
