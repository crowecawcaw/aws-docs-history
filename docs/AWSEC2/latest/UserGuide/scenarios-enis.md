# Multiple network interfaces for your Amazon EC2 instances

Attaching multiple network interfaces to an instance is useful when you need the following:

- A [management network](#creating-a-management-network "#creating-a-management-network").
- [Network and security appliances](#use-network-and-security-appliances-in-your-vpc "#use-network-and-security-appliances-in-your-vpc").
- Dual-homed instances with workloads in different
  [subnets](#creating-dual-homed-instances-with-workloads-roles-on-distinct-subnets "#creating-dual-homed-instances-with-workloads-roles-on-distinct-subnets")
  or [VPCs](#creating-dual-homed-instances-with-workloads-roles-on-distinct-subnets "#creating-dual-homed-instances-with-workloads-roles-on-distinct-subnets").
- A [low-budget, high-availability](#create-a-low-budget-high-availability-solution "#create-a-low-budget-high-availability-solution") solution.

## Management network

The following overview describes a management network created using multiple network interfaces.

###### Criteria

- The primary network interface on the instance (for example, eth0) handles
  public traffic.
- The secondary network interface on the instance (for example, eth1)
  handles backend management traffic. It's connected to a separate subnet that
  has more restrictive access controls, and is located within the same
  Availability Zone as the primary network interface.

###### Settings

- The primary network interface, which may or may not be behind a load balancer,
  has an associated security group that allows access to the server from the internet.
  For example, allow TCP port 80 and 443 from 0.0.0.0/0 or from the load
  balancer.
- The secondary network interface has an associated security group that allows
  SSH access only, initiated from one of the following locations:
  - An allowed range of IP addresses, either within the VPC, or from the
    internet.
  - A private subnet within the same Availability Zone as the primary network
    interface.
  - A virtual private gateway.

###### Note

To ensure failover capabilities, consider using a secondary private IPv4 for incoming
traffic on a network interface. In the event of an instance failure, you can move
the interface and/or secondary private IPv4 address to a standby instance.

![Creating a management network](images/EC2_ENI_management_network.png)

## Network and security appliances

Some network and security appliances, such as load balancers, network address translation
(NAT) servers, and proxy servers prefer to be configured with multiple network
interfaces. You can create and attach secondary network interfaces to instances
that are running these types of applications and configure the additional
interfaces with their own public and private IP addresses, security groups, and
source/destination checking.

## Dual-homed instances with workloads in different subnets

You can place a network interface on each of your web servers that connects to a mid-tier
network where an application server resides. The application server can also be
dual-homed to a backend network (subnet) where the database server resides. Instead
of routing network packets through the dual-homed instances, each dual-homed
instance receives and processes requests on the front end, initiates a connection to
the backend, and then sends requests to the servers on the backend network.

## Dual-homed instances with workloads in different VPCs in the same account

You can launch an EC2 instance in one VPC and attach a secondary ENI from a different VPC,
as long as the network interface is in the same Availability Zone as the instance.
This enables you to create multi-homed instances across VPCs with different
networking and security configurations. You can't create multi-homed instances
across VPCs in different AWS accounts.

You can use dual-homed instances across VPCs in the following use cases:

- **Overcome CIDR overlaps between two VPCs that can’t be peered
  together**: You can leverage a secondary CIDR in a VPC and
  allow an instance to communicate across two non-overlapping IP ranges.
- **Connect multiple VPCs within a single account**: Enable
  communication between individual resources that would normally be separated
  by VPC boundaries.

## Low-budget, high-availability solution

If one of your instances serving a particular function fails, its network interface can be
attached to a replacement or hot standby instance pre-configured for the same role
in order to rapidly recover the service. For example, you can use a network
interface as your primary or secondary network interface to a critical service such
as a database instance or a NAT instance. If the instance fails, you (or more
likely, the code running on your behalf) can attach the network interface to a hot
standby instance. Because the interface maintains its private IP addresses, Elastic
IP addresses, and MAC address, network traffic begins flowing to the standby
instance as soon as you attach the network interface to the replacement instance.
Users experience a brief loss of connectivity between the time the instance fails
and the time that the network interface is attached to the standby instance, but no
changes to the route table or your DNS server are required.
