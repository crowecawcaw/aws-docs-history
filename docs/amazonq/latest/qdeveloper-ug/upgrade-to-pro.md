# Upgrading to Amazon Q Developer Pro

How you upgrade to the Pro tier from the Free tier depends on whether you're an end-user with a
personal account (Builder ID) or whether you're an administrator of IAM Identity Center workforce users.

## Upgrading a personal account (Builder ID)

Read this section if you want to upgrade your personal account (Builder ID) from the Free tier to
a Pro tier monthly subscription. For reasons why you might consider upgrading, see [Tiers of service](q-tiers.md "q-tiers.md"), and [Limitations of Builder IDs](getting-started-builderid.md#builder-id-limitations "getting-started-builderid.md#builder-id-limitations").

You can upgrade starting from one of the following interfaces:

- IDE
- command line

###### Before you begin

- Create an AWS account if you don't have one yet. This account will be linked to
  your Builder ID, and will be charged the monthly subscription fee. For more information
  about creating an account, see [Create an AWS account](../../../accounts/latest/reference/manage-acct-creating.md "../../../accounts/latest/reference/manage-acct-creating.md") in the _AWS Account Management
  Reference Guide_.

###### Note

You cannot link multiple Builder IDs to a single AWS account. If you have multiple
Builder IDs that you want to upgrade, create separate AWS accounts for each.

IDE

###### To upgrade starting from the IDE

1. Authenticate to Amazon Q in your IDE using your personal account (Builder ID). For
   more information, see [Installing the Amazon Q Developer extension or plugin in your IDE](q-in-IDE-setup.md "q-in-IDE-setup.md").
2. In your IDE, do one of the following:
   - If you see a `Monthly request limit
reached` message in the Amazon Q chat window,
     choose **Subscribe to Q Developer Pro**.

   Or
   - From the Amazon Q menu, choose **Subscribe to Q
     Developer Pro**.

   A browser window opens.

3. If prompted, sign in using your AWS account. You should have created
   this account previously, as described in **Before you
   begin**.

A **Review upgrade details for Q Developer Pro** page
appears. The page shows your Builder ID, AWS account number, and subscription
fee, among other information. For more information about the subscription
fee, see [Subscription billing](tracking-across-org-cost-usage.md "tracking-across-org-cost-usage.md"). The
**Activation token** field shows a one-time token
that links your AWS account with your Builder ID. This token is never used
again. 4. Choose **Confirm upgrade**.

The **Subscriptions** page of the
Amazon Q Developer console appears with an **Upgrade to Q Developer Pro
successful** message at the top. You should see your user
name listed in the **Builder ID users**
section.

Your personal account (Builder ID) is now subscribed to the Pro tier. 5. (Optional) Return to the Amazon Q chat window in your IDE.

You should see a **Successfully subscribed to
Amazon Q Developer Pro** message.

Command line

###### To upgrade starting from the command line

1. On a computer where Amazon Q for the command line is installed, open a
   terminal.
2. Make sure you're signed in with your personal account (Builder ID) by typing
   `q whoami` at the command line.

You should see a `Logged in with Builder ID`
message. 3. Start a chat session by typing `q chat`
at your terminal's prompt.

An interactive chat sessions opens. 4. Type `/subscribe`.

The AWS Management Console launches in a browser window.

###### Note

If the AWS Management Console doesn't automatically launch, copy and paste the
URL from the terminal into a browser window. 5. If prompted, sign in using your AWS account. You should have created
this account previously, as described in **Before you
begin**.

A **Review upgrade details for Q Developer Pro** page
appears. The page shows your Builder ID, AWS account number, and subscription
fee, among other information. For more information about the subscription
fee, see [Subscription billing](tracking-across-org-cost-usage.md "tracking-across-org-cost-usage.md"). The
**Activation token** field shows a one-time token
that links your AWS account with your Builder ID. This token is never used
again. 6. Choose **Confirm upgrade**.

The **Subscriptions** page of the
Amazon Q Developer console appears with a **Upgrade to Q Developer Pro
successful** message at the top. You should see your user
name listed in the **Builder ID users**
section.

Your personal account (Builder ID) is now subscribed to the Pro tier. 7. (Optional) Verify that you're subscribed by typing
`/subscribe` at the Q CLI prompt. Amazon Q should
indicate that you're already subscribed.

## Upgrading IAM Identity Center workforce users to the Pro tier

If you are the administrator of IAM Identity Center workforce users, you can upgrade these users to the
Pro tier following the instructions in [Getting started with IAM Identity Center](getting-started-idc.md "getting-started-idc.md").
