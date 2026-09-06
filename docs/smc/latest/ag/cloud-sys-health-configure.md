

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring AWS Health integration
<a name="cloud-sys-health-configure"></a>

This section describes how to configure AWS Health integration in Jira Service Management.

**Note**  
To allow the connector to synchronize AWS Health data for a specific Region, you must enable AWS Health in that account and Region. For more information, refer to [What is AWS Health?](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)

**Configuring AWS Health integration**

1. Set up an SQS queue to sync AWS Health events. Name the queue **AwsSmcJsmCloudForgeHealthQueue** to align it with the default name in the connector settings. For more information, refer to [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html).

1. Set up an Amazon EventBridge rule to detect changes to findings and push them to the queue. For more information, refer to [Getting started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html). The rule should have the following event pattern and point to the SQS queue from step 1.

```
"EventPattern": {
    "source": ["aws.health"]
}
```

**Note**  
A queue with this name must exist in all Regions defined by the AWS account that has the AWS Health integration enabled. The default value is **AwsSmcJsmCloudForgeHealthQueue**.

**Configuring AWS Health**

1. Navigate to the **Settings** menu, and then choose **Apps**.

1. Choose **AWS Service Management Connector**, and then navigate to **Connector** settings.

1. In the **AWS Health** section, enter the SQS queue name from where you want to sync the AWS Health. The default value is **AwsSmcJsmCloudForgeHealthQueue**. The configured queue is available in all AWS accounts and Regions where the integration is configured. 

1. Assign onboarded AWS accounts to Jira projects.

1. Choose **Save**.