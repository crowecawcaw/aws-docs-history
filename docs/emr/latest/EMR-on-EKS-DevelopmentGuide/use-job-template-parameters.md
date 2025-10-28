# Defining job template parameters

Job template parameters allow you to specify variables in the job template. Values for
these parameter variables will need to be specified when starting a job run using that job
template. Job template parameters are specified in `${parameterName}` format. You
can choose to specify any value in a `jobTemplateData` field as a job template
parameter. For each of the job template parameter variables, specify its data type
(`STRING` or `NUMBER`) and optionally a default value. The example
below shows how you can specify job template parameters for entry point location, main
class, and S3 log location values.

**To specify entry point location, main class, and Amazon S3 log location
as job template parameters**

1. Create a `create-job-template-request.json` file and specify the required
   parameters for your job template, as shown in the following example JSON file. For more
   information about the parameters, see the [CreateJobTemplate](../../../emr-on-eks/latest/APIReference/Welcome.md "../../../emr-on-eks/latest/APIReference/Welcome.md")
   API.

```
{
   "name": "mytemplate",
   "jobTemplateData": {
        "executionRoleArn": "`iam_role_arn_for_job_execution`",
        "releaseLabel": "emr-6.7.0-latest",
        "jobDriver": {
            "sparkSubmitJobDriver": {
                "entryPoint": "${EntryPointLocation}",
                "entryPointArguments": [ "`argument1`","`argument2`",...],
                "sparkSubmitParameters": "--class ${MainClass} --conf spark.executor.instances=2 --conf spark.executor.memory=2G --conf spark.executor.cores=2 --conf spark.driver.cores=1"
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
                    "logUri": "${LogS3BucketUri}"
                }
            }
        },
        "parameterConfiguration": {
            "EntryPointLocation": {
                "type": "STRING"
            },
            "MainClass": {
                "type": "STRING",
                "defaultValue":"`Main`"
            },
            "LogS3BucketUri": {
                "type": "STRING",
                "defaultValue":"s3://`my_s3_log_location`/"
            }
        }
    }
}
```

2. Use the `create-job-template` command with a path to the
   `create-job-template-request.json` file stored locally or in Amazon S3.

```
aws emr-containers create-job-template \
--cli-input-json file:`//./create-job-template-request.json`
```

**To start a job run using job template with job template
parameters**

To start a job run with a job template containing job template parameters, specify the
job template id as well as values for job template parameters in the
`StartJobRun` API request as shown below.

```
aws emr-containers start-job-run \
--virtual-cluster-id `123456` \
--name `myjob` \
--job-template-id `1234abcd` \
--job-template-parameters '{"EntryPointLocation": "`entry_point_location`","MainClass": "`ExampleMainClass`","LogS3BucketUri": "s3://`example_s3_bucket`/"}'
```
