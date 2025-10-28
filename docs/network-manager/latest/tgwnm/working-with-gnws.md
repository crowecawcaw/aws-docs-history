# Modify a global network using AWS Network Manager

After setting up a global network you further modify it by performing a number of tasks.

Tasks you can perform to enhance your global network include:

- **Monitor and manage global network resources from other AWS
  accounts.**

AWS Global Networks for Transit Gateways supports multi-account access. If enabled, multi-account allows you to
manage, monitor, and view dashboards of resources from AWS accounts shared with
your account.

- **Register a transit gateway**

Register existing transit gateways in your global network. When you register a
transit gateway all transit gateway attachments are automatically included in the
registration. A transit gateway must first be created before it can be registered.
For more information about transit gateways and creating one, see [Transit
gateways](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md") in the _Amazon VPC Transit Gateways User Guide_.

- **Create sites and links, and connect devices**

Add representations of physical devices and sites to your global network. You can
then create a link that associates a device and a site.

- **Create customer gateway associations**

Create associations between two devices or between a device and a transit gateway
Connect peer.

- **Access global network dashboards**

AWS Global Networks for Transit Gateways includes separate transit gateway network and transit gateway
dashboards. On these dashboards you can view logical trees and geographic maps of
your networks, which includes attachments, sites and devices. You can also view
monitoring and events dashboards, allowing you to view Amazon CloudWatch metrics and
to set threshold alarms on these metrics.
If your account is set up for multi-account, you can manage global network resources from multiple AWS accounts. For more information on multi-account, see [Multi-account in AWS Global Networks for Transit Gateways](nm-multi-account.md "nm-multi-account.md").

###### Contents

- [Multi-account](nm-multi-account.md "nm-multi-account.md")
- [Global networks](global-networks.md "global-networks.md")
- [Transit gateway registrations](tgw-registrations.md "tgw-registrations.md")
- [Sites and links](nm-sites.md "nm-sites.md")
- [Devices](nm-devices.md "nm-devices.md")
- [Connections](device-connections.md "device-connections.md")
- [Gateway associations](gw-association.md "gw-association.md")
- [Resource tags](gnw-tagging.md "gnw-tagging.md")
