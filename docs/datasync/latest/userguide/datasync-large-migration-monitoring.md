# Monitoring your transfers

AWS DataSync provides several monitoring options to help you validate and debug your
transfer.

## Monitoring

your transfers with CloudWatch metrics

You can create custom CloudWatch dashboards with metrics from your DataSync task
executions. For more information, see [Monitoring data transfers with Amazon CloudWatch metrics](monitor-datasync.md "monitor-datasync.md").

## Monitoring your

transfers with task reports

If you’re transferring millions of files or objects, considering using task
reports. Task reports provide detailed information about what DataSync attempts to
transfer, skip, verify, and delete during a task execution. For more
information, see [Monitoring your data transfers with task reports](task-reports.md "task-reports.md").

You can also visualize your task reports by using AWS services such as
AWS Glue, Amazon Athena, and Amazon Quick Suite. For more information, see the [AWS Storage
Blog](https://aws.amazon.com/blogs/storage/derive-insights-from-aws-datasync-task-reports-using-aws-glue-amazon-athena-and-amazon-quicksight/ "https://aws.amazon.com/blogs/storage/derive-insights-from-aws-datasync-task-reports-using-aws-glue-amazon-athena-and-amazon-quicksight/").

## Monitoring your

transfers with CloudWatch Logs

At minimum, we recommend that you configure your task to log basic information
and transfer errors. For more information, see
[Monitoring data transfers with Amazon CloudWatch Logs](configure-logging.md "configure-logging.md").
