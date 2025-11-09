Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Monitoring API calls by AWS accounts using AWS CloudTrail logging

Amazon CodeCatalyst is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service. CloudTrail captures API calls made on behalf of CodeCatalyst in
connected AWS accounts as events. If you create a trail, you can enable continuous
delivery of CloudTrail events to an S3 bucket, including events for CodeCatalyst. If you don't configure
a trail, you can still view the most recent events in the CloudTrail console in **Event
history**.

CodeCatalyst supports logging the following actions as events in CloudTrail log files:

- Management events for CodeCatalyst spaces will be logged in the AWS account that is
  the designated billing account for the space. For more information, see [CodeCatalyst space events](#cloudtrail-logs-spaces-projects "#cloudtrail-logs-spaces-projects").

###### Note

Data events for CodeCatalyst spaces are accessible by using the CLI as detailed in
[Accessing logged events using event logging](ipa-logs.md "ipa-logs.md").

- Events for resources that are used in CodeCatalyst workflow actions that occur in a
  connected AWS account will be logged as events in that AWS account. For more
  information, see [CodeCatalyst account connections and billing
  events](#cloudtrail-logs-connections "#cloudtrail-logs-connections").

###### Important

While multiple accounts can be associated with a space, CloudTrail logging for events
in CodeCatalyst spaces and projects apply only for the billing account.

The space billing account is your AWS account that is charged for CodeCatalyst resources
beyond the AWS
Free
tier. Multiple accounts can be connected to a space, while only one account can be the
designated billing account. The billing account or additional connected accounts for the
space can have IAM roles that are used for deploying AWS resources and
infrastructure, such as an Amazon ECS cluster or S3 bucket, from CodeCatalyst workflows. You can use
the workflow YAML to identify the AWS account that you deployed to.

###### Note

AWS resources that are deployed into connected accounts for CodeCatalyst workflows, are
not logged as part of CloudTrail logging for the CodeCatalyst space. For example, CodeCatalyst
resources include a space or project. AWS resources include an Amazon ECS service or
Lambda function. CloudTrail logging must be configured separately for each AWS account where
resources are deployed into.

CodeCatalyst logging in connected accounts includes the following considerations:

- Access to CloudTrail events is managed with IAM in the connected account and not in
  CodeCatalyst.
- Third-party connections, such as linking to a GitHub repository, will result in
  third-party resource names being recorded in CloudTrail logs.

###### Note

CloudTrail logging for CodeCatalyst events is at the space level and does not isolate events by
project boundaries.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

###### Note

This section describes CloudTrail logging for all events logged in a logged in a CodeCatalyst
space and the AWS accounts that are connected to CodeCatalyst. Additionally, to review
all events logged in a CodeCatalyst space, you can also use the AWS CLI and the
**aws codecatalyst list-event-logs** command. For more
information, see
[Accessing logged events using event logging](ipa-logs.md "ipa-logs.md").

## CodeCatalyst space events

Actions in CodeCatalyst for managing space-level and project-level resources are logged
in the billing account for the space. For CloudTrail logging for a CodeCatalyst space,
events are logged with the following considerations.

- CloudTrail events apply across the entire space and are not scoped to any
  single project.
- When you connect an AWS account to a CodeCatalyst space, loggable events for
  account connections will be logged in that AWS account. After you enable this
  connection, you cannot disable it.
- When you connect an AWS account to a CodeCatalyst space and designate it as
  the billing account for the space, events will be logged in that
  AWS account. After you enable this connection, you cannot disable it.

Events for space-level and project-level resources are logged only in the
billing account. To change the CloudTrail destination account, update the billing
account in CodeCatalyst. At the beginning of the next monthly billing cycle, the
change takes effect for the new billing account in CodeCatalyst. After that, the CloudTrail
destination account is updated.

The following are examples of events in AWS that are related to actions in CodeCatalyst
for managing space-level and project-level resources. The following APIs are
released through the SDK and CLI. Events will be logged in the AWS account specified
as the billing account for the CodeCatalyst space.

- `CreateDevEnvironment`
- `CreateProject`
- `DeleteDevEnvironment`
- `GetDevEnvironment`
- `GetProject`
- `GetSpace`
- `GetSubscription`
- `ListDevEnvironments`
- `ListDevEnvironmentSessions`
- `ListEventLogs`
- `ListProjects`
- `ListSourceRepositories`
- `StartDevEnvironment`
- `StartDevEnvironmentSession`
- `StopDevEnvironment`
- `StopDevEnvironmentSession`
- `UpdateDevEnvironment`

## CodeCatalyst account connections and billing

events

The following are examples of events in AWS that are related to actions in CodeCatalyst
for account connections or billing:

- `AcceptConnection`
- `AssociateIAMRoletoConnection`
- `DeleteConnection`
- `DissassociateIAMRolefromConnection`
- `GetBillingAuthorization`
- `GetConnection`
- `GetPendingConnection`
- `ListConnections`
- `ListIAMRolesforConnection`
- `PutBillingAuthorization`
- `RejectConnection`

## CodeCatalyst information in CloudTrail

CloudTrail is enabled on an AWS account when you create that account. When you connect
that AWS account to a CodeCatalyst space, events for that space that occur in that
AWS account are logged in CloudTrail logs
in
that AWS account.
Loggable
events in CodeCatalyst are recorded as CloudTrail events in CloudTrail logs in the connected account and
in **Event history** in the CloudTrail console, along with other loggable
AWS events in that account.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made by a user with their AWS Builder ID.
- Whether the request was made with root or AWS Identity and Access Management (IAM) user
  credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Accessing CloudTrail events

For an ongoing record of events in your AWS account, including events for CodeCatalyst
activity in the AWS account, create a trail. A _trail_ enables CloudTrail
to deliver log files to an S3 bucket. By default, when you create a trail in the
console, the trail applies to all AWS Regions. The trail logs events from all Regions
in the AWS partition and delivers the log files to the S3 bucket that you specify.
Additionally, you can configure other AWS services to further analyze and act upon the
event data collected in CloudTrail logs. For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications for
  CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
  and [Receiving CloudTrail log files from multiple
  accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

A trail is a configuration that enables delivery of events as log files to an S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event
represents a single request from any source and includes information about the requested
action, the date and time of the action, request parameters, and so on. CloudTrail log files
aren't an ordered stack trace of the public API calls, so they don't appear in any
specific order.

## Example CodeCatalyst account connections

event in AWS

The following example shows a CloudTrail log entry that demonstrates the
`ListConnections`

action. For an AWS account that is connected to the space,
`ListConnections` is used to view all account connections to CodeCatalyst for
this AWS account. The event will be logged in the AWS account specified in
`accountId`, and the value of the `arn` will be the Amazon
Resource Name (ARN) of the role used for the action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AKIAI44QH8DHBEXAMPLE",
        "arn": "`role-ARN`",
        "accountId": "`account-ID`",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AKIAI44QH8DHBEXAMPLE",
                "arn": "`role-ARN`",
                "accountId": "`account-ID`",
                "userName": "user-name"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2022-09-06T15:04:31Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2022-09-06T15:08:43Z",
    "eventSource": "`account-ID`",
    "eventName": "**ListConnections**",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.168.0.1",
    "userAgent": "aws-cli/1.18.147 Python/2.7.18 Linux/5.4.207-126.363.amzn2int.x86_64 botocore/1.18.6",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 ",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 ",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`account-ID`",
    "eventCategory": "Management"
}

```

## Example CodeCatalyst project

resource event in AWS

The following example shows a CloudTrail log entry that demonstrates the
`CreateDevEnvironment`

action. An AWS account that is connected to the space and is the designated billing
account for the space is used for project-level events in the space, such as creating a
Dev Environment.

Under `userIdentity`, in the `accountId` field, this is the
IAM Identity Center account ID (`432677196278`) that hosts the identity
pool for all AWS Builder ID identities. This account ID contains the following information
about the CodeCatalyst user for the event.

- The `type` field indicates the type of IAM entity for the
  request. For CodeCatalyst events for space and project resources, this value is
  `IdentityCenterUser`. The `accountId` field specifies
  the account that owns the entity that was used to get credentials.
- The `userId` field contains the AWS Builder ID identifier for the
  user.
- The `identityStoreArn` field contains the role ARN for the identity
  store account and user.

The `recipientAccountId` field contains the account ID for the billing
account for the space, with an example value here of 111122223333.

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

```
{
	"eventVersion": "1.09",
	"userIdentity": {
		"type": "IdentityCenterUser",
		"accountId": "`432677196278`",
		"onBehalfOf": {
			"userId": "`user-ID`",
			"identityStoreArn": "`arn:aws:identitystore::432677196278:identitystore/d-9067642ac7`"
		},
		"credentialId": "ABCDefGhiJKLMn11Lmn_1AbCDEFgHijk-AaBCdEFGHIjKLmnOPqrs11abEXAMPLE"
	},
	"eventTime": "2023-05-18T17:10:50Z",
	"eventSource": "codecatalyst.amazonaws.com",
	"eventName": "CreateDevEnvironment",
	"awsRegion": "us-west-2",
	"sourceIPAddress": "192.168.0.1",
	"userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
	"requestParameters": {
		"spaceName": "MySpace",
		"projectName": "MyProject",
		"ides": [{
			"runtime": "public.ecr.aws/q6e8p2q0/cloud9-ide-runtime:2.5.1",
			"name": "Cloud9"
		}],
		"instanceType": "dev.standard1.small",
		"inactivityTimeoutMinutes": 15,
		"persistentStorage": {
			"sizeInGiB": 16
		}
	},
	"responseElements": {
		"spaceName": "MySpace",
		"projectName": "MyProject",
		"id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 "
	},
	"requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
	"eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
	"readOnly": false,
	"eventType": "AwsApiCall",
	"managementEvent": true,
	"recipientAccountId": "`111122223333`",
	"sharedEventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
	"eventCategory": "Management"
}

```

###### Note

In certain events, the user agent may not be known. In this case, CodeCatalyst will
provide a value of `Unknown` in the `userAgent` field in the
CloudTrail event.

## Querying your CodeCatalyst event

trails

You can create and manage queries for your CloudTrail logs using a query table in Amazon Athena.
For more information about creating a query, see [Querying
AWS CloudTrail logs](../../../athena/latest/ug/cloudtrail-logs.md "../../../athena/latest/ug/cloudtrail-logs.md") in the _Amazon Athena User
Guide_.
