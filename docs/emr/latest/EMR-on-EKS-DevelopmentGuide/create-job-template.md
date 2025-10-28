# Create and using a job template to start a job

run

This section describes creating a job template and using the template to start a job run
with the AWS Command Line Interface (AWS CLI).

**To create a job template**

1. Create a `create-job-template-request.json` file and specify the required
   parameters for your job template, as shown in the following example JSON file. For
   information about all available parameters, see the [CreateJobTemplate](../../../emr-on-eks/latest/APIReference/Welcome.md "../../../emr-on-eks/latest/APIReference/Welcome.md")
   API.

Most values that are required for the `StartJobRun` API are also required
for `jobTemplateData`. If you want to use placeholders for any parameters and
provide values when invoking StartJobRun using a job template, please see the next
section on job template parameters.

```
{
   "name": "`mytemplate`",
   "jobTemplateData": {
        "executionRoleArn": "`iam_role_arn_for_job_execution`",
        "releaseLabel": "emr-6.7.0-latest",
        "jobDriver": {
            "sparkSubmitJobDriver": {
                "entryPoint": "`entryPoint_location`",
                "entryPointArguments": [ "`argument1`","`argument2`",...],
                "sparkSubmitParameters": "--class <`main_class`> --conf spark.executor.instances=2 --conf spark.executor.memory=2G --conf spark.executor.cores=2 --conf spark.driver.cores=1"
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
                    "logUri": "s3://`my_s3_log_location`/"
                }
            }
        }
     }
}
```

2. Use the `create-job-template` command with a path to the
   `create-job-template-request.json` file stored locally.

```
aws emr-containers create-job-template \
--cli-input-json file:`//./create-job-template-request.json`
```

**To start a job run using a job template**

Supply the virtual cluster id, job template id, and job name in the
`StartJobRun` command, as shown in the following example.

```
aws emr-containers start-job-run \
--virtual-cluster-id `123456` \
--name `myjob` \
--job-template-id `1234abcd`
```
