# Step B: Prepare the Elemental Live node for

migration

## Upgrade to the latest 2.25 minor

version

To upgrade to version 2.26.0 or higher, the software currently
installed on the node must be version 2.25.5 or higher. For instructions about how
to upgrade to that version, see the [AWS Elemental Live Upgrade Guide](../upgradeguide.md "../upgradeguide.md").

## Verify access to the BMC on the

appliances

Make sure that you have access to the BMC on each appliance:

- On a Dell server, make sure that iDRAC is installed and that you can start
  it.
- On an SMC server, make sure that IPMI is installed and that you can
  install it.

You can install iDRAC or IPMI even when Elemental Live is running events.

## Update firmware

Both the BIOS firmware and the BMC firmware (IPMI for SuperMicro, iDRAC for Dell)
must be at the latest versions that have been qualified by AWS Elemental. They must be at
the latest versions before you can set the [boot mode to UEFI](migrate-worker-boot-mode-uefi.md "migrate-worker-boot-mode-uefi.md"). To obtain the
versions, go to the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter"), and read the Knowledge article [Latest AWS Elemental Qualified Remote Management and BIOS Firmware](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/Latest-AWS-Elemental-Qualified-Remote-Management-and-BIOS-Firmware "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/Latest-AWS-Elemental-Qualified-Remote-Management-and-BIOS-Firmware") or
open a case.

We recommend that you update the firmware on all your nodes at the same time. We
also recommend that you perform this update during a maintenance window. After you
install the firmware, you must reboot the node. For more information, see Update firmware.

## Make a note of router

information

This information applies if the appliance is connected to an SDI input using a
router. After you upgrade, the node will still have information about the SDI inputs
and about the router, but it will be missing the mapping from the inputs to the
router.

In order to reconfigure the information accurately, make a note of the current
configuration: on the Elemental Live web interface, hover over **Settings**
and choose **Routers**.

## Move custom files

You might have custom files in `/opt/elemental_se/scripts` on the node.
These are files that you created. They aren't part of the installation of the Elemental Live
software, and they aren't backed up and restored.

Copy these files to storage off the node, so that you can copy the files back to
the node after you've upgraded it.
