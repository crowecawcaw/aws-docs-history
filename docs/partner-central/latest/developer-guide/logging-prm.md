The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Logging the AWS Partner Central Revenue Attribution API

[AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") is a
service that enables governance, compliance, operational auditing, and risk auditing of your
AWS account. With AWS CloudTrail, you can log, continuously monitor, and retain account activity
related to actions across your AWS infrastructure. AWS Partner Central Revenue Measurement API
activity is recorded as events in CloudTrail. You can create a trail, a configuration that
enables delivery of events as log files to an Amazon S3 bucket.

## Overview

The AWS Partner Central Revenue Measurement API is integrated with AWS CloudTrail, a service that
provides a record of actions taken by a user, role, or an AWS service in AWS Partner Central.
CloudTrail captures all API calls for AWS Partner Central Revenue Attribution as events. The calls
captured include calls from the AWS Partner Central console and from code calls to the AWS Partner Central
Revenue Measurement API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an
Amazon S3 bucket, including events for AWS Partner Central Revenue Measurement. If you don't
configure a trail, you can still view the most recent events in the CloudTrail console
in **Event history**.

Using the information collected by CloudTrail, you can determine the request that was
made to AWS Partner Central Revenue Measurement, the IP address from which the request was made,
who made the request, when it was made, and additional details.

The following AWS Partner Central Revenue Measurement API actions are logged in
CloudTrail:

- `CreateRevenueAttribution`
- `UpdateRevenueAttribution`
- `GetRevenueAttribution`
- `ListRevenueAttributions`
- `TagResource`
- `UntagResource`
- `ListTagsForResource`
- `CreateMarketplaceRevenueShare`
- `GetMarketplaceRevenueShare`
- `ListMarketplaceRevenueShares`
- `CreateMarketplaceRevenueShareAllocation`
- `GetMarketplaceRevenueShareAllocation`
- `UpdateMarketplaceRevenueShareAllocation`
- `ListMarketplaceRevenueShareAllocations`
- `StartRevenueAttributionAllocationsTask`
- `GetRevenueAttributionAllocationsTask`
- `ListRevenueAttributionAllocations`
- `GetRevenueAttributionAllocation`

## Understanding AWS Partner Central Revenue Measurement API log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon
S3 bucket. When your trail tracks AWS Partner Central Revenue Measurement events, CloudTrail
processes the events as log files across all the regions. Each log file can contain one
or more events.

The following example shows a CloudTrail log entry that demonstrates the
`CreateRevenueAttribution` action on AWS Partner Central Revenue
Attribution:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:user/CloudTrailTestUser",
        "accountId": "123456789012",
        "accessKeyId": "AKIAEXAMPLEKEY",
        "userName": "CloudTrailTestUser"
    },
    "eventTime": "2026-06-02T11:53:54Z",
    "eventSource": "partnercentral-prm.amazonaws.com",
    "eventName": "CreateRevenueAttribution",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.1",
    "userAgent": "aws-sdk-java/2.20.0",
    "requestParameters": {
        "catalog": "AWS",
        "name": "my-revenue-attribution",
        "marketplaceProduct": {
            "tenancyModel": "MULTI_TENANT"
        }
    },
    "responseElements": {
        "id": "ra-0123456789abcdef0",
        "arn": "arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/revenue-attribution/ra-0123456789abcdef0",
        "name": "my-revenue-attribution",
        "revision": "1"
    },
    "requestID": "5ce2f907-3850-412a-b1a4-r012r1234567",
    "eventID": "80b39b72-eefe-4578-8db0-01ee2e34ee56",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "123456789012"
}
```

In this example, the `CreateRevenueAttribution` action was called by the
IAM user named CloudTrailTestUser. The action was called in the
_us-east-1_ AWS Region, and the request was made on June 2, 2026
at 11:53:54 UTC. A new revenue attribution resource was created with the ID
`ra-0123456789abcdef0`.

## Fields in AWS Partner Central Revenue Measurement API log file entries

Each entry in a CloudTrail log file contains information about who made a request,
the resources acted upon in the request, and the response elements returned by
AWS Partner Central Revenue Measurement. The list of fields in a log entry, such as
`eventVersion`, `userIdentity`, and `eventTime`,
provide detailed information about the action. For example, the
`sourceIPAddress` field shows the IP address that the request was made
from.
