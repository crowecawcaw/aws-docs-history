# Update an Amazon GameLift Servers fleet configuration

Use the Amazon GameLift Servers console or the AWS CLI to update your fleet settings, change remote
locations, or delete a fleet. For managed fleets, you can't change a fleet's game server
build or instance type. Instead, you must replace the fleet.

###### Fast Build Update Tool (for development only)

With managed EC2 fleets, to deploy a game server build update,
you need to upload each new build to Amazon GameLift Servers and create a new fleet for it.

The Fast Build Update Tool lets you can bypass these steps during development,
saving you time and allowing for faster development iteration. With this tool, you
can quickly update your game build files across all computes in an existing fleet.
The tool has several options; you can replace an entire game build or change
6 specific files, and you can manage how to restart game server processes after
the updates. You can also use it to update individual computes in a fleet.

To get the Fast Build Update Tool and learn more about how to use it, visit the Amazon GameLift Servers Toolkit repo for
[The Fast Build Update Tool](https://github.com/aws/amazon-gamelift-toolkit/tree/main/fast-build-update-tool "https://github.com/aws/amazon-gamelift-toolkit/tree/main/fast-build-update-tool") in Github.

You can update mutable fleet attributes, port settings, and runtime configurations
using the Amazon GameLift Servers console or the AWS CLI. To change scaling limits, see [Auto-scale fleet capacity with Amazon GameLift Servers](fleets-autoscaling.md "fleets-autoscaling.md").

Console

1. In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), in the navigation pane, choose
   **Fleets**.
2. Choose the fleet you want to update. A fleet must be in
   `ACTIVE` status before you can edit it.
3. On the Fleet detail page, in any of the following sections, choose
   **Edit**.
   - **Fleet settings**
     - Change the fleet attributes such as
       **Name** and
       **Description**.
     - Add or remove **Metric groups**,
       that Amazon CloudWatch uses to track aggregated Amazon GameLift Servers metrics
       for multiple fleets.
     - Update **Resource creation
       limit** settings.
     - Turn game session protection on or off.

   - **Runtime configuration** – You
     can change any of the following settings of your runtime
     configurations and add or remove runtime
     configurations.
     - Change the **Launch path** of
       your game server.
     - Add, remove, or change optional **Launch
       parameters**.
     - Change the number of **Concurrent
       processes** that your game servers
       run.

   - **Game session activation** –
     Change how you want server processes to run and host game
     sessions by updating **Max concurrent game session
     activations** and **New activation
     timeout**.
   - **EC2 port settings** – Update the
     IP addresses and port ranges that allow inbound access to
     the fleet.

4. Choose **Confirm** to save changes.

AWS CLI

Use the following AWS CLI commands to update a fleet:

- [update-fleet-attributes](../../../cli/latest/reference/gamelift/update-fleet-attributes.md "../../../cli/latest/reference/gamelift/update-fleet-attributes.md")
- [update-fleet-port-settings](../../../cli/latest/reference/gamelift/update-fleet-port-settings.md "../../../cli/latest/reference/gamelift/update-fleet-port-settings.md")
- [update-runtime-configuration](../../../cli/latest/reference/gamelift/update-runtime-configuration.md "../../../cli/latest/reference/gamelift/update-runtime-configuration.md")
