NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Activating and deactivating post-launch

actions

This setting controls whether post-launch actions are active or inactive. You must leave
the **Install Systems Manager agent and allow executing actions on launched
servers** option toggled in order for post-launch actions to work. Untoggling the
option disallows AWS MGN to install the SSM Agent on your servers and post-launch actions
are no longer executed on them.

The feature is activated and deactivated at the account level from the **Settings > Post-launch template** screen. [Learn more about activating post-launch
settings](post-launch-settings.md#post-launch-settings-activation "post-launch-settings.md#post-launch-settings-activation").

After it was activated once, the feature can also be deactivated and reactivated for a
single server. Simply selecting a server, go to the **Post-launch
settings** tab and click **Edit**.

When the feature is inactive:

- All actions are hidden.
- You are not able to activate actions at the account level or the feature
  level.
  When the feature is active:

- The actions are visible.
- You can activate them.
