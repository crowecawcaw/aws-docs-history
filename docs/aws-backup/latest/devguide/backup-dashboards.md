# AWS Backup console dashboards

###### Note

The jobs dashboard is available in all Regions where AWS Backup Audit Manager is supported.
See [Feature availability by AWS Region](backup-feature-availability.md#features-by-region "backup-feature-availability.md#features-by-region") for those
Regions. All other Regions will be able to access the [CloudWatch Dashboard](cloudwatch.md#cloudwatch-dashboard "cloudwatch.md#cloudwatch-dashboard").

###### Topics

- [Backup dashboards overview](#backup-dashboards-overview "#backup-dashboards-overview")
- [Viewing the jobs dashboard](#backup-dashboards-viewing "#backup-dashboards-viewing")
- [Reasons for problematic jobs](#problematic-reasons "#problematic-reasons")
- [Obtaining dashboard data through AWS CLI](#dashboard-data-cli "#dashboard-data-cli")

## Backup dashboards overview

AWS Backup provides a Jobs dashboard in the console to help you monitor the health of your
backup, copy, and restore jobs. The same data that is visually displayed in the console can
be retrieved in the command line through AWS CLI.

The jobs dashboard can be used to identify issues with backup, copy, and restore jobs
through organization level or member account monitoring. With this information, you can
identify and diagnose events and possible issues to help ensure fidelity in your
activities.

The jobs dashboard can display two timeframes. By default, data from the latest 14 days
are displayed, but you can change the view to show the latest 7 days. If you change the
timeframe, the data will update to reflect to new time interval.

Note the dashboard displays data until the most recent 0:00 UTC; that is, the current
day's data is not included. The dashboard updates daily during approximately 1:30 - 2:30
UTC.

## Viewing the jobs dashboard

To view the jobs dashboard, [log into
the AWS Backup console](https://console.aws.amazon.com/backup/ "https://console.aws.amazon.com/backup/") and select **Jobs dashboards** in the left
navigation bar.

On the jobs dashboard page, you can select from the backup, copy, or restore jobs
tab.

The jobs dashboard overview displays the aggregated view over the specified timeframe
for job activity, including completed, completed with issues, expired, and failed jobs. By
default, data from the latest 14 days are displayed, but you can change the view to show 7
days.

###### Note

`Completed with issues` is a status of a job displayed in the console that
denotes a completed job with a status message.

### Job health

The line chart displays the successful and unsuccessful jobs rate lines over time. The
successful rate line shows an aggregation of completed and completed with issues jobs. The
unsuccessful rate line shows the sum of failed and expired jobs according to the specified
time range.

Jobs in a non-completed or non-failed state (jobs with a status of created, pending,
running, aborted, aborting, or partial) are not included; percentage totals may not equal
100%.

### Job status over time

With the bar chart, you can generate a custom bar chart that shows the number of jobs
in each category (Completed, Complete with issues, Failed, and Expired), distributed by
days.

With the dropdown menus, choose the status(es), resource types, and AWS Regions you
want to see in the chart. If you want to explore your selection further, select
**View jobs** to see a pre-filtered portion of the jobs/cross-account
monitoring page.

You can hover the mouse over a bar to display a popover that shows detailed job data
for the selected date.

### Problematic jobs

A **problematic** job is a job that has the status Failed, Expired,
or Completed with issues. Each chart displays the corresponding metric that contains
either the accounts, resource types, or top reasons that contain the highest number of
problematic jobs.

The default display sorts the dashboard widget by the specified metric in descending
order, starting with the metric with the highest number of problematic jobs that belong to
the metric.

The top problematic accounts display will only be visible in accounts that have access
through Organizations, such as administrative accounts and delegated administrator accounts. If
visible, you can hover over an account to display the number of problematic jobs that
belong to the chosen account.

You can select a bar within the graph to open a popup window. In this window, you can
select a job status to open a jobs/cross-account monitoring table filtered by the status
selected.

## Reasons for problematic jobs

The **Top problematic reasons** widget shows the message code category
to which error messages belong. However, the category might not explain the issues a job
experiences. Expand the message code categories below to see more details about the specific
messages or errors your jobs could be encountering. All error messages not belonging to the
message code categories below will fall under "MISCELLANEOUS".

- "Windows VSS Backup attempt failed because either Instance or SSM Agent has
  invalid state or insufficient privileges."
- "Windows VSS Backup attempt failed because of insufficient privileges to perform
  this operation"
- "Windows VSS Backup attempt failed because ec2-vss-agent.exe is not installed in
  the Instance"
- "Windows VSS Backup Job Error encountered, trying for regular backup"
- "Windows VSS Backup attempt failed because of timeout on VSS enabled snapshot
  creation"
- "Windows VSS Backup attempt failed because of unsupported Windows Server
  version. Supported Versions are Windows Server 2012 or later."
- "Windows VSS Backup attempt failed because of timeout on VSS enabled snapshot
  creation"

- "Subscriber limit exceeded: You have reached the maximum concurrent number of
  backups, which is 300. Wait until other jobs finish, and try again. You can also
  reach out to Support to request a quota increase."
- "Maximum allowed in-progress snapshots for a single volume exceeded."
- "Maximum allowed active snapshot limit exceeded."
- "Image creation throttled due to maximum number of concurrent snapshots on an EBS volume."
- "Cannot create more than 20 user snapshots"
- "The resultant tag set must not have more than 50 user tags."
- "You have reached the maximum supported backups for your account/database. See
  Quotas in the Timestream developer guide for additional information."
- "You have reached your quota of 50,000 for the number of public and private
  images allowed in this Region. Deregister unused images, or request an increase in
  your AMI quota."
- "Your backup succeeded, but we were unable to persist NetworkInterfaces metadata
  as its size exceeded our internal limits."
- "REGEX#subscriber limit exceeded"
- "REGEX#More than 50 tags specified"
- "REGEX#can have at most"

- "You are not authorized to perform this operation."
- "Access Denied trying to call AWS Backup service"
- "Customer credential miss permission to get bucket versioning for bucket."
- "Images from AWS Marketplace cannot be copied to another AWS account."
- "Copy job failed because the destination Backup vault is encrypted with the
  default Backup service managed key. The contents of this vault cannot be copied.
  Only the contents of a Backup vault encrypted by an AWS KMS key may be copied.
- Snapshots encrypted with the AWS managed key can't be shared. Specify another
  snapshot.
- "Encrypted snapshots with Amazon EBS default key cannot be shared
- "Copy job failed. Both source and destination account must be a member of the
  same organization."
- "REGEX#access denied"
- "REGEX#not authorized to"
- "REGEX#cannot be assumed by AWS Backup
- "REGEX#does not have permission"
- "REGEX#missing permission"

- "Backup job failed because there was a running job for the same
  resource."
- "There are too many copy jobs running for resource."

- "Copy job failed. Cross-account copy feature is not enabled for the current
  organization."

- "Backup job expired before completion."

- "Copy job failed. The retention specified in the job is not within the range
  specified for the target Backup Vault."
- "REGEX#could not start because it is either inside or too close to the weekly
  maintenance window configured"
- "REGEX#could not start because it is either inside or too close to the automated
  backup window configured"

- "REGEX#Instance is not in state"
- "REGEX#not in the available state"
- "REGEX#not in available state"
- "REGEX#Cannot snapshot volume"

- "KMS key is either disabled or pending deletion or access to KMS key is
  denied"
- "Given key ID is not accessible"
- "AMI snapshot copy failed with error: Given key ID is not accessible. You must
  have DescribeKey permissions on the default key"
- "REGEX#kms key"

- "The AWS Access Key Id needs a subscription for the service"

- "This operation is not valid for the specified hypervisor because it is not
  online"

- "The specified volume was not found."
- "The virtual machine is not found."
- "Given key ID does not exist"
- "Table not found."
- "REGEX#does not exist"
- "REGEX#Could not find resource"
- "REGEX#Could not find cryopod"
- "REGEX#Cannot find recovery point"
- "REGEX#resource not found"
- "REGEX#no longer available"
- "REGEX#is invalid"

- "REGEX#unsupported resource type"
- "REGEX#Unsupported resource type"

- "We are unable to copy resource tags to your backup because of the Internal
  Failure."
- "We are unable to copy resource tags to your backup because source or
  destination recovery point is unavailable"

- "Token expired. Try again."

- "CreateSnapshot method not supported on hypervisor during snapshot creation.
  Aborted backup job"
- "UnsupportedOperation : Storage Gateway backup copies require a user-created
  backup vault and key at destination."
- "REGEX#Feature is not supported for provided resource type."

- "An internal error occurred."
- "Copy job encountered a fatal error. Please contact AWS Support for further
  assistance."
- "Copy job encountered a fatal error."
- "REGEX#Backup job encountered a fatal error"

## Obtaining dashboard data through AWS CLI

You can use the command line to retrieve the same data which appears in the console. Use
one of the following CLI commands:

- [`list-backup-job-summaries`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-job-summaries.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-job-summaries.html")
- [`list-copy-job-summaries`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-copy-job-summaries.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-copy-job-summaries.html")
- [`list-restore-job-summaries`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-job-summaries.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-job-summaries.html")

There are the valid parameters you can include in each command:

```
BackupJobSummaries (list)
    Region (string),
    Account (string),
    State (string),
    ResourceType (string),
    MessageCategory (string),
AggregationPeriod: (string),
NextToken (string),
MaxResults (number)

CopyJobSummaries (list)
    Region (string),
    Account (string),
    State (string),
    ResourceType (string),
    MessageCategory (string),
AggregationPeriod: (string),
NextToken (string),
MaxResults (number)

RestoreJobSummaries (list)
    Region (string),
    Account (string),
    State (string),
    ResourceType (string),
AggregationPeriod: (string),
NextToken (string)
```

This example shows a sample request where the a user has input
`list-backup-job-summaries` where the request asks to return all available
accounts with a state of `FAILED` over the prior 14 days:

```
GET /audit/backup-job-summaries/
    ?accountId=ANY
    &state=FAILED
    &aggregationPeriod=FOURTEEN_DAYS
```

To obtain a job count for jobs with a status of `completed with issues`,
subtract the job count of `COMPLETED` jobs with a `MessageCategory` of
`SUCCESS` from the total number of `COMPLETED`.
