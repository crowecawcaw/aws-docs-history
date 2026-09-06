

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Logging session activity
<a name="session-manager-auditing"></a>

In addition to providing information about current and completed sessions in the Systems Manager console, Session Manager provides you with the ability to log session activity in your AWS account using AWS CloudTrail.

CloudTrail captures session API calls through the Systems Manager console, the AWS Command Line Interface (AWS CLI), and the Systems Manager SDK. You can view the information on the CloudTrail console or store it in a specified Amazon Simple Storage Service (Amazon S3) bucket. One Amazon S3 bucket is used for all CloudTrail logs for your account. For more information, see [Logging AWS Systems Manager API calls with AWS CloudTrail](monitoring-cloudtrail-logs.md).

**Note**  
For recurring, historical, analytical analysis of your log files, consider querying CloudTrail logs using [CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) or a table you maintain. For more information, see [Querying AWS CloudTrail logs](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html) in the *AWS CloudTrail User Guide*. 

## Monitoring session activity using Amazon EventBridge (console)
<a name="session-manager-auditing-eventbridge-events"></a>

With EventBridge, you can set up rules to detect when changes happen to AWS resources. You can create a rule to detect when a user in your organization starts or ends a session, and then, for example, receive a notification through Amazon SNS about the event. 

EventBridge support for Session Manager relies on records of API operations that were recorded by CloudTrail. (You can use CloudTrail integration with EventBridge to respond to most AWS Systems Manager events.) Actions that take place within a session, such as an `exit` command, that don't make an API call aren't detected by EventBridge.

The following steps outline how to initiate notifications through Amazon Simple Notification Service (Amazon SNS) when a Session Manager API event occurs, such as **StartSession**.

**To monitor session activity using Amazon EventBridge (console)**

1. Create an Amazon SNS topic to use for sending notifications when the Session Manager event occurs that you want to track.

   For more information, see [Create a Topic](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) in the *Amazon Simple Notification Service Developer Guide*.

1. Create an EventBridge rule to invoke the Amazon SNS target for the type of Session Manager event you want to track.

   For information about how to create the rule, see [Creating Amazon EventBridge rules that react to events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) in the *Amazon EventBridge User Guide*.

   As you follow the steps to create the rule, make the following selections:
   + For **AWS service**, choose **Systems Manager**.
   + For **Event type**, choose **AWS API Call through CloudTrail**.
   + Choose **Specific operation(s)**, and then enter the Session Manager command or commands (one at a time) you want to receive notifications for. You can choose **StartSession**, **ResumeSession**, and **TerminateSession**. (EventBridge doesn't support `Get*`,` List*`, and `Describe*` commands.)
   + For **Select a target**, choose **SNS topic**. For **Topic**, choose the name of the Amazon SNS topic you created in Step 1.

For more information, see the *[Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/)* and the *[Amazon Simple Notification Service Getting Started Guide](https://docs.aws.amazon.com/sns/latest/gsg/)*.