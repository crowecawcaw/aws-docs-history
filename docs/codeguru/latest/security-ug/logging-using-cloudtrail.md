On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Logging Amazon CodeGuru Security API calls using AWS CloudTrail

Amazon CodeGuru Security is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in CodeGuru Security. CloudTrail captures all API calls for
CodeGuru Security as events. The calls captured include calls from the CodeGuru Security console and
code calls to the CodeGuru Security API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for CodeGuru Security. If
you don't configure a trail, you can still view the most recent events in the CloudTrail console
in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to CodeGuru Security, the IP address from which the request
was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## CodeGuru Security information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs
in CodeGuru Security, that activity is recorded in a CloudTrail event along with other AWS service events
in **Event history**. You can view, search, and download recent events in
your AWS account. For more information, see [Viewing events with CloudTrail Event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for CodeGuru Security,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket.
By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail
logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket
that you specify. Additionally, you can configure other AWS services to further analyze and act
upon the event data collected in CloudTrail logs. For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications
  for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log
  files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log
  files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All CodeGuru Security actions are logged by
CloudTrail and are documented in the [Amazon CodeGuru Security API Reference](../security-api.md "../security-api.md"). For example, calls to the
`CreateScan`, `GetScan` and `GetFindings` actions generate
entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding CodeGuru Security log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `CreateScan` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE:i-1234567890abcdef0",
        "arn": "arn:aws:sts::`123456789012`:assumed-role/`user-name`",
        "accountId": "`123456789012`",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::`123456789012`:role/`user-name`",
                "accountId": "`123456789012`",
                "userName": "`user-name`"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-02-24T00:38:51Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-02-24T00:39:16Z",
    "eventSource": "codeguru-security.amazonaws.com",
    "eventName": "CreateScan",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "205.251.233.176",
    "userAgent": "aws-sdk-java/Linux/x.xx.fleetxen Java_HotSpot(TM)_64-Bit_Server_VM/xx",
    "requestParameters": {
        "resourceId": {
            "codeArtifactId": "cb8c167e-EXAMPLE"
        },

        "clientToken": "e3c6f4ce-EXAMPLE"
    },
    "responseElements": {
        "scanName": "a4469191-EXAMPLE",
        "resourceId": {
            "codeArtifactId": "cb8c167e-EXAMPLE"
        },
        "runId": "a4469191-EXAMPLE",
        "scanState": "InProgress"
    },
    "requestID": "07c4a4de-EXAMPLE",
    "eventID": "711cb5a3-EXAMPLE",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`123456789012`",
    "eventCategory": "Management"
}



```
