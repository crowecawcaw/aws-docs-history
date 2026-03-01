# Monitoring and tracking the use of Amazon Q Developer

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon Q Developer and your other AWS solutions. AWS provides the following
monitoring tools and features to monitor and record Amazon Q Developer activity:

- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon Simple Storage Service (Amazon S3) bucket that you
  specify. You can identify which users and accounts called AWS, the source IP address
  from which the calls were made, and when the calls occurred. For more information, see
  [Logging Amazon Q Developer API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
- _Amazon CloudWatch_ monitors your AWS resources and the applications you
  run on AWS in real time. You can collect and track metrics, create customized
  dashboards, and set alarms that notify you or take actions when a specified metric
  reaches a threshold that you specify. For example, you can have CloudWatch track the number of
  times that Amazon Q has been invoked on your account, or the number of daily active users.
  For more information, see [Monitoring Amazon Q Developer with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
  Amazon Q Developer also includes the following features to help you track and record user activity
  in Amazon Q:

- _A dashboard_ shows you aggregate user activity metrics of Amazon Q Developer Pro
  subscribers. For more information, see [Viewing Amazon Q Developer user activity on the dashboard](dashboard.md "dashboard.md").
- _User activity reports_ show you what individual users are up to in
  Amazon Q. For more information, see [Viewing the activity of specific users in Amazon Q Developer](q-admin-user-telemetry.md "q-admin-user-telemetry.md").
- _Prompt logs_ provide you with a record of all the prompts that users
  enter into the Amazon Q chat in their integrated development environment (IDE). For more
  information, see [Logging users' prompts in Amazon Q Developer](q-admin-prompt-logging.md "q-admin-prompt-logging.md").
