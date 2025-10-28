# Adding members to the

organization

As a delegated GuardDuty administrator account, you can add one or more AWS accounts to the GuardDuty organization. When
you add an account as a GuardDuty member, it will automatically have GuardDuty enabled in that
Region. There is an exception to the organization management account. Before the
management account account gets added as a GuardDuty member, it must have GuardDuty
enabled.

Choose a preferred method to add a member account to your GuardDuty organization.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

To sign in, use the delegated GuardDuty administrator account credentials. 2. In the navigation pane, choose
**Accounts**.

The accounts table displays all the member accounts that are
active (not suspended AWS accounts) and may be associated with the
delegated GuardDuty administrator account. If the member account is associated with the organization's
administrator account, then the **Type** will be one of the
following: **Via Organizations** or **By
invitation**. If a member account is not associated
with the organization's GuardDuty administrator account, the **Type**
of this member account is **Not a member**. 3. Select one or more account IDs that you want to add as members.
These account IDs must have the **Type** as
**Via Organizations**.

Accounts that are added through invitation are not a part of your
organization. You can manage such accounts individually. For more
information, see [Managing accounts by
invitation](guardduty_invitations.md "guardduty_invitations.md"). 4. Choose the **Actions** dropdown, and then choose
**Add member**. After you add this account as a
member, the auto-enable GuardDuty configuration will apply. Based on the
settings in [Setting organization auto-enable
preferences](set-guardduty-auto-enable-preferences.md "set-guardduty-auto-enable-preferences.md"), the
GuardDuty configuration of these accounts may change. 5. You can select the down arrow of the **Status**
column to sort the accounts by the **Not a member**
status and then choose each account that doesn't have GuardDuty enabled
in the current Region.

If none of the accounts listed in the accounts table have been
added as a member yet, you can enable GuardDuty in the current Region
for all organization accounts. Choose **Enable** in
the banner at the top of the page. This action automatically turns
on the **Auto-enable** GuardDuty configuration so that
GuardDuty gets enabled for any new account that joins the
organization. 6. Choose **Confirm** to add the accounts as
members. This action also enables GuardDuty for all of the selected
accounts. The **Status** for the accounts will
change to **Enabled**. 7. (Recommended) Repeat these steps in each AWS Region. This
ensures that the delegated GuardDuty administrator account can manage findings and other
configurations for member accounts in all the Regions where you have
GuardDuty enabled.

The auto-enable feature enables GuardDuty for all future members of
your organization. This allows your delegated GuardDuty administrator account to manage any new
members that are created within or get added to the organization.
When the number of member accounts reaches the limit of 50,000, the
Auto-enable feature is automatically turned off. If you remove a
member account and the total number of members decreases to fewer
than 50,000, the Auto-enable feature turns back on.

API/CLI

- Run [CreateMembers](../APIReference/API_CreateMembers.md "../APIReference/API_CreateMembers.md") by using the
  credentials of the delegated GuardDuty administrator account.

You must specify the regional detector ID of the delegated GuardDuty administrator account and the
account details (AWS account IDs and corresponding email
addresses) of the accounts that you want to add as GuardDuty members.
You can create one or more members with this API operation.

When you run CreateMembers in your organization,
the auto-enable preferences for new members will apply as new member
accounts join your organization. When you run
CreateMembers with an existing member account,
the organization configuration will also apply to the existing
members. This might change the current configuration of the existing
member accounts.

Run [ListAccounts](../../../organizations/latest/APIReference/API_ListAccounts.md "../../../organizations/latest/APIReference/API_ListAccounts.md") in the
_AWS Organizations API Reference_, to view all the accounts in
the AWS organization.

    + Alternatively, you can use AWS Command Line Interface. Run the following
     AWS CLI command and make sure to use your own valid detector
     ID, AWS account ID, and the email address associated with
     the account ID.


    To find the `detectorId` for your account and current Region, see the
    **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
    or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.



    ```
    aws guardduty create-members --detector-id `12abc34d567e8fa901bc2d34e56789f0` --account-details AccountId=`111122223333`,Email=`guardduty-member-name@amazon.com`
    ```

    You can view a list of all organization members by running
     the following AWS CLI command:



    ```
    aws organizations list-accounts
    ```After you add this account as a member, the auto-enable GuardDuty

configuration will apply.
