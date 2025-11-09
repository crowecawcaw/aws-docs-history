# Logging AWS Lambda API calls using

AWS CloudTrail

AWS Lambda is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a service
that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures API
calls for Lambda as events. The calls captured include calls from the Lambda console and
code calls to the Lambda API operations. Using the information collected by CloudTrail, you can
determine the request that was made to Lambda, the IP address from which the request was
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

## Lambda data events in CloudTrail

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") provide information about the resource operations performed on or in a
resource (for example, reading or writing to an Amazon S3
object). These are also known as data
plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log
most data events, and the CloudTrail **Event history** doesn't record them.

One CloudTrail data event that is logged by default for supported services is `LambdaESMDisabled`.
To learn more about using this event to help troubleshoot issues with Lambda event source mappings, see
[Using CloudTrail to troubleshoot disabled Lambda event sources](#cloudtrail-ESM-troubleshooting "#cloudtrail-ESM-troubleshooting").

Additional charges apply for data events. For more information about CloudTrail pricing, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

You can log data events for the `AWS::Lambda::Function` resource type by using
the CloudTrail console, AWS CLI, or CloudTrail API operations. For more information about how to log data
events, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") and [Logging data events with the AWS Command Line Interface](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI") in the
_AWS CloudTrail User Guide_.

