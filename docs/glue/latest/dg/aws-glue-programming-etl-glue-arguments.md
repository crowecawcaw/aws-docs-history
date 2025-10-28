# Using job parameters in AWS Glue jobs

When creating a AWS Glue job, you set some standard fields, such as `Role` and `WorkerType`.
You can provide additional configuration information through the `Argument` fields (**Job
Parameters** in the console). In these fields, you can provide AWS Glue jobs with the arguments (parameters)
listed in this topic.

For more information about the AWS Glue Job API, see [Jobs](aws-glue-api-jobs-job.md "aws-glue-api-jobs-job.md").

###### Note

Job arguments have a maximum size limit of 260KB. A validation check will raise an error if the argument size is
greater than 260KB.

## Setting job parameters

You can configure a job through the console on the **Job details** tab, under the
**Job Parameters** heading. You can also configure a job through the AWS CLI by setting
`DefaultArguments` or `NonOverridableArguments` on a job, or setting `Arguments`
on a job run. Arguments set on the job will be passed in every time the job is run, while arguments set on the job
run will only be passed in for that individual run.

For example, the following is the syntax for running a job using `--arguments` to
set a job parameter.

```
$ aws glue start-job-run --job-name "CSV to CSV" --arguments='--scriptLocation="s3://my_glue/libraries/test_lib.py"'
```

## Accessing job parameters

When writing AWS Glue scripts, you may want to access job parameter values to alter the behavior of your own
code. We provide helper methods to do so in our libraries. These methods resolve job run parameter values that
override job parameter values. When resolving parameters set in multiple places, job `NonOverridableArguments` will
override job run `Arguments`, which will override job `DefaultArguments`.

**In Python:**

In Python jobs, we provide a function named `getResolvedParameters`. For more information, see
[Accessing
parameters using getResolvedOptions](aws-glue-api-crawler-pyspark-extensions-get-resolved-options.md "aws-glue-api-crawler-pyspark-extensions-get-resolved-options.md"). Job parameters are available in
the `sys.argv` variable.

**In Scala:**

In Scala jobs, we provide an object named `GlueArgParser`. For more information, see [AWS Glue Scala GlueArgParser
APIs](glue-etl-scala-apis-glue-util-glueargparser.md "glue-etl-scala-apis-glue-util-glueargparser.md"). Job parameters are available in the `sysArgs`
variable.

## Job parameter reference

**AWS Glue recognizes the following argument names that you can use to set up the
script environment for your jobs and job runs:**

**`--additional-python-modules`**

A comma delimited list representing a set of Python packages to be installed. You can
install packages from PyPI or provide a custom distribution. A PyPI package entry will be
in the format
``package`==`version``,
with the PyPI name and version of your target package. A custom distribution entry is the
S3 path to the distribution.

