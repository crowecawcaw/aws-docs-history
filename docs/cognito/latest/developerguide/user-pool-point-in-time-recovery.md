

# Point-in-time recovery for user pools

With point-in-time recovery, you can restore the user data in your user pool to its state at a point in time in the past. Use point-in-time recovery when users, their attributes, or their sign-in credentials are deleted or modified by mistake, for example by an administrative script, an application bug, or unauthorized activity in your AWS account. Point-in-time recovery restores the MFA settings and passkeys of users, and the passwords of deleted users, so recovered users can sign in with their existing credentials and don't have to reset their passwords.

A point-in-time recovery is a two-step process. First, you initiate a recovery to a recovery point that you choose. Amazon Cognito pauses write operations (rejects requests that modify the user pool or its users) and then generates a recovery preview that shows how many entities the recovery creates, updates, and deletes. Then, you review the preview and either start the recovery or cancel it. Amazon Cognito doesn't change your user pool data until you start the recovery.

Amazon Cognito restores user data in place, in the same user pool. The user pool keeps its ID, ARN, and configuration. You can't restore user data to a new user pool, to another AWS Region, or to another AWS account.

**Important**  
Point-in-time recovery is a disaster recovery feature. When you initiate a recovery, Amazon Cognito pauses all write operations in the user pool, starting with the generation of the recovery preview and before you decide whether to apply the recovery. When you apply a recovery, Amazon Cognito reverts all changes to user data after the recovery point. Use it to recover from accidental or unauthorized changes that affect your user data, for example the deletion or corruption of many users. Point-in-time recovery isn't a routine tool to remove users that were created recently or to revert changes to individual users. To delete or update individual users, use operations like [AdminDeleteUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDeleteUser.html) and [AdminUpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.html).

