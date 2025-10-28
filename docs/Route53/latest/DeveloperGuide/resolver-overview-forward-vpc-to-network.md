# How Route 53 Resolver endpoint forwards DNS

queries from your VPCs to your network

When you want to forward DNS queries from the EC2 instances in one or more VPCs in an AWS Region to your network, you perform
the following steps.

1.  You create a Route 53 Resolver outbound endpoint in a VPC, and you specify several values:

        * The VPC that you want DNS queries to pass through on the way to the resolvers on your network.
        * A [VPC security group](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") that includes
         outbound rules allowing TCP and UDP access on port 53 (or the port
         you're using for DNS queries on your network)

    For each IP address that you specify for the outbound endpoint, Resolver creates an Amazon VPC elastic network interface
    in the VPC that you specify. For more information, see
    [Considerations when creating inbound and outbound endpoints](resolver-choose-vpc.md "resolver-choose-vpc.md").

2.  You create one or more rules, which specify the domain names of the DNS queries that you want
    to delegate to Resolver to forward, or want Resolver to forward to resolvers on
    your network. For forwarding rules, you also specify the IP addresses of the
    resolvers. For more information, see [Using rules to control which queries are forwarded
    to your network](resolver-overview-forward-vpc-to-network-using-rules.md "resolver-overview-forward-vpc-to-network-using-rules.md").
3.  You associate each rule with the VPCs for which you want to forward DNS queries to your network.
