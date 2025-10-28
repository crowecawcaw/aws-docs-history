# Managing your membership in an

organization in Macie

###### Note

We recommend using AWS Organizations instead of Macie invitations to centrally manage Macie for
multiple accounts. For more information, see [Managing multiple Macie accounts with AWS Organizations](accounts-mgmt-ao.md "accounts-mgmt-ao.md").

If you’re invited to join an organization in Amazon Macie, you can optionally accept or
decline the invitation. In Macie, an organization is a set of accounts that are centrally
managed as a group of related accounts. An organization consists of one designated
Macie administrator account and one or more associated member accounts.

If you accept an invitation, your account becomes a member account in the organization. When
you accept, the account that sent the invitation becomes the Macie administrator account for your
account—you associate your account with the other account and you enable an
administrator-member relationship between the accounts. The Macie administrator account can then access
certain Macie settings, data, and resources for your account in the applicable AWS Region.
For details about tasks that the administrator account can perform, see [Macie administrator and member account
relationships](accounts-mgmt-relationships.md "accounts-mgmt-relationships.md").

If you decline an invitation, the current status and settings for your Macie account aren’t
changed.

###### Topics

- [Responding to membership
  invitations](#accounts-mgmt-invitations-respond "#accounts-mgmt-invitations-respond")
- [Disassociating from an administrator account](#accounts-mgmt-invitations-disassociate-admin "#accounts-mgmt-invitations-disassociate-admin")

## Responding to membership invitations

for organizations

When you receive an invitation to join an organization, Amazon Macie notifies you in
several ways. By default, Macie sends the invitation to you as an email message. Macie
also creates an AWS Health event for your AWS account. If you already use Macie
in the AWS Region from which the invitation was sent, Macie also displays an
**Accounts** badge and notification on the Macie console.

After you receive an invitation, you can optionally accept or decline the invitation.
Before you respond, note the following:

- You can be a member of only one organization at a time. If you receive
  multiple invitations, you can accept only one. Or, if you’re already a member of
  an organization, you have to disassociate your account from its current
  Macie administrator account before you can join a different organization.
- If you use Macie in multiple Regions, your account has to have the same
  Macie administrator account in all of those Regions. The Macie administrator has to send
  invitations to you separately from each Region, and you have to accept the
  invitations separately in each Region.
- To accept or decline an invitation, you have to enable Macie in the Region
  that the invitation was sent from. Declining an invitation is optional. If you
  enable Macie to decline an invitation, you can [disable Macie](disable-macie.md "disable-macie.md") in the Region after you decline the invitation. This
  helps ensure that you don’t incur unnecessary charges for using Macie in the
  Region.
- If automated sensitive data discovery is enabled for your account and you accept an invitation, you
  lose access to statistical data, inventory data, and other information that
  Macie produced and directly provided while performing automated discovery for your account.
  After you accept an invitation, your Macie administrator can enable automated discovery for your
  account. However, this doesn't restore access to the existing data. Instead,
  Macie generates and maintains new data while it performs automated discovery for your
  account.

For additional considerations, see [Responding to and
managing membership invitations](accounts-mgmt-invitations-notes.md#accounts-mgmt-invitations-notes-invitations-manage "accounts-mgmt-invitations-notes.md#accounts-mgmt-invitations-notes-invitations-manage").

###### To respond to a membership invitation for an organization

To respond to a membership invitation, you can use the Amazon Macie console or the
Amazon Macie API.

Console
Follow these steps to respond to a membership invitation by using the
Amazon Macie console.

###### To respond to a membership invitation

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you received the invitation.
3. If you haven't enabled Macie in the Region, choose **Get
   started**, and then choose **Enable
   Macie**. You have to enable Macie before you can accept
   or decline an invitation.
4. In the navigation pane, choose **Accounts**.
5. Under **Administrator account**, do one of the
   following:
   - To accept the invitation, turn on
     **Accept** (
     ![A toggle switch with a gray background and the toggle positioned to the left.](images/tgl-gray-off.png)
     ) next to the invitation. Then choose
     **Accept invitation** or
     **Update**, depending on whether you
     previously accepted another invitation.
   - To decline the invitation, choose **Decline
     invitation** next to the invitation, and then
     confirm that you want to decline the invitation.

If you received and want to respond to the invitation in additional
Regions, repeat the preceding steps in each additional Region.

API
To respond to an invitation programmatically, use the [AcceptInvitation](../APIReference/invitations-accept.md "../APIReference/invitations-accept.md") or [DeclineInvitations](../APIReference/invitations-decline.md "../APIReference/invitations-decline.md") operation of the Amazon Macie API, depending on
whether you want to accept or decline the invitation. When you submit your
request, be sure to specify the Region that the invitation was sent from. To
respond to the invitation in additional Regions, submit your request in each
additional Region.

In an `AcceptInvitation` request, use the
`administratorAccountId` parameter to specify the 12-digit
account ID for the AWS account that sent the invitation. Use the
`invitationId` parameter to specify the unique ID for the
invitation to accept.

In a `DeclineInvitations` request, use the
`accountIds` parameter to specify the 12-digit account ID for
the AWS account that sent the invitation to decline.

To retrieve the IDs, you can use the [ListInvitations](../APIReference/invitations.md "../APIReference/invitations.md")
operation of the Amazon Macie API. If the operation succeeds, Macie returns an
`invitations` array that provides details about invitations
that you’ve received, including the account ID for the account that sent
each invitation and the unique ID for each invitation. If the value for the
`relationshipStatus` property of an invitation is
`Invited`, you haven’t responded to the invitation
yet.

To respond to an invitation by using the [AWS Command Line Interface
(AWS CLI)](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md"), run the [accept-invitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/accept-invitation.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/accept-invitation.html") or [decline-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/decline-invitations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/decline-invitations.html") command, depending on whether you want to
accept or decline the invitation. Use the `region` parameter to
specify the Region that the invitation was sent from. For example:

```
`C:\>` `aws macie2 accept-invitation --region `us-east-1` --administrator-account-id `123456789012` --invitation-id `d8bdad0e203fd1242e0a4721bexample``
```

Where `us-east-1` is the Region that
the invitation was sent from (the US East (N. Virginia) Region),
`123456789012` is the account ID for
the account that sent the invitation, and
`d8bdad0e203fd1242e0a4721bexample` is the
unique ID for the invitation to accept.

If a request to accept an invitation succeeds, Macie returns an empty
response. If a request to decline an invitation succeeds, Macie returns an
empty `unprocessedAccounts` array.

After you decline an invitation, the invitation persists as a resource for
your Macie account. You can optionally delete it by using the [DeleteInvitations](../APIReference/invitations-delete.md "../APIReference/invitations-delete.md") operation or, for the AWS CLI, the [delete-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-invitations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-invitations.html") command.

## Disassociating from a

Macie administrator account

If you accept an invitation to join an organization in Amazon Macie, you can subsequently
resign from the organization by disassociating your account from its current
Macie administrator account. Note that you can't do this if your account is a member account in an
AWS Organizations organization. To resign from an AWS Organizations organization, work with your
Macie administrator to remove your account as a Macie member account.

If you disassociate your account from its Macie administrator account, the Macie administrator loses
access to all settings, data, and resources for your Macie account. This includes
metadata and policy findings for Amazon S3 data that you own. This also means that the
administrator can no longer analyze your Amazon S3 data by performing automated sensitive data discovery or running
sensitive data discovery jobs.

When you disassociate your account, Macie continues to be enabled for your account in
the applicable Region. However, your account becomes a standalone Macie account in the
Region. The status of your account changes to **Member resigned** in
the administrator’s account inventory.

###### To disassociate from a Macie administrator account

To disassociate your account from its current Macie administrator account, you can use the
Amazon Macie console or the Amazon Macie API.

Console
Follow these steps to disassociate your account from its Macie administrator account
by using the Amazon Macie console.

###### To disassociate from an administrator account

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to disassociate your account from
   its administrator account.
3. In the navigation pane, choose **Accounts**.
4. Under **Administrator account**, turn off
   **Accept** (
   ![A toggle switch with a blue background and the toggle positioned to the right.](images/tgl-blue-on.png)
   ) next to the invitation, and then choose
   **Update**.

The account continues to appear on the **Accounts** page.
If you decide to re-join the organization, you can use this page to accept
the original invitation again. Alternatively, you can decline and delete the
invitation, which also deletes the association between your account and the
other account. To do this, choose **Decline
invitation**.

If you want to disassociate your account from its Macie administrator account in
additional Regions, repeat the preceding steps in each additional
Region.

API
To disassociate your account from its Macie administrator account programmatically,
use the [DisassociateFromAdministratorAccount](../APIReference/administrator-disassociate.md "../APIReference/administrator-disassociate.md") operation of the Amazon Macie
API. When you submit your request, be sure to specify the Region that the
request applies to. To disassociate from the account in additional Regions,
submit your request in each additional Region.

To disassociate your account from its Macie administrator account by using the AWS CLI,
run the [disassociate-from-administrator-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/disassociate-from-administrator-account.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/disassociate-from-administrator-account.html") command. Use the
`region` parameter to specify the Region in which to
disassociate from the account.

If your request succeeds, Macie returns an empty response.

After you disassociate from the account, the original invitation persists
as a resource for your Macie account unless you delete it. If you decide to
re-join the organization, you can use this resource to accept the original
invitation again. Alternatively, you can delete the invitation by using the
[DeleteInvitations](../APIReference/invitations-delete.md "../APIReference/invitations-delete.md") operation or, for the AWS CLI, the [delete-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-invitations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-invitations.html") command. If you delete the invitation, you
also delete the association between your account and the other
account.
