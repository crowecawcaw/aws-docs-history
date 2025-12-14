**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# List of resources that AWS Shield Advanced protects

This section provides information about Shield Advanced
protections for each resource type.

Shield Advanced protects AWS resources in the network and transport layers (layers 3 and 4) and in the
application layer (layer 7). You can protect some resources directly and others through
association with protected resources. Shield Advanced supports IPv4, and does not support IPv6.

###### Note

Shield Advanced protects only resources that you have specified either in Shield Advanced or through an
AWS Firewall Manager Shield Advanced policy. It doesn't automatically protect your resources.

You can use Shield Advanced for advanced monitoring and protection with the following resource
types:

- Amazon CloudFront distributions. For CloudFront continuous deployment, Shield Advanced protects any staging distribution that's associated with
  a protected primary distribution.
- Amazon Route 53 hosted zones.
- AWS Global Accelerator standard accelerators.
- Amazon EC2 Elastic IP addresses. Shield Advanced protects the resources that are associated with
  protected Elastic IP addresses.
- Amazon EC2 instances, through association to Amazon EC2 Elastic IP addresses.
- The following ELB (ELB) load balancers:
  - Application Load Balancers.
  - Classic Load Balancers.
  - Network Load Balancers, through associations to Amazon EC2 Elastic IP addresses.

###### Note

You can't use Shield Advanced to protect any other resource type. For example, you can't protect
AWS Global Accelerator custom routing accelerators or Gateway Load Balancers.

###### Note

NAT Gateways handle outbound traffic only, whereas Shield Advanced protects against inbound DDoS. For outbound traffic protection, use [AWS Network Firewall](../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md "../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md").

You can monitor and protect up to 1,000 resources for each resource type per AWS account.
For example, in a single account, you could protect 1,000 Amazon EC2 Elastic IP addresses, 1,000 CloudFront distributions, and 1,000 Application Load Balancers. You can request an increase to the number of resources that you can
protect with Shield Advanced through the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
