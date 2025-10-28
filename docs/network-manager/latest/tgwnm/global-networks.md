# Global networks in AWS Global Networks for Transit Gateways

A global network in AWS Global Networks for Transit Gateways is a container for your network objects. When you create a
global network, you create only the framework of the global network itself. You'll then further
define this network by adding network objects to it, such as

- transit gateways.
- sites, devices, and links, and then creating connections using links between those sites
  and devices.
- customer gateway associations.
- Connect peer associations.

###### Note

When creating a global network, you're prompted to create an associated core network. A core
network is a feature of AWS Cloud WAN and is not needed if you're not using this feature. While
creating a global network, you're prompted whether or not to create a core network. Clear the
option to create the core network. If you decide later on that you want to create a core
network for this global network you can. For the steps to create a core network, see [What is
AWS Cloud WAN](../cloudwan/what-is-cloudwan.md "../cloudwan/what-is-cloudwan.md") in the _AWS Cloud WAN User Guide._

You can create, view, update, and delete a global network using either the AWS Network Manager console
or by using the CLI.

###### Global network tasks

- [Create a global network](global-networks-creating.md "global-networks-creating.md")
- [View a global network](global-networks-viewing.md "global-networks-viewing.md")
- [Update a global network](global-networks-updating.md "global-networks-updating.md")
- [Delete a global network](global-networks-deleting.md "global-networks-deleting.md")
