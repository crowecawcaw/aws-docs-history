# Prerequisites for using AWS B2B Data Interchange

This topic describes how to sign up for an AWS account, create an admin user, and
configure an Amazon S3 bucket to use with B2B Data Interchange.

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

## Configure an Amazon S3 bucket

You need to have an Amazon S3 bucket set up and ready to use. B2B Data Interchange requires buckets for storing
input, output, and instruction documents. For details, see [Getting started with Amazon S3](../../../AmazonS3/latest/userguide/GetStartedWithS3.md "../../../AmazonS3/latest/userguide/GetStartedWithS3.md").

- The Amazon S3 bucket must be in the same AWS account as the B2B Data Interchange user.
- The Amazon S3 bucket must be in the same region as the B2B Data Interchange user.

## Setting up S3 bucket policies and

permissions

Before you can transform and generate Electronic Data Interchange (EDI) documents, you
must configure S3 bucket policies for your trading capabilities. This topic provides
step-by-step instructions and example policies to help you get started.

### Configuring S3 bucket policies

Follow these steps to configure policies for both your input and output buckets. If
your buckets use SSE-KMS encryption, you must also update your AWS KMS key policy. For
policy examples, see [Example policies](#bucket-policy-examples "#bucket-policy-examples").

###### To configure a bucket policy

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Navigate to your bucket and choose the **Permissions**
   tab.
3. In the **Bucket policy** section, choose
   **Edit**.
4. Do one of the following:
   - Copy an example policy from [Example policies](#bucket-policy-examples "#bucket-policy-examples")
     and paste it into the policy editor.
   - Choose **Copy policy** when creating a trading
     capability, and paste the copied policy.

5. Choose **Save changes**.

###### Note

For information about temporary files and related permissions, see [Managing temporary files and
permissions](#temp-files-permissions "#temp-files-permissions").

### Enabling EventBridge notifications

You must enable Amazon EventBridge notifications for your input S3 bucket.

###### To enable EventBridge notifications

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Navigate to your bucket and choose the **Properties**
   tab.
3. Scroll to the **EventBridge** section.
4. If notifications are already enabled, you're done. Otherwise, continue to the
   next step.
5. Choose **Edit**.
6. Select **On** and choose **Save
   changes**.

###### Important

After enabling EventBridge, wait at least 5 minutes before placing files in your
S3 bucket. This allows time for the changes to take effect.

### Managing temporary files and

permissions

Your output bucket policies require the following permissions:

- `s3:GetObject` - Allows the service to read temporary files
- `s3:DeleteObject` - Enables cleanup of temporary files

###### Important

Without the `s3:DeleteObject` permission:

- Temporary files remain in your S3 bucket and incur storage charges.
- These files can be up to ten times larger than the input X12 file.

The service uses the following locations for temporary files:

- `customerOutputDirectory/parsed` - For service use
- `customerOutputDirectory/`tradingPartnerId`/parsed`

* For S3 use (when using partnerships)

### Example policies

Use these example policies to configure permissions for your S3 buckets and AWS KMS
keys.

###### Important

Replace all `user input placeholder` values with your own
information.

Input bucket policy
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Id": "B2BIEdiCapabilityInputPolicy",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "b2bi.amazonaws.com"
 },
 "Action": [
 "s3:GetObject",
 "s3:GetObjectAttributes"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/`input-folder`*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
 ]
}`

```

Output bucket policy
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Id": "B2BIEdiCapabilityOutputPolicy",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "b2bi.amazonaws.com"
 },
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:AbortMultipartUpload"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/`output-folder`/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
 ]
}`

```

If you use SSE-KMS or DSSE-KMS encryption, you must also configure AWS KMS key
policies:

###### Important

Don't use AWS managed key policies - they can't be edited. Create a customer
managed key instead.

Input KMS key policy
Use this policy for encrypted input buckets to allow decryption of
files:

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Id": "B2BIEdiCapabilityInputKeyPolicy",
 "Statement": [
 {
 "Sid": "Allow administration of the key",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Sid": "Allow B2Bi access",
 "Effect": "Allow",
 "Principal": {
 "Service": "b2bi.amazonaws.com"
 },
 "Action": "kms:Decrypt",
 "Resource": "*"
 }
 ]
}`

```

Output KMS key policy
Use this policy for encrypted output buckets to allow encryption of
files:

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Id": "B2BIEdiCapabilityOutputKeyPolicy",
 "Statement": [
 {
 "Sid": "Allow administration of the key",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Sid": "Allow B2Bi access",
 "Effect": "Allow",
 "Principal": {
 "Service": "b2bi.amazonaws.com"
 },
 "Action": "kms:GenerateDataKey",
 "Resource": "*"
 }
 ]
}`

```

If you use the same bucket for both input and output, use either policy and add the
other permission, as shown in this example:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "B2BIEdiCapabilityOutputKeyPolicy",
 "Statement": [
 {
 "Sid": "Allow administration of the key",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Sid": "Allow B2Bi access",
 "Effect": "Allow",
 "Principal": {
 "Service": "b2bi.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*"
 }
 ]
}`

```
