# How logging works for sensitive data

discovery jobs

When you start running sensitive data discovery jobs, Amazon Macie automatically creates and
configures the appropriate resources in Amazon CloudWatch Logs to log events for all of your jobs.
Macie then publishes event data to those resources automatically when your jobs run. The
permissions policy for the Macie [service-linked
role](service-linked-roles.md "service-linked-roles.md") for your account allows Macie to perform these tasks on your behalf. You
don't need to take any steps to create or configure resources in CloudWatch Logs to log event data
for your jobs.

In CloudWatch Logs, logs are organized into _log groups_. Each
log group contains _log streams_. Each log stream contains
_log events_. The general purpose of each of these
resources is as follows:

- A _log group_ is a collection of log streams that
  share the same retention, monitoring, and access control settings—for example,
  the collection of logs for all of your sensitive data discovery jobs.
- A _log stream_ is a sequence of log events that
  share the same source—for example, an individual sensitive data discovery
  job.
- A _log event_ is a record of an activity that was
  recorded by an application or resource—for example, an individual event that
  Macie recorded and published for a particular sensitive data discovery job.
  Macie publishes events for all of your sensitive data discovery jobs to one log group. Each
  job has a unique log stream in that log group. The log group has the following prefix
  and name:

`/aws/macie/classificationjobs`

If this log group already exists, Macie uses it to store log events for your jobs. This can
be helpful if your organization uses automated configuration, such as [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md"), to create log groups with predefined retention periods,
encryption settings, tags, metric filters, and so on, for job events.

If this log group doesn't exist, Macie creates it with the default settings that CloudWatch Logs uses
for new log groups. The settings include a log retention period of **Never
Expire**, which means that CloudWatch Logs stores the logs indefinitely. You can
change the retention period for the log group. To learn how, see [Working
with log groups and log streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the _Amazon CloudWatch Logs
User Guide_.

Within this log group, Macie creates a unique log stream for each job that you run, the
first time that the job runs. The name of the log stream is the unique identifier for
the job, such as `85a55dc0fa6ed0be5939d0408example`, in the following
format:

`/aws/macie/classificationjobs/85a55dc0fa6ed0be5939d0408example`

Each log stream contains all the log events that Macie recorded and published for the
corresponding job. For periodic jobs, this includes events for all of the job's runs. If
you delete the log stream for a periodic job, Macie creates the stream again the next time
that the job runs. If you delete the log stream for a one-time job, you can't restore
it.

Note that logging is enabled by default for all of your jobs. You can't disable it or
otherwise prevent Macie from publishing job events to CloudWatch Logs. If you don't want to store the
logs, you can reduce the retention period for the log group to as little as one day. At the
end of the retention period, CloudWatch Logs automatically deletes expired event data from the log
group.
