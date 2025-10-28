# Job runs

The Jobs Runs API describes the data types and API related to starting,
stopping, or viewing job runs, and resetting job bookmarks, in AWS Glue. Job run history is accessible for 90 days for your workflow and job run.

## Data types

- [JobRun structure](#aws-glue-api-jobs-runs-JobRun "#aws-glue-api-jobs-runs-JobRun")
- [Predecessor structure](#aws-glue-api-jobs-runs-Predecessor "#aws-glue-api-jobs-runs-Predecessor")
- [JobBookmarkEntry structure](#aws-glue-api-jobs-runs-JobBookmarkEntry "#aws-glue-api-jobs-runs-JobBookmarkEntry")
- [BatchStopJobRunSuccessfulSubmission structure](#aws-glue-api-jobs-runs-BatchStopJobRunSuccessfulSubmission "#aws-glue-api-jobs-runs-BatchStopJobRunSuccessfulSubmission")
- [BatchStopJobRunError structure](#aws-glue-api-jobs-runs-BatchStopJobRunError "#aws-glue-api-jobs-runs-BatchStopJobRunError")
- [NotificationProperty structure](#aws-glue-api-jobs-runs-NotificationProperty "#aws-glue-api-jobs-runs-NotificationProperty")

## JobRun structure

Contains information about a job run.

###### Fields

- `Id` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of this job run.

- `Attempt` – Number (integer).

The number of the attempt to run this job.

- `PreviousRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the previous run of this job. For example, the `JobRunId`
specified in the `StartJobRun` action.

- `TriggerName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the trigger that started this job run.

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job definition being used in this run.

- `JobMode` – UTF-8 string (valid values: `SCRIPT=""` | `VISUAL=""` | `NOTEBOOK=""`).

A mode that describes how a job was created. Valid values are:

    + `SCRIPT` - The job was created using the AWS Glue Studio script editor.
    + `VISUAL` - The job was created using the AWS Glue Studio visual editor.
    + `NOTEBOOK` - The job was created using an interactive sessions
     notebook.

When the `JobMode` field is missing or null, `SCRIPT`
is assigned as the default value.

- `JobRunQueuingEnabled` – Boolean.

Specifies whether job run queuing is enabled for the job run.

A value of true means job run queuing is enabled for the job run. If false
or not populated, the job run will not be considered for queueing.

- `StartedOn` – Timestamp.

The date and time at which this job run was started.

- `LastModifiedOn` – Timestamp.

The last time that this job run was modified.

- `CompletedOn` – Timestamp.

The date and time that this job run completed.

- `JobRunState` – UTF-8 string (valid values: `STARTING` | `RUNNING` | `STOPPING` | `STOPPED` | `SUCCEEDED` | `FAILED` | `TIMEOUT` | `ERROR` | `WAITING` | `EXPIRED`).

The current state of the job run. For more information about the statuses
of jobs that have terminated abnormally, see [AWS Glue Job Run Statuses](job-run-statuses.md "job-run-statuses.md").

- `Arguments` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

The job arguments associated with this run. For this job run, they replace
the default arguments set in the job definition itself.

You can specify arguments here that your own job-execution script consumes,
as well as arguments that AWS Glue itself consumes.

Job arguments may be logged. Do not pass plaintext secrets as arguments.
Retrieve secrets from a AWS Glue Connection, AWS Secrets Manager or other secret management mechanism if you intend to keep them within the Job.

For information about how to specify and consume your own Job arguments,
see the [Calling
AWS Glue APIs in Python](aws-glue-programming-python-calling.md "aws-glue-programming-python-calling.md") topic in the developer guide.

For information about the arguments you can provide to this field when
configuring Spark jobs, see the [Special
Parameters Used by AWS Glue](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md") topic in the developer guide.

For information about the arguments you can provide to this field when
configuring Ray jobs, see [Using
job parameters in Ray jobs](author-job-ray-job-parameters.md "author-job-ray-job-parameters.md") in the developer guide.

- `ErrorMessage` – UTF-8 string.

An error message associated with this job run.

- `PredecessorRuns` – An array of [Predecessor](#aws-glue-api-jobs-runs-Predecessor "#aws-glue-api-jobs-runs-Predecessor") objects.

A list of predecessors to this job run.

- `AllocatedCapacity` – Number (integer).

This field is deprecated. Use `MaxCapacity` instead.

The number of AWS Glue data processing units (DPUs) allocated
to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative
measure of processing power that consists of 4 vCPUs of compute capacity and 16
GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

- `ExecutionTime` – Number (integer).

The amount of time (in seconds) that the job run consumed resources.

- `Timeout` – Number (integer), at least 1.

The `JobRun` timeout in minutes. This is the maximum time
that a job run can consume resources before it is terminated and enters `TIMEOUT`
status. This value overrides the timeout value set in the parent job.

Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise,
the jobs will throw an exception.

When the value is left blank, the timeout is defaulted to 2880 minutes.

Any existing AWS Glue jobs that had a timeout value greater
than 7 days will be defaulted to 7 days. For instance if you have specified a timeout
of 20 days for a batch job, it will be stopped on the 7th day.

For streaming jobs, if you have set up a maintenance window, it will be restarted
during the maintenance window after 7 days.

- `MaxCapacity` – Number (double).

For Glue version 1.0 or earlier jobs, using the standard worker type, the
number of AWS Glue data processing units (DPUs) that can be allocated
when this job runs. A DPU is a relative measure of processing power that consists
of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the
[AWS Glue pricing
page](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

For Glue version 2.0+ jobs, you cannot specify a `Maximum capacity`.
Instead, you should specify a `Worker type` and the `Number
 of workers`.

Do not set `MaxCapacity` if using `WorkerType`
and `NumberOfWorkers`.

The value that can be allocated for `MaxCapacity` depends
on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache
Spark streaming ETL job:

    + When you specify a Python shell job (`JobCommand.Name`="pythonshell"),
     you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
    + When you specify an Apache Spark ETL job (`JobCommand.Name`="glueetl")
     or Apache Spark streaming ETL job (`JobCommand.Name`="gluestreaming"),
     you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot
     have a fractional DPU allocation.

- `WorkerType` – UTF-8 string (valid values: `Standard=""` | `G.1X=""` | `G.2X=""` | `G.025X=""` | `G.4X=""` | `G.8X=""` | `Z.2X=""`).

The type of predefined worker that is allocated when a job runs. Accepts
a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X
for Ray jobs.

    + For the `G.1X` worker type, each worker maps to 1 DPU (4 vCPUs,
     16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend
     this worker type for workloads such as data transforms, joins, and queries, to
     offers a scalable and cost effective way to run most jobs.
    + For the `G.2X` worker type, each worker maps to 2 DPU (8 vCPUs,
     32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend
     this worker type for workloads such as data transforms, joins, and queries, to
     offers a scalable and cost effective way to run most jobs.
    + For the `G.4X` worker type, each worker maps to 4 DPU (16 vCPUs,
     64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend
     this worker type for jobs whose workloads contain your most demanding transforms,
     aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific
     (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central),
     Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).
    + For the `G.8X` worker type, each worker maps to 8 DPU (32 vCPUs,
     128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend
     this worker type for jobs whose workloads contain your most demanding transforms,
     aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs, in the same AWS
     Regions as supported for the `G.4X` worker type.
    + For the `G.025X` worker type, each worker maps to 0.25 DPU
     (2 vCPUs, 4 GB of memory) with 84GB disk, and provides 1 executor per worker. We
     recommend this worker type for low volume streaming jobs. This worker type is
     only available for AWS Glue version 3.0 or later streaming jobs.
    + For the `Z.2X` worker type, each worker maps to 2 M-DPU (8vCPUs,
     64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.

- `NumberOfWorkers` – Number (integer).

The number of workers of a defined `workerType` that are allocated
when a job runs.

- `SecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the `SecurityConfiguration` structure to be
used with this job run.

- `LogGroupName` – UTF-8 string.

The name of the log group for secure logging that can be server-side encrypted
in Amazon CloudWatch using AWS KMS. This name can be `/aws-glue/jobs/`,
in which case the default encryption is `NONE`. If you add a role name
and `SecurityConfiguration` name (in other words, `/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/`),
then that security configuration is used to encrypt the log group.

- `NotificationProperty` – A [NotificationProperty](#aws-glue-api-jobs-runs-NotificationProperty "#aws-glue-api-jobs-runs-NotificationProperty") object.

Specifies configuration properties of a job run notification.

- `GlueVersion` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #48](aws-glue-api-common.md#regex_48 "aws-glue-api-common.md#regex_48").

In Spark jobs, `GlueVersion` determines the versions of
Apache Spark and Python that AWS Glue available in a job. The Python
version indicates the version supported for jobs of type Spark.

Ray jobs should set `GlueVersion` to `4.0` or
greater. However, the versions of Ray, Python and additional libraries available
in your Ray job are determined by the `Runtime` parameter of the Job
command.

For more information about the available AWS Glue versions
and corresponding Spark and Python versions, see [Glue version](add-job.md "add-job.md") in the developer
guide.

Jobs that are created without specifying a Glue version default to Glue
0.9.

- `DPUSeconds` – Number (double).

This field can be set for either job runs with execution class `FLEX`
or when Auto Scaling is enabled, and represents the total time each executor ran
during the lifecycle of a job run in seconds, multiplied by a DPU factor (1 for `G.1X`,
2 for `G.2X`, or 0.25 for `G.025X` workers). This value
may be different than the `executionEngineRuntime` \* `MaxCapacity`
as in the case of Auto Scaling jobs, as the number of executors running at a given
time may be less than the `MaxCapacity`. Therefore, it is possible
that the value of `DPUSeconds` is less than `executionEngineRuntime` \* `MaxCapacity`.

- `ExecutionClass` – UTF-8 string, not more than 16 bytes long (valid values: `FLEX=""` | `STANDARD=""`).

Indicates whether the job is run with a standard or flexible execution
class. The standard execution-class is ideal for time-sensitive workloads
that require fast job startup and dedicated resources.

The flexible execution class is appropriate for time-insensitive jobs
whose start and completion times may vary.

Only jobs with AWS Glue version 3.0 and above and command type
`glueetl` will be allowed to set `ExecutionClass`
to `FLEX`. The flexible execution class is available for Spark jobs.

- `MaintenanceWindow` – UTF-8 string, matching the [Custom string pattern #34](aws-glue-api-common.md#regex_34 "aws-glue-api-common.md#regex_34").

This field specifies a day of the week and hour for a maintenance window
for streaming jobs. AWS Glue periodically performs maintenance
activities. During these maintenance windows, AWS Glue will need
to restart your streaming jobs.

AWS Glue will restart the job within 3 hours of the specified
maintenance window. For instance, if you set up the maintenance window for Monday
at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.

- `ProfileName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of an AWS Glue usage profile associated with the job
run.

- `StateDetail` – UTF-8 string, not more than 400000 bytes long.

This field holds details that pertain to the state of a job run. The field
is nullable.

For example, when a job run is in a WAITING state as a result of job run queuing,
the field has the reason why the job run is in that state.

- `ExecutionRoleSessionPolicy` – UTF-8 string, not less than 2 or more than 2048 bytes long.

This inline session policy to the StartJobRun API allows you to dynamically
restrict the permissions of the specified execution role for the scope of the
job, without requiring the creation of additional IAM roles.

## Predecessor structure

A job run that was used in the predicate of a conditional trigger that triggered
this job run.

###### Fields

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job definition used by the predecessor job run.

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The job-run ID of the predecessor job run.

## JobBookmarkEntry structure

Defines a point that a job can resume processing.

###### Fields

- `JobName` – UTF-8 string.

The name of the job in question.

- `Version` – Number (integer).

The version of the job.

- `Run` – Number (integer).

The run ID number.

- `Attempt` – Number (integer).

The attempt ID number.

- `PreviousRunId` – UTF-8 string.

The unique run identifier associated with the previous job run.

- `RunId` – UTF-8 string.

The run ID number.

- `JobBookmark` – UTF-8 string.

The bookmark itself.

## BatchStopJobRunSuccessfulSubmission structure

Records a successful request to stop a specified `JobRun`.

###### Fields

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job definition used in the job run that was stopped.

- `JobRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The `JobRunId` of the job run that was stopped.

## BatchStopJobRunError structure

Records an error that occurred when attempting to stop a specified job
run.

###### Fields

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job definition that is used in the job run in question.

- `JobRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The `JobRunId` of the job run in question.

- `ErrorDetail` – An [ErrorDetail](aws-glue-api-common.md#aws-glue-api-common-ErrorDetail "aws-glue-api-common.md#aws-glue-api-common-ErrorDetail") object.

Specifies details about the error that was encountered.

## NotificationProperty structure

Specifies configuration properties of a notification.

###### Fields

- `NotifyDelayAfter` – Number (integer), at least 1.

After a job run starts, the number of minutes to wait before sending a job
run delay notification.

## Operations

- [StartJobRun action (Python: start_job_run)](#aws-glue-api-jobs-runs-StartJobRun "#aws-glue-api-jobs-runs-StartJobRun")
- [BatchStopJobRun action (Python: batch_stop_job_run)](#aws-glue-api-jobs-runs-BatchStopJobRun "#aws-glue-api-jobs-runs-BatchStopJobRun")
- [GetJobRun action (Python: get_job_run)](#aws-glue-api-jobs-runs-GetJobRun "#aws-glue-api-jobs-runs-GetJobRun")
- [GetJobRuns action (Python: get_job_runs)](#aws-glue-api-jobs-runs-GetJobRuns "#aws-glue-api-jobs-runs-GetJobRuns")
- [GetJobBookmark action (Python: get_job_bookmark)](#aws-glue-api-jobs-runs-GetJobBookmark "#aws-glue-api-jobs-runs-GetJobBookmark")
- [GetJobBookmarks action (Python: get_job_bookmarks)](#aws-glue-api-jobs-runs-GetJobBookmarks "#aws-glue-api-jobs-runs-GetJobBookmarks")
- [ResetJobBookmark action (Python: reset_job_bookmark)](#aws-glue-api-jobs-runs-ResetJobBookmark "#aws-glue-api-jobs-runs-ResetJobBookmark")

## StartJobRun action (Python: start_job_run)

Starts a job run using a job definition.

###### Request

- `JobName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job definition to use.

- `JobRunQueuingEnabled` – Boolean.

Specifies whether job run queuing is enabled for the job run.

A value of true means job run queuing is enabled for the job run. If false
or not populated, the job run will not be considered for queueing.

- `JobRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of a previous `JobRun` to retry.

- `Arguments` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

The job arguments associated with this run. For this job run, they replace
the default arguments set in the job definition itself.

You can specify arguments here that your own job-execution script consumes,
as well as arguments that AWS Glue itself consumes.

Job arguments may be logged. Do not pass plaintext secrets as arguments.
Retrieve secrets from a AWS Glue Connection, AWS Secrets Manager or other secret management mechanism if you intend to keep them within the Job.

For information about how to specify and consume your own Job arguments,
see the [Calling
AWS Glue APIs in Python](aws-glue-programming-python-calling.md "aws-glue-programming-python-calling.md") topic in the developer guide.

For information about the arguments you can provide to this field when
configuring Spark jobs, see the [Special
Parameters Used by AWS Glue](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md") topic in the developer guide.

For information about the arguments you can provide to this field when
configuring Ray jobs, see [Using
job parameters in Ray jobs](author-job-ray-job-parameters.md "author-job-ray-job-parameters.md") in the developer guide.

- `AllocatedCapacity` – Number (integer).

This field is deprecated. Use `MaxCapacity` instead.

The number of AWS Glue data processing units (DPUs) to allocate
to this JobRun. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a
relative measure of processing power that consists of 4 vCPUs of compute capacity
and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

- `Timeout` – Number (integer), at least 1.

The `JobRun` timeout in minutes. This is the maximum time
that a job run can consume resources before it is terminated and enters `TIMEOUT`
status. This value overrides the timeout value set in the parent job.

Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise,
the jobs will throw an exception.

When the value is left blank, the timeout is defaulted to 2880 minutes.

Any existing AWS Glue jobs that had a timeout value greater
than 7 days will be defaulted to 7 days. For instance if you have specified a timeout
of 20 days for a batch job, it will be stopped on the 7th day.

For streaming jobs, if you have set up a maintenance window, it will be restarted
during the maintenance window after 7 days.

- `MaxCapacity` – Number (double).

For Glue version 1.0 or earlier jobs, using the standard worker type, the
number of AWS Glue data processing units (DPUs) that can be allocated
when this job runs. A DPU is a relative measure of processing power that consists
of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the
[AWS Glue pricing
page](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

For Glue version 2.0+ jobs, you cannot specify a `Maximum capacity`.
Instead, you should specify a `Worker type` and the `Number
 of workers`.

Do not set `MaxCapacity` if using `WorkerType`
and `NumberOfWorkers`.

The value that can be allocated for `MaxCapacity` depends
on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache
Spark streaming ETL job:

    + When you specify a Python shell job (`JobCommand.Name`="pythonshell"),
     you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
    + When you specify an Apache Spark ETL job (`JobCommand.Name`="glueetl")
     or Apache Spark streaming ETL job (`JobCommand.Name`="gluestreaming"),
     you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot
     have a fractional DPU allocation.

- `SecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the `SecurityConfiguration` structure to be
used with this job run.

- `NotificationProperty` – A [NotificationProperty](#aws-glue-api-jobs-runs-NotificationProperty "#aws-glue-api-jobs-runs-NotificationProperty") object.

Specifies configuration properties of a job run notification.

- `WorkerType` – UTF-8 string (valid values: `Standard=""` | `G.1X=""` | `G.2X=""` | `G.025X=""` | `G.4X=""` | `G.8X=""` | `Z.2X=""`).

The type of predefined worker that is allocated when a job runs. Accepts
a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X
for Ray jobs.

    + For the `G.1X` worker type, each worker maps to 1 DPU (4 vCPUs,
     16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend
     this worker type for workloads such as data transforms, joins, and queries, to
     offers a scalable and cost effective way to run most jobs.
    + For the `G.2X` worker type, each worker maps to 2 DPU (8 vCPUs,
     32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend
     this worker type for workloads such as data transforms, joins, and queries, to
     offers a scalable and cost effective way to run most jobs.
    + For the `G.4X` worker type, each worker maps to 4 DPU (16 vCPUs,
     64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend
     this worker type for jobs whose workloads contain your most demanding transforms,
     aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific
     (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central),
     Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).
    + For the `G.8X` worker type, each worker maps to 8 DPU (32 vCPUs,
     128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend
     this worker type for jobs whose workloads contain your most demanding transforms,
     aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs, in the same AWS
     Regions as supported for the `G.4X` worker type.
    + For the `G.025X` worker type, each worker maps to 0.25 DPU
     (2 vCPUs, 4 GB of memory) with 84GB disk, and provides 1 executor per worker. We
     recommend this worker type for low volume streaming jobs. This worker type is
     only available for AWS Glue version 3.0 or later streaming jobs.
    + For the `Z.2X` worker type, each worker maps to 2 M-DPU (8vCPUs,
     64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.

- `NumberOfWorkers` – Number (integer).

The number of workers of a defined `workerType` that are allocated
when a job runs.

- `ExecutionClass` – UTF-8 string, not more than 16 bytes long (valid values: `FLEX=""` | `STANDARD=""`).

Indicates whether the job is run with a standard or flexible execution
class. The standard execution-class is ideal for time-sensitive workloads
that require fast job startup and dedicated resources.

The flexible execution class is appropriate for time-insensitive jobs
whose start and completion times may vary.

Only jobs with AWS Glue version 3.0 and above and command type
`glueetl` will be allowed to set `ExecutionClass`
to `FLEX`. The flexible execution class is available for Spark jobs.

- `ProfileName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of an AWS Glue usage profile associated with the job
run.

- `ExecutionRoleSessionPolicy` – UTF-8 string, not less than 2 or more than 2048 bytes long.

This inline session policy to the StartJobRun API allows you to dynamically
restrict the permissions of the specified execution role for the scope of the
job, without requiring the creation of additional IAM roles.

###### Response

- `JobRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID assigned to this job run.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `ConcurrentRunsExceededException`

## BatchStopJobRun action (Python: batch_stop_job_run)

Stops one or more job runs for a specified job definition.

###### Request

- `JobName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job definition for which to stop job runs.

- `JobRunIds` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 25 strings.

A list of the `JobRunIds` that should be stopped for that job
definition.

###### Response

- `SuccessfulSubmissions` – An array of [BatchStopJobRunSuccessfulSubmission](#aws-glue-api-jobs-runs-BatchStopJobRunSuccessfulSubmission "#aws-glue-api-jobs-runs-BatchStopJobRunSuccessfulSubmission") objects.

A list of the JobRuns that were successfully submitted for stopping.

- `Errors` – An array of [BatchStopJobRunError](#aws-glue-api-jobs-runs-BatchStopJobRunError "#aws-glue-api-jobs-runs-BatchStopJobRunError") objects.

A list of the errors that were encountered in trying to stop `JobRuns`,
including the `JobRunId` for which each error was encountered and
details about the error.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## GetJobRun action (Python: get_job_run)

Retrieves the metadata for a given job run. Job run history is accessible
for 365 days for your workflow and job run.

###### Request

- `JobName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the job definition being run.

- `RunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the job run.

- `PredecessorsIncluded` – Boolean.

True if a list of predecessor runs should be returned.

###### Response

- `JobRun` – A [JobRun](#aws-glue-api-jobs-runs-JobRun "#aws-glue-api-jobs-runs-JobRun") object.

The requested job-run metadata.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`

## GetJobRuns action (Python: get_job_runs)

Retrieves metadata for all runs of a given job definition.

`GetJobRuns` returns the job runs in chronological order,
with the newest jobs returned first.

###### Request

- `JobName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job definition for which to retrieve all job runs.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

- `MaxResults` – Number (integer), not less than 1 or more than 200.

The maximum size of the response.

###### Response

- `JobRuns` – An array of [JobRun](#aws-glue-api-jobs-runs-JobRun "#aws-glue-api-jobs-runs-JobRun") objects.

A list of job-run metadata objects.

- `NextToken` – UTF-8 string.

A continuation token, if not all requested job runs have been returned.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`

## GetJobBookmark action (Python: get_job_bookmark)

Returns information on a job bookmark entry.

For more information about enabling and using job bookmarks, see:

- [Tracking
  processed data using job bookmarks](monitor-continuations.md "monitor-continuations.md")
- [Job
  parameters used by AWS Glue](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md")
- [Job
  structure](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-Job "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-Job")

###### Request

- `JobName` – _Required:_ UTF-8 string.

The name of the job in question.

- `Version` – Number (integer).

The version of the job.

- `RunId` – UTF-8 string.

The unique run identifier associated with this job run.

###### Response

- `JobBookmarkEntry` – A [JobBookmarkEntry](#aws-glue-api-jobs-runs-JobBookmarkEntry "#aws-glue-api-jobs-runs-JobBookmarkEntry") object.

A structure that defines a point that a job can resume processing.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ValidationException`

## GetJobBookmarks action (Python: get_job_bookmarks)

Returns information on the job bookmark entries. The list is ordered on
decreasing version numbers.

For more information about enabling and using job bookmarks, see:

- [Tracking
  processed data using job bookmarks](monitor-continuations.md "monitor-continuations.md")
- [Job
  parameters used by AWS Glue](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md")
- [Job
  structure](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-Job "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-Job")

###### Request

- `JobName` – _Required:_ UTF-8 string.

The name of the job in question.

- `MaxResults` – Number (integer).

The maximum size of the response.

- `NextToken` – Number (integer).

A continuation token, if this is a continuation call.

###### Response

- `JobBookmarkEntries` – An array of [JobBookmarkEntry](#aws-glue-api-jobs-runs-JobBookmarkEntry "#aws-glue-api-jobs-runs-JobBookmarkEntry") objects.

A list of job bookmark entries that defines a point that a job can resume
processing.

- `NextToken` – Number (integer).

A continuation token, which has a value of 1 if all the entries are returned,
or > 1 if not all requested job runs have been returned.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`

## ResetJobBookmark action (Python: reset_job_bookmark)

Resets a bookmark entry.

For more information about enabling and using job bookmarks, see:

- [Tracking
  processed data using job bookmarks](monitor-continuations.md "monitor-continuations.md")
- [Job
  parameters used by AWS Glue](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md")
- [Job
  structure](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-Job "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-Job")

###### Request

- `JobName` – _Required:_ UTF-8 string.

The name of the job in question.

- `RunId` – UTF-8 string.

The unique run identifier associated with this job run.

###### Response

- `JobBookmarkEntry` – A [JobBookmarkEntry](#aws-glue-api-jobs-runs-JobBookmarkEntry "#aws-glue-api-jobs-runs-JobBookmarkEntry") object.

The reset bookmark entry.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
