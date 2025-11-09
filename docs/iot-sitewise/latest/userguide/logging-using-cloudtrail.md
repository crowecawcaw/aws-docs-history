# Log AWS IoT SiteWise API calls with AWS CloudTrail

AWS IoT SiteWise is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in AWS IoT SiteWise. CloudTrail captures API calls for AWS IoT SiteWise
as events. The calls captured include calls from the AWS IoT SiteWise console and code calls to the
AWS IoT SiteWise API operations. If you create a trail, you can activate continuous delivery of
CloudTrail events to an Amazon S3 bucket, including events for AWS IoT SiteWise. If you don't configure a
trail, you can still view the most recent events in the CloudTrail console in **Event
history**. Using the information collected by CloudTrail, you can determine the request
that was made to AWS IoT SiteWise, the IP address from which the request was made, who made the
request, when it was made, and additional details.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## AWS IoT SiteWise information in CloudTrail

CloudTrail is activated on your AWS account when you create the account. When supported event
activity occurs in AWS IoT SiteWise, that activity is recorded in a CloudTrail event along with other
AWS service events in **Event history**. You can view, search, and download
recent events in your AWS account. For more information, see [Viewing events with CloudTrail event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for AWS IoT SiteWise,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all AWS
Regions. The trail logs events from all Regions in the AWS partition and delivers the log
files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following:

- [Overview for
  creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail
  log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## AWS IoT SiteWise data events in CloudTrail

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") provide information about the resource operations performed on or in a
resource (for example, reading or writing to an Amazon S3
object). These are also known as data
plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log
data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

You can log data events for the AWS IoT SiteWise resource types by using the CloudTrail console, AWS CLI,
or CloudTrail API operations. The [table](#data-events-table "#data-events-table") in this section
shows the resource types available for AWS IoT SiteWise.

- To log data events using the CloudTrail console, create a [trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console") or [event data
  store](../../../awscloudtrail/latest/userguide/query-event-data-store-cloudtrail.md "../../../awscloudtrail/latest/userguide/query-event-data-store-cloudtrail.md") to log data events, or [update an existing trail or event data store](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") to log data events.
  1.  Choose **Data events** to log data events.
  2.  From the **Data event type** list, choose the resource type for
      which you want to log data events.
  3.  Choose the log selector template you want to use. You can log all data events for
      the resource type, log all `readOnly` events, log all
      `writeOnly` events, or create a custom log selector template to filter on
      the `readOnly`, `eventName`, and `resources.ARN`
      fields.

- To log data events using the AWS CLI, configure the
  `--advanced-event-selectors` parameter to set the `eventCategory`
  field equal to `Data` and the `resources.type` field equal to the
  resource type value (see [table](#data-events-table "#data-events-table")). You can add
  conditions to filter on the values of the `readOnly`, `eventName`,
  and `resources.ARN` fields.
  - To configure a trail to log data events, run the [AWS CloudTrail
    put-event-selectors](../../../cli/latest/reference/cloudtrail/put-event-selectors.md "../../../cli/latest/reference/cloudtrail/put-event-selectors.md") command. For more information, see [Logging data events for trails with the AWS CLI](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-CLI-trail-examples "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-CLI-trail-examples").
  - To configure an event data store to log data events, run the [AWS CloudTrail
    create-event-data-store](../../../cli/latest/reference/cloudtrail/create-event-data-store.md "../../../cli/latest/reference/cloudtrail/create-event-data-store.md") command to create a new event data store to log data
    events, or run the [AWS CloudTrail
    update-event-data-store](../../../cli/latest/reference/cloudtrail/update-event-data-store.md "../../../cli/latest/reference/cloudtrail/update-event-data-store.md") command to update an existing event data store. For
    more information, see [Logging data events for event data stores with the AWS CLI](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-CLI-eds-examples "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-CLI-eds-examples").

The following table lists the AWS IoT SiteWise resource types. The **Data
event type (console)** column shows the value to choose from the **Data
event type** list on the CloudTrail console. The **resources.type
value** column shows the `resources.type` value, which you would specify
when configuring advanced event selectors using the AWS CLI or CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API calls logged to CloudTrail
for the resource type.

| Data event type (console)        | resources.type value                   | Data APIs logged to CloudTrail\*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AWS IoT SiteWise asset**       | `AWS::IoTSiteWise::Asset`              | • [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md")<br>• [GetAssetPropertyValue](../APIReference/API_GetAssetPropertyValue.md "../APIReference/API_GetAssetPropertyValue.md")<br>• [GetAssetPropertyValueHistory](../APIReference/API_GetAssetPropertyValueHistory.md "../APIReference/API_GetAssetPropertyValueHistory.md")<br>• [GetAssetPropertyAggregates](../APIReference/API_GetAssetPropertyAggregates.md "../APIReference/API_GetAssetPropertyAggregates.md")<br>• [GetInterpolatedAssetPropertyValues](../APIReference/API_GetInterpolatedAssetPropertyValues.md "../APIReference/API_GetInterpolatedAssetPropertyValues.md")<br>• [BatchGetAssetPropertyValue](../APIReference/API_BatchGetAssetPropertyValue.md "../APIReference/API_BatchGetAssetPropertyValue.md")<br>• [BatchGetAssetPropertyValueHistory](../APIReference/API_BatchGetAssetPropertyValueHistory.md "../APIReference/API_BatchGetAssetPropertyValueHistory.md")<br>• [BatchGetAssetPropertyAggregates](../APIReference/API_BatchGetAssetPropertyAggregates.md "../APIReference/API_BatchGetAssetPropertyAggregates.md") |
| **AWS IoT SiteWise time series** | `AWS::IoTSiteWise::TimeSeries`         | • [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md")<br>• [GetAssetPropertyValue](../APIReference/API_GetAssetPropertyValue.md "../APIReference/API_GetAssetPropertyValue.md")<br>• [GetAssetPropertyValueHistory](../APIReference/API_GetAssetPropertyValueHistory.md "../APIReference/API_GetAssetPropertyValueHistory.md")<br>• [GetAssetPropertyAggregates](../APIReference/API_GetAssetPropertyAggregates.md "../APIReference/API_GetAssetPropertyAggregates.md")<br>• [GetInterpolatedAssetPropertyValues](../APIReference/API_GetInterpolatedAssetPropertyValues.md "../APIReference/API_GetInterpolatedAssetPropertyValues.md")<br>• [BatchGetAssetPropertyValue](../APIReference/API_BatchGetAssetPropertyValue.md "../APIReference/API_BatchGetAssetPropertyValue.md")<br>• [BatchGetAssetPropertyValueHistory](../APIReference/API_BatchGetAssetPropertyValueHistory.md "../APIReference/API_BatchGetAssetPropertyValueHistory.md")<br>• [BatchGetAssetPropertyAggregates](../APIReference/API_BatchGetAssetPropertyAggregates.md "../APIReference/API_BatchGetAssetPropertyAggregates.md") |
| **AWS IoT SiteWise Assistant**   | `AWS::SitewiseAssistant::Conversation` | • [InvokeAssistant](../APIReference/API_InvokeAssistant.md "../APIReference/API_InvokeAssistant.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

###### Note

The resources.type logged in the Cloudtrail event depends on the identifier used in the
API request. If an asset id is specified in the request then the Asset resources.type is
logged, else the TimeSeries resources.type is logged.

\*You can configure advanced event selectors to filter on the `eventName`,
`readOnly`, and `resources.ARN` fields to log only those events that
are important to you. For more information about these fields, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md").

## AWS IoT SiteWise management events in

CloudTrail

[Logging
management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md") provide information about management operations that are performed
on resources in your AWS account. These are also known as control plane operations. By
default, CloudTrail logs management events.

AWS IoT SiteWise logs all AWS IoT SiteWise control plane operations as management events. For a list
of the AWS IoT SiteWise control plane operations that AWS IoT SiteWise logs to CloudTrail, see the [AWS IoT SiteWise API Reference](../APIReference/API_Operations.md "../APIReference/API_Operations.md").

## Example: AWS IoT SiteWise log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested operation, the date and
time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack
trace of the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the
`CreateAsset` operation.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE",
    "arn": "arn:aws:iam::123456789012:user/Administrator",
    "accountId": "123456789012",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "userName": "Administrator",
    "sessionContext": {
      "sessionIssuer": {},
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2020-03-11T17:26:40Z"
      }
    },
    "invokedBy": "signin.amazonaws.com"
  },
  "eventTime": "2020-03-11T18:01:22Z",
  "eventSource": "iotsitewise.amazonaws.com",
  "eventName": "CreateAsset",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "203.0.113.0",
  "userAgent": "signin.amazonaws.com",
  "requestParameters": {
    "assetName": "Wind Turbine 1",
    "assetModelId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-00000EXAMPLE"
  },
  "responseElements": {
    "assetId": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
    "assetArn": "arn:aws:iotsitewise:us-east-1:123456789012:asset/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
    "assetStatus": {
      "state": "CREATING"
    }
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE",
  "eventID": "a1b2c3d4-5678-90ab-cdef-bbbbbEXAMPLE",
  "eventType": "AwsApiCall",
  "recipientAccountId": "123456789012"
}
```
