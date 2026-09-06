

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring AWS Security Hub CSPM Integration
<a name="config-security-hub"></a>

AWS Security Hub CSPM enables users to view security findings from AWS services, such as Amazon Guard Duty, Amazon Inspector, as well as AWS Partner solutions.

If you use both [AWS Security Hub](https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc) and [Jira Service Management](https://www.atlassian.com/software/jira/service-management) (JSM), the AWS Service Management Connector for JSM allows you to create an automated, bidirectional integration between Security Hub CSPM and JSM. This two-way integration synchronizes your Security Hub findings and Jira issues.

Specifically, as a Jira administrator, you can use this integration to automatically create Jira issues from Security Hub CSPM findings. When you update those tickets in Jira, the changes are automatically replicated back to the original Security Hub CSPM findings. For example, when you resolve the issue in Jira, the workflow status of the Security Hub CSPM finding also changes to `RESOLVED`. This action ensures Security Hub CSPM always has up-to-date information about your security posture.

**To configure AWS Security Hub CSPM integration features**

1. Enable AWS Security Hub CSPM. For more information, see [Accessing Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html#securityhub-get-started).

1. Set up an SQS queue to receive updated Findings. Name the queue **AwsSmcJsmSecurityHubQueue** to align with the default name in the JSM Connector Settings for the AWS Security Hub CSPM integration. For more information, see [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html).

1. Set up a Amazon EventBridge rule to detect changes to Findings and push these to the queue. For more information, see [Getting started with Amazon EventBridge.](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html) 

   The CloudWatch rule should have the following event pattern and should point to the SQS queue created in Step 2.

   ```
   "EventPattern": {
   
          "source": [
   
           "aws.securityhub"
   
           ]
   }
   ```

1. You can also customize this CloudWatch Events rule to only pull in Security Hub CSPM findings that have specific finding types, severity labels, workflow statuses, or compliance statuses. For details about how to filter the event pattern, see [Configuring an EventBridge rule for automatically sent findings](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cwe-all-findings.html) in the *AWS Security Hub User Guide*.

**Note**  
You can use the available AWS CloudFormation templates for the JSM connector to configure your AWS account to enable AWS Service Catalog integration. For more information, see [Baseline Permissions](https://docs.aws.amazon.com/smc/latest/ag/jsd-baseline-permissions.html).

## Video: Bidirectional integration with Atlassian Jira Service Management
<a name="video-intro-sh-jira"></a>

This video (8:40) describes how to set up a bidirectional integration with Atlassian Jira Service Management. This feature makes it easier for AWS Security Hub CSPM users to automatically create and update issues in Jira Service Management from AWS Security Hub CSPM findings and ensure that updates to those tickets are synced with the findings.

[![AWS Videos](http://img.youtube.com/vi/uEKwu0M8S3M/0.jpg)](http://www.youtube.com/watch?v=uEKwu0M8S3M)
