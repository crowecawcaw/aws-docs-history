# Logging Macie API calls with AWS CloudTrail

Amazon Macie integrates with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), which is a
service that provides a record of actions taken by a user, a role, or an AWS service. CloudTrail
captures all
API calls for Macie as management events. The calls captured include calls from the Amazon Macie
console and programmatic calls to Amazon Macie API operations. By using the information collected
by CloudTrail, you can determine the request that was made to Macie, the IP address from which the
request was made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity
information helps you determine the following:

- Whether the request was made with root user or user credentials.
- Whether the request was made on behalf of an AWS IAM Identity Center user.
- Whether the request was made with temporary security credentials for a role or federated
  user.
- Whether the request was made by another AWS service.
  CloudTrail is active in your AWS account when you create the account, and you automatically have
  access to the CloudTrail **Event history**. The CloudTrail **Event
  history** provides a viewable, searchable, downloadable, and immutable record of the
  past 90 days of recorded management events in an AWS Region. For more information, see [Working
  with CloudTrail event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_. There are no CloudTrail
  charges for viewing the **Event history**.

For an ongoing record of events in your AWS account for the past 90 days, create a trail
or a CloudTrail Lake event data store.

**CloudTrail trails**

A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") and [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the _AWS CloudTrail User Guide_.

You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

**CloudTrail Lake event data stores**

_CloudTrail Lake_ lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/") format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into _event data stores_, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors"). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") in the _AWS CloudTrail User Guide_.

CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

## Macie management events in AWS CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

Amazon Macie logs all Macie control plane operations as management events in CloudTrail. For
example, calls to the `ListFindings`, `DescribeBuckets`, and
`CreateClassificationJob` operations generate management events in CloudTrail. Each
event includes an `eventSource` field. This field indicates the AWS service that
a request was made to. For Macie events, the value for this field is:
`macie2.amazonaws.com`.

For a list of the control plane operations that Macie logs in CloudTrail, see [Operations](../APIReference/operations.md "../APIReference/operations.md") in
the _Amazon Macie API Reference_.

