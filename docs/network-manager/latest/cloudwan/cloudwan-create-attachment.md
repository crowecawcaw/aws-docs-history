# Attachments in AWS Cloud WAN

You can work with core network attachments using the Amazon VPC Console or the command line or
 API. 

Attachment states can be one of the following. Attachment states appear on the Attachments
 page of the AWS Cloud WAN console.


* **Creating** — Creation of an attachment is in process.
* **Deleting** — Deletion of an attachment is in process.
* **Pending network update** — Waiting for the connection of
 attachments to the core network.
* **Pending tag acceptance** —
 Waiting for the core network owner to review the tag
 change for an attachment.
* **Pending attachment acceptance** — Waiting for the core network
 owner to accept or reject an attachment.
* **Rejected** — The core network owner rejected the
 attachment.
* **Available** — The attachment is fully functional.
* **Failed** — The attachment failed to attach to the core
 network. For example, this might be due to an input error or a service linked role
 issue.
The following are the supported core network attachment types. 


* Direct Connect
* Connect


You can also create a Connect peer through the Network Manager console.
* VPC
* Transit gateway route table
You can create an attachment using either using the Network Manager console or by using the command
 line or API.


## Route evaluation


Cloud WAN evaluates routes at each core network edge in the following order:



1. The most specific route for the destination
2. For routes with the same destination IP address, but different targets, the
 following route priority is used:




	1. Static routes
	2. VPC-propagated routes in the same Region.
	3. For dynamic routes received at the core network with an
	 *unequal* AS path length and/or MED BGP
	 attributes, Cloud WAN evaluates them in the following order:
	
	
	
	
		1. AS path length
		2. MED
	4. For dynamic routes received at the core network with
	 *equal* AS path length and MED BGP attributes,
	 Cloud WAN evaluates them in the following order:
	
	
	
	
		1. AWS Direct Connect gateway-propagated routes.
		2. Cloud WAN Connect-propagates routes in the same
		 Region.
		3. Site-to-Site VPN-propagated routes in the same
		 Region.
		4. Routes propagated from other sources, such as transit gateway peering
		 and core network edges in other remote Regions
		 over the AWS global infrastructure. If identical routes are
		 received from two or more sources, a single attachment will be
		 chosen in a deterministically random manner.

###### Topics

* [Connect attachments and Connect peers](cloudwan-connect-attachment.md "cloudwan-connect-attachment.md")
* [Direct Connect gateway
 attachments](cloudwan-dxattach-about.md "cloudwan-dxattach-about.md")
* [VPC attachments](cloudwan-vpc-attachment.md "cloudwan-vpc-attachment.md")
* [Site-to-Site VPN attachments in Cloud WAN](cloudwan-s2s-vpn-attachment.md "cloudwan-s2s-vpn-attachment.md")
* [Transit gateway route table attachments](cloudwan-tgw-attachment.md "cloudwan-tgw-attachment.md")
* [Accept or reject a core network attachment](cloudwan-attachments-acceptance.md "cloudwan-attachments-acceptance.md")
* [Delete an attachment](cloudwan-attachments-deleting.md "cloudwan-attachments-deleting.md")
