# VPC route table configuration for AWS Network Firewall

After you create your firewall, you reroute your VPC network traffic through the
firewall endpoints so they can start filtering traffic. Perform the following
steps:

1. Review the route table configurations in your VPC Availability Zones for
   the subnets that you want to protect and for any location that sends traffic
   to the subnets or receives traffic from them.
2. Determine which traffic you want the firewall to filter and insert your
   firewall endpoints into the traffic flow. Network Firewall supports up to 100 Gbps of network traffic per firewall endpoint. Update the route tables for both
   directions of traffic flow, if you want to filter incoming and outgoing
   traffic.
   For example, suppose you wanted to filter traffic that's currently routed between
   a customer subnet and an internet gateway. You would update your route table
   configuration as follows to insert a firewall endpoint into the traffic flow:

3. Change the customer subnet route table so that it directs internet-bound
   traffic to the firewall endpoint.
4. Change the internet gateway route table so that it directs traffic that's
   bound for the customer subnet to the firewall endpoint.
5. Create a route table for the firewall endpoint so that it directs
   internet-bound traffic to the internet gateway and directs traffic that's
   bound for any destination inside the VPC to the destination specification
   `local`.
   In this way, the firewall endpoint sits between the customer subnet and the
   internet gateway and can filter all incoming and outgoing traffic for the customer
   subnet.

For an overview of common Network Firewall architectures, with example route table
configurations, see [Architecture and routing
examples](architectures.md "architectures.md").

For information about managing route tables for your VPC, see
[Route
tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") in the _Amazon Virtual Private Cloud User
Guide_.
