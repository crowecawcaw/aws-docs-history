NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Configuring launch settings

After you have added your source servers to the AWS Application Migration Service console, you will need to
configure the launch settings for each server. The launch settings are a set of instructions
that determine how a test or cutover instance will be launched for each source server on AWS.
You must configure the launch settings prior to launching test or cutover instances. You can use
the default settings or configure the settings to fit your requirements.

###### Note

You can change the launch settings after a test or cutover instance has been launched. You
will need to launch a new test or cutover instance for the new settings to take effect.

You can access the launch settings by clicking on the source server name of a source server
on the **Source servers** page.

Within the individual server view, navigate to the **Launch
settings** tab.

Here you can see your **General launch settings** and
**EC2 launch template**. Click the **Edit** button to edit your Launch settings or **Modify**
to change your EC2 launch template.

Launch settings are composed of the following:

- **Instance type right-sizing** – The Instance type
  right-sizing feature allows AWS Application Migration Service to launch a test or cutover instance type that best
  matches the hardware configuration of the source server. When activated, this feature
  overrides the instance type selected in the EC2 launch template.
- **Start instance upon launch** – Choose whether you want to
  start your test and cutover instances automatically upon launch or whether you want to start
  them manually through the Amazon EC2 Console.
- **Copy private IP** – Choose whether you want Application
  Migration Service to verify that the private IP used by the test or cutover instance matches
  the private IP used by the source server.
- **Transfer server tags** – Choose whether you want AWS Application Migration Service
  to transfer any user-configured custom tags from your source servers to your test or cutover
  instance.
- **OS Licensing** – Choose whether you want to Bring Your Own
  Licenses (BYOL) from the source server to the test or cutover instance.
  AWS Application Migration Service automatically creates an **EC2 launch template** for
  each new source server. AWS Application Migration Service bases the majority of the instance launch settings on this
  template. You can edit this template to fit your needs.

[Learn more about Launch settings.](launch-settings.md "launch-settings.md")
