# Use an interface endpoint to Access AWS Batch

You can use AWS PrivateLink to create a private connection between your VPC and AWS Batch. You can access
AWS Batch as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect
connection. Instances in your VPC don't need public IP addresses to access AWS Batch.

You establish this private connection by creating an _interface endpoint_, powered by
AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint.
These are requester-managed network interfaces that serve as the entry point for traffic destined for
AWS Batch.

For more information, see [Interface VPC endpoints](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md")
in the _AWS PrivateLink Guide_.
