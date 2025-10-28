# Suspending GuardDuty for

member account

As a delegated GuardDuty administrator account, you can suspend the GuardDuty service for a member account in your
organization. If you do this, the member account stills stays in your GuardDuty
organization. You can also re-enable GuardDuty for these member accounts at a later time.
However, if you eventually want to disassociate (remove) this member account, then
**after** following the steps in this section, you must
follow the steps in [Disassociating
(removing) member account from administrator account](disassociate-remove-member-account-from-admin.md "disassociate-remove-member-account-from-admin.md").

When you suspend GuardDuty in a member account, you can expect the following
changes:

- GuardDuty no longer monitors the security of the AWS environment, or generates
  new findings.
- The existing findings in the member account remain intact.
- A GuardDuty suspended member account does't incur any charges for
  GuardDuty.

If the member account has enabled Malware Protection for S3 for one or more buckets in their
account, then suspending GuardDuty doesn't impact the configuration of
Malware Protection for S3. The member account will continue incurring the usage cost for
Malware Protection for S3. For the member account to stop using Malware Protection for S3, they must disable
this feature for the protected buckets. For more information, see [Disabling Malware Protection for S3 for a protected
bucket](disable-malware-s3-protected-bucket.md "disable-malware-s3-protected-bucket.md").
Choose a preferred method to suspend GuardDuty for a member account in your
organization.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

To sign in, use the credentials of the delegated GuardDuty administrator account. 2. In the navigation pane, choose
**Accounts**. 3. In the Accounts page, select one or more accounts for which you
want to suspend GuardDuty. 4. Choose the **Actions** dropdown menu and then,
choose **Suspend GuardDuty**. 5. Choose **Suspend GuardDuty** to confirm the
selection.

This will change the **Status** of the member
account to **Disabled (suspended)**.

Repeat the preceding steps in each additional Region where you
want to disassociate or remove the member account.

API

1. To retrieve the member account account ID for which you want to
   suspend GuardDuty, use the [ListMembers](../APIReference/API_ListMembers.md "../APIReference/API_ListMembers.md") API. Include the
   `OnlyAssociated` parameter in your request. If you
   set this parameter's value to `true`, GuardDuty returns a
   `members` array that provides details about only
   those accounts that are currently GuardDuty members.

Alternatively, you can use AWS Command Line Interface (AWS CLI) to run the following
command:

```
aws guardduty list-members --only-associated true --region `us-east-1`
```

Replace `us-east-1` by the Region where
you want to suspend GuardDuty for this account. 2. To suspend one or more GuardDuty member accounts, run [StopMonitoringMembers](../APIReference/API_StopMonitoringMembers.md "../APIReference/API_StopMonitoringMembers.md") to suspend
GuardDuty for a member account.

Alternatively, you can use AWS CLI to run the following
command:

```
aws guardduty stop-monitoring-members --detector-id 12abc34d567e8fa901bc2d34EXAMPLE --account-ids `111122223333` --region `us-east-1`
```

Replace `us-east-1` by the Region where
you want to suspend this account. If you have a list of account IDs
that you want to remove, separate them by a space character.

If you further want to disassociate (remove) this member account, then follow the
steps in [Disassociating
(removing) member account from administrator account](disassociate-remove-member-account-from-admin.md "disassociate-remove-member-account-from-admin.md").
