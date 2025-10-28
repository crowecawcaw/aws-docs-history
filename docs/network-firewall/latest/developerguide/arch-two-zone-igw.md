# Multi zone architecture with an internet gateway using AWS Network Firewall

This topic provides a high-level view of a simple two zone VPC configuration using an
internet gateway and AWS Network Firewall. It describes the basic route table
modifications that are required to use the Network Firewall firewall.

###### Two zone architecture with internet gateway and the Network Firewall

firewall

The following figure depicts a Network Firewall configuration for a VPC that
spans multiple Availability Zones. In this case, each Availability Zone that the
VPC spans has a firewall subnet and a customer subnet. The VPC has an internet
gateway for internet access. All incoming traffic for the VPC routes to the
firewall in the same Availability Zone as the destination customer subnet. All
outgoing traffic routes through the firewalls.

![An AWS Region is shown with a two Availability Zones. The Region also has an internet gateway, which has arrows out to and in from an internet cloud. Inside the Region, spanning parts of each Availability Zone, is a VPC. Inside the VPC, each Availability Zone holds a firewall subnet and a customer subnet. In each zone, one arrow shows traffic going between the customer subnet and the firewall subnet. Each firewall subnet has an arrow between it and the single internet gateway.](images/arch-igw-2az-simple.png)

###### Route tables in the two zone architecture with the firewall

The following figure depicts a VPC configuration with two Availability Zones.
Each zone has its own Network Firewall firewall, which provides
monitoring and protection for the subnets in the zone. You can expand this
configuration to any number of zones in your VPC.

![An AWS Region is shown with two Availability Zones. The Region has an internet gateway, which has arrows leading out to and in from an internet cloud. Inside the Region, and spanning the two Availability Zones, is a VPC. In each Availability Zone, the VPC has a firewall subnet and a customer subnet. The VPC address range is 10.0.0.0/8. The address ranges for the customer subnets are 10.0.0.0/16 and 10.1.0.0/16. The route tables are listed for the internet gateway and for each of the four subnets. The route table for the internet gateway directs incoming traffic for the two customer subnets to their relative firewall subnets. For each customer subnet, the route table directs traffic inside the VPC to local, and directs all other traffic to its relative firewall subnet. For each firewall subnet, the route table directs traffic inside the VPC to local, and directs all other traffic to the internet gateway.](images/arch-igw-2az-with-route-tables.png)
In the preceding figure, the route tables enforce similar traffic flows to the single
Availability Zone model, with the primary difference being the splitting of incoming
traffic by the internet gateway, to accommodate the two different customer subnets:

- **Internet gateway route table** –
  Routes traffic that's destined for each customer subnet (range
  `10.0.2.0/24` or `10.0.3.0/24`) to the firewall
  subnet in the same Availability Zone (`vpce-4114` or `vpce-5588`,
  respectively).
- **Firewall subnet route tables** –
  Route traffic that's destined for anywhere inside the VPC
  (`10.0.0.0/16`) to the local address. Route traffic that's
  destined for anywhere else (`0.0.0.0/0`) to the internet gateway
  (`igw-1232`). These are identical to the route table for the
  firewall subnet in the single Availability Zone.
- **Customer subnet route tables** –
  Route traffic that's destined for anywhere inside the VPC
  (`10.0.0.0/16`) to the local address. Route traffic that's
  destined for anywhere else (`0.0.0.0/0`) to the firewall subnet
  in the same Availability Zone (`vpce-4114` for zone AZ1 and `vpce-5588` for
  zone AZ2).
