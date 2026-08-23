# Monitoring Amazon Quick using CloudTrail

Amazon Quick is integrated with AWS CloudTrail. This service provides a record of actions
taken by a user, role, or an AWS service in Amazon Quick. CloudTrail captures API calls for
Amazon Quick as events. The calls captured include some calls from the
console and all code calls to API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for
Amazon Quick. If you don't configure a trail, you can still view the most recent events
in the CloudTrail console in **Event history**. Using the information
collected by CloudTrail, you can determine who made a request to Amazon Quick and when.
You can also identify the source IP address, the specific request, and other
details.

###### Note

CloudTrail records supported Amazon Quick API operations and the non-API
events documented on this page. When you examine event samples, event records
include selected metadata such as account ID, resource ID, and user identity.
For chat conversations and feedback, use [Monitoring Amazon Quick using CloudWatch Logs](monitoring-cloudwatch-logs.md "monitoring-cloudwatch-logs.md"). For the full
signal-by-capability model, see [Incident response, logging, and monitoring in Amazon Quick](incident-response-logging-and-monitoring.md "incident-response-logging-and-monitoring.md").

Amazon Quick publishes operational metrics to CloudWatch, and you can create CloudWatch alarms
on those metrics. For more information, see [Creating alarms with the Amazon CloudWatch console](monitoring-cloudwatch-metrics.md#cw-alerts "monitoring-cloudwatch-metrics.md#cw-alerts"). To alert on individual CloudTrail events, you can develop a
custom solution that processes CloudTrail logs.

Amazon Quick service status can be viewed on the [Service Health Dashboard](https://status.aws.amazon.com/ "https://status.aws.amazon.com/").

By default, CloudTrail encrypts the log files it delivers to your bucket using
[Amazon S3-managed encryption keys (SSE-S3)](../../../AmazonS3/latest/dev/UsingServerSideEncryption.md "../../../AmazonS3/latest/dev/UsingServerSideEncryption.md"). For a directly manageable
security layer, you can instead use [AWS KMS–managed keys (SSE-KMS)](../../../AmazonS3/latest/dev/UsingKMSEncryption.md "../../../AmazonS3/latest/dev/UsingKMSEncryption.md") for your
CloudTrail log files. SSE-KMS encrypts the log files but not the
digest files. Digest files are encrypted with [Amazon S3-managed encryption keys (SSE-S3)](../../../AmazonS3/latest/dev/UsingServerSideEncryption.md "../../../AmazonS3/latest/dev/UsingServerSideEncryption.md").

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Logging Amazon Quick operations with AWS CloudTrail](#logging-using-cloudtrail "#logging-using-cloudtrail")
- [Discovering Amazon Quick events in your trail](#logging-discovering-events "#logging-discovering-events")
- [Example: Amazon Quick log file entries](#understanding-quicksight-entries "#understanding-quicksight-entries")
- [Logging Amazon Quick data events in CloudTrail](#logging-data-events "#logging-data-events")
- [Tracking non-API events by using CloudTrail logs](#logging-non-api "#logging-non-api")

## Logging Amazon Quick operations with AWS CloudTrail

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

CloudTrail is enabled on your AWS account when you create the account. When supported
event activity occurs in Amazon Quick, that activity is recorded in a CloudTrail event along
with other AWS service events in **Event history**. You can view,
search, and download recent events in your AWS account. For more information, see
[Viewing Events with CloudTrail
Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
Amazon Quick, create a trail. A _trail_ enables CloudTrail to deliver log
files to an Amazon S3 bucket. By default, when you create a trail in the console, the
trail applies to all . The trail logs events from all Regions in the
AWS partition and delivers the log files to the Amazon S3 bucket that you specify.
Additionally, you can configure other AWS services to further analyze and act upon
the event data collected in CloudTrail logs. For more information, see the following:

- [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")
- [Cross-Account CloudTrail
  Logging](../../../lake-formation/latest/dg/cross-account-logging.md "../../../lake-formation/latest/dg/cross-account-logging.md") in the AWS Lake Formation Developer Guide Guide – This topic includes
  instructions for including principal identities in cross-account CloudTrail
  logs.

Amazon Quick supports logging the following actions as events in CloudTrail log files:

- Whether the request was made with root or AWS Identity and Access Management user
  credentials
- Whether the request was made with temporary security credentials for an
  IAM role or federated user
- Whether the request was made by another AWS service

For more information on user identity, see the [CloudTrail
userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

By default, each Amazon Quick log entry contains the following information:

- userIdentity – User identity
- eventTime – Event time
- eventID – Event ID
- readOnly – Read only
- awsRegion – AWS Region
- eventSource (quicksight) – Source of
  the event (Amazon Quick)
- eventType (AwsServiceEvent) – Event
  type (AWS service event)
- recipientAccountId (customer AWS account)
  – Recipient account ID (Customer AWS account)

Some events include a `userIdentity.invokedBy` field set to
`quicksight.amazonaws.com`. This indicates that the event was triggered
by the Amazon Quick service on behalf of the account rather than by a direct user action.
You can use this field to distinguish user-initiated operations from
service-internal calls when analyzing your trail.

###### Note

CloudTrail displays the user identity as `unknown` for users that were
provisioned directly by Amazon Quick (legacy provisioning). Users authenticated
through IAM Identity Center appear as `IdentityCenterUser` with full
`onBehalfOf` details in the `userIdentity` element.

## Discovering Amazon Quick events in your trail

Amazon Quick adds new event names as features launch and evolve. The non-API
events listed below represent a subset of what your trail captures. To discover
all Amazon Quick events in your account, query your trail for
`eventSource: quicksight.amazonaws.com` and inspect the
`eventName` values. Event names follow a consistent pattern: the
operation name (such as `CreateFlow` or `UpdateAgent`)
matches the feature it relates to.

## Example: Amazon Quick log file entries

A trail is a configuration that enables delivery of events as log files to an
Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An
event represents a single request from any source and includes information about the
requested action, the date and time of the action, request parameters, and so on.
CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't
appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the BatchCreateUser
action.

```
{
   "eventVersion":"1.11",
   "userIdentity":
	{
	   "type":"Root",
	   "principalId":"123456789012",
	   "arn":"arn:aws:iam::123456789012:root",
	   "accountId":"123456789012",
	   "userName":"test-username"
	},
	   "eventTime":"2017-04-19T03:16:13Z",
	   "eventSource":"quicksight.amazonaws.com",
	   "eventName":"BatchCreateUser",
	   "awsRegion":"us-west-2",
	   "requestParameters":null,
	   "responseElements":null,
	   "eventID":"e7d2382e-70a0-3fb7-9d41-a7a913422240",
	   "readOnly":false,
	   "eventType":"AwsServiceEvent",
	   "recipientAccountId":"123456789012",
	   "serviceEventDetails":
	   {
		   "eventRequestDetails":
		   {
				"users":
				{
					"test-user-11":
					{
						"role":"USER"
					},
					"test-user-22":
					{
						"role":"ADMIN"
					}
				}
			},
			"eventResponseDetails":
			{
			"validUsers":[
				],
			"InvalidUsers":[
				"test-user-11",
				"test-user-22"
				]
			}
	   }
   }

```

## Logging Amazon Quick data events in CloudTrail

In addition to management events, Amazon Quick supports CloudTrail data events for
selected resource types. Data events are off by default. Enable them through
advanced event selectors on your trail.

The following Amazon Quick resource types support data events:

| Resource type                      | Event name     | Availability        |
| ---------------------------------- | -------------- | ------------------- |
| `AWS::Quicksight::ActionConnector` | `InvokeAction` | Generally available |
| `AWS::QuickSight::Flow`            | –              | Generally available |
| `AWS::QuickSight::FlowSession`     | –              | Generally available |
| `AWS::Quicksight::Companion`       | –              | Varies by Region    |
| `AWS::Quicksight::CompanionAccess` | –              | Varies by Region    |
| `AWS::QuickSight::Namespace`       | –              | Varies by Region    |

###### Important

Data-event resource-type availability varies by account and AWS Region. If
a resource type is not supported in your Region, the
`put-event-selectors` call returns an error for that type. Build
one `put-event-selectors` call that includes only the resource
types supported in your Region, and omit unsupported types from that
call.

###### Note

The casing of `Quicksight` compared with `QuickSight` in
resource type ARNs is intentional and varies by resource type. Use the exact
casing shown above when configuring event selectors.

### Enabling data events

Use advanced event selectors to enable data events. Include a
management-events selector to retain management event logging:

```
aws cloudtrail put-event-selectors \
  --trail-name `your-trail-name` \
  --region `us-east-1` \
  --advanced-event-selectors '[
    { "Name": "All management events",
      "FieldSelectors": [ { "Field": "eventCategory", "Equals": ["Management"] } ] },
    { "Name": "Quick action connector data events",
      "FieldSelectors": [
        { "Field": "eventCategory", "Equals": ["Data"] },
        { "Field": "resources.type", "Equals": ["AWS::Quicksight::ActionConnector"] } ] },
    { "Name": "Quick flow data events",
      "FieldSelectors": [
        { "Field": "eventCategory", "Equals": ["Data"] },
        { "Field": "resources.type", "Equals": ["AWS::QuickSight::Flow"] } ] },
    { "Name": "Quick flow session data events",
      "FieldSelectors": [
        { "Field": "eventCategory", "Equals": ["Data"] },
        { "Field": "resources.type", "Equals": ["AWS::QuickSight::FlowSession"] } ] }
  ]'
```

Add selectors for `AWS::Quicksight::Companion`,
`AWS::Quicksight::CompanionAccess`, and
`AWS::QuickSight::Namespace` if supported in your Region.

### `InvokeAction` data event

When a user or flow invokes an action connector, CloudTrail records an
`InvokeAction` data event. This event captures the following
information:

- Caller identity, including `onBehalfOf.userId` and
  `endUserArn`
- The `actionConnectorId` and `actionId` of the
  invoked action
- The outcome: `invokeActionStatus` and
  `httpStatusCode`
- `readOnly: false` (always)
- `eventCategory: Data`,
  `managementEvent: false`
- Resource type:
  `AWS::Quicksight::ActionConnector`

###### Important

`InvokeAction` does not include the action's input parameters
(such as an email recipient, subject, or body) or any approval decision.
Use CloudWatch vended logs for conversation content.

###### Note

The `readOnly` field is always `false` for action
connector invocations, including read-only actions such as listing emails.
To distinguish read from write operations, filter by
`actionId` rather than the `readOnly` field.

The following example shows an `InvokeAction` data event
for a successful email action:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "IdentityCenterUser",
        "accountId": "111122223333",
        "onBehalfOf": {
            "userId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "identityStoreArn": "arn:aws:identitystore::111122223333:identitystore/d-1234567890"
        }
    },
    "eventTime": "2026-08-19T20:26:36Z",
    "eventSource": "quicksight.amazonaws.com",
    "eventName": "InvokeAction",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "203.0.113.1",
    "requestParameters": {
        "awsAccountId": "111122223333",
        "actionConnectorId": "52bde8f0-3de5-4e3d-9283-222f81a9fc4f",
        "actionId": "SendUserEmail",
        "endUserArn": "arn:aws:quicksight:us-east-1:111122223333:user/default/johndoe"
    },
    "responseElements": {
        "invokeActionStatus": "SUCCESS",
        "invokeActionOutput": {
            "httpInvokeActionOutput": {
                "httpStatusCode": "200"
            }
        }
    },
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::Quicksight::ActionConnector",
            "ARN": "arn:aws:quicksight:us-east-1:111122223333:action-connector/52bde8f0-3de5-4e3d-9283-222f81a9fc4f"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": false,
    "eventCategory": "Data"
}
```

## Tracking non-API events by using CloudTrail logs

The following non-API events are captured in your CloudTrail trail:

###### User management

- CreateAccount – Create Account
- BatchCreateUser – Create User
- BatchResendUserInvite – Invite
  User
- UpdateGroups – Update Groups

This event works with Enterprise edition only.

- UpdateSpiceCapacity – Update
  SPICE Capacity
- DeleteUser – Delete User
- Unsubscribe – Unsubscribe
  User

###### Subscription

- CreateSubscription – Create
  Subscription
- UpdateSubscription – Update
  Subscription
- DeleteSubscription – Delete
  Subscription

###### Dashboard

- GetDashboard – Get Dashboard
- CreateDashboard – Create
  Dashboard
- UpdateDashboard – Update
  Dashboard
- UpdateDashboardAccess – Update
  Dashboard Access
- DeleteDashboard – Delete
  Dashboard

###### Analysis

- GetAnalysis – Get Analysis
- CreateAnalysis – Create
  Analysis
- UpdateAnalysisAccess – Update
  Analysis Access
- UpdateAnalysis – Update
  Analysis

  - RenameAnalysis – Rename
    Analysis
  - CreateVisual – Create
    Visual
  - RenameVisual – Rename
    Visual
  - DeleteVisual – Delete
    Visual
  - DeleteAnalysis – Delete
    Analysis

###### Data source

- CreateDataSource – Create Data
  Source

  - FlatFile – Flat file
  - External – External
  - S3 – S3
  - ImportS3ManifestFile – S3
    Manifest File
  - Presto – Presto
  - RDS – RDS
  - Redshift – Redshift
    (manual)

- UpdateDataSource – Update Data
  Source
- DeleteDataSource – Delete Data
  Source

###### Data set

- CreateDataSet – Create Data Set

  - CustomSQL – Custom
    SQL
  - SQLTable – SQL Table
  - File – CSV or XLSX

- UpdateDataSet – Update SQL Join
  Dataset
- UpdateDatasetAccess – Update Dataset
  Access
- DeleteDataSet – Delete
  Dataset
- Querydatabase – During a dataset
  refresh, query data source.
