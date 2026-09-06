

# Viewing your Elastic Beanstalk environment logs
<a name="environments-cfg-logging"></a>

AWS Elastic Beanstalk provides two ways to regularly view logs from the Amazon EC2 instances that run your application:
+ Configure your Elastic Beanstalk environment to upload rotated instance logs to the environment's Amazon S3 bucket.
+ Configure the environment to stream instance logs to Amazon CloudWatch Logs.

When you configure instance log streaming to CloudWatch Logs, Elastic Beanstalk creates CloudWatch Logs log groups for proxy and deployment logs on the Amazon EC2 instances, and transfers these log files to CloudWatch Logs in real time. For more information about instance logs, see [Viewing logs from Amazon EC2 instances in your Elastic Beanstalk environment](using-features.logging.md).

In addition to instance logs, if you enable [enhanced health](health-enhanced.md) for your environment, you can configure the environment to stream health information to CloudWatch Logs. When the environment's health status changes, Elastic Beanstalk adds a record to a health log group, with the new status and a description of the cause of the change. For information about environment health streaming, see [Streaming Elastic Beanstalk environment health information to Amazon CloudWatch Logs](AWSHowTo.cloudwatchlogs.envhealth.md).

## Configuring instance log viewing
<a name="environments-cfg-logging-console"></a>

To view instance logs, you can enable instance log rotation and log streaming in the Elastic Beanstalk console.

**To configure instance log rotation and log streaming in the Elastic Beanstalk console**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. In the navigation pane, choose **Configuration**.

1. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.

1. In the **S3 log storage** section, select **Activated** beneath **Rotate logs** to enable uploading rotated logs to Amazon S3.

1. in the **Instance log streaming to CloudWatch Logs** section, configure the following settings:
   + **Log streaming** – Select **Activated** to enable log streaming.
   + **Retention** – Specify the number of days to retain logs in CloudWatch Logs.
   + **Lifecycle** – Set to **Delete logs upon termination** to delete logs from CloudWatch Logs immediately if the environment is terminated, instead of waiting for them to expire.

1. To save the changes choose **Apply** at the bottom of the page.

After you enable log streaming, Elastic Beanstalk displays the streamed CloudWatch Logs log groups in the environment management console, on the **Logs** page. Choose a log group to view its log events in a built-in viewer—Elastic Beanstalk automatically selects the most recently active log stream, and you can switch streams, search and filter events, and load earlier events.

## Configuring environment health log viewing
<a name="environments-cfg-logging-health-console"></a>

To view environment health logs, you can enable environment health log streaming in the Elastic Beanstalk console.

**To configure environment health log streaming in the Elastic Beanstalk console**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. In the navigation pane, choose **Configuration**.

1. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.

1. Go to the **Monitoring** section.

1. Under **Health event streaming to CloudWatch Logs**, configure the following settings:
   + **Log streaming** – Choose to **Activated** to enable log streaming.
   + **Retention** – Specify the number of days to retain logs in CloudWatch Logs.
   + **Lifecycle** – Set to **Delete logs upon termination** to delete logs from CloudWatch Logs immediately if the environment is terminated, instead of waiting for them to expire.

1. To save the changes choose **Apply** at the bottom of the page.

## Log viewing namespaces
<a name="environments-cfg-logging-namespaces"></a>

The following namespaces contain settings for log viewing:
+ [`aws:elasticbeanstalk:hostmanager`](command-options-general.md#command-options-general-elasticbeanstalkhostmanager) – Configure uploading rotated logs to Amazon S3.
+ [`aws:elasticbeanstalk:cloudwatch:logs`](command-options-general.md#command-options-general-cloudwatchlogs) – Configure instance log streaming to CloudWatch.
+ [`aws:elasticbeanstalk:cloudwatch:logs:health`](command-options-general.md#command-options-general-cloudwatchlogs-health) – Configure environment health streaming to CloudWatch.