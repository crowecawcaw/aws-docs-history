# Monitoring Amazon Transcribe

with AWS CloudTrail

Amazon Transcribe is integrated with AWS CloudTrail, a service that provides a
record of actions taken in Amazon Transcribe by an AWS Identity and Access Management (IAM)
user or role, or by an AWS service. CloudTrail captures all API calls for
Amazon Transcribe. That includes calls from the AWS Management Console and code calls to the
Amazon Transcribe APIs, as events. By creating a trail, you can enable continuous delivery of
CloudTrail events, including events for Amazon Transcribe, to an Amazon S3
bucket. If you don't create a trail, you can still view the most recent events in the CloudTrail
AWS Management Console in **Event history**. Using the information collected by
CloudTrail, you can see each request that is made to Amazon Transcribe, the IP address
from which the request is made, who made the request, when it is made, and additional
details.

To learn more about CloudTrail, refer to the [_AWS CloudTrail User Guide_](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Amazon Transcribe and CloudTrail

CloudTrail is enabled on your AWS account when you create
the account. When activity occurs in Amazon Transcribe, that activity is recorded in a
CloudTrail event along with other AWS service events in the
CloudTrail **Event history**. You can view, search, and
download recent events in your AWS account. For more information, see
[Viewing Events with
CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

To get an ongoing record of events in your AWS account, including
events for Amazon Transcribe, create a trail. A _trail_
is a configuration that enables CloudTrail to deliver events as log files to a specified
Amazon S3 bucket. CloudTrail log files contain one or more log entries. An
_event_ represents a single request from any source. It
includes information about the requested action, the date and time of the action, request
parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public
API calls, so they don't appear in any specific order.

By default, when you create a trail in the AWS Management Console, the trail applies to all
AWS Regions. The trail logs events from all AWS Regions in the
AWS partition and delivers the log files to the Amazon S3 bucket that you
specify. Additionally, you can configure other AWS services to further analyze and
act upon the event data collected in CloudTrail logs. For more information, see:

- [Overview for
  Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving
  CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving
  CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

CloudTrail logs all Amazon Transcribe actions, which are documented in the
[API Reference](../APIReference/API_Reference.md "../APIReference/API_Reference.md").
For example, the [`CreateVocabulary`](../APIReference/API_CreateVocabulary.md "../APIReference/API_CreateVocabulary.md"),
[`GetTranscriptionJob`](../APIReference/API_GetTranscriptionJob.md "../APIReference/API_GetTranscriptionJob.md"), and
[`StartTranscriptionJob`](../APIReference/API_StartTranscriptionJob.md "../APIReference/API_StartTranscriptionJob.md")
operations generate entries in the CloudTrail log files.
When CloudTrail logs Amazon Transcribe API operations, the CloudTrail log entry uses empty strings for sensitive information in the request and response parameters, such as Amazon S3 URI values.

Every event or log entry contains information about who generated the request. This
information helps you determine the following:

- Whether the request is made with root or IAM user credentials
- Whether the request is made with temporary security credentials for an IAM
  role or federated user
- Whether the request is made by another AWS service

For more information, see the [CloudTrail
userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

You can also aggregate Amazon Transcribe log files from multiple AWS Regions and multiple
AWS accounts into a single Amazon S3 bucket. For more information, see [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving
CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md").

### Example: Amazon Transcribe log file entries

A _trail_ is a configuration that enables delivery of
events as log files to a specified Amazon S3 bucket. CloudTrail log files
contain one or more log entries. An _event_ represents a
single request from any source. It includes such information about the requested action as
the date and time of the action, and request parameters. CloudTrail log files aren't
an ordered stack trace of the public API calls, so they don't appear in any specific order.

Calls to the [`StartTranscriptionJob`](../APIReference/API_StartTranscriptionJob.md "../APIReference/API_StartTranscriptionJob.md") and
[`GetTranscriptionJob`](../APIReference/API_GetTranscriptionJob.md "../APIReference/API_GetTranscriptionJob.md") API operations
create the following entry.

###### Note

When CloudTrail logs Amazon Transcribe API operations, the CloudTrail log entry uses empty strings for sensitive information in the request and response parameters, such as Amazon S3 URI values.

```
{
    "Records": [
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "`IAMUser`",
                "principalId": "`111122223333`",
                "arn": "`arn:aws:iam:us-west-2:111122223333:user/my-user-name`",
                "accountId": "`111122223333`",
                "accessKeyId": "`AKIAIOSFODNN7EXAMPLE`",
                "userName": "`my-user-name`"
            },
            "eventTime": "`2022-03-07T15:03:45Z`",
            "eventSource": "transcribe.amazonaws.com",
            "eventName": "StartTranscriptionJob",
            "awsRegion": "`us-west-2`",
            "sourceIPAddress": "`127.0.0.1`",
            "userAgent": "`[]`",
            "requestParameters": {
                "mediaFormat": "`flac`",
                "languageCode": "`en-US`",
                "transcriptionJobName": "`my-first-transcription-job`",
                "media": {
                    "mediaFileUri": ""
                }
            },
            "responseElements": {
                "transcriptionJob": {
                    "transcriptionJobStatus": "IN_PROGRESS",
                    "mediaFormat": "`flac`",
                    "creationTime": "`2022-03-07T15:03:44.229000-08:00`",
                    "transcriptionJobName": "`my-first-transcription-job`",
                    "languageCode": "`en-US`",
                    "media": {
                        "mediaFileUri": ""
                    }
                }
            },
            "requestID": "`47B8E8D397DCE7A6`",
            "eventID": "`cdc4b7ed-e171-4cef-975a-ad829d4123e8`",
            "eventType": "AwsApiCall",
            "recipientAccountId": "`111122223333`"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "`IAMUser`",
                "principalId": "`111122223333`",
                "arn": "``arn:aws:iam:us-west-2:111122223333:user/my-user-name``",
                "accountId": "`111122223333`",
                "accessKeyId": "`AKIAIOSFODNN7EXAMPLE`",
                "userName": "`my-user-name`"
            },
            "eventTime": "`2022-03-07T15:07:11Z`",
            "eventSource": "transcribe.amazonaws.com",
            "eventName": "GetTranscriptionJob",
            "awsRegion": "`us-west-2`",
            "sourceIPAddress": "`127.0.0.1`",
            "userAgent": "`[]`",
            "requestParameters": {
                "transcriptionJobName": "`my-first-transcription-job`"
            },
            "responseElements": {
                "transcriptionJob": {
                    "settings": {

                    },
                    "transcriptionJobStatus": "`COMPLETED`",
                    "mediaFormat": "`flac`",
                    "creationTime": "`2022-03-07T15:03:44.229000-08:00`",
                    "transcriptionJobName": "`my-first-transcription-job`",
                    "languageCode": "`en-US`",
                    "media": {
                        "mediaFileUri": ""
                    },
                    "transcript": {
                        "transcriptFileUri": ""
                    }
                }
            },
            "requestID": "`BD8798EACDD16751`",
            "eventID": "`607b9532-1423-41c7-b048-ec2641693c47`",
            "eventType": "AwsApiCall",
            "recipientAccountId": "`111122223333`"
        }
    ]
}
```
