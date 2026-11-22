

# Create a VPC with subnets and route tables

Create the VPC that Amazon Elastic VMware Service deploys your environment into, with a private subnet for service access and route tables with the gateway routes that deployment needs. You can use the Amazon VPC console or the AWS CLI.

**Important**  
You can’t change the VPC CIDR block after you create the environment. The VPC CIDR block must have a minimum size of /22 and must leave room for the VLAN subnets that Amazon EVS creates and for future growth. For sizing guidance, see [Plan your VPC and VLAN subnets](plan-network-sizing.md) and [VLAN subnets, VLAN IDs, and IP addresses](vlan-subnet-reference.md).

## Before you begin
<a name="network-create-vpc-prereqs"></a>

Make sure that the following are true.
+ You plan to create the VPC, the subnets, and the Amazon EVS environment in the same AWS account. Amazon EVS doesn’t support cross-account sharing of VPC subnets or environments.
+ You’ve chosen an AWS Region where Amazon EVS is available. For more information, see [AWS Regions for Amazon EVS](regions-reference.md).
+ You’ve chosen one Availability Zone. An Amazon EVS environment runs in one Availability Zone. Identify the zone by its Availability Zone ID, for example `usw2-az1`, because zone names map to different zone IDs in different accounts. Create every subnet of the VPC in this zone. For more information, see [VPC and subnets](plan-network-supported.md#plan-network-supported-vpc).
+ You’ve chosen the IPv4 CIDR block for the VPC and for each subnet. Amazon EVS doesn’t support IPv6.
+ You’ve decided whether you need a NAT gateway. In Self-deployed mode you must create one, because the VMware Cloud Foundation (VCF) Installer downloads the VCF software from the Broadcom online depot over the internet. In EVS-deployed mode, you need one only if your environment needs outbound internet access. A NAT gateway has a cost. For more information, see [Pricing for NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-pricing.html).

The private subnet that you create is the service access subnet that you provide to Amazon EVS when you create the environment. For more information, see [Concepts and components of Amazon EVS](concepts.md).

## Create the VPC and subnets
<a name="network-create-vpc-steps"></a>

You can create the VPC and subnets in the Amazon VPC console or with the AWS CLI. Choose the tab for the method that you use.

**Example**  

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc), and on the VPC dashboard choose **Create VPC**.

1. For **Resources to create**, choose **VPC and more**. Keep **Name tag auto-generation** selected to create Name tags, or clear it to enter your own Name tags.

1. For **IPv4 CIDR block**, enter the IPv4 CIDR block that you chose for the VPC.

1. Keep **Tenancy** as `Default`. EC2 instances that launch into this VPC then use the tenancy attribute that is specified at launch. Amazon EVS launches bare metal EC2 instances on your behalf.

1. For **Number of Availability Zones (AZs)**, choose **1**. Expand **Customize AZs** and choose the Availability Zone for your subnets.

1. For **Number of public subnets**, choose **1**. The NAT gateway needs this public subnet. In EVS-deployed mode without outbound internet access, choose **0**.

1. For **Number of private subnets**, choose **1**. This subnet is the service access subnet.

1. Expand **Customize subnets CIDR blocks** and enter the IP address ranges for your subnets. Leave enough space in the VPC CIDR block for the VLAN subnets that Amazon EVS creates.

1. For **NAT gateways**, choose **In 1 AZ**. Self-deployed mode requires the NAT gateway. In EVS-deployed mode, choose it only if you need outbound internet access over IPv4.

1. For **VPC endpoints**, choose **None**. Amazon EVS doesn’t support gateway VPC endpoints for Amazon S3. To connect to Amazon S3, set up an interface VPC endpoint. For more information, see [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) in the * Amazon S3 User Guide*.

1. For **DNS options**, keep the defaults selected, because Amazon EVS requires DNS resolution for all VCF components. (Optional) To add a tag, expand **Additional tags**, choose **Add new tag**, and enter a tag key and value.

1. Choose **Create VPC**.

    Amazon VPC creates a main route table and implicitly associates the subnets with it.

1. Create the VPC and store its ID for the following commands. Replace the example addresses and names with your own values.

   ```bash
   VPC_ID=$(aws ec2 create-vpc \
     --cidr-block 10.10.0.0/16 \
     --instance-tenancy default \
     --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=evs-vpc}]' \
     --query 'Vpc.VpcId' \
     --output text)
   ```

1. Enable DNS hostnames and DNS support.

   ```bash
   aws ec2 modify-vpc-attribute \
     --vpc-id $VPC_ID \
     --enable-dns-hostnames
   aws ec2 modify-vpc-attribute \
     --vpc-id $VPC_ID \
     --enable-dns-support
   ```

1. Create the private subnet (the service access subnet) and store its ID.

   ```bash
   PRIVATE_SUBNET_ID=$(aws ec2 create-subnet \
     --vpc-id $VPC_ID \
     --cidr-block 10.10.200.0/24 \
     --availability-zone-id usw2-az1 \
     --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=evs-private-subnet}]' \
     --query 'Subnet.SubnetId' \
     --output text)
   ```

1. Create a public subnet for the NAT gateway and store its ID. Self-deployed mode requires the NAT gateway. In EVS-deployed mode, you can skip this step and the next two if you don’t need outbound internet access.

   ```bash
   PUBLIC_SUBNET_ID=$(aws ec2 create-subnet \
     --vpc-id $VPC_ID \
     --cidr-block 10.10.201.0/24 \
     --availability-zone-id usw2-az1 \
     --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=evs-public-subnet}]' \
     --query 'Subnet.SubnetId' \
     --output text)
   ```

