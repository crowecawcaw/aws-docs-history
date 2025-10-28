# Managing Macie member accounts for an

organization

After an AWS Organizations organization is [integrated and
configured](accounts-mgmt-ao-integrate.md "accounts-mgmt-ao-integrate.md") in Amazon Macie, the organization’s delegated Macie administrator can access
certain Macie settings, data, and resources for member accounts. As the Macie administrator for an
organization, you can use Macie to centrally perform certain account management and
administration tasks for the accounts. For example, you can:

- Add and remove accounts as Macie member accounts.
- Manage the status of Macie for individual accounts, such as enable or suspend Macie for an
  account.
- Monitor Macie quotas and estimated usage costs for individual accounts and the organization
  overall.
  You can also review Amazon Simple Storage Service (Amazon S3) inventory data and policy findings for Macie member
  accounts. And you can discover sensitive data in S3 buckets that the accounts own. For a
  detailed list of tasks that you can perform, see [Macie administrator and member account
  relationships](accounts-mgmt-relationships.md "accounts-mgmt-relationships.md").

By default, Macie gives you visibility into relevant data and resources for all the Macie
member accounts in your organization. You can also drill down to review data and resources for
individual accounts. For example, if you [use the
Summary dashboard](monitoring-s3-dashboard.md "monitoring-s3-dashboard.md") to assess your organization’s Amazon S3 security posture, you can
filter the data by account. Similarly, if you [monitor
estimated usage costs](account-mgmt-costs.md "account-mgmt-costs.md"), you can access breakdowns of estimated costs for individual
member accounts.

In addition to tasks that are common to administrator and member accounts, you can perform
various administrative tasks for your organization.

###### Tasks

