This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Configure Ethernet Devices on AWS Elemental Statmux Nodes

When you installed each AWS Elemental product in the cluster, you configured eth0. You can now set up eth1 and any additional Ethernet devices. Optionally, you can also bond two devices that you have set up.

###### Ethernet devices and the management interface

When you installed AWS Elemental Statmux, you configured eth0 as the management interface. Note
that setting up a device as the management interface does _not_ dedicate
this device to management traffic. The device can still handle other traffic.

###### Topics

- [Add Ethernet Devices](config-wrkr-sm-cg-ethernet-add.md "config-wrkr-sm-cg-ethernet-add.md")
- [Bond Ethernet Devices](config-wrkr-sm-cg-ethernet-bond.md "config-wrkr-sm-cg-ethernet-bond.md")
