# Prerequisites to create a subscriber

with data access in Security Lake

You must complete the following prerequisites before you can create a subscriber with
data access in Security Lake.

## Verify

permissions

To verify your permissions, use IAM to review the IAM policies that are
attached to your IAM identity. Then, compare the information in those policies to
the following list of (permissions) actions that you must have to notify subscribers when new
data is written to the data lake.

You will need permission to perform the following actions:

- `iam:CreateRole`
- `iam:DeleteRolePolicy`
- `iam:GetRole`
- `iam:PutRolePolicy`
- `lakeformation:GrantPermissions`
- `lakeformation:ListPermissions`
- `lakeformation:RegisterResource`
- `lakeformation:RevokePermissions`
- `ram:GetResourceShareAssociations`
- `ram:GetResourceShares`
- `ram:UpdateResourceShare`

In addition to the preceding list, you also need permission to perform the following actions:

- `events:CreateApiDestination`
- `events:CreateConnection`
- `events:DescribeRule`
- `events:ListApiDestinations`
- `events:ListConnections`
- `events:PutRule`
- `events:PutTargets`
- `s3:GetBucketNotification`
- `s3:PutBucketNotification`
- `sqs:CreateQueue`
- `sqs:DeleteQueue`
- `sqs:GetQueueAttributes`
- `sqs:GetQueueUrl`
- `sqs:SetQueueAttributes`

## Get the subscriber's external ID

To create a subscriber, apart from the subscriber's AWS account ID, you will also need to get
their _external
ID_. The external ID is a unique identifier that
the subscriber provides to you. Security Lake adds the external ID to the subscriber
IAM role that it creates. You use the external ID when you create a subscriber in the Security Lake console,
through the API, or AWS CLI.

For more information about external IDs, see [How to use
an external ID when granting access to your AWS resources to a third
party](../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md "../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md") in the _IAM User Guide_.

###### Important

If you plan to use the Security Lake console to add a subscriber, you can
skip the next step and proceed to [Creating a subscriber with data
access in Security Lake](create-subscriber-data-access.md "create-subscriber-data-access.md"). The Security Lake console offers a
streamlined process for getting started, and creates all necessary IAM roles or uses
existing roles on your behalf.

If you plan to use Security Lake API or AWS CLI to add a subscriber, continue with
the next step to create an IAM role to invoke EventBridge API destinations.

## Create IAM role to invoke EventBridge API

destinations (API and AWS CLI-only step)

If you're using Security Lake through API or AWS CLI, create a role in AWS Identity and Access Management (IAM)
that grants Amazon EventBridge permissions to invoke API destinations and send object
notifications to the correct HTTPS endpoints.

After creating this IAM role, you'll need the Amazon Resource Name (ARN) of the
role in order to create the subscriber. This IAM role isn't necessary if the
subscriber polls data from an Amazon Simple Queue Service (Amazon SQS) queue or directly queries data from
AWS Lake Formation. For more information about this type of data access method (access type), see [Managing query access for Security Lake
subscribers](subscriber-query-access.md "subscriber-query-access.md").

Attach the following policy to your IAM role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowInvokeApiDestination",
 "Effect": "Allow",
 "Action": [
 "events:InvokeApiDestination"
 ],
 "Resource": [
 "arn:aws:events:`us-east-1`:`123456789012`:api-destination/AmazonSecurityLake*/*"
 ]
 }
 ]
}`

```

Attach the following trust policy to your IAM role to permit EventBridge to assume the
role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowEventBridgeToAssume",
 "Effect": "Allow",
 "Principal": {
 "Service": "events.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

[Show moreShow less](# "#")
Security Lake automatically creates an IAM role that permits the subscriber to read
data from the data lake (or poll events from an Amazon SQS queue if that's the preferred
method of notification). This role is protected with an AWS managed policy called
[AmazonSecurityLakePermissionsBoundary](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSecurityLakePermissionsBoundary "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSecurityLakePermissionsBoundary").
