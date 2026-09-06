# Inline conda queue environments for Deadline Cloud customer-managed fleets

The samples repository on the GitHub website includes the following
inline conda queue environments that run conda directly instead of using the
`conda-queue-env-enter` command:

[conda\_queue\_env\_inline.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_inline.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_inline.yaml")

Has nearly the same behavior as the console conda queue
environment but runs conda directly. The behavior is to create a
new conda virtual environment for every Open Job Description
session that runs on a worker host, then delete the environment when
the session completes. Conda keeps a cache of downloaded packages so
it doesn't repeatedly re-download applications, but each session
has the overhead of linking packages into the virtual environment.

Unlike the console queue environment, which uses
`strict` channel priority, this inline queue environment
uses `flexible` channel priority.

[conda\_queue\_env\_inline\_improved\_caching.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_inline_improved_caching.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_inline_improved_caching.yaml")

Extends the inline conda queue environment with a mechanism to
reuse conda virtual environments across multiple jobs. The default
environment name uses the hash of the conda channels and packages,
or you can explicitly set the name in the job. A parameter controls
how long to use an environment before running a package update, so
that activating a reused environment usually takes seconds.

To use these queue environments on customer-managed fleets, install
conda on the worker hosts (for example, in your AMI) and configure
`conda activate` to work in non-interactive bash shells. The
samples
[README](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/README.md "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/README.md")
on the GitHub website includes example setup scripts for Amazon Linux 2023,
Ubuntu, and Windows.
