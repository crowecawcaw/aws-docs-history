# Logging CloudWatch Logs API and console operations in AWS CloudTrail

Amazon CloudWatch Logs is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a service that provides a record of actions taken by a user, role, or an
AWS service. CloudTrail captures API calls for CloudWatch Logs as events. The calls captured include calls from the CloudWatch Logs console
and code calls to the CloudWatch Logs API operations. Using the information collected by CloudTrail, you can
determine the request that was made to CloudWatch Logs, the IP address from which the request was
made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity
information helps you determine the following:

- Whether the request was made with root user or user credentials.
- Whether the request was made on behalf of an IAM Identity Center user.
- Whether the request was made with temporary security credentials for a role or federated
  user.
- Whether the request was made by another AWS service.
  CloudTrail is active in your AWS account when you create the account and you automatically have
  access to the CloudTrail **Event history**. The CloudTrail **Event
  history** provides a viewable, searchable, downloadable, and immutable record of the
  past 90 days of recorded management events in an AWS Region. For more information, see [Working
  with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_. There are no CloudTrail
  charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a
[CloudTrail
Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") event data store.

**CloudTrail trails**

A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") and [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the _AWS CloudTrail User Guide_.

You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

**CloudTrail Lake event data stores**

_CloudTrail Lake_ lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/") format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into _event data stores_, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors"). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") in the _AWS CloudTrail User Guide_.

CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

CloudWatch Logs supports logging the following actions as events in CloudTrail log files:

- [AssociateKmsKey](../../../AmazonCloudWatchLogs/latest/APIReference/API_AssociateKmsKey.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_AssociateKmsKey.md")
- [CancelExportTask](../../../AmazonCloudWatchLogs/latest/APIReference/API_CancelExportTask.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CancelExportTask.md")
- [CreateDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md")
- [CreateExportTask](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateExportTask.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateExportTask.md")
- [CreateLogAnomalyDetector](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogAnomalyDetector.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogAnomalyDetector.md")
- [CreateLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md")
- [CreateLogStream](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md")
- [DeleteAccountPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteAccountPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteAccountPolicy.md")
- [DeleteDataProtectionPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDataProtectionPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDataProtectionPolicy.md")
- [DeleteDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDelivery.md")
- [DeleteDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliveryDestination.md")
- [DeleteDeliveryDestinationPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliveryDestinationPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliveryDestinationPolicy.md")
- [DeleteDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.md")
- [DeleteDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDestination.md")
- [DeleteIndexPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteIndexPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteIndexPolicy.md")
- [DeleteIntegration](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteIntegration.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteIntegration.md")
- [DeleteLogAnomalyDetector](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogAnomalyDetector.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogAnomalyDetector.md")
- [DeleteLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogGroup.md")
- [DeleteLogStream](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogStream.md")
- [DeleteMetricFilter](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteMetricFilter.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteMetricFilter.md")
- [DeleteQueryDefinition](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteQueryDefinition.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteQueryDefinition.md")
- [DeleteResourcePolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteResourcePolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteResourcePolicy.md")
- [DeleteRetentionPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.md")
- [DeleteSubscriptionFilter](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteSubscriptionFilter.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteSubscriptionFilter.md")
- [DeleteTransformer](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteTransformer.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteTransformer.md")
- [DescribeAccountPolicies](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeAccountPolicies.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeAccountPolicies.md")
- [DescribeConfigurationTemplates](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.md")
- [DescribeDeliveries](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveries.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveries.md")
- [DescribeDeliveryDestinations](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveryDestinations.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveryDestinations.md")
- [DescribeDeliverySources](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliverySources.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliverySources.md")
- [DescribeDestinations](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDestinations.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDestinations.md")
- [DescribeExportTasks](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeExportTasks.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeExportTasks.md")
- [DescribeFieldIndexes](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeFieldIndexes.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeFieldIndexes.md")
- [DescribeIndexPolicies](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeIndexPolicies.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeIndexPolicies.md")
- [DescribeLogGroups](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.md")
- [DescribeLogStreams](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogStreams.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogStreams.md")
- [DescribeMetricFilters](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeMetricFilters.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeMetricFilters.md")
- [DescribeQueries](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueries.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueries.md")
- [DescribeQueryDefinitions](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.md")
- [DescribeResourcePolicies](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeResourcePolicies.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeResourcePolicies.md")
- [DescribeSubscriptionFilters](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeSubscriptionFilters.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeSubscriptionFilters.md")
- [DisassociateKmsKey](../../../AmazonCloudWatchLogs/latest/APIReference/API_DisassociateKmsKey.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DisassociateKmsKey.md")
- [FilterLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.md")
- [GetDataProtectionPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetDataProtectionPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetDataProtectionPolicy.md")
- [GetDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetDelivery.md")
- [GetDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetDeliveryDestination.md")
- [GetDeliveryDestinationPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetDeliveryDestinationPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetDeliveryDestinationPolicy.md")
- [GetDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetDeliverySource.md")
- [GetIntegration](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetIntegration.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetIntegration.md")
- [GetLogAnomalyDetector](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogAnomalyDetector.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogAnomalyDetector.md")
- [GetLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.md")
- [GetLogGroupFields](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogGroupFields.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogGroupFields.md")
- [GetLogRecord](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogRecord.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogRecord.md")
- [GetQueryResults](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.md")
- [GetTransformer](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetTransformer.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetTransformer.md")
- [ListAnomalies](../../../AmazonCloudWatchLogs/latest/APIReference/API_ListAnomalies.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_ListAnomalies.md")
- [ListIntegrations](../../../AmazonCloudWatchLogs/latest/APIReference/API_ListIntegrations.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_ListIntegrations.md")
- [ListLogAnomalyDetectors](../../../AmazonCloudWatchLogs/latest/APIReference/API_ListLogAnomalyDetectors.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_ListLogAnomalyDetectors.md")
- [ListLogGroups](../../../AmazonCloudWatchLogs/latest/APIReference/API_ListLogGroups.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_ListLogGroups.md")
- [ListLogGroupsForQuery](../../../AmazonCloudWatchLogs/latest/APIReference/API_ListLogGroupsForQuery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_ListLogGroupsForQuery.md")
- [ListTagsForResource](../../../AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.md")
- [ListTagsLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_ListTagsLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_ListTagsLogGroup.md")
- [PutAccountPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.md")
- [PutDataProtectionPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.md")
- [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md")
- [PutDeliveryDestinationPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.md")
- [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md")
- [PutDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.md")
- [PutDestinationPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.md")
- [PutIndexPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.md")
- [PutIntegration](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutIntegration.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutIntegration.md")
- [PutMetricFilter](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutMetricFilter.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutMetricFilter.md")
- [PutQueryDefinition](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutQueryDefinition.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutQueryDefinition.md")
- [PutResourcePolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.md")
- [PutRetentionPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutRetentionPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutRetentionPolicy.md")
- [PutSubscriptionFilter](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutSubscriptionFilter.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutSubscriptionFilter.md")
- [PutTransformer](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.md")
- [StartLiveTail](../../../AmazonCloudWatchLogs/latest/APIReference/API_StartLiveTail.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_StartLiveTail.md")
- [StartQuery](../../../AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.md")
- [StopQuery](../../../AmazonCloudWatchLogs/latest/APIReference/API_StopQuery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_StopQuery.md")
- [TagResource](../../../AmazonCloudWatchLogs/latest/APIReference/API_TagResource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_TagResource.md")
- [TestMetricFilter](../../../AmazonCloudWatchLogs/latest/APIReference/API_TestMetricFilter.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_TestMetricFilter.md")
- [TestTransformer](../../../AmazonCloudWatchLogs/latest/APIReference/API_TestTransformer.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_TestTransformer.md")
- [UntagResource](../../../AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.md")
- [UpdateAnomaly](../../../AmazonCloudWatchLogs/latest/APIReference/API_UpdateAnomaly.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_UpdateAnomaly.md")
- [UpdateDeliveryConfiguration](../../../AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.md")
- [UpdateLogAnomalyDetector](../../../AmazonCloudWatchLogs/latest/APIReference/API_UpdateLogAnomalyDetector.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_UpdateLogAnomalyDetector.md")
  Every event or log entry contains information about who generated the request. The
  identity information helps you determine the following:

- Whether the request was made with root or IAM user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.
  For more information, see the [CloudTrail userIdentity
  Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Query generation information in CloudTrail

CloudTrail logging for Query generator console events is also supported. Query generator is currently supported for CloudWatch Logs Insights and
CloudWatch Metric Insights. In these CloudTrail events, the `eventSource` is `monitoring.amazonaws.com`.

The following example shows a
CloudTrail log entry that demonstrates the **GenerateQuery** action in CloudWatch Logs Insights.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::123456789012:assumed-role/role_name",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111222333444:role/Administrator",
                "accountId": "123456789012",
                "userName": "SAMPLE_NAME"
            },
            "attributes": {
                "creationDate": "2020-04-08T21:43:24Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2020-04-08T23:06:30Z",
    "eventSource": "monitoring.amazonaws.com",
    "eventName": "GenerateQuery",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "exampleUserAgent",
    "requestParameters": {
        "query_ask": "***",
        "query_type": "LogsInsights",
        "logs_insights": {
            "fields": "***",
            "log_group_names": ["yourloggroup"]
        },
        "include_description": true
    },
    "responseElements": null,
    "requestID": "2f56318c-cfbd-4b60-9d93-1234567890",
    "eventID": "52723fd9-4a54-478c-ac55-1234567890",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

## Understanding log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following log file entry shows that a user called the CloudWatch Logs
**CreateExportTask** action.

```
{
        "eventVersion": "1.03",
        "userIdentity": {
            "type": "IAMUser",
            "principalId": "EX_PRINCIPAL_ID",
            "arn": "arn:aws:iam::123456789012:user/someuser",
            "accountId": "123456789012",
            "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "userName": "someuser"
        },
        "eventTime": "2016-02-08T06:35:14Z",
        "eventSource": "logs.amazonaws.com",
        "eventName": "CreateExportTask",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "127.0.0.1",
        "userAgent": "aws-sdk-ruby2/2.0.0.rc4 ruby/1.9.3 x86_64-linux Seahorse/0.1.0",
        "requestParameters": {
            "destination": "yourdestination",
            "logGroupName": "yourloggroup",
            "to": 123456789012,
            "from": 0,
            "taskName": "yourtask"
        },
        "responseElements": {
            "taskId": "15e5e534-9548-44ab-a221-64d9d2b27b9b"
        },
        "requestID": "1cd74c1c-ce2e-12e6-99a9-8dbb26bd06c9",
        "eventID": "fd072859-bd7c-4865-9e76-8e364e89307c",
        "eventType": "AwsApiCall",
        "apiVersion": "20140328",
        "recipientAccountId": "123456789012"
}
```
