# Logging and monitoring in CodeDeploy

This section provides an overview of monitoring, logging, and incident response in
CodeDeploy.

## Auditing of all interactions with

CodeDeploy

CodeDeploy is integrated with AWS CloudTrail, a service that captures API calls made by or on
behalf of CodeDeploy in your AWS account and delivers the log files to an S3 bucket you
specify. CloudTrail captures API calls from the CodeDeploy console, from CodeDeploy commands through the
AWS CLI, or from the CodeDeploy APIs directly. Using the information collected by CloudTrail, you can
determine which request was made to CodeDeploy, the source IP address from which the request
was made, who made the request, when it was made, and so on. To learn more about CloudTrail,
see [Working with CloudTrail
log files](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md") in the _AWS CloudTrail User Guide_.

You can view the log data created by a CodeDeploy deployment by setting up the Amazon CloudWatch
agent to view aggregated data in the CloudWatch console or by signing in to an instance to
review the log file. For more information, see [Send CodeDeploy agent logs to
CloudWatch](codedeploy-agent-operations-cloudwatch-agent.md "codedeploy-agent-operations-cloudwatch-agent.md").

## Alerting and incident management

You can use Amazon CloudWatch Events to detect and react to changes in the state of an instance or a
deployment (an _event_) in your CodeDeploy operations. Then,
based on rules you create, CloudWatch Events invokes one or more target actions when a deployment or
instance enters the state you specify in a rule. Depending on the type of state change,
you might want to send notifications, capture state information, take corrective action,
initiate events, or take other actions. You can select the following types of targets
when you use CloudWatch Events as part of your CodeDeploy operations:

- AWS Lambda functions
- Kinesis streams
- Amazon SQS SQS queues
- Built-in targets (CloudWatch alarm actions)
- Amazon SNS topics

The following are some use cases:

- Use a Lambda function to pass a notification to a Slack channel whenever
  deployments fail.
- Push data about deployments or instances to a Kinesis stream to support
  comprehensive, real-time status monitoring.
- Use CloudWatch alarm actions to automatically stop, terminate, reboot, or recover
  EC2 instances when a deployment or instance event you specify occurs.

For more information, see [What is
Amazon CloudWatch Events](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchEvents.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchEvents.md") in the _Amazon CloudWatch User Guide_.
