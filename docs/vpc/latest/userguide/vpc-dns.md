# DNS attributes for your VPC

Domain Name System (DNS) is a standard by which names used on the internet are resolved to
their corresponding IP addresses. A DNS hostname is a name that uniquely and absolutely names a
computer; it's composed of a host name and a domain name. DNS servers resolve DNS hostnames to
their corresponding IP addresses.

Public IPv4 addresses enable communication over the internet, while private IPv4 addresses
enable communication within the network of the instance. For more information, see [IP addressing for your VPCs and subnets](vpc-ip-addressing.md "vpc-ip-addressing.md").

Amazon provides a DNS server ([the Amazon Route 53 Resolver](AmazonDNS-concepts.md#AmazonDNS "AmazonDNS-concepts.md#AmazonDNS")) for
your VPC. To use your own DNS server instead, create a new set of DHCP options for your VPC. For
more information, see [DHCP option sets in Amazon VPC](VPC_DHCP_Options.md "VPC_DHCP_Options.md").

###### Contents

- [Understanding Amazon DNS](AmazonDNS-concepts.md "AmazonDNS-concepts.md")
- [View DNS hostnames for your EC2 instance](vpc-dns-viewing.md "vpc-dns-viewing.md")
- [View and update DNS attributes for your VPC](vpc-dns-updating.md "vpc-dns-updating.md")
