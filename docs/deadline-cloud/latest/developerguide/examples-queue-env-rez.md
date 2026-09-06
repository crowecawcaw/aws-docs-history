

# Rez queue environment for Deadline Cloud customer-managed fleets
<a name="examples-queue-env-rez"></a>

The [rez\_queue\_env.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/rez_queue_env.yaml) queue environment on the GitHub website provides the same functionality as the conda queue environments but for the [Rez](https://rez.readthedocs.io/) package manager on the Rez website. The queue environment works in a farm with customer-managed fleets that have a shared file system for the Rez package repository.

To use this queue environment on a customer-managed fleet, install Rez on the worker hosts (for example, in your AMI). Modify the `RezRepositories` default value to point to the shared file system path of your Rez package repository.

When you submit a job, set the `RezPackages` parameter to the list of packages the job needs. The queue environment creates and activates a Rez environment containing the requested packages and their dependencies before each job runs.

The [rez\_shim](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/queue_environments/rez_shim) variant on the GitHub website applies a resolved Rez context to each task by wrapping its command instead of replaying environment variables. Choose it if your Rez packages configure software with anything other than plain environment variables, such as an `alias` for a launcher, a shell function, or a `PATH` entry that must shadow a system binary. Job templates keep calling tools by bare name, so job bundles need no changes. If your packages only set variables, the simpler `rez_queue_env.yaml` works and needs no extra pieces.