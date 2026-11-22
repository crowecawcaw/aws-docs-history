

# AWS Transit Gateway network function attachments

AWS Transit Gateway supports network function attachments for AWS Network Firewall and Gateway Load Balancer. How you create and manage the attachment depends on its type.

Network function attachment of type AWS Network Firewall  
You can create a network function attachment to connect your transit gateway directly to AWS Network Firewall. This eliminates the need to create and manage inspection VPCs.  
With a firewall attachment, AWS automatically provisions and manages all the necessary resources behind the scenes. You'll see a new transit gateway attachment rather than individual firewall endpoints. This simplifies the process of implementing centralized network traffic inspection.  
Before you can use a firewall attachment, you must first create the attachment in AWS Network Firewall. For instructions on creating the attachment, see [Getting started with AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/getting-started.html) in the *AWS Network Firewall Developer Guide*. After the firewall is created, you can view the attachment in Amazon VPC Console under **Transit gateway attachments**. The attachment is listed with a type of **Network function**.

Network function attachment of type Gateway Load Balancer  
Create and manage this attachment in Transit Gateway. Specify the Gateway Load Balancer VPC endpoint service that fronts the firewall deployment. Use this attachment type for firewall appliances that you deploy or for a firewall-as-a-service (FWaaS) offering. Transit Gateway creates one Gateway Load Balancer endpoint in each Availability Zone you select. For instructions, see [Manage a network function attachment of type Gateway Load Balancer](manage-nf-attachment-gwlb.md).

Network function attachments support transit gateway route table associations and static routes. A network function attachment does not support route propagation.

Both network function attachment types support context sharing with security services. For more information, see [Context sharing with security services](https://docs.aws.amazon.com/network-manager/latest/tgwnm/context-stores.html).

**Topics**
+ [Manage a network function attachment of type Gateway Load Balancer](manage-nf-attachment-gwlb.md)
+ [Accept or reject a transit gateway network function attachment](accept-reject-firewall-attachment.md)
+ [View network function attachments](view-nf-attachment-nm.md)
+ [Route traffic through a transit gateway network function attachment](route-traffic-nf-attachment.md)