The following table lists the Lambda resource type for which you can log data events.
The **Data event type (console)** column shows the value to
choose from the **Data event type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type`
value, which you would specify when configuring advanced event selectors using the AWS CLI or
CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API
calls logged to CloudTrail for the resource type.

| Data event type (console) | resources.type value    | Data APIs logged to CloudTrail                        |
| ------------------------- | ----------------------- | ----------------------------------------------------- |
| **Lambda**                | `AWS::Lambda::Function` | [Invoke](../api/API_Invoke.md "../api/API_Invoke.md") |

You can configure advanced event selectors to filter on the `eventName`,
`readOnly`, and `resources.ARN` fields to log only those events that
are important to you. The following example is the JSON view of a data event configuration
that logs events for a specific function only. For more information about these fields, see
[AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") in the
_AWS CloudTrail API Reference_.

```
[
  {
    "name": "function-invokes",
    "fieldSelectors": [
      {
        "field": "eventCategory",
        "equals": [
          "Data"
        ]
      },
      {
        "field": "resources.type",
        "equals": [
          "AWS::Lambda::Function"
        ]
      },
      {
        "field": "resources.ARN",
        "equals": [
          "`arn:aws:lambda:us-east-1:111122223333:function:hello-world`"
        ]
      }
    ]
  }
]
```

## Lambda management events in CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

Lambda supports logging the following actions as management events in CloudTrail log
files.

###### Note

In the CloudTrail log file, the `eventName` might include date and version
information, but it is still referring to the same public API action. For example the,
`GetFunction` action appears as `GetFunction20150331v2`. The
following list specifies when the event name differs from the API action name.

- [AddLayerVersionPermission](../api/API_AddLayerVersionPermission.md "../api/API_AddLayerVersionPermission.md")
- [AddPermission](../api/API_AddPermission.md "../api/API_AddPermission.md") (event name: `AddPermission20150331v2`)
- [CreateAlias](../api/API_CreateAlias.md "../api/API_CreateAlias.md") (event name: `CreateAlias20150331`)
- [CreateEventSourceMapping](../api/API_CreateEventSourceMapping.md "../api/API_CreateEventSourceMapping.md") (event name:
  `CreateEventSourceMapping20150331`)
- [CreateFunction](../api/API_CreateFunction.md "../api/API_CreateFunction.md") (event name: `CreateFunction20150331`)

(The `Environment` and `ZipFile` parameters are omitted from the
CloudTrail logs for `CreateFunction`.)

- [CreateFunctionUrlConfig](../api/API_CreateFunctionUrlConfig.md "../api/API_CreateFunctionUrlConfig.md")
- [DeleteAlias](../api/API_DeleteAlias.md "../api/API_DeleteAlias.md") (event name: `DeleteAlias20150331`)
- [DeleteCodeSigningConfig](../api/API_DeleteCodeSigningConfig.md "../api/API_DeleteCodeSigningConfig.md")
- [DeleteEventSourceMapping](../api/API_DeleteEventSourceMapping.md "../api/API_DeleteEventSourceMapping.md") (event name:
  `DeleteEventSourceMapping20150331`)
- [DeleteFunction](../api/API_DeleteFunction.md "../api/API_DeleteFunction.md") (event name: `DeleteFunction20150331`)
- [DeleteFunctionConcurrency](../api/API_DeleteFunctionConcurrency.md "../api/API_DeleteFunctionConcurrency.md") (event name:
  `DeleteFunctionConcurrency20171031`)
- [DeleteFunctionUrlConfig](../api/API_DeleteFunctionUrlConfig.md "../api/API_DeleteFunctionUrlConfig.md")
- [DeleteProvisionedConcurrencyConfig](../api/API_DeleteProvisionedConcurrencyConfig.md "../api/API_DeleteProvisionedConcurrencyConfig.md")
- [GetAlias](../api/API_GetAlias.md "../api/API_GetAlias.md") (event name: `GetAlias20150331`)
- [GetEventSourceMapping](../api/API_GetEventSourceMapping.md "../api/API_GetEventSourceMapping.md")
- [GetFunction](../api/API_GetFunction.md "../api/API_GetFunction.md")
- [GetFunctionUrlConfig](../api/API_GetFunctionUrlConfig.md "../api/API_GetFunctionUrlConfig.md")
- [GetFunctionConfiguration](../api/API_GetFunctionConfiguration.md "../api/API_GetFunctionConfiguration.md")
- [GetLayerVersionPolicy](../api/API_GetLayerVersionPolicy.md "../api/API_GetLayerVersionPolicy.md")
- [GetPolicy](../api/API_GetPolicy.md "../api/API_GetPolicy.md")
- [ListEventSourceMappings](../api/API_ListEventSourceMappings.md "../api/API_ListEventSourceMappings.md")
- [ListFunctions](../api/API_ListFunctions.md "../api/API_ListFunctions.md")
- [ListFunctionUrlConfigs](../api/API_ListFunctionUrlConfigs.md "../api/API_ListFunctionUrlConfigs.md")
- [PublishLayerVersion](../api/API_PublishLayerVersion.md "../api/API_PublishLayerVersion.md") (event name:
  `PublishLayerVersion20181031`)

(The `ZipFile` parameter is omitted from the CloudTrail logs for
`PublishLayerVersion`.)

- [PublishVersion](../api/API_PublishVersion.md "../api/API_PublishVersion.md") (event name: `PublishVersion20150331`)
- [PutFunctionConcurrency](../api/API_PutFunctionConcurrency.md "../api/API_PutFunctionConcurrency.md") (event name:
  `PutFunctionConcurrency20171031`)
- [PutFunctionCodeSigningConfig](../api/API_PutFunctionCodeSigningConfig.md "../api/API_PutFunctionCodeSigningConfig.md")
- [PutFunctionEventInvokeConfig](../api/API_PutFunctionEventInvokeConfig.md "../api/API_PutFunctionEventInvokeConfig.md")
- [PutProvisionedConcurrencyConfig](../api/API_PutProvisionedConcurrencyConfig.md "../api/API_PutProvisionedConcurrencyConfig.md")
- [PutRuntimeManagementConfig](../api/API_PutRuntimeManagementConfig.md "../api/API_PutRuntimeManagementConfig.md")
- [RemovePermission](../api/API_RemovePermission.md "../api/API_RemovePermission.md") (event name: `RemovePermission20150331v2`)
- [TagResource](../api/API_TagResource.md "../api/API_TagResource.md") (event name: `TagResource20170331v2`)
- [UntagResource](../api/API_UntagResource.md "../api/API_UntagResource.md") (event name: `UntagResource20170331v2`)
- [UpdateAlias](../api/API_UpdateAlias.md "../api/API_UpdateAlias.md") (event name: `UpdateAlias20150331`)
- [UpdateCodeSigningConfig](../api/API_UpdateCodeSigningConfig.md "../api/API_UpdateCodeSigningConfig.md")
- [UpdateEventSourceMapping](../api/API_UpdateEventSourceMapping.md "../api/API_UpdateEventSourceMapping.md") (event name:
  `UpdateEventSourceMapping20150331`)
- [UpdateFunctionCode](../api/API_UpdateFunctionCode.md "../api/API_UpdateFunctionCode.md") (event name:
  `UpdateFunctionCode20150331v2`)

(The `ZipFile` parameter is omitted from the CloudTrail logs for
`UpdateFunctionCode`.)

- [UpdateFunctionConfiguration](../api/API_UpdateFunctionConfiguration.md "../api/API_UpdateFunctionConfiguration.md") (event name:
  `UpdateFunctionConfiguration20150331v2`)

(The `Environment` parameter is omitted from the CloudTrail logs for
`UpdateFunctionConfiguration`.)

- [UpdateFunctionEventInvokeConfig](../api/API_UpdateFunctionEventInvokeConfig.md "../api/API_UpdateFunctionEventInvokeConfig.md")
- [UpdateFunctionUrlConfig](../api/API_UpdateFunctionUrlConfig.md "../api/API_UpdateFunctionUrlConfig.md")

## Using CloudTrail to troubleshoot disabled Lambda event sources

When you change the state of an event source mapping using the [UpdateEventSourceMapping](../api/API_UpdateEventSourceMapping.md "../api/API_UpdateEventSourceMapping.md") API action, the
API call is logged as a management event in CloudTrail. Event source mappings can also transition directly to the `Disabled`
state due to errors.

For the following services, Lambda publishes the `LambdaESMDisabled` data event to CloudTrail when your event source
transitions to the Disabled state:

- Amazon Simple Queue Service (Amazon SQS)
- Amazon DynamoDB
- Amazon Kinesis

Lambda doesn't support this event for any other event source mapping types.

To receive alerts when event source mappings for supported services transition to the `Disabled` state,
set up an alarm in Amazon CloudWatch using the `LambdaESMDisabled` CloudTrail event. To learn more about setting up a CloudWatch
alarm, see [Creating CloudWatch alarms for
CloudTrail events: examples](../../../awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.md").

The `serviceEventDetails` entity in the `LambdaESMDisabled` event message contains one of the following
error codes.

**`RESOURCE_NOT_FOUND`**

The resource specified in the request does not exist.

**`FUNCTION_NOT_FOUND`**

The function attached to the event source does not exist.

**`REGION_NAME_NOT_VALID`**

A Region name provided to the event source or function is invalid.

**`AUTHORIZATION_ERROR`**

Permissions have not been set, or are misconfigured.

**`FUNCTION_IN_FAILED_STATE`**

The function code does not compile, has encountered an unrecoverable exception, or a bad deployment has occurred.

## Lambda event examples

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows CloudTrail log entries for the `GetFunction` and `DeleteFunction`
actions.

###### Note

The `eventName` might include date and version information, such as
`"GetFunction20150331"`, but it is still referring to the same public API.

```
{
  "Records": [
    {
      "eventVersion": "1.03",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "A1B2C3D4E5F6G7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/myUserName",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "myUserName"
      },
      "eventTime": "2015-03-18T19:03:36Z",
      "eventSource": "lambda.amazonaws.com",
      "eventName": "GetFunction",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "127.0.0.1",
      "userAgent": "Python-httplib2/0.8 (gzip)",
      "errorCode": "AccessDenied",
      "errorMessage": "User: arn:aws:iam::111122223333:user/myUserName is not authorized to perform: lambda:GetFunction on resource: arn:aws:lambda:us-west-2:111122223333:function:other-acct-function",
      "requestParameters": null,
      "responseElements": null,
      "requestID": "7aebcd0f-cda1-11e4-aaa2-e356da31e4ff",
      "eventID": "e92a3e85-8ecd-4d23-8074-843aabfe89bf",
      "eventType": "AwsApiCall",
      "recipientAccountId": "111122223333"
    },
    {
      "eventVersion": "1.03",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "A1B2C3D4E5F6G7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/myUserName",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "myUserName"
      },
      "eventTime": "2015-03-18T19:04:42Z",
      "eventSource": "lambda.amazonaws.com",
      "eventName": "DeleteFunction20150331",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "127.0.0.1",
      "userAgent": "Python-httplib2/0.8 (gzip)",
      "requestParameters": {
        "functionName": "basic-node-task"
      },
      "responseElements": null,
      "requestID": "a2198ecc-cda1-11e4-aaa2-e356da31e4ff",
      "eventID": "20b84ce5-730f-482e-b2b2-e8fcc87ceb22",
      "eventType": "AwsApiCall",
      "recipientAccountId": "111122223333"
    }
  ]
}
```

For information about CloudTrail record contents, see [CloudTrail
record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the _AWS CloudTrail User Guide_.