Entries use Python version matching to match package and version. This means you will
need to use two equals signs, such as `==`. There are other version matching
operators, for more information see [PEP 440](https://peps.python.org/pep-0440/#version-matching "https://peps.python.org/pep-0440/#version-matching").

To pass module installation options to `pip3`, use the [--python-modules-installer-option](#python-modules-installer-option "#python-modules-installer-option") parameter.

**`--auto-scale-within-microbatch`**

The default value is true. This parameter can only be used for AWS Glue streaming jobs, which process the streaming data in a series of micro batches, and auto scaling must be enabled. When setting this value to false, it computes the exponential moving average of batch duration for completed micro-batches and compares this value with the window size to determine whether to scale up or scale down the number of executors. Scaling only happens when a micro batch is completed. When setting this value to true, during a micro-batch, it scales up when the number of Spark tasks remains the same for 30 seconds, or the current batch processing is greater than the window size. The number of executors will drop if an executor has been idle for more than 60 seconds, or the exponential moving average of batch duration is low.

**`--class`**

The Scala class that serves as the entry point for your Scala script. This applies
only if your `--job-language` is set to `scala`.

**`--continuous-log-conversionPattern`**

Specifies a custom conversion log pattern for a job enabled for continuous logging.
The conversion pattern applies only to driver logs and executor logs. It does not affect
the AWS Glue progress bar.

**`--continuous-log-logGroup`**

Specifies a custom Amazon CloudWatch log group name for a job enabled for continuous
logging.

**`--continuous-log-logStreamPrefix`**

Specifies a custom CloudWatch log stream prefix for a job enabled for continuous
logging.

**`--customer-driver-env-vars` and `--customer-executor-env-vars`**

These parameters set environment variables on the operating system respectively for each worker (driver or executor). You can use these parameters when building platforms and custom frameworks on top of AWS Glue, to let your users write jobs on top of it. Enabling these two flags will allow you to set different environment variables on the driver and executor respectively without having to inject the same logic in the job script itself.

###### Example usage

The following is an example of using these parameters:

```
"—customer-driver-env-vars", "CUSTOMER_KEY1=VAL1,CUSTOMER_KEY2=\"val2,val2 val2\"",
"—customer-executor-env-vars", "CUSTOMER_KEY3=VAL3,KEY4=VAL4"

```

Setting these in the job run argument is equivalent to running the following commands:

In the driver:

- export CUSTOMER_KEY1=VAL1
- export CUSTOMER_KEY2="val2,val2 val2"

In the executor:

- export CUSTOMER_KEY3=VAL3

Then, in the job script itself, you can retrieve the environment variables using `os.environ.get("CUSTOMER_KEY1")` or `System.getenv("CUSTOMER_KEY1")`.

###### Enforced syntax

Observe the following standards when defining environment variables:

- Each key must have the `CUSTOMER_ prefix`.

For example: for `"CUSTOMER_KEY3=VAL3,KEY4=VAL4"`, `KEY4=VAL4` will be ignored and not set.

- Each key and value pair must be delineated with a single comma.

For example: `"CUSTOMER_KEY3=VAL3,CUSTOMER_KEY4=VAL4"`

- If the "value" has spaces or commas, then it must be defined within quotations.

For example: `CUSTOMER_KEY2=\"val2,val2 val2\"`

This syntax closely models the standards of setting bash environment variables.

**`--datalake-formats`**

Supported in AWS Glue 3.0 and later versions.

Specifies the data lake framework to use. AWS Glue adds the required JAR files for the
frameworks that you specify into the `classpath`. For more information, see
[Using data lake
frameworks with AWS Glue ETL jobs](aws-glue-programming-etl-datalake-native-frameworks.md "aws-glue-programming-etl-datalake-native-frameworks.md").

You can specify one or more of the following values, separated by a comma:

- `hudi`
- `delta`
- `iceberg`

For example, pass the following argument to specify all three frameworks.

```
'--datalake-formats': 'hudi,delta,iceberg'
```

**`--disable-proxy-v2`**

Disable the service proxy to allow AWS service calls to Amazon S3, CloudWatch, and
AWS Glue originating from your script through your VPC. For more
information, see [Configuring
AWS calls to go through your VPC](connection-VPC-disable-proxy.md "connection-VPC-disable-proxy.md") . To disable the service proxy, set the value of this paramater to `true`.

**`--enable-auto-scaling`**

Turns on auto scaling and per-worker billing when you set the value to
`true`.

**`--enable-continuous-cloudwatch-log`**

Enables real-time continuous logging for AWS Glue jobs. You can view
real-time Apache Spark job logs in CloudWatch.

**`--enable-continuous-log-filter`**

Specifies a standard filter (`true`) or no filter (`false`) when
you create or edit a job enabled for continuous logging. Choosing the standard filter
prunes out non-useful Apache Spark driver/executor and Apache Hadoop YARN heartbeat log
messages. Choosing no filter gives you all the log messages.

**`--enable-glue-datacatalog`**

Enables you to use the AWS Glue Data Catalog as an Apache Spark Hive metastore. To enable this
feature, set the value to `true`.

**`--enable-job-insights`**

Enables additional error analysis monitoring with AWS Glue job run insights. For details,
see [Monitoring with AWS Glue job run insights](monitor-job-insights.md "monitor-job-insights.md"). By default, the value is set to
`true` and job run insights are enabled.

This option is available for AWS Glue version 2.0 and 3.0.

**`--enable-lakeformation-fine-grained-access`**

Enables fine-grained access control for AWS Glue jobs. For more information, see [Using AWS Glue with AWS Lake Formation for fine-grained access control](security-lf-enable.md "security-lf-enable.md").

**`--enable-metrics`**

Enables the collection of metrics for job profiling for this job run. These metrics
are available on the AWS Glue console and the Amazon CloudWatch console.
The value of this parameter is not relevant. To enable this feature,
you can provide this parameter with any value, but `true` is recommended for clarity.
To disable this feature, remove this parameter from your job configuration.

**`--enable-observability-metrics`**

Enables a set of Observability metrics to generate insights into what is happening inside each job run on Job Runs
Monitoring page under AWS Glue console and the Amazon CloudWatch console. To enable this feature,
set the value of this parameter to true.
To disable this feature, set it to `false` or remove this parameter from your job configuration.

**`--enable-rename-algorithm-v2`**

Sets the EMRFS rename algorithm version to version 2. When a Spark job uses dynamic
partition overwrite mode, there is a possibility that a duplicate partition is created.
For instance, you can end up with a duplicate partition such as
`s3://bucket/table/location/p1=1/p1=1`. Here, P1 is the partition that is
being overwritten. Rename algorithm version 2 fixes this issue.

This option is only available on AWS Glue version 1.0.

**`--enable-s3-parquet-optimized-committer`**

Enables the EMRFS S3-optimized committer for writing Parquet data into Amazon S3. You can
supply the parameter/value pair via the AWS Glue console when creating or
updating an AWS Glue job. Setting the value to `true`
enables the committer. By default, the flag is turned on in AWS Glue 3.0 and off in AWS Glue
2.0.

For more information, see [Using the EMRFS S3-optimized Committer](../../../emr/latest/ReleaseGuide/emr-spark-s3-optimized-committer.md "../../../emr/latest/ReleaseGuide/emr-spark-s3-optimized-committer.md").

**`--enable-spark-ui`**

When set to `true`, turns on the feature to use the Spark UI to monitor and
debug AWS Glue ETL jobs.

**`--executor-cores`**

Number of spark tasks that can run in parallel. This option is supported on AWS Glue 3.0+. The value should not exceed 2x the number of vCPUs on the worker type, which is 8 on `G.1X`, 16 on `G.2X`, 32 on `G.4X`, 64 on `G.8X`, 96 on `G.12X`, 128 on `G.16X`, and 8 on `R.1X`, 16 on `R.2X`, 32 on `R.4X`, 64 on `R.8X`. You should exercise caution while updating this configuration as it could impact job performance because increased task parallelism causes memory, disk pressure as well as it could throttle the source and target systems (for example: it would cause more concurrent connections on Amazon RDS).

**`--extra-files`**

The Amazon S3 paths to additional files, such as configuration files that
AWS Glue copies to the working directory of your script on the driver node before running it.
Multiple values must be complete paths separated by a comma (`,`). The value can be individual files or directory locations.
This option is not supported for Python Shell job types.

**`--extra-jars`**

The Amazon S3 paths to additional files that AWS Glue copies to the driver and executors. AWS Glue also adds these files to the Java classpath before executing your script. Multiple
values must be complete paths separated by a comma (`,`). The extension need not be `.jar`

**`--extra-py-files`**

The Amazon S3 paths to additional Python modules that AWS Glue adds to the
Python path on the driver node before running your script. Multiple values must be complete paths separated
by a comma (`,`). Only individual files are supported, not a directory
path.

**`--job-bookmark-option`**

Controls the behavior of a job bookmark. The following option values can be
set.

| ‑‑job‑bookmark‑option value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `job-bookmark-enable`       | Keep track of previously processed data. When a job runs, process new data since the last checkpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `job-bookmark-disable`      | Always process the entire dataset. You are responsible for managing the output from previous job runs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `job-bookmark-pause`        | Process incremental data since the last successful run or the data in the range identified by the following suboptions, without updating the state of the last bookmark. You are responsible for managing the output from previous job runs. The two suboptions are as follows: <br>• **`job-bookmark-from`** `<from-value>` is the run ID that represents all the input that was processed until the last successful run before and including the specified run ID. The corresponding input is ignored. <br>• **`job-bookmark-to`**`<to-value>` is the run ID that represents all the input that was processed until the last successful run before and including the specified run ID. The corresponding input excluding the input identified by the `<from-value>` is processed by the job. Any input later than this input is also excluded for processing. The job bookmark state is not updated when this option set is specified. The suboptions are optional. However, when used, both suboptions must be provided. | For example, to enable a job bookmark, pass the following argument. `'--job-bookmark-option': 'job-bookmark-enable'` **`--job-language`** The script programming language. This value must be either `scala` or `python`. If this parameter is not present, the default is `python`. **`--python-modules-installer-option`** A plaintext string that defines options to be passed to `pip3` when installing modules with [--additional-python-modules](#additional-python-modules "#additional-python-modules"). Provide options as you would in the command line, separated by spaces and prefixed by dashes. For more information about usage, see [Installing additional Python modules with pip in AWS Glue 2.0 or later](aws-glue-programming-python-libraries.md#addl-python-modules-support "aws-glue-programming-python-libraries.md#addl-python-modules-support"). ###### Note This option is not supported for AWS Glue jobs when you use Python 3.9. **`--scriptLocation`** The Amazon Simple Storage Service (Amazon S3) location where your ETL script is located (in the form `s3://path/to/my/script.py`). This parameter overrides a script location set in the `JobCommand` object. **`--spark-event-logs-path`** Specifies an Amazon S3 path. When using the Spark UI monitoring feature, AWS Glue flushes the Spark event logs to this Amazon S3 path every 30 seconds to a bucket that can be used as a temporary directory for storing Spark UI events. **`--TempDir`** Specifies an Amazon S3 path to a bucket that can be used as a temporary directory for the job. For example, to set a temporary directory, pass the following argument. ``'--TempDir': '`s3-path-to-directory`'`` ###### Note AWS Glue creates a temporary bucket for jobs if a bucket doesn't already exist in a Region. This bucket might permit public access. You can either modify the bucket in Amazon S3 to set the public access block, or delete the bucket later after all jobs in that Region have completed. **`--use-postgres-driver`** When setting this value to `true`, it prioritizes the Postgres JDBC driver in the class path to avoid a conflict with the Amazon Redshift JDBC driver. This option is only available in AWS Glue version 2.0. **`--user-jars-first`** When setting this value to `true`, it prioritizes the customer's extra JAR files in the classpath. This option is only available in AWS Glue version 2.0 or later. **`--conf`** Controls Spark config parameters. It is for advanced use cases. **`--encryption-type`** Legacy parameter. The corresponding behavior should be configured using security configurations. for more information about security configurations, see [Encrypting data written by AWS Glue](encryption-security-configuration.md "encryption-security-configuration.md"). AWS Glue uses the following arguments internally and you should never use them: <br>• `--debug` — Internal to AWS Glue. Do not set. <br>• `--mode` — Internal to AWS Glue. Do not set. <br>• `--JOB_NAME` — Internal to AWS Glue. Do not set. <br>• `--endpoint` — Internal to AWS Glue. Do not set. ## AWS Glue supports bootstrapping an environment with Python's `site` module using `sitecustomize` to perform site-specific customizations. Bootstrapping your own initilization functions is recommended for advanced use cases only and is supported on a best-effort basis on AWS Glue 4.0. The environment variable prefix, `GLUE_CUSTOMER`, is reserved for customer use. |
