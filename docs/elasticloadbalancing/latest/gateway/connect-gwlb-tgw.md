

# Connect your Gateway Load Balancer to a transit gateway

A network function attachment of type Gateway Load Balancer connects a transit gateway to your Gateway Load Balancer VPC endpoint service. Transit Gateway creates one Gateway Load Balancer endpoint in each Availability Zone you select.

## Prerequisites
<a name="connect-gwlb-tgw-prerequisites"></a>

Before you begin, create a Gateway Load Balancer with healthy firewall targets and a VPC endpoint service that fronts the firewall deployment. For more information, see [Create a load balancer](create-load-balancer.md) and [Create an inspection system as a Gateway Load Balancer endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/create-gateway-load-balancer-endpoint-service.html) in the *AWS PrivateLink Guide*.

If the endpoint service and transit gateway are in different AWS accounts, allow the transit gateway owner's account to connect. For more information, see [Manage permissions](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#add-remove-permissions) in the *AWS PrivateLink Guide*.

Encryption Support must be disabled on the transit gateway. For more information, see [Transit gateway encryption support](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-encryption-support.html) in the *AWS Transit Gateway User Guide*.

## Create the network function attachment
<a name="connect-gwlb-tgw-create"></a>

The transit gateway owner creates the network function attachment and selects the endpoint service and Availability Zones. Each Availability Zone must be supported by both the transit gateway and endpoint service. For instructions, see [Create, modify, and delete a network function attachment of type Gateway Load Balancer](https://docs.aws.amazon.com/vpc/latest/tgw/manage-nf-attachment-gwlb.html) in the *AWS Transit Gateway User Guide*.

## Accept the endpoint connection
<a name="connect-gwlb-tgw-accept"></a>

If the endpoint service requires acceptance, the endpoint service owner must accept the endpoint connection before the attachment becomes active. No action is required when automatic acceptance is enabled. For instructions, see [Accept or reject connection requests](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#accept-reject-connection-requests) in the *AWS PrivateLink Guide*.

## Next steps
<a name="connect-gwlb-tgw-next-steps"></a>

After the attachment becomes available, update the transit gateway route tables to send traffic to it. For more information, see [Route traffic through an AWS Transit Gateway network function attachment](https://docs.aws.amazon.com/vpc/latest/tgw/route-traffic-nf-attachment.html) in the *AWS Transit Gateway User Guide*.

To share AWS resource context with the firewall, configure context sharing with security services. For more information, see [Context sharing with security services](https://docs.aws.amazon.com/network-manager/latest/tgwnm/context-stores.html).