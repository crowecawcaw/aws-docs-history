The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Logging the AWS Partner Central Benefits API

[AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") is a service that enables governance, compliance, operational auditing, and
risk auditing of your AWS account. With AWS CloudTrail, you can log, continuously monitor, and
retain account activity related to actions across your AWS infrastructure. AWS Partner Central Benefits API
activity is recorded as events in CloudTrail. You can create a trail, a configuration that
enables delivery of events as log files to an Amazon S3 bucket.

## Overview

The AWS Partner Central Benefits API is integrated with AWS CloudTrail, a service that provides a record of
actions taken by a user, role, or an AWS service in AWS Partner Central. CloudTrail captures all API
calls for AWS Partner Central Benefits API as events. The calls captured include calls from the AWS Partner Central and from
code calls to the AWS Partner Central Benefits API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an
Amazon S3 bucket, including events for AWS Partner Central Benefits API. If you don't configure a trail, you can
still view the most recent events in the CloudTrail console in Event history.

Using the information collected by CloudTrail, you can determine the request that was
made to AWS Partner Central Benefits API, the IP address from which the request was made, who made the request, when
it was made, and additional details.

## Understanding AWS Partner Central Benefits API log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket. When your trail tracks AWS Partner Central Benefits API events, CloudTrail processes the events as log files
across all the regions. Each log file can contain one or more events.

The following example shows a CloudTrail log entry that demonstrates the
`ListBenefitApplications` action on AWS Partner Central Benefits API:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::123456789012:user/CloudTrailTestUser",
        "accountId": "123456789012",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::123456789012:role/TestRole",
                "accountId": "123456789012",
                "userName": "TestRole"
            },
            "attributes": {
                "creationDate": "2025-10-21T03:08:23Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-10-21T03:10:59Z",
    "eventSource": "partnercentral-benefits.amazonaws.com",
    "eventName": "ListBenefitApplications",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "python-requests/2.32.4",
    "requestParameters": {
        "catalog": "AWS"
    },
    "responseElements": null,
    "requestID": "12345678-1234-5678-9abc-def012345678",
    "eventID": "87654321-4321-8765-cba9-fed098765432",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

In this example, the `ListBenefitApplications` action was called by the IAM user
named Alice. The request was made on October 21, 2025 at 03:10:59 UTC.
The request listed benefit applications for the AWS catalog.

## Fields in AWS Partner Central Benefits API log file entries

Each entry in a CloudTrail log file contains information about who made a request, the
resources acted upon in the request, and the response elements returned by AWS Partner Central Benefits API. The
list of fields in a log entry, such as `eventVersion`, `userIdentity`,
and `eventTime`, provide detailed information about the action. For example, the
`sourceIPAddress` field shows the IP address that the request was made from.
