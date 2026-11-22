

# Context sharing with security services

Context sharing with security services lets you use Amazon Virtual Private Clouds (VPCs), subnets, security groups, and transit gateway attachments alongside IP addresses in policies enforced by security services such as firewalls. AWS Transit Gateway adds this resource context to traffic sent to the security service, which resolves the context and enforces your policies.

## How context sharing with security services works
<a name="context-stores-how-it-works"></a>

After you create a context store, associate one or more transit gateways with it. The context store monitors context for resources connected to associated transit gateways and shares that context with security services. Resource context can include VPCs, subnets, security groups, and transit gateway attachments.

A security service reads the context store to resolve resource context in traffic and enforce policies alongside its existing rules that are based on IP addresses. For more information, see [Consume context from a context store](consume-context-store.md).

You can associate transit gateways in multiple Regions with one context store. Resource context includes the Region of each resource. Resource context is not shared across an inter-Region transit gateway peering attachment.

## Prerequisites
<a name="context-stores-prerequisites"></a>

Before you share context with security services, complete the following prerequisites:
+ Create a global network and register the transit gateways whose resource context you want to share. For more information, see [Global networks in AWS Global Networks for Transit Gateways](global-networks.md) and [Transit gateway registrations in AWS Global Networks for Transit Gateways](tgw-registrations.md).
+ Connect your firewall to the transit gateway through a network function attachment, and route traffic that requires inspection to the attachment. For more information, see [Transit gateway network function attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-nf-fw.html).
+ Ensure that you have permissions to create and manage context stores and their transit gateway associations in AWS Network Manager.

## Limitations
<a name="context-stores-limitations"></a>

Context sharing with security services has the following limitations:
+ A global network can have one context store.
+ A transit gateway can be associated with one context store.
+ Context sharing is available only for traffic routed through a transit gateway network function attachment of type AWS Network Firewall or Gateway Load Balancer.
+ Resource context includes up to five security groups. If a resource is associated with more than five security groups, its context does not include any security groups.
+ Resource context is not shared across inter-Region transit gateway peering attachments.
+ You can view context stores and their associations in the AWS Network Manager console. To view individual context records, use the Network Manager API or the AWS CLI. For more information, see [Consume context from a context store](consume-context-store.md).

**Topics**
+ [How context sharing with security services works](#context-stores-how-it-works)
+ [Prerequisites](#context-stores-prerequisites)
+ [Limitations](#context-stores-limitations)
+ [Create a context store](create-context-store.md)
+ [Manage context store associations](context-store-associations.md)
+ [View, update, and delete](manage-context-store.md)
+ [Consume context from a context store](consume-context-store.md)