

# Tutorial: Plan VPC IP address space for subnet IP allocations
<a name="tutorials-subnet-planning"></a>

Complete this tutorial to plan the VPC IP address space for allocating IP addresses to VPC subnets and monitor IP address-related metrics at the subnet and VPC level.

**Note**  
This tutorial covers allocating private IPv4 address space in a private IPAM scope to VPCs and subnets. You can also complete this tutorial using an IPv6 CIDR range by creating the VPC with an Amazon-provided IPv6 CIDR block option on the VPC console.

Planning VPC IP address space for subnets enables you to do the following:
+ **Plan and organize your VPC's IP addresses for allocation to subnets**: You can divide VPC IP address space into smaller CIDR blocks and provision those CIDR blocks to subnets with different business needs, such as if you're running workloads in development or production subnets.
+ **Simplify IP address allocations for VPC subnets**: Once your VPC's address space is planned and organized, you can choose a netmask length rather than manually inputting a CIDR. For example, if a developer is creating a subnet for hosting development workloads, they need to choose a pool and a netmask length for the subnet and IPAM will automatically allocate the CIDR block to your subnet.

The following example shows the hierarchy of the pool and resource structure that you will create with this tutorial:
+ Private scope
  + Resource planning pool (10.0.0.0/20)
    + Dev subnet pool (10.0.0.0/24)
      + Dev subnet (10.0.0.0/28)
    + Prod subnet pool (10.0.0.1/24)
      + Prod subnet (10.0.0.16/28)

**Important**  
The resource planning pool can be used to allocate CIDRs to subnets or it can be used as a source pool in which you can create other pools. In this tutorial, we use the resource planning pool as a source pool for subnet pools.
You can create multiple resource planning pools using the same VPC if the VPC has more than one CIDR provisioned to it. For example, if a VPC has two CIDRs assigned to it, you can create two resource planning pools, one from each CIDR. Each CIDR can be assigned to one pool at a time.

## Step 1: Create a VPC
<a name="tutorials-subnet-planning-1"></a>

Complete the steps in this section to create a VPC to be used for subnet IP address planning. For more information about the IAM permissions that are required to create VPCs, see [Amazon VPC policy examples](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-policy-examples.html) in the *Amazon VPC User Guide*.

**Note**  
You can use an existing VPC rather than creating a new one, but this tutorial focuses on the scenario where the VPC is configured with a manually-allocated CIDR block, not an IPAM-allocated automatically CIDR block. 

**To create a VPC**

1. Using the IPAM admin account, open the VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. Choose **Create VPC**.

1. Enter a name for the VPC, such as tutorial-vpc.

1. Choose **IPv4 CIDR manual input** and enter an IPv4 CIDR block. In this tutorial, we use 10.0.0.0/20.

1. Skip the option to add an IPv6 CIDR block.

1. Choose **Create VPC**.

1. Using the IPAM admin account, open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/).

1. Choose **Resources** in the left navigation pane.

1. Wait for the VPC that you created to appear. This takes some time to happen and you may need to refresh the window to see it appear. The VPC must be discovered by IPAM before you continue to the next step.

## Step 2: Create a resource planning pool
<a name="tutorials-subnet-planning-2"></a>

Complete the steps in this section to create a resource planning pool.

**To create a resource planning pool**

1. Using the IPAM admin account, open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/).

1. In the navigation pane, choose **Pools**.

1. Choose the private scope.

1. Choose **Create pool**.

1. Under **IPAM scope**, leave the private scope selected.

1. (Optional) Add a **Name tag** for the pool, such as "Resource-planning-pool".

1. Under **Source**, choose **IPAM scope**. 

1. Under **Resource planning**, choose **Plan IP space within a VPC** and choose the VPC you created in the previous step. The VPC is the resource used to provision CIDRs to the resource planning pool.

1. Under **CIDRs to provision**, choose the VPC CIDR to provision for the resource pool. The CIDR you provision to the resource planning pool must match the CIDR provisioned to the VPC. In this tutorial, we use 10.0.0.0/20.

