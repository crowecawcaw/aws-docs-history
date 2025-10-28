# Disassociating

(removing) member account from administrator account

When you want to stop configuring the GuardDuty settings and accessing the data from a
member account, remove that account as a GuardDuty member account. You can do it by
disassociating (removing) that account from the GuardDuty administrator account.

When you disassociate a GuardDuty member account, the following happens:

- GuardDuty remains enabled for the account in the current AWS Region, but the account becomes
  disassociated from the delegated GuardDuty administrator account.
- The disassociated account continues to show in the account inventory.
- The GuardDuty administrator account no longer has access to this standalone account's findings.
- The account owner is not notified of the disassociation.
  You can add the disassociated account to your organization again at a later time.

Choose a preferred method to disassociate (remove) a member account from your
organization.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

To sign in, use the credentials of the delegated GuardDuty administrator account. 2. In the navigation pane, choose
**Accounts**. 3. In the **Accounts** table, you can remove an
account that has **Type** as **Via
Organizations** and **Status** as
**Enabled**.

Select one or more accounts with the same
**Type** and
**Status**. 4. From the **Actions** dropdown menu, choose
**Disassociate account**. 5. Choose **Disassociate account** to confirm your
selection. 6. The **Status** value for the selected accounts
will change to **Not a member**. The **Via
Organizations (Active/All)** count at the top right
corner of the Accounts page will change to reflect the
update.

Repeat the preceding steps in each additional Region where you
want to disassociate the member account.

API

1. To retrieve the account ID for the member account that you want to
   remove, use the [ListMembers](../APIReference/API_ListMembers.md "../APIReference/API_ListMembers.md") API. Include the
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
you want to remove this account. 2. To remove one or more GuardDuty member accounts, run [DisassociateMembers](../APIReference/API_DisassociateMembers.md "../APIReference/API_DisassociateMembers.md") to remove the
member account that is associated with the administrator account.

Alternatively, you can use AWS CLI to run the following
command:

```
aws guardduty disassociate-members --detector-id 12abc34d567e8fa901bc2d34EXAMPLE --account-ids `111122223333` --region `us-east-1`
```

Replace `us-east-1` by the Region where
you want to remove this account. If you have a list of account IDs
that you want to remove, separate them by a space character.
