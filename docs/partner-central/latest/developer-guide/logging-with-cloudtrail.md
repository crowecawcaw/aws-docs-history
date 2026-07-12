The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Logging the AWS Partner Central Selling API

[AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") is a service that enables governance, compliance, operational auditing, and
risk auditing of your AWS account. With AWS CloudTrail, you can log, continuously monitor, and
retain account activity related to actions across your AWS infrastructure. AWS Partner Central API
activity is recorded as events in CloudTrail. You can create a trail, a configuration that
enables delivery of events as log files to an Amazon S3 bucket.

## Overview

The AWS Partner Central API is integrated with AWS CloudTrail, a service that provides a record of
actions taken by a user, role, or an AWS service in AWS Partner Central. CloudTrail captures all API
calls for AWS Partner Central as events. The calls captured include calls from the AWS Partner Central and from
code calls to the AWS Partner Central API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an
Amazon S3 bucket, including events for AWS Partner Central. If you don't configure a trail, you can
still view the most recent events in the CloudTrail console in Event history.

Using the information collected by CloudTrail, you can determine the request that was
made to AWS Partner Central, the IP address from which the request was made, who made the request, when
it was made, and additional details.

## Understanding AWS Partner Central Selling API log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket. When your trail tracks AWS Partner Central events, CloudTrail processes the events as log files
across all the regions. Each log file can contain one or more events.

The following example shows a CloudTrail log entry that demonstrates the
`ListOpportunities` action on AWS Partner Central:

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "ABCDEFGHIJKLMNOP12345",
        "arn": "arn:aws:iam::123456789010:user/CloudTrailTestUser",
        "accountId": "123456789010",
        "accessKeyId": "ABCDEFGHIJKLMNOP1234",
        "userName": "CloudTrailTestUser"
    },
    "eventTime": "2023-10-17T21:49:23Z",
    "eventSource": "partnercentral-selling.amazonaws.com",
    "eventName": "ListOpportunities",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "PostmanRuntime/7.18.0",
    "requestParameters": {
        "MaxResults": 20
    },
    "responseElements": null,
    "requestID": "fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
    "eventID": "7EXAMPLE-97d6-4139-91e3-01aEXAMPLE48",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "recipientAccountId": "123456789010"
}
```

In this example, the `ListOpportunities` action was called by the IAM user
named CloudTrailTestUser. The action was called in the _us-east-1_
AWS Region, and the request was made on October 17, 2023 at 21:49:23 UTC.

## Fields in AWS Partner Central Selling API log file entries

Each entry in a CloudTrail log file contains information about who made a request, the
resources acted upon in the request, and the response elements returned by AWS Partner Central. The
list of fields in a log entry, such as `eventVersion`, `userIdentity`,
and `eventTime`, provide detailed information about the action. For example, the
`sourceIPAddress` field shows the IP address that the request was made from.
