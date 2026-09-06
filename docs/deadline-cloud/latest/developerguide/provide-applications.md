# Provide applications for your jobs

You can use a queue environment to load applications to process your jobs. When you create
a service-managed fleet using the Deadline Cloud console, you have the option of creating a queue
environment that uses the conda package manager to load applications.

If you want to use a different package manager, you can create a queue environment for
that manager. For an example using Rez, see [Use a different package manager](#provide-applications-other-package "#provide-applications-other-package").

Deadline Cloud provides a conda channel to load a selection of rendering applications into your
environment. They support the submitters that Deadline Cloud provides for digital content creation
applications.

You can also load software for conda-forge to use in your jobs. The following examples
show job templates using the queue environment provided by Deadline Cloud to load applications before
running the job.

###### Topics

- [Getting an application from a conda channel](#provide-applications-get-application "#provide-applications-get-application")
- [Use a different package manager](#provide-applications-other-package "#provide-applications-other-package")
- [Use pip for Python-only packages](#provide-applications-pip "#provide-applications-pip")

## Getting an application from a conda channel

You can create a custom queue environment for your Deadline Cloud workers that installs the
software of your choice. This example queue environment has the same behavior as the
environment used by the console for service-managed fleets. It runs conda directly to create
the environment.

The environment creates a new conda virtual environment for every Deadline Cloud session that
runs on a worker, and then deletes the environment when it is done.

Conda caches the downloaded packages so that they don't need to be downloaded again, but
each session must link all of the packages into the environment.

The environment defines three scripts that run when Deadline Cloud starts a session on a worker.
The first script runs when the `onEnter` action is called. It calls the other two
to set up environment variables. When the script finishes running, the conda environment is
available with all of the specified environment variables set.

For the latest version of the example, see [conda\_queue\_env\_from\_console.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_from_console.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_from_console.yaml") in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline") repository on the GitHub website.

If you want to use an application that is not available in the conda channel, you
can create a conda channel in Amazon S3 and then build your own packages for that application. See
[Create a conda channel using S3](configure-jobs-s3-channel.md "configure-jobs-s3-channel.md") to learn more.

### Get open source libraries from conda-forge

This section describes how to use open source libraries from the `conda-forge` channel.
The following example is a job template that uses the `polars` Python package.

The job sets the `CondaPackages` and `CondaChannels` parameters
defined in the queue environment that tell Deadline Cloud where to get the package.

The section of the job template that sets the parameters is:

```
- name: CondaPackages
  description: A list of conda packages to install. The job expects a Queue Environment to handle this.
  type: STRING
  default: polars
- name: CondaChannels
  description: A list of conda channels to get packages from. The job expects a Queue Environment to handle this.
  type: STRING
  default: conda-forge
```

For the latest version of the complete example job template, see [stage\_1\_self\_contained\_template/template.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/job_bundles/job_dev_progression/stage_1_self_contained_template/template.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/job_bundles/job_dev_progression/stage_1_self_contained_template/template.yaml") on the GitHub website. For the latest version of the
queue environment that loads the conda packages, see [conda\_queue\_env\_from\_console.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_from_console.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_from_console.yaml") in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline") repository on the GitHub website.

### Get Blender from the deadline-cloud channel

The following example shows a job template that gets Blender from the
`deadline-cloud` conda channel. This channel supports the submitters that
Deadline Cloud provides for digital content creation software, though you can use the same channel
to load software for your own use.

For a list of the software provided by the `deadline-cloud` channel, see
[Default queue environment](../userguide/create-queue-environment.md#conda-queue-environment "../userguide/create-queue-environment.md#conda-queue-environment") in the _AWS Deadline Cloud User
Guide_.

This job sets the `CondaPackages` parameter defined in the queue
environment to tell Deadline Cloud to load Blender into the environment.

The section of the job template that sets the parameter is:

```
- name: CondaPackages
  type: STRING
  userInterface:
    control: LINE_EDIT
    label: Conda Packages
    groupLabel: Software Environment
  default: blender
  description: >
    Tells the queue environment to install Blender from the deadline-cloud conda channel.
```

For the latest version of the complete example job template, see [blender\_render/template.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/job_bundles/blender_render/template.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/job_bundles/blender_render/template.yaml") on the GitHub website. For the latest version of the queue environment
that loads the conda packages, see [conda\_queue\_env\_from\_console.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_from_console.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_from_console.yaml") in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline") repository on the GitHub website.

## Use a different package manager

The default package manager for Deadline Cloud is conda. If you need to use a different package
manager, such as Rez, you can create a custom queue environment that contains scripts that
use your package manager instead.

This example queue environment provides the same behavior as the environment used by the
console for service-managed fleets. It replaces the conda package manager with Rez.

The environment defines three scripts that run when Deadline Cloud starts a session on a worker.
The first script runs when the `onEnter` action is called. It calls the other two
to set up environment variables. When the script finishes running, the Rez environment is
available with all of the specified environment variables set.

The example assumes that you have a customer-managed fleet that uses a shared file
system for the Rez packages.

For the latest version of the example, see [rez\_queue\_env.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/rez_queue_env.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/rez_queue_env.yaml") in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline") repository on the GitHub website.

## Use pip for Python-only packages

If the applications or libraries your jobs need are pure Python packages available on
PyPI, you can use pip and the Python standard library `venv` module instead of
conda or Rez. This approach works well when a package isn't published to a
conda channel, or when you want a smaller virtual environment than conda creates. Unlike
conda and Rez, pip and `venv` are included with Python itself, so
worker hosts only need a `python3` interpreter on the `PATH`. Deadline Cloud
service-managed fleets provide one.

The [Pip queue environment for Deadline Cloud](examples-queue-env-pip.md "examples-queue-env-pip.md") creates a Python virtual environment in the
session working directory when a job sets the `PipPackages` parameter, installs
the requested packages into it with pip, and activates it so that the job's steps run with
those packages available. Because the environment is created in the session working
directory, Deadline Cloud cleans it up automatically when the session ends, and you don't need to
write cleanup logic of your own. If a job doesn't set `PipPackages`, the queue
environment does nothing, so you can add it to a queue that also runs jobs that don't use
it.

To install packages from a private index such as an [AWS CodeArtifact](../../../codeartifact/latest/ug/welcome.md "../../../codeartifact/latest/ug/welcome.md") repository instead of the
public PyPI index, set the `PipIndexUrl` and `PipExtraIndexUrls`
parameters that the queue environment provides.

If you'd rather not configure a queue environment, you can define the same pip
environment inline in a job bundle instead. For an example of each approach, see the
[pip\_package\_job](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/pip_package_job "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/pip_package_job") and [pip\_self\_contained\_job](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/pip_self_contained_job "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/pip_self_contained_job") job bundles in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline") repository on the GitHub website.

For production queues, pin package versions in the `PipPackages` parameter
value instead of installing the latest release each time. Version pinning gives you
reproducible environments and avoids unexpected breakages when a package publishes a new
version. If a job depends on matching submitter and adaptor versions, pin both to the same
release.

If your customer-managed fleet workers run jobs for more than one digital content
creation (DCC) application, and you install Deadline Cloud adaptors with pip, install each adaptor
into its own virtual environment. Installing multiple adaptors together in the same virtual
environment can cause pip to resolve a shared dependency to a version that conflicts with one
of the adaptors.

Worker hosts need network access to a package source, such as PyPI or a private mirror,
to install packages when a session starts. If your customer-managed fleet workers run in a
private subnet without internet access, use a VPC endpoint to your package source, a private
pip mirror, or install the packages into your worker AMI instead.

The following table summarizes the trade-offs of each package manager to help you choose
which one to use.

| Package manager | Best for                                                               | Trade-offs                                                                                    |
| --------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Conda (default) | DCC applications, complex native dependencies, cross-platform packages | Larger environments; packages must be published to a conda channel                            |
| Rez             | Studio pipelines with existing Rez infrastructure                      | Requires Rez installed on worker hosts and a shared file system for<br>the package repository |
| Pip             | Python-only packages, PyPI-hosted libraries, lightweight installs      | Limited to Python packages; no native dependency resolution                                   |

After you choose a queue environment, attach it to your queue. You can either add the YAML
template from the **Queue environments** tab for your queue in the Deadline Cloud
console, or use the [deadline:CreateQueueEnvironment](../APIReference/API_CreateQueueEnvironment.md "../APIReference/API_CreateQueueEnvironment.md") operation. For console instructions, see [Create a queue environment](../userguide/create-queue-environment.md "../userguide/create-queue-environment.md") in the _AWS Deadline Cloud User Guide_. To
attach a queue environment with the AWS CLI:

```
aws deadline create-queue-environment \
    --farm-id `FARM_ID` \
    --queue-id `QUEUE_ID` \
    --priority 1 \
    --template-type YAML \
    --template file://`queue-environment.yaml`
```
