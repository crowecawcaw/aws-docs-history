# Step B: Prepare each

AWS Elemental Conductor File
node
for migration

Prepare the nodes during one or more maintenance windows. The number of windows
depends on the number of nodes you can complete in one maintenance window.

## Upgrade to the latest 2.17 minor

version

To upgrade to version 2.18 or higher, the software currently installed on the node
must be version 2.17.0 or higher.

- If the Conductor nodes are on one version and the worker nodes are on a
  different version, upgrade all nodes to the same version.

## Verify access to the BMC on the

appliances

Make sure that you have access to the BMC on each appliance:

- On a Dell server, make sure that iDRAC is installed and that you can start
  it.
- On an SMC server, make sure that IPMI is installed and that you can start
  it.

You can install iDRAC or IPMI even when the node is active — when AWS Elemental Server is running
events or Conductor is controlling the cluster.

## Note the network adapter for the management interface

Make a note of the management network device listed in the web UI under
**Settings**, **Network**, **Network
Settings**, **Current Settings**, **Network
Devices**. By default, eth0 is the management network device, but this
may differ on your system. You'll need to know this adapter later during the
migration process.

## Update firmware

Both the BIOS firmware and the BMC firmware (IPMI for SuperMicro, iDRAC for Dell)
must be at the latest versions available from the manufacturer. They must be at the
latest versions before you can set the boot mode to UEFI.

We recommend that you update the firmware on all your nodes at the same time. We
also recommend that you perform this update during a maintenance window. If you need
to upgrade to the latest 2.17 version of the AWS Elemental software, you might want to
perform both tasks during the same maintenance window.

After you install the firmware, you must reboot each node. For more information,
see [Updating firmware](migrate-topic-firmware.md "migrate-topic-firmware.md").

## Move custom files

You might have custom files in `/opt/elemental_se/scripts` on the node.
These are files that you created. They aren't part of the installation of the Conductor File
or AWS Elemental Server software, and they aren't backed up and restored.

Copy these files to storage off the node, so that you can copy the files back to
the node after you've upgraded it.
