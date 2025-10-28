# Logging AWS RTB Fabric API calls using

AWS CloudTrail

AWS RTB Fabric is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a service that provides a record of actions taken by a user, role, or an
AWS service. CloudTrail captures all
API calls for RTB Fabric as events. The calls captured include calls from the RTB Fabric console
and code calls to the RTB Fabric API operations. Using the information collected by CloudTrail, you can
determine the request that was made to RTB Fabric, the IP address from which the request was
made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity
information helps you determine the following:

- Whether the request was made with root user or user credentials.
- Whether the request was made on behalf of an IAM Identity Center user.
- Whether the request was made with temporary security credentials for a role or federated
  user.
- Whether the request was made by another AWS service.
  CloudTrail is active in your AWS account when you create the account and you automatically have
  access to the CloudTrail **Event history**. The CloudTrail **Event
  history** provides a viewable, searchable, downloadable, and immutable record of the
  past 90 days of recorded management events in an AWS Region. For more information, see [Working
  with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_. There are no CloudTrail
  charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a
[CloudTrail
Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") event data store.

**CloudTrail trails**

A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") and [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the _AWS CloudTrail User Guide_.

You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

**CloudTrail Lake event data stores**

_CloudTrail Lake_ lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/") format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into _event data stores_, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors"). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") in the _AWS CloudTrail User Guide_.

CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

## RTB Fabric management events in CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

AWS RTB Fabric logs all RTB Fabric control plane operations as management events. For a list
of the AWS RTB Fabric control plane operations that RTB Fabric logs to CloudTrail, see the
[AWS RTB Fabric API Reference](../../../RTB Fabric/latest/APIReference.md "../../../RTB Fabric/latest/APIReference.md").

## RTB Fabric event examples

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail event that demonstrates the
`AcceptLink` operation.

```
{
      "eventVersion": "1.09",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AAAABACDEFFGHIJ3KLM5N:IntegrationTest",
        "arn": "arn:aws:sts::123456789012:assumed-role/TestRole/IntegrationTest",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "AAAABACDEFFGHIJ3KLM5N",
            "arn": "arn:aws:iam::123456789012:role/TestRole",
            "accountId": "123456789012",
            "userName": "TestRole"
          },
          "attributes": {
            "creationDate": "2025-10-01T22:16:35Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2025-10-01T22:17:29Z",
      "eventSource": "rtbfabric.amazonaws.com",
      "eventName": "AcceptLink",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "10.0.0.1",
      "userAgent": "aws-sdk-java/2.34.3 md/io#sync md/http#Apache ua/2.1 api/Some#2.34.x os/Linux#5.10.242-219.961.amzn2int.x86_64 lang/java#17.0.16 md/OpenJDK_64-Bit_Server_VM#17.0.16+8-LTS md/vendor#Amazon.com_Inc. md/en_US md/kotlin/2.0.21-release-482 cfg/auth-source#stsrole m/D,N",
      "requestParameters": {
        "rtbGatewayId": "rtb-gw-responder456",
        "linkId": "link-12345678",
        "attributes": {
          "customerProvidedId": "accepted-link-123"
        },
        "logSettings": {
          "applicationLogs": {
            "sampling": {
              "errorLog": 0,
              "filterLog": 0
            }
          }
        }
      },
      "responseElements": {
        "rtbGatewayId": "rtb-gw-responder456",
        "peerRtbGatewayId": "rtb-gw-requester123",
        "linkId": "link-12345678",
        "createdTimestamp": 1695734400,
        "attributes": {
          "customerProvidedId": "accepted-link-123"
        },
        "state": "ACTIVATING",
        "updatedTimestamp": 1695734500,
        "direction": "INBOUND"
      },
      "requestID": "ba5b8aa9-30a5-4a65-88eb-8e8c9d644d48",
      "eventID": "200c17c9-40c9-4f2c-b24f-864c3a4db0b9",
      "readOnly": false,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "123456789012",
      "eventCategory": "Management"
}
```

For information about CloudTrail record contents, see [CloudTrail
record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the _AWS CloudTrail User Guide_.
