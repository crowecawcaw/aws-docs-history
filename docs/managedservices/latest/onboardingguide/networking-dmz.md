# Perimeter (DMZ) VPC

The Perimeter, or DMZ, VPC contains the necessary resources for AMS Operations engineers to
access AMS networks. It contains public subnets across 2-3 AZs, with SSH Bastions hosts in an
Auto Scaling group (ASG) for AMS Operations engineers to log into or tunnel through. The
security groups attached to the DMZ bastions contain port 22 inbound rules from
**Amazon Corp Networks**.

*DMZ VPC CIDR range:* When you create a VPC, you must specify a
range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing
(CIDR) block; for example, 10.0.16.0/24. This is the primary CIDR block for your VPC.

###### Note

The AMS team recommends the range of 24 (with more IP address) to
provide some buffer in case other resources, such as a firewall, are
deployed in the future.
