# Users unable to use their subscription on AWS

websites

**Problem: Users are unable to use their subscriptions on AWS
websites**

When attempting to use Amazon Q [in the AWS Management Console, and on AWS apps and
websites](q-on-aws.md "q-on-aws.md"), users see the following message in their browser:

`Your account has not been configured to use an Amazon Q subscription. You currently have access
 to the Free tier of Amazon Q. Contact your AWS administrator to configure your
 subscription.`

**Solutions:**

- Verify that identity-enhanced console sessions are enabled (only available with
  organization instances of IAM Identity Center). For information about how to enable identity-enhanced
  console sessions, see [Enabling
  identity-enhanced console sessions](../../../singlesignon/latest/userguide/identity-aware-sessions.md "../../../singlesignon/latest/userguide/identity-aware-sessions.md").
- Check that the user has an active Amazon Q Developer Pro subscription. For more information, see
  [Amazon Q Developer subscription statuses](q-admin-setup-subscribe-status.md "q-admin-setup-subscribe-status.md").
- Verify that you're not using an account instance of IAM Identity Center. Account instances don't
  support console access. For more information, see [Account instance considerations](../../../singlesignon/latest/userguide/account-instances-identity-center.md#about-account-instance "../../../singlesignon/latest/userguide/account-instances-identity-center.md#about-account-instance") in the
  _AWS IAM Identity Center User Guide_.

Users with identities in an account instance of IAM Identity Center can still use Amazon Q in the console
but will be limited to Free tier.

- If the user recently switched from the Free tier to the Pro tier, have them sign out of
  the AWS Management Console or another AWS website and sign back in again.
- If you subscribed the user as part of a group, allow up to 24 hours for their
  subscription to be activated. There might be a delay between the time the user is added to
  the group and the time their subscription becomes active.
- Verify that the user's access to the Amazon Q Developer Pro managed application was not revoked
  or that the managed application was not deleted. Restore access to the managed application
  if needed.
- If users don't have an active subscription, try getting them to refresh their page so
  that they can use the Free tier.
