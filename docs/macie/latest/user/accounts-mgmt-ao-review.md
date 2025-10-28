# Reviewing Macie accounts for an organization

After an AWS Organizations organization is [integrated and
configured](accounts-mgmt-ao-integrate.md "accounts-mgmt-ao-integrate.md") in Amazon Macie, the delegated Macie administrator can access an inventory of the
organization's accounts in Macie. As the Macie administrator for an organization, you can use this
inventory to review statistics and details for your organization's Macie accounts in an
AWS Region. You can also use it to [perform
certain management tasks](accounts-mgmt-ao-administer.md "accounts-mgmt-ao-administer.md") for the accounts.

###### To review the Macie accounts for an organization

To review the accounts for your organization, you can use the Amazon Macie console or the
Amazon Macie API. If you prefer to use the console, you must be allowed to perform the
following AWS Organizations action: `organizations:ListAccounts`. This action allows
you to retrieve and display information about accounts that are part of your
organization in AWS Organizations.

Console
Follow these steps to review your organization's Macie accounts by using the
Amazon Macie console.

###### To review your organization's accounts

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to review your organization's
   accounts.
3. In the navigation pane, choose **Accounts**.

The **Accounts** page opens and displays aggregated statistics
and a table of the accounts that are associated with your Macie account in the
current AWS Region.

At the top of the **Accounts** page, you'll find the following
aggregated statistics.

**Via AWS Organizations**

**Active** reports the total number of accounts that are
associated with your account through AWS Organizations and are currently Macie member
accounts in your organization. Macie is enabled for these accounts and
you’re the Macie administrator of the accounts.

**All** reports the total number of accounts that are associated with
your account through AWS Organizations. This includes accounts that aren’t
currently Macie member accounts. It also includes member accounts
that Macie is currently suspended for.

**By invitation**

**Active** reports the total number of accounts that are associated
with your account by Macie invitation and are currently Macie member
accounts in your organization. These accounts aren’t associated with
your account through AWS Organizations. Macie is enabled for the accounts and
you’re the Macie administrator of the accounts because they accepted a Macie
membership invitation from you.

**All** reports the total number of accounts that are
associated with your account by Macie invitation, including accounts that
haven’t responded to an invitation from you.

**Active/All**

**Active** reports the total number of accounts that Macie is
currently enabled for in your organization, including your own
account. You’re the Macie administrator of these accounts through AWS Organizations
or by Macie invitation.

**All** reports the total number of accounts that are associated with
your account, through AWS Organizations or by Macie invitation, plus your own
account. This includes accounts that are part of your organization
in AWS Organizations and aren’t currently Macie member accounts. It also
includes any accounts that haven’t responded to a Macie membership
invitation from you.

In the table, you’ll find details about each account in the current Region. The table
includes all the accounts that are associated with your Macie account through
AWS Organizations or by Macie invitation.

**Account ID**

The account ID and email address for the AWS account.

**Name**

The account name for the AWS account. This value is typically
**N/A** for your own account, and any accounts
that are associated with your account by Macie invitation.

**Type**

How the account is associated with your account, through AWS Organizations or by Macie
invitation. For your own account, this value is **Current
account**.

**Status**

The status of the relationship between your account and the
account. For an account in an AWS Organizations organization
(**Type** is **Via
AWS Organizations**), possible values are:

- **Account suspended** – The
  AWS account is suspended.
- **Enabled** – The account is a Macie member account. Macie is
  enabled for the account and you’re the Macie administrator of the
  account.
- **Enabling in process** – Macie is processing a request to
  enable and add the account as a Macie member account.
- **Not a member** – The account is
  part of your organization in AWS Organizations but it isn’t a Macie
  member account.
- **Paused (suspended)** – The
  account is a Macie member account but Macie is currently
  suspended for the account.
- **Region disabled** – The account
  is part of your organization in AWS Organizations but the current
  Region is disabled for the AWS account.
- **Removed (disassociated)** – The
  account was previously a Macie member account but was
  subsequently removed as a member account. You disassociated
  the account from your Macie administrator account. Macie continues to
  be enabled for the account.

**Last status update**

When you or the associated account most recently performed an
action that affected the relationship between your accounts.

**Automated sensitive data discovery**

Whether automated sensitive data discovery is currently enabled or disabled for the
account.

To sort the table by a specific field, choose the column heading for the field. To change
the sort order, choose the column heading again. To filter the table, place your
cursor in the filter box, and then add a filter condition for a field. To
further refine the results, add filter conditions for additional fields.

API
To review your organization’s accounts programmatically, use the [ListMembers](../APIReference/members.md "../APIReference/members.md") operation of the Amazon Macie API and specify the Region
that your request applies to. To review the accounts in additional Regions,
submit your request in each additional Region.

When you submit your request, use the `onlyAssociated` parameter to specify
which accounts to include in the response. By default, Macie returns details
about only those accounts that are Macie member accounts in the specified Region
through AWS Organizations or by Macie invitation. To retrieve these details for all the
accounts that are associated with your Macie account, including accounts that
aren’t member accounts, include the `onlyAssociated` parameter in
your request and set the parameter’s value to `false`.

To review your organization’s accounts by using the [AWS Command Line Interface (AWS CLI)](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md"), run
the [list-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-members.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-members.html") command. For the `only-associated` parameter,
specify whether to include all associated accounts or only Macie member accounts. To
include only member accounts, omit this parameter or set the parameter’s value to
`true`. To include all accounts, set this value to `false`.
For example:

```
`C:\>` `aws macie2 list-members --region `us-east-1` --only-associated false`
```

Where `us-east-1` is the Region that the request applies
to, the US East (N. Virginia) Region.

If your request succeeds, Macie returns a `members` array. The array
contains a `member` object for each account that meets the criteria
specified in the request. In that object, the `relationshipStatus` field
indicates the current status of the relationship between your account and the other
account in the specified Region. For an account in an AWS Organizations organization, possible
values are:

- `AccountSuspended` – The AWS account is
  suspended.
- `Created` – Macie is processing a request to enable and
  add the account as a Macie member account.
- `Enabled` – The account is a Macie member account. Macie is enabled
  for the account and you’re the Macie administrator of the account.
- `Paused` – The account is a Macie member account but Macie
  is currently suspended (paused) for the account.
- `RegionDisabled` – The account is part of your
  organization in AWS Organizations but the current Region is disabled for the
  AWS account.
- `Removed` – The account was previously a Macie member account but was
  subsequently removed as a member account. You disassociated the account
  from your Macie administrator account. Macie continues to be enabled for the
  account.

For information about other fields in the `member` object, see [Members](../APIReference/members.md "../APIReference/members.md")
in the _Amazon Macie API Reference_.
