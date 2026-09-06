

# Monitoring AWS Support authorization with AWS CloudTrail
<a name="support-authorization-monitoring"></a>

AWS CloudTrail logs all AWS Support authorization API calls and support operations as management events. These events are logged by default without additional configuration.

## AWS service events
<a name="support-authorization-monitoring-service-events"></a>

When AWS Support performs operations related to your support permits, AWS CloudTrail delivers the following events as `AwsServiceEvent` types. The event source for all events is `supportauthz.amazonaws.com`.

### SupportPermitRequestCreated
<a name="support-authorization-monitoring-request"></a>

AWS CloudTrail logs this event when AWS Support requests access to your resources. It indicates that a support permit request was created.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "accountId": "111122223333",
        "invokedBy": "supportauthz.amazonaws.com"
    },
    "eventTime": "2026-06-16T20:04:51Z",
    "eventSource": "supportauthz.amazonaws.com",
    "eventName": "SupportPermitRequestCreated",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "supportauthz.amazonaws.com",
    "userAgent": "supportauthz.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::SupportAuthZ::SupportPermitRequest",
            "ARN": "arn:aws:supportauthz:us-east-1:111122223333:supportpermitrequest/e5f6a7b8-c9d0-1234-efab-345678901234"
        }
    ],
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "supportPermitRequestArn": "arn:aws:supportauthz:us-east-1:111122223333:supportpermitrequest/e5f6a7b8-c9d0-1234-efab-345678901234",
        "supportCaseDisplayId": "1234567890",
        "resources": ["arn:aws:example:us-east-1:111122223333:resourcetype/resource-id"],
        "actions": ["example:ExampleAction"]
    },
    "eventCategory": "Management"
}
```

### RetrieveSupportPermit
<a name="support-authorization-monitoring-get"></a>

AWS CloudTrail logs this event when AWS Support retrieves a signed authorization to perform a support action. This indicates that your AWS KMS key was used to sign the authorization.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "accountId": "111122223333",
        "invokedBy": "supportauthz.amazonaws.com"
    },
    "eventTime": "2026-06-16T20:22:42Z",
    "eventSource": "supportauthz.amazonaws.com",
    "eventName": "RetrieveSupportPermit",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "supportauthz.amazonaws.com",
    "userAgent": "supportauthz.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
    "readOnly": true,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "supportCaseDisplayId": "1234567890",
        "resource": "arn:aws:example:us-east-1:111122223333:resourcetype/resource-id",
        "action": "example:ExampleAction",
        "supportPermitArn": "arn:aws:supportauthz:us-east-1:111122223333:supportpermit/f6a7b8c9-d0e1-2345-fabc-456789012345"
    },
    "eventCategory": "Management"
}
```

### StartSupportAction
<a name="support-authorization-monitoring-execute"></a>

AWS CloudTrail logs this event when AWS Support performs an authorized action on your resources.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "accountId": "111122223333",
        "invokedBy": "supportauthz.amazonaws.com"
    },
    "eventTime": "2026-06-17T21:38:37Z",
    "eventSource": "supportauthz.amazonaws.com",
    "eventName": "StartSupportAction",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "supportauthz.amazonaws.com",
    "userAgent": "supportauthz.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "c3d4e5f6-a7b8-9012-cdef-123456789012",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::SupportAuthZ::SupportPermit",
            "ARN": "arn:aws:supportauthz:us-west-2:111122223333:supportpermit/example-permit"
        }
    ],
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "supportCaseDisplayId": "1234567890",
        "resourceIdentifiers": ["arn:aws:example:us-east-1:111122223333:resourcetype/resource-id"],
        "action": "example:ExampleAction",
        "supportPermitArn": "arn:aws:supportauthz:us-east-1:111122223333:supportpermit/f6a7b8c9-d0e1-2345-fabc-456789012345"
    },
    "eventCategory": "Management"
}
```

**Note**  
A single signed authorization can result in multiple `StartSupportAction` events. Each event represents one action performed on one resource. For example, if AWS Support reads diagnostic data from a cluster multiple times during a support case, each access generates a separate `StartSupportAction` event referencing the same `customerPermitArn`.

### CancelSupportPermitRequest
<a name="support-authorization-monitoring-cancel"></a>

AWS CloudTrail logs this event when AWS Support cancels a support permit request.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "accountId": "111122223333",
        "invokedBy": "supportauthz.amazonaws.com"
    },
    "eventTime": "2026-06-16T20:04:42Z",
    "eventSource": "supportauthz.amazonaws.com",
    "eventName": "CancelSupportPermitRequest",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "supportauthz.amazonaws.com",
    "userAgent": "supportauthz.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "d4e5f6a7-b8c9-0123-defa-234567890123",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::SupportAuthZ::SupportPermitRequest",
            "ARN": "arn:aws:supportauthz:us-east-1:111122223333:supportpermitrequest/a7b8c9d0-e1f2-3456-abcd-567890123456"
        }
    ],
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "supportPermitRequestArn": "arn:aws:supportauthz:us-east-1:111122223333:supportpermitrequest/a7b8c9d0-e1f2-3456-abcd-567890123456"
    },
    "eventCategory": "Management"
}
```

## API events
<a name="support-authorization-monitoring-customer-events"></a>

AWS CloudTrail also generates standard management events for your own API calls to AWS Support authorization, including `CreateSupportPermit`, `DeleteSupportPermit`, `GetSupportPermit`, `ListSupportPermits`, `ListSupportPermitRequests`, and `RejectSupportPermitRequest`.

## Setting up alerts
<a name="support-authorization-monitoring-alerts"></a>

You can create Amazon CloudWatch alarms based on AWS CloudTrail events to alert you when AWS Support requests access or performs actions on your resources. To set up alerts:

1. Create an AWS CloudTrail trail that delivers events to Amazon CloudWatch Logs.

1. Create a metric filter for the AWS CloudTrail log group that matches on `eventSource` value `supportauthz.amazonaws.com` and the desired `eventName` (for example, `SupportPermitRequestCreated` or `StartSupportAction`).

1. Create a CloudWatch alarm on the metric filter to notify you through Amazon SNS.

## Amazon EventBridge events
<a name="support-authorization-monitoring-eventbridge"></a>

Events are sent to Amazon EventBridge when a support permit request is created. You can use these events to automate responses, such as automatically creating a support permit for low-risk actions or notifying your security team for review.

The following is an example event for a new support permit request:

```
{
    "version": "0",
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "detail-type": "Support Permit Request Created",
    "source": "aws.supportauthz",
    "account": "111122223333",
    "time": "2026-06-01T12:00:00Z",
    "region": "us-east-1",
    "detail": {
        "requestArn": "arn:aws:supportauthz:us-east-1:111122223333:supportpermitrequest/req-1234abcd",
        "supportCaseDisplayId": "case-12345678",
        "requestedActions": ["rds:ReadClusterData"],
        "requestedResources": ["arn:aws:rds:us-east-1:111122223333:cluster:my-aurora-cluster"],
        "status": "PENDING"
    }
}
```

To create an Amazon EventBridge rule that matches support permit request events, use the following event pattern:

```
{
    "source": ["aws.supportauthz"],
    "detail-type": ["Support Permit Request Created"]
}
```

You can route these events to targets such as Lambda functions, Amazon SNS topics, or Amazon SQS queues to build automated approval workflows.