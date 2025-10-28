# Reviewing Macie accounts for an

invitation-based organization

###### Note

We recommend using AWS Organizations instead of Macie invitations to manage member
accounts. For more information, see [Managing multiple Macie accounts with AWS Organizations](accounts-mgmt-ao.md "accounts-mgmt-ao.md").

If you're the Amazon Macie administrator for an invitation-based organization, Macie provides you with
an inventory of the accounts that are associated with your Macie account in each
AWS Region where you use Macie. You can use this inventory to review account statistics
and details for your organization. You can also use it to [perform certain management tasks](accounts-mgmt-invitations-administer.md "accounts-mgmt-invitations-administer.md")
for member accounts, and manage the status of the relationship between your account and
other accounts.

###### To review accounts for an invitation-based organization

To review the accounts in your organization, you can use the Amazon Macie console or the
Amazon Macie API.

Console
Follow these steps to review your organization's accounts by using the Amazon Macie
console.

###### To review your organization's accounts

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to review your organization's accounts.
3. In the navigation pane, choose **Accounts**.

The **Accounts** page opens and displays aggregated statistics and a
table of the accounts that are associated with your Macie account in the current
AWS Region.

At the top of the **Accounts** page, you'll find the following
aggregated statistics.

**Via AWS Organizations**

If you're the Macie administrator for an organization in AWS Organizations, **Active**
reports the total number of accounts that are associated with your account
through AWS Organizations and are currently Macie member accounts in your
organization. Macie is enabled for these accounts and you’re the Macie administrator
of the accounts.

**All** reports the total number of accounts that are associated with
your account through AWS Organizations. This includes accounts that aren’t
currently Macie member accounts. It also includes member accounts
that Macie is currently suspended for.

**By invitation**

**Active** reports the total number of accounts that are currently
Macie member accounts in your invitation-based organization. Macie is
enabled for these accounts and you’re the Macie administrator of the accounts
because they accepted a membership invitation from you.

**All** reports the total number of accounts that are
associated with your account by Macie invitation, including accounts that
haven’t responded to an invitation from you.

**Active/All**

**Active** reports the total number of accounts that Macie is
currently enabled for in your organization, including your own
account. You’re the Macie administrator of these accounts through AWS Organizations
or by Macie invitation.

**All** reports the total number of accounts that are associated with
your account, through AWS Organizations or by invitation, plus your own
account. This includes accounts that haven’t responded to a Macie
membership invitation from you. It also includes accounts that are
associated with your account through AWS Organizations and aren’t currently
Macie member accounts.

In the table, you’ll find details about each account in the current Region. The table
includes all the accounts that are associated with your Macie account by Macie
invitation or through AWS Organizations.

**Account ID**

The account ID and email address for the AWS account.

**Name**

The account name for the AWS account. This value is typically
**N/A** for your own account, and accounts that
are associated with your account by invitation.

**Type**

How the account is associated with your account, by invitation or through AWS Organizations. For
your own account, this value is **Current
account**.

**Status**

The status of the relationship between your account and the
account. For an account in an invitation-based organization
(**Type** is **By
invitation**), possible values are:

- **Account suspended** – The
  AWS account is suspended.
- **Created (Invite)** – You added
  the account but haven’t sent a membership invitation to
  it.
- **Email verification failed** –
  You tried to send a membership invitation to the account but
  the specified email address isn’t valid for the
  account.
- **Email verification in progress**
  – You sent a membership invitation to the account and
  Macie is processing the request.
- **Enabled** – The account is a
  member account. Macie is enabled for the account and you’re
  the Macie administrator of the account.
- **Invited** – You sent a
  membership invitation to the account and the account hasn’t
  responded to your invitation.
- **Member resigned** – The account
  was previously a member account. However, the account
  resigned from your organization by disassociating from your
  account.
- **Paused (suspended)** – The
  account is a member account but Macie is currently suspended
  for the account.
- **Region disabled** – The current
  Region is disabled for the AWS account.
- **Removed (disassociated)** – The
  account was previously a member account. However, you
  removed it as a member account by disassociating it from
  your account.

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
To review your organization's accounts programmatically, use the [ListMembers](../APIReference/members.md "../APIReference/members.md") operation of the Amazon Macie API and specify the Region
that your request applies to. To review the details in additional Regions,
submit your request in each additional Region.

When you submit your request, use the `onlyAssociated` parameter to specify
which accounts to include in the response. By default, Macie returns details
about only those accounts that are member accounts in the specified Region, by
invitation or through AWS Organizations. To retrieve the details of all associated
accounts, including accounts that aren’t member accounts, include the
`onlyAssociated` parameter in your request and set the
parameter’s value to `false`.

To review your organization’s accounts by using the [AWS Command Line Interface (AWS CLI)](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md"), run
the [list-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-members.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-members.html") command. For the `only-associated` parameter,
specify whether to include all associated accounts or only member accounts. To
include only member accounts, omit this parameter or set the parameter’s value to
`true`. To include all accounts, set this value to `false`.
For example:

```
`C:\>` `aws macie2 list-members --region `us-east-1` --only-associated false`
```

Where `us-east-1` is the Region that the
request applies to, the US East (N. Virginia) Region.

If your request succeeds, Macie returns a `members` array. The array contains a
`member` object for each account that meets the criteria specified in
the request. In that object, the `relationshipStatus` field indicates the
current status of the association between your account and the other account in the
specified Region. For an account in an invitation-based organization, possible values
are:

- `AccountSuspended` – The AWS account is
  suspended.
- `Created` – You added the account but haven’t sent a
  membership invitation to it.
- `EmailVerificationFailed` – You tried to send a membership
  invitation to the account but the specified email address isn’t valid for the
  account.
- `EmailVerificationInProgress` – You sent a membership
  invitation to the account and Macie is processing the request.
- `Enabled` – The account is a member account. Macie is enabled for the
  account and you’re the Macie administrator of the account.
- `Invited` – You sent a membership invitation to the
  account and the account hasn’t responded to your invitation.
- `Paused` – The account is a member account but Macie is
  currently suspended (paused) for the account.
- `RegionDisabled` – The current Region is disabled for the
  AWS account.
- `Removed` – The account was previously a member account. However, you
  removed it as a member account by disassociating it from your account.
- `Resigned` – The account was previously a member account.
  However, the account resigned from your organization by disassociating from
  your account.

For information about other fields in the `member` object, see [Members](../APIReference/members.md "../APIReference/members.md")
in the _Amazon Macie API Reference_.
