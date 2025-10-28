# Prerequisites

The following steps are prequisites for the getting started exercises. The steps show you
how to set up your account, create an IAM role that gives Amazon Kendra
permission to make calls on your behalf, and index documents from an Amazon S3 bucket.
An S3 bucket is used as an example, but you can use other data sources that Amazon Kendra
supports. See [Data
sources](hiw-data-source.md "hiw-data-source.md").

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

- If you are using an S3 bucket containing documents to test Amazon Kendra, create
  an S3 bucket in the same region that you are using Amazon Kendra. For instructions,
  see [Creating and Configuring an S3
  Bucket](../../../AmazonS3/latest/userguide/create-configure-bucket.md "../../../AmazonS3/latest/userguide/create-configure-bucket.md") in the _Amazon Simple Storage Service User Guide_.

Upload your documents to your S3 bucket. For instructions, see [Uploading, Downloading, and Managing
Objects](../../../AmazonS3/latest/userguide/upload-download-objects.md "../../../AmazonS3/latest/userguide/upload-download-objects.md") in the _Amazon Simple Storage Service User Guide_.

If you are using another data source, you must have an active site and credentials to
connect to the data source.
If you are using the console to get started, start with [Getting started with the Amazon Kendra console](gs-console.md "gs-console.md").

## Amazon Kendra resources: AWS CLI, SDK,

console

There are certain permissions required if you use CLI, SDK, or the console.

To use Amazon Kendra for the CLI, SDK, or console you must have permissions to
allow Amazon Kendra to create and manage resources on your behalf. Depending on your
use case, these permissions include access to the Amazon Kendra API itself, AWS KMS keys if you want to encrypt your data through a custom CMK, Identity
Center directory if you want to integrate with AWS IAM Identity Center or [create a Search
Experience](deploying-search-experience-no-code.md "deploying-search-experience-no-code.md"). For a full list of permissions for different use cases, see [IAM
roles](iam-roles.md "iam-roles.md").

First, you must attach the below permissions to your IAM user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt1644430853544",
 "Action": [
 "kms:CreateGrant",
 "kms:DescribeKey"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Sid": "Stmt1644430878150",
 "Action": "kendra:*",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Sid": "Stmt1644430973706",
 "Action": [
 "sso:AssociateProfile",
 "sso:CreateManagedApplicationInstance",
 "sso:DeleteManagedApplicationInstance",
 "sso:DisassociateProfile",
 "sso:GetManagedApplicationInstance",
 "sso:GetProfile",
 "sso:ListDirectoryAssociations",
 "sso:ListProfileAssociations",
 "sso:ListProfiles"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Sid": "Stmt1644430999558",
 "Action": [
 "sso-directory:DescribeGroup",
 "sso-directory:DescribeGroups",
 "sso-directory:DescribeUser",
 "sso-directory:DescribeUsers"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Sid": "Stmt1644431025960",
 "Action": [
 "identitystore:DescribeGroup",
 "identitystore:DescribeUser",
 "identitystore:ListGroups",
 "identitystore:ListUsers"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

Second, if you use the CLI or SDK, you must also create an IAM role and
policy to access Amazon CloudWatch Logs. If you are using the console, you don't need to
create an IAM role and policy for this. You create this as part of the
console procedure.

###### To create an IAM role and policy for the AWS CLI and SDK

that allows Amazon Kendra to access your Amazon CloudWatch Logs.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. From the left menu, choose **Policies** and then choose
   **Create policy**.
3. Choose **JSON** and then replace the default policy with the
   following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/Kendra"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/kendra/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/kendra/*:log-stream:*"
 ]
 }
 ]
}`

```

4. Choose **Review policy**.
5. Name the policy "KendraPolicyForGettingStartedIndex" and then choose
   **Create policy**.
6. From the left menu, choose **Roles** and then choose
   **Create role**.
7. Choose **Another AWS account** and then type your
   account ID in **Account ID**. Choose **Next:
   Permissions**.
8. Choose the policy that you created above and then choose **Next:
   Tags**
9. Don't add any tags. Choose **Next: Review**.
10. Name the role "KendraRoleForGettingStartedIndex" and then choose
    **Create role**.
11. Find the role that you just created. Choose the role name to open the summary.
    Choose **Trust relationships** and then choose **Edit trust
    relationship**.
12. Replace the existing trust relationship with the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "kendra.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

13. Choose **Update trust policy**.

Third, if you use an Amazon S3 to store your documents or you are using S3 to
test Amazon Kendra, you also must create an IAM role and policy to
access your bucket. If you are using another data source, see [IAM roles for data
sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

###### To create an IAM role and policy that allows Amazon Kendra to

access and index your Amazon S3 bucket.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. From the left menu, choose **Policies** and then choose
   **Create policy**.
3. Choose **JSON** and then replace the default policy with the
   following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket name`/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket name`"
 ],
 "Effect": "Allow"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:`us-east-1`:`123456789012`:index/*"
 }
 ]
}`

```

4. Choose **Review policy**.
5. Name the policy "KendraPolicyForGettingStartedDataSource" and then choose
   **Create policy**.
6. From the left menu, choose **Roles** and then choose
   **Create role**.
7. Choose **Another AWS account** and then type your
   account ID in **Account ID**. Choose **Next:
   Permissions**.
8. Choose the policy that you created above and then choose **Next:
   Tags**
9. Don't add any tags. Choose **Next: Review**.
10. Name the role "KendraRoleForGettingStartedDataSource" and then choose
    **Create role**.
11. Find the role that you just created. Choose the role name to open the summary.
    Choose **Trust relationships** and then choose **Edit trust
    relationship**.
12. Replace the existing trust relationship with the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "kendra.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

13. Choose **Update trust policy**.

Depending on how you want to use the Amazon Kendra API, do one of the
following.

- [Getting started (AWS CLI)](gs-cli.md "gs-cli.md")
- [Getting started (AWS SDK for Java)](gs-java.md "gs-java.md")
- [Getting started (AWS SDK for Python (Boto3))](gs-python.md "gs-python.md")
