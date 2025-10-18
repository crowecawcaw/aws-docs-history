# View device details in an AWS Cloud WAN global network

View details about a device. On the device details page you can access tabs:


* **Overview**


This tab provides general information about the device, such as the device State,
 Vendor, and Model. You can also edit, delete, and associate or disassociate the
 device with a site,
* **Links**


Associate or disassociate a link with a device.
* **On-premises associations**


Associate or disassociate a device with a customer gateway. You must have at least
 one gateway set up and one link to create the association.
* **Connect peer associations**


Associate a Connect peer with a device, allowing you to connect with a transit
 gateway. You must have at least one Connect peer and one link.
* **Connections**


Create a connection between two devices using a link. You can create a connection
 between two devices in your global network. The connection can be between a physical
 or virtual appliance and a third-party appliance in a VPC, or between physical
 appliances in an on-premises network. A connection is created for a specific global
 network and cannot be shared with other global networks.
* **VPNs**


View the VPNs associated with the device. On this tab you can only view the
 associations of a transit gateway with a device.
* **Monitoring**


Monitor the device's data in, data out, and Tunnel down count average with
 CloudWatch metrics. You can modify the CloudWatch time frame as well as add these
 metrics to your global network dashboard.
###### Topics

* [Associate or disassociate a device](cloudwan-device-link-associate.md "cloudwan-device-link-associate.md")
* [Associate or disassociate an on-premises link](cloudwan-devices-on-premises.md "cloudwan-devices-on-premises.md")
* [Associate or disassociate a Connect peer link](cloudwan-devices-connect-peer.md "cloudwan-devices-connect-peer.md")
* [Create or delete a device connection](cloudwan-devices-connections.md "cloudwan-devices-connections.md")
* [View VPNs](cloudwan-devices-vpns.md "cloudwan-devices-vpns.md")
* [Monitor devices](cloudwan-devices-monitoring.md "cloudwan-devices-monitoring.md")
