

# Prepare for HCX migration

Before you connect VMware HCX to your Amazon Elastic VMware Service environment, check that the HCX VLAN subnet is ready and create the HCX uplink port group. You can do the AWS checks with the console or the AWS CLI. The port group step is in the vSphere Client.

## Before you begin
<a name="hcx-prepare-prereqs"></a>
+ You have chosen private or internet connectivity and meet the HCX requirements. For more information, see [Plan HCX connectivity](plan-hcx-connectivity.md).
+ For internet connectivity, you have associated Elastic IP addresses with the public HCX VLAN subnet. For instructions, see [Configure HCX public internet connectivity](evs-env-hcx-internet-access.md).

## Step 1. Check the status of the HCX VLAN subnet
<a name="check-hcx-config"></a>

Amazon EVS creates a VLAN subnet for HCX as part of every environment deployment. Check that it is ready.

To check the HCX VLAN subnet in the Amazon EVS console or with the AWS CLI, choose the tab for the method that you use.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment.

1. Select the **Networks and connectivity** tab.

1. Under **VLANs**, find the HCX VLAN and check that **State** is **Created**. For internet connectivity, also check that **Public** is **true**.

1. Run the following command with the ID of your environment and the Region that contains your resources.

   ```bash
   aws evs list-environment-vlans --region <region-code> --environment-id <environment-id>
   ```

1. In the output, find the VLAN with a `functionName` of `hcx`. Check that `vlanState` is `CREATED`. For internet connectivity, also check that `isPublic` is `true`.

   The following is an example of the HCX VLAN in the output.

   ```json
   {
     "environmentVlans": [
       {
         "vlanId": 80,
         "cidr": "203.0.113.0/28",
         "availabilityZone": "us-east-2c",
         "functionName": "hcx",
         "subnetId": "subnet-01234a1b2cde1234f",
         "vlanState": "CREATED",
         "stateDetails": "VLAN successfully created",
         "eipAssociations": [
           {
             "associationId": "eipassoc-09876543210abcdef",
             "allocationId": "eipalloc-0123456789abcdef0",
             "ipAddress": "203.0.113.3"
           },
           {
             "associationId": "eipassoc-12345678901abcdef",
             "allocationId": "eipalloc-1234567890abcdef1",
             "ipAddress": "203.0.113.4"
           }
         ],
         "isPublic": true,
         "networkAclId": "acl-0123456789abcdef0"
       }
     ]
   }
   ```

## Step 2. Check that the HCX VLAN subnet has a network ACL
<a name="check-nacl-config"></a>

Check that the HCX VLAN subnet is associated with a network ACL. To create one, see [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md).

**Important**  
Associating an Elastic IP address with a VLAN subnet gives direct internet access to all resources on that subnet. Security groups don’t apply to traffic on Amazon EVS VLAN subnets, so use a network access control list (ACL) to restrict access. For more information, see [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md).

To check the network ACL in the Amazon VPC console or with the AWS CLI, choose the tab for the method that you use.

**Example**  

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc).

1. In the navigation pane, choose **Network ACLs**.

1. Select the network ACL for your VLAN subnets.

1. Select the **Subnet associations** tab.

1. Check that the HCX VLAN subnet is in the list.

1. Run the following command with the HCX VLAN subnet ID in the `Values` filter.

   ```bash
   aws ec2 describe-network-acls --filters "Name=subnet-id,Values=subnet-abcdefg9876543210"
   ```

1. Check that the output returns the correct network ACL.

## Step 3. Check the route table association
<a name="check-hcx-vlan-rtb-association"></a>

Amazon EVS requires that every VLAN subnet is explicitly associated with a route table in your VPC. A VLAN subnet without an explicit association uses the main route table implicitly. In that case, Amazon EVS doesn’t work correctly. For internet connectivity, the public HCX VLAN subnet must be associated with a public route table that has an internet gateway as a target.

To check the route table association in the Amazon VPC console or with the AWS CLI, choose the tab for the method that you use.

**Example**  

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc).

1. In the navigation pane, choose **Route tables**.

1. Choose the route table for your VLAN subnets.

1. Select the **Subnet associations** tab.

1. Under **Explicit subnet associations**, check that all VLAN subnets are in the list.

1. If a VLAN subnet is missing, choose **Edit subnet associations** and add it.

1. Open a terminal session.

1. Check which route table is explicitly associated with a VLAN subnet. Replace the example subnet ID with your own value.

   ```bash
   aws ec2 describe-route-tables \
     --filters "Name=association.subnet-id,Values=subnet-01234a1b2cde1234f"
   ```

1. If no route table is returned, associate the VLAN subnet with a route table. Replace the example route table ID and subnet ID with your own values.

   ```bash
   aws ec2 associate-route-table \
     --route-table-id rtb-0123456789abcdef0 \
     --subnet-id subnet-01234a1b2cde1234f
   ```

For more information, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md).

## Step 4. (Internet connectivity) Check the Elastic IP address associations
<a name="check-hcx-internet-eip-assoc"></a>

For internet connectivity, each HCX network appliance needs an Elastic IP address from the IPAM pool, associated with the public HCX VLAN subnet. You need at least two, one for the HCX Manager and one for the HCX Interconnect (HCX-IX) appliance. HCX internet connectivity fails if fewer than two Elastic IP addresses from the IPAM pool are associated with the public HCX VLAN subnet.

To check the associations in the Amazon EVS console or with the AWS CLI, choose the tab for the method that you use.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment.

1. On the **Networks and connectivity** tab, select the HCX public VLAN.

1. On the **EIP associations** tab, check that the Elastic IP addresses are listed.

1. Run the `list-environment-vlans` command from [Step 1](#check-hcx-config).

1. In the `eipAssociations` array of the HCX VLAN, check that each Elastic IP address is listed. Each entry has these fields:  
 `associationId`   
The ID of the association.  
 `allocationId`   
The allocation ID of the Elastic IP address.  
 `ipAddress`   
The IP address assigned on the VLAN.

To add missing associations, see [Configure HCX public internet connectivity](evs-env-hcx-internet-access.md).

## Step 5. Create a distributed port group with the HCX uplink VLAN ID
<a name="hcx-create-port-group"></a>

In the vSphere Client, do the following:

1. Add a distributed port group to the vSphere Distributed Switch. Follow the steps in [Add a Distributed Port Group](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-networking-8-0/basic-networking-with-vnetwork-distributed-switches/dvport-groups/add-a-distributed-port-group.html) in the Broadcom documentation.

1. For the VLAN setting, enter the HCX VLAN ID that you found in [Step 1](#check-hcx-config).

1. In the failover settings, set `uplink1` as an active uplink and `uplink2` as a standby uplink. This gives active/standby failover.

You have checked the HCX VLAN subnet and created the HCX uplink port group.

## Next step
<a name="hcx-prepare-next"></a>

Turn on the optional HCX features and verify HCX connectivity. For instructions, see [Optimize and verify HCX migration](hcx-optimize-verify.md).