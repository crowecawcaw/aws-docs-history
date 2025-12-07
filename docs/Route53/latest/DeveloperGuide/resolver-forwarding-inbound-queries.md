# Forwarding inbound DNS queries to your VPCs

To forward DNS queries from your network to VPC Resolver, you create an inbound endpoint. An inbound endpoint specifies the IP addresses
(from the range of IP addresses available to your VPC) that you want DNS resolvers on your network to forward DNS queries to.
Those IP addresses aren't public IP addresses, so for each inbound endpoint, you need to connect your VPC to your network
using either an Direct Connect connection or a VPN connection.

When implementing inbound delegation, you're delegating DNS authority for a subdomain from your on-premises DNS
infrastructure to VPC Resolver. To properly configure this delegation, you must use the inbound endpoint's IP addresses
as glue records (NS records) on your on-premises name server for the subdomain being delegated.
For example, if you're delegating the subdomain "aws.example.com" to VPC Resolver through an inbound delegation endpoint
with IP addresses 10.0.1.100 and 10.0.1.101, you would create NS records on your on-premises DNS server pointing
"aws.example.com" to these IP addresses. This makes sure that DNS queries for the delegated subdomain are properly
routed to the VPC Resolver via the inbound endpoint, allowing the VPC Resolver to respond with records from the associated private hosted zone.
