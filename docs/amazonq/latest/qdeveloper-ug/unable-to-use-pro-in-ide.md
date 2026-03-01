# Users unable to use their subscription in the IDE

**Problem: IAM Identity Center workforce users are unable to use their Pro subscriptions
in the IDE**

**Solutions:**

- Check that the user has an active Amazon Q Developer Pro subscription. For more information, see
  [Amazon Q Developer subscription statuses](q-admin-setup-subscribe-status.md "q-admin-setup-subscribe-status.md").
- If the user recently switched from the Free tier to the Pro tier, have them sign out of
  Amazon Q in the IDE and sign back in again.
- If you subscribed the user as part of a group, allow up to 24 hours for their
  subscription to be activated. There might be a delay between the time the user is added to
  the group and the time their subscription becomes active.
- Verify that the user's access to the Amazon Q Developer Pro managed application was not revoked or
  that the managed application was not deleted. Restore access to the managed application if
  needed.
- Have users sign in with a Builder ID to use the Free tier while they wait for their
  subscription to become active. For more information, see [Installing the Amazon Q Developer extension or plugin in your IDE](q-in-IDE-setup.md "q-in-IDE-setup.md").
