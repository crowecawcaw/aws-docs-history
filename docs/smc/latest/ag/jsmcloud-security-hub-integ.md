# Configuring AWS Security Hub CSPM integration

This section describes how to configure your AWS services in Jira Service Management Cloud.

###### To configure AWS Security Hub CSPM integration features

1. Enable AWS Security Hub CSPM. For more information, refer to [Setting up AWS Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md") with the Console.
2. Set up an SQS queue to receive updated Findings. Name the queue,
   `AwsSmcJsmCloudForgeSecurityHubQueue`, to align with
   the default name in the Jira Service Management Connector Settings for the AWS Security Hub CSPM
   integration. For more information, refer to [Getting started with Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md").
3. Set up an Amazon EventBridge rule to detect changes to Findings and push these to the
   queue. For more information, refer to [Getting started with Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md").

The CloudWatch rule should have this event pattern and point to the SQS queue created in
Step 2.

```


                    "EventPattern": {"source": [

                        "aws.securityhub"

                        ]
                    }

```

4. You can also customize this CloudWatch Events rule to only pull in Security Hub CSPM
   Findings that have specific Finding types, severity labels, workflow statuses,
   or compliance statuses. For details about how to filter the event pattern, refer to
   [Configuring an EventBridge rule for automatically sent findings](../../../securityhub/latest/userguide/securityhub-cwe-all-findings.md "../../../securityhub/latest/userguide/securityhub-cwe-all-findings.md") in
   the _AWS Security Hub CSPM User Guide_.

###### Note

You can use the AWS CloudFormation templates for the Connector for Jira Service Management to
automate the AWS Config custom resource and AWS Security Hub CSPM integration features. For more information, refer to
[Setting baseline
permissions for AWS Service Management Connector for ServiceNow](sn-base-perms.md "sn-base-perms.md").
