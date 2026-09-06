

# Access Patterns for Accessing a MemoryDB Cluster in an Amazon VPC
<a name="memorydb-vpc-accessing"></a>

MemoryDB supports the following scenarios for accessing a cluster in an Amazon VPC:

**Contents**
+ [Accessing a MemoryDB Cluster when it and the Amazon EC2 Instance are in the Same Amazon VPC](#memorydb-vpc-accessing-same-vpc)
+ [Accessing a MemoryDB Cluster when it and the Amazon EC2 Instance are in Different Amazon VPCs](#memorydb-vpc-accessing-different-vpc)
  + [In Different Amazon VPCs in the Same Region](#memorydb-vpc-accessing-different-vpc-same-region)
    + [Using Transit Gateway](#memorydb-vpc-accessing-using-transit-gateway)
  + [In Different Amazon VPCs in Different Regions](#memorydb-vpc-accessing-different-vpc-different-region)
    + [Using Transit VPC](#memorydb-vpc-accessing-different-vpc-different-region-using-transit-vpc)
+ [Accessing a MemoryDB Cluster from an Application Running in a Customer's Data Center](#memorydb-vpc-accessing-data-center)
  + [Using VPN Connectivity](#memorydb-vpc-accessing-data-center-vpn)
  + [Using Direct Connect](#memorydb-vpc-accessing-data-center-direct-connect)

## Accessing a MemoryDB Cluster when it and the Amazon EC2 Instance are in the Same Amazon VPC
<a name="memorydb-vpc-accessing-same-vpc"></a>

The most common use case is when an application deployed on an EC2 instance needs to connect to a cluster in the same VPC.

The simplest way to manage access between EC2 instances and clusters in the same VPC is to do the following:

1. Create a VPC security group for your cluster. This security group can be used to restrict access to the clusters. For example, you can create a custom rule for this security group that allows TCP access using the port you assigned to the cluster when you created it and an IP address you will use to access the cluster. 

   The default port for MemoryDB clusters is `6379`.

1. Create a VPC security group for your EC2 instances (web and application servers). This security group can, if needed, allow access to the EC2 instance from the Internet via the VPC's routing table. For example, you can set rules on this security group to allow TCP access to the EC2 instance over port 22.

1. Create custom rules in the security group for your cluster that allow connections from the security group you created for your EC2 instances. This would allow any member of the security group to access the clusters.

**To create a rule in a VPC security group that allows connections from another security group**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com/vpc).

1. In the left navigation pane, choose **Security Groups**.

1. Select or create a security group that you will use for your clusters. Under **Inbound Rules**, select **Edit Inbound Rules** and then select **Add Rule**. This security group will allow access to members of another security group.

1. From **Type** choose **Custom TCP Rule**.

   1. For **Port Range**, specify the port you used when you created your cluster.

      The default port for MemoryDB clusters is `6379`.

   1. In the **Source** box, start typing the ID of the security group. From the list select the security group you will use for your Amazon EC2 instances.

1. Choose **Save** when you finish.

## Accessing a MemoryDB Cluster when it and the Amazon EC2 Instance are in Different Amazon VPCs
<a name="memorydb-vpc-accessing-different-vpc"></a>

When your cluster is in a different VPC from the EC2 instance you are using to access it, there are several ways to access the cluster. If the cluster and EC2 instance are in different VPCs but in the same region, you can use VPC peering. If the cluster and the EC2 instance are in different regions, you can create VPN connectivity between regions.

**Topics**
+ [In Different Amazon VPCs in the Same Region](#memorydb-vpc-accessing-different-vpc-same-region)
+ [In Different Amazon VPCs in Different Regions](#memorydb-vpc-accessing-different-vpc-different-region)

 

### Accessing a MemoryDB Cluster when it and the Amazon EC2 Instance are in Different Amazon VPCs in the Same Region
<a name="memorydb-vpc-accessing-different-vpc-same-region"></a>

*Cluster accessed by an Amazon EC2 instance in a different Amazon VPC within the same Region - VPC Peering Connection*

A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them using private IP addresses. Instances in either VPC can communicate with each other as if they are within the same network. You can create a VPC peering connection between your own Amazon VPCs, or with an Amazon VPC in another AWS account within a single region. To learn more about Amazon VPC peering, see the [VPC documentation](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-peering.html).

**To access a cluster in a different Amazon VPC over peering**

1. Make sure that the two VPCs do not have an overlapping IP range or you will not be able to peer them.

1. Peer the two VPCs. For more information, see [Creating and Accepting an Amazon VPC Peering Connection](http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/create-vpc-peering-connection.html).

1. Update your routing table. For more information, see [Updating Your Route Tables for a VPC Peering Connection](http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/vpc-peering-routing.html)

1. Modify the Security Group of your MemoryDB cluster to allow inbound connection from the Application security group in the peered VPC. For more information, see [Reference Peer VPC Security Groups](http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/vpc-peering-security-groups.html).

Accessing a cluster over a peering connection will incur additional data transfer costs.

 

#### Using Transit Gateway
<a name="memorydb-vpc-accessing-using-transit-gateway"></a>

A transit gateway enables you to attach VPCs and VPN connections in the same AWS Region and route traffic between them. A transit gateway works across AWS accounts, and you can use AWS Resource Access Manager to share your transit gateway with other accounts. After you share a transit gateway with another AWS account, the account owner can attach their VPCs to your transit gateway. A user from either account can delete the attachment at any time.

You can enable multicast on a transit gateway, and then create a transit gateway multicast domain that allows multicast traffic to be sent from your multicast source to multicast group members over VPC attachments that you associate with the domain.

You can also create a peering connection attachment between transit gateways in different AWS Regions. This enables you to route traffic between the transit gateways' attachments across different Regions.

For more information, see [Transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html).

### Accessing a MemoryDB Cluster when it and the Amazon EC2 Instance are in Different Amazon VPCs in Different Regions
<a name="memorydb-vpc-accessing-different-vpc-different-region"></a>

#### Using Transit VPC
<a name="memorydb-vpc-accessing-different-vpc-different-region-using-transit-vpc"></a>

An alternative to using VPC peering, another common strategy for connecting multiple, geographically disperse VPCs and remote networks is to create a transit VPC that serves as a global network transit center. A transit VPC simplifies network management and minimizes the number of connections required to connect multiple VPCs and remote networks. This design can save time and effort and also reduce costs, as it is implemented virtually without the traditional expense of establishing a physical presence in a colocation transit hub or deploying physical network gear.

*Connecting across different VPCs in different regions*

Once the Transit Amazon VPC is established, an application deployed in a “spoke” VPC in one region can connect to a MemoryDB cluster in a “spoke” VPC within another region. 

**To access a cluster in a different VPC within a different AWS Region**

1. Deploy a Transit VPC Solution. For more information, see, [AWSTransit Gateway](https://aws.amazon.com/transit-gateway/).

1. Update the VPC routing tables in the App and VPCs to route traffic through the VGW (Virtual Private Gateway) and the VPN Appliance. In case of Dynamic Routing with Border Gateway Protocol (BGP) your routes may be automatically propagated.

1. Modify the Security Group of your MemoryDB cluster to allow inbound connection from the Application instances IP range. Note that you will not be able to reference the application server Security Group in this scenario.

Accessing a cluster across regions will introduce networking latencies and additional cross-region data transfer costs.

## Accessing a MemoryDB Cluster from an Application Running in a Customer's Data Center
<a name="memorydb-vpc-accessing-data-center"></a>

Another possible scenario is a Hybrid architecture where clients or applications in the customer’s data center may need to access a MemoryDB Cluster in the VPC. This scenario is also supported providing there is connectivity between the customers’ VPC and the data center either through VPN or Direct Connect.

**Topics**
+ [Using VPN Connectivity](#memorydb-vpc-accessing-data-center-vpn)
+ [Using Direct Connect](#memorydb-vpc-accessing-data-center-direct-connect)

 

### Accessing a MemoryDB Cluster from an Application Running in a Customer's Data Center Using VPN Connectivity
<a name="memorydb-vpc-accessing-data-center-vpn"></a>

*Connecting to MemoryDB from your data center via a VPN*

**To access a cluster in a VPC from on-prem application over VPN connection**

1. Establish VPN Connectivity by adding a hardware Virtual Private Gateway to your VPC. For more information, see [Adding a Hardware Virtual Private Gateway to Your VPC](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html).

1. Update the VPC routing table for the subnet where your MemoryDB cluster is deployed to allow traffic from your on-premises application server. In case of Dynamic Routing with BGP your routes may be automatically propagated.

1. Modify the Security Group of your MemoryDB cluster to allow inbound connection from the on-premises application servers.

Accessing a cluster over a VPN connection will introduce networking latencies and additional data transfer costs.

 

### Accessing a MemoryDB Cluster from an Application Running in a Customer's Data Center Using Direct Connect
<a name="memorydb-vpc-accessing-data-center-direct-connect"></a>

*Connecting to MemoryDB from your data center via Direct Connect*

**To access a MemoryDB cluster from an application running in your network using Direct Connect**

1. Establish Direct Connect connectivity. For more information, see, [Getting Started with AWS Direct Connect](http://docs.aws.amazon.com/directconnect/latest/UserGuide/getting_started.html).

1. Modify the Security Group of your MemoryDB cluster to allow inbound connection from the on-premises application servers.

Accessing a cluster over DX connection may introduce networking latencies and additional data transfer charges.