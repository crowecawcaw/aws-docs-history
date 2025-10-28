# Logging AWS Elemental MediaConvert API calls using

AWS CloudTrail

AWS Elemental MediaConvert integrates with AWS CloudTrail, a service that provides a record of operations taken
by a user, role, or an AWS service. CloudTrail captures all operations (API calls) you perform,
including those from the MediaConvert Console, as events. Events contain information about requests
to MediaConvert, including the IP address, who made the request, when it was made, the MediaConvert
operation, and additional details. For more information about CloudTrail events, see [What are CloudTrail events?](../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md#cloudtrail-concepts-events "../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md#cloudtrail-concepts-events")

A few examples of what CloudTrail can help you find include: when you submitted a create job
request, who deleted a queue, or what tags were added to a resource.

For a complete list of all MediaConvert operations you can perform, see the [MediaConvert API Reference](../apireference/resources.md "../apireference/resources.md").

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

###### Topics

- [Finding information about MediaConvert in
  CloudTrail](#service-name-info-in-cloudtrail "#service-name-info-in-cloudtrail")
- [Understanding CloudTrail management
  events for MediaConvert](#understanding-service-name-entries "#understanding-service-name-entries")

## Finding information about MediaConvert in

CloudTrail

You can view, search, and download events from the last 90 days in [Event
history](https://console.aws.amazon.com/cloudtrailv2/home?region=us-west-2#/events "https://console.aws.amazon.com/cloudtrailv2/home?region=us-west-2#/events") in the CloudTrail console. For more information, see [Working with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of CloudTrail events beyond the last 90 days, you must create a CloudTrail
_trail_ or CloudTrail Lake event data store.

**CloudTrail trails**

With CloudTrail trails, CloudTrail delivers log files for events to an Amazon S3 bucket.
Additionally, you can configure other AWS services to [further analyze and act upon the event data](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md") collected. When you
create a trail, CloudTrail [also emits each event to Amazon EventBridge](../../../eventbridge/latest/userguide/eb-service-event.md "../../../eventbridge/latest/userguide/eb-service-event.md"). For more
information about CloudTrail trails, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-getting-started.md "../../../awscloudtrail/latest/userguide/cloudtrail-getting-started.md").

**CloudTrail Lake event data stores**

With CloudTrail Lake event data stores, CloudTrail provides a searchable store of
event data. For more information, see [Working with
CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md").

## Understanding CloudTrail management

events for MediaConvert

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are
performed on resources in your AWS account. These are also known as control plane
operations, or MediaConvert operations. By default, CloudTrail logs all management events.

CloudTrail management events represent a single request from any source. They include
information about where a request originated, who made the request, when the request was
made, the MediaConvert operation, and other important details.

For details about the contents of these events, see [CloudTrail record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md").

**Origin**

Events include the source IP address under `sourceIPAddress`,
AWS Region under `awsRegion`, and user agent (browser or client
info) under `userAgent` to help you find where a request
originated.

**Identity**

Events include identity information, under `userIdentity`, to
help you find who made the request. You can use this information to
determine the following:

- Whether the request was made with root user or user
  credentials.
- Whether the request was made on behalf of an IAM Identity Center user.
- Whether the request was made with temporary security credentials
  for a role or federated user.
- Whether the request was made by another AWS service.

For more information, including a list of relevant fields, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

**Time**

Events include a time stamp, under `eventTime`.

**MediaConvert operation**

Events include the MediaConvert operation under `eventName`. For
example, `CreateJob` when you submit a new job, or
`CreateQueue` when you request a new Queue.

**Other important details**

Some events include specific details about your MediaConvert request under
`requestParameters`, as well as MediaConvert's response under
`responseElements`.

For example, if you submit a `CreateJob` request, the
`requestParameters` field will include the JSON for the job
settings that you submitted. If successful, the event also includes the
complete and validated job settings JSON, as well as the job ID, under
`responseElements`.

For another example, if you submit a `CreateQueue` request, the
`requestParameters` field will include the the queue settings
that you submitted. If successful, the event will also include the queue ARN
under `responseElements`.

###### Note

MediaConvert only supports recording management events in CloudTrail, it does not support data
events. For details about these event types, and their differences, see [CloudTrail
concepts](../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md "../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md").

### Example events

The following examples show a CloudTrail event for the `CreateJob`,
`CreateQueue`, `DeleteQueue`, and `TagResource`
operations. CloudTrail also records all other [MediaConvert operations](../apireference/resources.md "../apireference/resources.md"), though they are not shown here.

**Example event: CreateJob**

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AKIAIOSFODNN7EXAMPLE:example-admin",
        "arn": "arn:aws:sts::111122223333:assumed-role/admin/example-admin",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AKIAIOSFODNN7EXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/admin",
                "accountId": "111122223333",
                "userName": "admin"
            },
            "attributes": {
                "creationDate": "2024-04-04T17:30:19Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-04-04T17:45:26Z",
    "eventSource": "mediaconvert.amazonaws.com",
    "eventName": "CreateJob",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "203.0.113.100",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "requestParameters": {
        "settings": {...},
        "accelerationSettings": {
            "mode": "DISABLED"
        },
        "role": "arn:aws:iam::111122223333:role/service-role/MediaConvert_Default_Role",
        "clientRequestToken": "1712252705233-zyxwvut",
        "statusUpdateInterval": "SECONDS_60",
        "billingTagsSource": "JOB",
        "priority": 0,
        "queue": "arn:aws:mediaconvert:us-west-2:111122223333:queues/Default"
    },
    "responseElements": {
        "job": {
            "arn": "arn:aws:mediaconvert:us-west-2:111122223333:jobs/1712252725875-defhgi",
            "id": "1712252725875-defhgi",
            "createdAt": 1712252726,
            "queue": "arn:aws:mediaconvert:us-west-2:111122223333:queues/Default",
            "role": "arn:aws:iam::111122223333:role/service-role/MediaConvert_Default_Role",
            "settings": {...},
            "status": "SUBMITTED",
            "timing": {
                "submitTime": 1712252726
            },
            "billingTagsSource": "JOB",
            "accelerationSettings": {
                "mode": "DISABLED"
            },
            "statusUpdateInterval": "SECONDS_60",
            "priority": 0,
            "accelerationStatus": "NOT_APPLICABLE",
            "messages": {
                "info": [],
                "warning": []
            },
            "clientRequestToken": "1712252705233-abcDEF"
        }
    },
    "requestID": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "eventID": "0987dcba-09fe-87dc-65ba-ab0987654321",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

**Example event: CreateQueue**

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AKIAIOSFODNN7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/testuser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "testUser",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2018-07-10T14:01:57Z"
            }
        },
        "invokedBy": "signin.amazonaws.com"
    },
    "eventTime": "2018-07-10T16:49:13Z",
    "eventSource": "mediaconvert.amazonaws.com",
    "eventName": "CreateQueue",
    "awsRegion": "eu-west-1",
    "sourceIPAddress": "203.0.113.100",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "requestParameters": {
        "name": "QueueName",
        "description": "Example queue description.",
        "tags": {}
    },
    "responseElements": {
        "queue": {
            "arn": "arn:aws:mediaconvert:eu-west-1:111122223333:queues/QueueName",
            "createdAt": 1531241353,
            "lastUpdated": 1531241353,
            "type": "CUSTOM",
            "status": "ACTIVE",
            "description": "",
            "name": "QueueName",
            "submittedJobsCount": 0,
            "progressingJobsCount": 0
        }
    },
    "requestID": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "eventID": "0987dcba-09fe-87dc-65ba-ab0987654321",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

**Example event: DeleteQueue**

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AKIAIOSFODNN7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/testuser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "testuser",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2018-07-10T14:01:57Z"
            }
        },
        "invokedBy": "signin.amazonaws.com"
    },
    "eventTime": "2018-07-10T15:36:29Z",
    "eventSource": "mediaconvert.amazonaws.com",
    "eventName": "DeleteQueue",
    "awsRegion": "eu-west-1",
    "sourceIPAddress": "203.0.113.100",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "requestParameters": {
        "name": "QueueName"
    },
    "responseElements": null,
    "requestID": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "eventID": "0987dcba-09fe-87dc-65ba-ab0987654321",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

**Example event: TagResource**

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AKIAIOSFODNN7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/testuser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "testuser"
    },
    "eventTime": "2018-07-10T18:44:27Z",
    "eventSource": "mediaconvert.amazonaws.com",
    "eventName": "TagResource",
    "awsRegion": "eu-west-1",
    "sourceIPAddress": "203.0.113.100",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "requestParameters": {
        "arn": "arn:aws:mediaconvert:eu-west-1:111122223333:queues/ExampleQueue",
        "Tags": {
            "CostCenter": "Example-Tag"
        }
    },
    "responseElements": null,
    "requestID": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "eventID": "0987dcba-09fe-87dc-65ba-ab0987654321",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```
