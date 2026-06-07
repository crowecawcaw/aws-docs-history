# Use job environments on Deadline Cloud

The following job bundles supplement the
[Control the job environment with OpenJD queue environments](control-the-job-environment.md "control-the-job-environment.md") section in the developer guide.
Each bundle demonstrates a different way to use
[Open
Job Description environments](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment "https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment"):

[job_env_vars](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_vars "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_vars")

Sets environment variables through a job environment.

[job_env_with_new_command](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_with_new_command "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_with_new_command")

Wraps the task command through a job environment.

[job_env_daemon_process](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_daemon_process "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_daemon_process")

Runs a background daemon process alongside the task.

For more queue-level environment examples, see
[Queue environment examples for Deadline Cloud](examples-queue-environments.md "examples-queue-environments.md").
