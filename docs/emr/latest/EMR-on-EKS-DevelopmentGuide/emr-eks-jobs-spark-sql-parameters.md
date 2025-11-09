# Running Spark SQL scripts through the

StartJobRun API

Amazon EMR on EKS releases 6.7.0 and higher include a Spark SQL job driver so that you can run
Spark SQL scripts through the `StartJobRun` API. You can supply SQL entry-point
files to directly run Spark SQL queries on Amazon EMR on EKS with the `StartJobRun` API,
without any modifications to existing Spark SQL scripts. The following table lists Spark
parameters that are supported for the Spark SQL jobs through the StartJobRun API.

You can choose from the following Spark parameters to send to a Spark SQL job. Use these
parameters to override default Spark properties.

| Option                     | Description                                                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| --name NAME                | Application Name                                                                                                                                |
| --jars JARS                | Comma separated list of jars to be included with driver and execute<br>classpath.                                                               |
| --packages                 | Comma-separated list of maven coordinates of jars to include on the driver and<br>executor classpaths.                                          |
| --exclude-packages         | Comma-separated list of groupId:artifactId, to exclude while resolving the<br>dependencies provided in –packages to avoid dependency conflicts. |
| --repositories             | Comma-separated list of additional remote repositories to search for the maven<br>coordinates given with –packages.                             |
| --files FILES              | Comma-separated list of files to be placed in the working directory of each<br>executor.                                                        |
| --conf PROP=VALUE          | Spark configuration property.                                                                                                                   |
| --properties-file FILE     | Path to a file from which to load extra properties.                                                                                             |
| --driver-memory MEM        | Memory for driver. Default 1024MB.                                                                                                              |
| --driver-java-options      | Extra Java options to pass to the driver.                                                                                                       |
| --driver-library-path      | Extra library path entries to pass to the driver.                                                                                               |
| --driver-class-path        | Extra classpath entries to pass to the driver.                                                                                                  |
| --executor-memory MEM      | Memory per executor. Default 1GB.                                                                                                               |
| --driver-cores NUM         | Number of cores used by the driver.                                                                                                             |
| --total-executor-cores NUM | Total cores for all executors.                                                                                                                  |
| --executor-cores NUM       | Number of cores used by each executor.                                                                                                          |
| --num-executors NUM        | Number of executors to launch.                                                                                                                  |
| -hivevar <key=value>       | Variable substitution to apply to Hive commands, for example, `-hivevar<br>A=B`                                                                 |
| -hiveconf <property=value> | Value to use for the given property.                                                                                                            |

For a Spark SQL job, create a start-job-run-request.json file and specify the required
parameters for your job run, as in the following example:

```
{
  "name": "`myjob`",
  "virtualClusterId": "`123456`",
  "executionRoleArn": "`iam_role_name_for_job_execution`",
  "releaseLabel": "`emr-6.7.0-latest`",
  "jobDriver": {
    "sparkSqlJobDriver": {
      "entryPoint": "`entryPoint_location`",
       "sparkSqlParameters": "--conf spark.executor.instances=2 --conf spark.executor.memory=2G --conf spark.executor.cores=2 --conf spark.driver.cores=1"
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
