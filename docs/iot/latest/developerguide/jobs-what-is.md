# What is AWS IoT Jobs?

Use AWS IoT Jobs to define a set of remote operations that can be sent to and run on one
or more devices connected to AWS IoT.

To create jobs, first define a _job document_ that contains a list
of instructions describing operations that the device must perform remotely. To perform
these operations, specify a list of _targets_, which are individual
things, [thing groups](thing-groups.md "thing-groups.md"), or both. The job document and
targets together constitute a _deployment_.

Each deployment can have additional configurations:

- **Rollout**: This configuration defines how many
  devices receive the job document every minute.
- **Abort**: If a certain number of devices don't
  receive the job notification, use this configuration to cancel the job. This
  avoids sending a bad update to an entire fleet.
- **Timeout**: If a response isn't received from
  your job targets within a certain duration, the job can fail. You can track the
  job that's running on these devices.
- **Retry**: If a device reports failure or a job
  times out, you can use AWS IoT Jobs to resend the job document to the device
  automatically.
- **Scheduling**: This configuration enables you to
  schedule a job for a future date and time. It also enables you to create
  recurring maintenance windows that update devices during predefined, low-traffic
  periods.
  AWS IoT Jobs sends a message to inform the targets that a job is available. The target
  starts the _execution_ of the job by downloading the job document,
  performing the operations it specifies, and reporting its progress to AWS IoT. You can
  track the progress of a job for a specific target or for all targets by running commands
  that are provided by AWS IoT Jobs. When a job starts, it has a status of _In progress_. The devices then report incremental updates
  while displaying this status until the job succeeds, fails, or times out.

The following topics describe some key concepts of jobs and the lifecycle of jobs and
job executions.

###### Topics

- [Jobs key concepts](key-concepts-jobs.md "key-concepts-jobs.md")
- [Jobs and job execution states](iot-jobs-lifecycle.md "iot-jobs-lifecycle.md")
