# Changing the Macie administrator account for an

invitation-based organization

###### Note

We recommend using AWS Organizations instead of Macie invitations to manage member
accounts. For more information, see [Managing multiple Macie accounts with AWS Organizations](accounts-mgmt-ao.md "accounts-mgmt-ao.md").

After you create and establish an invitation-based organization, you can change the
Amazon Macie administrator account for the organization. To do this, administrators and members of the
organization should take the following steps:

1. The current Macie administrator optionally exports the current inventory of member accounts for the
   organization. This simplifies the transition by helping you identify accounts that
   should continue to be part of the organization.
2. The current Macie administrator [removes all member accounts](accounts-mgmt-invitations-administer.md#accounts-mgmt-invitations-members-remove "accounts-mgmt-invitations-administer.md#accounts-mgmt-invitations-members-remove") from the current organization. This
   disassociates the accounts from the current administrator account. Macie continues
   to be enabled for the accounts but the accounts become standalone Macie
   accounts.

###### Important

When the current Macie administrator removes the member accounts, Macie automatically
disables automated sensitive data discovery for the accounts. This also disables access to statistical
data, inventory data, and other information that Macie produced and directly
provided while performing automated discovery for the accounts. When the transition to the
new organization is complete, the new Macie administrator can't access this data. 3. The new Macie administrator [adds the
previous member accounts](accounts-mgmt-invitations-administer.md#accounts-mgmt-invitations-members-add "accounts-mgmt-invitations-administer.md#accounts-mgmt-invitations-members-add") to the new organization. This associates the
accounts with the new administrator account. 4. Each member account accepts the invitation to join the new organization. When an account
accepts the invitation, the account becomes a member account in the new
organization. The new Macie administrator can then access Macie settings, data, and
resources for the account. If automated sensitive data discovery was previously enabled for the account,
this doesn't include data that Macie previously produced and directly provided while
performing automated discovery for the account. Instead, Macie generates and maintains new data
for the account, if the new Macie administrator enables automated discovery for the account.
If your organization uses Macie in multiple AWS Regions, perform the preceding steps in
each of those Regions.

To export the current inventory of member accounts, the current Macie administrator can use the
Amazon Macie console or the Amazon Macie API. With the console, the current administrator can
export the data to a comma-separated values (CSV) file. The new administrator can then use
the console to upload the CSV file and add all the accounts (in bulk) to the new
organization.

###### To export member account data by using the console

1. Sign in to the AWS Management Console using the current Macie administrator account.
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to export the data.
3. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
4. In the navigation pane, choose **Accounts**. The
   **Accounts** page opens and displays a table of the accounts
   that are associated with the current Macie administrator account.
5. (Optional) To filter the table and show only those accounts that are currently member
   accounts in the organization, use the filter box above the table to add the
   following filter conditions:
   - **Type** = **Invitation**
   - **Status** = **Enabled**
   - **Status** = **Paused**

6. In the table, select the checkbox for each member account to include in the exported
   data.
7. Choose **Export CSV**.
8. Specify a name and location for the file.
   With the Amazon Macie API, the current Macie administrator can retrieve the data in JSON format. The new
   Macie administrator can then use that data to generate the list of account IDs and email addresses
   for the accounts to add and invite to the new organization. To retrieve the data in JSON
   format, use the [ListMembers](../APIReference/members.md "../APIReference/members.md") operation of the Amazon Macie API. If the operation succeeds, Macie
   returns a `members` array that provides details about all the accounts that are
   associated with the administrator’s account. If an account is currently a member account,
   the value for the `relationshipStatus` property of the account is
   `Enabled` or `Paused`, and the `invitedAt` property
   specifies a date and time.
