# Configuring Support integration in ServiceNow

This section describes how to configure Support integration in ServiceNow.

###### To configure AWS Support integration features

1. Set up an SQS queue (in N.Virginia (us-east-1) for Commercial regions and US West
   (us-gov-west-1) for GovCloud regions) to sync AWS Support cases. Name the queue,
   **AwsServiceManagementConnectorForSupportQueue**, to align with the
   default name in the ServiceNow System Properties for the AWS Support
   integration. For more information, see [Getting started with Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md").
2. Set up an Amazon EventBridge rule to detect changes to AWS Support Cases and push these to the
   queue. For more information, see [Getting started with Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md").
   The rule should have this event pattern and point to the SQS queue created in Step 1.

```

            "EventPattern": {
{
    "detail-type": ["Support Case Update"],
    "source": ["aws.support"]
}
}

```

###### Note

You can use baseline AWS CloudFormation tempates for the Connector for ServiceNow to automate the Support
integration features. For more information, see [Baseline Permissions](../../../en_us/smc/latest/ag/sn-base-perms.md "../../../en_us/smc/latest/ag/sn-base-perms.md").

To create the required SQS queue and EventBridge rule, use Connector for ServiceNow - [AWS Support Commercial Regions](https://servicecatalogconnector.s3.amazonaws.com/SMC-AWS_Support_SQS.json "https://servicecatalogconnector.s3.amazonaws.com/SMC-AWS_Support_SQS.json"), and Connector for Service Management - [AWS Support GovCloud West Region](https://servicecatalogconnector.s3.amazonaws.com/SMC-AWS_Support_SQS.json "https://servicecatalogconnector.s3.amazonaws.com/SMC-AWS_Support_SQS.json").
