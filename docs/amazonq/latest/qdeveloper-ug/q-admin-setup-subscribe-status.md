# Amazon Q Developer subscription statuses

Subscription status information varies depending on whether you're an end-user with a personal
account (Builder ID), or you're an administrator of IAM Identity Center workforce users.

## Personal account (Builder ID) users

If you are a user with a personal account (Builder ID), you can view the status of your Amazon Q Developer Pro
subscription on the **Subscriptions** page of the Amazon Q Developer console.

The possible statuses of your subscription are:

- **Active** – You have activated your
  subscription by using Amazon Q Developer features. You are being charged for your
  subscription.
- **Canceled** – You canceled your subscription by
  unsubscribing from the Pro tier. You can no longer access Amazon Q Developer features and
  limits. For more information, see [Unsubscribing from Amazon Q Developer Pro](q-admin-setup-unsubscribe.md "q-admin-setup-unsubscribe.md").

## IAM Identity Center workforce users

If you're an administrator who has subscribed a set of IAM Identity Center workforce users to the Pro
tier, you can view the status of your users' subscriptions on the
**Subscriptions** page of the Amazon Q Developer console.

The statuses will be slightly different depending on whether you’re looking at the
**Groups** tab or the **Users** tab.

The statuses on the **Groups** tab are:

- **Subscribed** – The group is subscribed to
  Amazon Q Developer Pro. You will be charged for active user subscriptions in the group.
- **Canceled** – The group was canceled
  (unsubscribed) by an administrator. Users in the group can no longer access Amazon Q Developer Pro
  features. For more information, see [Unsubscribing from Amazon Q Developer Pro](q-admin-setup-unsubscribe.md "q-admin-setup-unsubscribe.md").

The statuses on the **Users** tab are:

- **Active** – The user has activated their
  subscription by using Amazon Q Developer features. You are being charged for this
  subscription.
- **Pending** – The user is subscribed but has not
  activated their subscription. You are not being charged for this subscription.
- **Canceled** – The user's subscription was
  canceled (unsubscribed) by an administrator, and the user can no longer access
  Amazon Q Developer features. For more information, see [Unsubscribing from Amazon Q Developer Pro](q-admin-setup-unsubscribe.md "q-admin-setup-unsubscribe.md").

###### Note

The **Users** tab of the Amazon Q Developer console does
_not_ show users who are subscribed as part of a group. To
see these users, navigate to the Amazon Q console's (_not_ the
Amazon Q Developer console's) **Subscriptions** page. On this page,
group-subscribed users will appear with a status of
**Unavailable**. To see their actual status, choose a user
from the table, and look for their status under **User
associations**.
