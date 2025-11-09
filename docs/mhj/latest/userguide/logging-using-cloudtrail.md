AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Logging AWS Migration Hub Journeys API calls with

AWS CloudTrail

AWS Migration Hub Journeys is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in Migration Hub Journeys. CloudTrail captures API calls for
Migration Hub Journeys as events. The calls captured include calls from the Migration Hub Journeys console and code
calls to the Migration Hub Journeys API operations. If you create a trail, you can enable continuous
delivery of CloudTrail events to an Amazon S3 bucket, including events for Migration Hub Journeys. If you don't
configure a trail, you can still view the most recent events in the CloudTrail console in
**Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to Migration Hub Journeys, the IP address from which the request was
made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Migration Hub Journeys information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity
occurs in Migration Hub Journeys, that activity is recorded in a CloudTrail event along with other AWS
service events in **Event history**. You can view, search, and download
recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account past 90 days, create a trail or
a [CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") event data store.

**CloudTrail trails**

A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") and [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the _AWS CloudTrail User Guide_.

You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

**CloudTrail Lake event data stores**

_CloudTrail Lake_ lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/") format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into _event data stores_, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors"). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") in the _AWS CloudTrail User Guide_.

CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

Migration Hub Journeys supports logging the following actions as events in CloudTrail log files:

- AcceptConnection
- BatchAssociateIamRoleWithConnection
- BatchDisassociateIamRoleFromConnection
- DeleteConnection
- GetConnection
- ListConnectionRoles
- ListConnections
- RejectConnection

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user
  credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding Migration Hub Journeys log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event
represents a single request from any source and includes information about the requested
action, the date and time of the action, request parameters, and so on. CloudTrail log files
aren't an ordered stack trace of the public API calls, so they don't appear in any
specific order.

The following example shows a CloudTrail log entry that demonstrates the
`AcceptConnection` action.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "ABCDEFGHIJKLMNOPQRSTU:22b8b0d6c28b408a888c64ea23271305",
        "arn": "arn:aws:sts::123456789012:assumed-role/HydraInvocationRole-f5c34611abfd4b2098a561bd5729dfabf5c3461/22b8b0d6c28b408a888c64ea23271305",
        "accountId": "123456789012",
        "accessKeyId": "VWXYZABCDEFGHIJKLMNO",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "ABCDEFGHIJKLMNOPQRSTU",
                "arn": "arn:aws:iam::123456789012:role/HydraInvocationRole-f5c34611abfd4b2098a561bd5729dfabf5c3461",
                "accountId": "123456789012",
                "userName": "HydraInvocationRole-f5c34611abfd4b2098a561bd5729dfabf5c3461"
            },
            "attributes": {
                "creationDate": "2024-11-19T22:16:50Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-11-19T22:39:58Z",
    "eventSource": "journeys.amazonaws.com",
    "eventName": "AcceptConnection",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "35.83.56.40",
    "userAgent": "Coral/Apache-HttpClient5",
    "requestParameters": {
        "connectionArn": "arn%3Aaws%3Amgh%3Aus-east-2%3A123456789012%3Aconnections%2FA4mCDLsAvvD3WERjkA49c"
    },
    "responseElements": {
        "connection": {
            "arn": "arn:aws:mgh:us-east-2:123456789012:connections/A4mCDLsAvvD3WERjkA49c",
            "createdBy": {
                "arn": "arn:aws:mgh:::users/960e62ae-1ad3-4d5a-b0d9-c51f34c122f3",
                "displayName": "***",
                "emailAddress": "***"
            },
            "creationTime": 1732055997.346,
            "lastUpdatedBy": {
                "arn": "arn:aws:mgh:::users/960e62ae-1ad3-4d5a-b0d9-c51f34c122f3",
                "displayName": "***",
                "emailAddress": "***"
            },
            "lastUpdatedTime": 1732055997.346,
            "name": "migops_cp_test_beta_20241119-223957_6DhSIqM",
            "requestRespondedBy": "ABCDEFGHIJKLMNOPQRSTU:22b8b0d6c28b408a888c64ea23271305",
            "resourceArn": "arn:aws:mgh:us-east-2::journeys/ofocphgdQUOzT0H4cAVswA",
            "resourceName": "migops_cp_test_beta_20241119-223900_Hs625sm",
            "status": "Connected"
        }
    },
    "requestID": "bb730d41-62a4-4df4-a6da-0586307c2b55",
    "eventID": "900cae4d-27eb-48aa-87e2-c99c285e3012",
    "readOnly": false,
    "resources": [
        {
            "accountId": "123456789012",
            "type": "AWS::MGH::Connections",
            "ARN": "arn:aws:mgh:us-east-2:123456789012:connections/A4mCDLsAvvD3WERjkA49c"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```
