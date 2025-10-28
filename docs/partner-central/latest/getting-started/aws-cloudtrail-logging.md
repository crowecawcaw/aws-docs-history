# Logging AWS Partner Central API calls with AWS CloudTrail

AWS Partner Central is integrated with [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/"), a service that provides a record of actions taken by a user, role, or an AWS service in AWS Partner Central. CloudTrail captures calls from the AWS Partner Central console and code calls to the AWS Partner Central API operations as events.

CloudTrail is active in your AWS account when you create it and doesn't require any manual setup. Supported event activity in AWS Partner Central is recorded in a CloudTrail event, along with other AWS service events, on the **Event history** page of the [CloudTrail console](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/"). There you can view, search, and download events in your AWS account.

Every event or log entry contains the identity of the user who generated the request. This information helps you determine if the request was made by any of the following:

- A user with root or AWS Identity and Access Management user credentials.
- A user with temporary security credentials for a role, or a federated user.
- Another AWS service.
  AWS Partner Central supports logging the `partnerCentralAccountManagement` operation as events in CloudTrail log files with `eventSource` `partnercentral-account-management.amazonaws.com`

###### Topics

- [AWS Partner Central log file entry examples](#entry-examples "#entry-examples")
- [Related topics](#logging-related-topics "#logging-related-topics")

## AWS Partner Central log file entry examples

**Example: `AssociatePartnerAccount`**

```
{
   "eventVersion":"1.08",
   "userIdentity":{
      "type":"IAMUser",
      "principalId":"EX_PRINCIPAL_ID",
      "arn":"arn:aws:iam::123456789012:user/Alice",
      "accountId":"123456789012",
      "accessKeyId":"EXAMPLE_KEY_ID",
      "userName":"Alice"
   },
   "eventTime":"2023-10-11T20:57:35Z",
   "eventSource":"partnercentral-account-management.amazonaws.com",
   "eventName":"AssociatePartnerAccount",
   "awsRegion":"us-east-1",
   "sourceIPAddress":"192.0.0.2/24",
   "userAgent":"Mozilla/5.0",
   "requestParameters":{
      "value":"HIDDEN_DUE_TO_SECURITY_REASONS"
   },
   "responseElements":null,
   "requestID":"F9PAD7MAYFGV73S4T7B3",
   "eventID":"fe2a5873-773c-462a-b7c8-810d224de821",
   "readOnly":false,
   "eventType":"AwsApiCall",
   "managementEvent":true,
   "recipientAccountId":"123456789012",
   "eventCategory":"Management"
}

```

**Example: `DisassociatePartnerUser`**

```
{
   "eventVersion":"1.09",
   "userIdentity":{
      "type":"AssumedRole",
      "principalId":"EX_PRINCIPAL_ID",
      "arn":"arn:aws:iam::123456789012:role/PartnerCentralRoleForCloudAdmin-1234",
      "accountId":"123456789012",
      "accessKeyId":"EXAMPLE_KEY_ID",
      "invokedBy":"partnercentral-account-management.amazonaws.com"
   },
   "eventTime":"2023-10-11T20:57:35Z",
   "eventSource":"partnercentral-account-management.amazonaws.com",
   "eventName":"AssociatePartnerUser",
   "awsRegion":"us-east-1",
   "sourceIPAddress":"partnercentral-account-management.amazonaws.com",
   "userAgent":"partnercentral-account-management.amazonaws.com",
   "requestParameters":{
      "partnerUserId":"005123456789012345",
      "iamRoleArn":"arn:aws:iam::123456789012:role/PartnerCentralRoleForUser-1234",
      "partnerAccountId":"1234567"
   },
   "responseElements":null,
   "requestID":"655832a6-8452-4088-9a0f-17212fa55765",
   "eventID":"f7394769-4a3b-4101-9b00-ee0b86a77d89",
   "readOnly":false,
   "eventType":"AwsApiCall",
   "managementEvent":true,
   "recipientAccountId":"123456789012",
   "eventCategory":"Management"
}

```

## Related topics

For more information, refer to the following sections in the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md"):

- [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [AWS service integrations with CloudTrail logs](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md")
