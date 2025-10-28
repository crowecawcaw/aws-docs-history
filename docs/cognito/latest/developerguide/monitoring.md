# Logging and monitoring in Amazon Cognito

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon Cognito and your other AWS solutions. Amazon Cognito currently supports the following
AWS services so that you can monitor your organization and the activity that happens within
it.

- **AWS CloudTrail –** With CloudTrail you can capture API calls
  from the Amazon Cognito console and from code calls to the Amazon Cognito API operations. For example, when a
  user authenticates, CloudTrail can record details such as the IP address in the request, who made
  the request, and when it was made.
- **Amazon CloudWatch Logs** – With CloudWatch Logs, you can send
  fine-grained logs of user activity to a log group. For example, you can review detailed user
  activity logs to troubleshoot the delivery of email and SMS messages to your users.
- **Amazon CloudWatch Metrics –** With CloudWatch metrics you can
  monitor, report, and take automatic actions in case of an event in near real time. For
  example, you can create CloudWatch dashboards on the provided metrics to monitor your Amazon Cognito user
  pools, or you can create CloudWatch alarms on the provided metrics to notify you on breach of a
  set threshold.
- **Amazon CloudWatch Logs Insights** – With CloudWatch Logs Insights, you
  can configure CloudTrail to send events to CloudWatch for monitoring Amazon Cognito CloudTrail log files.

###### Topics

- [Monitoring and managing costs](tracking-cost.md "tracking-cost.md")
- [Exporting logs from Amazon Cognito user pools](exporting-quotas-and-usage.md "exporting-quotas-and-usage.md")
- [Tracking quotas
  and usage in CloudWatch and Service Quotas](tracking-quotas-and-usage-in-cloud-watch-and-service-quotas.md "tracking-quotas-and-usage-in-cloud-watch-and-service-quotas.md")
- [Amazon Cognito logging in AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
