# Monitoring Amazon MWAA Serverless

Monitoring helps maintain the reliability, availability, and performance of Amazon MWAA Serverless and your other AWS solutions. Amazon MWAA Serverless uses CloudTrail and CloudWatch to capture different logs and metrics.
You can provide an option loggorup while creating Amazon MWAA Serverless workflows. If you do not provide a loggoroup name, Amazon MWAA Serverless will create a new loggroup where all the logs for the workflows are published.

You can leverage a mix of AWS services such as AWS Lambda and EventBridge to build a custom CloudWatch dashboard to monitor the health of your workflows:

- _Amazon CloudWatch_ monitors your AWS resources and and the applications you run on AWS in real time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2 instances and automatically launch new instances when needed. For more information, refer to the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Logs_ enables you to monitor, store, and access your log files from Amazon EC2 instances, CloudTrail, and other sources. CloudWatch Logs can monitor information in the log files and notify you when certain thresholds are met. You can also archive your log data in highly durable storage. For more information, refer to the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _Amazon EventBridge_ can be used to automate your AWS services and respond automatically to system events, such as application availability issues or resource changes. Events from AWS services are delivered to EventBridge in near real time. You can write simple rules to indicate which events are of interest to you and which automated actions to take when an event matches a rule. For more information, refer to [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, refer to the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _AWS Lambda_ enables you to run code without provisioning or managing servers. You pay only for the compute time that you consume—there's no charge when your code isn't running. You can run code for virtually any type of application or backend service—all with zero administration. Just upload your code and Lambda takes care of everything required to run and scale your code with high availability.

###### Topics

- [Observability with CloudWatch](observe-with-cloudwatch.md "observe-with-cloudwatch.md")
- [Logging Amazon MWAA Serverless APIs with CloudTrail](log-apis-with-cloudtrail.md "log-apis-with-cloudtrail.md")
