# Enabling continuous logging for AWS Glue 4.0 and earlier jobs

###### Note

In AWS Glue 4.0 and earlier versions, continuous logging was an available feature. However, with the introduction of AWS Glue 5.0, all jobs have real-time
logging capability. For more details on the logging capabilities and configuration options in AWS Glue 5.0, see
[Logging for AWS Glue jobs](monitor-continuous-logging.md "monitor-continuous-logging.md").

You can enable continuous logging using the AWS Glue console or through the AWS Command Line Interface (AWS CLI).

You can enable continuous logging when you create a new job, edit an existing job, or enable it through the AWS CLI.

You can also specify custom configuration options such as the Amazon CloudWatch log
group name, CloudWatch log stream prefix before the AWS Glue job run ID driver/executor ID, and log
conversion pattern for log messages. These configurations help you to set aggregate logs in
custom CloudWatch log groups with different expiration policies, and analyze them further with custom
log stream prefixes and conversions patterns.

###### Topics

- [Using the AWS Management Console](#monitor-continuous-logging-enable-console "#monitor-continuous-logging-enable-console")
- [Logging application-specific messages
  using the custom script logger](#monitor-continuous-logging-script "#monitor-continuous-logging-script")
- [Enabling the progress bar to show job
  progress](#monitor-continuous-logging-progress "#monitor-continuous-logging-progress")
- [Security configuration with continuous logging](#monitor-logging-encrypt-log-data "#monitor-logging-encrypt-log-data")

## Using the AWS Management Console

Follow these steps to use the console to enable continuous logging when creating or
editing an AWS Glue job.

###### To create a new AWS Glue job with continuous logging

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. In the navigation pane, choose **ETL jobs**.
3. Choose **Visual ETL**.
4. In the **Job details** tab, expand the **Advanced properties** section.
5. Under **Continuous logging** select **Enable logs in CloudWatch**.

###### To enable continuous logging for an existing AWS Glue job

1. Open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. In the navigation pane, choose **Jobs**.
3. Choose an existing job from the **Jobs** list.
4. Choose **Action**, **Edit job**.
5. In the **Job details** tab, expand the **Advanced properties** section.
6. Under **Continuous logging** select **Enable logs in CloudWatch**.

### Using the AWS CLI

To enable continuous logging, you pass in job parameters to an AWS Glue job. Pass the following special job parameters similar to other AWS Glue job
parameters. For more information, see [Using job parameters in AWS Glue jobs](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md").

```
'--enable-continuous-cloudwatch-log': 'true'
```

You can specify a custom Amazon CloudWatch log group name. If not specified, the default log group name is `/aws-glue/jobs/logs-v2`.

```
'--continuous-log-logGroup': '`custom_log_group_name`'
```

You can specify a custom Amazon CloudWatch log stream prefix. If not specified, the default log stream prefix is the job run ID.

```
'--continuous-log-logStreamPrefix': '`custom_log_stream_prefix`'
```

You can specify a custom continuous logging conversion pattern. If not specified, the
default conversion pattern is `%d{yy/MM/dd HH:mm:ss} %p %c{1}: %m%n`. Note that the
conversion pattern only applies to driver logs and executor logs. It does not affect the AWS Glue
progress bar.

```
'--continuous-log-conversionPattern': '`custom_log_conversion_pattern`'
```

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

## Security configuration with continuous logging

If a security configuration is enabled for CloudWatch logs, AWS Glue will create a log group named as follows for continuous logs:

```
<Log-Group-Name>-<Security-Configuration-Name>
```

The default and custom log groups will be as follows:

- The default continuous log group will be `/aws-glue/jobs/error-<`Security-Configuration-Name>``
- The custom continuous log group will be `<`custom-log-group-name>`-<`Security-Configuration-Name>``

You need to add the `logs:AssociateKmsKey` to your IAM role permissions, if you
enable a security configuration with CloudWatch Logs. If that permission is not included, continuous
logging will be disabled. Also, to configure the encryption for the CloudWatch Logs, follow the
instructions at [Encrypt Log Data in
CloudWatch Logs Using AWS Key Management Service](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md") in the
_Amazon CloudWatch Logs User Guide_.

For more information on creating security configurations, see [Managing security configurations on
the AWS Glue console](console-security-configurations.md "console-security-configurations.md").

###### Note

You may incur additional charges when you enable logging and additional CloudWatch log events are created.
For more information, see
[Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/") .