1. Choose **Create pool**.

1. Once the pool is created, choose the **CIDR** tab to see the state of the provisioned CIDR. Refresh the page and wait for the CIDR state to change from *Pending-provision* to *Provisioned* before you go to the next step.

## Step 3: Create subnet pools
<a name="tutorials-subnet-planning-3"></a>

Complete the steps in this section to create two subnet pools that will be used for allocating IP space to subnets.

**To create subnet pools**

1. Using the IPAM admin account, open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/).

1. In the navigation pane, choose **Pools**.

1. Choose the private scope.

1. Choose **Create pool**.

1. Under **IPAM scope**, leave the private scope selected.

1. (Optional) Add a **Name tag** for the pool, such as "dev-subnet-pool".

1. Under **Source**, choose **IPAM pool** and select the resource planning pool you created in Step 3. The address family, Resource planning configuration, and Locale are automatically inherited from the source pool.

1. Under **CIDRs to provision**, choose the CIDR to provision for the subnet pool. In this tutorial, we use 10.0.0.0/24.

1. Choose **Create pool**.

1. Once the pool is created, choose the **CIDR tab** to see the state of the provisioned CIDR. Refresh the page and wait for the CIDR state to change from *Pending-provision* to *Provisioned* before you go to the next step.

1. Repeat this process to create another subnet called "prod-subnet-pool".

At this point, if you want to make this subnet pool available to other AWS accounts, you can share the subnet pool. For instructions on how to do that, see [Share an IPAM pool using AWS RAM](share-pool-ipam.md). Then return here to complete the tutorial.

## Step 4: Create subnets
<a name="tutorials-subnet-planning-4"></a>

Complete these steps to create two subnets.

**To create subnets**

1. Using the appropriate account, open the VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. Choose **Subnets** > **Create subnet**.

1. Choose the VPC you created at the start of this tutorial.

1. Enter a name for the subnet, such as "tutorial-subnet".

1. (optional) Choose an **Availability Zone**.

1. Under **IPv4 CIDR block**, choose **IPAM-allocated IPV4 CIDR block** and choose the dev subnet pool and a /28 netmask.

1. Choose **Create subnet**.

1. Repeat this process to create another subnet. This time choose the prod subnet pool and a /28 netmask.

1. Return to the IPAM console and choose **Resources** in the left navigation pane.

1. Look for the subnet pools you created and wait for the subnets that you created to appear beneath it. This takes some time to happen and you may need to refresh the window to see it appear.

The tutorial is complete. You can create additional subnet pools as needed or you can launch in EC2 instance into one of the subnets.

IPAM publishes metrics related to IP address usage in subnets. You can set CloudWatch alarms on the SubnetIPUsage metric, thereby allowing you to take action when IP utilization thresholds are breached. If, for example, you have a /24 CIDR (256 IP addresses) assigned to a subnet and you want to be notified when 80% of the IPs have been utilized, you can set up a CloudWatch alarm to alert you when this threshold is reached. For more information on creating an alarm for subnet IP usage, see [Quick tip for creating alarms](cloudwatch-ipam-res-util.md#cloudwatch-ipam-res-util-tip).

## Step 5: Cleanup
<a name="tutorials-subnet-planning-5"></a>

Complete these steps to delete the resources you created with this tutorial.

**To clean up the resources**

1. Using the IPAM admin account, open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/).

1. In the navigation pane, choose **Pools**.

1. Choose the private scope.

1. Choose the resource planning pool and choose **Action** > **Delete**.

1. Select **Cascade delete**. The resource planning pool and the subnet pools will be deleted. This will not delete the subnets themselves. They will stay with CIDRs provisioned to them, though the CIDRs will no longer be from an IPAM pool.

1. Choose **Delete**.

1. [Delete the subnets](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-deleting.html).

1. [Delete the VPC](https://docs.aws.amazon.com/vpc/latest/userguide/delete-vpc.html).

Cleanup is complete.