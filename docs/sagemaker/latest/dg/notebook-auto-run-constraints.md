# Constraints and considerations

Review the following constraints to ensure your notebook jobs complete successfully.
Studio uses Papermill to run notebooks. You might need to update Jupyter notebooks to align
to Papermill's requirements. There are also restrictions on the content of LCC scripts and
important details to understand regarding VPC configuration.

## JupyterLab version

JupyterLab version 4.0 is supported.

## Installation of packages that

require kernel restart

Papermill does not support calling `pip install` to install packages that
require a kernel restart. In this situation, use `pip install` in an
initialization script. For a package installation that does not require kernel restart, you
can still include `pip install` in the notebook.

## Kernel and language names

registered with Jupyter

Papermill registers a translator for specific kernels and languages. If you bring your
own instance (BYOI), use a standard kernel name as shown in the following snippet:

```
papermill_translators.register("python", PythonTranslator)
papermill_translators.register("R", RTranslator)
papermill_translators.register("scala", ScalaTranslator)
papermill_translators.register("julia", JuliaTranslator)
papermill_translators.register("matlab", MatlabTranslator)
papermill_translators.register(".net-csharp", CSharpTranslator)
papermill_translators.register(".net-fsharp", FSharpTranslator)
papermill_translators.register(".net-powershell", PowershellTranslator)
papermill_translators.register("pysparkkernel", PythonTranslator)
papermill_translators.register("sparkkernel", ScalaTranslator)
papermill_translators.register("sparkrkernel", RTranslator)
papermill_translators.register("bash", BashTranslator)
```

## Parameters and environment

variable limits

**Parameters and environment variable limits.** When you
create your notebook job, it receives the parameters and environment variables you specify.
You can pass up to 100 parameters. Each parameter name can be up to 256 characters long, and
the associated value can be up to 2500 characters long. If you pass environment variables,
you can pass up to 28 variables. The variable name and associated value can be up to 512
characters long. If you need more than 28 environment variables, use additional environment
variables in an initialization script which has no limit on the number of environment
variables you can use.

## Viewing jobs and job

definitions

**Viewing jobs and job definitions.** If you schedule your
notebook job in the Studio UI in the JupyterLab notebook, you can [view your notebook
jobs](view-notebook-jobs.md "view-notebook-jobs.md") and your [notebook job
definitions](view-def-detail-notebook-auto-run.md "view-def-detail-notebook-auto-run.md") in the Studio UI. If you scheduled your notebook job with the
SageMaker Python SDK, you can view your jobs only—the SageMaker Python SDK notebook job step
does not create job definitions. To view your jobs, you also need to supply additional tags
to your notebook job step instance. For details, see [View your notebook jobs in the Studio
UI dashboard](create-notebook-auto-run-sdk.md#create-notebook-auto-run-dash "create-notebook-auto-run-sdk.md#create-notebook-auto-run-dash").

## Image

You need to manage image constraints depending on whether you run notebook jobs in
Studio or the SageMaker Python SDK notebook job step in a pipeline.

### Image constraints for SageMaker AI

Notebook Jobs (Studio)

**Image and kernel support.** The driver that launches
your notebook job assumes the following:

- A base Python runtime environment is installed in the Studio or
  bring-your-own (BYO) images and is the default in the shell.
- The base Python runtime environment includes the Jupyter client with kernelspecs
  properly configured.
- The base Python runtime environment includes the `pip` function so the
  notebook job can install system dependencies.
- For images with multiple environments, your initialization script should switch to
  the proper kernel-specific environment before installing notebook-specific packages.
  You should switch back to the default Python runtime environment, if different from
  the kernel runtime environment, after configuring the kernel Python runtime
  environment.

The driver that launches your notebook job is a bash script, and Bash v4 must be
available at /bin/bash.

**Root privileges on bring-your-own-images (BYOI).** You
must have root privileges on your own Studio images, either as the root user or through
`sudo` access. If you are not a root user but accessing root privileges through
`sudo`, use `1000/100` as the
`UID/GID`.

### Image constraints for SageMaker AI

Python SDK notebook jobs

The notebook job step supports the following images:

- SageMaker Distribution Images listed in [Amazon SageMaker Images Available for Use With
  Studio Classic Notebooks](notebooks-available-images.md "notebooks-available-images.md").
- A custom image based on the SageMaker Distribution images in the previous list. Use a
  [SageMaker Distribution
  image](https://github.com/aws/sagemaker-distribution "https://github.com/aws/sagemaker-distribution") as a base.
- A custom image (BYOI) pre-installed with notebook job dependencies (i.e., [sagemaker-headless-execution-driver](https://pypi.org/project/sagemaker-headless-execution-driver/ "https://pypi.org/project/sagemaker-headless-execution-driver/"). Your image must meet the following
  requirements:
  - The image is pre-installed with notebook job dependencies.
  - A base Python runtime environment is installed and is default in the shell
    environment.
  - The base Python runtime environment includes the Jupyter client with
    kernelspecs properly configured.
  - You have root privileges, either as the root user or through `sudo`
    access. If you are not a root user but accessing root privileges through
    `sudo`, use `1000/100` as the
    `UID/GID`.

## VPC subnets used during job

creation

If you use a VPC, Studio uses your private subnets to create your job. Specify one
to five private subnets (and 1–15 security groups).

If you use a VPC with private subnets, you must choose one of the following options to
ensure the notebook job can connect to dependent services or resources:

- If the job needs access to an AWS service that supports interface VPC endpoints,
  create an endpoint to connect to the service. For a list of services that support
  interface endpoints, see [AWS services
  that integrate with AWS PrivateLink](../../../vpc/latest/privatelink/aws-services-privatelink-support.md "../../../vpc/latest/privatelink/aws-services-privatelink-support.md"). For information about creating an interface
  VPC endpoint, see [Access an AWS service
  using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md"). At minimum, an Amazon S3 VPC endpoint
  gateway must be provided.
- If a notebook job needs access to an AWS service that doesn't support interface
  VPC endpoints or to a resource outside of AWS, create a NAT gateway and configure your
  security groups to allow outbound connections. For information about setting up a NAT
  gateway for your VPC, see _VPC with public and private Subnets
  (NAT)_ in the [Amazon Virtual Private Cloud User
  Guide](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").

## Service limits

Since the notebook job scheduler is built from Pipelines, SageMaker Training, and Amazon EventBridge
services, your notebook jobs are subject to their service-specific quotas. If you exceed
these quotas, you may see error messages related to these services. For example, there are
limits for how many pipelines you can run at one time, and how many rules you can set up for
a single event bus. For more information about SageMaker AI quotas, see [Amazon SageMaker AI Endpoints and Quotas](../../../general/latest/gr/sagemaker.md "../../../general/latest/gr/sagemaker.md"). For more
information about EventBridge quotas, see [Amazon EventBridge Quotas](../../../eventbridge/latest/userguide/eb-quota.md "../../../eventbridge/latest/userguide/eb-quota.md").
