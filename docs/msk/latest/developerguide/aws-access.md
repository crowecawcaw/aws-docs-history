

# Access from within AWS but outside cluster's VPC
<a name="aws-access"></a>

To connect to an MSK cluster from inside AWS but outside the cluster's Amazon VPC, the following options exist.

## Amazon VPC peering
<a name="vpc-peering"></a>

To connect to your MSK cluster from a VPC that's different from the cluster's VPC, you can create a peering connection between the two VPCs. For information about VPC peering, see the [Amazon VPC Peering Guide](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html).

## Direct Connect
<a name="direct-connect"></a>

Direct Connect links your on-premise network to AWS over a standard 1 gigabit or 10 gigabit Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an Direct Connect router. With this connection in place, you can create virtual interfaces directly to the AWS cloud and Amazon VPC, bypassing Internet service providers in your network path. For more information, see [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html).

## AWS Transit Gateway
<a name="transit-gateway"></a>

AWS Transit Gateway is a service that enables you to connect your VPCs and your on-premises networks to a single gateway. For information about how to use AWS Transit Gateway, see [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

## VPN connections
<a name="vpn-connections"></a>

You can connect your MSK cluster's VPC to remote networks and users using the VPN connectivity options described in the following topic: [VPN Connections](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html).

## REST proxies
<a name="rest-proxies"></a>

You can install a REST proxy on an instance running within your cluster's Amazon VPC. REST proxies enable your producers and consumers to communicate with the cluster through HTTP API requests.

## Multiple Region multi-VPC connectivity
<a name="multi-vpc-multi-region"></a>

The following document describes connectivity options for multiple VPCs that reside in different Regions: [Multiple Region Multi-VPC Connectivity](https://aws.amazon.com/answers/networking/aws-multiple-region-multi-vpc-connectivity/).

## Single Region multi-VPC private connectivity
<a name="multi-vpc-single-region"></a>

Multi-VPC private connectivity (powered by [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)) for Amazon Managed Streaming for Apache Kafka (Amazon MSK) clusters is a feature that enables you to more quickly connect Kafka clients hosted in different Virtual Private Clouds (VPCs) and AWS accounts to an Amazon MSK cluster.

See [Single Region multi-VPC connectivity for cross-account clients](https://docs.aws.amazon.com/msk/latest/developerguide/aws-access-mult-vpc.html).

## EC2-Classic networking is retired
<a name="ec2-classic-retired"></a>

Amazon MSK no longer supports Amazon EC2 instances running with Amazon EC2-Classic networking.

See [EC2-Classic Networking is Retiring – Here’s How to Prepare](https://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/).