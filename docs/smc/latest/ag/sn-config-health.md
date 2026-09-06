

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring AWS
<a name="sn-config-health"></a>

This section describes how to configure AWS Health integration in ServiceNow.

**Configure AWS for health-integration features**

1. Set up an Amazon SQS queue to sync AWS Health events. Name the queue, **AwsServiceManagementConnectorForHealthDashboardQueue**, to align with the default name in the ServiceNow System Properties for the AWS Health integration. For more information, refer to [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html).

1. Set up an Amazon EventBridge rule to detect **Health Event** changes and push them to the queue. For more information, refer to [Getting started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html). The rule should have the following event pattern and point to the Amazon SQS queue from step 1:

```
"EventPattern":
{
    "source":
    [
        "aws.health"
    ]
}
```

**Note**  
The SQS queue synchronizes every five minutes. To change this threshold, navigate to **Scheduled Jobs**, and modify the **Repeat Interval** value of the **Synchronize AWS Health** job.

**Note**  
You can use baseline CloudFormation tempates to automate AWS Health integration features. For more information, refer to [Setting baseline permissions for AWS Service Management Connector for ServiceNow](sn-base-perms.md). 