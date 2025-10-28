# Responding to an invitation to be a Security Hub CSPM

member account

###### Note

We recommend using AWS Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see
[Managing Security Hub CSPM for multiple accounts with
AWS Organizations](securityhub-accounts-orgs.md "securityhub-accounts-orgs.md").

You can accept or decline an invitation to be an AWS Security Hub CSPM member account.

If you accept an invitation, your account becomes a Security Hub CSPM member account. The
account that sent the invitation becomes your Security Hub CSPM administrator account. The
administrator account user can view findings for your member account in Security Hub CSPM.

If you decline the invitation, then your account is marked as
**Resigned** on the administrator account's list of member
accounts.

You can only accept one invitation to be a member account.

Before you can accept or decline an invitation, you must enable Security Hub CSPM.

Remember that all Security Hub CSPM accounts must have AWS Config enabled and configured to record all
resources. For details on the requirement for AWS Config, see [Enabling and configuring AWS Config](securityhub-prereq-config.md "securityhub-prereq-config.md").

## Accepting an invitation

You can send an invitation to be a Security Hub CSPM member account from the administrator account. You can then accept the
invitation after signing in to the member account.

Choose your preferred method, and follow the steps to accept an invitation to be a member account.

Security Hub CSPM console

###### To accept a membership invitation

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose **Settings**, and then
   choose **Accounts**.
3. In the **Administrator account** section, turn on
   **Accept**, and then choose
   **Accept invitation**.

Security Hub CSPM API
**To accept a membership invitation**

Invoke the [`AcceptAdministratorInvitation`](../../1.0/APIReference/API_AcceptAdministratortInvitation.md "../../1.0/APIReference/API_AcceptAdministratortInvitation.md") API. You
must provide the invitation identifier and the AWS account ID of the
administrator account. To retrieve details about the invitation, use the
[`ListInvitations`](../../1.0/APIReference/API_ListInvitations.md "../../1.0/APIReference/API_ListInvitations.md") operation.

AWS CLI
**To accept a membership invitation**

Run
the [`accept-administrator-invitation`](../../../cli/latest/reference/securityhub/accept-administrator-invitation.md "../../../cli/latest/reference/securityhub/accept-administrator-invitation.md")
command. You
must provide the invitation identifier and the AWS account ID of the
administrator account. To retrieve details about the invitation, run the
[`list-invitations`](../../../cli/latest/reference/securityhub/list-invitations.md "../../../cli/latest/reference/securityhub/list-invitations.md")
command.

```
aws securityhub accept-administrator-invitation --administrator-id `<administratorAccountID>` --invitation-id `<invitationID>`
```

**Example**

```
aws securityhub accept-administrator-invitation --administrator-id 123456789012 --invitation-id 7ab938c5d52d7904ad09f9e7c20cc4eb
```

###### Note

The Security Hub CSPM console continues to use `AcceptInvitation`. It will
eventually change to use `AcceptAdministratorInvitation`. Any IAM
policies that specifically control access to this function must continue to use
`AcceptInvitation`. You should also add
`AcceptAdministratorInvitation` to your policies to ensure that
the correct permissions are in place after the console begins to use
`AcceptAdministratorInvitation`.

## Declining an invitation

You can decline an invitation to be a Security Hub CSPM member account. When you decline an
invitation in the Security Hub CSPM console, your account is marked as **Resigned** on the
administrator account's list of member accounts. The **Resigned** status
appears only when you sign in to the Security Hub CSPM console using the administrator account. However,
the invitation remains unchanged in the console for the member account until you sign in to the
administrator account and delete the invitation.

To decline an invitation, you must sign in to the member account that received the invitation.

Choose your preferred method, and follow the steps to decline an invitation to be a member account.

Security Hub CSPM console

###### To decline a membership invitation

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose **Settings**, and then
   choose **Accounts**.
3. In the **Administrator account** section, choose **Decline
   invitation**.

Security Hub CSPM API
**To decline a membership invitation**

Invoke the [`DeclineInvitations`](../../1.0/APIReference/API_DeclineInvitations.md "../../1.0/APIReference/API_DeclineInvitations.md") API. You must provide
the AWS account ID of the administrator account that issued the
invitation. To view information about your invitations, use the [`ListInvitations`](../../1.0/APIReference/API_ListInvitations.md "../../1.0/APIReference/API_ListInvitations.md") operation.

AWS CLI
**To decline a membership invitation**

Run
the [`decline-invitations`](../../../cli/latest/reference/securityhub/decline-invitations.md "../../../cli/latest/reference/securityhub/decline-invitations.md") command.
You must provide
the AWS account ID of the administrator account that issued the
invitation. To view information about your invitations, run the [`list-invitations`](../../../cli/latest/reference/securityhub/list-invitations.md "../../../cli/latest/reference/securityhub/list-invitations.md") command.

```
aws securityhub decline-invitations --account-ids "`<administratorAccountId>`"
```

**Example**

```
aws securityhub decline-invitations --account-ids "123456789012"
```
