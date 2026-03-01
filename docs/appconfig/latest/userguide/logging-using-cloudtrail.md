# Logging AWS AppConfig API calls using AWS CloudTrail

AWS AppConfig is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a service
that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all
API calls for AWS AppConfig as events. The calls captured include calls from the AWS AppConfig console
and code calls to the AWS AppConfig API operations. Using the information collected by CloudTrail, you can
determine the request that was made to AWS AppConfig, the IP address from which the request was
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

## AWS AppConfig data events in CloudTrail

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") provide information about the resource operations performed on or in a
resource (for example, retrieving the latest deployed configuration by calling
GetLatestConfiguration). These are also known as data plane operations. Data events are often
high-volume activities. By default, CloudTrail doesn’t log data events. The CloudTrail **Event
history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

You can log data events for the AWS AppConfig resource types by using the CloudTrail console, AWS CLI,
or CloudTrail API operations. The [table](#data-events-table "#data-events-table") in this section
shows the resource types available for AWS AppConfig.

- To log data events using the CloudTrail console, create a [trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console") or [event data
  store](../../../awscloudtrail/latest/userguide/query-event-data-store-cloudtrail.md "../../../awscloudtrail/latest/userguide/query-event-data-store-cloudtrail.md") to log data events, or [update an existing trail or event data store](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") to log data events.
  1.  Choose **Data events** to log data events.
  2.  From the **Data event type** list, choose
      **AWS AppConfig**.
  3.  Choose the log selector template you want to use. You can log all data events for
      the resource type, log all `readOnly` events, log all
      `writeOnly` events, or create a custom log selector template to filter on
      the `readOnly`, `eventName`, and `resources.ARN`
      fields.
  4.  For **Selector name**, enter
      **AppConfigDataEvents**. For information about enabling Amazon CloudWatch Logs
      for your data event trail, see [Logging metrics for AWS AppConfig data plane calls](monitoring-data-plane-call-logging.md "monitoring-data-plane-call-logging.md").

- To log data events using the AWS CLI, configure the
  `--advanced-event-selectors` parameter to set the `eventCategory`
  field equal to `Data` and the `resources.type` field equal to the
  resource type value (see [table](#data-events-table "#data-events-table")). You can add
  conditions to filter on the values of the `readOnly`, `eventName`,
  and `resources.ARN` fields.
  - To configure a trail to log data events, run the [put-event-selectors](../../../cli/latest/reference/cloudtrail/put-event-selectors.md "../../../cli/latest/reference/cloudtrail/put-event-selectors.md") command. For more information, see
    [Logging data events for trails with the AWS CLI](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-CLI-trail-examples "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-CLI-trail-examples").
  - To configure an event data store to log data events, run the [create-event-data-store](../../../cli/latest/reference/cloudtrail/create-event-data-store.md "../../../cli/latest/reference/cloudtrail/create-event-data-store.md") command to create a new event data
    store to log data events, or run the [update-event-data-store](../../../cli/latest/reference/cloudtrail/update-event-data-store.md "../../../cli/latest/reference/cloudtrail/update-event-data-store.md") command to update an existing
    event data store. For more information, see [Logging data events for event data stores with the AWS CLI](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-CLI-eds-examples "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-CLI-eds-examples").

The following table lists the AWS AppConfig resource types. The **Data
event type (console)** column shows the value to choose from the **Data
event type** list on the CloudTrail console. The **resources.type
value** column shows the `resources.type` value, which you would specify
when configuring advanced event selectors using the AWS CLI or CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API calls logged to CloudTrail
for the resource type.

| Data event type (console) | resources.type value            | Data APIs logged to CloudTrail\*                                                                                                                                                                                                                                                                                                                                                |
| ------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AWS AppConfig**         | `AWS::AppConfig::Configuration` | • [GetLatestConfiguration](../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md "../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md")<br>• [StartConfigurationSession](../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md "../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md") |

\*You can configure advanced event selectors to filter on the `eventName`,
`readOnly`, and `resources.ARN` fields to log only those events that
are important to you. For more information about these fields, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md").

## AWS AppConfig management events in CloudTrail

AWS AppConfig logs all AWS AppConfig control plane operations as management events. For a list
of the AWS AppConfig control plane operations that AWS AppConfig logs to CloudTrail, see the
[AWS AppConfig API Reference](../../2019-10-09/APIReference/Welcome.md "../../2019-10-09/APIReference/Welcome.md").

## AWS AppConfig event examples

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail event that demonstrates the [StartConfigurationSession](../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md "../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md") operation.

```
{
      "eventVersion": "1.09",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::123456789012:user/Administrator",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
          "sessionIssuer": {},
          "attributes": {
            "creationDate": "2024-01-11T14:37:02Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2024-01-11T14:45:15Z",
      "eventSource": "appconfig.amazonaws.com",
      "eventName": "StartConfigurationSession",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "203.0.113.0",
      "userAgent": "Boto3/1.34.11 md/Botocore#1.34.11 ua/2.0 os/macos#22.6.0 md/arch#x86_64 lang/python#3.11.4 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.34.11",
      "requestParameters": {
        "applicationIdentifier": "rrfexample",
        "environmentIdentifier": "mexampleqe0",
        "configurationProfileIdentifier": "3eexampleu1"
      },
      "responseElements": null,
      "requestID": "a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE",
      "eventID": "a1b2c3d4-5678-90ab-cdef-bbbbbEXAMPLE",
      "readOnly": false,
      "resources": [
        {
          "accountId": "123456789012",
          "type": "AWS::AppConfig::Configuration",
          "ARN": "arn:aws:appconfig:us-east-1:123456789012:application/rrfexample/environment/mexampleqe0/configuration/3eexampleu1"
        }
      ],
      "eventType": "AwsApiCall",
      "managementEvent": false,
      "recipientAccountId": "123456789012",
      "eventCategory": "Data",
      "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "appconfigdata.us-east-1.amazonaws.com"
      }
    }
```

For information about CloudTrail record contents, see [CloudTrail
record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the _AWS CloudTrail User Guide_.
