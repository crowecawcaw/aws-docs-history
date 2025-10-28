We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Logging Amazon ML API Calls with AWS CloudTrail

Amazon Machine Learning (Amazon ML) is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in Amazon ML. CloudTrail captures all API calls for
Amazon ML as events. The calls captured include calls from the Amazon ML console and
code calls to the Amazon ML API operations. If you create a trail, you can enable continuous delivery
of CloudTrail events to an Amazon S3 bucket, including events for Amazon ML. If you don't configure a trail, you can
still view the most recent events in the CloudTrail console in **Event history**.
Using the information collected by CloudTrail, you can determine the request that was made to
Amazon ML, the IP address from which the request was made, who made the request, when it was
made, and additional details.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Amazon ML Information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported event
activity occurs in Amazon ML, that activity is recorded in a CloudTrail event along with other
AWS service events in **Event history**. You can view, search, and download
recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon ML,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket.
By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events
from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you
specify. Additionally, you can configure other AWS services to further analyze and act upon
the event data collected in CloudTrail logs. For more information, see the following:

- [Overview for
  Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail
  Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Amazon ML supports logging the following actions as events in CloudTrail log files:

- [AddTags](../APIReference/API_AddTags.md "../APIReference/API_AddTags.md")
- [CreateBatchPrediction](../APIReference/API_CreateBatchPrediction.md "../APIReference/API_CreateBatchPrediction.md")
- [CreateDataSourceFromRDS](../APIReference/API_CreateDataSourceFromRDS.md "../APIReference/API_CreateDataSourceFromRDS.md")
- [CreateDataSourceFromRedshift](../APIReference/API_CreateDataSourceFromRedshift.md "../APIReference/API_CreateDataSourceFromRedshift.md")
- [CreateDataSourceFromS3](../APIReference/API_CreateDataSourceFromS3.md "../APIReference/API_CreateDataSourceFromS3.md")
- [CreateEvaluation](../APIReference/API_CreateEvaluation.md "../APIReference/API_CreateEvaluation.md")
- [CreateMLModel](../APIReference/API_CreateMLModel.md "../APIReference/API_CreateMLModel.md")
- [CreateRealtimeEndpoint](../APIReference/API_CreateRealtimeEndpoint.md "../APIReference/API_CreateRealtimeEndpoint.md")
- [DeleteBatchPrediction](../APIReference/API_DeleteBatchPrediction.md "../APIReference/API_DeleteBatchPrediction.md")
- [DeleteDataSource](../APIReference/API_DeleteDataSource.md "../APIReference/API_DeleteDataSource.md")
- [DeleteEvaluation](../APIReference/API_DeleteEvaluation.md "../APIReference/API_DeleteEvaluation.md")
- [DeleteMLModel](../APIReference/API_DeleteMLModel.md "../APIReference/API_DeleteMLModel.md")
- [DeleteRealtimeEndpoint](../APIReference/API_DeleteRealtimeEndpoint.md "../APIReference/API_DeleteRealtimeEndpoint.md")
- [DeleteTags](../APIReference/API_DeleteTags.md "../APIReference/API_DeleteTags.md")
- [DescribeTags](../APIReference/API_DescribeTags.md "../APIReference/API_DescribeTags.md")
- [UpdateBatchPrediction](../APIReference/API_UpdateBatchPrediction.md "../APIReference/API_UpdateBatchPrediction.md")
- [UpdateDataSource](../APIReference/API_UpdateDataSource.md "../APIReference/API_UpdateDataSource.md")
- [UpdateEvaluation](../APIReference/API_UpdateEvaluation.md "../APIReference/API_UpdateEvaluation.md")
- [UpdateMLModel](../APIReference/API_UpdateMLModel.md "../APIReference/API_UpdateMLModel.md")

The following Amazon ML operations use request parameters that contain credentials. Before
these requests are sent to CloudTrail, the credentials are replaced with three
asterisks ("\*\*\*"):

- [CreateDataSourceFromRDS](../APIReference/API_CreateDataSourceFromRDS.md "../APIReference/API_CreateDataSourceFromRDS.md")
- [CreateDataSourceFromRedshift](../APIReference/API_CreateDataSourceFromRedshift.md "../APIReference/API_CreateDataSourceFromRedshift.md")

When the following Amazon ML operations are performed with the Amazon ML console, the attribute
`ComputeStatistics` is not included in the `RequestParameters` component
of the CloudTrail log:

- [CreateDataSourceFromRedshift](../APIReference/API_CreateDataSourceFromRedshift.md "../APIReference/API_CreateDataSourceFromRedshift.md")
- [CreateDataSourceFromS3](../APIReference/API_CreateDataSourceFromS3.md "../APIReference/API_CreateDataSourceFromS3.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Example: Amazon ML Log File Entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the action.

```

{
    "Records": [
        {
            "eventVersion": "1.03",
            "userIdentity": {
                "type": "IAMUser",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::012345678910:user/Alice",
                "accountId": "012345678910",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "userName": "Alice"
            },
            "eventTime": "2015-11-12T15:04:02Z",
            "eventSource": "machinelearning.amazonaws.com",
            "eventName": "CreateDataSourceFromS3",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "127.0.0.1",
            "userAgent": "console.amazonaws.com",
            "requestParameters": {
                "data": {
                    "dataLocationS3": "s3://aml-sample-data/banking-batch.csv",
                    "dataSchema": "{\"version\":\"1.0\",\"rowId\":null,\"rowWeight\":null,
                        \"targetAttributeName\":null,\"dataFormat\":\"CSV\",
                        \"dataFileContainsHeader\":false,\"attributes\":[
                          {\"attributeName\":\"age\",\"attributeType\":\"NUMERIC\"},
                          {\"attributeName\":\"job\",\"attributeType\":\"CATEGORICAL\"},
                          {\"attributeName\":\"marital\",\"attributeType\":\"CATEGORICAL\"},
                          {\"attributeName\":\"education\",\"attributeType\":\"CATEGORICAL\"},
                          {\"attributeName\":\"default\",\"attributeType\":\"CATEGORICAL\"},
                          {\"attributeName\":\"housing\",\"attributeType\":\"CATEGORICAL\"},
                          {\"attributeName\":\"loan\",\"attributeType\":\"CATEGORICAL\"},
                          {\"attributeName\":\"contact\",\"attributeType\":\"CATEGORICAL\"},
                          {\"attributeName\":\"month\",\"attributeType\":\"CATEGORICAL\"},
                          {\"attributeName\":\"day_of_week\",\"attributeType\":\"CATEGORICAL\"},
                          {\"attributeName\":\"duration\",\"attributeType\":\"NUMERIC\"},
                          {\"attributeName\":\"campaign\",\"attributeType\":\"NUMERIC\"},
                          {\"attributeName\":\"pdays\",\"attributeType\":\"NUMERIC\"},
                          {\"attributeName\":\"previous\",\"attributeType\":\"NUMERIC\"},
                          {\"attributeName\":\"poutcome\",\"attributeType\":\"CATEGORICAL\"},
                          {\"attributeName\":\"emp_var_rate\",\"attributeType\":\"NUMERIC\"},
                          {\"attributeName\":\"cons_price_idx\",\"attributeType\":\"NUMERIC\"},
                          {\"attributeName\":\"cons_conf_idx\",\"attributeType\":\"NUMERIC\"},
                          {\"attributeName\":\"euribor3m\",\"attributeType\":\"NUMERIC\"},
                          {\"attributeName\":\"nr_employed\",\"attributeType\":\"NUMERIC\"}
                        ],\"excludedAttributeNames\":[]}"
                },
                "dataSourceId": "exampleDataSourceId",
                "dataSourceName": "Banking sample for batch prediction"
            },
            "responseElements": {
                "dataSourceId": "exampleDataSourceId"
            },
            "requestID": "9b14bc94-894e-11e5-a84d-2d2deb28fdec",
            "eventID": "f1d47f93-c708-495b-bff1-cb935a6064b2",
            "eventType": "AwsApiCall",
            "recipientAccountId": "012345678910"
        },
        {
            "eventVersion": "1.03",
            "userIdentity": {
                "type": "IAMUser",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::012345678910:user/Alice",
                "accountId": "012345678910",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "userName": "Alice"
            },
            "eventTime": "2015-11-11T15:24:05Z",
            "eventSource": "machinelearning.amazonaws.com",
            "eventName": "CreateBatchPrediction",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "127.0.0.1",
            "userAgent": "console.amazonaws.com",
            "requestParameters": {
                "batchPredictionName": "Batch prediction: ML model: Banking sample",
                "batchPredictionId": "exampleBatchPredictionId",
                "batchPredictionDataSourceId": "exampleDataSourceId",
                "outputUri": "s3://EXAMPLE_BUCKET/BatchPredictionOutput/",
                "mLModelId": "exampleModelId"
            },
            "responseElements": {
                "batchPredictionId": "exampleBatchPredictionId"
            },
            "requestID": "3e18f252-8888-11e5-b6ca-c9da3c0f3955",
            "eventID": "db27a771-7a2e-4e9d-bfa0-59deee9d936d",
            "eventType": "AwsApiCall",
            "recipientAccountId": "012345678910"
        }
    ]
}
```
