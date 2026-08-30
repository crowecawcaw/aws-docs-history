# Accessing Amazon VPC Endpoints from On-Premises Environments

Publication date: **March 25, 2022 ([Diagram history](#onprem-diagram-history "#onprem-diagram-history"))**

This architecture uses [AWS Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md") to access interface Amazon VPC endpoints from on-premises environments. It uses [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") or [AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") as transport between AWS and the corporate data center.

## Accessing Amazon VPC endpoints from on-premises architecture

![Architecture diagram showing on-premises access to VPC endpoints through AWS Transit Gateway using AWS Direct Connect or AWS Site-to-Site VPN.](images/centralizing-vpc-endpoints-tgw-2.png)

The following steps describe the data flow in this architecture:

1. A client in the corporate data center sends the request through the customer gateway. It resolves the DNS name to obtain the private IP address of the VPC endpoint.
2. The traffic sends to AWS Transit Gateway through an AWS Direct Connect link or an AWS Site-to-Site VPN connection.
3. The **Transit Gateway on-premises route table** forwards the traffic to the **shared services VPC**.
4. The Transit Gateway ENI forwards the traffic to the VPC endpoint.

The return path follows these steps:

1. The VPC endpoint sends the response back to the Transit Gateway ENI.
2. The traffic forwards to AWS Transit Gateway.
3. The **Transit Gateway shared services route table** sends the traffic to the corporate data center through the Direct Connect link or Site-to-Site VPN connection.
4. The response arrives at the on-premises client.

For more information about centralizing AWS PrivateLink endpoints with AWS Transit Gateway, see the [Integrating AWS Transit Gateway with AWS PrivateLink and Amazon Route 53 Resolver](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-aws-transit-gateway-with-aws-privatelink-and-amazon-route-53-resolver/ "https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-aws-transit-gateway-with-aws-privatelink-and-amazon-route-53-resolver/") blog post.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change                                                                                                                                     | Description                                     | Date           |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- | -------------- |
| [Initial publication](centralizing-vpc-endpoint-access.md#cvpc-diagram-history "centralizing-vpc-endpoint-access.md#cvpc-diagram-history") | Reference architecture diagram first published. | March 25, 2022 |
| Initial publication                                                                                                                        | Reference architecture diagram first published. | March 25, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
