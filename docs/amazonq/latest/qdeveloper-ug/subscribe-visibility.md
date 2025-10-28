# Viewing an aggregated list of Amazon Q Developer

subscriptions

###### Note

This section does not apply to personal accounts (Builder IDs).

If you are a management account administrator within an organization managed by [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md"), you can configure Amazon Q to display Amazon Q Developer Pro subscriptions from both
_management_ and _member_ accounts in a single, unified
list on the **Subscriptions** page of the Amazon Q console (_not_
the Amazon Q Developer console) while signed in to your management account. This organization-wide
visibility eliminates the need to sign in to multiple accounts to track your subscriptions.

###### Note

Unified subscription information also appears on the **Dashboard** page of
the Amazon Q Developer console when you enable organization-wide visibility.

If you are a member account administrator, you will only ever be able to view the subscriptions
within the member accounts that you administer. This is true regardless of whether
organization-wide visibility was enabled in the management account.

To enable organization-wide visibility of Amazon Q Developer subscriptions, you must enable trusted
access to Amazon Q in your organization. _Trusted access_ is an AWS Organizations feature
that lets you designate Amazon Q as a _trusted service_ that is allowed to query
your organization's structure. This querying is required in order to show the status of
subscriptions.

To learn more about trusted access, see [Enabling trusted access for
AWS Account Management](../../../accounts/latest/reference/using-orgs-trusted-access.md "../../../accounts/latest/reference/using-orgs-trusted-access.md") in the _AWS Organizations User Guide_.

To learn more about member and management accounts, see [Terminology and
concepts for AWS Organizations](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") in the _AWS Organizations User Guide_ for
explanations.

Use the following instructions to enable trusted access to Amazon Q in your organization.

**Prerequisites**

Before you begin, make sure that:

- You are an administrator of an AWS _management_ account.
- You have an _organization instance_ of IAM Identity Center set up in your
  management account and connected to Amazon Q Developer.
- Your organization instance of IAM Identity Center contains users who are subscribed to Amazon Q Developer Pro in
  member accounts.
- You have the minimum permissions required to perform actions in the Amazon Q or
  Amazon Q Developer console (you can use either console to enable trusted access). For more
  information, see [Allow administrators to use the Amazon Q console](id-based-policy-examples-admins.md#q-admin-setup-admin-users-sub "id-based-policy-examples-admins.md#q-admin-setup-admin-users-sub") and [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users "id-based-policy-examples-admins.md#q-admin-setup-admin-users").

###### To enable trusted access (enable organization-wide visibility of subscriptions)

1. Sign in to the AWS Management Console using your AWS management account.
2. Do one of the following depending on the console you want to use:
   - Switch to the Amazon Q console.

   Choose **Subscriptions**.

   At the bottom of the page, in the **Subscription view
   settings** section, choose **Edit**.

   Choose **On**.
   - Switch to the Amazon Q Developer console.

   Choose **Settings**.

   In the **Subscription view settings** section, choose
   **Edit**.

   Enable the toggle.

3. Choose **Save**.

Trusted access to Amazon Q is now enabled. Users and groups who are subscribed in member
accounts now appear in the Amazon Q console (not the Amazon Q Developer console) when you're signed in
as a management account administrator.
