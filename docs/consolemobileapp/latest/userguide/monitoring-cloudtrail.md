# Logging DeviceIdentity API calls in AWS CloudTrail

Mobile devices using the Console Mobile Application can be configured as delivery channels for AWS User Notifications. This is done using the ListDeviceIdentities and GetDeviceIdentity APIs. These APIs are integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service on these APIs. CloudTrail captures API calls for ListDeviceIdentities and GetDeviceIdentity as events. The calls captured include calls from the the User Notifications console and code calls to the aforementioned API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for ListDeviceIdentities and GetDeviceIdentity. If you don’t configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to ListDeviceIdentities and GetDeviceIdentity, the IP address from which the request was made, who made the request, when it was made, and additional details. For more information, see
[Viewing Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

## DeviceIdentity API information in CloudTrail

The DeviceIdentity APIs support logging of the following actions as events in CloudTrail log files:

- ListDeviceIdentities
- GetDeviceIdentity

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding the Console Mobile Application log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren’t an ordered stack trace of the public API calls, so they don’t appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `ListDeviceIdentities` action.

```
 {
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE:jdoe",
        "arn": "arn:aws:sts::111122223333:assumed-role/user/jdoe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::111111112222:role/Admin",
                "accountId": "111111112222",
                "userName": "jdoe"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2022-10-24T04:13:00Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2022-10-24T04:13:35Z",
    "eventSource": "consoleapp.amazonaws.com",
    "eventName": "ListDeviceIdentities",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "10.24.34.3",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "requestParameters": {
        "maxResults": "100"
    },
    "responseElements": null,
    "requestID": "0def12ce-3020-4981-9346-5b5deb71eabb",
    "eventID": "3b5d601f-d1ef-4985-9ddd-5207065faf41",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111111112222",
    "eventCategory": "Management"
}
```