- [Adding member
  accounts](#accounts-mgmt-ao-members-add "#accounts-mgmt-ao-members-add")
- [Suspending Macie for member
  accounts](#accounts-mgmt-ao-members-suspend "#accounts-mgmt-ao-members-suspend")
- [Removing member
  accounts](#accounts-mgmt-ao-members-remove "#accounts-mgmt-ao-members-remove")
  As the Macie administrator for an organization, you can perform these tasks by using the Amazon Macie
  console or the Amazon Macie API. If you prefer to use the console, you must be allowed to
  perform the following AWS Organizations action: `organizations:ListAccounts`. This action
  allows you to retrieve and display information about accounts that are part of your
  organization in AWS Organizations.

## Adding Macie member accounts to an

organization

In some cases, you might need to manually add an account as an Amazon Macie member account.
This is the case for accounts that you previously removed (disassociated) as member
accounts. This is also the case if you didn’t configure Macie to [automatically enable and add new
member accounts](accounts-mgmt-ao-integrate.md#accounts-mgmt-ao-members-autoenable "accounts-mgmt-ao-integrate.md#accounts-mgmt-ao-members-autoenable") when accounts are added to your organization in
AWS Organizations.

When you add an account as a Macie member account:

- Macie is enabled for the account in the current AWS Region, if it isn’t
  already enabled in the Region.
- The account is associated with your Macie administrator account as a member account in
  the Region. The member account doesn’t receive an invitation or other
  notification that you established this relationship between your
  accounts.
- Automated sensitive data discovery might be enabled for the account in the Region. This depends
  on configuration settings that you specified for the organization. For more
  information, see [Configuring automated sensitive data discovery](discovery-asdd-account-manage.md "discovery-asdd-account-manage.md").

Note that you can’t add an account that’s already associated with another
Macie administrator account. The account must first disassociate from its current
administrator account. In addition, you can’t add the AWS Organizations management account as
a member account unless Macie is already enabled for the account. To learn about
additional requirements, see [Considerations for using Macie with
AWS Organizations](accounts-mgmt-ao-notes.md "accounts-mgmt-ao-notes.md").

###### To add a Macie member account to an organization

To add one or more Macie member accounts to your organization, you can use the
Amazon Macie console or the Amazon Macie API.

Console
Follow these steps to add one or more Macie member accounts by using the
Amazon Macie console.

###### To add a Macie member account

1.  Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2.  By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to add a member account.
3.  In the navigation pane, choose **Accounts**. The
    **Accounts** page opens and displays a table of
    the accounts that are associated with your account.
4.  (Optional) To more easily identify accounts that are part of your organization in
    AWS Organizations and aren’t Macie member accounts, use the filter box above
    the **Existing accounts** table to add the
    following filter conditions:

        * **Type = Organization**
        * **Status = Not a Member**

    To also display accounts that you previously removed and might
    want to add as member accounts, also add a **Status =
    Removed** filter condition.

5.  In the **Existing accounts** table, select the checkbox for each
    account that you want to add as a member account.
6.  On the **Actions** menu, choose **Add
    member**.
7.  Confirm that you want to add the selected accounts as member
    accounts.

After you confirm your selections, the status of the selected accounts
changes to **Enabling in process**, and then
**Enabled** in your account inventory.

To add a member account in additional Regions, repeat the preceding steps in each
additional Region.

API
To add one or more Macie member accounts programmatically, use the [CreateMember](../APIReference/members.md "../APIReference/members.md") operation of the Amazon Macie API.

When you submit your request, use the supported parameters to specify the
12-digit account ID and email address for each AWS account that you want
to add. Also specify the Region that the request applies to. To add an
account in additional Regions, submit your request in each additional
Region.

To retrieve the account ID and email address of an account to add, you can
correlate the output of the [ListAccounts](../../../organizations/latest/APIReference/API_ListAccounts.md "../../../organizations/latest/APIReference/API_ListAccounts.md") operation of the AWS Organizations API and the [ListMembers](../APIReference/members.md "../APIReference/members.md") operation of the Amazon Macie API. For the
**ListMembers** operation of the Macie API, include the
`onlyAssociated` parameter in your request and set the
parameter’s value to `false`. If the operation succeeds, Macie
returns a `members` array that provides details about all the
accounts that are associated with your Macie administrator account in the specified
Region, including accounts that aren't currently member accounts. Note the
following in the array:

- If the value for the `relationshipStatus` property of an account isn’t
  `Enabled` or `Paused`, the account is
  associated with your account but it isn’t a Macie member
  account.
- If an account isn’t included in the array but is included in the
  output of the **ListAccounts** operation of the
  AWS Organizations API, the account is part of your organization in AWS Organizations
  but it isn’t associated with your account and, therefore, isn’t a
  Macie member account.

To add a member account by using the AWS Command Line Interface (AWS CLI), run the [create-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-member.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-member.html") command. Use the `region` parameter to
specify the Region in which to add the account. Use the `account`
parameters to specify the account ID and email address for each account to
add. For example:

```
`C:\>` `aws macie2 create-member --region `us-east-1` --account={\"accountId\":\"`123456789012`\",\"email\":\"`janedoe@example.com`\"}`
```

Where `us-east-1` is the Region in
which to add the account as a member account (the US East (N. Virginia)
Region), and the `account` parameters specify the account ID
(`123456789012`) and email address
(`janedoe@example.com`) for the account.

If your request succeeds, the status (`relationshipStatus`) of
the specified account changes to `Enabled` in your account
inventory.

## Suspending Macie for member accounts in an

organization

As the Amazon Macie administrator for an organization in AWS Organizations, you can suspend Macie for a member
account in your organization. If you do this, you can also re-enable Macie for the
account at a later time.

When you suspend Macie for a member account:

- Macie loses access to and stops providing metadata about the account's Amazon S3 data
  in the current AWS Region.
- Macie stops performing all activities for the account in the Region. This includes
  monitoring S3 buckets for security and access control, performing automated sensitive data discovery,
  and running sensitive data discovery jobs that are currently in progress.
- Macie cancels all sensitive data discovery jobs that were created by the account in the
  Region. A job can't be resumed or restarted after it's cancelled. If you created
  jobs to analyze data that the member account owns, Macie doesn’t cancel your
  jobs. Instead, the jobs skip resources that are owned by the account.

While it's suspended, Macie retains the session identifier, settings, and resources that it
stores or maintains for the account in the applicable Region. Macie also retains certain
data for the account in the Region. For example, the account's findings remain intact
and aren't affected for up to 90 days. If automated sensitive data discovery was enabled for the account,
existing results also remain intact and aren't affected for up to 30 days. Your
organization doesn’t incur Macie charges for the account in that Region while Macie is
suspended for the account in the Region.

###### To suspend Macie for a member account in an organization

To suspend Macie for a member account in an organization, you can use the Amazon Macie
console or the Amazon Macie API.

Console
Follow these steps to suspend Macie for a member account by using the Amazon Macie
console.

###### To suspend Macie for a member account

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to suspend Macie for a member account.
3. In the navigation pane, choose **Accounts**. The
   **Accounts** page opens and displays a table of
   the accounts that are associated with your account.
4. In the **Existing accounts** table, select the checkbox for the
   account to suspend Macie for.
5. On the **Actions** menu, choose **Suspend
   Macie**.
6. Confirm that you want to suspend Macie for the account.

After you confirm the suspension, the status of the account changes to **Paused
(suspended)** in your account inventory. To suspend Macie for
the account in additional Regions, repeat the preceding steps in each
additional Region.

To later re-enable Macie for the account, return to the **Accounts**
page on the console. Select the checkbox for the account, and then choose
**Enable Macie** on the **Actions**
menu. To re-enable Macie for the account in additional Regions, repeat these
steps in each additional Region.

API
To suspend Macie for a member account programmatically, use the [UpdateMemberSession](../APIReference/macie-members-id.md "../APIReference/macie-members-id.md") operation of the Amazon Macie API. You can
also use this operation to later re-enable Macie for the account.

When you submit your request, use the `id` parameter to specify the 12-digit
account ID for the AWS account that you want to suspend Macie for. For the
`status` parameter, specify `PAUSED`. Also specify
the Region that the request applies to. To suspend Macie for the account in
additional Regions, submit your request in each additional Region.

To retrieve the account ID for the account, you can use the [ListMembers](../APIReference/members.md "../APIReference/members.md")
operation of the Amazon Macie API. If you do this, consider filtering the
results by including the `onlyAssociated` parameter in your
request. If you set this parameter’s value to `true`, Macie
returns a `members` array that provides details about only those
accounts that are currently member accounts.

To suspend Macie for a member account by using the AWS CLI, run the [update-member-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-member-session.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-member-session.html") command. Use the `region`
parameter to specify the Region in which to suspend Macie for the account.
Use the `id` parameter to specify the account ID for the account.
For the `status` parameter, specify `PAUSED`. For
example:

```
`C:\>` `aws macie2 update-member-session --region `us-east-1` --id `123456789012` --status PAUSED`
```

Where `us-east-1` is the Region in which to
suspend Macie (the US East (N. Virginia) Region),
`123456789012` is the account ID for the
account to suspend Macie for, and `PAUSED` is the new status of Macie
for the account.

If your request succeeds, Macie returns an empty response and the status of the specified
account changes to `Paused` in your account inventory. To later
re-enable Macie for the account, run the
**update-member-session** command again and specify
`ENABLED` for the `status` parameter.

## Removing Macie member accounts from an

organization

If you want to stop accessing Amazon Macie settings, data, and resources for a member
account, you can remove the account as a Macie member account. You do this by
disassociating the account from your Macie administrator account. Note that only you can do this
for a member account. An AWS Organizations member account can’t disassociate from its
Macie administrator account.

When you remove a Macie member account, Macie remains enabled for the account in the
current AWS Region. However, the account is disassociated from your Macie administrator account
and it becomes a standalone Macie account. This means that you lose access to all Macie
settings, data, and resources for the account, including metadata and policy findings
for the account’s Amazon S3 data. This also means that you can no longer use Macie to
discover sensitive data in S3 buckets that the account owns. If you already created
sensitive data discovery jobs to do this, the jobs skip buckets that the account owns.
If you enabled automated sensitive data discovery for the account, both you and the member account lose access
to statistical data, inventory data, and other information that Macie produced and
directly provided while performing automated discovery for the account.

After you remove a Macie member account, the account continues to appear in your
account inventory. Macie doesn't notify the account's owner that you removed the
account. Therefore, consider contacting the account owner to ensure that they begin
managing settings and resources for their account.

You can add the account to your organization again at a later time. If you do this and you
enable automated sensitive data discovery for the account again within 30 days, you also regain access to data
and information that Macie previously produced and directly provided while performing
automated discovery for the account. In addition, subsequent runs of your existing jobs start
including the account's S3 buckets again.

###### To remove a Macie member account from an organization

To remove a Macie member account from your organization, you can use the Amazon Macie
console or the Amazon Macie API.

Console
Follow these steps to remove a Macie member account by using the Amazon Macie
console.

###### To remove a Macie member account

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to remove a member account.
3. In the navigation pane, choose **Accounts**. The
   **Accounts** page opens and displays a table of
   the accounts that are associated with your account.
4. In the **Existing accounts** table, select the
   checkbox for the account that you want to remove as a member
   account.
5. On the **Actions** menu, choose
   **Disassociate account**.
6. Confirm that you want to remove the selected account as a member
   account.

After you confirm your selection, the status of the account changes to
**Removed (disassociated)** in your account
inventory.

To remove the member account in additional Regions, repeat the preceding
steps in each additional Region.

API
To remove a Macie member account programmatically, use the [DisassociateMember](../APIReference/members-disassociate-id.md "../APIReference/members-disassociate-id.md") operation of the Amazon Macie API.

When you submit your request, use the `id` parameter to specify
the 12-digit AWS account ID for the member account to remove. Also specify
the Region that the request applies to. To remove the account in additional
Regions, submit your request in each additional Region.

To retrieve the account ID for the member account to remove, you can use
the [ListMembers](../APIReference/members.md "../APIReference/members.md") operation of the Amazon Macie API. If you do this,
consider filtering the results by including the `onlyAssociated`
parameter in your request. If you set this parameter’s value to
`true`, Macie returns a `members` array that
provides details about only those accounts that are currently Macie member
accounts.

To remove a Macie member account by using the AWS CLI, run the [disassociate-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/disassociate-member.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/disassociate-member.html") command. Use the `region`
parameter to specify the Region in which to remove the account. Use the
`id` parameter to specify the account ID for the member
account to remove. For example:

```
`C:\>` `aws macie2 disassociate-member --region `us-east-1` --id `123456789012``
```

Where `us-east-1` is the Region in
which to remove the account (the US East (N. Virginia) Region) and
`123456789012` is the account ID for
the account to remove.

If your request succeeds, Macie returns an empty response and the status
of the specified account changes to `Removed` in your account
inventory.
