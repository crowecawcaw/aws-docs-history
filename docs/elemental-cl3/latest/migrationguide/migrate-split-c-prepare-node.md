# Step B: Prepare each node

Prepare the nodes during one or more maintenance windows. The number of windows
depends on the number of nodes you can complete in one maintenance window.

## Upgrade to the latest 3.25 minor

version

To upgrade to version 3.26.1 or higher (version 2.26.x or higher for
workers nodes), the software currently installed on the node must be version 3.25.5
or higher (or 2.25.5).

- If the Conductor nodes are currently on version 3.25.5 or higher (or 2.25.5 or
  higher), you don't have to upgrade to a higher patch.
- If the Conductor nodes are on one major version and the worker nodes are on a
  different major version, upgrade all nodes to the same major version.
  Normally, there is a rule that Conductor Live can be a lower major version than the
  workers. This rule doesn't apply when upgrading to 3.26.1 or higher. All the
  nodes in the cluster must be running version 3.25.5 (or 2.25.5) or
  higher.
- If the Conductor nodes are on a version below 3.25.5, upgrade to the current
  highest patch version.

To upgrade to 3.25.5 or higher (or 2.25.5), see the [AWS Elemental Conductor Live Upgrade Guide](../upgradeguide.md "../upgradeguide.md").

## Verify access to the BMC on the

appliances

Make sure that you have access to the BMC on each appliance:

- On a Dell server, make sure that iDRAC is installed and that you can start
  it.
- On an SMC server, make sure that IPMI is installed and that you can
  install it.

You can install iDRAC or IPMI even when the node is active — when Elemental Live is running
events or Conductor is controlling the cluster.

## Update firmware

Both the BIOS firmware and the BMC firmware (IPMI for SuperMicro, iDRAC for Dell)
must be at the latest versions that have been qualified by AWS Elemental. They must be at
the latest versions before you can set the boot mode to UEFI, as part of [upgrading each node](migrate-split-c-upgrade-w-nodes.md "migrate-split-c-upgrade-w-nodes.md"). To obtain
these versions, go to the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter"), and read the Knowledge article [Latest AWS Elemental Qualified Remote Management and BIOS Firmware](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/Latest-AWS-Elemental-Qualified-Remote-Management-and-BIOS-Firmware "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/Latest-AWS-Elemental-Qualified-Remote-Management-and-BIOS-Firmware") or
open a case.

We recommend that you update the firmware on all your nodes at the same time. We
also recommend that you perform this update during a maintenance window. If you need
to upgrade to the latest 3.25.5 (2.26.x) version of the AWS Elemental software,
you might want to perform both tasks during the same maintenance window.

After you install the firmware, you must reboot each node. For more information,
see [Updating firmware](migrate-topic-firmware.md "migrate-topic-firmware.md").

## Make a note of node

assignments

Before you upgrade any worker node, you must make a note of the channels that are
assigned to this node. You will use this information to restart the channels, after
you've completed the migration.

1. On the web interface for the primary Conductor node, access the
   **Channels** screen.
2. Filter the information on the screen to show one node. Then make a note of
   all the channels that are assigned to that node.
3. Repeat for each node.

## Make a note of router

information

This information applies if the cluster includes nodes that connected to an SDI
input using a router. After you upgrade, the cluster will still have information
about the SDI inputs and about the router, but it will be missing the mapping from
the inputs to the router.

In order to reconfigure the information accurately, make a note of the current
configuration. For more information see the information about configuring routers in
the _Reference: Configure connectivity_ section of
the [AWS Elemental Conductor Live Configuration Guide](../configguide.md "../configguide.md").

## Move custom files

You might have custom files in `/opt/elemental_se/scripts` on the node.
These are files that you created. They aren't part of the installation of the Conductor Live
or Elemental Live software, and they aren't backed up and restored.

Copy these files to storage off the node, so that you can copy the files back to
the node after you've upgraded it.
