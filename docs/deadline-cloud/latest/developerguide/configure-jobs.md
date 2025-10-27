# Configure jobs using queue environments

AWS Deadline Cloud uses _queue environments_ to configure the software on your
workers. An environment enables you to perform time-consuming tasks, such as set up and
tear-down, once for all the tasks in a session. It defines the actions to run on a worker when
starting or stopping a session. You can configure an environment for a queue, jobs that run in
the queue, and the individual steps for a job.

You define environments as queue environments or job environments. Create queue environments
with the Deadline Cloud console or with the [deadline:CreateQueueEnvironment](../APIReference/API_CreateQueueEnvironment.md "../APIReference/API_CreateQueueEnvironment.md") operation and define job environments in the job
templates of the jobs you submit. They follow the Open Job Description (OpenJD) specification
for environments. For details, see [<Environment>](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment "https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment") in the OpenJD specification on GitHub.

In addition to a `name` and `description`, each environment contains
two fields that define the environment on the host. They are:

- `script` – The action taken when this environment is run on a
  worker.
- `variables` – A set of environment variable name/value pairs that are
  set when entering the environment.
  You must set at least one of `script` or `variables`.

You can define more than one environment in your job template. Each environment is applied
in the order that they are listed in the template. You can use this to help manage the
complexity of your environments.

The default queue environment for Deadline Cloud uses the conda package manager to load software into
the environment, but you can use other package managers. The default environment defines two
parameters to specify the software that should be loaded. These variables are set by submitters
provided by Deadline Cloud, though you can set them in your own scripts and applications that use the
default environment. They are:

- `CondaPackages` – A space-separated list of conda package match
  specifications to install for the job. For example, the Blender submitter would add
  `blender=3.6` to render frames in Blender 3.6.
- `CondaChannels` – A space-separated list of conda channels to install
  packages from. For service-managed fleets, packages are installed from the
  `deadline-cloud` channel. You can add other channels.

###### Topics

- [Control the job environment with OpenJD queue
  environments](control-the-job-environment.md "control-the-job-environment.md")
- [Provide applications for your jobs](provide-applications.md "provide-applications.md")
