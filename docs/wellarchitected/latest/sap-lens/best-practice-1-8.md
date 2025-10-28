# Best Practice 1.8 – Use automated

response and recovery techniques to react to monitoring alerts

Automate responses to events to reduce errors caused by manual processes, and to
ensure prompt and consistent responses.

**Suggestion 1.8.1 - Use automation services to automate your
responses to events**

There are multiple ways to automate the running of remediation activities for events
triggered from your monitoring tools. Generally, you should seek to funnel all of your SAP
application and database events into a single channel which can provide event-based
automation in response.

- To respond to an event from a state change in your AWS resources, or from your
  own custom events from SAP, you could create [EventBridge rules](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md") to
  invoke actions in Event [targets](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md") (for example,
  Lambda functions, Amazon Simple Notification Service (Amazon SNS) topics, Amazon ECS tasks,
  and AWS Systems Manager Automation). AWS Systems Manager automation can be used to
  call the `sapcontrol` command and perform SAP system tasks automatically.
- To respond to a metric that crosses a threshold for a resource (for example, wait
  time), you should create [CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") to perform one or more actions using [Amazon EC2 actions](../../../AWSEC2/latest/APIReference/OperationList-query-ec2.md "../../../AWSEC2/latest/APIReference/OperationList-query-ec2.md"), [Auto Scaling actions](../../../autoscaling/ec2/APIReference/API_Operations_List.md "../../../autoscaling/ec2/APIReference/API_Operations_List.md"), or to send a notification to an [Amazon SNS topic](http://aws.amazon.com/sns/ "http://aws.amazon.com/sns/").
- If you need to perform custom actions in response to an alarm, invoke Lambda
  through Amazon SNS notification or an AWS Systems Manager Automation (for example,
  using Action `aws:runCommand` ) see [AWS Blog: Automate Start or Stop of Distributed SAP HANA systems using AWS
  Systems Manager](https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/ "https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/").
- Use Amazon SNS to publish Event Notifications and escalation messages to keep people
  informed.
- AWS also supports third-party systems through the AWS service APIs and SDKs.
  There are a number of monitoring tools provided by AWS Partners and third parties that
  allow for monitoring, notifications, and responses. Some of these tools include Avantra,
  New Relic, Splunk, Loggly, SumoLogic, and Datadog.
- Consider pushing events and interactions into third-party ITIL tools where
  applicable for your organization - such as [AWS to ServiceNow](../../../servicecatalog/latest/adminguide/integrations-servicenow.md "../../../servicecatalog/latest/adminguide/integrations-servicenow.md") integration.
  You should keep critical manual procedures available for use when automated procedures
  fail.
