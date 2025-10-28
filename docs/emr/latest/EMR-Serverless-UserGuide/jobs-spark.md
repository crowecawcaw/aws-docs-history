# Using Spark configurations when you run EMR Serverless jobs

You can run Spark jobs on an application with the `type` parameter set to
`SPARK`. Jobs must be compatible with the Spark version compatible with the Amazon EMR
release version. For example, when you run jobs with Amazon EMR release 6.6.0, your job must be
compatible with Apache Spark 3.2.0. For information on the application versions for each
release, refer to [Amazon EMR Serverless release versions](release-versions.md "release-versions.md").

## Spark job parameters

When you use the [`StartJobRun`
API](../../../emr-serverless/latest/APIReference/API_StartJobRun.md "../../../emr-serverless/latest/APIReference/API_StartJobRun.md") to run a Spark job, specify the following parameters.

###### Required parameters

- [Spark job runtime role](#spark-defaults-executionRoleArn "#spark-defaults-executionRoleArn")
- [Spark job driver parameter](#spark-defaults-jobDriver "#spark-defaults-jobDriver")
- [Spark configuration override
  parameter](#spark-defaults-configurationOverrides "#spark-defaults-configurationOverrides")
- [Spark dynamic resource allocation optimization](#spark-defaults-dynamicResourceAllocation "#spark-defaults-dynamicResourceAllocation")

### Spark job runtime role

Use **`executionRoleArn`** to specify the ARN
for the IAM role that your application uses to execute Spark jobs. This role must
contain the following permissions:

- Read from S3 buckets or other data sources where your data resides
- Read from S3 buckets or prefixes where your PySpark script or JAR file
  resides
- Write to S3 buckets where you intend to write your final output
- Write logs to a S3 bucket or prefix that
  `S3MonitoringConfiguration`specifies
- Access to KMS keys if you use KMS keys to encrypt data in your S3
  bucket
- Access to the AWS Glue Data Catalog if you use SparkSQL

If your Spark job reads or writes data to or from other data sources, specify the
appropriate permissions in this IAM role. If you don't provide these permissions to the
IAM role, the job might fail. For more information, refer to [Job runtime roles for Amazon EMR Serverless](security-iam-runtime-role.md "security-iam-runtime-role.md") and
[Storing logs](logging.md "logging.md").

### Spark job driver parameter

Use **`jobDriver`** to provide input to the
job. The job driver parameter accepts only one value for the job type that you want to
run. For a Spark job, the parameter value is `sparkSubmit`. You can use this
job type to run Scala, Java, PySpark, and any other supported jobs through Spark
submit. Spark jobs have the following parameters:

- **`sparkSubmitParameters`** – These
  are the additional Spark parameters that you want to send to the job. Use this
  parameter to override default Spark properties such as driver memory or number of
  executors, like those defined in the `--conf` or `--class`
  arguments.
- **`entryPointArguments`** – This is
  an array of arguments that you want to pass to your main JAR or Python file. You
  should handle reading these parameters using your entrypoint code. Separate each
  argument in the array by a comma.
- **`entryPoint`** – This is the
  reference in Amazon S3 to the main JAR or Python file that you want to run. If you are
  running a Scala or Java JAR, specify the main entry class in the
  `SparkSubmitParameters` using the `--class` argument.

For additional information, refer to [Launching Applications with spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit "https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit").

### Spark configuration override

parameter

Use **`configurationOverrides`** to override
monitoring-level and application-level configuration properties. This parameter accepts a
JSON object with the following two fields:

- **`monitoringConfiguration`** ‐ Use
  this field to specify the Amazon S3 URL (`s3MonitoringConfiguration`) where you
  want the EMR Serverless job to store logs of your Spark job. Make sure you've created
  this bucket with the same AWS account that hosts your application, and in the same
  AWS Region where your job is running.
- **`applicationConfiguration`** – To
  override the default configurations for applications, you can provide a configuration
  object in this field. You can use a shorthand syntax to provide the configuration, or
  you can reference the configuration object in a JSON file. Configuration objects
  consist of a classification, properties, and optional nested configurations.
  Properties consist of the settings that you want to override in that file. You can
  specify multiple classifications for multiple applications in a single JSON
  object.

###### Note

Available configuration classifications vary by specific EMR Serverless
release. For example, classifications for custom Log4j
`spark-driver-log4j2` and `spark-executor-log4j2` are only
available with releases 6.8.0 and higher.

If you use the same configuration in an application override and in Spark submit
parameters, the Spark submit parameters take priority. Configurations rank in priority as
follows, from highest to lowest:

- Configuration that EMR Serverless provides when it creates
  `SparkSession`.
- Configuration that you provide as part of `sparkSubmitParameters` with
  the `--conf` argument.
- Configuration that you provide as part of your application overrides when you
  start a job.
- Configuration that you provide as part of your `runtimeConfiguration`
  when you create an application.
- Optimized configurations that Amazon EMR uses for the release.
- Default open source configurations for the application.

For more information on declaring configurations at the application level, and
overriding configurations during job run, refer to [Default application configuration for EMR Serverless](default-configs.md "default-configs.md").

### Spark dynamic resource allocation optimization

Use `dynamicAllocationOptimization` to optimize resource usage in EMR Serverless. Setting
this property to `true` in your Spark configuration classification indicates to EMR Serverless to optimize executor resource allocation to better align the rate
at which Spark requests and cancels executors with the rate at which EMR Serverless creates and releases workers. By doing so, EMR Serverless more optimally
reuses workers across stages, resulting in lower cost when running jobs with multiple stages while maintaining the same performance.

This property is available in all Amazon EMR release versions.

The following is a sample configuration classification with `dynamicAllocationOptimization`.

```
[
  {
    "Classification": "spark",
    "Properties": {
      "dynamicAllocationOptimization": "true"
    }
  }
]
```

Consider the following if you're using dynamic allocation optimization:

- This optimization is available for the Spark jobs for which you enabled dynamic resource allocation.
- To achieve the best cost efficiency, we suggest configuration of an upper scaling bound on workers using either
  the job-level setting `spark.dynamicAllocation.maxExecutors` or the [application-level maxium capacity](app-behavior.md#max-capacity "app-behavior.md#max-capacity")
  setting based on your workload.
- You might not notice cost improvement in simpler jobs. For example, if your job runs on a small dataset or finishes
  running in one stage, Spark might not need a larger number of executors or multiple scaling events.
- Jobs with a sequence of a large stage, smaller stages, and then a large stage again might experience regression in job runtime. As EMR Serverless uses
  resources more efficiently, it might lead to fewer available workers for larger stages, leading to longer runtime.

## Spark job properties

The following table lists optional Spark properties and their default values that you
can override when you submit a Spark job.

| Optional Spark properties and default values       | Key                                                                                                                                                                                                                                                                                                 | Description                                                  | Default value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ----------- | ------------- |
| `spark.archives`                                   | A comma-separated list of archives that Spark extracts into each executor's working directory. Supported file types include `.jar`,`.tar.gz`, `.tgz` and `.zip`. To specify the directory name to extract, add `#` after the file name that you want to extract. For example, `file.zip#directory`. | `NULL`                                                       |
| `spark.authenticate`                               | Option that turns on authentication of Spark's internal connections.                                                                                                                                                                                                                                | `TRUE`                                                       |
| `spark.driver.cores`                               | The number of cores that the driver uses.                                                                                                                                                                                                                                                           | 4                                                            |
| `spark.driver.extraJavaOptions`                    | Extra Java options for the Spark driver.                                                                                                                                                                                                                                                            | `NULL`                                                       |
| `spark.driver.memory`                              | The amount of memory that the driver uses.                                                                                                                                                                                                                                                          | 14G                                                          |
| `spark.dynamicAllocation.enabled`                  | Option that turns on dynamic resource allocation. This option scales up or down the number of executors registered with the application, based on the workload.                                                                                                                                     | `TRUE`                                                       |
| `spark.dynamicAllocation.executorIdleTimeout`      | The length of time that an executor can remain idle before Spark removes it. This only applies if you turn on dynamic allocation.                                                                                                                                                                   | 60s                                                          |
| `spark.dynamicAllocation.initialExecutors`         | The initial number of executors to run if you turn on dynamic allocation.                                                                                                                                                                                                                           | `3`                                                          |
| `spark.dynamicAllocation.maxExecutors`             | The upper bound for the number of executors if you turn on dynamic allocation.                                                                                                                                                                                                                      | For 6.10.0 and higher, `infinity` For 6.9.0 and lower, `100` |
| `spark.dynamicAllocation.minExecutors`             | The lower bound for the number of executors if you turn on dynamic allocation.                                                                                                                                                                                                                      | `0`                                                          |
| `spark.emr-serverless.allocation.batch.size`       | The number of containers to request in each cycle of executor allocation. There is a one-second gap between each allocation cycle.                                                                                                                                                                  | 20                                                           |
| `spark.emr-serverless.driver.disk`                 | The Spark driver disk.                                                                                                                                                                                                                                                                              | 20G                                                          |
| `spark.emr-serverless.driverEnv.`[KEY]``           | Option that adds environment variables to the Spark driver.                                                                                                                                                                                                                                         | `NULL`                                                       |
| `spark.emr-serverless.executor.disk`               | The Spark executor disk.                                                                                                                                                                                                                                                                            | 20G                                                          |
| `spark.emr-serverless.memoryOverheadFactor`        | Sets the memory overhead to add to the driver and executor container memory.                                                                                                                                                                                                                        | 0.1                                                          |
| `spark.emr-serverless.driver.disk.type`            | The disk type attached to Spark driver.                                                                                                                                                                                                                                                             | Standard                                                     |
| `spark.emr-serverless.executor.disk.type`          | The disk type attached to Spark executors.                                                                                                                                                                                                                                                          | Standard                                                     |
| `spark.executor.cores`                             | The number of cores that each executor uses.                                                                                                                                                                                                                                                        | 4                                                            |
| `spark.executor.extraJavaOptions`                  | Extra Java options for the Spark executor.                                                                                                                                                                                                                                                          | `NULL`                                                       |
| `spark.executor.instances`                         | The number of Spark executor containers to allocate.                                                                                                                                                                                                                                                | 3                                                            |
| `spark.executor.memory`                            | The amount of memory that each executor uses.                                                                                                                                                                                                                                                       | 14G                                                          |
| `spark.executorEnv.`[KEY]``                        | Option that adds environment variables to the Spark executors.                                                                                                                                                                                                                                      | `NULL`                                                       |
| `spark.files`                                      | A comma-separated list of files to go in the working directory of each executor. You can access the file paths of these files in the executor with `SparkFiles.get(`fileName`)`.                                                                                                                    | `NULL`                                                       |
| `spark.hadoop.hive.metastore.client.factory.class` | The Hive metastore implementation class.                                                                                                                                                                                                                                                            | `NULL`                                                       |
| `spark.jars`                                       | Additional jars to add to the runtime classpath of the driver and executors.                                                                                                                                                                                                                        | `NULL`                                                       |
| `spark.network.crypto.enabled`                     | Option that turns on AES-based RPC encryption. This includes the authentication protocol added in Spark 2.2.0.                                                                                                                                                                                      | `FALSE`                                                      |
| `spark.sql.warehouse.dir`                          | The default location for managed databases and tables.                                                                                                                                                                                                                                              | The value of `$PWD/spark-warehouse`                          |
| `spark.submit.pyFiles`                             | A comma-separated list of `.zip`, `.egg`, or`.py` files to place in the `PYTHONPATH` for Python apps.                                                                                                                                                                                               | `NULL`                                                       | The following table lists the default Spark submit parameters. Default Spark submit parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Key | Description | Default value |
| ---                                                | ---                                                                                                                                                                                                                                                                                                 | ---                                                          |
| `archives`                                         | A comma-separated list of archives that Spark extracts into each executor's working directory.                                                                                                                                                                                                      | `NULL`                                                       |
| `class`                                            | The application's main class (for Java and Scala apps).                                                                                                                                                                                                                                             | `NULL`                                                       |
| `conf`                                             | An arbitrary Spark configuration property.                                                                                                                                                                                                                                                          | `NULL`                                                       |
| `driver-cores`                                     | The number of cores that the driver uses.                                                                                                                                                                                                                                                           | 4                                                            |
| `driver-memory`                                    | The amount of memory that the driver uses.                                                                                                                                                                                                                                                          | 14G                                                          |
| `executor-cores`                                   | The number of cores that each executor uses.                                                                                                                                                                                                                                                        | 4                                                            |
| `executor-memory`                                  | The amount of memory that the executor uses.                                                                                                                                                                                                                                                        | 14G                                                          |
| `files`                                            | A comma-separated list of files to place in the working directory of each executor. You can access the file paths of these files in the executor with `SparkFiles.get(`fileName`)`.                                                                                                                 | `NULL`                                                       |
| `jars`                                             | A comma-separated list of jars to include on the driver and executor classpaths.                                                                                                                                                                                                                    | `NULL`                                                       |
| `num-executors`                                    | The number of executors to launch.                                                                                                                                                                                                                                                                  | 3                                                            |
| `py-files`                                         | A comma-separated list of `.zip`, `.egg`, or `.py` files to place on the `PYTHONPATH` for Python apps.                                                                                                                                                                                              | `NULL`                                                       |
| `verbose`                                          | Option that turns on additional debug output.                                                                                                                                                                                                                                                       | `NULL`                                                       | ## Resource configuration best practices ### Configuring driver and executor resources via the StartJobRun API ###### Note Spark driver and executor cores and memory properties, if specified, must be directly specified in the StartJobRun API request. Configuring your resources in this manner ensures that EMR Serverless can allocate the correct resources before running the job. This is in contrast to settings provided in the user script, such as in the .py or .jar file, which are evaluated too late, as driver and executor workers are sometimes pre-provisioned before script execution begins. There are two supported ways to configure these resources during job submission: #### Option 1: Use sparkSubmitParameters `"jobDriver": { "sparkSubmit": { "entryPoint": "s3://your-script-path.py", "sparkSubmitParameters": "—conf spark.driver.memory=4g \ —conf spark.driver.cores=2 \ —conf spark.executor.memory=8g \ —conf spark.executor.cores=4" } }` #### Option 2: Use configurationOverrides for the spark-defaults classification `"configurationOverrides": { "applicationConfiguration": [ { "classification": "spark-defaults", "properties": { "spark.driver.memory": "4g", "spark.driver.cores": "2", "spark.executor.memory": "8g", "spark.executor.cores": "4" } } ] }` ## Spark examples The following example shows how to use the `StartJobRun` API to run a Python script. For an end-to-end tutorial that uses this example, refer to [Getting started with Amazon EMR Serverless](getting-started.md "getting-started.md"). You can find additional examples of how to run PySpark jobs and add Python dependencies in the [EMR Serverless Samples](https://github.com/aws-samples/emr-serverless-samples/tree/main/examples/pyspark "https://github.com/aws-samples/emr-serverless-samples/tree/main/examples/pyspark") GitHub repository. ``aws emr-serverless start-job-run \ --application-id `application-id` \ --execution-role-arn `job-role-arn` \ --job-driver '{ "sparkSubmit": { "entryPoint": "s3://us-east-1.elasticmapreduce/emr-containers/samples/wordcount/scripts/wordcount.py", "entryPointArguments": ["s3://`amzn-s3-demo-destination-bucket`/wordcount_output"], "sparkSubmitParameters": "--conf spark.executor.cores=1 --conf spark.executor.memory=4g --conf spark.driver.cores=1 --conf spark.driver.memory=4g --conf spark.executor.instances=1" } }'`` The following example shows how to use the `StartJobRun` API to run a Spark JAR. ``aws emr-serverless start-job-run \ --application-id `application-id` \ --execution-role-arn `job-role-arn` \ --job-driver '{ "sparkSubmit": { "entryPoint": "/usr/lib/spark/examples/jars/spark-examples.jar", "entryPointArguments": ["1"], "sparkSubmitParameters": "--class org.apache.spark.examples.SparkPi --conf spark.executor.cores=4 --conf spark.executor.memory=20g --conf spark.driver.cores=4 --conf spark.driver.memory=8g --conf spark.executor.instances=1" } }'`` |
