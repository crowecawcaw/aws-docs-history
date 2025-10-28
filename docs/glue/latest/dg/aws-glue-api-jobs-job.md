# Jobs

The Jobs API describes the data types and API related to creating, updating,
deleting, or viewing jobs in AWS Glue.

## Data types

- [Job structure](#aws-glue-api-jobs-job-Job "#aws-glue-api-jobs-job-Job")
- [ExecutionProperty structure](#aws-glue-api-jobs-job-ExecutionProperty "#aws-glue-api-jobs-job-ExecutionProperty")
- [NotificationProperty structure](#aws-glue-api-jobs-job-NotificationProperty "#aws-glue-api-jobs-job-NotificationProperty")
- [JobCommand structure](#aws-glue-api-jobs-job-JobCommand "#aws-glue-api-jobs-job-JobCommand")
- [ConnectionsList structure](#aws-glue-api-jobs-job-ConnectionsList "#aws-glue-api-jobs-job-ConnectionsList")
- [JobUpdate structure](#aws-glue-api-jobs-job-JobUpdate "#aws-glue-api-jobs-job-JobUpdate")
- [SourceControlDetails structure](#aws-glue-api-jobs-job-SourceControlDetails "#aws-glue-api-jobs-job-SourceControlDetails")

## Job structure

Specifies a job definition.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name you assign to this job definition.

- `JobMode` – UTF-8 string (valid values: `SCRIPT=""` | `VISUAL=""` | `NOTEBOOK=""`).

A mode that describes how a job was created. Valid values are:

    + `SCRIPT` - The job was created using the AWS Glue Studio script editor.
    + `VISUAL` - The job was created using the AWS Glue Studio visual editor.
    + `NOTEBOOK` - The job was created using an interactive sessions
     notebook.

When the `JobMode` field is missing or null, `SCRIPT`
is assigned as the default value.

- `JobRunQueuingEnabled` – Boolean.

Specifies whether job run queuing is enabled for the job runs for this job.

A value of true means job run queuing is enabled for the job runs. If false
or not populated, the job runs will not be considered for queueing.

If this field does not match the value set in the job run, then the value from
the job run field will be used.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the job.

- `LogUri` – UTF-8 string.

This field is reserved for future use.

- `Role` – UTF-8 string.

The name or Amazon Resource Name (ARN) of the IAM role associated with this
job.

- `CreatedOn` – Timestamp.

The time and date that this job definition was created.

- `LastModifiedOn` – Timestamp.

The last point in time when this job definition was modified.

- `ExecutionProperty` – An [ExecutionProperty](#aws-glue-api-jobs-job-ExecutionProperty "#aws-glue-api-jobs-job-ExecutionProperty") object.

An `ExecutionProperty` specifying the maximum number of
concurrent runs allowed for this job.

- `Command` – A [JobCommand](#aws-glue-api-jobs-job-JobCommand "#aws-glue-api-jobs-job-JobCommand") object.

The `JobCommand` that runs this job.

- `DefaultArguments` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

The default arguments for every run of this job, specified as name-value
pairs.

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

- `NonOverridableArguments` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

Arguments for this job that are not overridden when providing job arguments
in a job run, specified as name-value pairs.

- `Connections` – A [ConnectionsList](aws-glue-api-interactive-sessions.md#aws-glue-api-interactive-sessions-ConnectionsList "aws-glue-api-interactive-sessions.md#aws-glue-api-interactive-sessions-ConnectionsList") object.

The connections used for this job.

- `MaxRetries` – Number (integer).

The maximum number of times to retry this job after a JobRun fails.

- `AllocatedCapacity` – Number (integer).

This field is deprecated. Use `MaxCapacity` instead.

The number of AWS Glue data processing units (DPUs) allocated
to runs of this job. You can allocate a minimum of 2 DPUs; the default is 10. A DPU
is a relative measure of processing power that consists of 4 vCPUs of compute capacity
and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

- `Timeout` – Number (integer), at least 1.

The job timeout in minutes. This is the maximum time that a job run can consume
resources before it is terminated and enters `TIMEOUT` status.

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

For Glue version 2.0 or later jobs, you cannot specify a `Maximum
 capacity`. Instead, you should specify a `Worker type` and
the `Number of workers`.

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

The type of predefined worker that is allocated when a job runs.

AWS Glue provides multiple worker types to accommodate different
workload requirements:

G Worker Types (General-purpose compute workers):

    + G.1X: 1 DPU (4 vCPUs, 16 GB memory, 94GB disk)
    + G.2X: 2 DPU (8 vCPUs, 32 GB memory, 138GB disk)
    + G.4X: 4 DPU (16 vCPUs, 64 GB memory, 256GB disk)
    + G.8X: 8 DPU (32 vCPUs, 128 GB memory, 512GB disk)
    + G.12X: 12 DPU (48 vCPUs, 192 GB memory, 768GB disk)
    + G.16X: 16 DPU (64 vCPUs, 256 GB memory, 1024GB disk)

R Worker Types (Memory-optimized workers):

    + R.1X: 1 M-DPU (4 vCPUs, 32 GB memory)
    + R.2X: 2 M-DPU (8 vCPUs, 64 GB memory)
    + R.4X: 4 M-DPU (16 vCPUs, 128 GB memory)
    + R.8X: 8 M-DPU (32 vCPUs, 256 GB memory)

- `NumberOfWorkers` – Number (integer).

The number of workers of a defined `workerType` that are allocated
when a job runs.

- `SecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the `SecurityConfiguration` structure to be
used with this job.

- `NotificationProperty` – A [NotificationProperty](aws-glue-api-jobs-runs.md#aws-glue-api-jobs-runs-NotificationProperty "aws-glue-api-jobs-runs.md#aws-glue-api-jobs-runs-NotificationProperty") object.

Specifies configuration properties of a job notification.

- `Running` – Boolean.

This field is reserved for future use.

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

- `CodeGenConfigurationNodes` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

Each value is a A [CodeGenConfigurationNode](aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-CodeGenConfigurationNode "aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-CodeGenConfigurationNode") object.

The representation of a directed acyclic graph on which both the Glue Studio
visual component and Glue Studio code generation is based.

- `ExecutionClass` – UTF-8 string, not more than 16 bytes long (valid values: `FLEX=""` | `STANDARD=""`).

Indicates whether the job is run with a standard or flexible execution
class. The standard execution class is ideal for time-sensitive workloads that
require fast job startup and dedicated resources.

The flexible execution class is appropriate for time-insensitive jobs
whose start and completion times may vary.

Only jobs with AWS Glue version 3.0 and above and command type
`glueetl` will be allowed to set `ExecutionClass`
to `FLEX`. The flexible execution class is available for Spark jobs.

- `SourceControlDetails` – A [SourceControlDetails](#aws-glue-api-jobs-job-SourceControlDetails "#aws-glue-api-jobs-job-SourceControlDetails") object.

The details for a source control configuration for a job, allowing synchronization
of job artifacts to or from a remote repository.

- `MaintenanceWindow` – UTF-8 string, matching the [Custom string pattern #34](aws-glue-api-common.md#regex_34 "aws-glue-api-common.md#regex_34").

This field specifies a day of the week and hour for a maintenance window
for streaming jobs. AWS Glue periodically performs maintenance
activities. During these maintenance windows, AWS Glue will need
to restart your streaming jobs.

AWS Glue will restart the job within 3 hours of the specified
maintenance window. For instance, if you set up the maintenance window for Monday
at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.

- `ProfileName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of an AWS Glue usage profile associated with the job.

## ExecutionProperty structure

An execution property of a job.

###### Fields

- `MaxConcurrentRuns` – Number (integer).

The maximum number of concurrent runs allowed for the job. The default
is 1. An error is returned when this threshold is reached. The maximum value you
can specify is controlled by a service limit.

## NotificationProperty structure

Specifies configuration properties of a notification.

###### Fields

- `NotifyDelayAfter` – Number (integer), at least 1.

After a job run starts, the number of minutes to wait before sending a job
run delay notification.

## JobCommand structure

Specifies code that runs when a job is run.

###### Fields

- `Name` – UTF-8 string.

The name of the job command. For an Apache Spark ETL job, this must be `glueetl`.
For a Python shell job, it must be `pythonshell`. For an Apache Spark
streaming ETL job, this must be `gluestreaming`. For a Ray job, this
must be `glueray`.

- `ScriptLocation` – UTF-8 string, not more than 400000 bytes long.

Specifies the Amazon Simple Storage Service (Amazon S3) path to a script
that runs a job.

- `PythonVersion` – UTF-8 string, matching the [Custom string pattern #49](aws-glue-api-common.md#regex_49 "aws-glue-api-common.md#regex_49").

The Python version being used to run a Python shell job. Allowed values
are 2 or 3.

- `Runtime` – UTF-8 string, not more than 64 bytes long, matching the [Custom string pattern #33](aws-glue-api-common.md#regex_33 "aws-glue-api-common.md#regex_33").

In Ray jobs, Runtime is used to specify the versions of Ray, Python and additional
libraries available in your environment. This field is not used in other job types.
For supported runtime environment values, see [Supported Ray runtime environments](ray-jobs-section.md "ray-jobs-section.md")
in the AWS Glue Developer Guide.

## ConnectionsList structure

Specifies the connections used by a job.

###### Fields

- `Connections` – An array of UTF-8 strings, not more than 1000 strings.

A list of connections used by the job.

## JobUpdate structure

Specifies information used to update an existing job definition. The
previous job definition is completely overwritten by this information.

###### Fields

- `JobMode` – UTF-8 string (valid values: `SCRIPT=""` | `VISUAL=""` | `NOTEBOOK=""`).

A mode that describes how a job was created. Valid values are:

    + `SCRIPT` - The job was created using the AWS Glue Studio script editor.
    + `VISUAL` - The job was created using the AWS Glue Studio visual editor.
    + `NOTEBOOK` - The job was created using an interactive sessions
     notebook.

When the `JobMode` field is missing or null, `SCRIPT`
is assigned as the default value.

- `JobRunQueuingEnabled` – Boolean.

Specifies whether job run queuing is enabled for the job runs for this job.

A value of true means job run queuing is enabled for the job runs. If false
or not populated, the job runs will not be considered for queueing.

If this field does not match the value set in the job run, then the value from
the job run field will be used.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

Description of the job being defined.

- `LogUri` – UTF-8 string.

This field is reserved for future use.

- `Role` – UTF-8 string.

The name or Amazon Resource Name (ARN) of the IAM role associated with this
job (required).

- `ExecutionProperty` – An [ExecutionProperty](#aws-glue-api-jobs-job-ExecutionProperty "#aws-glue-api-jobs-job-ExecutionProperty") object.

An `ExecutionProperty` specifying the maximum number of
concurrent runs allowed for this job.

- `Command` – A [JobCommand](#aws-glue-api-jobs-job-JobCommand "#aws-glue-api-jobs-job-JobCommand") object.

The `JobCommand` that runs this job (required).

- `DefaultArguments` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

The default arguments for every run of this job, specified as name-value
pairs.

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

- `NonOverridableArguments` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

Arguments for this job that are not overridden when providing job arguments
in a job run, specified as name-value pairs.

- `Connections` – A [ConnectionsList](aws-glue-api-interactive-sessions.md#aws-glue-api-interactive-sessions-ConnectionsList "aws-glue-api-interactive-sessions.md#aws-glue-api-interactive-sessions-ConnectionsList") object.

The connections used for this job.

- `MaxRetries` – Number (integer).

The maximum number of times to retry this job if it fails.

- `AllocatedCapacity` – Number (integer).

This field is deprecated. Use `MaxCapacity` instead.

The number of AWS Glue data processing units (DPUs) to allocate
to this job. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a relative
measure of processing power that consists of 4 vCPUs of compute capacity and 16
GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

- `Timeout` – Number (integer), at least 1.

The job timeout in minutes. This is the maximum time that a job run can consume
resources before it is terminated and enters `TIMEOUT` status.

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
for Ray jobs. For more information, see [Defining
job properties for Spark jobs](add-job.md#create-job "add-job.md#create-job")

- `NumberOfWorkers` – Number (integer).

The number of workers of a defined `workerType` that are allocated
when a job runs.

- `SecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the `SecurityConfiguration` structure to be
used with this job.

- `NotificationProperty` – A [NotificationProperty](aws-glue-api-jobs-runs.md#aws-glue-api-jobs-runs-NotificationProperty "aws-glue-api-jobs-runs.md#aws-glue-api-jobs-runs-NotificationProperty") object.

Specifies the configuration properties of a job notification.

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

- `CodeGenConfigurationNodes` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

Each value is a A [CodeGenConfigurationNode](aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-CodeGenConfigurationNode "aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-CodeGenConfigurationNode") object.

The representation of a directed acyclic graph on which both the Glue Studio
visual component and Glue Studio code generation is based.

- `ExecutionClass` – UTF-8 string, not more than 16 bytes long (valid values: `FLEX=""` | `STANDARD=""`).

Indicates whether the job is run with a standard or flexible execution
class. The standard execution-class is ideal for time-sensitive workloads
that require fast job startup and dedicated resources.

The flexible execution class is appropriate for time-insensitive jobs
whose start and completion times may vary.

Only jobs with AWS Glue version 3.0 and above and command type
`glueetl` will be allowed to set `ExecutionClass`
to `FLEX`. The flexible execution class is available for Spark jobs.

- `SourceControlDetails` – A [SourceControlDetails](#aws-glue-api-jobs-job-SourceControlDetails "#aws-glue-api-jobs-job-SourceControlDetails") object.

The details for a source control configuration for a job, allowing synchronization
of job artifacts to or from a remote repository.

- `MaintenanceWindow` – UTF-8 string, matching the [Custom string pattern #34](aws-glue-api-common.md#regex_34 "aws-glue-api-common.md#regex_34").

This field specifies a day of the week and hour for a maintenance window
for streaming jobs. AWS Glue periodically performs maintenance
activities. During these maintenance windows, AWS Glue will need
to restart your streaming jobs.

AWS Glue will restart the job within 3 hours of the specified
maintenance window. For instance, if you set up the maintenance window for Monday
at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.

- `ProfileName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of an AWS Glue usage profile associated with the job.

## SourceControlDetails structure

The details for a source control configuration for a job, allowing synchronization
of job artifacts to or from a remote repository.

###### Fields

- `Provider` – UTF-8 string (valid values: `GITHUB` | `AWS_CODE_COMMIT`).

The provider for the remote repository.

- `Repository` – UTF-8 string, not less than 1 or more than 512 bytes long.

The name of the remote repository that contains the job artifacts.

- `Owner` – UTF-8 string, not less than 1 or more than 512 bytes long.

The owner of the remote repository that contains the job artifacts.

- `Branch` – UTF-8 string, not less than 1 or more than 512 bytes long.

An optional branch in the remote repository.

- `Folder` – UTF-8 string, not less than 1 or more than 512 bytes long.

An optional folder in the remote repository.

- `LastCommitId` – UTF-8 string, not less than 1 or more than 512 bytes long.

The last commit ID for a commit in the remote repository.

- `LastSyncTimestamp` – UTF-8 string, not less than 1 or more than 512 bytes long.

The date and time that the last job synchronization was performed.

- `AuthStrategy` – UTF-8 string (valid values: `PERSONAL_ACCESS_TOKEN` | `AWS_SECRETS_MANAGER`).

The type of authentication, which can be an authentication token stored
in AWS Secrets Manager, or a personal access token.

- `AuthToken` – UTF-8 string, not less than 1 or more than 512 bytes long.

The value of an authorization token.

## Operations

- [CreateJob action (Python: create_job)](#aws-glue-api-jobs-job-CreateJob "#aws-glue-api-jobs-job-CreateJob")
- [UpdateJob action (Python: update_job)](#aws-glue-api-jobs-job-UpdateJob "#aws-glue-api-jobs-job-UpdateJob")
- [GetJob action (Python: get_job)](#aws-glue-api-jobs-job-GetJob "#aws-glue-api-jobs-job-GetJob")
- [GetJobs action (Python: get_jobs)](#aws-glue-api-jobs-job-GetJobs "#aws-glue-api-jobs-job-GetJobs")
- [DeleteJob action (Python: delete_job)](#aws-glue-api-jobs-job-DeleteJob "#aws-glue-api-jobs-job-DeleteJob")
- [ListJobs action (Python: list_jobs)](#aws-glue-api-jobs-job-ListJobs "#aws-glue-api-jobs-job-ListJobs")
- [BatchGetJobs action (Python: batch_get_jobs)](#aws-glue-api-jobs-job-BatchGetJobs "#aws-glue-api-jobs-job-BatchGetJobs")

## CreateJob action (Python: create_job)

Creates a new job definition.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name you assign to this job definition. It must be unique in your account.

- `JobMode` – UTF-8 string (valid values: `SCRIPT=""` | `VISUAL=""` | `NOTEBOOK=""`).

A mode that describes how a job was created. Valid values are:

    + `SCRIPT` - The job was created using the AWS Glue Studio script editor.
    + `VISUAL` - The job was created using the AWS Glue Studio visual editor.
    + `NOTEBOOK` - The job was created using an interactive sessions
     notebook.

When the `JobMode` field is missing or null, `SCRIPT`
is assigned as the default value.

- `JobRunQueuingEnabled` – Boolean.

Specifies whether job run queuing is enabled for the job runs for this job.

A value of true means job run queuing is enabled for the job runs. If false
or not populated, the job runs will not be considered for queueing.

If this field does not match the value set in the job run, then the value from
the job run field will be used.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

Description of the job being defined.

- `LogUri` – UTF-8 string.

This field is reserved for future use.

- `Role` – _Required:_ UTF-8 string.

The name or Amazon Resource Name (ARN) of the IAM role associated with this
job.

- `ExecutionProperty` – An [ExecutionProperty](#aws-glue-api-jobs-job-ExecutionProperty "#aws-glue-api-jobs-job-ExecutionProperty") object.

An `ExecutionProperty` specifying the maximum number of
concurrent runs allowed for this job.

- `Command` – _Required:_ A [JobCommand](#aws-glue-api-jobs-job-JobCommand "#aws-glue-api-jobs-job-JobCommand") object.

The `JobCommand` that runs this job.

- `DefaultArguments` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

The default arguments for every run of this job, specified as name-value
pairs.

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

- `NonOverridableArguments` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

Arguments for this job that are not overridden when providing job arguments
in a job run, specified as name-value pairs.

- `Connections` – A [ConnectionsList](aws-glue-api-interactive-sessions.md#aws-glue-api-interactive-sessions-ConnectionsList "aws-glue-api-interactive-sessions.md#aws-glue-api-interactive-sessions-ConnectionsList") object.

The connections used for this job.

- `MaxRetries` – Number (integer).

The maximum number of times to retry this job if it fails.

- `AllocatedCapacity` – Number (integer).

This parameter is deprecated. Use `MaxCapacity` instead.

The number of AWS Glue data processing units (DPUs) to allocate
to this Job. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a relative
measure of processing power that consists of 4 vCPUs of compute capacity and 16
GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

- `Timeout` – Number (integer), at least 1.

The job timeout in minutes. This is the maximum time that a job run can consume
resources before it is terminated and enters `TIMEOUT` status.

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
used with this job.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

The tags to use with this job. You may use tags to limit access to the job.
For more information about tags in AWS Glue, see [AWS Tags in AWS Glue](monitor-tags.md "monitor-tags.md") in the developer guide.

- `NotificationProperty` – A [NotificationProperty](aws-glue-api-jobs-runs.md#aws-glue-api-jobs-runs-NotificationProperty "aws-glue-api-jobs-runs.md#aws-glue-api-jobs-runs-NotificationProperty") object.

Specifies configuration properties of a job notification.

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

- `NumberOfWorkers` – Number (integer).

The number of workers of a defined `workerType` that are allocated
when a job runs.

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
     aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (N. California), US
     West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore),
     Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt),
     Europe (Ireland), Europe (London), Europe (Spain), Europe (Stockholm), and
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

- `CodeGenConfigurationNodes` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

Each value is a A [CodeGenConfigurationNode](aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-CodeGenConfigurationNode "aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-CodeGenConfigurationNode") object.

The representation of a directed acyclic graph on which both the Glue Studio
visual component and Glue Studio code generation is based.

- `ExecutionClass` – UTF-8 string, not more than 16 bytes long (valid values: `FLEX=""` | `STANDARD=""`).

Indicates whether the job is run with a standard or flexible execution
class. The standard execution-class is ideal for time-sensitive workloads
that require fast job startup and dedicated resources.

The flexible execution class is appropriate for time-insensitive jobs
whose start and completion times may vary.

Only jobs with AWS Glue version 3.0 and above and command type
`glueetl` will be allowed to set `ExecutionClass`
to `FLEX`. The flexible execution class is available for Spark jobs.

- `SourceControlDetails` – A [SourceControlDetails](#aws-glue-api-jobs-job-SourceControlDetails "#aws-glue-api-jobs-job-SourceControlDetails") object.

The details for a source control configuration for a job, allowing synchronization
of job artifacts to or from a remote repository.

- `MaintenanceWindow` – UTF-8 string, matching the [Custom string pattern #34](aws-glue-api-common.md#regex_34 "aws-glue-api-common.md#regex_34").

This field specifies a day of the week and hour for a maintenance window
for streaming jobs. AWS Glue periodically performs maintenance
activities. During these maintenance windows, AWS Glue will need
to restart your streaming jobs.

AWS Glue will restart the job within 3 hours of the specified
maintenance window. For instance, if you set up the maintenance window for Monday
at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.

- `ProfileName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of an AWS Glue usage profile associated with the job.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique name that was provided for this job definition.

###### Errors

- `InvalidInputException`
- `IdempotentParameterMismatchException`
- `AlreadyExistsException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `ConcurrentModificationException`

## UpdateJob action (Python: update_job)

Updates an existing job definition. The previous job definition is completely
overwritten by this information.

###### Request

- `JobName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job definition to update.

- `JobUpdate` – _Required:_ A [JobUpdate](#aws-glue-api-jobs-job-JobUpdate "#aws-glue-api-jobs-job-JobUpdate") object.

Specifies the values with which to update the job definition. Unspecified
configuration is removed or reset to default values.

- `ProfileName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of an AWS Glue usage profile associated with the job.

###### Response

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Returns the name of the updated job definition.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ConcurrentModificationException`

## GetJob action (Python: get_job)

Retrieves an existing job definition.

###### Request

- `JobName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job definition to retrieve.

###### Response

- `Job` – A [Job](#aws-glue-api-jobs-job-Job "#aws-glue-api-jobs-job-Job") object.

The requested job definition.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`

## GetJobs action (Python: get_jobs)

Retrieves all current job definitions.

###### Request

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum size of the response.

###### Response

- `Jobs` – An array of [Job](#aws-glue-api-jobs-job-Job "#aws-glue-api-jobs-job-Job") objects.

A list of job definitions.

- `NextToken` – UTF-8 string.

A continuation token, if not all job definitions have yet been returned.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`

## DeleteJob action (Python: delete_job)

Deletes a specified job definition. If the job definition is not found,
no exception is thrown.

###### Request

- `JobName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job definition to delete.

###### Response

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job definition that was deleted.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## ListJobs action (Python: list_jobs)

Retrieves the names of all job resources in this AWS account,
or the resources with the specified tag. This operation allows you to see which
resources are available in your account, and their names.

This operation takes the optional `Tags` field, which you
can use as a filter on the response so that tagged resources can be retrieved as
a group. If you choose to use tags filtering, only resources with the tag are retrieved.

###### Request

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation request.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum size of a list to return.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

Specifies to return only these tagged resources.

###### Response

- `JobNames` – An array of UTF-8 strings.

The names of all jobs in the account, or the jobs with the specified tags.

- `NextToken` – UTF-8 string.

A continuation token, if the returned list does not contain the last metric
available.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`

## BatchGetJobs action (Python: batch_get_jobs)

Returns a list of resource metadata for a given list of job names. After
calling the `ListJobs` operation, you can call this operation to
access the data to which you have been granted permissions. This operation supports
all IAM permissions, including permission conditions that uses tags.

###### Request

- `JobNames` – _Required:_ An array of UTF-8 strings.

A list of job names, which might be the names returned from the `ListJobs`
operation.

###### Response

- `Jobs` – An array of [Job](#aws-glue-api-jobs-job-Job "#aws-glue-api-jobs-job-Job") objects.

A list of job definitions.

- `JobsNotFound` – An array of UTF-8 strings.

A list of names of jobs not found.

###### Errors

- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`
