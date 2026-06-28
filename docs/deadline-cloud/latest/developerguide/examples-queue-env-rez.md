# Rez queue environment for Deadline Cloud customer-managed fleets

The
[rez\_queue\_env.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/rez_queue_env.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/rez_queue_env.yaml")
queue environment provides the same functionality as the conda queue
environments but for the
[Rez](https://rez.readthedocs.io/ "https://rez.readthedocs.io/") package manager. The
queue environment works in a farm with customer-managed fleets that have
a shared file system for the Rez package repository.

To use this queue environment on a customer-managed fleet, install
Rez on the worker hosts (for example, in your AMI). Modify the
`RezRepositories` default value to point to the shared file
system path of your Rez package repository.

When you submit a job, set the `RezPackages` parameter to
the list of packages the job needs. The queue environment creates and
activates a Rez environment containing the requested packages and their
dependencies before each job runs.
