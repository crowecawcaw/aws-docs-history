

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring Support Integration
<a name="config-support"></a>

To enable the Connector to synchronize Support tickets, the account should have a [Business](https://aws.amazon.com/premiumsupport/plans/business/) or [Enterprise](https://aws.amazon.com/premiumsupport/plans/enterprise/) Support plan. For more information, see [Getting started with Support.](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html)

**Note**  
AWS Service Management Connector allows AWS Managed Services (AMS) Accelerate users to create Incidents and Service Requests through Jira Service Management. To ensure that your account has the required permissions to create AMS Accelerate (Accelerate) support cases, make sure you onboard your account to Accelerate. For more information, see [Getting Started with AMS Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/getting-started-acc.html).

**To configure Support integration features**

1. Set up an SQS queue (in N.Virginia (us-east-1) for Commercial regions and US West (us-gov-west-1) for GovCloud regions) to receive updates on Support cases. Name the queue **AWSServiceManagementConnectorSupportQueue **to align with the default name within the JSM Connector Settings for the Support integration. For more information, see [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html).

1. Set up an Amazon EventBridge rule to detect changes to Support case and push these to the queue. For more information, see [Getting Started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html).

   The Amazon EventBridge rule should have the following event pattern and should point to the SQS queue created in Step 2.

   ```
   EventPattern":{
      "source":[
         "aws.support"
      ],
   }
   ```

**Note**  
You can use the available AWS CloudFormation templates for the JSM connector to configure your AWS account to enable AWS Service Catalog integration. For more information, see [Baseline Permissions](https://docs.aws.amazon.com/smc/latest/ag/jsd-baseline-permissions.html).

For creation of SQS queue and EventBridge rule, use [ Connector for Jira Service Management - AWS Support Commercial Regions](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForJSMv1.9.0-AWS_Support_Configurations_Commercial.json) and [ Connector for Jira Service Management AWS Support GovCloud West Region](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForJSMv1.9.0-AWS_Support_Configurations_GovCloud.json).