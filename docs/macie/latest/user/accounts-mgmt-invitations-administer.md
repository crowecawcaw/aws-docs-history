# Creating and managing an

invitation-based organization in Macie

###### Note

We recommend using AWS Organizations instead of Macie invitations to manage member
accounts. For more information, see [Managing multiple Macie accounts with AWS Organizations](accounts-mgmt-ao.md "accounts-mgmt-ao.md").

To create an invitation-based organization in Amazon Macie, you start by determining which
account you want to be the Macie administrator account for the organization. You then use that account
to add member accounts—you send membership invitations to other AWS accounts,
inviting the accounts to join the organization as Macie member accounts in the current
AWS Region. To create the organization in multiple Regions, send membership invitations
from each Region in which the other accounts currently use or plan to use Macie.

When an account accepts an invitation, it becomes a Macie member account that's associated
with the Macie administrator account in the applicable Region. The Macie administrator account can then access
certain Macie settings, data, and resources for the member account in that Region.

As the Macie administrator for an invitation-based organization, you can review Amazon Simple Storage Service (Amazon S3)
inventory data and policy findings for member accounts. You can also enable automated sensitive data discovery and
run sensitive data discovery jobs to detect sensitive data in S3 buckets that member
accounts own. For a detailed list of the tasks that you can perform, see [Macie administrator and member account
relationships](accounts-mgmt-relationships.md "accounts-mgmt-relationships.md").

By default, Macie gives you visibility into relevant data and resources for your organization
overall. You can also drill down to review data and resources for individual accounts in your
organization. For example, if you [use the Summary
dashboard](monitoring-s3-dashboard.md "monitoring-s3-dashboard.md") to assess your organization’s Amazon S3 security posture, you can filter the
data by account. Similarly, if you [monitor estimated usage
costs](account-mgmt-costs.md "account-mgmt-costs.md"), you can access breakdowns of estimated costs for individual member
accounts.

In addition to tasks that are common to administrator and member accounts, you can centrally
perform various administrative tasks for your organization. Before you perform these tasks,
it’s a good idea to review the [considerations
and recommendations](accounts-mgmt-invitations-notes.md "accounts-mgmt-invitations-notes.md") for managing invitation-based organizations in Macie.

###### Tasks

