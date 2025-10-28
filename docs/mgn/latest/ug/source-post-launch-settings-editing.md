NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Editing the post-launch settings

To edit the post-launch settings for a single source servers, check the box to the left of
the Hostname of each source server for which you want to edit the post-launch settings, open
the **Replication** menu, and choose **Edit
post-launch settings**.

Alternatively, when editing the settings for a single server, you can choose **Edit** from the **Post-launch settings**
tab.

These settings can be edited within the post-launch settings template. Once you
have edited all your settings, click **Save template**.

## Types of post-launch actions

AWS MGN supports post-launch modernization actions, giving you the opportunity to move
and improve. All post-launch actions are based on SSM documents (either public or ones you
created) that can executed on your EC2 launch instances.

There are 2 types of post-launch actions:

- **Predefined post-launch actions** – These out-of-the box
  actions are based on public SSM documents that cannot be changed and have certain
  unchangeable parameters such as the platform name and order. Fields are prepopulated with
  the necessary values and only need to be activated or deactivated. For a list of the available actions, see [Predefined post-launch actions
  reference](predefined-post-launch-actions.md "predefined-post-launch-actions.md")
- **Custom post-launch actions** – These actions are based
  on SSM documents that you create and upload to your account.

To add a custom post-launch action, see [Create a custom
post-launch action](post-launch-settings.md#post-launch-settings-custom-actions-add "post-launch-settings.md#post-launch-settings-custom-actions-add").
To edit a custom post-launch action, see [Edit custom post-launch
actions](post-launch-settings.md#post-launch-settings-custom-actions-edit "post-launch-settings.md#post-launch-settings-custom-actions-edit").

Use the **Filter by** options on the left-hand side to
filter the available actions according to your preferences.

Click the settings icon in the right-hand corner of the screen to alternate between card
and list view, according to your preferences.
