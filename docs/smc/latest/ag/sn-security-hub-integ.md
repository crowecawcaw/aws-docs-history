

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring AWS Security Hub CSPM in ServiceNow
<a name="sn-security-hub-integ"></a>

This section describes how to configure your AWS services in ServiceNow.

**To configure AWS Security Hub CSPM integration features**

1. Enable AWS Security Hub CSPM. For more information, see [Setting up AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) with the Console. 

1. Set up an SQS queue to receive updated Findings. Name the queue, `AwsServiceManagementConnectorForSecurityHubQueue`, to align with the default name in the ServiceNow System Properties for the AWS Security Hub CSPM integration. For more information, see [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html). 

1. Set up an Amazon EventBridge rule to detect changes to Findings and push these to the queue. For more information, see [Getting started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html).

   The rule should have this event pattern and point to the SQS queue created in Step 2.

   ```
   "EventPattern": {
   
          "source": [
   
           "aws.securityhub"
   
           ]
   }
   ```

1. You can also customize this CloudWatch Events rule to only pull in Security Hub CSPM findings that have specific finding types, severity labels, workflow statuses, or compliance statuses. For details about how to filter the event pattern, see [Configuring an EventBridge rule for automatically sent findings](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cwe-all-findings.html) in the *AWS Security Hub User Guide*.

**Note**  
You can use the CloudFormation templates for the Connector for ServiceNow to automate the AWS Config custom resource and AWS Security Hub CSPM integration features. For more information, see [Baseline Permissions](https://docs.aws.amazon.com/smc/latest/ag/sn-base-perms.html). 