# Using Spark container log rotation

With Amazon EMR 6.11.0 and later, you can turn on the Spark container log rotation feature for
Amazon EMR on EKS. Instead of generating a single `stdout` or `stderr` log file,
this feature rotates the file based on your configured rotation size and removes the oldest
log files from the container.

Rotating Spark container logs can help you avoid potential issues with a large Spark log
files generated for long-running or streaming jobs. For example, you might start a
long-running Spark job, and the Spark driver generates a container log file. If the job runs
for hours or days and there is limited disk space on the Kubernetes node, the container log
file can consume all available disk space. When you turn on Spark container log rotation, you
split the log file into multiple files, and remove the oldest files.

To turn on the Spark container log rotation feature, configure the following Spark
parameters:

**`containerLogRotationConfiguration`**

Include this parameter in `monitoringConfiguration` to turn on log
rotation. It is disabled by default. You must use
`containerLogRotationConfiguration` in addition to
`s3MonitoringConfiguration`.

**`rotationSize`**

The `rotationSize` parameter specifies file size for the log rotation.
The range of possible values is from `2KB` to `2GB`. The numeric
unit portion of the `rotationSize` parameter is passed as an integer. Since
decimal values aren't supported, you can specify a rotation size of 1.5GB, for example,
with the value `1500MB`.

**`maxFilesToKeep`**

The `maxFilesToKeep` parameter specifies the maximum number of files to
retain in container after rotation has taken place. The minimum value is 1, and the
maximum value is 50.

You can specify these parameters in the `monitoringConfiguration` section of
the `StartJobRun` API, as the following example shows. In this example, with
`rotationSize = "10 MB"` and `maxFilesToKeep = 3`, Amazon EMR on EKS rotates
your logs at 10 MB, generates a new log file, and then purges the oldest log file once the
number of log files reaches 3.

```
{
  "name": "`my-long-running-job`",
  "virtualClusterId": "`123456`",
  "executionRoleArn": "`iam_role_name_for_job_execution`",
  "releaseLabel": "emr-6.11.0-latest",
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "`entryPoint_location`",
      "entryPointArguments": [`"argument1", "argument2", ...`],
       "sparkSubmitParameters": "--class `main_class` --conf spark.executor.instances=2 --conf spark.executor.memory=2G --conf spark.executor.cores=2 --conf spark.driver.cores=1"
    }
  },
  "configurationOverrides": {
    "applicationConfiguration": [
      {
        "classification": "spark-defaults",
        "properties": {
          "spark.driver.memory":"2G"
         }
      }
    ],
    "monitoringConfiguration": {
      "persistentAppUI": "ENABLED",
      "cloudWatchMonitoringConfiguration": {
        "logGroupName": "`my_log_group`",
        "logStreamNamePrefix": "log_stream_prefix"
      },
      "s3MonitoringConfiguration": {
        "logUri": "s3://`my_s3_log_location`"
      },
      "containerLogRotationConfiguration": {
        "rotationSize":"`10MB`",
        "maxFilesToKeep":"`3`"
      }
    }
  }
}
```

To start a job run with Spark container log rotation, include a path to the json file that
you configured with these parameters in the [StartJobRun](emr-eks-jobs-submit.md "emr-eks-jobs-submit.md") command.

```
aws emr-containers start-job-run \
--cli-input-json file://`path-to-json-request-file`
```
