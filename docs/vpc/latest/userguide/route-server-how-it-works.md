# How Amazon VPC Route Server works

This section explains how Amazon VPC Route Server works and helps you understand how
it achieves routing fault tolerance for your workloads running in subnets.

###### Contents

- [Overview](#route-server-overview "#route-server-overview")
- [Diagrams](#route-server-diagrams "#route-server-diagrams")

## Overview

How Amazon VPC Route Server works:

1. You configure a network device (like a firewall running on an EC2 instance in the VPC) to use
   Amazon VPC Route Server.
2. The network device fails.
3. The route server endpoints detect the failure through [BFD
   (Bidirectional Forwarding Detection)](https://en.wikipedia.org/wiki/Bidirectional_Forwarding_Detection "https://en.wikipedia.org/wiki/Bidirectional_Forwarding_Detection") configured on the route server
   peer.
4. The route server endpoints update the route server to withdraw routes in a [Routing Information Base
   (RIB)](https://en.wikipedia.org/wiki/Routing_table "https://en.wikipedia.org/wiki/Routing_table") where the failed device is the next hop.
5. The route server computes a [Forwarding
   Information Base (FIB)](https://en.wikipedia.org/wiki/Forwarding_information_base "https://en.wikipedia.org/wiki/Forwarding_information_base") from the RIB, selecting the best available
   routes.
6. Route server updates the configured route tables with the routes from the FIB.
7. All new traffic is forwarded to the standby device.

## Diagrams

The following is an example diagram of VPC route server with route server endpoints configured for devices in two subnets.

![Basic Amazon VPC Route Server setup](images/route-server-main.png)

Starting with the example above as a baseline, the example below shows a more detailed
design, where both Device A and Device B advertise over BGP that they can accept any
traffic with a destination IP in the range of 192.0.0.0/24 (from 192.0.0.0 to
192.0.0.255). The MED (Multi-Exit Discriminator) attribute of 0 tells route server
that Device A should be preferred over Device B. The route server receives the route
and the MED attribute from Device A and installs that route in the subnet route
tables with the network interface of Device A as the "next hop". As a result, any
traffic within the subnet with a destination IP in the 192.0.0.0/24 range is sent to
Device A. Device A then processes the traffic and sends it onward. Traffic within
either subnet (10.0.0.0/24 or 10.0.1.0/24) that is bound for 192.0.0.0/24 will be
routed to Device A eni-abcd (10.0.0.1) as the next hop.

![Amazon VPC Route Server setup before device A failure](images/route-server-failover-part-1.png)

This last example below shows how route server handles failover. While the higher MED attribute tells route server that Device B is less preferred than Device A, if Device A eni-abcd (10.0.0.1) goes down, route server updates the subnet route tables, and traffic to 192.0.0.0/24 is routed to Device B eni-efgh (10.0.1.1) as the next hop.

![Amazon VPC Route Server failover to device B](images/route-server-failover-part-2.png)
