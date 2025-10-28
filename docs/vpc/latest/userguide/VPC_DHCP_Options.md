# DHCP option sets in Amazon VPC

Network devices in your VPC use Dynamic Host Configuration Protocol (DHCP). You can use DHCP
option sets to control the following aspects of the network configuration in your virtual network:

- The DNS servers, domain names, or Network Time Protocol (NTP) servers used by the devices in your VPC.
- Whether DNS resolution is enabled in your VPC.

###### Contents

- [What is DHCP?](#DHCPOptionSets "#DHCPOptionSets")
- [DHCP option set concepts](DHCPOptionSetConcepts.md "DHCPOptionSetConcepts.md")
- [Work with DHCP option sets](DHCPOptionSet.md "DHCPOptionSet.md")

## What is DHCP?

Every device on a TCP/IP network requires an IP address to communicate over the network.
In the past, IP addresses had to be assigned to each device in your network manually. Today,
IP addresses are assigned dynamically by DHCP servers using the Dynamic Host Configuration
Protocol (DHCP).

Applications running on EC2 instances can communicate with Amazon DHCP servers as needed
to retrieve their IP address lease or other network configuration information (such as the IP
address of an Amazon DNS server or the IP address of the router in your VPC).

You can specify the network configurations that are provided by Amazon DHCP servers by
using DHCP option sets.

If you have a VPC configuration that requires your applications to make direct requests
to the Amazon IPv6 DHCP server, note the following:

- An EC2 instance in a dual-stack subnet can only retrieve its IPv6 address from the IPv6 DHCP
  server. _It cannot retrieve any additional network
  configurations from the IPv6 DHCP server, such as DNS server names or domain
  names._
- An EC2 instance in a IPv6-only subnet can retrieve its IPv6 address from the IPv6 DHCP server
  _and can retrieve additional networking configuration
  information, such as DNS server names and domain names._
- For an EC2 instance in an IPv6-only subnet, the IPv4 DHCP Server will return 169.254.169.253
  as the name server if "AmazonProvidedDNS" is explicitly mentioned in the DHCP option set.
  If "AmazonProvidedDNS" is missing from the option set, the IPv4 DHCP Server won't return
  an address whether other IPv4 name servers are mentioned in the option set or not.

The Amazon DHCP servers can also provide an entire IPv4 or IPv6 prefix to a network
interface in your VPC using prefix delegation (see [Assigning prefixes to Amazon EC2 network
interfaces](../../../AWSEC2/latest/UserGuide/ec2-prefix-eni.md "../../../AWSEC2/latest/UserGuide/ec2-prefix-eni.md") in the _Amazon EC2 User Guide_). IPv4 prefix delegation is
not provided in DHCP responses. IPv4 prefixes assigned to the interface can be retrieved using
IMDS (see [Instance metadata
categories](../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md#instancedata-data-categories "../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md#instancedata-data-categories") in the _Amazon EC2 User Guide_).
