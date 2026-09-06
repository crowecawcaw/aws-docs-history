

# Connectivity through service link
<a name="service-links"></a>

The service link is a necessary connection between your Outposts and the AWS Region (or home Region). It allows for the management of the Outposts and the exchange of traffic to and from the AWS Region. The service link leverages an encrypted set of VPN connections to communicate with the home Region.

After the service link connection is established, your Outpost becomes operational and is managed by AWS. The service link facilitates the following traffic:
+ Customer VPC traffic between the Outpost and any associated VPCs.
+ Outposts management traffic, such as resource management, resource monitoring, and firmware and software updates.

## Service link maximum transmission unit (MTU) requirements
<a name="sl-max-mtu-requirements"></a>

The maximum transmission unit (MTU) of a network connection is the size, in bytes, of the largest permissible packet that can be passed over the connection.

Note the following:
+ The network **must** support 1500-bytes MTU between the Outpost and the service link endpoints in the parent AWS Region.
+ The traffic that goes from an instance in Outposts to an instance in the Region has an MTU of 1300 bytes, which is lower than the required MTU of 1500 bytes due to packet overheads.

## Service link bandwidth recommendations
<a name="sl-bandwidth-recommendations"></a><a name="region-bw-rec"></a>

For an optimal experience and resiliency, AWS requires that you use redundant connectivity of at least 500 Mbps for each compute rack and a maximum of 175 ms round trip latency for the service link connection to the AWS Region. You can use AWS Direct Connect or an internet connection for the service link. The minimum 500 Mbps and maximum round trip time requirements for the service link connection allows you to launch Amazon EC2 instances, attach Amazon EBS volumes, and access AWS services, such as Amazon EKS, Amazon EMR, and CloudWatch metrics with optimal performance.

Your Outposts service link bandwidth requirements vary depending on the following characteristics:
+ Number of AWS Outposts racks and capacity configurations
+ Workload characteristics, such as AMI size, application elasticity, burst speed needs, and Amazon VPC traffic to the Region 

We strongly recommend consulting with your AWS sales representative or APN partner to evaluate available home Region options in your geography and seek a custom recommendation about the service link bandwidth and latency requirements for your workloads. 

## Redundant internet connections
<a name="redundant-connections"></a>

When you build connectivity from your Outpost to the AWS Region, we recommend that you create multiple connections for higher availability and resiliency. For more information, see [Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/).

If you need connectivity to the public internet, you can use redundant internet connections and diverse internet providers, just as you would with your existing on-premises workloads.

## Set up your service link
<a name="sl-setup-steps"></a>

The following steps explain the service link setup process.

1. Choose a connection option between your Outposts and the home AWS Region. You can choose either a [public](https://docs.aws.amazon.com/outposts/latest/network-userguide/sl-public-connectivity.html) or [private](https://docs.aws.amazon.com/outposts/latest/network-userguide/private-connectivity.html) connection.

1. After you order your Outposts racks, AWS contacts you to collect VLAN, IP, BGP, and infrastructure subnet IPs. For more information, see [Local network connectivity](https://docs.aws.amazon.com/outposts/latest/network-userguide/outposts-rack2ndgen-local-rack.html).

1. During installation, AWS configures service link on the Outpost based on the information you provided.

1. You configure your local networking devices, such as routers, to connect to each Outpost network device through BGP connectivity. For information on service link VLAN, IP, and BGP connectivity, see [Network connectivity requirements](outposts-rack2ndgen-requirements.md#facility-networking).

1. You configure your networking devices, such as firewalls, to enable your Outposts to access to the AWS Region or home Region. AWS Outposts utilizes the [service link infrastructure subnet IPs](https://docs.aws.amazon.com/outposts/latest/network-userguide/outposts-rack2ndgen-local-rack.html#service-link-subnet) to set up VPN connections and exchange control and data traffic with the Region. Service link establishment is always initiated from the Outpost.

1. 
**Note**  
You won't be able to modify the service link configuration or connectivity type after you complete the order.