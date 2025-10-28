# Streaming CloudWatch Logs data to Amazon OpenSearch Service

You can configure a log group in Amazon CloudWatch Logs, so you can stream data to your Amazon OpenSearch Service cluster in near real-time.
For more information, see [Real-time processing of log data with subscriptions](Subscriptions.md "Subscriptions.md").

###### Note

Streaming to OpenSearch Service is supported only for log groups in the Standard log class.
For more information about log classes, see [Log classes](CloudWatch_Logs_Log_Classes.md "CloudWatch_Logs_Log_Classes.md").

Depending on the amount of log data that's streamed, consider setting a function-level concurrency limit.
For more information, see [Lambda function scaling](../../../lambda/latest/dg/concurrent-executions.md#per-function-concurrency "../../../lambda/latest/dg/concurrent-executions.md#per-function-concurrency").

###### Note

Because streaming large amounts of CloudWatch Logs data to OpenSearch Service might result in high usage charges, we recommend that you create a budget in the AWS Billing and Cost Management console.
For more information, see [Managing your costs with AWS Budgets](../../../awsaccountbilling/latest/aboutv2/budgets-managing-costs.md "../../../awsaccountbilling/latest/aboutv2/budgets-managing-costs.md").

This section describes the prerequisites you must complete before subscribing a log group to OpenSearch Service.
It also describes how to subscribe a log group to OpenSearch Service.

## Prerequisites

Before you begin, create an OpenSearch Service domain. The domain can have either public access or
VPC access, but you can't then modify the type of access after the domain is created.
You might want to review your OpenSearch Service domain settings later, and modify your cluster
configuration based on the amount of data your cluster will be processing. For
instructions to create a domain, see [Creating OpenSearch Service
domains](../../../opensearch-service/latest/developerguide/createupdatedomains.md#createdomains "../../../opensearch-service/latest/developerguide/createupdatedomains.md#createdomains").

For more information about OpenSearch Service, see the [Amazon OpenSearch Service Developer Guide](../../../opensearch-service/latest/developerguide.md "../../../opensearch-service/latest/developerguide.md").

## Subscribe a log group to OpenSearch Service

You can use the CloudWatch console to subscribe a log group to OpenSearch Service.

###### To subscribe a log group to OpenSearch Service

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Log groups**.
3. Select the name of the log group.
4. Choose **Actions**, **Subscription
   filters**, **Create Amazon OpenSearch Service subscription
   filter**.
5. Choose whether you want to stream to a cluster in this account or another
   account.
   - If you chose this account, select the domain you created in the
     previous step.
   - If you chose another account, provide the domain ARN and
     endpoint.

6. For **Lambda IAM Execution Role**, choose the IAM role
   that Lambda should use when executing calls to OpenSearch.

The IAM role you choose must fulfill these requirements:

    * It must have `lambda.amazonaws.com` in the trust relationship.
    * It must include the following policy:



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Sid": "AllowOpenSearchStreamingAccess",
     "Action": [
     "es:*"
     ],
     "Effect": "Allow",
     "Resource": "arn:aws:es:`us-east-1`:`123456789012`:domain/`cloudwatch-logs`/*"
     }
     ]
    }`

    ```
    * If the target OpenSearch Service domain uses VPC access, the role must have the
      **AWSLambdaVPCAccessExecutionRole** policy
     attached. This Amazon-managed policy grants Lambda access to the
     customer's VPC, enabling Lambda to write to the OpenSearch endpoint in
     the VPC.

7. For **Log format**, choose a log format.
8. For **Subscription filter pattern**, type the terms or
   pattern to find in your log events. This ensures that you send only the data
   you're interested in to your OpenSearch cluster. For more information, see [Creating metrics from log events using filters](MonitoringLogData.md "MonitoringLogData.md").
9. (Optional) For **Select log data to test**, select a log
   stream and then choose **Test pattern** to verify that your
   search filter is returning the results you expect.
10. Choose **Start streaming**.
