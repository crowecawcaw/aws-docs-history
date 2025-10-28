# Deleting the Amazon Q Developer profile

###### Note

This section does not apply to personal accounts (Builder IDs).

You might want to delete the Amazon Q Developer profile to quickly cancel all subscriptions and
remove all Q Developer configurations from your AWS account. When you delete the Amazon Q Developer
profile, the following occurs:

- All subscriptions associated with the profile marked as
  **Canceled**, and users will no longer be able to access
  Amazon Q Developer features. The final monthly subscription fee is charged at the end of the
  current billing cycle for all users who had active subscriptions. You'll be charged
  for the full month; the fee won't be prorated. Subscriptions will continue to be
  visible in the Amazon Q Developer console until the end of the month, at which time they will
  be removed from view.
- All settings and options in the Amazon Q Developer console that became available as a result
  of creating the profile will no longer be visible or take effect. For example, the Q
  Developer dashboard will no longer be visible, customizations will no longer be
  configurable or applied, and user activity reports will no longer be configurable or
  generated.
- The managed application (called
  **QDevProfile-`region`**) will be
  removed from the IAM Identity Center instance that is connected to Amazon Q Developer. (This IAM Identity Center instance
  might be a different account from the one where the profile is being deleted,
  depending on your [deployment option](deployment-options.md "deployment-options.md").)

###### Note

If you accidentally delete the profile:

- You'll have to recreate it and then resubscribe users. You'll also have to reset
  any settings you configured previously through the Amazon Q Developer console. Your IAM Identity Center
  instance will remain, so there is no need to recreate user identities.
- You won't be able to see historical data in the Amazon Q Developer dashboard after
  recreating the profile; you can only see data starting from the date of the new
  profile creation onward.
  Use the following instructions to delete the Amazon Q Developer profile.

###### Before you begin

- Remove any customizations you might have created to allow for the successful
  deletion of the profile.

###### To delete the Amazon Q Developer profile

1. Sign in to the AWS Management Console.
2. Switch to the Amazon Q Developer console.

To use the Amazon Q Developer console, you must have the permissions defined in [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users "id-based-policy-examples-admins.md#q-admin-setup-admin-users"). 3. Choose **Settings**. 4. Near the top of the page, choose **Delete profile**.
