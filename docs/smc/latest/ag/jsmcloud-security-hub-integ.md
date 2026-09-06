

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring AWS Security Hub CSPM integration
<a name="jsmcloud-security-hub-integ"></a>

This section describes how to configure your AWS services in Jira Service Management Cloud.

**To configure AWS Security Hub CSPM integration features**

1. Enable AWS Security Hub CSPM. For more information, refer to [Setting up AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) with the Console. 

1. Set up an SQS queue to receive updated Findings. Name the queue, `AwsSmcJsmCloudForgeSecurityHubQueue`, to align with the default name in the Jira Service Management Connector Settings for the AWS Security Hub CSPM integration. For more information, refer to [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html). 

1. Set up an Amazon EventBridge rule to detect changes to Findings and push these to the queue. For more information, refer to [Getting started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html).

   The CloudWatch rule should have this event pattern and point to the SQS queue created in Step 2.

   ```
                       
                       "EventPattern": {"source": [
                       
                           "aws.securityhub"
                           
                           ]
                       }
   ```

1. You can also customize this CloudWatch Events rule to only pull in Security Hub CSPM Findings that have specific Finding types, severity labels, workflow statuses, or compliance statuses. For details about how to filter the event pattern, refer to [Configuring an EventBridge rule for automatically sent findings](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cwe-all-findings.html) in the *AWS Security Hub CSPM User Guide*.

**Note**  
You can use the AWS CloudFormation templates for the Connector for Jira Service Management to automate the AWS Config custom resource and AWS Security Hub CSPM integration features. For more information, refer to [Setting baseline permissions for AWS Service Management Connector for ServiceNow](sn-base-perms.md). 