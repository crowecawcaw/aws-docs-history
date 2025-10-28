# Logging for AWS Glue jobs

In AWS Glue 5.0, all jobs have real-time logging capabilities. Additionally, you can specify custom configuration options to tailor the logging behavior.
These options include setting the Amazon CloudWatch log group name, the Amazon CloudWatch log stream prefix (which will precede the
AWS Glue job run ID and driver/executor ID), and the log conversion pattern for log messages. These configurations allow you to aggregate logs in custom
Amazon CloudWatch log groups with different expiration policies. Furthermore, you can analyze the logs more effectively by using custom log stream
prefixes and conversion patterns. This level of customization enables you to optimize log management and analysis according to your specific requirements.

## Logging behavior in AWS Glue 5.0

By default, system logs, Spark daemon logs, and user AWS Glue Logger logs are written to the `/aws-glue/jobs/error` log group in
Amazon CloudWatch. On the other hand, user stdout (standard output) and stderr (standard error) logs are written to the
`/aws-glue/jobs/output` log group by default.

## Custom logging

You can customize the default log group and log stream prefixes using the following job arguments:

- `--custom-logGroup-prefix`: Allows you to specify a custom prefix for the `/aws-glue/jobs/error` and
  `/aws-glue/jobs/output` log groups. If you provide a custom prefix, the log group names will be in the following format:
  - `/aws-glue/jobs/error` will be ``<customer prefix>`/error`
  - `/aws-glue/jobs/output` will be ``<customer prefix>`/output`

- `--custom-logStream-prefix`: Allows you to specify a custom prefix for the log stream names within the log groups.
  If you provide a custom prefix, the log stream names will be in the following format:
  - `jobrunid-driver` will be ``<customer log stream>`-driver`
  - `jobrunid-executorNum` will be ``<customer log stream>`-executorNum`

Validation rules and limitations for custom prefixes:

- The entire log stream name must be between 1 and 512 characters long.
- The custom prefix itself is restricted to 400 characters.
- The custom prefix must match the regular expression pattern `[^:\*]\*` (special characters allowed are '\_', '-', and '/').

## Logging application-specific messages

using the custom script logger

You can use the AWS Glue logger to log any application-specific messages in the script that
are sent in real time to the driver log stream.

The following example shows a Python script.

```
from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)
logger = glueContext.get_logger()
logger.info("info message")
logger.warn("warn message")
logger.error("error message")

```

The following example shows a Scala script.

```
import com.amazonaws.services.glue.log.GlueLogger

object GlueApp {
  def main(sysArgs: Array[String]) {
    val logger = new GlueLogger
    logger.info("info message")
    logger.warn("warn message")
    logger.error("error message")
  }
}

```

## Enabling the progress bar to show job

progress

AWS Glue provides a real-time progress bar under the `JOB_RUN_ID-progress-bar` log
stream to check AWS Glue job run status. Currently it supports only jobs that initialize
`glueContext`. If you run a pure Spark job without initializing
`glueContext`, the AWS Glue progress bar does not appear.

The progress bar shows the following progress update every 5 seconds.

```
Stage Number (Stage Name): > (numCompletedTasks + numActiveTasks) / totalNumOfTasksInThisStage]
```

## Security configuration with Amazon CloudWatch logging

When a security configuration is enabled for Amazon CloudWatch logs, AWS Glue creates log groups with specific naming patterns that incorporate the security configuration name.

### Log group naming with security configuration

The default and custom log groups will be as follows:

- **Default error log group:** `/aws-glue/jobs/`Security-Configuration-Name`-role/`glue-job-role`/error`
- **Default output log group:** `/aws-glue/jobs/`Security-Configuration-Name`-role/`glue-job-role`/output`
- **Custom error log group (AWS Glue 5.0):** ``custom-log-group-prefix`/`Security-Configuration-Name`-role/`glue-job-role`/error`
- **Custom output log group (AWS Glue 5.0):** ``custom-log-group-prefix`/`Security-Configuration-Name`-role/`glue-job-role`/output`

### Required IAM Permissions

You need to add the `logs:AssociateKmsKey` permission to your IAM role permissions, if you enable a security configuration with
Amazon CloudWatch Logs. If that permission is not included, continuous logging will be disabled.

Also, to configure the encryption for the Amazon CloudWatch Logs, follow the instructions at
[Encrypt Log Data in Amazon CloudWatch Logs Using AWS Key Management Service](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md") in the Amazon Amazon CloudWatch Logs User Guide.

### Additional Information

For more information on creating security configurations, see [Managing security configurations on the AWS Glue console](console-security-configurations.md "console-security-configurations.md").

###### Topics

- [Enabling continuous logging for AWS Glue 4.0 and earlier jobs](monitor-continuous-logging-enable.md "monitor-continuous-logging-enable.md")
- [Viewing logs for AWS Glue jobs](monitor-continuous-logging-view.md "monitor-continuous-logging-view.md")
