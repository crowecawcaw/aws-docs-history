

# Perform a privileged task on an AWS Organizations member account
<a name="id_root-user-privileged-task"></a>

The AWS Organizations management account or a delegated administrator account for IAM can perform some privileged tasks on member accounts that would otherwise require root user credentials. With centralized root access, these tasks are performed through short-term privileged sessions. These sessions provide temporary credentials scoped to specific privileged actions, without requiring root user sign-in on the member account.

Once you launch a privileged session, you can delete a misconfigured Amazon S3 bucket policy, delete a misconfigured Amazon SQS queue policy, delete the root user credentials for a member account, and reenable root user credentials for a member account.

**Note**  
To use centralized root access, you must sign in via a management account or a delegated administrator account as an IAM user or role with the `sts:AssumeRoot` permission explicitly granted. You cannot use root user credentials to call `sts:AssumeRoot`.

## Prerequisites
<a name="root-user-privileged-task_prerequisite"></a>

Before you can launch a privileged session, you must have the following settings:
+ You have enabled centralized root access in your organization. For steps to enable this feature, see [Centralize root access for member accounts](id_root-enable-root-access.md).
+ Your management account or delegated administrator account has the following permissions: `sts:AssumeRoot`

## Taking a privileged action on a member account (console)
<a name="root-user-privileged-task_action-console"></a>

**To launch a session for privileged action in a member account in the AWS Management Console**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the console, choose **Root access management**.

1. Select a name from the member account list, and choose **Take privileged action**.

