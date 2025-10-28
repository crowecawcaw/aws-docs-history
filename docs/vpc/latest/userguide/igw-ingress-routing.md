# Route internet traffic to a single network interface

You can route inbound internet traffic destined for large pools of public IP addresses to a single elastic network interface (ENI) in your VPC.

Previously, internet gateways only accepted traffic destined for public IP addresses that were directly associated with network interfaces in the VPC. Instance types have limits on the number of IP addresses that can be associated with network interfaces, creating challenges for industries like Telecommunications and Internet of Things (IoT) that need to handle traffic for IP pools larger than these limits.

This routing eliminates complex address translation on inbound internet connections. You can bring your own public IP pools (BYOIP) and configure your VPC internet gateway to accept and route traffic for the entire pool to a single network interface. This feature is particularly valuable for:

- **Telecommunications**: Managing large subscriber IP pools without address translation overhead
- **IoT applications**: Consolidating traffic from thousands of device IP addresses
- **Any scenario**: Requiring traffic routing beyond ENI association limits
  You can integrate this routing with VPC Route Server for dynamic route updates during failover scenarios.

###### Key benefits

This routing approach provides the following benefits:

- **No address translation required** - Direct routing
  eliminates NAT complexity
- **Bypass ENI limits** - Handle IP pools larger than
  instance association limits
- **Industry-optimized** - Purpose-built for Telco and IoT
  requirements
- **Dynamic failover** - Integrates with Route Server for
  automatic updates

###### Availability

You can use this feature in all AWS commercial regions, AWS China regions, and AWS
GovCloud regions.

###### Contents