## Things to know about point-in-time recovery
<a name="user-pool-point-in-time-recovery-things-to-know"></a>
+ Point-in-time recovery is available in user pools on the Essentials and Plus [feature plans](cognito-sign-in-feature-plans.md).
+ Point-in-time recovery is enabled automatically in eligible user pools.
+ The feature plan of your user pool determines how far back in time you can recover. For more information, see [Recovery window and feature plans](#user-pool-point-in-time-recovery-window).
+ The recovery point must be at least 15 minutes in the past and can't be earlier than the creation time of the user pool.
+ After you initiate a recovery, you have 24 hours to start or cancel the recovery. If you don't start or cancel the recovery within 24 hours, the recovery preview expires, and Amazon Cognito resumes write operations without changing your user pool data.
+ From the time that you initiate a recovery until the recovery ends, Amazon Cognito blocks operations that write to the user pool. Sign-in and read operations continue to work, with some exceptions. For more information, see [User pool behavior during a recovery](#user-pool-point-in-time-recovery-during).
+ Point-in-time recovery restores user data only, not user pool configuration. For more information, see [What point-in-time recovery restores](#user-pool-point-in-time-recovery-scope).
+ You can't initiate a recovery while a [user import job](cognito-user-pools-import-users.md) is in progress in your user pool. Wait for the import job to complete, or stop it, and then initiate the recovery.
+ In a user pool with [multi-Region replication](user-pool-multi-region.md), you can initiate a recovery only in the primary AWS Region, and only when no replication changes are in progress. For example, if you created a replica user pool and its status isn't yet `ACTIVE` or `INACTIVE`, Amazon Cognito returns an error when you initiate a recovery. Wait for the replication to complete, and then initiate the recovery again. Amazon Cognito replicates the restored user data to your replica user pools.
+ If your user pool uses a customer managed key in AWS KMS for [encryption](data-protection.md#data-encryption), the key must remain enabled and accessible to Amazon Cognito for the duration of the recovery.
+ Some user pools don't support point-in-time recovery, for example some older user pools and user pools that contain user data with characters or formats that point-in-time recovery doesn't support. If your user pool doesn't support it, Amazon Cognito returns an error when you initiate a recovery. In the Amazon Cognito console, the **Initiate recovery** button is unavailable for these user pools, and the **Point-in-time recovery** page shows the message **Point-in-time recovery isn't available for this user pool**. If your user pool doesn't support point-in-time recovery, contact AWS Support for help with this limitation.
+ To monitor a recovery, check its status in the Amazon Cognito console or with a [DescribePointInTimeRecovery](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribePointInTimeRecovery.html) request.

## Recovery window and feature plans
<a name="user-pool-point-in-time-recovery-window"></a>

The recovery window is the period of time in the past that you can choose a recovery point from. The length of the recovery window depends on the feature plan of your user pool.


**Recovery window by feature plan**  

| Feature plan | Maximum recovery window | 
| --- | --- | 
| Lite | Not available | 
| Essentials | 1 day | 
| Plus | 14 days | 

Your recovery window begins when your user pool starts to use a feature plan that includes it, and can't be longer than the maximum for that feature plan. For example, you can recover to a point in time 14 days in the past only if your user pool has been on the Plus feature plan for the past 14 days without interruption. When your user pool leaves a feature plan, it loses the recovery window that it had on that feature plan. The following examples show how changes to your feature plan affect the recovery window:
+ When you change your user pool from the Lite feature plan to the Essentials or Plus feature plan, your recovery window starts at the time of the change. You can't recover to a point in time before the change.
+ When you change your user pool from the Essentials to the Plus feature plan, your Plus recovery window starts at the time of the change. Until your Plus recovery window is longer than 1 day, you can still recover up to 1 day in the past. For example, 5 days after you change to the Plus feature plan, you can recover to a point in time up to 5 days in the past. After 14 days, you can recover to any point in time in the past 14 days.
+ When you change your user pool from the Plus to the Essentials feature plan, your recovery window changes immediately to the 1-day window of the Essentials feature plan. If you later change back to the Plus feature plan, your Plus recovery window starts again at the time of that change, as if you had never used the Plus feature plan. For example, if your user pool was on the Plus feature plan for 30 days, then on the Essentials feature plan, and then on the Plus feature plan again, you can recover up to 1 day in the past right after the last change.
+ When you change your user pool from the Essentials or Plus feature plan to the Lite feature plan, point-in-time recovery isn't available, and your user pool loses its recovery window. If you later change back to the Essentials or Plus feature plan, your recovery window starts at the time of that change.

## What point-in-time recovery restores
<a name="user-pool-point-in-time-recovery-scope"></a>

A point-in-time recovery reverts changes to user data that occurred between the recovery point and the time that you initiated the recovery. Users that were deleted after the recovery point are re-created, users that were created after the recovery point are deleted, and users that were modified after the recovery point are reverted to their state at the recovery point.

Point-in-time recovery restores the following user data:
+ User profiles, including standard and custom attribute values
+ Groups and group memberships
+ Passwords of re-created users. When Amazon Cognito re-creates a user that was deleted after the recovery point, it also restores the password of the user.
+ User MFA settings, including authenticator app (TOTP) MFA
+ Passkeys

**Note**  
Point-in-time recovery doesn't revert password changes. Users who changed their password after the recovery point keep their existing password. To require users to reset their password after a recovery, use the [AdminResetUserPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.html) API operation.

The following resources and settings aren't restored and keep their current state after a recovery:
+ User pool configuration, including the attribute schema, password and MFA policies, Lambda triggers, message templates, threat protection settings, and multi-Region replication settings
+ App clients and client secrets
+ Identity providers and resource servers
+ Domains, managed login branding, and classic hosted UI customization
+ Encryption settings, including customer managed keys
+ Log delivery configuration and AWS WAF web ACL associations
+ Remembered devices and user authentication event history
+ User sessions, issued and revoked tokens, and one-time codes
+ User import jobs

## User pool behavior during a recovery
<a name="user-pool-point-in-time-recovery-during"></a>

When you initiate a recovery, Amazon Cognito pauses write operations in the user pool. Writes stay paused while Amazon Cognito waits for available capacity and generates the recovery preview, while the preview waits for you to start or cancel the recovery, and while Amazon Cognito restores your user data. The 24-hour period to start or cancel the recovery begins when you initiate it, and includes the time that Amazon Cognito waits for available capacity. The time that it takes Amazon Cognito to generate a recovery preview doesn't depend on the size of your user pool.

While write operations are paused, the following behavior applies to your user pool:
+ Amazon Cognito rejects operations that modify the user pool, its users, or its configuration, for example user sign-up, user creation and deletion, attribute updates, password changes, and changes to user pool settings. You also can't delete the user pool. Requests that you sign with AWS credentials return a `ValidationException` error. Requests from users return a `ForbiddenException` error.
+ Existing users can sign in, refresh tokens, and sign out. Read operations like `AdminGetUser`, `ListUsers`, and `DescribeUserPool` continue to work.
+ Users who must set a new password, set up MFA, or respond to an authenticator app (TOTP) MFA challenge can't complete sign-in. Sign-in with the `NEW_PASSWORD_REQUIRED`, `MFA_SETUP`, and `SOFTWARE_TOKEN_MFA` challenges fails until the recovery ends.
+ Federated users can sign in only if they have previously signed in to the user pool and their attributes from the external identity provider haven't changed.
+ You can't create or start [user import jobs](cognito-user-pools-import-users.md). Start your import jobs after the recovery ends.

We recommend that you prepare your applications for this period. For example, display a maintenance message in place of sign-up and profile update options.

## Point-in-time recovery limits
<a name="user-pool-point-in-time-recovery-limits"></a>

The following limits apply to point-in-time recovery, and Amazon Cognito returns a `LimitExceededException` error when you exceed them:
+ A user pool can have one active recovery at a time.
+ You can complete one recovery of a user pool in a 24-hour period.
+ You can initiate up to three recoveries of a user pool in a 24-hour period, including recoveries that you cancel or that expire.
+ You can initiate up to ten recoveries of a user pool in a 30-day period, including recoveries that you cancel or that expire.
+ An AWS account can have up to five active recoveries at a time across all of its user pools.
+ An organization in AWS Organizations can have up to ten active recoveries at a time across all of its accounts.
+ You can initiate up to ten recoveries in an AWS account in a 24-hour period, across all of its user pools and including recoveries that you cancel or that expire.
+ You can initiate up to 15 recoveries in an organization in AWS Organizations in a 24-hour period, across all of its accounts and including recoveries that you cancel or that expire.

To request an increase to the account or organization limits, contact AWS Support.

## Recovery statuses
<a name="user-pool-point-in-time-recovery-statuses"></a>

A recovery has one of the following statuses:


**Point-in-time recovery statuses**  

| Status | Description | Write operations | 
| --- | --- | --- | 
| PREVIEW\_GENERATING | Amazon Cognito is waiting for available capacity or is generating the recovery preview. | Paused | 
| PREVIEW\_GENERATED | The recovery preview is ready. Start or cancel the recovery within 24 hours after you initiated it. | Paused | 
| PREVIEW\_CANCELLED | You canceled the recovery. Amazon Cognito didn't change your user pool data. | Resumed | 
| PREVIEW\_EXPIRED | You didn't start or cancel the recovery within 24 hours after you initiated it. Amazon Cognito didn't change your user pool data. | Resumed | 
| PREVIEW\_GENERATION\_FAILED | Amazon Cognito couldn't generate the recovery preview. Amazon Cognito didn't change your user pool data. You can initiate a new recovery. | Resumed | 
| RESTORING | Amazon Cognito is restoring your user data to its state at the recovery point. You can't cancel the recovery. | Paused | 
| RESTORE\_COMPLETED | Amazon Cognito restored your user data to its state at the recovery point. | Resumed | 
| TEMPORARY\_INTERNAL\_ERROR\_SEE\_SUPPORT\_CASE | The recovery encountered an internal error. In the unlikely event of this status, AWS Support contacts you through a support case to resolve the issue. | Paused | 
| AWS\_ABORTED | Amazon Cognito stopped the recovery because of an internal failure. You can't cancel or retry the recovery. In the unlikely event of this status, AWS Support contacts you through a support case to resolve the issue. | Paused | 

## Recovering a user pool to a point in time
<a name="user-pool-point-in-time-recovery-recover"></a>

To recover a user pool, initiate a recovery, review the recovery preview, and then start or cancel the recovery.

------
#### [ AWS Management Console ]

**To recover a user pool to a point in time**

1. Sign in to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).

1. Choose **User pools**, and then choose your user pool.

1. In the navigation menu, under **Settings**, choose **Point-in-time recovery**.

1. In the **Recovery** section, choose **Initiate recovery**.

1. Under **Recovery configuration**, for **Target recovery date and time**, enter the date and time of the recovery point. The page shows the **Earliest recovery point** and the **Latest recovery point** that you can choose.

1. Review the warning that Amazon Cognito pauses write operations in the user pool, and then choose **Initiate recovery**.

1. To open the recovery, in the **Recovery** section, choose **View recovery**, or choose its ID in **Recovery history**.

1. When the status changes to **Ready to recover**, review the **Affected entities** table. For each entity type, the table shows the number of entities that the recovery creates, updates, and deletes.

1. Choose one of the following options:
   + To apply the recovery, choose **Approve recovery**, and then confirm your choice.
   + To discard the recovery and resume write operations without changes, choose **Cancel recovery**, and then confirm your choice.

1. After you approve the recovery, monitor its status until it changes to **Recovery completed**.

------
#### [ AWS CLI ]

**To recover a user pool to a point in time**

1. Initiate a recovery with the `initiate-point-in-time-recovery` command. The following example initiates a recovery to October 7, 2026 at 12:00 UTC.

   ```bash
   aws cognito-idp initiate-point-in-time-recovery \
       --user-pool-id {{us-east-1_EXAMPLE}} \
       --restore-timestamp {{2026-10-07T12:00:00Z}}
   ```

   The response includes the ID of the recovery.

   ```json
   {
       "Restoration": {
           "RestoreId": "a1b2c3d4-5678-90ab-cdef-111111111111",
           "RestoreStatus": "PREVIEW_GENERATING",
           "RestoreTimestamp": "2026-10-07T12:00:00+00:00",
           "TriggerTimestamp": "2026-10-08T15:30:00+00:00"
       }
   }
   ```

1. Check the status of the recovery and review the recovery preview with the `describe-point-in-time-recovery` command.

   ```bash
   aws cognito-idp describe-point-in-time-recovery \
       --user-pool-id {{us-east-1_EXAMPLE}} \
       --restore-id {{a1b2c3d4-5678-90ab-cdef-111111111111}}
   ```

   When the status is `PREVIEW_GENERATED`, the response includes the recovery preview. For each type of entity, the preview shows the number of entities that the recovery creates, updates, and deletes.

   ```json
   {
       "Restoration": {
           "RestoreId": "a1b2c3d4-5678-90ab-cdef-111111111111",
           "RestorePreview": [
               {
                   "CreateCount": 12,
                   "DeleteCount": 3,
                   "Entity": "Users",
                   "UpdateCount": 40
               },
               {
                   "CreateCount": 1,
                   "DeleteCount": 0,
                   "Entity": "Groups",
                   "UpdateCount": 2
               },
               {
                   "CreateCount": 10,
                   "DeleteCount": 2,
                   "Entity": "User MFAs",
                   "UpdateCount": 5
               },
               {
                   "CreateCount": 4,
                   "DeleteCount": 1,
                   "Entity": "Passkeys",
                   "UpdateCount": 0
               }
           ],
           "RestoreStatus": "PREVIEW_GENERATED",
           "RestoreTimestamp": "2026-10-07T12:00:00+00:00",
           "TriggerTimestamp": "2026-10-08T15:30:00+00:00"
       }
   }
   ```

1. Start or cancel the recovery.
   + To apply the recovery, use the `start-point-in-time-recovery` command.

     ```bash
     aws cognito-idp start-point-in-time-recovery \
         --user-pool-id {{us-east-1_EXAMPLE}} \
         --restore-id {{a1b2c3d4-5678-90ab-cdef-111111111111}}
     ```
   + To discard the recovery and resume write operations without changes, use the `cancel-point-in-time-recovery` command.

     ```bash
     aws cognito-idp cancel-point-in-time-recovery \
         --user-pool-id {{us-east-1_EXAMPLE}} \
         --restore-id {{a1b2c3d4-5678-90ab-cdef-111111111111}}
     ```

1. After you start the recovery, check its status with the `describe-point-in-time-recovery` command until the status is `RESTORE_COMPLETED`. To list the current and past recoveries of a user pool, use the `list-point-in-time-recoveries` command.

   ```bash
   aws cognito-idp list-point-in-time-recoveries \
       --user-pool-id {{us-east-1_EXAMPLE}}
   ```

------
#### [ API ]

Use the following Amazon Cognito API operations to recover a user pool:
+ [InitiatePointInTimeRecovery](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiatePointInTimeRecovery.html) – Pauses write operations and generates a recovery preview for the recovery point that you specify.
+ [DescribePointInTimeRecovery](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribePointInTimeRecovery.html) – Returns the status and recovery preview of a recovery.
+ [StartPointInTimeRecovery](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_StartPointInTimeRecovery.html) – Applies a recovery after you review its preview.
+ [CancelPointInTimeRecovery](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CancelPointInTimeRecovery.html) – Discards a recovery before you start it and resumes write operations.
+ [ListPointInTimeRecoveries](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListPointInTimeRecoveries.html) – Lists the current and past recoveries of a user pool.

------

## Permissions for point-in-time recovery
<a name="user-pool-point-in-time-recovery-permissions"></a>

To manage point-in-time recoveries, your IAM principal needs permissions for the following actions on the user pool resource `arn:{{aws}}:cognito-idp:{{region}}:{{account-id}}:userpool/{{user-pool-id}}`:
+ `cognito-idp:InitiatePointInTimeRecovery`
+ `cognito-idp:DescribePointInTimeRecovery`
+ `cognito-idp:StartPointInTimeRecovery`
+ `cognito-idp:CancelPointInTimeRecovery`
+ `cognito-idp:ListPointInTimeRecoveries`

The `AmazonCognitoPowerUser` AWS managed policy includes all of these permissions. The `AmazonCognitoReadOnly` AWS managed policy includes the `DescribePointInTimeRecovery` and `ListPointInTimeRecoveries` permissions. For more information, see [AWS managed policies for Amazon Cognito](security-iam-awsmanpol.md).

**Important**  
A principal that can initiate a recovery can pause write operations in your user pool for up to 24 hours, and a principal that can start a recovery can revert changes to your user data. Grant `InitiatePointInTimeRecovery` and `StartPointInTimeRecovery` permissions only to trusted administrators.

The following example identity-based policy allows a principal to view the recoveries of all user pools in an AWS account, and to initiate, start, and cancel recoveries of one user pool.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewPointInTimeRecoveries",
            "Effect": "Allow",
            "Action": [
                "cognito-idp:DescribePointInTimeRecovery",
                "cognito-idp:ListPointInTimeRecoveries"
            ],
            "Resource": "arn:{{aws}}:cognito-idp:{{us-east-1}}:{{111122223333}}:userpool/*"
        },
        {
            "Sid": "ManagePointInTimeRecoveries",
            "Effect": "Allow",
            "Action": [
                "cognito-idp:InitiatePointInTimeRecovery",
                "cognito-idp:StartPointInTimeRecovery",
                "cognito-idp:CancelPointInTimeRecovery"
            ],
            "Resource": "arn:{{aws}}:cognito-idp:{{us-east-1}}:{{111122223333}}:userpool/{{us-east-1_EXAMPLE}}"
        }
    ]
}
```

**Note**  
If your user pool uses a customer managed key in AWS KMS for encryption at rest, the principals that manage recoveries also need AWS KMS permissions to use the key through Amazon Cognito. Grant these permissions in the key policy of your KMS key or in IAM policies. For more information, see [Encryption at rest](data-protection.md#data-encryption-at-rest).

## Monitoring point-in-time recovery with CloudTrail
<a name="user-pool-point-in-time-recovery-cloudtrail"></a>

CloudTrail records point-in-time recovery API operations as management events. `InitiatePointInTimeRecovery`, `StartPointInTimeRecovery`, and `CancelPointInTimeRecovery` are write events. `DescribePointInTimeRecovery` and `ListPointInTimeRecoveries` are read-only events.

When Amazon Cognito applies a recovery, CloudTrail also records a `CognitoPointInTimeRecovery` service event for each user, group, and group membership that the recovery creates, updates, or deletes. Use these events to audit the changes that a recovery made to your user pool. For more information, see [Amazon Cognito logging in AWS CloudTrail](logging-using-cloudtrail.md).