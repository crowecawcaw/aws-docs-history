# Configuring AWS Security Hub in ServiceNow

This section describes how to configure your AWS services in ServiceNow.

###### To configure AWS Security Hub integration features

1. Enable AWS Security Hub. For more information, see [Setting up AWS Security Hub](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md") with the Console.
2. Set up an SQS queue to receive updated Findings. Name the queue,
   `AwsServiceManagementConnectorForSecurityHubQueue`, to align with
   the default name in the ServiceNow System Properties for the AWS Security Hub
   integration. For more information, see [Getting started with Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md").
3. Set up an Amazon EventBridge rule to detect changes to Findings and push these to the
   queue. For more information, see [Getting started with Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md").

The rule should have this event pattern and point to the SQS queue created in
Step 2.

```
"EventPattern": {

       "source": [

        "aws.securityhub"

        ]
}
```

4. You can also customize this CloudWatch Events rule to only pull in Security Hub
   findings that have specific finding types, severity labels, workflow statuses,
   or compliance statuses. For details about how to filter the event pattern, see
   [Configuring an EventBridge rule for automatically sent findings](../../../securityhub/latest/userguide/securityhub-cwe-all-findings.md "../../../securityhub/latest/userguide/securityhub-cwe-all-findings.md") in
   the _AWS Security Hub User Guide_.

###### Note

You can use the AWS CloudFormation templates for the Connector for ServiceNow to automate
the AWS Config custom resource and AWS Security Hub integration features. For more information, see [Baseline Permissions](sn-base-perms.md "sn-base-perms.md").
