# Unsubscribing from Amazon Q Developer Pro

How you unsubscribe from the Pro tier depends on whether you're an end-user with a personal
account (Builder ID) or an administrator of IAM Identity Center workforce users.

## Unsubscribing a personal account (Builder ID)

Read this section if you want to unsubscribe your personal account (Builder ID) from the Pro
tier.

When you unsubscribe your Builder ID, your subscription is marked as **Canceled**, and you can no longer access Amazon Q Developer features. (You can still use
the [Free tier](q-tiers.md "q-tiers.md") though, provided you have not exceeded your Free
tier limits.) The final monthly subscription fee is charged at the end of the current billing
cycle. You'll be charged for the full month; the fee won't be prorated.

###### Warning

Deleting your Builder ID does not unsubscribe you. To stop being billed, you must actively
unsubscribe yourself using the instructions in this section.

You can unsubscribe starting from one of the following interfaces:

- IDE
- command line
- AWS Management Console

IDE

###### To unsubscribe your Builder ID starting from your IDE

1. Authenticate to Amazon Q in your IDE using your personal account (Builder ID). For
   more information, see [Installing the Amazon Q Developer extension or plugin in your IDE](q-in-IDE-setup.md "q-in-IDE-setup.md").
2. From the Amazon Q menu, choose **Manage Q Developer Pro
   Subscription**.

A browser window opens. 3. If prompted, sign in to the AWS Management Console using the AWS account that's
linked to your personal account (Builder ID). You specified this AWS account
when you upgraded your Builder ID to the Pro tier. For more information, see
[Upgrading a personal account (Builder ID)](upgrade-to-pro.md#upgrade-builder-id "upgrade-to-pro.md#upgrade-builder-id").

The **Subscriptions** page in the Amazon Q Developer console
appears. 4. In the **Builder ID users** section, choose **Unsubscribe**.

Command line

###### To unsubscribe your Builder ID starting from the command line

1. On a computer where Amazon Q for the command line is installed, open a
   terminal.
2. Make sure you're signed in with your personal account (Builder ID) by typing
   `q whoami` at the command line.

You should see a `Logged in with Builder ID`
message. 3. Start a chat session by typing `q chat`
at your terminal's prompt.

An interactive chat sessions opens. 4. Type `/subscribe --manage`.

The AWS Management Console launches in a browser window.

###### Note

If the AWS Management Console doesn't automatically launch, copy and paste the
URL from the terminal into a browser window. 5. If prompted, sign in to the AWS Management Console using the AWS account that's
linked to your personal account (Builder ID). You specified this AWS account
when you upgraded your Builder ID to the Pro tier. For more information, see
[Upgrading a personal account (Builder ID)](upgrade-to-pro.md#upgrade-builder-id "upgrade-to-pro.md#upgrade-builder-id").

The **Subscriptions** page in the Amazon Q Developer console
appears. 6. In the **Builder ID users** section, choose **Unsubscribe**.

AWS Management Console

###### To unsubscribe your Builder ID starting from the AWS Management Console

1. Sign in to the AWS Management Console using the AWS account that's linked to your
   personal account (Builder ID). You specified this AWS account when you
   upgraded your Builder ID to the Pro tier. For more information, see [Upgrading a personal account (Builder ID)](upgrade-to-pro.md#upgrade-builder-id "upgrade-to-pro.md#upgrade-builder-id").
2. Switch to the Amazon Q Developer console in the US East (N. Virginia) Region (IAD).
3. Choose **Subscriptions**.
4. In the **Builder ID users** section, choose
   **Unsubscribe**.

## Unsubscribing IAM Identity Center workforce users

If you are the administrator of an AWS standalone account, an AWS management account, or
an AWS member account, use the following procedure to unsubscribe IAM Identity Center workforce users from
your account.

For more information about AWS management and member accounts, see [Managing AWS accounts in an organization with AWS Organizations](../../../organizations/latest/userguide/orgs_manage_accounts.md "../../../organizations/latest/userguide/orgs_manage_accounts.md").

Notes about unsubscribing users:

- If you are an administrator of either a management or member account within an
  organization managed by [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md"), you
  can only unsubscribe users if your created their subscriptions.
- If a user has been subscribed in both member and management accounts, both account
  administrators must unsubscribe the user from their respective accounts for the user
  to be fully unsubscribed.
- If you are a management account administrator, you can view other accounts the user
  is subscribed in by choosing **View subscriptions from member
  accounts** on the **Settings** page of the
  Amazon Q Developer console. This allows you to coordinate with member account administrators
  for unsubscription. Alternatively, if you have the appropriate permissions, you can
  sign in as a member account administrator and unsubscribe the user directly. For more
  information about viewing member account subscriptions as a management account
  administrator, see [Viewing an aggregated list of Amazon Q Developer subscriptions](subscribe-visibility.md "subscribe-visibility.md").
- After unsubscribing users or groups, their subscriptions are marked as
  **Canceled**, and they can no longer access Amazon Q Developer features.
  (They can still use the [Free tier](q-tiers.md "q-tiers.md") though, provided they
  have not exceeded their Free tier limits.) The final monthly subscription fee is
  charged at the end of the current billing cycle for all users who had active
  subscriptions. You'll be charged for the full month; the fee won't be prorated.

###### To unsubscribe a user or group you manage

1. Sign in to the AWS Management Console using your AWS standalone, management, or member
   account.
2. Switch to the Amazon Q Developer console.
3. In the **Identity provider users and groups** section, choose the
   **Users** or **Groups** tab.
4. Choose the user or group you want to unsubscribe.
5. Choose **More actions**.
6. Choose **Unsubscribe**.