1. Choose the privileged action you want to take in the member account.
   + Select **Delete Amazon S3 bucket policy** to remove a misconfigured bucket policy that denies all principals from accessing the Amazon S3 bucket.

     1. Choose **Browse S3** to select a name from the buckets owned by the member account, and select **Choose**.

     1. Choose **Delete bucket policy**.

     1. Use the Amazon S3 console to correct the bucket policy after deleting the misconfigured policy. For more information, see [Adding a bucket policy by using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html) in the *Amazon S3 User Guide*.
   + Select **Delete Amazon SQS policy** to delete an Amazon Simple Queue Service resource-based policy that denies all principals from accessing an Amazon SQS queue.

     1. Enter the queue name in **SQS queue name**, and select **Delete SQS policy**.

     1. Use the Amazon SQS console to correct the queue policy after deleting the misconfigured policy. For more information, see [Configuring an access policy in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-add-permissions.html) in the *Amazon SQS Developer Guide*.
   + Select **Delete root credentials** to remove root access from a member account. Deleting root user credentials removes the root user password, access keys, signing certificates, and deactivates multi-factor authentication (MFA) for the member account.

     1. Choose **Delete root credentials**.
   + Select **Allow password recovery** to recover root user credentials for a member account.

     This option is only available when the member account has no root user credentials.

     1. Choose **Allow password recovery**.

     1. After taking this privileged action, the person with access to the root user email inbox for the member account can [ reset the root user password](https://docs.aws.amazon.com/IAM/latest/UserGuide/reset-root-password.html) and sign in to the member account root user.

## Taking a privileged action on a member account (AWS CLI)
<a name="root-user-privileged-task_action-cli"></a>

**To launch a session for privileged action in a member account from the AWS Command Line Interface**

1. Use the following command to assume a root user session: [aws sts assume-root](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-root.html).
**Note**  
The global endpoint is not supported for `sts:AssumeRoot`. You must send this request to a Regional AWS STS endpoint. For more information, see [Manage AWS STS in an AWS Region](id_credentials_temp_enable-regions.md).

   When you launch a privileged root user session for a member account, you must define `task-policy-arn` to scope the session to the privileged action to be performed during the session. You can use one of following AWS managed policies to scope privileged session actions.
   + [IAMAuditRootUserCredentials](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMAuditRootUserCredentials)
   + [IAMCreateRootUserPassword](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMCreateRootUserPassword)
   + [IAMDeleteRootUserCredentials](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMDeleteRootUserCredentials)
   + [S3UnlockBucketPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-S3UnlockBucketPolicy)
   + [SQSUnlockQueuePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-SQSUnlockQueuePolicy)

   To limit the actions a management account or delegated administrator can perform during a privileged root user session, you can use the AWS STS condition key [sts:TaskPolicyArn](reference_policies_iam-condition-keys.md#ck_taskpolicyarn).

    In the following example, the delegated administrator assumes root to delete the root user credentials for the member account ID {{111122223333}}. 

   ```
   aws sts assume-root \
     --target-principal {{111122223333}} \
     --task-policy-arn arn={{arn:aws:iam::aws:policy/root-task/IAMDeleteRootUserCredentials}} \
     --duration-seconds {{900}}
   ```

1. Use the `SessionToken`, `AccessKeyId`, and `SecretAccessKey` from the response to perform privileged actions in the member account. You can omit the user name and password in the request to default to the member account.
   + **Check the status of root user credentials**. Use the following commands to check the status of root user credentials for a member account.
     + [get-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user.html)
     + [get-login-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-login-profile.html)
     + [list-access-keys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-access-keys.html)
     + [list-signing-certificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-signing-certificates.html)
     + [list-mfa-devices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-mfa-devices.html)
     + [get-access-key-last-used](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-access-key-last-used.html)
   + **Delete root user credentials**. Use the following commands to delete root access. You can remove the root user password, access keys, signing certificates, and deactivate multi-factor authentication (MFA) to remove all access to and recovery of the root user.
     + [delete-login-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-login-profile.html)
     + [delete-access-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-access-key.html)
     + [delete-signing-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html)
     + [deactivate-mfa-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/deactivate-mfa-device.html)
   + **Delete Amazon S3 bucket policy**. Use the following commands to read, edit, and delete a misconfigured bucket policy that denies all principals from accessing the Amazon S3 bucket.
     + [list-buckets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-buckets.html)
     + [get-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-policy.html)
     + [put-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-policy.html)
     + [delete-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-policy.html)
   + **Delete Amazon SQS policy**. Use the following commands to view and delete an Amazon Simple Queue Service resource-based policy that denies all principals from accessing an Amazon SQS queue.
     + [list-queues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/list-queues.html)
     + [get-queue-url](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-url.html)
     + [get-queue-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-attributes.html)
     + [set-queue-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/set-queue-attributes.html)
   + **Allow password recovery**. Use the following commands to view the user name and recover root user credentials for a member account.
     + [get-login-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-login-profile.html)
     + [create-login-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-login-profile.html)

## Taking a privileged action on a member account (AWS API)
<a name="root-user-privileged-task_action-api"></a>

**To launch a session for privileged action in a member account from the AWS API**

1. Use the following command to assume a root user session: [AssumeRoot](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html).
**Note**  
The global endpoint is not supported for AssumeRoot. You must send this request to a Regional AWS STS endpoint. For more information, see [Manage AWS STS in an AWS Region](id_credentials_temp_enable-regions.md).

   When you launch a privileged root user session for a member account, you must define `TaskPolicyArn` to scope the session to the privileged action to be performed during the session. You can use one of following AWS managed policies to scope privileged session actions.
   + [IAMAuditRootUserCredentials](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMAuditRootUserCredentials)
   + [IAMCreateRootUserPassword](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMCreateRootUserPassword)
   + [IAMDeleteRootUserCredentials](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMDeleteRootUserCredentials)
   + [S3UnlockBucketPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-S3UnlockBucketPolicy)
   + [SQSUnlockQueuePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-SQSUnlockQueuePolicy)

   To limit the actions a management account or delegated administrator can perform during a privileged root user session, you can use the AWS STS condition key [sts:TaskPolicyArn](reference_policies_iam-condition-keys.md#ck_taskpolicyarn).

   In the following example, the delegated administrator assumes root to read, edit and delete a misconfigured resource-based policy for an Amazon S3 bucket for the member account ID {{111122223333}}.

   ```
   https://sts.us-east-2.amazonaws.com/
     ?Version=2011-06-15
     &Action=AssumeRoot
     &TargetPrincipal={{111122223333}}
     &PolicyArns.arn={{arn:aws:iam::aws:policy/root-task/S3UnlockBucketPolicy}} 
     &DurationSeconds={{900}}
   ```

1. Use the `SessionToken`, `AccessKeyId`, and `SecretAccessKey` from the response to perform privileged actions in the member account. You can omit the user name and password in the request to default to the member account.
   + **Check the status of root user credentials**. Use the following commands to check the status of root user credentials for a member account.
     + [GetUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUser.html)
     + [GetLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetLoginProfile.html)
     + [ListAccessKeys](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html)
     + [ListSigningCertificates](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSigningCertificates.html)
     + [ListMFADevices](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListMFADevices.html)
     + [GetAccessKeyLastUsed](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccessKeyLastUsed.html)
   + **Delete root user credentials**. Use the following commands to delete root access. You can remove the root user password, access keys, signing certificates, and deactivate multi-factor authentication (MFA) to remove all access to and recovery of the root user.
     + [DeleteLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteLoginProfile.html)
     + [DeleteAccessKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteAccessKey.html)
     + [DeleteSigningCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteSigningCertificate.html)
     + [DeactivateMfaDevice](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeactivateMFADevice.html)
   + **Delete Amazon S3 bucket policy**. Use the following commands to read, edit, and delete a misconfigured bucket policy that denies all principals from accessing the Amazon S3 bucket.
     + [ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html)
     + [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html)
     + [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html)
     + [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html)
   + **Delete Amazon SQS policy**. Use the following commands to view and delete an Amazon Simple Queue Service resource-based policy that denies all principals from accessing an Amazon SQS queue.
     + [ListQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html)
     + [GetQueueUrl](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html)
     + [GetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html)
     + [SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html)
   + **Allow password recovery**. Use the following commands to view the user name and recover root user credentials for a member account.
     + [GetLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetLoginProfile.html)
     + [CreateLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateLoginProfile.html)