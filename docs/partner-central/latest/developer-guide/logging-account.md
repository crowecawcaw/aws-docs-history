The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Logging the AWS Partner Central Account API

[AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") is a service that enables governance, compliance, operational auditing, and
risk auditing of your AWS account. With AWS CloudTrail, you can log, continuously monitor, and
retain account activity related to actions across your AWS infrastructure. AWS Partner Central Account API
activity is recorded as events in CloudTrail. You can create a trail, a configuration that
enables delivery of events as log files to an Amazon S3 bucket.

## Overview

The AWS Partner Central Account API is integrated with AWS CloudTrail, a service that provides a record of
actions taken by a user, role, or an AWS service in AWS Partner Central. CloudTrail captures all API
calls for AWS Partner Central Account API as events. The calls captured include calls from the AWS Partner Central and from
code calls to the AWS Partner Central Account API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an
Amazon S3 bucket, including events for AWS Partner Central Account API. If you don't configure a trail, you can
still view the most recent events in the CloudTrail console in Event history.

Using the information collected by CloudTrail, you can determine the request that was
made to AWS Partner Central Account API, the IP address from which the request was made, who made the request, when
it was made, and additional details.

## Understanding AWS Partner Central Account API log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket. When your trail tracks AWS Partner Central Account API events, CloudTrail processes the events as log files
across all the regions. Each log file can contain one or more events.

The following example shows a CloudTrail log entry that demonstrates the
`CreatePartner` action on AWS Partner Central Account API:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::123456789012:user/CloudTrailTestUser",
        "accountId": "123456789012",
        "accessKeyId": "ABCDEFGHIJKLMNOP1234",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAEXAMPLE52AGFT725JGDZ",
                "arn": "arn:aws:iam::123456789012:role/ExampleRole",
                "accountId": "123456789012",
                "userName": "ExampleRole"
            },
            "attributes": {
                "creationDate": "2025-11-07T19:45:28Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-07T19:45:58Z",
    "eventSource": "partnercentral-account.amazonaws.com",
    "eventName": "CreatePartner",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "PostmanRuntime/7.18.0",
    "requestParameters": {
        "catalog": "AWS",
        "clientToken": "abcdef12-3456-7890-bcde-f123456789ab",
        "legalName": "ExampleLegalName",
        "primarySolutionType": "VALUE_ADDED_RESALE_AWS_SERVICES",
        "allianceLeadContact": {
            "firstName": "ExampleFirstName",
            "lastName": "ExampleLastName",
            "email": "example@domain.com",
            "businessTitle": "ExampleBusinessTitle"
        },
        "emailVerificationCode": "ExampleVerificationCode",
        "tags": [
            {
                "key": "office",
                "value": "1"
            }
        ]
    },
    "responseElements": {
        "catalog": "AWS",
        "arn": "arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/partner/EXAMPLE_PARTNER_ID",
        "id": "EXAMPLE_PARTNER_ID",
        "legalName": "ExampleLegalName",
        "createdAt": "2025-11-07T19:45:57.867007329Z",
        "profile": {
            "primarySolutionType": "VALUE_ADDED_RESALE_AWS_SERVICES"
        },
        "allianceLeadContact": {
            "firstName": "ExampleFirstName",
            "lastName": "ExampleLastName",
            "email": "example@domain.com",
            "businessTitle": "ExampleBusinessTitle"
        }
    },
    "requestID": "12345678-1234-5678-9abc-def012345678",
    "eventID": "87654321-4321-8765-cba9-fed098765432",
    "readOnly": false,
    "resources": [
        {
            "accountId": "123456789012",
            "type": "AWS::PartnerCentral::Partner",
            "ARN": "arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/partner/EXAMPLE_PARTNER_ID"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "partnercentral-account.partner.us-east-1.api.aws"
    }
}
```

In this example, the `CreatePartner` action was called by the IAM user
named CloudTrailTestUser. The request was made on November 7, 2025 at 19:45:58 UTC.
The request created a new partner with ID `EXAMPLE_PARTNER_ID` for the AWS catalog with the legal name "ExampleLegalName".

## Fields in AWS Partner Central Account API log file entries

Each entry in a CloudTrail log file contains information about who made a request, the
resources acted upon in the request, and the response elements returned by AWS Partner Central Account API. The
list of fields in a log entry, such as `eventVersion`, `userIdentity`,
and `eventTime`, provide detailed information about the action. For example, the
`sourceIPAddress` field shows the IP address that the request was made from.
