# Configuring Support integration

This section describes how to configure Support in
Jira Service Management Cloud.

###### To configure Support integration features

1. Set up an Amazon SQS queue in us-east-1 for Commercial regions and AWS GovCloud (US-West) for AWS GovCloud (US) to sync Support cases.
2. Enter `AwsSmcJsmCloudForgeSupportQueue` for the queue name, which
   aligns with the default name in the JSM Cloud connector settings for the Support integration.
   For more information, review [Getting started with Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md").
3. Create an Amazon EventBridge rule to detect changes to Support cases and push those changes to the
   queue. For more information, review [Getting started with Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md").
4. The rule you created must have the following event pattern and point to the Amazon SQS
   queue you created in step 1:

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

###### Note

You can use baseline AWS CloudFormation templates for the Connector for JSM Cloud to automate the Support integration features.
For more information, see [Setting baseline
permissions for AWS Service Management Connector for ServiceNow](sn-base-perms.md "sn-base-perms.md").

To create the required Amazon SQS queue and EventBridge rule, use Connector for JSM Cloud -
[AWS Support Commercial Regions](https://servicecatalogconnector.s3.amazonaws.com/SMC_ConnectorforJSMCloud-AWS_Support_Commercial.json "https://servicecatalogconnector.s3.amazonaws.com/SMC_ConnectorforJSMCloud-AWS_Support_Commercial.json")
and Connector for Service Management - [AWS Support for GovCloud West Region](https://servicecatalogconnector.s3.amazonaws.com/SMC_ConnectorforJSMCloud-AWS_Support_Gov.json "https://servicecatalogconnector.s3.amazonaws.com/SMC_ConnectorforJSMCloud-AWS_Support_Gov.json").
