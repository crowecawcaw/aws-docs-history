# Configuring AWS Health integration

This section describes how to configure AWS Health integration in Jira
Service Management.

###### Note

To allow the connector to synchronize AWS Health data for a
specific Region, you must enable AWS Health in that account and Region. For more
information, refer to [What is AWS Health?](../../../health/latest/ug/what-is-aws-health.md "../../../health/latest/ug/what-is-aws-health.md")

**Configuring AWS Health integration**

1. Set up an SQS queue to sync AWS Health events. Name the queue **AwsSmcJsmCloudForgeHealthQueue** to align it with the
   default name in the connector settings. For more information, refer to [Getting started with Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md").
2. Set up an Amazon EventBridge rule to detect changes to findings and push them to the
   queue. For more information, refer to [Getting started with Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md"). The rule should have the
   following event pattern and point to the SQS queue from step 1.

```
"EventPattern": {
    "source": ["aws.health"]
}
```

###### Note

A queue with this name must exist in all Regions defined by the AWS account that
has the AWS Health integration enabled. The default value is **AwsSmcJsmCloudForgeHealthQueue**.

**Configuring AWS Health**

1. Navigate to the **Settings** menu, and then
   choose **Apps**.
2. Choose **AWS Service Management Connector**, and then navigate to
   **Connector** settings.
3. In the **AWS Health** section, enter the SQS
   queue name from where you want to sync the AWS Health. The default value is
   **AwsSmcJsmCloudForgeHealthQueue**. The configured
   queue is available in all AWS accounts and Regions where the integration is
   configured.
4. Assign onboarded AWS accounts to Jira projects.
5. Choose **Save**.
