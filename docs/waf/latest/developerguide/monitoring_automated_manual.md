**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Monitoring tools

AWS provides various tools that you can use to monitor AWS WAF and AWS Shield Advanced. You
can configure some of these tools to do the monitoring for you, while other tools
require manual intervention. We recommend that you automate monitoring tasks as much as
possible.

## Automated monitoring tools

You can use the following automated monitoring tools to watch AWS WAF and
AWS Shield Advanced and report when something is wrong:

- **protection pack (web ACL) traffic overview dashboards** – Access
  summaries of the web traffic that a protection pack (web ACL) evaluates by going to the web
  ACL's page in the AWS WAF console and opening the **Traffic
  overview** tab.

The traffic overview dashboards provide near real-time summaries of the
Amazon CloudWatch metrics that AWS WAF collects when it evaluates your application web
traffic. You can see summaries for all of your web traffic and for traffic
evaluated by the intelligent threat mitigation rule groups.

For more information, see [Traffic overview dashboards for protection packs (web ACLs)](web-acl-dashboards.md "web-acl-dashboards.md") or go to the dashboards in the
console.

- **Amazon CloudWatch Alarms** – Watch a single metric over a time period you specify, and perform one or more actions based on the value of the metric relative to a given threshold over a number of time periods. The action is a notification sent to an Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto Scaling policy. Alarms invoke actions for sustained state changes only. CloudWatch alarms will not invoke actions simply because they are in a particular state; the state must have changed and been maintained for a specified number of periods. For more information, see [Monitoring CloudFront
  Activity Using CloudWatch](../../../AmazonCloudFront/latest/DeveloperGuide/monitoring-using-cloudwatch.md "../../../AmazonCloudFront/latest/DeveloperGuide/monitoring-using-cloudwatch.md").

###### Note

CloudWatch metrics and alarms are not enabled for AWS Firewall Manager.

Not only can you use CloudWatch to monitor AWS WAF and Shield Advanced metrics as
described in [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md"), you also should use CloudWatch to
monitor activity for your protected resources. For more information, see the
following:

    + [Monitoring CloudFront Activity Using CloudWatch](../../../AmazonCloudFront/latest/DeveloperGuide/monitoring-using-cloudwatch.md "../../../AmazonCloudFront/latest/DeveloperGuide/monitoring-using-cloudwatch.md") in the
     *Amazon CloudFront Developer Guide*
    + [Logging and monitoring in Amazon API Gateway](../../../apigateway/latest/developerguide/security-monitoring.md "../../../apigateway/latest/developerguide/security-monitoring.md") in the
     *API Gateway Developer Guide*
    + [CloudWatch Metrics for Your Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.md "../../../elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.md") in the
     *Elastic Load Balancing User Guide*
    + [Monitoring and
     Logging](../../../appsync/latest/devguide/monitoring.md "../../../appsync/latest/devguide/monitoring.md") in the
     *AWS AppSync Developer Guide*
    + [Logging and monitoring in Amazon Cognito](../../../cognito/latest/developerguide/monitoring.md "../../../cognito/latest/developerguide/monitoring.md") in the *Amazon Cognito Developer Guide*
    + [Viewing App Runner logs streamed to CloudWatch Logs](../../../apprunner/latest/dg/monitor-cwl.md "../../../apprunner/latest/dg/monitor-cwl.md") and [Viewing App Runner service metrics reported to CloudWatch](../../../apprunner/latest/dg/monitor-cw.md "../../../apprunner/latest/dg/monitor-cw.md") in the
     *AWS App Runner Developer Guide*

- **Amazon CloudWatch Logs** – Monitor, store, and access your log files from AWS CloudTrail or other sources. For more information, see [What is Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").
- **Amazon CloudWatch Events** – Automate your AWS services and
  respond automatically to system events. Events from AWS services are
  delivered to CloudWatch Events in near real time, and you can specify automated actions
  to take when an event matches a rule that you write. For more information,
  see [What is Amazon CloudWatch Events?](../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md "../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md")
- **AWS CloudTrail Log Monitoring** – Share log files
  between accounts, monitor CloudTrail log files in real time by sending them to
  CloudWatch Logs, write log-processing applications in Java, and validate that your log
  files have not changed after delivery by CloudTrail. For more information, see
  [Logging API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md") and [Working with
  CloudTrail Log Files](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md") in the _AWS CloudTrail User Guide_.
- **AWS Config** – View the configuration of AWS resources in your AWS
  account, including how the resources are related to one another and how they
  were configured in the past so that you can see how the configurations and
  relationships change over time.

## Manual monitoring tools

Another important part of monitoring AWS WAF and AWS Shield Advanced involves manually
monitoring those items that the CloudWatch alarms don't cover. You can view the AWS WAF,
Shield Advanced, CloudWatch, and other AWS Management Console dashboards to see the state of your AWS
environment. We recommend that you also check the log files for your
web ACLs and rules.

- For example, to view the AWS WAF dashboard:
  - On the **Requests** tab of the AWS WAF **Web
    ACLs** page, view a graph of total requests and
    requests that match each rule that you have created. For more
    information, see [Viewing a sample of web requests](web-acl-testing-view-sample.md "web-acl-testing-view-sample.md").

- View the CloudWatch home page for the following:

      + Current alarms and status
      + Graphs of alarms and resources
      + Service health status

  In addition, you can use CloudWatch to do the following:

      + Create [customized dashboards](../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.md") to monitor the services that you
       care about.
      + Graph metric data to troubleshoot issues and discover
       trends.
      + Search and browse all of your AWS resource metrics.
      + Create and edit alarms to be notified of problems.