1. Create an internet gateway and attach it to the VPC.

   ```bash
   IGW_ID=$(aws ec2 create-internet-gateway \
     --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=evs-igw}]' \
     --query 'InternetGateway.InternetGatewayId' \
     --output text)
   
   aws ec2 attach-internet-gateway \
     --vpc-id $VPC_ID \
     --internet-gateway-id $IGW_ID
   ```

1. Allocate an Elastic IP address and create a NAT gateway in the public subnet.

   ```bash
   EIP_ID=$(aws ec2 allocate-address \
     --domain vpc \
     --tag-specifications 'ResourceType=elastic-ip,Tags=[{Key=Name,Value=evs-nat-eip}]' \
     --query 'AllocationId' \
     --output text)
   
   NAT_GW_ID=$(aws ec2 create-nat-gateway \
     --subnet-id $PUBLIC_SUBNET_ID \
     --allocation-id $EIP_ID \
     --tag-specifications 'ResourceType=natgateway,Tags=[{Key=Name,Value=evs-nat}]' \
     --query 'NatGateway.NatGatewayId' \
     --output text)
   ```

   The NAT gateway must be in the `available` state before you create a route that uses it. To check, run `aws ec2 describe-nat-gateways --nat-gateway-ids $NAT_GW_ID --query 'NatGateways[0].State'`.

1. Create a private route table and a public route table, and store their IDs.

   ```bash
   PRIVATE_RT_ID=$(aws ec2 create-route-table \
     --vpc-id $VPC_ID \
     --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=evs-private-rt}]' \
     --query 'RouteTable.RouteTableId' \
     --output text)
   
   PUBLIC_RT_ID=$(aws ec2 create-route-table \
     --vpc-id $VPC_ID \
     --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=evs-public-rt}]' \
     --query 'RouteTable.RouteTableId' \
     --output text)
   ```

1. Add the default routes. The public route table routes to the internet gateway, and the private route table routes to the NAT gateway.

   ```bash
   aws ec2 create-route \
     --route-table-id $PUBLIC_RT_ID \
     --destination-cidr-block 0.0.0.0/0 \
     --gateway-id $IGW_ID
   
   aws ec2 create-route \
     --route-table-id $PRIVATE_RT_ID \
     --destination-cidr-block 0.0.0.0/0 \
     --nat-gateway-id $NAT_GW_ID
   ```

1. Associate the route tables with your subnets.

   ```bash
   aws ec2 associate-route-table \
     --route-table-id $PRIVATE_RT_ID \
     --subnet-id $PRIVATE_SUBNET_ID
   
   aws ec2 associate-route-table \
     --route-table-id $PUBLIC_RT_ID \
     --subnet-id $PUBLIC_SUBNET_ID
   ```

    Amazon VPC also creates a main route table for the VPC. Subnets without an explicit association use it.

You have created the VPC, the service access subnet, and the route tables.

## Configure the main route table
<a name="vpc-main-rt"></a>

During environment deployment, the Amazon EVS VLAN subnets are implicitly associated with the VPC main route table. For deployment to succeed, the main route table must route traffic to dependent services such as your DNS servers and on-premises systems. The main route table must also include a route for the VPC CIDR block.

**Important**  
Don’t use a custom route table for the VLAN subnets while you create the environment, because this can cause connectivity issues. Amazon EVS supports custom route tables only after the environment is created. After deployment, you must associate each VLAN subnet explicitly. For more information, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md).

### Gateway route requirements
<a name="vpc-main-rt-reqs"></a>

Add routes on the main route table for the gateways that your connectivity needs.


| Gateway | Required | Route rules | 
| --- | --- | --- | 
| NAT gateway | Yes in Self-deployed mode, for the Broadcom online depot. In EVS-deployed mode, only for outbound internet access. | Place the NAT gateway in a public subnet with internet gateway access. Add routes from the private subnets and the Amazon EVS VLAN subnets to the NAT gateway. For more information, see [Work with NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html). | 
| Transit gateway | For on-premises connectivity through Direct Connect or AWS Site-to-Site VPN | Add routes for your on-premises network ranges. Configure route propagation if you use Border Gateway Protocol (BGP). For more information, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md) and [Transit gateways in Amazon VPC Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html). | 

To add a route in the Amazon VPC console or with the AWS CLI, choose the tab for the method that you use.

**Example**  

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc) and choose **Route tables** in the navigation pane.

1. Select the route table for your VPC where **Main** is **Yes**.

1. On the **Routes** tab, choose **Edit routes**, and then choose **Add route**.

1. Enter the destination CIDR block and choose the target gateway.

1. Choose **Save changes**.

1. Find the ID of the main route table. If `$VPC_ID` isn’t set in your shell, replace it in the following commands with the ID of your VPC.

   ```bash
   MAIN_RT_ID=$(aws ec2 describe-route-tables \
     --filters Name=vpc-id,Values=$VPC_ID Name=association.main,Values=true \
     --query 'RouteTables[0].RouteTableId' \
     --output text)
   ```

1. Add a route. This example sends the default route to the NAT gateway. If `$NAT_GW_ID` isn’t set in your shell, replace it in the following commands with the ID of your NAT gateway.

   ```bash
   aws ec2 create-route \
     --route-table-id $MAIN_RT_ID \
     --destination-cidr-block 0.0.0.0/0 \
     --nat-gateway-id $NAT_GW_ID
   ```

You have added the routes to the main route table.

We recommend that you document your route table configurations, use consistent names, and test connectivity after each change, so that you can find routing problems quickly. For more information, see [Configure route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the * Amazon VPC User Guide*.

Next, configure DNS and NTP for the VPC. See [Configure DNS and NTP with a DHCP option set](network-dhcp-dns-ntp.md).