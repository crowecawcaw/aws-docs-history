# Perform a privileged task on an AWS Organizations

member account

The AWS Organizations management account or a delegated administrator account for IAM can perform
some root user tasks on member accounts using short-term root access. These tasks can only be
performed when you sign in as the root user of an account. Short-term privileged sessions give
you temporary credentials that you can scope to take privileged actions on a member account
in your organization.

Once you launch a privileged session, you can delete a misconfigured Amazon S3 bucket policy,
delete a misconfigured Amazon SQS queue policy, delete the root user credentials for a member
account, and reenable root user credentials for a member account.

###### Note

To use centralized root access, you must sign in via a management account or a
delegated administrator account and must have the `sts:AssumeRoot` permission
explicitly granted.

## Prerequisites

Before you can launch a privileged session, you must have the following
settings:

- You have enabled centralized root access in your organization. For steps to
  enable this feature, see [Centralize root access for member
  accounts](id_root-enable-root-access.md "id_root-enable-root-access.md").
- Your management account or delegated administrator account has the following
  permissions: `sts:AssumeRoot`

## Taking a privileged action on

a member account (console)

###### To launch a session for privileged action in a member account in the

AWS Management Console

1.  Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane of the console, choose **Root access
    management**.
3.  Select a name from the member account list, and choose **Take
    privileged action**.
