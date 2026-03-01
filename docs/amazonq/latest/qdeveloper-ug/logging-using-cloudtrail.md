# Logging Amazon Q Developer API calls using AWS CloudTrail

Amazon Q Developer Pro is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, role, or an AWS service in Amazon Q. CloudTrail captures all API calls for Amazon Q as events.
The calls captured include calls from the Amazon Q console and code calls to the Amazon Q API
operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an
Amazon S3 bucket, including events for Amazon Q. If you don’t configure a trail, you can still view
the most recent events in the CloudTrail console in **Event
history**. Using the information collected by CloudTrail, you can determine the request
that was made to Amazon Q, the IP address from which the request was made, who made the
request, when it was made, and additional details.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Amazon Q Developer information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs
in Amazon Q Developer, that activity is recorded in a CloudTrail event along with other AWS service events
in **Event history**. You can view, search, and download
recent events in your AWS account. For more information, see [Viewing Events with
CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User
Guide_.

For an ongoing record of events in your AWS account, including events for Amazon Q,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all
AWS Regions. The trail logs events from all Regions in the AWS partition and delivers
the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other
AWS services to further analyze and act upon the event data collected in CloudTrail logs. For
more information, see the following topics in the _AWS CloudTrail User
Guide_:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All Amazon Q Developer actions are logged by CloudTrail and generate entries in the CloudTrail log
files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials
- Whether the request was made with temporary security credentials for a role or
  federated user
- Whether the request was made by another AWS service

For more information, see [CloudTrail
userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md") in the _AWS CloudTrail User
Guide_.

## Understanding Amazon Q Developer log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event
represents a single request from any source and includes information about the requested
action, the date and time of the action, request parameters, and so on. CloudTrail log files
aren’t an ordered stack trace of the public API calls, so they don’t appear in any specific
order.

Amazon Q Developer also makes API calls with a `dryRun` parameter to verify that you have
the necessary permissions for the action, without actually making the request. Calls to Amazon Q Developer
APIs with the `dryRun` parameter are captured as events and recorded in a CloudTrail log with
`"dryRun" : true` in the `requestParameters` field.

The following example shows a CloudTrail log entry that demonstrates the
`SendMessage` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAXD12ABCDEF3G4HI5J:aws-user",
        "arn": "arn:aws:sts::123456789012:assumed-role/PowerUser/aws-user",
        "accountId": "123456789012",
        "accessKeyId": "ASIAAB12CDEFG34HIJK",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAXD12ABCDEF3G4HI5J",
                "arn": "arn:aws:iam::123456789012:role/PowerUser",
                "accountId": "123456789012",
                "userName": "PowerUser"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-11-28T10:00:00Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-11-28T10:00:00Z",
    "eventSource": "q.amazonaws.com",
    "eventName": "SendMessage",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "123.456.789.012",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "requestParameters": {
        "Origin": "https://conversational-experience-worker.widget.console.aws.amazon.com",
        "conversationId": "a298ec0d-0a49-4d2e-92bd-7d6e629b4619",
        "source": "CONSOLE",
        "conversationToken": "***",
        "utterance": "***"
    },
    "responseElements": {
        "result": {
            "content": {
                "text": {
                    "body": "***",
                    "references": []
                }
            },
            "format": "PLAINTEXT",
            "intents": {},
            "type": "TEXT"
        },
        "Access-Control-Expose-Headers": "x-amzn-RequestId,x-amzn-ErrorType,x-amzn-ErrorMessage,Date",
        "metadata": {
            "conversationExpirationTime": "2024-02-25T19:31:38Z",
            "conversationId": "a298ec0d-0a49-4d2e-92bd-7d6e629b4619",
            "conversationToken": "***",
            "utteranceId": "3b87b46f-04a9-41ef-b8fe-8abf52d2c053"
        },
        "resultCode": "LLM"
    },
    "additionalEventData": {
        "quickAction": "dev"
    },
    "requestID": "19b3c30e-906e-4b7f-b5c3-509f67248655",
    "eventID": "a552c487-7d97-403a-8ec4-d49539c7a03d",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates the
`PassRequest` action.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDA6ON6E4XEGIEXAMPLE",
        "arn": "arn:aws:iam::555555555555:user/Mary",
        "accountId": "555555555555",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
            "type": "Role",
            "principalId": "AIDA6ON6E4XEGIEXAMPLE",
            "arn": "arn:aws:iam::555555555555:user/Mary",
            "accountId": "555555555555",
            "userName": "Mary"

        },
        "attributes": {
            "creationDate": "2024-04-10T20:03:01Z",
            "mfaAuthenticated": "false"
        },
        "invokedBy": "q.amazonaws.com"
    },
    "eventTime": "2024-04-10T20:04:42Z",
    "eventSource": "q.amazonaws.com",
    "eventName": "PassRequest",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "q.amazonaws.com",
    "userAgent": "q.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "2d528c76-329e-410b-9516-EXAMPLE565dc",
    "eventID": "ba0801a1-87ec-4d26-be87-EXAMPLE75bbb",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "555555555555",
    "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates Amazon Q calling
the `s3:ListBuckets` action on your behalf.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDA6ON6E4XEGIEXAMPLE",
        "arn": "arn:aws:iam::555555555555:user/Paulo",
        "accountId": "555555555555",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDA6ON6E4XEGIEXAMPLE",
                "arn": "arn:aws:iam::555555555555:user/Paulo",
                "accountId": "555555555555",
                "userName": "Paulo"
            },
            "attributes": {
                "creationDate": "2024-04-10T14:06:08Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "q.amazonaws.com"
    },
    "eventTime": "2024-04-10T14:07:55Z",
    "eventSource": "s3.amazonaws.com",
    "eventName": "ListBuckets",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "q.amazonaws.com",
    "userAgent": "q.amazonaws.com",
    "requestParameters": {
        "Host": "s3.amazonaws.com"
    },
    "responseElements": null,
    "additionalEventData": {
        "SignatureVersion": "SigV4",
        "CipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "bytesTransferredIn": 0,
        "AuthenticationMethod": "AuthHeader",
        "x-amz-id-2": "ExampleRequestId123456789",
        "bytesTransferredOut": 4054
    },
    "requestID": "ecd94349-b36f-44bf-b6f5-EXAMPLE9c463",
    "eventID": "2939ba50-1d26-4a5a-83bd-EXAMPLE85850",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "555555555555",
    "vpcEndpointId": "vpce-EXAMPLE1234",
    "eventCategory": "Management"
}

```
