# Terminology

The following terms are used in this guide:

- **FIB**: The [Forwarding Information Base (FIB)](https://en.wikipedia.org/wiki/Forwarding_information_base "https://en.wikipedia.org/wiki/Forwarding_information_base") serves as a forwarding table for what route server has determined are the best-path routes in the RIB after evaluating all available routing information and policies. The FIB routes that are installed on the route tables. The FIB is recomputed whenever there are changes to the RIB.
- **RIB**: The [Routing Information Base (RIB)](https://en.wikipedia.org/wiki/Routing_table "https://en.wikipedia.org/wiki/Routing_table") serves as a database that stores all the routing information and network topology data collected by a router or routing system, such as routes learned from BGP peers. The RIB is constantly updated as new routing information is received or existing routes change. This ensures that the route server always has the most current view of the network topology and can make optimal routing decisions.
- **Route server**: The route server component updates your VPC and internet gateway route tables with the IPv4 or IPv6 routes in your Forwarding Information Base (FIB). The route server represents a single FIB and Routing Information Base (RIB).
- **Route server association**: A route server association is the connection established between a route server and a VPC.
- **Route server endpoint**:
  A route server endpoint is an AWS-managed component inside a subnet that facilitates [BGP (Border Gateway Protocol)](https://en.wikipedia.org/wiki/Border_Gateway_Protocol "https://en.wikipedia.org/wiki/Border_Gateway_Protocol") connections between your route server and your BGP peers.
- **Route server peer**:
  A route server peer is a session between a route server endpoint and the device deployed in AWS (such as a firewall appliance or other network security function running on an EC2 instance). The device must meet these requirements:
  - Have an elastic network interface in the VPC
  - Support BGP (Border Gateway Protocol)
  - Can initiate BGP sessions

- **Route server propagation**:
  When enabled, route server propagation installs the routes in the FIB on the route table you've specified. Route server supports IPv4 and IPv6 route propagation.