- [Before you begin](#before-you-begin "#before-you-begin")
- [How this feature works](#how-this-feature-works "#how-this-feature-works")
- [Step 1: Create a VPC](#step-1-create-a-vpc "#step-1-create-a-vpc")
- [Step 2: Create and attach an internet gateway](#step-2-create-and-attach-an-internet-gateway "#step-2-create-and-attach-an-internet-gateway")
- [Step 3: Create a subnet for your target instance](#step-3-create-a-subnet "#step-3-create-a-subnet")
- [Step 4: Create a route table for the subnet](#step-4-create-a-route-table-for-the-subnet "#step-4-create-a-route-table-for-the-subnet")
- [Step 5: Create a security group for the target instance](#step-5-create-a-security-group "#step-5-create-a-security-group")
- [Step 6: Launch target EC2 instance](#step-6-launch-an-ec2-instance "#step-6-launch-an-ec2-instance")
- [Step 7: Create the internet gateway route table](#step-7-create-a-route-table-for-the-internet-gateway "#step-7-create-a-route-table-for-the-internet-gateway")
- [Step 8: Associate the route table with the internet gateway](#step-8-associate-the-route-table-with-the-internet-gateway "#step-8-associate-the-route-table-with-the-internet-gateway")
- [Step 9: Associate your BYOIP pool with the internet gateway](#step-9-associate-your-byoip-pool-with-the-internet-gateway "#step-9-associate-your-byoip-pool-with-the-internet-gateway")
- [Step 10: Add static route to target your instance](#step-10-add-static-route-to-target-your-instance "#step-10-add-static-route-to-target-your-instance")
- [Step 11: Configure the target instance](#step-11-configure-the-target-instance "#step-11-configure-the-target-instance")
- [Step 12: Configure instance for traffic handling](#step-12-configure-instance-for-traffic-handling "#step-12-configure-instance-for-traffic-handling")
- [Step 13: Test connectivity](#step-13-test-connectivity "#step-13-test-connectivity")
- [Troubleshooting](#troubleshooting "#troubleshooting")
- [Advanced option: Route server integration for dynamic routing](#advanced-option-route-server-integration "#advanced-option-route-server-integration")
- [Clean up](#clean-up "#clean-up")

## Before you begin

Before starting this tutorial, ensure you have:

1. **A BYOIP pool**: You must have already brought your own IP address range to AWS. Complete the steps in [Bring your own IP addresses (BYOIP) in Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-byoip.md "../../../AWSEC2/latest/UserGuide/ec2-byoip.md").
2. **Verify your BYOIP pool**: Confirm your pool is ready by running:

```
aws ec2 describe-public-ipv4-pools --region us-east-1
```

Look for your pool in the output and ensure the `PoolAddressRanges` shows `Available` addresses. 3. **Appropriate permissions**: Ensure your AWS account has permissions to create VPC resources, EC2 instances, and manage BYOIP pools.

## How this feature works

This section explains the technical concepts behind internet gateway ingress routing and how traffic flows from the internet to your target instance.

### Why use internet gateway ingress routing

Previously, you needed to perform address translation to consolidate traffic for large numbers of IP addresses due to ENI association limits. This enhancement removes that complexity by allowing direct routing of BYOIP pools to target instances.

### How the routing works

This feature only works with the public IP CIDRs that you bring to AWS following the BYOIP process. The BYOIP process ensures that your account owns the public IP CIDR. Once you have the BYOIP public CIDR:

1. You associate this public IP address pool with an internet gateway route table. The internet gateway must already be associated with a VPC. This association allows the VPC to accept traffic destined for the IP CIDR. Ensure that the internet gateway has a dedicated route table that is not shared with any subnets.
2. Now that you have associated the BYOIP pool with the internet gateway route table, you can enter a route with a destination equal to the IP CIDR or a subset of it in the internet gateway route table. The target of this route would be the ENI where you want to route your traffic.
3. When your traffic destined for your BYOIP CIDR enters AWS, AWS looks at the internet gateway route table and accordingly routes traffic to the relevant VPC.
4. Inside the VPC, the internet gateway routes the traffic to the target ENI.
5. The target (an elastic network interface associated with your workload) processes the traffic.

**Best practices**

- **Keep route tables separate**: The internet gateway route table must be dedicated only to the internet gateway. Do not associate this route table with any VPC subnets. Use separate route tables for subnet routing.
- **Don't directly assign BYOIP IPs**: Do not associate public IP addresses from your BYOIP pool directly to EC2 instances or network interfaces. The internet gateway ingress routing feature routes traffic to instances without requiring direct IP association.

###### Important

If you are using [VPC Block Public Access (BPA)](security-vpc-bpa.md "security-vpc-bpa.md"), when BPA is enabled, it will block traffic to
subnets using ingress routing, even if you've set a subnet-level BPA exclusion. Subnet-level
exclusions do not work for ingress routing. To allow ingress routing traffic with BPA
enabled:

- Disable BPA completely, or
- Use a VPC-level exclusion

## Step 1: Create a VPC

Complete this step to create a VPC that will host your target instance and internet gateway.

###### Note

Ensure you have not reached your VPC quota limit. For more information, see [Amazon VPC quotas](amazon-vpc-limits.md "amazon-vpc-limits.md").

**AWS console**

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc").
2. On the VPC dashboard, choose **Create VPC**.
3. For **Resources to create**, choose **VPC only**.
4. For **Name tag**, enter a name for your VPC (for example, `IGW-Ingress-VPC`).
5. For **IPv4 CIDR block**, enter a CIDR block (for example, `10.0.0.0/16`).
6. Choose **Create VPC**.

**AWS CLI**

```
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=IGW-Ingress-VPC}]' --region us-east-1
```

## Step 2: Create and attach an internet gateway

Complete this step to create an internet gateway and attach it to your VPC to enable internet connectivity.

**AWS console**

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc").
2. In the VPC console, choose **Internet gateways**.
3. Choose **Create internet gateway**.
4. For **Name tag**, enter a name for your internet gateway (for example, `IGW-Ingress-Gateway`).
5. Choose **Create internet gateway**.
6. Select your internet gateway and choose **Actions**, **Attach to VPC**.
7. Select your VPC and choose **Attach internet gateway**.

**AWS CLI**

```
aws ec2 create-internet-gateway --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=IGW-Ingress-Gateway}]' --region us-east-1

aws ec2 attach-internet-gateway --internet-gateway-id igw-0123456789abcdef0 --vpc-id vpc-0123456789abcdef0 --region us-east-1
```

**Note**: Replace the resource IDs with your actual IDs from the previous step.

## Step 3: Create a subnet for your target instance

Complete this step to create a subnet where your target instance will be deployed.

**AWS console**

1. In the VPC console navigation pane, choose **Subnets**.
2. Choose **Create subnet**.
3. Under **VPC ID**, choose your VPC.
4. For **Subnet name**, enter a name (for example, `Target-Subnet`).
5. For **Availability Zone**, you can choose a Zone for your subnet, or leave the default **No Preference** to let AWS choose one for you.
6. For **IPv4 CIDR block**, select **Manual input** and enter a CIDR block (for example, `10.0.1.0/24`).
7. Choose **Create subnet**.

**AWS CLI**

```
aws ec2 create-subnet \
    --vpc-id vpc-0123456789abcdef0 \
    --cidr-block 10.0.1.0/24 \
    --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Target-Subnet}]' \
    --region us-east-1
```

## Step 4: Create a route table for the subnet

Complete this step to create a route table for your subnet and associate it with the subnet.

**AWS console**

1. In the VPC console navigation pane, choose **Route tables**.
2. Choose **Create route table**.
3. For **Name**, enter a name for your route table (for example, `Target-Subnet-Route-Table`).
4. For **VPC**, choose your VPC.
5. Choose **Create route table**.
6. Select your route table and choose **Actions**, **Edit subnet associations**.
7. Select your subnet and choose **Save associations**.

**AWS CLI**

```
aws ec2 create-route-table \
    --vpc-id vpc-0123456789abcdef0 \
    --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=Target-Subnet-Route-Table}]' \
    --region us-east-1

aws ec2 associate-route-table \
    --route-table-id rtb-0987654321fedcba0 \
    --subnet-id subnet-0123456789abcdef0 \
    --region us-east-1
```

## Step 5: Create a security group for the target instance

Complete this step to create a security group that will control network access to your target instance.

**AWS console**

1. In the VPC console navigation pane, choose **Security Groups**.
2. Choose **Create security group**.
3. For **Security group name**, enter a name (for example, `IGW-Target-SG`).
4. For **Description**, enter `Security group for IGW ingress routing target instance`.
5. For **VPC**, select your VPC.
6. To add inbound rules, choose **Inbound rules**. For each rule, choose **Add rule** and specify the following:
   - **Type**: All ICMP - IPv4, **Source**: 0.0.0.0/0 (for ping testing).
   - **Type**: SSH, **Port**: 22, **Source**: 0.0.0.0/0 (for EC2 Instance Connect).

###### Note

This security group opens SSH ports to all internet traffic for this tutorial. This tutorial is for educational purposes and should not be configured for production environments. In production, restrict SSH access to specific IP ranges.

- Choose **Create security group**.

**AWS CLI**

```
aws ec2 create-security-group \
    --group-name IGW-Target-SG \
    --description "Security group for IGW ingress routing target instance" \
    --vpc-id vpc-0123456789abcdef0 \
    --region us-east-1

aws ec2 authorize-security-group-ingress \
    --group-id sg-0123456789abcdef0 \
    --protocol icmp \
    --port -1 \
    --cidr 0.0.0.0/0 \
    --region us-east-1

aws ec2 authorize-security-group-ingress \
    --group-id sg-0123456789abcdef0 \
    --protocol tcp \
    --port 22 \
    --cidr 0.0.0.0/0 \
    --region us-east-1
```

## Step 6: Launch target EC2 instance

Complete this step to launch the EC2 instance that will receive traffic from your BYOIP pool.

**AWS console**

1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").
2. Choose **Launch instance**.
3. For **Name**, enter a name for your instance (for example, `IGW-Target-Instance`).
4. For **Application and OS Images (Amazon Machine Image)**, choose **Amazon Linux 2023 AMI**.
5. For **Instance type**, choose **t2.micro** (eligible for free tier).
6. For **Key pair (login)**, select an existing key pair or create a new one.
7. For **Network settings**, choose **Edit** and configure:
   - **VPC**: Select your VPC
   - **Subnet**: Select your subnet
   - **Auto-assign public IP**: Enable
   - **Firewall (security groups)**: Select existing security group and choose your security group

8. Choose **Launch instance**.
9. **Important**: After launch, go to the instance details and note the **Network interface ID** (starts with "eni-") - you'll need this for Step 10.

**AWS CLI**

```
aws ec2 run-instances \
    --image-id ami-0abcdef1234567890 \
    --count 1 \
    --instance-type t2.micro \
    --key-name your-key-pair \
    --security-group-ids sg-0123456789abcdef0 \
    --subnet-id subnet-0123456789abcdef0 \
    --associate-public-ip-address \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=IGW-Target-Instance}]' \
    --region us-east-1
```

**To find the ENI ID in the console:**

1. In the EC2 console, select your instance.
2. Go to the **Networking** tab.
3. Note the **Network interface ID** (for example, `eni-0abcdef1234567890`).

**To find the ENI ID using AWS CLI:**

```
aws ec2 describe-instances --instance-ids i-0123456789abcdef0 --query 'Reservations[0].Instances[0].NetworkInterfaces[0].NetworkInterfaceId' --output text --region us-east-1
```

## Step 7: Create the internet gateway route table

Complete this step to create a dedicated route table for the internet gateway that will handle ingress routing.

**AWS console**

1. In the VPC console, choose **Route tables**.
2. Choose **Create route table**.
3. For **Name**, enter a name for your route table (for example, `IGW-Ingress-Route-Table`).
4. For **VPC**, choose your VPC.
5. Choose **Create route table**.
6. Select your route table and choose the **Edge associations** tab.
7. Choose **Edit edge associations**.
8. Select your internet gateway and choose **Save changes**.

**AWS CLI**

```
aws ec2 create-route-table \
    --vpc-id vpc-0123456789abcdef0 \
    --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=IGW-Ingress-Route-Table}]' \
    --region us-east-1
```

## Step 8: Associate the route table with the internet gateway

Complete this step to associate your route table with the internet gateway to enable ingress routing functionality.

**AWS console**

1. In the VPC console navigation pane, choose **Route tables**, and then select the route table you created.
2. From the **Edge associations** tab, choose **Edit edge associations**.
3. Select the checkbox for the internet gateway.
4. Choose **Save changes**.

**AWS CLI**

```
aws ec2 associate-route-table \
    --route-table-id rtb-0123456789abcdef0 \
    --gateway-id igw-0123456789abcdef0 \
    --region us-east-1
```

## Step 9: Associate your BYOIP pool with the internet gateway

Complete this step to associate your BYOIP pool with the internet gateway route table, enabling the VPC to accept traffic for your IP range.

**AWS console**

1. In the VPC console navigation pane, choose **Route tables**, and select the internet gateway route table you created.
2. Click on the **IPv4 pool associations** tab.
3. Click on the **Edit associations** button.
4. Select your BYOIP pool (for example, `pool-12345678901234567`).
5. Click on the **Save associations** button.

**AWS CLI**

```
aws ec2 associate-route-table \
    --route-table-id rtb-0123456789abcdef0 \
    --public-ipv4-pool pool-12345678901234567 \
    --region us-east-1
```

**Note**: Replace `rtb-0123456789abcdef0` with your internet gateway route table ID and `pool-12345678901234567` with your BYOIP pool ID.

## Step 10: Add static route to target your instance

Complete this step to add a route that directs traffic from your BYOIP range to your target instance's network interface.

**AWS console**

1. In the VPC console navigation pane, choose **Route tables**, and select the internet gateway route table you created.
2. Choose **Actions**, **Edit routes**.
3. Choose **Add route**.
4. For **Destination**, enter your BYOIP CIDR or a subset (for example, `203.0.113.0/24`). The prefix must be between /23 and /28.
5. For **Target**, select **Network interface** and enter your instance's ENI ID (for example, `eni-0abcdef1234567890`).
6. Choose **Save changes**.

**AWS CLI**

```
aws ec2 create-route \
    --route-table-id rtb-0123456789abcdef0 \
    --destination-cidr-block 203.0.113.0/24 \
    --network-interface-id eni-0abcdef1234567890 \
    --region us-east-1
```

## Step 11: Configure the target instance

Complete this step to configure your target instance to properly handle traffic destined for BYOIP addresses.

**Important**: Complete this instance configuration step before testing connectivity (Step 12). The instance must be configured to respond to BYOIP addresses for the ingress routing to work properly.

**AWS console**

1. Connect to your target instance using EC2 Instance Connect:
   - In the EC2 console, select your instance.
   - Choose **Actions** > **Connect**.
   - Select **EC2 Instance Connect** tab.
   - Choose **Connect**.

2. Add specific BYOIP IP address to your instance interface:

First, find your network interface name:

```
ip link show
```

Then add the IP address (replace `203.0.113.10` with an IP from your BYOIP range):

```
sudo ip addr add 203.0.113.10/32 dev eth0
```

**Note**: Replace `203.0.113.10` with any IP address from your BYOIP range that you want to test. The interface name may be `eth0`, `ens5`, or similar depending on your instance type. 3. In the EC2 console, disable source/destination check:

    * Select your instance.
    * Go to **Networking** tab, click on the network interface.
    * Choose **Actions**, **Change source/dest check**, **Disable**.

**AWS CLI**

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id eni-0abcdef1234567890 \
    --no-source-dest-check \
    --region us-east-1
```

## Step 12: Configure instance for traffic handling

Complete this step to add BYOIP addresses to your instance and disable source/destination checking to enable proper traffic handling.

**AWS console**

1. Connect to your target instance using EC2 Instance Connect:
   - In the EC2 console, select your instance.
   - Choose **Actions** > **Connect**.
   - Select **EC2 Instance Connect** tab.
   - Choose **Connect**.

2. Add specific BYOIP IP address to your instance interface:

First, find your network interface name:

```
ip link show
```

Then add the IP address (replace `ens5` with your actual interface name):

```
sudo ip addr add 203.0.113.10/32 dev ens5
```

**Note**: Replace `203.0.113.10` with any IP address from your BYOIP range that you want to test. The interface name may be `eth0`, `ens5`, or similar depending on your instance type. 3. In the EC2 console, disable source/destination check:

    * Select your instance.
    * Go to **Networking** tab, click on the network interface.
    * Choose **Actions**, **Change source/dest check**, **Disable**.

**AWS CLI**

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id eni-0abcdef1234567890 \
    --no-source-dest-check \
    --region us-east-1
```

## Step 13: Test connectivity

Complete this step to verify that internet traffic is properly routed to your target instance through the BYOIP addresses.

1. On your target instance, monitor incoming traffic using tcpdump:

```
sudo tcpdump -i any icmp
```

2. From another terminal or computer, test connectivity to your BYOIP IP
   address:

```
ping 203.0.113.10
```

3. Expected results:
   - Ping should succeed and show responses from your BYOIP IP address.
   - tcpdump should show incoming packets for the BYOIP address, similar to:

   ```
   12:34:56.789012 IP 203.0.113.100 > 203.0.113.10: ICMP echo request, id 1234, seq 1, length 64
   12:34:56.789123 IP 203.0.113.10 > 203.0.113.100: ICMP echo reply, id 1234, seq 1, length 64
   ```

   - Traffic should appear to come from external IP addresses, proving the internet gateway ingress routing is delivering internet traffic to your instance.

## Troubleshooting

Use this section to resolve common issues you might encounter when setting up internet gateway ingress routing.

**Traffic not reaching the instance**

- Verify the route table has the correct ENI ID as the target.
- Confirm the BYOIP pool is associated with the internet gateway route table.
- Check that source/destination check is disabled on the instance.
- Ensure security groups allow the traffic type you're testing.

**Route creation fails**

- Verify the BYOIP pool is properly associated with the route table.
- Confirm the destination CIDR is within your BYOIP range.
- Check that the target ENI exists and is attached to a running instance.
- Ensure your BYOIP prefix is between /23 and /28 (prefixes outside this range are not supported).

**Ping/connectivity fails**

- Verify the IP addresses are added to the instance interface.
- Check security groups allow ICMP (for ping) or relevant ports.
- Confirm the instance is in a running state.
- Test from multiple external locations.

## Advanced option: Route server integration for dynamic routing

For environments requiring automatic failover, this feature integrates with VPC Route
Server to:

- **Dynamically update routes** during instance failures.
- **Eliminate manual intervention** for route management.
- **Provide enterprise-grade availability** for critical workloads.

This is particularly important for Telco and IoT use cases where high availability is essential.

###### Note

When using Route Server with multiple BGP peers, be aware that a maximum of 32 BGP peers can advertise the same prefix to the same route table using route server.

For environments requiring dynamic routing, automatic failover, and load distribution
across multiple instances, consider integrating with AWS Route Server. Route Server enables
BGP-based dynamic routing instead of static routes, providing:

- **Dynamic route advertisement** from instances through BGP.
- **Automatic failover** between multiple target instances.
- **Load distribution** across multiple endpoints.
- **Centralized route management** through BGP protocols.

This is an important use case for enterprise deployments where high availability and dynamic routing capabilities are required. For detailed Route Server setup instructions, see the [AWS Route Server documentation](dynamic-routing-route-server.md "dynamic-routing-route-server.md").

## Clean up

To avoid ongoing charges, delete the resources you created in this tutorial:

### Step 1: Terminate EC2 instance

Complete this step to terminate the EC2 instance and stop incurring charges for compute resources.

**AWS console**

1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").
2. In the EC2 console navigation pane, choose **Instances**.
3. Select your instance and choose **Instance state**, **Terminate instance**.
4. Choose **Terminate** to confirm.

**AWS CLI**

```
aws ec2 terminate-instances --instance-ids i-0123456789abcdef0 --region us-east-1
```

### Step 2: Detach internet gateway from VPC

Complete this step to detach and delete the internet gateway from your VPC.

**AWS console**

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc").
2. In the VPC console navigation pane, choose **Internet gateways**.
3. Select your internet gateway and choose **Actions**, **Detach from VPC**.
4. Choose **Detach internet gateway**.
5. After detaching, choose **Actions**, **Delete internet gateway**.
6. Choose **Delete internet gateway**.

**AWS CLI**

```
aws ec2 detach-internet-gateway --internet-gateway-id igw-0123456789abcdef0 --vpc-id vpc-0123456789abcdef0 --region us-east-1

aws ec2 delete-internet-gateway --internet-gateway-id igw-0123456789abcdef0 --region us-east-1
```

### Step 3: Delete VPC

Complete this step to delete the VPC and all associated resources to complete the cleanup process.

**AWS console**

1. In the VPC console, choose **Your VPCs**.
2. Select your VPC and choose **Actions**, **Delete VPC**.
3. Type `delete` to confirm and choose **Delete**.

**AWS CLI**

```
aws ec2 delete-vpc --vpc-id vpc-0123456789abcdef0 --region us-east-1
```

###### Note

Deleting the VPC will also delete associated subnets, route tables, and security groups.

###### Note

Your BYOIP pool remains available for future use and is not deleted as part of this cleanup process.
