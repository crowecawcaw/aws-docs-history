# Logging Amazon RDS Data API calls with AWS CloudTrail

RDS Data API (Data API) is integrated with AWS CloudTrail, a service that provides a record of
actions taken by a user, role, or an AWS service in Data API. CloudTrail captures all API calls for
Data API as events, including calls from the Amazon RDS console and from code calls to Data API
operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3
bucket, including events for Data API. Using the data collected by CloudTrail, you can determine a lot
of information. This information includes the request that was made to Data API, the IP address
the request was made from, who made the request, when it was made, and additional
details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Working with Data API information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported
activity (management events) occurs in Data API, that activity is recorded in a CloudTrail event
along with other AWS service events in **Event history**. You can view,
search, and download recent management events in your AWS account. For more information, see
[Working with CloudTrail Event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide._

For an ongoing record of events in your AWS account, including events for Data API,
create a trail. A _trail_ enables CloudTrail to deliver log files
to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to
all AWS Regions. The trail logs events from all AWS Regions in the AWS partition and
delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure
other AWS services to further analyze and act upon the event data collected in CloudTrail logs.
For more information, see the following topics in the
_AWS CloudTrail User Guide_:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS notifications
  for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log
  files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log
  files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All Data API operations are logged by CloudTrail and documented in the [_Amazon RDS data service API reference_](../../../rdsdataservice/latest/APIReference/Welcome.md "../../../rdsdataservice/latest/APIReference/Welcome.md"). For example, calls to the
`BatchExecuteStatement`, `BeginTransaction`,
`CommitTransaction`, and `ExecuteStatement` operations generate
entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Including and excluding Data API events from an AWS CloudTrail trail

Most Data API users rely on the events in an AWS CloudTrail trail to provide a record of Data
API operations. Event data doesn't reveal the database name, schema name, or SQL statements in
requests to the Data API. However, knowing which user made a type of call against a specific
DB cluster at a given time can help to detect anomalous access patterns.

### Including Data API events in an AWS CloudTrail trail

For Aurora PostgreSQL Aurora serverless and provisioned databases, the following Data API
operations are logged to AWS CloudTrail as _data events_. [Data
events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") are high-volume data-plane API operations that CloudTrail doesn't log by default.
Additional charges apply for data events. For information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

- [BatchExecuteStatement](../../../rdsdataservice/latest/APIReference/API_BatchExecuteStatement.md "../../../rdsdataservice/latest/APIReference/API_BatchExecuteStatement.md")
- [BeginTransaction](../../../rdsdataservice/latest/APIReference/API_BeginTransaction.md "../../../rdsdataservice/latest/APIReference/API_BeginTransaction.md")
- [CommitTransaction](../../../rdsdataservice/latest/APIReference/API_CommitTransaction.md "../../../rdsdataservice/latest/APIReference/API_CommitTransaction.md")
- [ExecuteStatement](../../../rdsdataservice/latest/APIReference/API_ExecuteStatement.md "../../../rdsdataservice/latest/APIReference/API_ExecuteStatement.md")
- [RollbackTransaction](../../../rdsdataservice/latest/APIReference/API_RollbackTransaction.md "../../../rdsdataservice/latest/APIReference/API_RollbackTransaction.md")

You can use the CloudTrail console,AWS CLI, or CloudTrail API operations to log these Data API operations. In the CloudTrail console, choose **RDS Data API - DB Cluster**
for the Data event type. For more information, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI") in the _AWS CloudTrail User Guide_.

Using the AWS CLI, run the `aws cloudtrail put-event-selectors` command to log these Data API operations for your trail.
To log all Data API events on DB clusters, specify `AWS::RDS::DBCluster` for the
resource type. The following example logs all
Data API events on DB clusters. For more information, see [Logging data events with the AWS Command Line Interface](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli.md") in the _AWS CloudTrail User Guide_.

```
aws cloudtrail put-event-selectors --trail-name `trail_name` --advanced-event-selectors \
'{
   "Name": "RDS Data API Selector",
   "FieldSelectors": [
      {
         "Field": "eventCategory",
         "Equals": [
            "Data"
         ]
      },
      {
         "Field": "resources.type",
         "Equals": [
            "AWS::RDS::DBCluster"
         ]
      }
   ]
}'
```

You can configure advanced event selectors to additionally filter on the `readOnly`, `eventName,` and `resources.ARN` fields.
For more information on these fields, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md").

## Understanding Data API log file entries

A _trail_ is a configuration that enables delivery of
events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log
entries. An _event_ represents a single request from any
source and includes information about the requested action, the date and time of the action,
request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public
API calls, so they don't appear in any specific order.

**Aurora PostgreSQL Aurora serverless and provisioned**

The following example shows a CloudTrail log entry that demonstrates the
`ExecuteStatement` operation for Aurora PostgreSQL Aurora serverless and provisioned databases. For these databases,
all Data API events are data events where the event source is **rdsdataapi.amazonaws.com** and the event type is
**Rds Data Service**.

```

{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AKIAIOSFODNN7EXAMPLE",
        "arn": "arn:aws:iam::123456789012:user/johndoe",
        "accountId": "123456789012",
        "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
        "userName": "johndoe"
    },
    "eventTime": "2019-12-18T00:49:34Z",
    "eventSource": "**rdsdataapi.amazonaws.com**",
    "eventName": "ExecuteStatement",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/1.16.102 Python/3.7.2 Windows/10 botocore/1.12.92",
    "requestParameters": {
        "continueAfterTimeout": false,
        "database": "**********",
        "includeResultMetadata": false,
        "parameters": [],
        "resourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:my-database-1",
        "schema": "**********",
        "secretArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:dataapisecret-ABC123",
        "sql": "**********"
    },
    "responseElements": null,
    "requestID": "6ba9a36e-b3aa-4ca8-9a2e-15a9eada988e",
    "eventID": "a2c7a357-ee8e-4755-a0d0-aed11ed4253a",
    "eventType": "**Rds Data Service**",
    "recipientAccountId": "123456789012"
}

```
