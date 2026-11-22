

# NAT/Proxy firewall in AWS Network Firewall

When you create a firewall in AWS Network Firewall, you choose its *firewall capability*:
+ **Routed firewall** – The firewall filters traffic that your VPC route tables send to the firewall endpoints, and preserves the client source IP address. You route outbound traffic through your own NAT gateway or internet gateway. For information about creating a routed firewall, see [Getting started with AWS Network Firewall](getting-started.md).
+ **NAT/Proxy firewall** – Network Firewall creates a NAT gateway and a firewall endpoint in each Availability Zone that you add. The firewall filters traffic and sends it out through the NAT gateways, which replace the client source IP address with their own. The firewall also acts as an explicit forward proxy that your clients send HTTP and HTTPS requests to directly. Other traffic reaches the firewall endpoint through your VPC route tables.

This chapter describes the NAT/Proxy firewall capability.

NAT/Proxy firewall is available in the AWS Regions where it's listed in the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

**Topics**
+ [Key concepts for a NAT/Proxy firewall](nfw-proxy-concepts.md)
+ [How a NAT/Proxy firewall works](nfw-proxy-how-it-works.md)
+ [Requirements and considerations for a NAT/Proxy firewall](nfw-proxy-considerations.md)
+ [NAT gateways that Network Firewall creates for a NAT/Proxy firewall](nfw-proxy-nat-gateways.md)
+ [Using a custom proxy hostname and certificate](nfw-proxy-custom-hostname.md)
+ [Configuring workloads to use the proxy](nfw-proxy-client-config.md)
+ [Managing a NAT/Proxy firewall](nfw-proxy-managing.md)
+ [Permissions for a NAT/Proxy firewall](nfw-proxy-permissions.md)