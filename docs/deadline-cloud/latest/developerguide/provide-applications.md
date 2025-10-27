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

- [Getting an application from a conda
  channel](#provide-applications-get-application "#provide-applications-get-application")
- [Use a different package manager](#provide-applications-other-package "#provide-applications-other-package")

## Getting an application from a conda

channel

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

For the latest version of the example, see [conda_queue_env_console_equivalent.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_console_equivalent.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_console_equivalent.yaml") in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline") repository on GitHub.

If the you want to use an application that is not available in the conda channel, you
can create a conda channel in Amazon S3 and then build your own packages for that application. See
[Create a conda channel using S3](configure-jobs-s3-channel.md "configure-jobs-s3-channel.md") to learn more.

### Get open source libraries from

conda-forge

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

For the latest version of the complete example job template, see [stage_1_self_contained_template/template.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/job_bundles/job_dev_progression/stage_1_self_contained_template/template.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/job_bundles/job_dev_progression/stage_1_self_contained_template/template.yaml"). For the latest version of the
queue environment that loads the conda packages, see [conda_queue_env_console_equivalent.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_console_equivalent.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_console_equivalent.yaml") in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline") repository on GitHub.

### Get Blender from the deadline-cloud

channel

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

For the latest version of the complete example job template, see [blender_render/template.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/job_bundles/blender_render/template.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/job_bundles/blender_render/template.yaml"). For the latest version of the queue environment
that loads the conda packages, see [conda_queue_env_console_equivalent.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_console_equivalent.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_console_equivalent.yaml") in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline") repository on GitHub.

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

For the latest version of the example, see [rez_queue_env.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/rez_queue_env.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/rez_queue_env.yaml") in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline") repository on GitHub.
