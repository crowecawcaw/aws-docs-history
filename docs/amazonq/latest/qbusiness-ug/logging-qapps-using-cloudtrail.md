# Logging Amazon Q Apps API calls using

AWS CloudTrail

Amazon Q Apps is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in Amazon Q Apps. CloudTrail captures all API calls for
Amazon Q Apps as events. The calls captured include calls from theAmazon Q Apps web experience,
console and code calls to theAmazon Q Apps API operations.

A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. If you create a trail,
you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for
Amazon Q Apps. If you don't configure a trail, you can still view the most recent events in
the CloudTrail console in **Event history**. Using the information collected by
CloudTrail, you can determine the request that was made to Amazon Q Apps, the IP address from which
the request was made, who made the request, when it was made, and additional details.

For more information about CloudTrail, including how to configure and activate it, see the
[_AWS CloudTrail User
Guide_](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Amazon Q Apps information in CloudTrail

CloudTrail is activated on your AWS account when you create the account. When activity
occurs in Amazon Q Apps, that activity is recorded in a CloudTrail event along with other AWS
service events in **Event history** in the CloudTrail console. You can view,
search, and download recent events in your AWS account. For more information, see
[Viewing events with
CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_.

For an ongoing record of events in your AWS account, including events for
Amazon Q Apps, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all
AWS regions. The trail logs events from all Regions in the AWS partition and
delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can
configure other AWS services to further analyze and act upon the event data collected
in CloudTrail logs. For more information, see the following topics:

- [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

## Management events

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are
performed on resources in your AWS account. These management events are also known as
control plane operations. CloudTrail logs management event API operations by default.

CloudTrail supports logging the followingAmazon Q Apps actions:

- `CreateLibraryItem`
- `UpdateLibraryItem`
- `DeleteLibraryItem`
- `GetLibraryItem`
- `ListLibraryItems`
- `TagResource`
- `UntagResource`
- `ListTagsForResource`

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user
  credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md") in the _AWS CloudTrail User
Guide_.

## Data events

[Data
events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") provide visibility into the resource operations performed on or
within a resource. These are also known as data plane operations. Data events are often
high-volume activities. By default, CloudTrail doesn't log data events.

The following table shows theAmazon Q Apps API operations logged to CloudTrail as data events.
The **Data event type (console)** column shows the appropriate
selection in the CloudTrail console. The **Amazon Q Apps resource types
column** shows the `resources.type` value that you would specify
to log data events for the resource.

| Data event type (console)     | Amazon Q Apps resource types  | Supported data events                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Q Apps                 | `AWS::QApps::QApp`            | <br>• `CreateQApp` <br>• `CopyQApp` <br>• `UpdateQApp` <br>• `DeleteQApp` <br>• `AssociateQAppWithUser` <br>• `DisassociateQAppFromUser` <br>• `ImportDocumentToQApp` <br>• `ImportDocumentToQAppSession` <br>• `CreateLibraryItemReview` <br>• `StartQAppSession` <br>• `StopQAppSession` <br>• `GetQApp` <br>• `ListQApps` <br>• `ImportDocument` <br>• `GetQAppSession` <br>• `UpdateQAppSession` <br>• `AssociateLibraryItemReview` <br>• `DisassociateLibraryItemReview` |
| Amazon Q Business application | `AWS::QBusiness::Application` | <br>• `CreateSubscriptionToken` <br>• `PredictProblemStatementFromConversation` <br>• `PredictQAppFromProblemStatement` <br>• `PredictQApp`                                                                                                                                                                                                                                                                                                                                   | You can log these API operations by configuring advanced event selectors to record data events for theAmazon Q Apps resource types: `AWS::QApps::QApp` and `AWS::QBusiness::Application`. To configure advanced event selectors, you can use either the CloudTrail console or the AWS CLI: <br>• From the CloudTrail console, choose the **Data event type** for which you want to log data events. Additionally, you can filter on the `eventName` and `resources.ARN` fields by choosing a custom log selector template. For more information, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") in the _AWS CloudTrail User Guide_. <br>• From the AWS CLI, specify the `resources.type` value for which you want to log data events and set the `eventCategory` equal to `Data`. For more information, see [Logging data events with the AWS CLI](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI") in the _AWS CloudTrail User Guide_. The following example shows how to configure a trail to log allAmazon Q Apps data events for allAmazon Q Apps resource types. `aws cloudtrail put-event-selectors --trail-name trailName \ --advanced-event-selectors \ '[ { "Name": "Log all data events on anAmazon Q Apps", "FieldSelectors": [ { "Field": "eventCategory", "Equals": ["Data"] }, { "Field": "resources.type", "Equals": ["AWS::QApps::QApp"] } ] } ]'` You can additionally filter on the `eventName` and `resources.ARN` fields. For more information about configuring these fields, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") in the _AWS CloudTrail API Reference_. ###### Note Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). ## UnderstandingAmazon Q Apps log file entries A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the API calls, so they don't appear in any specific order. The following example shows a CloudTrail log entry that demonstrates the `GetLibraryItem` action. `{ "eventVersion": "1.09", "userIdentity": { "type": "AssumedRole", "principalId": "principal ID", "arn": "ARN", "accountId": "account ID", "accessKeyId": "access key ID", "sessionContext": { "sessionIssuer": { "type": "Role", "principalId": "principal ID", "arn": "ARN", "accountId": "account ID", "userName": "user name" }, "attributes": { "creationDate": "yyyy-mm-ddThh:mm:ssZ", "mfaAuthenticated": "false" } }, "onBehalfOf": { "userId": "user ID", "identityStoreArn": "ARN" } }, "eventTime": "yyyy-mm-ddThh:mm:ssZ", "eventSource": "qapps.amazonaws.com", "eventName": "GetLibraryItem", "awsRegion": "region", "sourceIPAddress": "source IP address", "userAgent": "user agent", "requestParameters": { "input": "query input", "idc-application-arn": "ARN", "application-id": "Q application ID" }, "requestID": "request ID", "eventID": "event ID", "readOnly": true, "eventType": "AwsApiCall", "managementEvent": true, "recipientAccountId": "account ID", "eventCategory": "Management" }` |
