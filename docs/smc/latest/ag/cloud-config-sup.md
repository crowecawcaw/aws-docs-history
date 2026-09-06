

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring Support integration
<a name="cloud-config-sup"></a>

This section describes how to configure Support in Jira Service Management Cloud.

**To configure Support integration features**

1. Set up an Amazon SQS queue in us-east-1 for Commercial regions and AWS GovCloud (US-West) for AWS GovCloud (US) to sync Support cases. 

1. Enter **AwsSmcJsmCloudForgeSupportQueue** for the queue name, which aligns with the default name in the JSM Cloud connector settings for the Support integration. For more information, review [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html). 

1. Create an Amazon EventBridge rule to detect changes to Support cases and push those changes to the queue. For more information, review [Getting started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html). 

1. The rule you created must have the following event pattern and point to the Amazon SQS queue you created in step 1:

   ```
   "EventPattern":{
        {
           "detail-type":[
               "Support Case Update"
           ],
           "source":[
               "aws.support"
          ]
       }
   }
   ```

**Note**  
You can use baseline AWS CloudFormation templates for the Connector for JSM Cloud to automate the Support integration features. For more information, see [Setting baseline permissions for AWS Service Management Connector for ServiceNow](sn-base-perms.md).   
To create the required Amazon SQS queue and EventBridge rule, use Connector for JSM Cloud - [AWS Support Commercial Regions](https://servicecatalogconnector.s3.amazonaws.com/SMC_ConnectorforJSMCloud-AWS_Support_Commercial.json) and Connector for Service Management - [AWS Support for GovCloud West Region](https://servicecatalogconnector.s3.amazonaws.com/SMC_ConnectorforJSMCloud-AWS_Support_Gov.json). 