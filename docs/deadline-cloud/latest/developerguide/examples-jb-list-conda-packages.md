# List available conda packages on Deadline Cloud

The deadline-cloud-samples repository on the GitHub website includes the
[list\_available\_conda\_packages](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/list_available_conda_packages "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/list_available_conda_packages")
job bundle, which lists all conda packages available in the
`deadline-cloud` channel using
`conda search -c deadline-cloud '*'` and prints the list to the
job log.

For a list of available packages with their major and minor versions,
and recommendations for pinning, see
[Conda
queue environment](../userguide/create-queue-environment.md#conda-queue-environment "../userguide/create-queue-environment.md#conda-queue-environment").
