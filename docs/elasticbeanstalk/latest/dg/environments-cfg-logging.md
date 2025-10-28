# Viewing your Elastic Beanstalk environment logs

AWS Elastic Beanstalk provides two ways to regularly view logs from the Amazon EC2 instances that run your application:

- Configure your Elastic Beanstalk environment to upload rotated instance logs to the environment's Amazon S3 bucket.
- Configure the environment to stream instance logs to Amazon CloudWatch Logs.
  When you configure instance log streaming to CloudWatch Logs, Elastic Beanstalk creates CloudWatch Logs log groups for proxy and deployment logs on the Amazon EC2 instances, and transfers
  these log files to CloudWatch Logs in real time. For more information about instance logs, see [Viewing logs from Amazon EC2 instances in your Elastic Beanstalk environment](using-features.md "using-features.md").

In addition to instance logs, if you enable [enhanced health](health-enhanced.md "health-enhanced.md") for your environment, you can configure the
environment to stream health information to CloudWatch Logs. When the environment's health status changes, Elastic Beanstalk adds a record to a health log group, with the new
status and a description of the cause of the change. For information about environment health streaming, see [Streaming Elastic Beanstalk environment health information to Amazon CloudWatch Logs](AWSHowTo.cloudwatchlogs.md "AWSHowTo.cloudwatchlogs.md").

## Configuring instance log viewing

To view instance logs, you can enable instance log rotation and log streaming in the Elastic Beanstalk console.

###### To configure instance log rotation and log streaming in the Elastic Beanstalk console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.
5. In the **S3 log storage** section, select **Activated** beneath **Rotate logs** to enable uploading
   rotated logs to Amazon S3.
6. in the **Instance log streaming to CloudWatch Logs** section, configure the following settings:
   - **Log streaming** – Select **Activated** to enable log streaming.
   - **Retention** – Specify the number of days to retain logs in CloudWatch Logs.
   - **Lifecycle** – Set to **Delete logs upon termination** to delete logs from CloudWatch Logs immediately if the
     environment is terminated, instead of waiting for them to expire.

7. To save the changes choose **Apply** at the bottom of the page.

After you enable log streaming, you can return to the **Software** configuration category or page and find the **Log
Groups** link. Click this link to see your instance logs in the CloudWatch console.

## Configuring environment health log viewing

To view environment health logs, you can enable environment health log streaming in the Elastic Beanstalk console.

###### To configure environment health log streaming in the Elastic Beanstalk console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.
5. Go to the **Monitoring** section.
6. Under **Health event streaming to CloudWatch Logs**, configure the following settings:
   - **Log streaming** – Choose to **Activated** to enable log streaming.
   - **Retention** – Specify the number of days to retain logs in CloudWatch Logs.
   - **Lifecycle** – Set to **Delete logs upon termination** to delete logs from CloudWatch Logs immediately if the
     environment is terminated, instead of waiting for them to expire.

7. To save the changes choose **Apply** at the bottom of the page.

## Log viewing namespaces

The following namespaces contain settings for log viewing:

- [aws:elasticbeanstalk:hostmanager](command-options-general.md#command-options-general-elasticbeanstalkhostmanager "command-options-general.md#command-options-general-elasticbeanstalkhostmanager")
  – Configure uploading rotated logs to Amazon S3.
- [aws:elasticbeanstalk:cloudwatch:logs](command-options-general.md#command-options-general-cloudwatchlogs "command-options-general.md#command-options-general-cloudwatchlogs") – Configure instance log
  streaming to CloudWatch.
- [aws:elasticbeanstalk:cloudwatch:logs:health](command-options-general.md#command-options-general-cloudwatchlogs-health "command-options-general.md#command-options-general-cloudwatchlogs-health") – Configure
  environment health streaming to CloudWatch.
