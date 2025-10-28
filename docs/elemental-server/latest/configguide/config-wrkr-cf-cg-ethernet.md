This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Configure Ethernet Devices on AWS Elemental Server Nodes

When you installed each AWS Elemental product in the cluster, you configured eth0. You can now set up eth1 and any additional Ethernet devices. Optionally, you can also bond two devices that you have set up.

###### Ethernet devices and the management interface

When you installed AWS Elemental Server, you configured eth0 as the management interface. Note
that setting up a device as the management interface does _not_ dedicate
this device to management traffic. The device can still handle other traffic.

###### Topics

- [Add Ethernet Devices](config-wrkr-cf-cg-ethernet-add.md "config-wrkr-cf-cg-ethernet-add.md")
- [Bond Ethernet Devices](config-wrkr-cf-cg-ethernet-bond.md "config-wrkr-cf-cg-ethernet-bond.md")

###### Important

If you use the Linux CLI to configure network interfaces, DO NOT use the web interface to
manage network settings. This will overwrite networking configurations that were made using
the CLI.
