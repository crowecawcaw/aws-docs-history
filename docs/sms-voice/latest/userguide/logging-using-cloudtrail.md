# Logging AWS End User Messaging SMS API calls using

AWS CloudTrail

AWS End User Messaging SMS is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a service that provides a record of actions taken by a user, role, or an
AWS service. CloudTrail captures all
API calls for AWS End User Messaging SMS as events. The calls captured include calls from the AWS End User Messaging SMS console
and code calls to the AWS End User Messaging SMS API operations. Using the information collected by CloudTrail, you can
determine the request that was made to AWS End User Messaging SMS, the IP address from which the request was
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

## AWS End User Messaging SMS data events in CloudTrail

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") provide information about the resource operations performed on or in a
resource (for example, reading or writing to an Amazon S3
object). These are also known as data
plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log
data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

You can log data events for the AWS End User Messaging SMS resource types by using the CloudTrail console, AWS CLI,
or CloudTrail API operations. For more information about how to log data events, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") and [Logging data events with the AWS Command Line Interface](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI") in the
_AWS CloudTrail User Guide_.

The following table lists the AWS End User Messaging SMS resource types for which you can log data events.
The **Data event type (console)** column shows the value to
choose from the **Data event type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type`
value, which you would specify when configuring advanced event selectors using the AWS CLI or
CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API
calls logged to CloudTrail for the resource type.

| Data event type (console)          | resources.type value                 | Data APIs logged to CloudTrail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **SMS Voice origination identity** | `AWS::SMSVoice::OriginationIdentity` | • [SendTextMessage](../../../pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.md "../../../pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.md")<br>• [SendVoiceMessage](../../../pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.md "../../../pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.md")<br>• [SendMediaMessage](../../../pinpoint/latest/apireference_smsvoicev2/API_SendMediaMessage.md "../../../pinpoint/latest/apireference_smsvoicev2/API_SendMediaMessage.md") |

You can configure advanced event selectors to filter on the `eventName`,
`readOnly`, and `resources.ARN` fields to log only those events that
are important to you. For more information about these fields, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") in the
_AWS CloudTrail API Reference_.

## AWS End User Messaging SMS management events in CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

AWS End User Messaging SMS logs all AWS End User Messaging SMS control plane operations as management events. For a list
of the AWS End User Messaging SMS control plane operations that AWS End User Messaging SMS logs to CloudTrail, see the
[AWS End User Messaging SMS and Voice V2 API Reference](../../../pinpoint/latest/apireference_smsvoicev2/Welcome.md "../../../pinpoint/latest/apireference_smsvoicev2/Welcome.md").

## AWS End User Messaging SMS event examples

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `CreateConfigurationSet` and `CreateEventDestination` actions.

```
{
  "Records": [
    {
      "eventVersion":"1.05",
      "userIdentity":{
        "type":"IAMUser",
        "principalId":"AIDAIHTHRCDA62EXAMPLE",
        "arn":"arn:aws:iam::111122223333:user/SampleUser",
        "accountId":"111122223333",
        "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
        "userName":"SampleUser"
      },
      "eventTime":"2018-11-06T21:45:55Z",
      "eventSource":"sms-voice.amazonaws.com",
      "eventName":"CreateConfigurationSet",
      "awsRegion":"us-east-1",
      "sourceIPAddress":"192.0.0.1",
      "userAgent":"PostmanRuntime/7.3.0",
      "requestParameters":{
        "ConfigurationSetName":"MyConfigurationSet"
      },
      "responseElements":null,
      "requestID":"56dcc091-e20d-11e8-87d2-9994aexample",
      "eventID":"725843fc-8846-41f4-871a-7c52dexample",
      "readOnly":false,
      "eventType":"AwsApiCall",
      "recipientAccountId":"123456789012"
    },
    {
      "eventVersion":"1.05",
      "userIdentity":{
        "type":"IAMUser",
        "principalId":"AIDAIHTHRCDA62EXAMPLE",
        "arn":"arn:aws:iam::111122223333:user/SampleUser",
        "accountId":"111122223333",
        "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
        "userName":"SampleUser"
      },
      "eventTime":"2018-11-06T21:47:08Z",
      "eventSource":"sms-voice.amazonaws.com",
      "eventName":"CreateEventDestination",
      "awsRegion":"us-east-1",
      "sourceIPAddress":"192.0.0.1",
      "userAgent":"PostmanRuntime/7.3.0",
      "requestParameters":{
        "EventDestinationName":"CloudWatchEventDestination",
        "ConfigurationSetName":"MyConfigurationSet",
        "EventDestination":{
          "Enabled":true,
          "MatchingEventTypes":[
            "INITIATED_CALL",
            "INITIATED_CALL"
          ],
          "CloudWatchLogsDestination":{
            "IamRoleArn":"arn:aws:iam::111122223333:role/iamrole-01",
            "LogGroupArn":"arn:aws:logs:us-east-1:111122223333:log-group:clientloggroup-01"
          }
        }
      },
      "responseElements":null,
      "requestID":"81de1e73-e20d-11e8-b158-d5536example",
      "eventID":"fcafc21f-7c93-4a3f-9e72-fca2dexample",
      "readOnly":false,
      "eventType":"AwsApiCall",
      "recipientAccountId":"111122223333"
    }
  ]
}
```

The following example shows a CloudTrail log entry that demonstrates the `SendTextMessage` action.

```
{
        "eventVersion": "1.10",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "QWERTYUIOPASDFGHJKLZXCVBNM:EXAMPLE",
            "arn": "arn:aws:sts::111122223333:assumed-role/ASDFGHJKL/QWERTYUIOP",
            "accountId": "111122223333",
            "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "sessionContext": {
                "sessionIssuer": {
                    "type": "Role",
                    "principalId": "ASDFGHJKLQWERTYUIOP",
                    "arn": "arn:aws:iam::123456789123:role/QWERTYUIOP",
                    "accountId": "111122223333",
                    "userName": "QWERTYUIOP"
                },
                "attributes": {
                    "creationDate": "2024-10-02T22:39:11Z",
                    "mfaAuthenticated": "false"
                }
            }
        },
        "eventTime": "2024-10-02T23:52:08Z",
        "eventSource": "sms-voice.amazonaws.com",
        "eventName": "SendTextMessage",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "192.0.2.1",
        "userAgent": "aws-cli/1.18.147 Python/2.7.18 Linux/5.10.218-186.862.amzn2int.x86_64 botocore/1.18.6",
        "requestParameters": {
            "destinationPhoneNumber": "+11235550123",
            "originationIdentity": "phone-aa012345678901234567890123456789",
            "messageBody": "HIDDEN_DUE_TO_SECURITY_REASONS",
        },
        "responseElements": {
            "messageId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        },
        "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
        "readOnly": false,
        "resources": [{
            "accountId": "111122223333",
            "type": "AWS::SMSVoice::OriginationIdentity",
            "ARN": "arn:aws:sms-voice:us-east-1:111122223333:phone-number/phone-aa012345678901234567890123456789"
        }],
        "eventType": "AwsApiCall",
        "managementEvent": false,
        "recipientAccountId": "111122223333",
        "eventCategory": "Data",
        "tlsDetails": {
            "clientProvidedHostHeader": "sms-voice.us-east-1.amazonaws.com"
        }
}
```

The following example shows a CloudTrail log entry that demonstrates the `SendVoiceMessage` action.

```
{
        "eventVersion": "1.10",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "QWERTYUIOPASDFGHJKLZXCVBNM:EXAMPLE",
            "arn": "arn:aws:sts::111122223333:assumed-role/ASDFGHJKL/QWERTYUIOP",
            "accountId": "111122223333",
            "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "sessionContext": {
                "sessionIssuer": {
                    "type": "Role",
                    "principalId": "ASDFGHJKLQWERTYUIOP",
                    "arn": "arn:aws:iam::123456789123:role/QWERTYUIOP",
                    "accountId": "111122223333",
                    "userName": "QWERTYUIOP"
                },
                "attributes": {
                    "creationDate": "2024-10-02T22:39:11Z",
                    "mfaAuthenticated": "false"
                }
            }
        },
        "eventTime": "2024-10-02T23:52:08Z",
        "eventSource": "sms-voice.amazonaws.com",
        "eventName": "SendVoiceMessage",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "192.0.2.1",
        "userAgent": "aws-cli/1.18.147 Python/2.7.18 Linux/5.10.218-186.862.amzn2int.x86_64 botocore/1.18.6",
        "requestParameters": {
            "destinationPhoneNumber": "+11235550123",
            "originationIdentity": "phone-aa012345678901234567890123456789",
            "messageBody": "HIDDEN_DUE_TO_SECURITY_REASONS",
        },
        "responseElements": {
            "messageId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa"
        },
        "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
        "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "readOnly": false,
        "resources": [{
            "accountId": "111122223333",
            "type": "AWS::SMSVoice::OriginationIdentity",
            "ARN": "arn:aws:sms-voice:us-east-1:111122223333:phone-number/phone-aa012345678901234567890123456789"
        }],
        "eventType": "AwsApiCall",
        "managementEvent": false,
        "recipientAccountId": "111122223333",
        "eventCategory": "Data",
        "tlsDetails": {
            "clientProvidedHostHeader": "sms-voice.us-east-1.amazonaws.com"
        }
}
```

The following example shows a CloudTrail log entry that demonstrates the `SendMediaMessage` action.

```
{
        "eventVersion": "1.10",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "QWERTYUIOPASDFGHJKLZXCVBNM:EXAMPLE",
            "arn": "arn:aws:sts::111122223333:assumed-role/ASDFGHJKL/QWERTYUIOP",
            "accountId": "111122223333",
            "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "sessionContext": {
                "sessionIssuer": {
                    "type": "Role",
                    "principalId": "ASDFGHJKLQWERTYUIOP",
                    "arn": "arn:aws:iam::377392627227:role/QWERTYUIOP",
                    "accountId": "111122223333",
                    "userName": "QWERTYUIOP"
                },
                "attributes": {
                    "creationDate": "2024-10-02T22:39:11Z",
                    "mfaAuthenticated": "false"
                }
            }
        },
        "eventTime": "2024-10-02T23:52:08Z",
        "eventSource": "sms-voice.amazonaws.com",
        "eventName": "SendMediaMessage",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "192.0.2.1",
        "userAgent": "aws-cli/1.18.147 Python/2.7.18 Linux/5.10.218-186.862.amzn2int.x86_64 botocore/1.18.6",
        "requestParameters": {
            "destinationPhoneNumber": "+11235550123",
            "originationIdentity": "phone-aa012345678901234567890123456789",
            "messageBody": "HIDDEN_DUE_TO_SECURITY_REASONS",
        },
        "responseElements": {
            "messageId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        },
        "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
        "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
        "readOnly": false,
        "resources": [{
            "accountId": "111122223333",
            "type": "AWS::SMSVoice::OriginationIdentity",
            "ARN": "arn:aws:sms-voice:us-east-1:111122223333:phone-number/phone-aa012345678901234567890123456789"
        }],
        "eventType": "AwsApiCall",
        "managementEvent": false,
        "recipientAccountId": "111122223333",
        "eventCategory": "Data",
        "tlsDetails": {
            "clientProvidedHostHeader": "sms-voice.us-east-1.amazonaws.com"
        }
}
```

For information about CloudTrail record contents, see [CloudTrail
record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the _AWS CloudTrail User Guide_.
