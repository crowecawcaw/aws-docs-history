# Job

configurations

You can have the following additional configurations for each job that you deploy to the
specified targets.

- **Rollout**: Defines how many devices receive the job
  document every minute.
- **Scheduling**: Schedules a job for a future date and
  time in addition to using recurring maintenance windows.
- **Abort**: Cancels a job in cases such as when some
  devices don't receive the job notification, or your devices report failure for their
  job executions.
- **Timeout**: If there isn't a response from your job
  targets within a certain duration after their job executions have started, the job
  can fail.
- **Retry**: Retries the job execution if your device
  reports failure when attempting to complete a job execution, or if your job
  execution times out.
  By using these configurations, you can monitor the status of your job execution and avoid
  a bad update from being sent to an entire fleet.

###### Topics

- [How job configurations work](jobs-configurations-details.md "jobs-configurations-details.md")
- [Specify additional configurations](jobs-configurations-specify.md "jobs-configurations-specify.md")
