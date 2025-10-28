# Submit a job run with

`StartJobRun`

###### To submit a job run with a JSON file with specified parameters

1. Create a `start-job-run-request.json` file and specify the required
   parameters for your job run, as the following example JSON file demonstrates. For more
   information about the parameters, see [Options for configuring a job run](emr-eks-jobs-CLI.md#emr-eks-jobs-parameters "emr-eks-jobs-CLI.md#emr-eks-jobs-parameters").

```
{
  "name": "`myjob`",
  "virtualClusterId": "`123456`",
  "executionRoleArn": "`iam_role_name_for_job_execution`",
  "releaseLabel": "`emr-6.2.0-latest`",
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "`entryPoint_location`",
      "entryPointArguments": ["`argument1`", "`argument2`", ...],
       "sparkSubmitParameters": "--class <main_class> --conf spark.executor.instances=2 --conf spark.executor.memory=2G --conf spark.executor.cores=2 --conf spark.driver.cores=1"
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
        "logStreamNamePrefix": "`log_stream_prefix`"
      },
      "s3MonitoringConfiguration": {
        "logUri": "s3://`my_s3_log_location`"
      }
    }
  }
}
```

2. Use the `start-job-run` command with a path to the
   `start-job-run-request.json` file stored locally.

```
aws emr-containers start-job-run \
--cli-input-json `file://./start-job-run-request.json`
```

###### To start a job run using the `start-job-run` command

1. Supply all the specified parameters in the `StartJobRun` command, as
   the following example demonstrates.

```
aws emr-containers start-job-run \
--virtual-cluster-id `123456` \
--name `myjob` \
--execution-role-arn `execution-role-arn` \
--release-label `emr-6.2.0-latest` \
--job-driver '{"sparkSubmitJobDriver": {"entryPoint": "`entryPoint_location`", "entryPointArguments": ["`argument1`", "`argument2`", ...], "sparkSubmitParameters": "--class <main_class> --conf spark.executor.instances=2 --conf spark.executor.memory=2G --conf spark.executor.cores=2 --conf spark.driver.cores=1"}}' \
--configuration-overrides '{"applicationConfiguration": [{"classification": "spark-defaults", "properties": {"spark.driver.memory": "2G"}}], "monitoringConfiguration": {"cloudWatchMonitoringConfiguration": {"logGroupName": "`log_group_name`", "logStreamNamePrefix": "`log_stream_prefix`"}, "persistentAppUI":"ENABLED",  "s3MonitoringConfiguration": {"logUri": "s3://`my_s3_log_location`" }}}'

```

2. For Spark SQL, supply all the specified parameters in the `StartJobRun`
   command, as the following example demonstrates.

```
aws emr-containers start-job-run \
--virtual-cluster-id `123456` \
--name `myjob` \
--execution-role-arn `execution-role-arn` \
--release-label `emr-6.7.0-latest` \
--job-driver '{"sparkSqlJobDriver": {"entryPoint": "`entryPoint_location`", "sparkSqlParameters": "--conf spark.executor.instances=2 --conf spark.executor.memory=2G --conf spark.executor.cores=2 --conf spark.driver.cores=1"}}' \
--configuration-overrides '{"applicationConfiguration": [{"classification": "spark-defaults", "properties": {"spark.driver.memory": "2G"}}], "monitoringConfiguration": {"cloudWatchMonitoringConfiguration": {"logGroupName": "`log_group_name`", "logStreamNamePrefix": "`log_stream_prefix`"}, "persistentAppUI":"ENABLED",  "s3MonitoringConfiguration": {"logUri": "s3://`my_s3_log_location`" }}}'

```
