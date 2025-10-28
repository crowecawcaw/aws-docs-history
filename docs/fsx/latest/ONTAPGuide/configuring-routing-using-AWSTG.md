# Configure routing to access Multi-AZ file systems from outside your VPC

If you have a Multi-AZ file system with an `EndpointIPv4AddressRange` or `EndpointIPv6AddressRange`
that's outside your VPC's IP address range, you need to set up additional routing
in your AWS Transit Gateway to access your file system from peered or on-premises networks.

###### Important

To access a Multi-AZ file system using a Transit Gateway, each of the Transit Gateway's attachments
must be created in a subnet whose route table is associated with your file system.

###### Note

No additional Transit Gateway configuration is required for Single-AZ file systems
or Multi-AZ file systems with an endpoint IP address range that's within
your VPC's IP address range.

###### To configure routing using AWS Transit Gateway

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Choose the FSx for ONTAP file system for which you are configuring
   access from a peered network.
3. In **Network & security** copy the
   endpoint IP address range.
4. Add a route to Transit Gateway that routes traffic destined for this IP
   address range to your file system's VPC. For more information, see
   [Work
   with transit gateways](../../../vpc/latest/tgw/working-with-transit-gateways.md "../../../vpc/latest/tgw/working-with-transit-gateways.md") in the
   _Amazon VPC Transit Gateways_.
5. Confirm that you can access your FSx for ONTAP file system from the
   peered network.
   To add the route table to your file system, see [Updating file systems](updating-file-system.md "updating-file-system.md").

###### Note

DNS records for the management, NFS, and SMB endpoints are only
resolvable from within the same VPC as the file system. In order to
mount a volume or connect to a management port from another network, you
need to use the endpoint's IP address. These IP addresses do not change
over time.