- [Adding member
  accounts](#accounts-mgmt-invitations-members-add "#accounts-mgmt-invitations-members-add")
- [Suspending Macie
  for member accounts](#accounts-mgmt-invitations-members-suspend "#accounts-mgmt-invitations-members-suspend")
- [Removing member
  accounts](#accounts-mgmt-invitations-members-remove "#accounts-mgmt-invitations-members-remove")
- [Deleting
  associations with other accounts](#accounts-mgmt-invitations-members-disassociate "#accounts-mgmt-invitations-members-disassociate")

## Adding Macie member accounts to an

invitation-based organization

As the Amazon Macie administrator for an invitation-based organization, you add member accounts to your
organization by performing two primary steps:

1. Add the accounts to your account inventory in Macie. This associates the accounts
   with your account.
2. Send membership invitations to the accounts.

When an account accepts your invitation, it becomes a member account in your
organization.

### Step 1: Add the

accounts

To add one or more accounts to your account inventory, you can use the Amazon Macie
console or the Amazon Macie API.

Console
With the Amazon Macie console, you can add one account at a time, or add multiple accounts
at the same time by uploading a comma-separated values (CSV) file. Follow these
steps to add one or more accounts by using the console.

###### To add one account

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to add an account.
3. In the navigation pane, choose **Accounts**.
   The **Accounts** page opens and displays a
   table of the accounts that are currently associated with your
   account.
4. Choose **Add accounts**.
5. In the **Enter account details** section,
   choose **Add account**. Then do the
   following:
   - For **Account ID**, enter the
     12-digit account ID for the AWS account to add.
   - For **Email address**, enter the
     email address for the AWS account to add.

6. Choose **Add**.
7. At the bottom of the page, choose **Next**.

Macie adds the account to your account inventory. The account’s type is **By
invitation** and its status is
**Created**. To add the account in additional Regions,
repeat the preceding steps in each additional Region.

###### To add multiple accounts

1. By using a text editor, create a CSV file as follows:
   1. Add the following header as the first line of the
      file: `Account ID,Email`
   2. For each account, create a new line that has the
      12-digit account ID for the AWS account to add and the
      email address for the account. Separate the entries with
      a comma, for example:
      `111111111111,janedoe@example.com`

   The email address must match the email address that’s
   associated with the AWS account. 3. Verify that the file’s contents are formatted as shown
   in the following example, which contains the required
   header and information for three accounts:

   ```
   Account ID,Email
   111111111111,janedoe@example.com
   222222222222,jorgesouza@example.com
   333333333333,lijuan@example.com
   ```

   4. Save the file on your computer.

2. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
3. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to add the accounts.
4. In the navigation pane, choose **Accounts**.
   The **Accounts** page opens and displays a
   table of the accounts that are currently associated with your
   account.
5. Choose **Add accounts**.
6. In the **Enter account details** section,
   choose **Upload list (CSV)**.
7. Choose **Browse**, and then select the CSV
   file that you created in step 1.
8. Choose **Add accounts**.
9. At the bottom of the page, choose **Next**.

Macie adds the accounts to your account inventory. Their type is **By
invitation** and their status is
**Created**. To add the accounts in additional
Regions, repeat steps 3 through 8 in each additional Region.

API
To add one or more accounts programmatically, use the [CreateMember](../APIReference/members.md "../APIReference/members.md") operation of the Amazon Macie API. When you submit your
request, use the supported parameters to specify the 12-digit account ID and
email address for each AWS account to add. Also specify the Region that the
request applies to. To add accounts in additional Regions, submit the request
in each additional Region.

To add accounts by using the AWS Command Line Interface (AWS CLI), run the [create-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-member.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-member.html") command. Use the `region`
parameter to specify the Region in which to add the accounts. Use the
`account` parameters to specify the account ID and email
address for each AWS account to add. For example:

```
`C:\>` `aws macie2 create-member --region `us-east-1` --account={\"accountId\":\"`111111111111`\",\"email\":\"`janedoe@example.com`\"}`
```

Where `us-east-1` is the Region in which to add the
account (the US East (N. Virginia) Region) and the `account` parameters
specify the account ID (`111111111111`) and
email address (`janedoe@example.com`) for the account
to add.

If your request succeeds, Macie adds each account to your account inventory with a
status of `Created` and you receive output similar to the
following:

```
`{
 "arn": "arn:aws:macie2:us-east-1:123456789012:member/111111111111"
}`
```

Where `arn` is the Amazon Resource Name (ARN) of the resource that was
created for the association between your account and the account that you
added. In this example, `123456789012` is the account ID for the
account that created the association and `111111111111` is the account
ID for the account that was added.

### Step 2: Send membership

invitations to the accounts

After you add an account to your account inventory, you can invite the account to join your
organization as a Macie member account. To do this, send a membership invitation to the
account. When you send an invitation, an **Accounts** badge and
notification appear on the Amazon Macie console for the recipient’s account, if Macie is
enabled for the account. Macie also creates an AWS Health event for the
account.

Depending on whether you use the Amazon Macie console or API to send the invitation, Macie
also sends the invitation to the email address that you specified for the recipient’s
account when you added the account. The email message indicates that you would like to
become the Macie administrator for their account, and it includes the account ID for your
AWS account and the recipient’s AWS account. The message also explains how to access
the invitation. You can optionally add custom text to the message.

To send a membership invitation to one or more accounts, you can use the Amazon Macie
console or the Amazon Macie API.

Console
Follow these steps to send a membership invitation by using the Amazon Macie
console.

###### To send a membership invitation

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to send the invitation.
3. In the navigation pane, choose **Accounts**. The
   **Accounts** page opens and displays a
   table of the accounts that are currently associated with your
   account.
4. In the **Existing accounts** table, select the checkbox for each
   account that you want to send the invitation to.

###### Tip

To more easily identify accounts that you added and haven't sent invitations to yet,
you can filter the table. To do this, place your cursor in
the filter box above the table, and then choose
**Status**. Then choose
**Status = Created**. 5. On the **Actions** menu, choose
**Invite**. 6. (Optional) In the **Message** box, enter any custom
text that you want to include in the email message that contains the
invitation. The text can contain as many as 80 alphanumeric
characters. 7. Choose **Invite**.

To send the invitation in additional AWS Regions, repeat the preceding steps in each
additional Region.

After you send the invitation, the status of a recipient account changes to
**Email verification in progress** in your account
inventory. If Macie can verify an account’s email address, the account’s status
subsequently changes to **Invited**. If Macie can’t verify the
address, the account’s status changes to **Email verification
failed**. If this happens, work with the account owner to get the
correct email address. Then [delete the
association between your accounts](#accounts-mgmt-invitations-members-disassociate "#accounts-mgmt-invitations-members-disassociate"), [add the
account](#accounts-mgmt-invitations-members-add-associate "#accounts-mgmt-invitations-members-add-associate") again, and send the invitation again.

When a recipient accepts an invitation, the status of the recipient’s account changes to
**Enabled** in your account inventory. If a recipient
declines an invitation, the recipient’s account is disassociated from your
account and removed from your account inventory.

API
To send an invitation programmatically, use the [CreateInvitations](../APIReference/invitations.md "../APIReference/invitations.md") operation of the Amazon Macie API. When you submit
your request, use the supported parameters to specify the 12-digit account ID
for each AWS account to send the invitation to. An account ID must match the
account ID for an account in your account inventory. Otherwise, an error
occurs. Also specify the Region to send the invitation from. To send the
invitation from additional Regions, submit the request in each additional
Region.

In your request, you can also specify whether to send the invitation as an
email message, and whether to include custom text in that message. If you
choose to send an email message, Macie sends the invitation to the email
address that you specified for an account when you added the account to your
account inventory. To send the invitation as an email message, omit the
`disableEmailNotification` parameter or set the value for the
parameter to `false`. (The default value is `false`.) To
add custom text to the message, use the `message` parameter to
specify the text to add. The text can contain as many as 80 alphanumeric
characters.

To send invitations by using the AWS CLI, run the [create-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-invitations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-invitations.html") command. Use the `region` parameter
to specify the Region to send the invitation from. Use the
`account-ids` parameter to specify the account ID for each
AWS account to send the invitation to. For example:

```
`C:\>` `aws macie2 create-invitations --region `us-east-1` --account-ids=[\"`111111111111`\",\"`222222222222`\",\"`333333333333`\"]`
```

Where `us-east-1` is the Region to send the
invitation from (the US East (N. Virginia) Region) and the
`account-ids` parameter specifies account IDs for three accounts
to send the invitation to. To send an invitation as an email message too, also
include the `no-disable-email-notification` parameter and optionally
include the `message` parameter to specify custom text to add to the
message.

After you send the invitation, the status of each recipient account changes to
`EmailVerificationInProgress`. If Macie can verify an account’s
email address, the account’s status subsequently changes to
`Invited`. If Macie can’t verify the address, the account’s
status changes to `EmailVerificationFailed`. If this happens, work
with the account owner to get the correct address. Then [delete the
association between your accounts](#accounts-mgmt-invitations-members-disassociate "#accounts-mgmt-invitations-members-disassociate"), [add the
account](#accounts-mgmt-invitations-members-add-associate "#accounts-mgmt-invitations-members-add-associate") again, and send the invitation again.

When a recipient accepts an invitation, the status of the recipient’s account changes to
`Enabled` in your account inventory. If a recipient declines an
invitation, the recipient’s account is disassociated from your account and
removed from your account inventory.

## Suspending Macie for member accounts

in an invitation-based organization

As the Amazon Macie administrator for an organization, you can suspend Macie in a specific AWS Region
for individual member accounts in your organization. Note, however, that you can’t
re-enable Macie for a member account after you suspend it. Only a user of the account
can subsequently re-enable Macie for the account.

When you suspend Macie for a member account:

- Macie loses access to and stops providing metadata about the account's Amazon S3 data
  in the Region.
- Macie stops performing all activities for the account in the Region. This includes
  monitoring S3 buckets for security and access control, performing automated sensitive data discovery,
  and running sensitive data discovery jobs that are currently in progress.
- Macie cancels all sensitive data discovery jobs that were created by the account in the
  Region. A job can't be resumed or restarted after it's cancelled. If you created
  jobs to analyze data that the member account owns, Macie doesn’t cancel your
  jobs. Instead, the jobs skip resources that are owned by the account.

While it's suspended, Macie retains the Macie session identifier, settings, and resources
that it stores or maintains for the account in the applicable Region. Macie also retains
certain data for the account in the Region. For example, the account's findings remain
intact and aren't affected for up to 90 days. If automated sensitive data discovery was enabled for the account,
existing results also remain intact and aren't affected for up to 30 days. The account
isn't charged for using Macie in the applicable Region while Macie is suspended for the
account in that Region.

###### To suspend Macie for a member account in an invitation-based organization

To suspend Macie for a member account in an invitation-based organization, you can use the
Amazon Macie console or the Amazon Macie API.

Console
Follow these steps to suspend Macie for a member account by using the Amazon Macie
console.

###### To suspend Macie for a member account

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to suspend Macie for a member account.
3. In the navigation pane, choose **Accounts**. The
   **Accounts** page opens and displays a table of
   the accounts that are currently associated with your account.
4. In the **Existing accounts** table, select the checkbox for the
   account that you want to suspend Macie for.
5. On the **Actions** menu, choose **Suspend
   Macie**.
6. Confirm that you want to suspend Macie for the selected account.

After you confirm the suspension, the status of the account changes to **Paused
(suspended)** in your account inventory.

To suspend Macie for the account in additional Regions, repeat the preceding steps in
each additional Region.

API
To suspend Macie for a member account programmatically, use the [UpdateMemberSession](../APIReference/macie-members-id.md "../APIReference/macie-members-id.md") operation of the Amazon Macie API. When you
submit your request, use the `id` parameter to specify the
12-digit account ID of the AWS account that you want to suspend Macie for.
For the `status` parameter, specify `PAUSED` as the
new status for Macie. Also specify the Region that the request applies to.
To suspend Macie in additional Regions, submit your request in each
additional Region.

To retrieve the account ID for the member account, you can use the [ListMembers](../APIReference/members.md "../APIReference/members.md") operation of the Amazon Macie API. If you do this, consider
filtering the results by including the `onlyAssociated` parameter in
your request. If you set this parameter’s value to `true`, Macie
returns a `members` array that provides details about only those
accounts that are currently member accounts for your
administrator account.

To suspend Macie for a member account by using the AWS CLI, run the [update-member-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-member-session.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-member-session.html") command. Use the `region`
parameter to specify the Region in which to suspend Macie. Use the
`id` parameter to specify the account ID for the account to
suspend Macie for. For the `status` parameter, specify
`PAUSED`. For example:

```
`C:\>` `aws macie2 update-member-session --region `us-east-1` --id `123456789012` --status PAUSED`
```

Where `us-east-1` is the Region in which to suspend
Macie (the US East (N. Virginia) Region),
`123456789012` is the account ID for the
account to suspend Macie for, and `PAUSED` is the new status of Macie
for the account.

If your request succeeds, Macie returns an empty response and the status of the specified
account changes to `Paused` in your account inventory.

## Removing Macie member

accounts from an invitation-based organization

As an Amazon Macie administrator, you can remove a member account from your organization. You do
this by disassociating the account from your Macie administrator account.

If you remove a member account, Macie continues to be enabled for the account and the
account continues to appear in your account inventory. However, the account becomes a
standalone Macie account. Macie doesn’t notify the account’s owner when you remove the
account. Therefore, consider contacting the account owner to ensure that they begin
managing settings and resources for their account.

When you remove a member account, you lose access to all Macie settings, resources,
and data for the account. This includes policy findings and metadata for S3 buckets that
the account owns. In addition, you can no longer use Macie to discover sensitive data in
S3 buckets that the account owns. If you already created sensitive data discovery jobs
to do this, the jobs skip buckets that the account owns. If you enabled automated sensitive data discovery for
the account, both you and the account lose access to statistical data, inventory data,
and other information that Macie produced and directly provided while performing automated discovery
for the account.

After you remove a member account, you can subsequently add it to your organization again by
sending a new invitation to the account. If the account accepts the new invitation and
you enable automated sensitive data discovery for it within 30 days, you also regain access to data and
information that Macie previously produced and directly provided while performing automated discovery
for the account. In addition, subsequent runs of your existing jobs start including the
account's S3 buckets again.

If you remove a member account and don't plan to add it again, you can remove it from
your account inventory completely. To learn how, see [Deleting
associations with other accounts](#accounts-mgmt-invitations-members-disassociate "#accounts-mgmt-invitations-members-disassociate").

###### To remove a member account from an invitation-based organization

To remove a member account from your organization, you can use the Amazon Macie
console or the Amazon Macie API.

Console
Follow these steps to remove a member account by using the Amazon Macie
console.

###### To remove a member account

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to remove a member account.
3. In the navigation pane, choose **Accounts**. The
   **Accounts** page opens and displays a table of
   the accounts that are currently associated with your account.
4. In the **Existing accounts** table, select the
   checkbox for the account that you want to remove.
5. On the **Actions** menu, choose
   **Disassociate account**.
6. Confirm that you want to remove the selected account as a member
   account.

After you confirm your selection, the status of the account changes to
**Removed (disassociated)** in your account
inventory.

To remove the member account in additional Regions, repeat the preceding steps in each
additional Region.

API
To remove a member account programmatically, use the [DisassociateMember](../APIReference/members-disassociate-id.md "../APIReference/members-disassociate-id.md") operation of the Amazon Macie API. When you
submit your request, use the `id` parameter to specify the
12-digit AWS account ID for the member account to remove. Also specify the
Region that the request applies to. To remove the account in additional
Regions, submit your request in each additional Region.

To retrieve the account ID for the account to remove, you can use the
[ListMembers](../APIReference/members.md "../APIReference/members.md") operation of the Amazon Macie API. If you do this,
consider filtering the results by including the `onlyAssociated`
parameter in your request. If you set this parameter’s value to
`true`, Macie returns a `members` array that
provides details about only those accounts that are currently member
accounts for your account.

To remove a member account by using the AWS CLI, run the [disassociate-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/disassociate-member.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/disassociate-member.html") command. Use the `region`
parameter to specify the Region in which to remove the account. Use the
`id` parameter to specify the account ID for the account to
remove. For example:

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

## Deleting associations with

other accounts

After you add an account to your account inventory in Amazon Macie, you can delete the
association between your account and the other account. You can do this for any account
in your inventory except:

- An account that’s part of your organization in AWS Organizations. This type of association is
  controlled through AWS Organizations not Macie.
- A member account that accepted a Macie membership invitation to join your organization.
  If this is the case, you must [remove the member
  account](#accounts-mgmt-invitations-members-remove "#accounts-mgmt-invitations-members-remove") before you can delete the association.

When you delete an association, Macie removes the account from your account inventory. If
you want to subsequently restore the association, you have to add the account again as
if it were a completely new account.

###### To delete an association with another account

To delete an association between your account and another account, you can use the
Amazon Macie console or the Amazon Macie API.

Console
To use the Amazon Macie console to delete an association with another account, follow these
steps.

###### To delete an association

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to delete an association.
3. In the navigation pane, choose **Accounts**. The
   **Accounts** page opens and displays a table of
   the accounts that are currently associated with your account.
4. In the **Existing accounts** table, select the checkbox for the
   account whose association you want to delete.
5. On the **Actions** menu, choose **Delete**.
6. Confirm that you want to delete the selected association.

To delete the association in additional Regions, repeat the preceding steps in each
additional Region.

API
To delete an association with another account programmatically, use the [DeleteMember](../APIReference/members-id.md "../APIReference/members-id.md") operation
of the Amazon Macie API. When you submit your request, use the `id`
parameter to specify the 12-digit account ID for the AWS account to delete the
association with. Also specify the Region that the request applies to. To delete
the association in additional Regions, submit your request in each additional
Region.

To retrieve the account ID for the account, you can use the [ListMembers](../APIReference/members.md "../APIReference/members.md") operation of
the Amazon Macie API. If you do this, include the `onlyAssociated`
parameter in your request and set the parameter’s value to `false`. If
the operation is successful, Macie returns a `members` array that
provides details about all the accounts that are associated with your account,
including accounts that aren’t currently member accounts.

To delete an association with another account by using the AWS CLI, run the [delete-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-member.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-member.html") command. Use the `region` parameter to
specify the Region in which to delete the association. Use the
`id` parameter to specify the account ID for the account. For
example:

```
`C:\>` `aws macie2 delete-member --region `us-east-1` --id `123456789012``
```

Where `us-east-1` is the Region in which to delete the association
with the other account (the US East (N. Virginia) Region) and `123456789012`
is the account ID for the account.

If your request succeeds, Macie returns an empty response and the association between
your account and the other account is deleted. The previously associated account
is removed from your account inventory.
