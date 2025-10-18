# Shared AWS Cloud WAN core network

You can use AWS Resource Access Manager to share a core network across accounts or across your organization.
 By default, AWS Identity and Access Management (IAM) users do not have permission to create or modify AWS RAM
 resources. To allow users to create or modify resources and perform tasks, you must
 create IAM policies that grant permission to use specific resources and API actions. You
 then attach those policies to the users or groups that require those permissions.

Only the network owner can perform the following operations:


* Create a resource share.
* Create a core network.
* Update a resource share.
* View a resource share.
* View the resources shared by your account, across all resource shares.
* View the principals with whom you're sharing your resources, across all resource
 shares. Viewing these principals provides you with the information to determine who
 has access to your shared resources.
* Delete a resource share.
You can perform the following operations on resources that are shared with you:


* Accept or reject a resource share invitation.
* View a resource share.
* View the shared resources that you can access.
* View a list of all of the principals that are sharing resources with you.
* Run the `list-core-networks` API to view information about the core
 networks you own. See [list-core-networks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/list-core-networks.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/list-core-networks.html").
* Run the APIs that create, view, and delete attachments:


###### Note

A shared core network supports only VPC and transit gateway route table attachments.




	+ Create a VPC attachment: [create-vpc-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-vpc-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-vpc-attachment.html")
	+ Get a VPC attachment: [get-vpc-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-vpc-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-vpc-attachment.html")
	+ Delete a VPC attachment: [delete-vpc-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-vpc-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-vpc-attachment.html")
	+ Create a transit gateway route table attachment:
	 [create-transit-gateway-route-table-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-transit-gateway-route-table-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-transit-gateway-route-table-attachment.html")
	+ Get a transit gateway route table attachment: [get-transit-gateway-route-table-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-transit-gateway-route-table-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-transit-gateway-route-table-attachment.html")
	+ Delete a transit gateway route table attachment: [delete-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-attachment.html")
	+ Create a Direct Connect gateway attachment: [create-direct-connect-gateway-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-direct-connect-gateway-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-direct-connect-gateway-attachment.html")
	+ Get a Direct Connect gateway attachment: [get-direct-connect-gateway-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-direct-connect-gateway-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-direct-connect-gateway-attachment.html")
	+ Update a Direct Connect gateway attachment: [update-direct-connect-gateway-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-direct-connect-gateway-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-direct-connect-gateway-attachment.html")
* Leave a resource share.
When a core network is shared with an account, the account that accepts the shared core
 network can't make any changes to it, but it can create VPC attachments, transit gateway route table
 attachments, and Direct Connect gateway attachments to the shared network.

###### Important

You must share your global resource from the N. Virginia (us-east-1) Region so that
 all other Regions can see the global resource.

###### Topics

* [Share a core network](cloudwan-share-network-steps.md "cloudwan-share-network-steps.md")
* [Stop sharing a core network](cloudwan-share-network-stop.md "cloudwan-share-network-stop.md")
