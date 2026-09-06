# Use job environments on Deadline Cloud

The following job bundles supplement the
[Control the job environment with OpenJD queue environments](control-the-job-environment.md "control-the-job-environment.md") section in the developer guide.
Each demonstrates a different way to use
[Open
Job Description environments](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment "https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment") on the GitHub website. The following
bundles are in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples")
repository on the GitHub website:

[job\_env\_vars](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_vars "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_vars")

Sets environment variables through a job environment.

[job\_env\_with\_new\_command](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_with_new_command "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_with_new_command")

Wraps the task command through a job environment.

[job\_env\_daemon\_process](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_daemon_process "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_daemon_process")

Runs a background daemon process alongside the task.

[pip\_self\_contained\_job](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/pip_self_contained_job "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/pip_self_contained_job")

Defines a job environment that creates a Python virtual
environment with `pip` and adds it to the
`PATH` for the job's steps, with no queue environment
required. Runs on any Linux worker with `python3`
available, including Deadline Cloud service-managed fleet workers.

[pip\_package\_job](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/pip_package_job "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/pip_package_job")

Provides the job's Python dependencies through the
[Pip queue environment for Deadline Cloud](examples-queue-env-pip.md "examples-queue-env-pip.md") instead of a job
environment. The job only sets the `PipPackages`
parameter that the queue environment reads. Use this style to
define the pip environment once and share it across many jobs on a
queue.

For more queue-level environment examples, see
[Queue environment examples for Deadline Cloud](examples-queue-environments.md "examples-queue-environments.md").
