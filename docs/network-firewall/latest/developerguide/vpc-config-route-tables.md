

# VPC route table configuration for AWS Network Firewall

After you create your firewall, you reroute your VPC network traffic through the firewall endpoints so they can start filtering traffic. Perform the following steps:

**Note**  
For a NAT/Proxy firewall, clients that use the explicit proxy don't need route table changes. You configure their proxy settings instead. Route only the traffic that doesn't use the explicit proxy to the firewall endpoint in the same Availability Zone. For information about configuring workloads to use the proxy, see [Configuring workloads to use the proxy](nfw-proxy-client-config.md).

1. Review the route table configurations in your VPC Availability Zones for the subnets that you want to protect and for any location that sends traffic to the subnets or receives traffic from them.

1. Determine which traffic you want the firewall to filter and insert your firewall endpoints into the traffic flow. Network Firewall supports up to 100 Gbps of network traffic per Availability Zone. The 100 Gbps bandwidth is shared across all associated VPC endpoints. Update the route tables for both directions of traffic flow, if you want to filter incoming and outgoing traffic.

For example, suppose you wanted to filter traffic that's currently routed between a customer subnet and an internet gateway. You would update your route table configuration as follows to insert a firewall endpoint into the traffic flow: 

1. Change the customer subnet route table so that it directs internet-bound traffic to the firewall endpoint.

1. Change the internet gateway route table so that it directs traffic that's bound for the customer subnet to the firewall endpoint.

1. Create a route table for the firewall endpoint so that it directs internet-bound traffic to the internet gateway and directs traffic that's bound for any destination inside the VPC to the destination specification `local`. 

In this way, the firewall endpoint sits between the customer subnet and the internet gateway and can filter all incoming and outgoing traffic for the customer subnet.

For an overview of common Network Firewall architectures, with example route table configurations, see [Architecture and routing examples](architectures.md). 

For information about managing route tables for your VPC, see [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the *Amazon Virtual Private Cloud User Guide*.