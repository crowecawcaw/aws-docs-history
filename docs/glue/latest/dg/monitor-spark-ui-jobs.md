# Enabling the Apache Spark web UI for AWS Glue jobs

You can use the Apache Spark web UI to monitor and debug AWS Glue ETL jobs running on the AWS Glue
job system. You can configure the Spark UI using the AWS Glue console or the AWS Command Line Interface
(AWS CLI).

Every 30 seconds, AWS Glue backs up the Spark event logs to the Amazon S3 path that you specify.

###### Topics

- [Configuring the Spark UI (console)](#monitor-spark-ui-jobs-console "#monitor-spark-ui-jobs-console")
- [Configuring the Spark UI (AWS CLI)](#monitor-spark-ui-jobs-cli "#monitor-spark-ui-jobs-cli")
- [Configuring the Spark UI for sessions using Notebooks](#monitor-spark-ui-sessions "#monitor-spark-ui-sessions")
- [Enable rolling logs](#monitor-spark-ui-rolling-logs "#monitor-spark-ui-rolling-logs")

## Configuring the Spark UI (console)

Follow these steps to configure the Spark UI by using the AWS Management Console. When creating an AWS Glue job, Spark UI is
enabled by default.

###### To turn on the Spark UI when you create or edit a job

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. In the navigation pane, choose **Jobs**.
3. Choose **Add job**, or select an existing one.
4. In **Job details**, open the **Advanced properties**.
5. Under the **Spark UI** tab, choose **Write Spark UI logs to
   Amazon S3**.
6. Specify an Amazon S3 path for storing the Spark event logs for the job. Note that if you use a security
   configuration in the job, the encryption also applies to the Spark UI log file. For more information, see
   [Encrypting data written by
   AWS Glue](encryption-security-configuration.md "encryption-security-configuration.md").
7. Under **Spark UI logging and monitoring configuration**:
   - Select **Standard** if you are generating logs to view in the AWS Glue console.
   - Select **Legacy** if you are generating logs to view on a Spark history server.
   - You can also choose to generate both.

## Configuring the Spark UI (AWS CLI)

To generate logs for viewing with Spark UI, in the AWS Glue console, use the AWS CLI to pass the following job
parameters to AWS Glue jobs. For more information, see [Using job parameters in AWS Glue jobs](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md").

```
'--enable-spark-ui': 'true',
'--spark-event-logs-path': 's3://s3-event-log-path'

```

To distribute logs to their legacy locations, set the `--enable-spark-ui-legacy-path` parameter to `"true"`. If you do
not want to generate logs in both formats, remove the `--enable-spark-ui` parameter.

## Configuring the Spark UI for sessions using Notebooks

###### Warning

AWS Glue interactive sessions do not currently support Spark UI in the console. Configure a Spark history
server.

If you use AWS Glue notebooks, set up SparkUI config before starting the session. To do this, use the
`%%configure` cell magic:

```
%%configure { “--enable-spark-ui”: “true”, “--spark-event-logs-path”: “s3://path” }
```

## Enable rolling logs

Enabling SparkUI and rolling log event files for AWS Glue jobs provides several benefits:

- Rolling Log Event Files – With rolling log event files enabled, AWS Glue generates separate log files for each step
  of the job execution, making it easier to identify and troubleshoot issues specific to a particular stage or transformation.
- Better Log Management – Rolling log event files help in managing log files more efficiently. Instead of
  having a single, potentially large log file, the logs are split into smaller, more manageable files based on the job
  execution stages. This can simplify log archiving, analysis, and troubleshooting.
- Improved Fault Tolerance – If a AWS Glue job fails or is interrupted, the rolling log event files can provide
  valuable information about the last successful stage, making it easier to resume the job from that point rather
  than starting from scratch.
- Cost Optimization – By enabling rolling log event files, you can save on storage costs associated with
  log files. Instead of storing a single, potentially large log file, you store smaller, more manageable log files,
  which can be more cost-effective, especially for long-running or complex jobs.

In a new environment, users can explicitly enable rolling logs through:

```
'—conf': 'spark.eventLog.rolling.enabled=true'
```

or

```
'—conf': 'spark.eventLog.rolling.enabled=true —conf
spark.eventLog.rolling.maxFileSize=128m'
```

When rolling logs are activated, `spark.eventLog.rolling.maxFileSize` specifies the maximum size of the event log
file before it rolls over. The default value of this optional parameter if not specified is 128 MB. Minimum is 10 MB.

The maximum sum of all generated rolled log event files is 2 GB. For AWS Glue jobs without rolling log support,
the maximum log event file size supported for SparkUI is 0.5 GB.

You can turn off rolling logs for a streaming job by passing an additional configuration. Note that very
large log files may be costly to maintain.

To turn off rolling logs, provide the following configuration:

```
'--spark-ui-event-logs-path': 'true',
'--conf': 'spark.eventLog.rolling.enabled=false'
```
