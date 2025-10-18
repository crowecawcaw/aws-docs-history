# Modify AWS Cloud WAN networks

After setting up your AWS Cloud WAN global and core networks set up, you can further modify these
 networks by performing a number of different tasks. 

###### Note

Modifying a global network or a core network requires that both be set up first. If you
 haven't yet created either, see [Quick start: Create an AWS Cloud WAN global network and
 core network](cloudwan-getting-started.md "cloudwan-getting-started.md") for the steps to
 create a global or core network. 

 Tasks you can perform to modify your global and core networks include: 


* **Add attachments.**


Add Connect, Site-to-Site VPN, VPC, or transit gateway route table attachments. In addition, you
 can create Connect peers.

* **Create a policy version.**


Create and deploy a version of any policy to become your new core network. You can
 create a policy version through either the Network Manager console or by modifying a JSON file.
* **Add sites, devices, and links.**


Add representations of physical devices and sites to your global network. You can then
 create a link that associates a device and a site.
* **Register transit gateways.**


Register transit gateways you've created in Amazon Virtual Private Cloud (VPC) with your Cloud WAN
 network. This allows you to view and monitor transit gateway resources within the
 network.
* **Create a peering.**


Create a peering connection to enable communication between your core network and
 transit gateways.
* **Share your core network.**


Share your core network across accounts or across your organizations. You can set
 permissions to allow users to view and modify network resources.
* **Share attachments**.


Share your VPC and transit gateway route table attachments from your shared core
 network. You can set permissions to allow users to create new VPC or transit gateway route
 table attachments.
* **Access network dashboards.**


Cloud WAN includes separate global network, core network, transit gateway network, and
 transit gateway dashboards. On these dashboards you can view logical trees and geographic
 maps of your networks, which includes attachments, sites and devices. You can also view
 monitoring and events dashboards, allowing you to view Amazon CloudWatch metrics and
 to set threshold alarms on these metrics.
###### Topics

* [Global and core networks](cloudwan-networks-working-with.md "cloudwan-networks-working-with.md")
* [Attachment tags](cloudwan-tags.md "cloudwan-tags.md")
* [Attachments](cloudwan-create-attachment.md "cloudwan-create-attachment.md")
* [Core network policy versions](cloudwan-create-policy-version.md "cloudwan-create-policy-version.md")
* [Devices](cloudwan-devices.md "cloudwan-devices.md")
* [Peerings](cloudwan-peerings.md "cloudwan-peerings.md")
* [Shared attachments](cloudwan-shared-attachments.md "cloudwan-shared-attachments.md")
* [Shared core network](cloudwan-share-network.md "cloudwan-share-network.md")
* [Shared peerings](cloudwan-shared-peerings.md "cloudwan-shared-peerings.md")
* [Sites and links](cloudwan-sites-links.md "cloudwan-sites-links.md")
* [Transit gateways](cloudwan-tgws-about.md "cloudwan-tgws-about.md")
