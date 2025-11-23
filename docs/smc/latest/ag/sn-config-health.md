# Configuring AWS

This section describes how to configure AWS Health integration in
ServiceNow.

###### Configure AWS for health-integration features

1. Set up an Amazon SQS queue to sync AWS Health events. Name the queue, **AwsServiceManagementConnectorForHealthDashboardQueue**, to align
   with the default name in the ServiceNow System Properties for the AWS Health
   integration. For more information, refer to [Getting started with Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md").
2. Set up an Amazon EventBridge rule to detect **Health Event** changes and
   push them to the queue. For more information, refer to [Getting started with Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md"). The rule should have the following
   event pattern and point to the Amazon SQS queue from step 1:

```
"EventPattern":
{
    "source":
    [
        "aws.health"
    ]
}
```

###### Note

The SQS queue synchronizes every five minutes. To change this threshold, navigate
to **Scheduled Jobs**, and modify the **Repeat Interval** value of the **Synchronize AWS Health** job.

###### Note

You can use baseline CloudFormation tempates to automate AWS Health integration features.
For more information, refer to [Setting baseline
permissions for AWS Service Management Connector for ServiceNow](sn-base-perms.md "sn-base-perms.md").
