# Logging IAM Roles Anywhere API calls using AWS CloudTrail

AWS Identity and Access Management Roles Anywhere is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in IAM Roles Anywhere. CloudTrail captures all API calls for
IAM Roles Anywhere as events. The calls captured include calls from the IAM Roles Anywhere console and
code calls to the IAM Roles Anywhere API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for IAM Roles Anywhere. If
you don't configure a trail, you can still view the most recent events in the CloudTrail console
in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to IAM Roles Anywhere, the IP address from which the request
was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## IAM Roles Anywhere information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs
in IAM Roles Anywhere, that activity is recorded in a CloudTrail event along with other AWS service events
in **Event history**. You can view, search, and download recent events in
your AWS account. For more information, see [Viewing events with CloudTrail Event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for IAM Roles Anywhere,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket.
By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail
logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket
that you specify. Additionally, you can configure other AWS services to further analyze and act
upon the event data collected in CloudTrail logs. For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications
  for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log
  files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log
  files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All IAM Roles Anywhere actions are logged by CloudTrail and are documented in the [IAM Roles Anywhere API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md"). For
example, calls to the
`CreateTrustAnchor`, `ListProfiles`, and `CreateSession`
operations generate entries in the CloudTrail log files. In addition, the userIdentity element's Role Session Name property is the
hex-encoded serial number of the certificate the session was created with and can be used to track a session back to it.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding IAM Roles Anywhere log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the
`UpdateProfile` operation.

```
{
  "eventVersion": "1.08",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAZR5EMTJKE753U4ZDS:test-session",
    "arn": "arn:aws:sts::111122223333:assumed-role/Admin/test-session",
    "accountId": "111122223333",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAZR5EMTJKE753U4ZDS",
        "arn": "arn:aws:iam::111122223333:role/Admin",
        "accountId": "111122223333",
        "userName": "Admin"
      },
      "webIdFederationData": {},
      "attributes": {
        "creationDate": "2022-03-21T22:40:46Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2022-07-01T18:11:27Z",
  "eventSource": "rolesanywhere.amazonaws.com",
  "eventName": "UpdateProfile",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "1.1.1.1",
  "userAgent": "test-agent",
  "requestParameters": {
    "durationSeconds": 3600,
    "managedPolicyArns": [
        "arn:aws:iam::aws:policy/AdministratorAccess",
        "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
    ],
    "name": "Updated Test Profile",
    "profileId": "0ace5b12-24b9-427e-a483-c55884852fbf",
    "sessionPolicy": "{\n  \"Version\":\"2012-10-17\",\n  \"Statement\":[\n    {\n      \"Effect\":\"Allow\",\n      \"Action\":\"s3:ListObjects\",\n      \"Resource\":\"*\"\n    }\n  ]\n}\n"
},
"responseElements": {
  "profile": {
      "createdAt": "2022-07-01T18:11:27.380711Z",
      "createdBy": "arn:aws:sts::111122223333:assumed-role/Admin/test-session",
      "durationSeconds": 3600,
      "enabled": false,
      "managedPolicyArns": [
          "arn:aws:iam::aws:policy/AdministratorAccess",
          "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
      ],
      "name": "Updated Test Profile",
      "profileArn": "arn:aws:rolesanywhere:us-east-1:111122223333:profile/0ace5b12-24b9-427e-a483-c55884852fbf",
      "profileId": "0ace5b12-24b9-427e-a483-c55884852fbf",
      "requireInstanceProperties": false,
      "roleArns": [
          "arn:aws:iam::111122223333:role/test-role"
      ],
      "sessionPolicy": "{\n  \"Version\":\"2012-10-17\",\n  \"Statement\":[\n    {\n      \"Effect\":\"Allow\",\n      \"Action\":\"s3:ListObjects\",\n      \"Resource\":\"*\"\n    }\n  ]\n}\n",
      "updatedAt": "2022-07-01T18:11:27.936687Z"
  }
},
  "requestID": "ca28860f-504a-4f2d-9f3f-f9cfb4ba0491",
  "eventID": "a7bb90c3-c47b-4832-88e7-aeaccda21f1a",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "clientProvidedHostHeader": "rolesanywhere.us-east-1.amazonaws.com"
  }
}
```
