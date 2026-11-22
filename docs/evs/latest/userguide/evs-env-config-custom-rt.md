

# Associate VLAN subnets with a route table

After your environment deploys, you must explicitly associate each Amazon Elastic VMware Service VLAN subnet with a route table in your VPC. NSX connectivity fails if your VLAN subnets are not explicitly associated with a VPC route table. You can use the Amazon VPC console or the AWS CLI.

## Why explicit association is required
<a name="evs-env-config-custom-rt-why"></a>

During environment deployment, the Amazon EVS VLAN subnets are implicitly associated with the VPC main route table. That is why the main route table must route to dependent services such as DNS and on-premises systems while you create the environment. For more information, see [Create a VPC with subnets and route tables](network-create-vpc.md).

Amazon EVS supports a custom route table only after the environment is created. The route table that you associate lets AWS resources communicate with virtual machines on NSX network segments. Route server propagation in Amazon VPC Route Server also needs it, because Border Gateway Protocol (BGP) route advertisement fails if a propagated route table has no explicit subnet association.

We recommend that you associate the VLAN subnets with a custom route table, because it gives you granular control over routing for specific subnets and gateways. For steps to create one, see [Create a route table for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc-route-table.html) in the * Amazon VPC User Guide*.

## Associate the VLAN subnets
<a name="getting-started-associate-vlans"></a>

You can associate the VLAN subnets in the Amazon VPC console or with the AWS CLI. Choose the tab for the method that you use.

**Example**  

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc).

1. In the navigation pane, choose **Route tables**.

1. Choose the route table that you want to associate with the Amazon EVS VLAN subnets. If you created a public VLAN for VMware Hybrid Cloud Extension (VMware HCX), associate the HCX public VLAN subnet with a public route table that routes to an internet gateway.

1. Choose the **Subnet associations** tab.

1. Under **Explicit subnet associations**, choose **Edit subnet associations**.

1. Select all of the Amazon EVS VLAN subnets.

1. Choose **Save associations**.

1. Verify that the VLAN subnets appear under **Explicit subnet associations**.

1. Identify the Amazon EVS VLAN subnet IDs in your VPC. If `$VPC_ID` isn’t set in your shell, replace it in the following commands with the ID of your VPC.

   ```bash
   aws ec2 describe-subnets \
     --filters Name=vpc-id,Values=$VPC_ID \
     --query 'Subnets[].[SubnetId,CidrBlock]' \
     --output table
   ```

1. Associate each VLAN subnet with the route table. If you created a public HCX VLAN, associate the HCX public VLAN subnet with a public route table that routes to an internet gateway. Replace the example route table ID and subnet ID with your own values.

   ```bash
   aws ec2 associate-route-table \
     --route-table-id rtb-0123456789abcdef0 \
     --subnet-id subnet-01234a1b2cde1234f
   ```

1. Verify the associations.

   ```bash
   aws ec2 describe-route-tables \
     --route-table-ids rtb-0123456789abcdef0 \
     --query 'RouteTables[0].Associations[].SubnetId'
   ```

   The output lists the IDs of the VLAN subnets that you associated.

You have explicitly associated the VLAN subnets with a route table.

Next, return to your deployment path.
+ In Self-deployed mode, record the VLAN IDs as described at the end of [Step 1: Create the environment](self-deployed-create-env.md), and then continue with [Step 2: Create DNS records](self-deployed-host-dns-records.md).
+ In EVS-deployed mode, continue with the remaining tasks in [Next steps](verify-env-creation.md#verify-env-evs-deployed-next).

If you connect on premises through a transit gateway, update the transit gateway route tables next. For more information, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md). For connectivity issues, see [Troubleshoot networking](troubleshoot-networking.md).