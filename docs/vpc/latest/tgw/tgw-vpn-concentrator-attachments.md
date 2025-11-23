# VPN Concentrator attachments in AWS Transit Gateway

AWS Site-to-Site VPN Concentrator is a new feature that simplifies multi-site connectivity for distributed enterprises. VPN Concentrator is suitable for customers who need to connect 25+ remote sites to AWS, with each site needing low bandwidth (under 100 Mbps).

## How VPN Concentrator works

A VPN Concentrator appears as a single attachment on your transit gateway, but can host multiple Site-to-Site VPN connections.

Traffic from all VPN connections on the Concentrator is routed through the same transit gateway attachment, allowing you to apply consistent routing policies and security rules across all connected sites. The Concentrator integrates seamlessly with transit gateway route tables, enabling you to control traffic flow between your remote sites and other attachments such as VPCs, other VPN connections, and peering connections.

## Benefits of VPN Concentrator

- **Cost optimization**: Reduce costs by consolidating multiple low-bandwidth VPN connections onto a single transit gateway attachment, especially beneficial when individual sites don't require full VPN attachment capacity.
- **Simplified management**: Manage multiple remote site connections through a unified attachment while maintaining individual VPN connection control and monitoring.
- **Consistent routing**: Apply unified routing policies across all connected sites through a single transit gateway route table association.
- **Scalable architecture**: Connect up to 100 remote sites using a single Concentrator, with support for up to 5 Concentrators per transit gateway.
- **Standard VPN features**: Each VPN connection supports the same security, monitoring, and routing capabilities as standard Site-to-Site VPN connections.

**Requirements and limitations**

- **BGP routing only**: VPN Concentrator supports BGP (dynamic) routing only. Static routing is not supported at launch.
- **Customer gateway requirements**: Each remote site requires a customer gateway that supports BGP routing. Before creating VPN connections on a Concentrator, review the customer gateway requirements in [Requirements for your Site-to-Site VPN customer gateway device](../../../vpn/latest/s2svpn/CGRequirements.md "../../../vpn/latest/s2svpn/CGRequirements.md") in the _AWS Site-to-Site VPN User Guide_.
- **Performance considerations**: Each VPN connection on a Concentrator is designed for a maximum of 100 Mbps bandwidth. For higher bandwidth requirements, consider using standard transit gateway VPN attachments.
  You can create, view, or delete a VPN Concentrator attachment using either the AWS VPC console or the AWS CLI. Individual VPN connections on the Concentrator are managed through the standard VPN connection APIs and console interfaces.

###### Tasks

- [Create a VPN Concentrator attachment](create-vpn-concentrator-attachment.md "create-vpn-concentrator-attachment.md")
- [View a VPN Concentrator attachment](view-vpn-concentrator-attachment.md "view-vpn-concentrator-attachment.md")
- [Delete a VPN Concentrator attachment](delete-vpn-concentrator-attachment.md "delete-vpn-concentrator-attachment.md")
