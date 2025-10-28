# Managing job runs with the AWS CLI

This topic covers how to manage job runs with the AWS Command Line Interface (AWS CLI). It goes into detail regarding properties, like security parameters, the driver, and various
override settings. It also includes subtopics that cover various ways to configure logging.

###### Topics

- [Options for configuring a job run](#emr-eks-jobs-parameters "#emr-eks-jobs-parameters")
- [Configure a job run to use Amazon S3 logs](emr-eks-jobs-s3.md "emr-eks-jobs-s3.md")
- [Configure a job run to use Amazon CloudWatch Logs](emr-eks-jobs-cloudwatch.md "emr-eks-jobs-cloudwatch.md")
- [List job runs](#emr-eks-jobs-list "#emr-eks-jobs-list")
- [Describe a job run](#emr-eks-jobs-describe "#emr-eks-jobs-describe")
- [Cancel a job run](#emr-eks-jobs-cancel "#emr-eks-jobs-cancel")

## Options for configuring a job run

Use the following options to configure job run parameters:

- `--execution-role-arn`: You must provide an IAM role that is used for
  running jobs. For more information, see [Using job execution roles with Amazon EMR on EKS](iam-execution-role.md "iam-execution-role.md").
- `--release-label`: You can deploy Amazon EMR on EKS with Amazon EMR versions 5.32.0
  and 6.2.0 and later. Amazon EMR on EKS is not supported in previous Amazon EMR release versions.
  For more information, see [Amazon EMR on EKS releases](emr-eks-releases.md "emr-eks-releases.md").
- `--job-driver`: Job driver is used to provide input on the main job.
  This is a union type field where you can only pass one of the values for the job type
  that you want to run. Supported job types include:
  - Spark submit jobs - Used to run a command through Spark submit. You can use
    this job type to run Scala, PySpark, SparkR, SparkSQL and any other supported jobs
    through Spark Submit. This job type has the following parameters:
    - Entrypoint - This is the HCFS (Hadoop compatible file system) reference to
      the main jar/py file you want to run.
    - EntryPointArguments - This is an array of arguments you want to pass to
      your main jar/py file. You should handle reading these parameters using your
      entrypoint code. Each argument in the array should be separated by a comma.
      EntryPointArguments cannot contain brackets or parentheses, such as (), {}, or
      [].
    - SparkSubmitParameters - These are the additional spark parameters you want
      to send to the job. Use this parameter to override default Spark properties
      such as driver memory or number of executors like —conf or —class. For
      additional information, see [Launching Applications with spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit "https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit").

  - Spark SQL jobs - Used to run a SQL query file through Spark SQL. You can use
    this job type to run SparkSQL jobs. This job type has the following
    parameters:
    - Entrypoint - This is the HCFS (Hadoop compatible file system) reference to
      the SQL query file you want to run.

    For a list of additional Spark parameters you can use for a Spark SQL job,
    see [Running Spark SQL scripts through the
    StartJobRun API](emr-eks-jobs-spark-sql-parameters.md "emr-eks-jobs-spark-sql-parameters.md").

- `--configuration-overrides`: You can override the default
  configurations for applications by supplying a configuration object. You can use a
  shorthand syntax to provide the configuration or you can reference the configuration
  object in a JSON file. Configuration objects consist of a classification, properties,
  and optional nested configurations. Properties consist of the settings you want to
  override in that file. You can specify multiple classifications for multiple
  applications in a single JSON object. The configuration classifications that are
  available vary by Amazon EMR release version. For a list of configuration classifications
  that are available for each release version of Amazon EMR, see [Amazon EMR on EKS releases](emr-eks-releases.md "emr-eks-releases.md").

If you pass the same configuration in an application override and in Spark submit
parameters, the Spark submit parameters take precedence. The complete configuration
priority list follows, in order of highest priority to lowest priority.

    + Configuration supplied when creating `SparkSession`.
    + Configuration supplied as part of `sparkSubmitParameters` using
     `—conf`.
    + Configuration provided as part of application overrides.
    + Optimized configurations chosen by Amazon EMR for the release.
    + Default open source configurations for the application.

To monitor job runs using Amazon CloudWatch or Amazon S3, you must provide the configuration
details for CloudWatch. For more information, see [Configure a job run to use Amazon S3 logs](emr-eks-jobs-s3.md "emr-eks-jobs-s3.md") and [Configure a job run to use Amazon CloudWatch Logs](emr-eks-jobs-cloudwatch.md "emr-eks-jobs-cloudwatch.md"). If the S3 bucket or CloudWatch log group does
not exist, then Amazon EMR creates it before uploading logs to the bucket.

- For an additional list of Kubernetes configuration options, see [Spark Properties on Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html#configuration "https://spark.apache.org/docs/latest/running-on-kubernetes.html#configuration").

The following Spark configurations are not supported.

    + `spark.kubernetes.authenticate.driver.serviceAccountName`
    + `spark.kubernetes.authenticate.executor.serviceAccountName`
    + `spark.kubernetes.namespace`
    + `spark.kubernetes.driver.pod.name`
    + `spark.kubernetes.container.image.pullPolicy`
    + `spark.kubernetes.container.image`


    ###### Note

    You can use `spark.kubernetes.container.image` for customized
     Docker images. For more information, see [Customizing Docker images for Amazon EMR on EKS](docker-custom-images.md "docker-custom-images.md").

## List job runs

You can run `list-job-run` to show the states of job runs, as the following
example demonstrates.

```
aws emr-containers list-job-runs --virtual-cluster-id <cluster-id>
```

## Describe a job run

You can run `describe-job-run` to get more details about the job, such as
job state, state details, and job name, as the following example demonstrates.

```
aws emr-containers describe-job-run --virtual-cluster-id `cluster-id` --id `job-run-id`
```

## Cancel a job run

You can run `cancel-job-run` to cancel running jobs, as the following
example demonstrates.

```
aws emr-containers cancel-job-run --virtual-cluster-id `cluster-id` --id `job-run-id`
```
