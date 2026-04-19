# Logging AWS User Experience Customization API calls using AWS CloudTrail

AWS User Experience Customization is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a service that provides a record of actions taken by a user, role, or an
AWS service. CloudTrail captures all
API calls for UXC as events. The calls captured include calls from the UXC console
and code calls to the UXC API operations. Using the information collected by CloudTrail, you can
determine the request that was made to UXC, the IP address from which the request was
made, when it was made, and additional details.

CloudTrail is active in your AWS account when you create the account and you automatically have
access to the CloudTrail **Event history**. The CloudTrail **Event
history** provides a viewable, searchable, downloadable, and immutable record of the
past 90 days of recorded management events in an AWS Region. For more information, see [Working
with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_. There are no CloudTrail
charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a
[CloudTrail
Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") event data store.

## UXC management events in CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

AWS User Experience Customization logs all UXC control plane operations as management events. For a list
of the AWS User Experience Customization control plane operations that UXC logs to CloudTrail, see the
[AWS User Experience Customization API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

## UXC event examples

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail event that demonstrates the
`GetAccountCustomizations` operation.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE:jdoe",
    "arn": "arn:aws:sts::111122223333:assumed-role/MyRole/jdoe",
    "accountId": "111122223333",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/MyRole",
        "accountId": "111122223333",
        "userName": "MyRole"
      },
      "attributes": {
        "creationDate": "2026-03-06T15:15:16Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-03-06T15:36:13Z",
  "eventSource": "uxc.amazonaws.com",
  "eventName": "GetAccountCustomizations",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "10.24.34.0",
  "userAgent": "aws-sdk-java/2.41.27",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "543db7ab-b4b2-11e9-8925-d139e92a1fe8",
  "eventID": "5b2805a5-3e06-4437-a7a2-b5fdb5cbb4e2",
  "readOnly": true,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::UXC::AccountCustomization",
      "ARN": "arn:aws:uxc::111122223333:account-customizations"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "111122223333",
  "eventCategory": "Data"
}
```

For information about CloudTrail record contents, see [CloudTrail
record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the _AWS CloudTrail User Guide_.
