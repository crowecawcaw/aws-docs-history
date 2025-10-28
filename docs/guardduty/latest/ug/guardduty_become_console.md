# Adding accounts by invitation

As an administrator account that already has GuardDuty enabled, you can add members to start using
GuardDuty. After adding the members, you can invite them to join GuardDuty, and they can choose
to respond to your invitation.

###### Note

GuardDuty recommends using AWS Organizations instead of GuardDuty invitations, to manage your member accounts.
For more information, see [Managing accounts with
AWS Organizations](guardduty_organizations.md "guardduty_organizations.md").

Choose a preferred access method to add GuardDuty member accounts as a GuardDuty administrator account.

Console

###### Step 1 - Add an account

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Accounts**.
3. Choose **Add accounts by invitation** in the top
   pane.
4. On the **Add member accounts** page, under
   **Enter account details**, enter the
   AWS account ID and email address associated with the account that
   you want to add.
5. To add another row to enter account details one at a time, choose
   **Add another account**. You can also choose
   **Upload .csv file with account details** to
   add accounts in bulk.

###### Important

The first line of your csv file must contain the header, as
depicted in the following example – `Account
 ID,Email`. Each subsequent line must contain a single
valid AWS account ID and its associated email address. The
format of a row is valid if it contains only one AWS account
ID and the associated email address separated by a comma.

```
Account ID,Email
                                `555555555555`,`user@example.com`
```

6. After you have added all the accounts' details, choose
   **Next**. You can view the newly-added accounts
   in the Accounts table. The **Status** of these
   accounts will be **Invite not sent**. For
   information about sending an invite to one or more added accounts,
   see [Step 2 - Invite an account](#guardduty_invite_member_proc "#guardduty_invite_member_proc").

###### Step 2 - Invite an

account

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Accounts**.
3. Select one or more accounts that you want to invite to Amazon GuardDuty.
4. Choose **Actions** dropdown menu and then choose
   **Invite**.
5. In the **Invitation to GuardDuty** dialog box, enter
   an (optional) invitation message.

If the invited account does not have access to email, select the
checkbox **Also send an email notification to the root user on
the invitee's AWS account and generate an alert in the
invitee's AWS Health Dashboard**. 6. Choose **Send invitation**. If the invitees have
access to the specified email address they can view the invite by
opening the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/"). 7. When an invitee accepts the invite, the value in the
**Status** column changes to
**Invited**. For information about accepting an
invite, see [Step 3 - Accept an invitation](#guardduty_accept_invite_proc "#guardduty_accept_invite_proc").

###### Step 3 - Accept an

invitation

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

###### Important

You must enable GuardDuty before you can view or accept a
membership invitation. 2. Do the following only if you haven't enabled GuardDuty yet; otherwise,
you can skip this step and continue with the next step.

If you haven't yet enabled GuardDuty, choose **Get
Started** on the Amazon GuardDuty page.

On the **Welcome to GuardDuty** page, choose
**Enable GuardDuty**. 3. After you enable GuardDuty for your account, use the following steps
to accept the membership invitation:

    1. In the navigation pane, choose
     **Settings**.
    2. Choose **Accounts**.
    3. On the **Accounts**, ensure to verify the
     owner of the account from which you accept the invitation.
     Turn on **Accept** to accept the membership
     invite.

4. After you accept the invite, your account becomes a GuardDuty member
   account. The account whose owner sent the invitation becomes the
   GuardDuty administrator account. The administrator account will know that you have accepted the
   invitation. The **Accounts** table in their GuardDuty
   account will get updated. The value in the
   **Status** column corresponding to your member
   account ID will change to **Enabled**. The administrator account
   owner can now view and manage GuardDuty and protection plan
   configurations on behalf of your account. The administrator account can also view
   and manage GuardDuty findings generated for your member account.

API/CLI
You can designate a GuardDuty administrator account, and create or add GuardDuty member accounts
by invitation through the API operations. Run the following GuardDuty API
operations in order to designate administrator account and member accounts in
GuardDuty.

Complete the following procedure using the credentials of the
AWS account that you want to designate as the GuardDuty administrator account.

###### Creating

or adding member accounts

1. Run the [CreateMembers](../APIReference/API_CreateMembers.md "../APIReference/API_CreateMembers.md") API operation using the credentials of
   the AWS account that has GuardDuty enabled. This is the account that
   you want to be the administrator account GuardDuty account.

You must specify the detector ID of the current AWS account and
the account ID and email address of the accounts that you want to
become GuardDuty members. You can create one or more members with this
API operation.

You can also use AWS Command Line Tools to designate a administrator account
by running the following CLI command. Make sure to use your own
valid detector ID, account ID, and email.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty create-members --detector-id `12abc34d567e8fa901bc2d34e56789f0` --account-details AccountId=`111122223333`,Email=`guardduty-member@organization.com`
```

2. Run [InviteMembers](../APIReference/API_InviteMembers.md "../APIReference/API_InviteMembers.md") by using the
   credentials of the AWS account that has GuardDuty enabled. This is the
   account that you want to be the administrator account GuardDuty account.

You must specify the detector ID of the current AWS account and
the account IDs of the accounts that you want to become GuardDuty
members. You can invite one or more members with this API
operation.

###### Note

You can also specify an optional invitation message by using
the `message` request parameter.

You can also use AWS Command Line Interface to designate member accounts by running
the following command. Make sure to use your own valid detector ID
and valid account IDs for the accounts you want to invite.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty invite-members --detector-id `12abc34d567e8fa901bc2d34e56789f0` --account-ids `111122223333`
```

###### Accepting invitations

Complete the following procedure using the credentials of each AWS
account that you want to designate as a GuardDuty member account.

1. Run the [CreateDetector](../APIReference/API_CreateDetector.md "../APIReference/API_CreateDetector.md") API operation for
   each AWS account that was invited to become a GuardDuty member account
   and that you want to accept an invitation.

You must specify if the detector resource is to be enabled using
the GuardDuty service. A detector must be created and enabled in order
for GuardDuty to become operational. You must first enable GuardDuty before
accepting an invitation.

You can also do this by using AWS Command Line Tools using the
following CLI command.

```
aws guardduty create-detector --enable
```

2. Run the [AcceptAdministratorInvitation](../APIReference/API_AcceptAdministratorInvitation.md "../APIReference/API_AcceptAdministratorInvitation.md") API
   operation for each AWS account that you want to accept the
   membership invitation, using that account's credentials.

You must specify the detector ID of this AWS account for the
member account, the account ID of the administrator account that sent the
invitation, and the invitation ID of the invitation that you are
accepting. You can find the account ID of the administrator account in the
invitation email or by using the [ListInvitations](../APIReference/API_ListInvitations.md "../APIReference/API_ListInvitations.md") operation of the
API.

You can also accept an invitation using AWS Command Line Tools
by running the following CLI command. Make sure to use a valid
detector ID, administrator account ID, and an invitation ID.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty accept-invitation --detector-id `12abc34d567e8fa901bc2d34e56789f0` --administrator-id `444455556666` --invitation-id `84b097800250d17d1872b34c4daadcf5`
```
