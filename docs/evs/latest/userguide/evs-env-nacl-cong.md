

# Create a network ACL for VLAN subnet traffic

A network access control list (ACL) allows or denies specific inbound or outbound traffic at the subnet level. You use network ACLs to control traffic to and from your Amazon Elastic VMware Service VLAN subnets, because security groups don’t apply to them. You can use the default network ACL of your VPC, or create a custom network ACL with the Amazon VPC console or the AWS CLI.

**Important**  
You must use a network ACL to control traffic to and from Amazon EVS VLAN subnets. If your security groups and network ACLs don’t allow the traffic in the following table, environment deployment fails, and existing environments can have a degraded compliance status.

## Required traffic
<a name="evs-env-nacl-rules"></a>

The following table lists the traffic that your network ACLs must allow.


| Traffic | Protocol and port | Between | 
| --- | --- | --- | 
| DNS queries from Amazon EVS | TCP and UDP 53 | Amazon EVS and the DNS servers in your DHCP option set | 
| HTTPS access from Amazon EVS | TCP 443 (HTTPS) | Amazon EVS and the host management VLAN subnet, and Amazon EVS and the management VLAN subnet | 
| SSH access from Amazon EVS | TCP 22 (SSH) | Amazon EVS and the host management VLAN subnet, and Amazon EVS and the management VLAN subnet | 
| Border Gateway Protocol (BGP) sessions with Amazon VPC Route Server | TCP 179 | The NSX Edge uplink IP addresses and the route server endpoint IP addresses | 
| NFS to Amazon FSx for OpenZFS, for diskless hosts with VMware Cloud Foundation (VCF) 9.x | TCP and UDP 111, 2049, and 20001 to 20003 | The host management VLAN subnet and the subnet of the storage, for example the service access subnet. For more information, see [Security group rules](config-fsx-openzfs-datastore.md#fsx-openzfs-security-group). | 
| NFS to Amazon FSx for NetApp ONTAP | TCP and UDP 111, 635, 2049, 4045, and 4046, and UDP 4049 | The host management VLAN subnet and the subnet of the storage. For more information, see [File system access control with Amazon VPC](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/limit-access-security-groups.html) in the *Amazon FSx for NetApp ONTAP User Guide*. | 
| iSCSI to Amazon FSx for NetApp ONTAP | TCP 3260 | The host management VLAN subnet and the subnet of the storage. | 

The security group that is attached to the route server endpoints must also allow inbound TCP 179.

In Self-deployed mode, your network ACLs must also allow the following traffic, which the VCF installation needs.
+ HTTPS (TCP 443) from the VM management VLAN subnet to the internet through your NAT gateway, so that the VCF Installer can download software from the Broadcom online depot. For more information, see [Create a VPC with subnets and route tables](network-create-vpc.md).
+ DNS (TCP and UDP 53) from the host management VLAN subnet and the VM management VLAN subnet to the DNS servers in your DHCP option set. For example, the DNS servers can be the IP addresses of a Route 53 Resolver inbound endpoint. For more information, see [Configure DNS and NTP with a DHCP option set](network-dhcp-dns-ntp.md).
+ HTTPS (TCP 443) from your access instance to the host management VLAN subnet and the VM management VLAN subnet. This traffic lets you open the VMware Host Client and the VCF Installer. For more information, see [Launch an instance to reach the VPC](network-dhcp-dns-ntp.md#network-access-instance).

Network ACLs are stateless, so you must also allow the return traffic for each rule. For how to allow return traffic on ephemeral ports, see [Ephemeral ports](https://docs.aws.amazon.com/vpc/latest/userguide/nacl-ephemeral-ports.html) in the * Amazon VPC User Guide*.

If you plan to configure VMware Hybrid Cloud Extension (VMware HCX) internet connectivity, your network ACL rules must also allow the inbound and outbound connections that the HCX components need. For the HCX port requirements, see the [VMware HCX User Guide](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11.html) in the Broadcom documentation.

**Important**  
When you associate an Elastic IP address with a VLAN, all resources on that VLAN subnet get direct internet access. Configure network ACLs that restrict access as your security requirements need. We recommend a custom network ACL that is dedicated to the HCX public VLAN, so that its internet-facing rules don’t affect other VLAN subnets.

## Create the network ACL and its rules
<a name="evs-env-nacl-steps"></a>

You can create the network ACL in the Amazon VPC console or with the AWS CLI. Choose the tab for the method that you use.

**Example**  

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc) and choose **Network ACLs** in the navigation pane.

1. Choose **Create network ACL**.

1. Enter a name, choose your VPC, and then choose **Create network ACL**.

1. Select the network ACL, choose the **Inbound rules** tab, and then choose **Edit inbound rules**.

1. Add a rule for each row in the required traffic table and for any traffic that your workloads need, and then choose **Save changes**.

1. Choose the **Outbound rules** tab, choose **Edit outbound rules**, add the matching outbound rules and return traffic rules, and then choose **Save changes**.

1. Create the network ACL and store its ID. If `$VPC_ID` isn’t set in your shell, replace it in the following commands with the ID of your VPC.

   ```bash
   NACL_ID=$(aws ec2 create-network-acl \
     --vpc-id $VPC_ID \
     --tag-specifications 'ResourceType=network-acl,Tags=[{Key=Name,Value=evs-vlan-nacl}]' \
     --query 'NetworkAcl.NetworkAclId' \
     --output text)
   ```

1. Add an entry for each rule. This example allows inbound HTTPS from the VPC CIDR block. Replace the example addresses with your own values.

   ```bash
   aws ec2 create-network-acl-entry \
     --network-acl-id $NACL_ID \
     --ingress \
     --rule-number 100 \
     --protocol tcp \
     --port-range From=443,To=443 \
     --cidr-block 10.10.0.0/16 \
     --rule-action allow
   ```

1. Repeat the previous step for each inbound rule. For outbound rules, use `--egress` instead of `--ingress`.

1. Verify the rules.

   ```bash
   aws ec2 describe-network-acls \
     --network-acl-ids $NACL_ID \
     --query 'NetworkAcls[0].Entries'
   ```

   The output includes the entries that you added, with their rule numbers, protocols, port ranges, and actions.

You have created a network ACL with the rules that the Amazon EVS VLAN subnets need. For more information, see [Create a network ACL for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-network-acl.html) in the * Amazon VPC User Guide*.

## Associate the network ACL with the VLAN subnets
<a name="evs-env-nacl-associate"></a>

Amazon EVS creates the VLAN subnets when you create the environment. Until you change the association, the VLAN subnets use the default network ACL of the VPC. In EVS-deployed mode with HCX internet connectivity, you choose the network ACL for the HCX VLAN when you create the environment. For more information, see [Create an environment](getting-started-create-env.md).

After you create the environment, associate your network ACL with the VLAN subnets in the Amazon VPC console or with the AWS CLI. Choose the tab for the method that you use.

**Example**  

1. In the Amazon VPC console, choose **Network ACLs** and select your network ACL.

1. Choose the **Subnet associations** tab, and then choose **Edit subnet associations**.

1. Select the Amazon EVS VLAN subnets, and then choose **Save changes**.

1. Find the current network ACL association ID for a VLAN subnet. Replace the example subnet ID with the ID of your VLAN subnet.

   ```bash
   aws ec2 describe-network-acls \
     --filters Name=association.subnet-id,Values=subnet-01234a1b2cde1234f \
     --query 'NetworkAcls[0].Associations[?SubnetId==`subnet-01234a1b2cde1234f`].NetworkAclAssociationId' \
     --output text
   ```

1. Replace the association with your network ACL. Replace the example association ID with the ID that the previous command returns. If `$NACL_ID` isn’t set in your shell, replace it in the following commands with the ID of your network ACL.

   ```bash
   aws ec2 replace-network-acl-association \
     --association-id aclassoc-0123456789abcdef0 \
     --network-acl-id $NACL_ID
   ```

1. Repeat these steps for each VLAN subnet.

Your VLAN subnets now use the network ACL that you created.

To check which network ACL a VLAN subnet uses, see [Troubleshoot networking](troubleshoot-networking.md).

Next, create the environment in your deployment mode. For VCF 9.x, see [Deploy in Self-deployed mode](getting-started-self-deployed.md). For VCF 5.2.x, see [Deploy in EVS-deployed mode](evs-deployed-overview.md). After you create the environment, associate the VLAN subnets with a route table. For instructions, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md).