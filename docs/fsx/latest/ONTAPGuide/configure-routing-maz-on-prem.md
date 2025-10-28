# Configure routing to access Multi-AZ file systems from on-premises

###### To configure AWS Transit Gateway for access to Multi-AZ file systems from on-premises

If you have a Multi-AZ file system with an `EndpointIPv4AddressRange` or `EndpointIPv6AddressRange`
that's outside your VPC's CIDR range, you need to set up additional routing
in your AWS Transit Gateway to access your file system from peered or on-premises networks.

###### Note

No additional Transit Gateway configuration is required for Single-AZ file systems
or Multi-AZ file systems with an endpoint IP address range that's within
your VPC's IP address range.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Choose the FSx for ONTAP file system for which you are configuring access
   from a peered network.
3. In **Network & security** copy the
   **Endpoint IPv4 or IPv6 address range**.
4. Add a route to the Transit Gateway that routes traffic destined for this IP
   address range to your file system's VPC. For more information, see
   [Work with transit gateways](../../../vpc/latest/tgw/working-with-transit-gateways.md "../../../vpc/latest/tgw/working-with-transit-gateways.md") in the _Amazon VPC Transit Gateway User Guide_.
5. Confirm that you can access your FSx for ONTAP file system from the
   peered network.

###### Important

To access a Multi-AZ file system using a Transit Gateway, each of the Transit Gateway's attachments
must be created in a subnet whose route table is associated with your file system. Where
you have separate Transit Gateway attachment subnets, you must also associate the route tables
for those subnets with Amazon FSx so that they are updated with the Amazon FSx endpoint addresses.

To add a route table to your file system, see [Updating file systems](updating-file-system.md "updating-file-system.md").