4.  Choose the privileged action you want to take in the member account.
    - Select **Delete Amazon S3 bucket policy** to remove a
      misconfigured bucket policy that denies all principals from accessing
      the Amazon S3 bucket.
      1. Choose **Browse S3** to select a name from
         the buckets owned by the member account, and select
         **Choose**.
      2. Choose **Delete bucket policy**.
      3. Use the Amazon S3 console to correct the bucket policy after
         deleting the misconfigured policy. For more information, see
         [Adding a bucket policy by using the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") in
         the _Amazon S3 User Guide_.

    - Select **Delete Amazon SQS policy** to delete an Amazon Simple Queue Service
      resource-based policy that denies all principals from accessing an Amazon SQS
      queue.
      1. Enter the queue name in **SQS queue name**,
         and select **Delete SQS policy**.
      2. Use the Amazon SQS console to correct the queue policy after
         deleting the misconfigured policy. For more information, see
         [Configuring an access policy in Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-add-permissions.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-add-permissions.md") in the
         _Amazon SQS Developer Guide_.

    - Select **Delete root credentials** to remove root
      access from a member account. Deleting root user credentials removes the
      root user password, access keys, signing certificates, and deactivates
      multi-factor authentication (MFA) for the member account.
      1. Choose **Delete root credentials**.

    - Select **Allow password recovery** to recover root user
      credentials for a member account.

    This option is only available when the member account has no root user
    credentials.

        1. Choose **Allow password recovery**.
        2. After taking this privileged action, the person with access to
         the root user email inbox for the member account can  [reset
         the root user password](reset-root-password.md "reset-root-password.md") and sign in to the member
         account root user.

## Taking a privileged action on a

member account (AWS CLI)

###### To launch a session for privileged action in a member account from the

AWS Command Line Interface

1. Use the following command to assume a root user session: [aws sts assume-root](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-root.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-root.html").

###### Note

The global endpoint is not supported for `sts:AssumeRoot`. You
must send this request to a Regional AWS STS endpoint. For more information,
see [Manage AWS STS in an AWS Region](id_credentials_temp_enable-regions.md "id_credentials_temp_enable-regions.md").

When you launch a privileged root user session for a member account, you must
define `task-policy-arn` to scope the session to the privileged
action to be performed during the session. You can use one of following AWS
managed policies to scope privileged session actions.

    * [IAMAuditRootUserCredentials](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMAuditRootUserCredentials "security-iam-awsmanpol.md#security-iam-awsmanpol-IAMAuditRootUserCredentials")
    * [IAMCreateRootUserPassword](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMCreateRootUserPassword "security-iam-awsmanpol.md#security-iam-awsmanpol-IAMCreateRootUserPassword")
    * [IAMDeleteRootUserCredentials](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMDeleteRootUserCredentials "security-iam-awsmanpol.md#security-iam-awsmanpol-IAMDeleteRootUserCredentials")
    * [S3UnlockBucketPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-S3UnlockBucketPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-S3UnlockBucketPolicy")
    * [SQSUnlockQueuePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-SQSUnlockQueuePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-SQSUnlockQueuePolicy")

To limit the actions a management account or delegated administrator can
perform during a privileged root user session, you can use the AWS STS condition key
[sts:TaskPolicyArn](reference_policies_iam-condition-keys.md#ck_taskpolicyarn "reference_policies_iam-condition-keys.md#ck_taskpolicyarn").

In the following example, the delegated administrator assumes root to delete
the root user credentials for the member account ID
`111122223333`.

```
aws sts assume-root \
  --target-principal `111122223333` \
  --task-policy-arn arn=`arn:aws:iam::aws:policy/root-task/IAMDeleteRootUserCredentials` \
  --duration-seconds `900`
```

2. Use the `SessionToken`, `AccessKeyId`, and
   `SecretAccessKey` from the response to perform privileged actions
   in the member account. You can omit the user name and password in the request to
   default to the member account.
   - **Check the status of root user credentials**. Use the
     following commands to check the status of root user credentials for a
     member account.
     - [get-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user.html")
     - [get-login-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-login-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-login-profile.html")
     - [list-access-keys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-access-keys.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-access-keys.html")
     - [list-signing-certificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-signing-certificates.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-signing-certificates.html")
     - [list-mfa-devices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-mfa-devices.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-mfa-devices.html")
     - [get-access-key-last-used](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-access-key-last-used.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-access-key-last-used.html")

   - **Delete root user credentials**. Use the following
     commands to delete root access. You can remove the root user password,
     access keys, signing certificates, and deactivate multi-factor
     authentication (MFA) to remove all access to and recovery of the
     root user.
     - [delete-login-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-login-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-login-profile.html")
     - [delete-access-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-access-key.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-access-key.html")
     - [delete-signing-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html")
     - [deactivate-mfa-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/deactivate-mfa-device.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/deactivate-mfa-device.html")

   - **Delete Amazon S3 bucket policy**. Use the following
     commands to read, edit, and delete a misconfigured bucket policy that
     denies all principals from accessing the Amazon S3 bucket.
     - [list-buckets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-buckets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-buckets.html")
     - [get-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-policy.html")
     - [put-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-policy.html")
     - [delete-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-policy.html")

   - **Delete Amazon SQS policy**. Use the following commands
     to view and delete an Amazon Simple Queue Service resource-based policy that denies all
     principals from accessing an Amazon SQS queue.
     - [list-queues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/list-queues.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/list-queues.html")
     - [get-queue-url](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-url.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-url.html")
     - [get-queue-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-attributes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-attributes.html")
     - [set-queue-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/set-queue-attributes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/set-queue-attributes.html")

   - **Allow password recovery**. Use the following
     commands to view the user name and recover root user credentials for a
     member account.
     - [get-login-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-login-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-login-profile.html")
     - [create-login-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-login-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-login-profile.html")

## Taking a privileged action on a

member account (AWS API)

###### To launch a session for privileged action in a member account from the AWS

API

1. Use the following command to assume a root user session: [AssumeRoot](../../../STS/latest/APIReference/API_AssumeRoot.md "../../../STS/latest/APIReference/API_AssumeRoot.md").

###### Note

The global endpoint is not supported for AssumeRoot. You must send this
request to a Regional AWS STS endpoint. For more information, see [Manage AWS STS in an AWS Region](id_credentials_temp_enable-regions.md "id_credentials_temp_enable-regions.md").

When you launch a privileged root user session for a member account, you must
define `TaskPolicyArn` to scope the session to the privileged action
to be performed during the session. You can use one of following AWS managed
policies to scope privileged session actions.

    * [IAMAuditRootUserCredentials](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMAuditRootUserCredentials "security-iam-awsmanpol.md#security-iam-awsmanpol-IAMAuditRootUserCredentials")
    * [IAMCreateRootUserPassword](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMCreateRootUserPassword "security-iam-awsmanpol.md#security-iam-awsmanpol-IAMCreateRootUserPassword")
    * [IAMDeleteRootUserCredentials](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMDeleteRootUserCredentials "security-iam-awsmanpol.md#security-iam-awsmanpol-IAMDeleteRootUserCredentials")
    * [S3UnlockBucketPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-S3UnlockBucketPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-S3UnlockBucketPolicy")
    * [SQSUnlockQueuePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-SQSUnlockQueuePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-SQSUnlockQueuePolicy")

To limit the actions a management account or delegated administrator can
perform during a privileged root user session, you can use the AWS STS condition key
[sts:TaskPolicyArn](reference_policies_iam-condition-keys.md#ck_taskpolicyarn "reference_policies_iam-condition-keys.md#ck_taskpolicyarn").

In the following example, the delegated administrator assumes root to read,
edit and delete a misconfigured resource-based policy for an Amazon S3 bucket for the
member account ID `111122223333`.

```
https://sts.us-east-2.amazonaws.com/
  ?Version=2011-06-15
  &Action=AssumeRoot
  &TargetPrincipal=`111122223333`
  &PolicyArns.arn=`arn:aws:iam::aws:policy/root-task/S3UnlockBucketPolicy`
  &DurationSeconds `900`
```

2. Use the `SessionToken`, `AccessKeyId`, and
   `SecretAccessKey` from the response to perform privileged actions
   in the member account. You can omit the user name and password in the request to
   default to the member account.
   - **Check the status of root user credentials**. Use the
     following commands to check the status of root user credentials for a
     member account.
     - [GetUser](../APIReference/API_GetUser.md "../APIReference/API_GetUser.md")
     - [GetLoginProfile](../APIReference/API_GetLoginProfile.md "../APIReference/API_GetLoginProfile.md")
     - [ListAccessKeys](../APIReference/API_ListAccessKeys.md "../APIReference/API_ListAccessKeys.md")
     - [ListSigningCertificates](../APIReference/API_ListSigningCertificates.md "../APIReference/API_ListSigningCertificates.md")
     - [ListMFADevices](../APIReference/API_ListMFADevices.md "../APIReference/API_ListMFADevices.md")
     - [GetAccessKeyLastUsed](../APIReference/API_GetAccessKeyLastUsed.md "../APIReference/API_GetAccessKeyLastUsed.md")

   - **Delete root user credentials**. Use the following
     commands to delete root access. You can remove the root user password,
     access keys, signing certificates, and deactivate multi-factor
     authentication (MFA) to remove all access to and recovery of the
     root user.
     - [DeleteLoginProfile](../APIReference/API_DeleteLoginProfile.md "../APIReference/API_DeleteLoginProfile.md")
     - [DeleteAccessKey](../APIReference/API_DeleteAccessKey.md "../APIReference/API_DeleteAccessKey.md")
     - [DeleteSigningCertificate](../APIReference/API_DeleteSigningCertificate.md "../APIReference/API_DeleteSigningCertificate.md")
     - [DeactivateMfaDevice](../APIReference/API_DeactivateMFADevice.md "../APIReference/API_DeactivateMFADevice.md")

   - **Delete Amazon S3 bucket policy**. Use the following
     commands to read, edit, and delete a misconfigured bucket policy that
     denies all principals from accessing the Amazon S3 bucket.
     - [ListBuckets](../../../AmazonS3/latest/API/API_ListBuckets.md "../../../AmazonS3/latest/API/API_ListBuckets.md")
     - [GetBucketPolicy](../../../AmazonS3/latest/API/API_GetBucketPolicy.md "../../../AmazonS3/latest/API/API_GetBucketPolicy.md")
     - [PutBucketPolicy](../../../AmazonS3/latest/API/API_PutBucketPolicy.md "../../../AmazonS3/latest/API/API_PutBucketPolicy.md")
     - [DeleteBucketPolicy](../../../AmazonS3/latest/API/API_DeleteBucketPolicy.md "../../../AmazonS3/latest/API/API_DeleteBucketPolicy.md")

   - **Delete Amazon SQS policy**. Use the following commands
     to view and delete an Amazon Simple Queue Service resource-based policy that denies all
     principals from accessing an Amazon SQS queue.
     - [ListQueues](../../../AWSSimpleQueueService/latest/APIReference/API_ListQueues.md "../../../AWSSimpleQueueService/latest/APIReference/API_ListQueues.md")
     - [GetQueueUrl](../../../AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.md "../../../AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.md")
     - [GetQueueAttributes](../../../AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.md "../../../AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.md")
     - [SetQueueAttributes](../../../AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.md "../../../AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.md")

   - **Allow password recovery**. Use the following
     commands to view the user name and recover root user credentials for a
     member account.
     - [GetLoginProfile](../APIReference/API_GetLoginProfile.md "../APIReference/API_GetLoginProfile.md")
     - [CreateLoginProfile](../APIReference/API_CreateLoginProfile.md "../APIReference/API_CreateLoginProfile.md")