## Examples of Macie events in AWS CloudTrail

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following examples show CloudTrail events that demonstrate Amazon Macie
operations. For details about the information that an event might contain, see [CloudTrail
record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the _AWS CloudTrail User
Guide_.

###### Examples

- [Listing findings](#logging-ct-events-example-listfindings "#logging-ct-events-example-listfindings")
- [Retrieving sensitive data
  samples for a finding](#logging-ct-events-example-getsdoccurrences "#logging-ct-events-example-getsdoccurrences")
- [Deleting a membership invitation](#logging-ct-events-example-deleteinvitations "#logging-ct-events-example-deleteinvitations")
- [Disabling Macie](#logging-ct-events-example-disablemacie "#logging-ct-events-example-disablemacie")

### Example: Listing findings

The following example shows a CloudTrail event for the Amazon Macie [ListFindings](../APIReference/findings.md "../APIReference/findings.md") operation. In this
example, an AWS Identity and Access Management (IAM) user (`Mary_Major`) used the Amazon Macie console to
retrieve a subset of information about current policy findings for their account.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "123456789012",
        "arn": "arn:aws:iam::123456789012:user/Mary_Major",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "Mary_Major",
        "sessionContext":{
            "attributes": {
                "creationdate": "2024-11-14T15:49:57Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-11-14T16:09:56Z",
    "eventSource": "macie2.amazonaws.com",
    "eventName": "ListFindings",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "198.51.100.1",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "requestParameters": {
        "sortCriteria": {
            "attributeName": "updatedAt",
            "orderBy": "DESC"
        },
        "findingCriteria": {
            "criterion": {
                "archived": {
                    "eq": [
                        "false"
                    ]
                },
                "category": {
                    "eq": [
                        "POLICY"
                    ]
                }
            }
        },
        "maxResults": 25,
        "nextToken": ""
    },
    "responseElements": null,
    "requestID": "d58af6be-1115-4a41-91f8-ace03example",
    "eventID": "ad97fac5-f7cf-4ff9-9cf2-d0676example",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

### Example: Retrieving sensitive data

samples for a finding

This example shows CloudTrail events for retrieving and revealing samples of sensitive data
that Amazon Macie reported in a finding. In this example, an IAM user (`JohnDoe`)
used the Amazon Macie console to retrieve and reveal sensitive data samples. The user's account
is configured to assume an IAM role (`MacieReveal`) to retrieve and reveal
sensitive data samples from affected Amazon Simple Storage Service (Amazon S3) objects.

The following event shows details about the user's request to retrieve and reveal
sensitive data samples by using the Amazon Macie [GetSensitiveDataOccurrences](../APIReference/findings-findingid-reveal.md "../APIReference/findings-findingid-reveal.md") operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "UU4MH7OYK5ZCOAEXAMPLE:JohnDoe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/JohnDoe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "UU4MH7OYK5ZCOAEXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2024-12-12T14:40:23Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-12-12T17:04:47Z",
    "eventSource": "macie2.amazonaws.com",
    "eventName": "GetSensitiveDataOccurrences",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "198.51.100.252",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "requestParameters": {
        "findingId": "3ad9d8cd61c5c390bede45cd2example"
    },
    "responseElements": null,
    "requestID": "c30cb760-5102-47e7-88d8-ff2e8example",
    "eventID": "baf52d92-f9c3-431a-bfe8-71c81example",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

The next event shows details about Macie then assuming the specified IAM role
(`MacieReveal`) by using the AWS Security Token Service (AWS STS) [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md")
operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "reveal-samples.macie.amazonaws.com"
    },
    "eventTime": "2024-12-12T17:04:47Z",
    "eventSource": "sts.amazonaws.com",
    "eventName": "AssumeRole",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "reveal-samples.macie.amazonaws.com",
    "userAgent": "reveal-samples.macie.amazonaws.com",
    "requestParameters": {
        "roleArn": "arn:aws:iam::111122223333:role/MacieReveal",
        "roleSessionName": "RevealCrossAccount"
    },
    "responseElements": {
        "credentials": {
            "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
            "sessionToken": "XXYYaz...
EXAMPLE_SESSION_TOKEN
XXyYaZAz",
            "expiration": "Dec 12, 2024, 6:04:47 PM"
        },
        "assumedRoleUser": {
            "assumedRoleId": "AROAXOTKAROCSNEXAMPLE:RevealCrossAccount",
            "arn": "arn:aws:sts::111122223333:assumed-role/MacieReveal/RevealCrossAccount"
        }
    },
    "requestID": "d905cea8-2dcb-44c1-948e-19419example",
    "eventID": "74ee4d0c-932d-3332-87aa-8bcf3example",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::IAM::Role",
            "ARN": "arn:aws:iam::111122223333:role/MacieReveal"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

### Example: Deleting a membership invitation

The following example shows a CloudTrail event for the Amazon Macie [DeleteInvitations](../APIReference/invitations-delete.md "../APIReference/invitations-delete.md")
operation. In this example, Macie logged an event in the delegated Macie administrator account for an
organization when a member disassociated their account from the administrator's account and
deleted the administrator's invitation to join the organization. In the example, the account
ID for the administrator's AWS account is `777788889999`. The account
ID for the member account is `111122223333`.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AWSAccount",
        "accountId": "111122223333",
        "invokedBy": "macie2.amazonaws.com"
    },
    "eventTime": "2025-09-20T18:44:58Z",
    "eventSource": "macie2.amazonaws.com",
    "eventName": "MacieMemberUpdated",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "macie2.amazonaws.com",
    "userAgent": "macie2.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "2f08152c-66b9-35f8-8a10-6fe1bexample",
    "readOnly": false,
    "resources": [{
        "accountId": "777788889999",
        "type": "AWS::Macie::Member",
        "ARN": "arn:aws:macie2:us-east-2:777788889999:member/111122223333"
    }],
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "777788889999",
    "sharedEventID": "2bff2ad0-f233-48c6-8720-ca9dbexample",
    "serviceEventDetails": {
        "memberAccount": "111122223333",
        "memberResourceStatus": "DELETED",
        "apiOperation": "DeleteInvitations"
    },
    "eventCategory": "Management"
}
```

### Example: Disabling Macie

This example shows CloudTrail events for disabling Amazon Macie for an AWS account. In this
example, an IAM user (`JohnDoe`) disabled Macie for their account. Macie then
cancelled and deleted all sensitive data discovery jobs for the account, in addition to deleting other
Macie resources and data for the account.

The following event shows details about the user's request to disable Macie for their
account by using the Amazon Macie [DisableMacie](../APIReference/macie.md "../APIReference/macie.md")
operation.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAXYKJR2G5JXEXAMPLE:JohnDoe",
        "arn": "arn:aws:sts::123456789012:assumed-role/Admin/JohnDoe",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAXYKJR2G5JXEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/Admin",
                "accountId": "123456789012",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-09-18T21:54:42Z",
                "mfaAuthenticated": "true"
            }
        }
    },
    "eventTime": "2025-09-18T21:57:06Z",
    "eventSource": "macie2.amazonaws.com",
    "eventName": "DisableMacie",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "198.51.100.1",
    "userAgent": "aws-cli/2.17.9 md/awscrt#0.20.11 ua/2.0 os/macos#24.4.0 md/arch#x86_64 lang/python#3.11.8 md/pyimpl#CPython cfg/retry-mode#standard md/installer#exe md/prompt#off md/command#macie2.disable-macie",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "941d1d6c-c1b2-4db5-845f-1250cexample",
    "eventID": "06554dba-417b-4a65-90b8-4e5d5example",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

The next event shows details about Macie then cancelling and deleting one of the
sensitive data discovery jobs for the account.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "Root",
        "accountId": "123456789012",
        "invokedBy": "macie2.amazonaws.com"
    },
    "eventTime": "2025-09-18T21:57:18Z",
    "eventSource": "macie2.amazonaws.com",
    "eventName": "MacieClassificationJobCancelled",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "macie2.amazonaws.com",
    "userAgent": "macie2.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "df39ea1d-cd4e-4130-8cd5-cd33cexample",
    "readOnly": false,
    "resources": [{
        "accountId": "123456789012",
        "type": "AWS::Macie::ClassificationJob",
        "ARN": "arn:aws:macie2:us-east-2:123456789012:classification-job/f252cbe854ae0a1a47d8304f4example"
    }],
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "serviceEventDetails": {
        "macieStatus": "DISABLED",
        "classificationJobStatus": "CANCELLED"
    },
    "eventCategory": "Management"
}
```
