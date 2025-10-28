# Logging Amazon Polly API calls with AWS CloudTrail

Amazon Polly is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, role, or an AWS service in Amazon Polly. CloudTrail captures all API calls for Amazon Polly as events.
The calls captured include calls from the Amazon Polly console and code calls to the Amazon Polly API
operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an
Amazon S3 bucket, including events for Amazon Polly. If you don't configure a trail, you can still view
the most recent events in the CloudTrail console in **Event history**. Using the
information collected by CloudTrail, you can determine the request that was made to Amazon Polly, the IP
address from which the request was made, who made the request, when it was made, and
additional details.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Amazon Polly information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported event
activity occurs in Amazon Polly, that activity is recorded in a CloudTrail event along with other
AWS service events in **Event history**. You can view, search, and download
recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon Polly,
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

Amazon Polly supports logging the following actions as events in CloudTrail log files:

- [DeleteLexicon](API_DeleteLexicon.md "API_DeleteLexicon.md")
- [DescribeVoices](API_DescribeVoices.md "API_DescribeVoices.md")
- [GetLexicon](API_GetLexicon.md "API_GetLexicon.md")
- [GetSpeechSynthesisTask](API_GetSpeechSynthesisTask.md "API_GetSpeechSynthesisTask.md")
- [ListLexicons](API_ListLexicons.md "API_ListLexicons.md")
- [ListSpeechSynthesisTasks](API_ListSpeechSynthesisTasks.md "API_ListSpeechSynthesisTasks.md")
- [PutLexicon](API_PutLexicon.md "API_PutLexicon.md")
- [StartSpeechSynthesisTask](API_StartSpeechSynthesisTask.md "API_StartSpeechSynthesisTask.md")
- [SynthesizeSpeech](API_SynthesizeSpeech.md "API_SynthesizeSpeech.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root user or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Example: Amazon Polly Log File Entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `SynthesizeSpeech`.

```
{
"Records": [
        {
"awsRegion": "us-east-2",
            "eventID": "19bd70f7-5e60-4cdc-9825-936c552278ae",
            "eventName": "SynthesizeSpeech",
            "eventSource": "polly.amazonaws.com",
            "eventTime": "2016-11-02T03:49:39Z",
            "eventType": "AwsApiCall",
            "eventVersion": "1.05",
            "recipientAccountId": "123456789012",
            "requestID": "414288c2-a1af-11e6-b17f-d7cfc06cb461",
            "requestParameters": {
"lexiconNames": [
                    "SampleLexicon"
                ],
                "engine": "neural",
                "outputFormat": "mp3",
                "sampleRate": "22050",
                "text": "**********",
                "textType": "text",
                "voiceId": "Kendra"
            },
            "responseElements": null,
            "sourceIPAddress": "1.2.3.4",
            "userAgent": "Amazon CLI/Polly 1.10 API 2016-06-10",
            "userIdentity": {
"accessKeyId": "EXAMPLE_KEY_ID",
                "accountId": "123456789012",
                "arn": "arn:aws:iam::123456789012:user/Alice",
                "principalId": "EX_PRINCIPAL_ID",
                "type": "IAMUser",
                "userName": "Alice"
            }
        }

    ]
}
```
