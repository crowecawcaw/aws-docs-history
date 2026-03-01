# (Recommended) Best practices to enhance investigations

As a best practice, we recommend that you enable several AWS services and features
in your account that can help CloudWatch investigations discover more information in your topology and make
better suggestions during investigations.

###### Topics

- [CloudWatch agent](#Investigations-CloudWatchAgent "#Investigations-CloudWatchAgent")
- [AWS CloudTrail](#Investigations-CloudTrail "#Investigations-CloudTrail")
- [CloudWatch Application Signals](#Investigations-ApplicationSignals "#Investigations-ApplicationSignals")
- [X-Ray](#Investigations-Xray "#Investigations-Xray")
- [Container insights](#Investigations-ContainerInsights "#Investigations-ContainerInsights")
- [Database insights](#Investigations-DatabaseInsights "#Investigations-DatabaseInsights")

## CloudWatch agent

We recommend that you install the latest version of the CloudWatch agent on your
servers. Using a recent version of the CloudWatch agent enhances the ability to find
issues in Amazon EC2 and Amazon EBS during investigations. At a minimum, you should use
Version 1.300049.1 or later of the CloudWatch agent. For more information about the CloudWatch
agent and how to install it, see [Collect metrics, logs, and traces using the CloudWatch agent](Install-CloudWatch-Agent.md "Install-CloudWatch-Agent.md").

## AWS CloudTrail

We recommend that you configure your CloudTrail trails to send management events to
CloudWatch Logs. CloudTrail records management events about control plane operations in your AWS
account, such as configuring permissions policies and creating, modifying, and
updating resources. When CloudTrail events are sent to CloudWatch Logs, CloudWatch investigations can analyze these
events in your AWS account to detect changes in your account related to your
investigation. For more information, see [What is
AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), [Creating a trail with the CloudTrail console](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md"), [Working with CloudTrail
trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") and [Sending events to CloudWatch Logs](../../../awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.md "../../../awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.md").

###### Note

CloudWatch investigations can only analyze CloudTrail events from trails that send events to CloudWatch Logs in the
same AWS Region where you conduct the investigation. For cross-account
investigations, it will review the CloudTrail trails in each configured account in the
same region where you conduct the investigation.

## CloudWatch Application Signals

CloudWatch Application Signals discovers the topology of your environment, including
your applications and their dependencies. It also automatically collects standard
metrics such as latency and availability. By enabling Application Signals, CloudWatch investigations can
use this topology and metric information during investigations.

For more information about application signals, see [Application Signals](CloudWatch-Application-Monitoring-Sections.md "CloudWatch-Application-Monitoring-Sections.md").

## X-Ray

We recommend that you enable AWS X-Ray. X-Ray collects traces about requests
that your applications serve. For any traced request to your application, you can
see detailed information not only about the request and response, but also about
calls that your application makes to downstream AWS resources, microservices,
databases, and web APIs. This information can help CloudWatch investigations during
investigations.

For more information, see [**What is
AWS X-Ray**](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md")

## Container insights

If you use Amazon ECS or Amazon EKS, we recommend that you install Container insights. This
improves the ability of CloudWatch investigations to find issues in your containers. For more information
about the CloudWatch agent and how to install it, see [Container Insights](ContainerInsights.md "ContainerInsights.md").

## Database insights

If you use Amazon RDS, we recommend that you enable the Advanced mode of Database Insights on
your database instances. Database Insights monitors database load and provides detailed
performance analysis that helps CloudWatch investigations identify database-related issues during
investigations. When Advanced Database Insights is enabled, CloudWatch investigations can automatically generate
performance analysis reports that include detailed observations, metric anomalies,
root cause analysis, and recommendations specific to your database workload. For
more information about Database Insights and how to enable Advanced mode, see [Monitoring Amazon RDS databases with CloudWatch Database
Insights](../../../AmazonRDS/latest/UserGuide/USER_DatabaseInsights.md "../../../AmazonRDS/latest/UserGuide/USER_DatabaseInsights.md").
