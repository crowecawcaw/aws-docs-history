

# Get started using Traffic Mirroring to monitor network traffic
<a name="traffic-mirroring-getting-started"></a>

To get started using Amazon VPC Traffic Mirroring, you'll need a VPC with at least one elastic network interface (ENI) that you want to mirror traffic from. In this section, you'll create a traffic mirror target and you'll create a traffic mirror session, which defines the parameters of the traffic mirroring operation, such as the source ENI, the mirror target, and any filtering rules. Once these components are in place, you'll start mirroring traffic to the target for monitoring and analysis. 

A mirror session is a connection between a mirror source and a mirror target. In the following diagram, both the mirror source and the mirror target are EC2 instances. The mirror filter determines which network packets are mirrored. For example, you can add inbound and outbound rules to the filter such that it rejects SSH traffic but accepts all other traffic. Traffic Mirroring applies the filter rules, and then copies the accepted traffic from the network interface of the mirror source to the network interface of the mirror target. You can run your capture and analysis tools on the packets delivered to the mirror target.

![A traffic mirror session where the mirror target is an EC2 instance.](http://docs.aws.amazon.com/vpc/latest/mirroring/images/get-started.png)


**Topics**
+ [Prerequisites](#traffic-mirroring-prerequisites)
+ [Step 1: Create the traffic mirror target](#step-create-traffic-mirroring-target)
+ [Step 2: Create the traffic mirror filter](#step-create-traffic-mirroring-filters)
+ [Step 3: Create the traffic mirror session](#step-create-traffic-mirroring-sessions)
+ [Step 4: Analyze the data](#analyze-data)

## Prerequisites
<a name="traffic-mirroring-prerequisites"></a>
+ The traffic mirror source is a network interface that you want to mirror traffic from. The traffic mirror target is the destination for the mirrored traffic, such as an EC2 instance.
+ The traffic mirror source and traffic mirror target must be in the same VPC or in VPCs that are connected (for example, using VPC peering or a transit gateway).
+ The traffic mirror target must allow traffic to UDP port 4789.
+ The traffic mirror source must have a route table entry for the traffic mirror target.
+ Security group rules and network ACL rules on the traffic mirror target cannot drop the mirrored traffic from the traffic mirror source.

## Step 1: Create the traffic mirror target
<a name="step-create-traffic-mirroring-target"></a>

Use an EC2 instance as the destination for the mirrored traffic.

**To create a traffic mirror target**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the **Region** selector, choose the AWS Region that you used when you created the EC2 instance.

1. On the navigation pane, choose **Traffic Mirroring**, **Mirror targets**.

1. Choose **Create traffic mirror target**.

1. (Optional) For **Name tag**, enter a name for the traffic mirror target.

1. (Optional) For **Description**, enter a description for the traffic mirror target.

1. For **Target type**, choose **Network Interface**.

1. For **Target**, choose the network interface of the EC2 instance.

1. (Optional) For each tag to add, choose **Add new tag** and enter the tag key and tag value.

1. Choose **Create**.

## Step 2: Create the traffic mirror filter
<a name="step-create-traffic-mirroring-filters"></a>

A traffic mirror filter contains one or more traffic mirror rules, and a set of network services. The filters and rules that you add define the traffic that is mirrored. 

**To create a traffic mirror filter**

1. On the navigation pane, choose **Traffic Mirroring**, **Mirror filters**.

1. Choose **Create traffic mirror filter**.

1. (Optional For **Name tag**, enter a name for the traffic mirror filter.

1. (Optional) For **Description**, enter a description for the traffic mirror filter.

1. For each rule, inbound or outbound, choose **Add rule**, and then specify the following information:
   + **Number**: The rule priority.
   + **Rule action**: Indicates whether to accept or reject the packets.
   + **Protocol**: The protocol.
   + (Optional) **Source port range**: The source port range.
   + (Optional) **Destination port range**: The destination port range.
   + **Source CIDR block**: The source CIDR block.
   + **Destination CIDR block**: The destination CIDR block.
   + **Description**: A description for the rule.

1. (Optional) For each tag to add, choose **Add new tag** and enter the tag key and tag value.

1. Choose **Create**.

## Step 3: Create the traffic mirror session
<a name="step-create-traffic-mirroring-sessions"></a>

Create a traffic mirror session that sends mirrored packets from the source to a target so that you can monitor and analyze traffic.

**To create a traffic mirror session**

1. In the navigation pane, choose **Traffic Mirroring**, **Mirror sessions**.

1. Choose **Create traffic mirror session**.

1. (Optional) For **Name tag**, enter a name for the traffic mirror session.

1. (Optional) For **Description**, enter a description for the traffic mirror session.

1. For **Mirror source**, choose the network interface of the mirror source. 

1. For **Mirror target**, choose your traffic mirror target.

1. For **Additional settings**, do the following:

   1. For **Session number**, enter **1**, which is the highest priority.

   1. (Optional) For **VNI**, enter the VXLAN ID to use for the traffic mirror session. For more information about the VXLAN protocol, see [RFC 7348](https://tools.ietf.org/html/rfc7348).

      If you do not enter a value, we assign a random unused number.

   1. (Optional) For **Packet length**, enter the number of bytes in each packet to mirror.

      To mirror the entire packet, do not enter a value. To mirror only a portion of each packet, set this value to the number of bytes to mirror. For example, if you set this value to 100, the first 100 bytes after the VXLAN header that meet the filter criteria are copied to the target.

   1. For **Filter**, choose your traffic mirror filter.

1. (Optional) For each tag to add, choose **Add new tag** and enter the tag key and tag value.

1. Choose **Create**.

## Step 4: Analyze the data
<a name="analyze-data"></a>

After the mirrored traffic is copied to the traffic mirror target, you can use a tool from the [AWS Partner Network](https://partners.amazonaws.com/search/partners/?keyword=traffic%20mirroring) to analyze the data.