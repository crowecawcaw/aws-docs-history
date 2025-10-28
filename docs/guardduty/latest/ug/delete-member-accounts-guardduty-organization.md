# Deleting member accounts

from GuardDuty organization

As a delegated GuardDuty administrator account, after you have disassociated a member account and you no longer want to
keep that member account in the GuardDuty organization, you can delete that member account
from your GuardDuty organization. This member account will no longer appear in your account
inventory. However, if GuardDuty was not suspended in this member account,
the configuration of GuardDuty and dedicated
protection plans remains the same. This account will now become a standalone account and can
[disable
GuardDuty](guardduty_suspend-disable.md "guardduty_suspend-disable.md") themselves.

This step will not delete the member account from your AWS organization.

Choose a preferred method to delete a member account from your GuardDuty
organization.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

To sign in, use the credentials of the delegated GuardDuty administrator account. 2. In the navigation pane, choose
**Accounts**. 3. In the **Accounts** table, you can remove an
account that has **Type** as **Via
Organizations** and **Status** as
**Removed (disassociated)**.

Select one or more accounts with the same
**Type** and
**Status**. 4. From the **Actions** dropdown menu, choose
**Delete account**. 5. Choose **Delete accounts** to confirm your
selection. The selected account member will no longer appear in your
Accounts table.

Repeat the preceding steps in each additional Region where you
want to delete this member account.

API/CLI

1. To retrieve the account ID for the member account that you want to
   delete, use the [ListMembers](../APIReference/API_ListMembers.md "../APIReference/API_ListMembers.md") API. Include the
   `OnlyAssociated` parameter in your request. If you
   set this parameter's value to `false`, GuardDuty returns a
   `members` array that provides details about only
   those accounts that are currently disassociated GuardDuty
   members.

Alternatively, you can use AWS Command Line Interface (AWS CLI) to run the following
command:

```
aws guardduty list-members --detector-id `12abc34d567e8fa901bc2d34EXAMPLE` --only-associated="false" --region `us-east-1`
```

Replace `12abc34d567e8fa901bc2d34EXAMPLE` with the delegated GuardDuty administrator account detector ID and `us-east-1` with the Region where
you want to remove this account. 2. To delete one or more GuardDuty member accounts, run [DeleteMembers](../APIReference/API_DeleteMembers.md "../APIReference/API_DeleteMembers.md") to delete the member
account from the GuardDuty organization.

Alternatively, you can use AWS CLI to run the following
command:

```
aws guardduty delete-members --detector-id `12abc34d567e8fa901bc2d34EXAMPLE` --account-ids `111122223333` --region `us-east-1`
```

Replace `12abc34d567e8fa901bc2d34EXAMPLE` with the delegated GuardDuty administrator account detector ID and `us-east-1` by the Region where
you want to remove this account. If you have a list of account IDs
that you want to remove, separate them by a space character.
