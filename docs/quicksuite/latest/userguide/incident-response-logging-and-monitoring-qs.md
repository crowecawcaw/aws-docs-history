# Incident response,

logging, and monitoring in Amazon Quick Sight using CloudTrail

Amazon Quick Sight is integrated with AWS CloudTrail. This service provides a record of actions taken
by a user, role, or an AWS service in Amazon Quick Sight. CloudTrail captures all API calls for Amazon Quick Sight
as events. The calls captured include some calls from the Amazon Quick Sight console and all code
calls to Amazon Quick Sight API operations. If you create a trail, you can enable continuous
delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon Quick Sight. If you don't
configure a trail, you can still view the most recent events in the CloudTrail console in
**Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to Amazon Quick Sight, the IP address from which the request
was made, who made the request, when it was made, and additional details.

Amazon Quick Sight doesn’t natively support alerting with Amazon CloudWatch or other external systems.
However, it's possible to develop a custom solution to process CloudTrail logs.

Amazon Quick Sight service status can be viewed on the [Service Health Dashboard](https://status.aws.amazon.com/ "https://status.aws.amazon.com/").

By default, the log files delivered by CloudTrail to your bucket are encrypted by
Amazon [server-side encryption with Amazon S3-managed encryption keys (SSE-S3)](../../../AmazonS3/latest/dev/UsingServerSideEncryption.md "../../../AmazonS3/latest/dev/UsingServerSideEncryption.md"). To
provide a security layer that is directly manageable, you can instead use [server-side encryption with AWS KMS–managed keys (SSE-KMS)](../../../AmazonS3/latest/dev/UsingKMSEncryption.md "../../../AmazonS3/latest/dev/UsingKMSEncryption.md") for your
CloudTrail log files. Enabling server-side encryption encrypts the log files but not the
digest files with SSE-KMS. Digest files are encrypted with [Amazon S3-managed encryption keys (SSE-S3)](../../../AmazonS3/latest/dev/UsingServerSideEncryption.md "../../../AmazonS3/latest/dev/UsingServerSideEncryption.md").

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Logging Amazon Quick Sight information with
  AWS CloudTrail](#logging-using-cloudtrail "#logging-using-cloudtrail")
- [Tracking non-API events by using CloudTrail logs](#logging-non-api "#logging-non-api")
- [Example: Amazon Quick Sight log file
  entries](#understanding-quicksight-entries "#understanding-quicksight-entries")

## Logging Amazon Quick Sight information with

AWS CloudTrail

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

CloudTrail is enabled on your AWS account when you create the account. When supported
event activity occurs in Amazon Quick Sight, that activity is recorded in a CloudTrail event along
with other AWS service events in **Event history**. You can view,
search, and download recent events in your AWS account. For more information, see
[Viewing Events with CloudTrail
Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
Amazon Quick Sight, create a trail. A _trail_ enables CloudTrail to deliver log
files to an Amazon S3 bucket. By default, when you create a trail in the console, the
trail applies to all AWS Regions. The trail logs events from all Regions in the
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

Amazon Quick Sight supports logging the following actions as events in CloudTrail log files:

- Whether the request was made with root or AWS Identity and Access Management user
  credentials
- Whether the request was made with temporary security credentials for an
  IAM role or federated user
- Whether the request was made by another AWS service

For more information on user identity, see the [CloudTrail
userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

By default, each Amazon Quick Sight log entry contains the following information:

- userIdentity – User identity
- eventTime – Event time
- eventId – Event Id
- readOnly – Read only
- awsRegion – AWS Region
- eventSource (quicksight) – Source of
  the event (Amazon Quick Sight)
- eventType (AwsServiceEvent) – Event
  type (AWS service event)
- recipientAccountId (customer AWS account)
  – Recipient account ID (Customer AWS account)

###### Note

CloudTrail displays users as `unknown` if they were provisioned by
Amazon Quick Sight. This display is because these users aren't a known IAM identity type.

## Tracking non-API events by using CloudTrail logs

Following is a list of the non-API events you can track.

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

## Example: Amazon Quick Sight log file

entries

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
   "eventVersion":"1.05",
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
