

# Step 1: Create the environment

In Self-deployed mode, environment creation provisions the Amazon Elastic VMware Service VLAN subnets that you specify. It doesn’t deploy VMware Cloud Foundation (VCF) or create hosts. You can create the environment with the Amazon EVS console or the AWS CLI. The steps are the same for hosts with local storage and for diskless hosts.

In Self-deployed mode, you don’t select peers for Amazon VPC Route Server when you create the environment. You configure Border Gateway Protocol (BGP) peering between the NSX Edge Tier-0 gateway and your route server yourself, after you install VCF. For more information, see [Step 5: Configure NSX networking](self-deployed-nsx-edge.md) and [Set up VPC Route Server and on-premises connectivity](network-route-server.md).

**Important**  
You can’t add VLAN subnets or change their CIDR blocks after you create the environment. Size each VLAN subnet before you start. For sizing guidance, see [Plan your VPC and VLAN subnets](plan-network-sizing.md).

Before you begin, complete the AWS account and network prerequisites. For more information, see [Prepare your AWS account](setting-up.md) and [Build the network foundation](network-foundation.md).

If you plan to use VMware HCX over the internet, also complete Part 1 of [Configure HCX public internet connectivity](evs-env-hcx-internet-access.md) first. The public HCX VLAN subnet uses a public CIDR block that you add to the VPC before you create the environment.

To create the environment in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs). Check that the Region selector in the upper right of the console shows the AWS Region where you want to create the environment.

1. In the navigation pane, choose **Environments**.

1. Choose **Create environment**.

1. On the **Configure environment** step, do the following.

   1. Review the ** AWS account requirements** panel to confirm that your account meets the Amazon EVS prerequisites.

   1. (Optional) For **Name**, enter an environment name.

   1. For **VCF version**, choose **Self-deployed**.

   1. Choose **Next**.

1. On the **Configure networks and connectivity** step, do the following.

   1. For **VPC**, choose the VPC that you created.

   1. For **Service access subnet**, choose the private subnet that you created.

   1. (Optional) For **Service access security group - optional**, choose up to two security groups that control communication between the Amazon EVS control plane and your VPC. Amazon EVS uses the default security group if you don’t choose a security group. The security groups that you choose must provide connectivity to the Amazon EVS VLAN subnets.

   1. Under **Management connectivity**, enter CIDR blocks for the Amazon EVS VLAN subnets. Amazon EVS creates these VLAN subnets as part of environment creation.

   1. Under **Expansion VLANs**, enter CIDR blocks for additional Amazon EVS VLAN subnets that you can use to extend your VCF deployment.

   1. Under **Workload/VCF connectivity**, enter the CIDR block for the NSX uplink VLAN.

   1. Choose **Next**.

1. (Optional) On the **Add tags** step, add tags and choose **Next**. Tags that you add to the Amazon EVS environment don’t propagate to underlying AWS resources such as EC2 instances.

1. On the **Review and create** step, review your configuration and choose **Create environment**.

   An information alert on the **Review** page confirms: "Your environment infrastructure will be provisioned now. After creation, add hosts and deploy VCF from the Environment Detail page."

1. Open a terminal session.

1. Run the `aws evs create-environment` command, and specify `--vcf-version SELF_DEPLOYED`.

   In Self-deployed mode, don’t specify the following parameters, because they cause a validation error: `--license-info`, `--hosts`, `--vcf-hostnames`, `--site-id`, and `--connectivity-info`.

   The following example creates an Amazon EVS environment in Self-deployed mode. Replace the example IDs, names, and CIDR blocks with your own values, and size the CIDR blocks for your VPC. The example CIDR blocks assume the 10.10.0.0/16 VPC from the earlier network steps. Each VLAN CIDR block must be inside a CIDR block of your VPC. Replace `<region-code>` with the Region where you want to create the environment.

   ```bash
   aws evs create-environment \
       --environment-name my-self-deployed-env \
       --vpc-id vpc-0abcdef1234567890 \
       --service-access-subnet-id subnet-01234a1b2cde1234f \
       --vcf-version SELF_DEPLOYED \
       --terms-accepted \
       --initial-vlans '{
         "vmkManagement":   { "cidr": "10.10.0.0/24" },
         "vmManagement":    { "cidr": "10.10.1.0/24" },
         "vMotion":         { "cidr": "10.10.2.0/24" },
         "vSan":            { "cidr": "10.10.3.0/24" },
         "vTep":            { "cidr": "10.10.4.0/24" },
         "edgeVTep":        { "cidr": "10.10.5.0/24" },
         "nsxUplink":       { "cidr": "10.10.6.0/24" },
         "hcx":             { "cidr": "10.10.7.0/24" },
         "expansionVlan1":  { "cidr": "10.10.8.0/24" },
         "expansionVlan2":  { "cidr": "10.10.9.0/24" }
       }' \
       --region <region-code>
   ```

   The `vSan` CIDR block is a required input, also for diskless hosts that don’t use vSAN.

1. Don’t run the command again while the environment is being created, because a repeated command can create a second environment. Check the environment state with `aws evs get-environment` until `environmentState` is `CREATED`.

Environment creation takes about 25 to 30 minutes. When the environment reaches the `CREATED` state, you have created the environment and its VLAN subnets.

## Prepare the VLAN subnets for VCF
<a name="self-deployed-create-env-after"></a>

After the environment is in the `CREATED` state, do the following.

1. Associate the Amazon EVS VLAN subnets with the route table that you want them to use. The VCF Installer needs outbound internet access from the VM management VLAN subnet, so use a route table with a default route to your NAT gateway. For more information, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md).

1. Record the VLAN IDs that Amazon EVS assigned. The VLAN IDs can differ for each environment, so read them from your environment. You can find them in the Amazon EVS console on the **Networks and connectivity** tab of your environment, or with the following command. Replace `<environment-id>` with the ID of your environment, and replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs list-environment-vlans \
       --environment-id <environment-id> \
       --query 'environmentVlans[].[functionName,vlanId,cidr]' \
       --output table \
       --region <region-code>
   ```

For how to use the VLAN IDs, see [Step 3: Add hosts](self-deployed-add-hosts.md).

Next step: [Step 2: Create DNS records](self-deployed-host-dns-records.md).