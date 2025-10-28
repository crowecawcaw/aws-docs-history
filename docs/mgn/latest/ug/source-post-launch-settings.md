NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Review post-launch settings

Post-launch settings allow you to control and automate actions performed after the server
has been launched in AWS. These settings are created automatically based on the **Post-launch settings template.**

You must activate the post-launch actions using one of these options:

- **Activating the post-launch actions for a specific
  server**:

      + Navigate to the **Source servers** page and select a
       source server.
      + Click **Post-launch settings > Edit**.
      + You are redirected to the **Edit post-launch
       settings** screen. Activate the toggle and click **Save
       settings**.

  Alternatively, you can select a specific source server, open the **Test and cutover** drop-down menu located in the top right corner of the screen and
  select **Edit post-launch settings** .

- **Activating the post-launch actions for all
  servers**:

      + Navigate to the **Settings** page and choose **Post-launch settings template**. You only need to do this once
       and the change applies to all newly added servers.


      After the post-launched actions have been activated from the template, you can
       deactivate and activate them for individual servers. [Learn more about activating post-launch
       settings.](post-launch-settings.md#post-launch-settings-activation "post-launch-settings.md#post-launch-settings-activation")

  The settings configured in the template are applied to every newly added server. You
  can change the settings for existing and newly added servers individually within the server
  details view.

The **Post-launch settings** template allows you to control
various post-launch actions, including:

- Deployment of test and cutover instances
- Disaster recovery configuration (installing the AWS Replication Agent for AWS DRS and
  configuring the target disaster recovery AWS Region)
- Operating system conversion on the target machine
- License and subscription changes on the target machine
