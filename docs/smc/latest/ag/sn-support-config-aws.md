

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring Support integration in ServiceNow
<a name="sn-support-config-aws"></a>

This section describes how to configure Support integration in ServiceNow.

**To configure AWS Support integration features**

1. Set up an SQS queue (in N.Virginia (us-east-1) for Commercial regions and US West (us-gov-west-1) for GovCloud regions) to sync AWS Support cases. Name the queue, **AwsServiceManagementConnectorForSupportQueue**, to align with the default name in the ServiceNow System Properties for the AWS Support integration. For more information, see [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html).

1. Set up an Amazon EventBridge rule to detect changes to AWS Support Cases and push these to the queue. For more information, see [Getting started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html). 

The rule should have this event pattern and point to the SQS queue created in Step 1.

```
            "EventPattern": {
{
    "detail-type": ["Support Case Update"],
    "source": ["aws.support"]
}
}
```

**Note**  
You can use baseline CloudFormation tempates for the Connector for ServiceNow to automate the Support integration features. For more information, see [Baseline Permissions](https://docs.aws.amazon.com/en_us/smc/latest/ag/sn-base-perms.html).   
To create the required SQS queue and EventBridge rule, use Connector for ServiceNow - [AWS Support Commercial Regions](https://servicecatalogconnector.s3.amazonaws.com/SMC-AWS_Support_SQS.json), and Connector for Service Management - [AWS Support GovCloud West Region](https://servicecatalogconnector.s3.amazonaws.com/SMC-AWS_Support_SQS.json). 