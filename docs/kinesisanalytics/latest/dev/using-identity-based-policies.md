After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Using Identity-Based Policies (IAM

Policies) for

The following are examples of identity-based policies that demonstrate how an account
administrator can attach permissions policies to IAM identities (that is, users,
groups, and roles) and grant permissions to perform operations on
resources.

###### Important

We recommend that you first review the introductory topics that explain the basic
concepts and options available to manage access to your
resources. For more information, see [Overview of Managing Access Permissions to Your
Resources](access-control-overview.md "access-control-overview.md").

###### Topics

- [Permissions Required to Use the
  Console](#console-permissions "#console-permissions")
- [Amazon-Managed (Predefined) Policies
  for](#access-policy-aws-managed-policies "#access-policy-aws-managed-policies")
- [Customer Managed Policy
  Examples](#access-policy-customer-managed-examples "#access-policy-customer-managed-examples")
  The following shows an example of a permissions policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt1473028104000",
 "Effect": "Allow",
 "Action": [
 "kinesisanalytics:CreateApplication"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The policy has one statement:

- The first statement grants permissions for one action
  (`kinesisanalytics:CreateApplication`) on a resource using the
  Amazon Resource Name (ARN) for the application. The ARN in this case specifies a
  wildcard character (\*) to indicate that the permission is granted for any
  resource.
  For a table showing all of the API operations and the resources that they apply
  to, see [API Permissions: Actions,
  Permissions, and Resources Reference](api-permissions-reference.md "api-permissions-reference.md").

## Permissions Required to Use the

Console

For a user to work with the console, you must grant the necessary
permissions. For example, if you want a user to have permissions to create an
application, grant permissions that show them the streaming sources in the account
so that the user can configure input and output on the console.

We recommend the following:

- Use the Amazon-managed policies to grant user permissions. For available
  policies, see [Amazon-Managed (Predefined) Policies
  for](#access-policy-aws-managed-policies "#access-policy-aws-managed-policies") .
- Create custom policies. In this case, we recommend that you review the
  example provided in this section. For more information, see
  [Customer Managed Policy
  Examples](#access-policy-customer-managed-examples "#access-policy-customer-managed-examples").

## Amazon-Managed (Predefined) Policies

for

AWS addresses many common use cases by providing standalone IAM policies
that are created and administered by AWS. These Amazon-managed policies grant necessary
permissions for common use cases so that you can avoid having to investigate what
permissions are needed. For more information, see [Amazon-Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

The following Amazon-managed policies, which you can attach to users in your account,
are specific to :

- **`AmazonKinesisAnalyticsReadOnly`** – Grants
  permissions for actions that enable a user to list
  applications and review input/output configuration. It also grants
  permissions that allow a user to view a list of Kinesis streams and Firehose
  delivery streams. As the application is running, the user can view source
  data and real-time analytics results in the console.
- **`AmazonKinesisAnalyticsFullAccess`** – Grants
  permissions for all actions and all other permissions that allows
  a user to create and manage applications. However, note the
  following:

   
  - These permissions are not sufficient if the user wants to
    create a new IAM role in the console (these permissions allow
    the user to select an existing role). If you want the user to be
    able to create an IAM role in the console, add the
    `IAMFullAccess` Amazon-managed policy.
  - A user must have permission for the `iam:PassRole`
    action to specify an IAM role when configuring
    application. This Amazon-managed policy grants permission for the
    `iam:PassRole` action to the user only on the IAM
    roles that start with the prefix
    `service-role/kinesis-analytics`.

  If the user wants to configure the application with
  a role that does not have this prefix, you first must explicitly
  grant the user permission for the `iam:PassRole` action
  on the specific role.

You can also create your own custom IAM policies to allow permissions for
actions and resources. You can attach these custom policies to
the users or groups that require those permissions.

## Customer Managed Policy

Examples

The examples in this section provide a group of sample policies that you can
attach to a user. If you are new to creating policies, we recommend that you first
create a user in your account. Then attach the policies to the user in
sequence, as outlined in the steps in this section. You can then use the console to
verify the effects of each policy as you attach the policy to the user.

Initially, the user doesn't have permissions and can't do anything on the console.
As you attach policies to the user, you can verify that the user can perform various
actions on the console. 

We recommend that you use two browser windows. In one window, create the user and
grant permissions. In the other, sign in to the AWS Management Console using the user's
credentials and verify permissions as you grant them.

For examples that show how to create an IAM role that you can use as an execution
role for your application, see [Creating IAM Roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") in the _IAM User Guide_.

###### Example steps

- [Step 1: Create an IAM User](#console-permissions-createuser "#console-permissions-createuser")
- [Step 2: Allow the User
  Permissions for Actions that Are Not Specific to](#console-permissions-grant-non-ka-permissions "#console-permissions-grant-non-ka-permissions")
- [Step 3: Allow the User to
  View a List of Applications and View Details](#console-permissions-grant-list-applications "#console-permissions-grant-list-applications")
- [Step 4: Allow the User
  to Start a Specific Application](#console-permissions-start-app "#console-permissions-start-app")
- [Step 5: Allow the User
  to Create an Application](#console-permissions-grant-create-applications "#console-permissions-grant-create-applications")
- [Step 6: Allow the Application to Use
  Lambda Preprocessing](#console-permissions-grant-lambda "#console-permissions-grant-lambda")

### Step 1: Create an IAM User

First, you need to create a user, add the user to an IAM group with
administrative permissions, and then grant administrative permissions to the user that
you created. You can then access AWS using a special URL and that user's credentials.

For instructions, see [Creating Your First IAM User and Administrators Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the _IAM User Guide_.

### Step 2: Allow the User

Permissions for Actions that Are Not Specific to

First, grant a user permission for all actions that aren't specific to
that the user will need when working with applications.
These include permissions for working with streams (Amazon Kinesis Data Streams actions, Amazon Data Firehose
actions), and permissions for CloudWatch actions. Attach the following policy to
the user.

You need to update the policy by providing an IAM role name for which you
want to grant the `iam:PassRole` permission, or specify a wildcard character (\*) indicating all IAM
roles. This is not a secure practice; however you might not have a specific IAM role
created during this testing.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kinesis:CreateStream",
 "kinesis:DeleteStream",
 "kinesis:DescribeStream",
 "kinesis:ListStreams",
 "kinesis:PutRecord",
 "kinesis:PutRecords"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "firehose:DescribeDeliveryStream",
 "firehose:ListDeliveryStreams"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "logs:GetLogEvents",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:ListPolicyVersions",
 "iam:ListRoles"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::*:role/service-role/`role-name`"
 }
 ]
}`

```

### Step 3: Allow the User to

View a List of Applications and View Details

The following policy grants a user the following permissions:

- Permission for the `kinesisanalytics:ListApplications`
  action so the user can view a list of applications. This is a
  service-level API call, and therefore you specify "\*" as the
  `Resource` value.
- Permission for the `kinesisanalytics:DescribeApplication`
  action so that you can get information about any of the
  applications.

Add this policy to the user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kinesisanalytics:ListApplications"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesisanalytics:DescribeApplication"
 ],
 "Resource": "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/*"
 }
 ]
}`

```

Verify these permissions by signing into the console using the user
credentials.

### Step 4: Allow the User

to Start a Specific Application

If you want the user to be able to start one of the existing
applications, attach the following policy to the user. The policy provides the
permission for the `kinesisanalytics:StartApplication` action. You
must update the policy by providing your account ID, AWS Region and application
name.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kinesisanalytics:StartApplication"
 ],
 "Resource": "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`application-name`"
 }
 ]
}`

```

### Step 5: Allow the User

to Create an Application

If you want the user to create an application, you can then attach
the following policy to the user. You must update the policy and provide an AWS Region, your account ID, and either a specific application name that you want
the user to create, or a "\*" so that the user can specify any application name
(and thus create multiple applications).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt1473028104000",
 "Effect": "Allow",
 "Action": [
 "kinesisanalytics:CreateApplication"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesisanalytics:StartApplication",
 "kinesisanalytics:UpdateApplication",
 "kinesisanalytics:AddApplicationInput",
 "kinesisanalytics:AddApplicationOutput"
 ],
 "Resource": "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`application-name`"
 }
 ]
}`

```

### Step 6: Allow the Application to Use

Lambda Preprocessing

If you want the application to be able to use Lambda preprocessing, attach the
following policy to the role.

```
     {
       "Sid": "UseLambdaFunction",
       "Effect": "Allow",
       "Action": [
           "lambda:InvokeFunction",
           "lambda:GetFunctionConfiguration"
       ],
       "Resource": "<FunctionARN>"
   }

```
