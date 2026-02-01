# Configuring DNS servers for Simple AD

You can configure DNS for Simple AD in two ways depending on your network architecture and requirements.

## Using Simple AD as Your Primary DNS

Configure your client computers to use the Simple AD DNS server IP addresses as their primary DNS resolvers. Simple AD forwards DNS requests to the IP address of the Amazon-provided DNS servers for
your Amazon VPC. These DNS servers will resolve names configured in your Amazon Route 53 private hosted
zones. By pointing your on-premises computers to your Simple AD, you can now resolve DNS
requests to the private hosted zone. For more information on Route 53, see [What is Route 53](../../../Route53/latest/DeveloperGuide/Welcome.md "../../../Route53/latest/DeveloperGuide/Welcome.md").

During Simple AD creation, the service performs a reachability test to amazon.com to determine which DNS resolver to use:

- **Customer VPC DNS Resolver (ETH1)** – Selected when amazon.com is reachable from customer VPC resolver. This option enables Route 53 private hosted zones and Resolver firewall rules.
- **Amazon Internal Resolver (ETH0)** – Selected when amazon.com is unreachable from customer VPC DNS Resolver (ETH1). Route 53 integration, private hosted zones, and Resolver firewall rules will not function with this option.

###### Important

The DNS resolver selection occurs automatically during Simple AD creation and cannot be modified afterward. We recommend that you ensure amazon.com is resolvable in your VPC before creating Simple AD to enable Route 53 integration.

## Using Route 53 as Your Primary DNS

You can also use Route 53 as your primary DNS service:

- Configure your client computers to use Route 53 Resolver IP addresses as their primary DNS resolvers
- Create Route 53 Resolver rules to conditionally forward only your domain's fully qualified domain name (FQDN) queries to Simple AD
- This approach maintains Route 53 as the authoritative DNS source, with Simple AD handling only domain-specific queries

Note that to enable your Simple AD to respond to external DNS queries, the network
access control list (ACL) for the VPC containing your Simple AD must be configured to
allow traffic from outside the VPC.

- If you are not using Route 53 private hosted zones, your DNS requests will be
  forwarded to public DNS servers.
- If you're using custom DNS servers that are outside of your VPC and you want to
  use private DNS, you must reconfigure to use custom DNS servers on EC2 instances
  within your VPC. For more information, see [Working with private hosted
  zones](../../../Route53/latest/DeveloperGuide/hosted-zones-private.md "../../../Route53/latest/DeveloperGuide/hosted-zones-private.md").
- If you want your Simple AD to resolve names using both DNS servers within your
  VPC and private DNS servers outside of your VPC, you can do this using a DHCP
  options set. For a detailed example, see [this article](https://aws.amazon.com/blogs/security/how-to-set-up-dns-resolution-between-on-premises-networks-and-aws-using-aws-directory-service-and-amazon-route-53/ "https://aws.amazon.com/blogs/security/how-to-set-up-dns-resolution-between-on-premises-networks-and-aws-using-aws-directory-service-and-amazon-route-53/").
- [Integrating your Directory Service's DNS resolution with Amazon Route 53 Resolver](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/ "https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/").

###### Note

DNS dynamic updates are not supported in Simple AD domains. You can instead make the
changes directly by connecting to your directory using DNS Manager on an instance that
is joined to your domain.
