

# Configure HCX public internet connectivity

You can migrate workloads to Amazon Elastic VMware Service with VMware HCX over the internet by associating Elastic IP addresses with the public HCX VLAN subnet. You create the IPAM pool, the Elastic IP addresses and the VPC CIDR block before you create the environment, and associate the addresses after. You can use the consoles or the AWS CLI.

**Important**  
Associating an Elastic IP address with a VLAN subnet gives direct internet access to all resources on that subnet. Security groups don’t apply to traffic on Amazon EVS VLAN subnets, so use a network access control list (ACL) to restrict access. For more information, see [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md).

## Before you begin
<a name="evs-env-hcx-internet-access-prereqs"></a>
+ Choose internet connectivity and review the CIDR and Elastic IP address rules in [Plan HCX connectivity](plan-hcx-connectivity.md).
+ Check that your IPAM quota for the netmask length of Amazon-provided contiguous public IPv4 CIDR blocks allows a /28. For more information, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html).

## Rules for the public HCX VLAN subnet
<a name="evs-env-hcx-internet-access-considerations-operation"></a>

For the CIDR block and Elastic IP address rules, see [CIDR and Elastic IP address rules for internet connectivity](plan-hcx-connectivity.md#plan-hcx-connectivity-rules).

## Part 1. Before you create the environment
<a name="hcx-internet-config"></a>

Do these steps before you create the environment. You can’t change the VLAN CIDR blocks after you create it.

After you create the environment, continue with [Part 2](#getting-started-eip-assoc).

### Step 1. Create an IPAM
<a name="evs-env-hcx-internet-access-create-ipam"></a>

Follow the steps in [Create an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html) in the *Amazon VPC IP Address Manager User Guide*.

You have created an IPAM.

**Note**  
You can use the IPAM Free Tier for these resources. You still pay for other AWS services that you use with IPAM, such as NAT gateways and public IPv4 addresses beyond the free tier. For more information, see the [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing).

Amazon EVS doesn’t support private IPv6 Global Unicast Address (GUA) CIDR blocks.

### Step 2. Create a public IPv4 IPAM pool
<a name="evs-env-hcx-internet-access-create-pool"></a>

The AWS CLI commands in Steps 2 to 4 store values in the shell variables `SCOPE_ID`, `POOL_ID`, and `CIDR_BLOCK`. Run them in the same terminal session.

To create the pool in the IPAM console or with the AWS CLI, choose the tab for the method that you use.

**Example**  

1. Open the [IPAM console](https://console.aws.amazon.com/ipam).

1. In the navigation pane, choose **Pools**.

1. Choose the public scope. For more information about scopes, see [How IPAM works](https://docs.aws.amazon.com/vpc/latest/ipam/how-it-works-ipam.html).

1. Choose **Create pool**.

1. (Optional) Add a **Name** tag and a **Description** for the pool.

1. Under **Address family**, choose **IPv4**.

1. Under **Resource planning**, keep **Plan IP space within the scope** selected.

1. Under **Locale**, choose the AWS Region of your VPC.

1. Under **Service**, choose **EC2 (EIP/VPC)**. CIDR blocks from this pool are advertised for Elastic IP addresses.

1. Under **Public IP source**, choose **Amazon-owned**.

1. Under **CIDRs to provision**, choose **Add Amazon-owned public CIDR**, and choose a netmask length. The minimum is /28.

1. Choose **Create pool**.

1. Get the public scope ID of your IPAM.

   ```bash
   SCOPE_ID=$(aws ec2 describe-ipam-scopes \
     --filters Name=ipam-scope-type,Values=public \
     --query 'IpamScopes[0].IpamScopeId' \
     --output text)
   ```

1. Create a pool in the public scope. Use the Region of your VPC for `--locale`.

   ```bash
   aws ec2 create-ipam-pool \
     --ipam-scope-id $SCOPE_ID \
     --address-family ipv4 \
     --no-auto-import \
     --locale {{region-code}} \
     --description "Public IPv4 pool for HCX" \
     --tag-specifications 'ResourceType=ipam-pool,Tags=[{Key=Name,Value=evs-hcx-public-pool}]' \
     --public-ip-source amazon \
     --aws-service ec2
   ```

1. Store the pool ID.

   ```bash
   POOL_ID=$(aws ec2 describe-ipam-pools \
     --filters Name=tag:Name,Values=evs-hcx-public-pool \
     --query 'IpamPools[0].IpamPoolId' \
     --output text)
   ```

1. Provision a CIDR block from the pool. The minimum netmask length is /28.

   ```bash
   aws ec2 provision-ipam-pool-cidr \
     --ipam-pool-id $POOL_ID \
     --netmask-length 28
   ```

You have created a public IPv4 IPAM pool.

### Step 3. Allocate Elastic IP addresses from the IPAM pool
<a name="evs-env-hcx-internet-access-allocate-eip"></a>

**Important**  
Enter each address manually. If you let IPAM choose the address, IPAM can allocate an address that Amazon EVS reserves, and the association with the VLAN subnet then fails. Don’t allocate the first two addresses or the last address of the CIDR block.

To allocate the addresses in the Amazon VPC console or with the AWS CLI, choose the tab for the method that you use.

**Example**  

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc).

1. In the navigation pane, choose **Elastic IPs**.

1. Choose **Allocate Elastic IP address**.

1. Select **Allocate using an IPv4 IPAM pool**, and select the Amazon-owned public IPv4 pool that you created.

1. Under **Allocate IPAM method**, choose **Manually input address within the IPAM pool**.

1. Enter the address to allocate, and choose **Allocate**.

1. Repeat for each address that you need. You need at least two, plus one for each HCX network appliance.

1. Allocate each address from the pool. Use the pool ID from [Step 2](#evs-env-hcx-internet-access-create-pool) (`POOL_ID`). Replace the example addresses with addresses from your CIDR block.

   ```bash
   aws ec2 allocate-address \
     --domain vpc \
     --tag-specifications 'ResourceType=elastic-ip,Tags=[{Key=Name,Value=evs-hcx-manager-eip}]' \
     --ipam-pool-id $POOL_ID \
     --address xx.xx.xxx.3
   
   aws ec2 allocate-address \
     --domain vpc \
     --tag-specifications 'ResourceType=elastic-ip,Tags=[{Key=Name,Value=evs-hcx-ix-eip}]' \
     --ipam-pool-id $POOL_ID \
     --address xx.xx.xxx.4
   
   aws ec2 allocate-address \
     --domain vpc \
     --tag-specifications 'ResourceType=elastic-ip,Tags=[{Key=Name,Value=evs-hcx-ne-eip}]' \
     --ipam-pool-id $POOL_ID \
     --address xx.xx.xxx.5
   ```

You have allocated the Elastic IP addresses.

### Step 4. Add the public CIDR block to the VPC
<a name="evs-env-hcx-internet-access-add-cidr"></a>

Amazon EVS uses this CIDR block to connect VMware HCX to your network.

**Important**  
You must enter the CIDR block manually. Amazon EVS doesn’t support an IPAM-allocated CIDR block for the VPC, and one can cause the Elastic IP address association to fail.

To add the CIDR block in the Amazon VPC console or with the AWS CLI, choose the tab for the method that you use.

**Example**  

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc).

1. In the navigation pane, choose **Your VPCs**.

1. Select your VPC, and choose **Actions**, **Edit CIDRs**.

1. Choose **Add new IPv4 CIDR**.

1. Select **IPv4 CIDR manual input**.

1. Enter the CIDR block from the public IPAM pool.

1. Get the CIDR block that you provisioned in the pool. Use the pool ID from [Step 2](#evs-env-hcx-internet-access-create-pool) (`POOL_ID`).

   ```bash
   CIDR_BLOCK=$(aws ec2 get-ipam-pool-cidrs \
     --ipam-pool-id $POOL_ID \
     --query 'IpamPoolCidrs[0].Cidr' \
     --output text)
   ```

1. Add the CIDR block to your VPC. Replace `<vpc-id>` with the ID of your VPC.

   ```bash
   aws ec2 associate-vpc-cidr-block \
     --vpc-id <vpc-id> \
     --cidr-block $CIDR_BLOCK
   ```

You have added the public CIDR block to your VPC.

### Step 5. Create the environment
<a name="evs-env-hcx-internet-access-create-env"></a>

When you create the environment, use the public CIDR block for the HCX uplink VLAN subnet. For Self-deployed environments, see [Step 1: Create the environment](self-deployed-create-env.md). For EVS-deployed environments, see [Create an environment](getting-started-create-env.md).

## Part 2. After you create the environment
<a name="getting-started-eip-assoc"></a>

After you create the environment, associate the Elastic IP addresses with the public HCX VLAN subnet.

### Associate Elastic IP addresses with the HCX VLAN subnet
<a name="evs-env-hcx-internet-access-associate-eip"></a>

Associate one Elastic IP address from the IPAM pool for each HCX appliance. HCX internet connectivity fails if fewer than two Elastic IP addresses from the IPAM pool are associated with the public HCX VLAN subnet.

To associate the addresses in the Amazon EVS console or with the AWS CLI, choose the tab for the method that you use.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment.

1. On the **Networks and connectivity** tab, select the HCX public VLAN.

1. Choose **Associate EIP to VLAN**.

1. Select the Elastic IP addresses to associate.

1. Choose **Associate EIPs**.

1. On the **EIP associations** tab, check that the addresses are listed.

1. Run the `associate-eip-to-vlan` command with these values:  
 `environment-id`   
The ID of your environment.  
 `vlan-name`   
Must be `hcx`.  
 `allocation-id`   
The allocation ID of the Elastic IP address.  

   ```bash
   aws evs associate-eip-to-vlan \
     --environment-id <environment-id> \
     --vlan-name "hcx" \
     --allocation-id "eipalloc-0429268f30c4a34f7"
   ```
The command returns the VLAN with the new association in the `eipAssociations` array:  

   ```json
   {
       "vlan": {
           "vlanId": 80,
           "cidr": "203.0.113.0/28",
           "functionName": "hcx",
           "vlanState": "CREATED",
           "eipAssociations": [
               {
                   "associationId": "eipassoc-09e966faad7ecc58a",
                   "allocationId": "eipalloc-0429268f30c4a34f7",
                   "ipAddress": "203.0.113.2"
               }
           ],
           "isPublic": true
       }
   }
   ```
Note the `associationId`. You need it to disassociate the address.

1. Repeat the command for each Elastic IP address.

You have associated the Elastic IP addresses with the public HCX VLAN subnet. Next, check the environment before you connect HCX. See [Prepare for HCX migration](hcx-prepare.md).

## Disassociate an Elastic IP address
<a name="evs-env-hcx-internet-access-disassociate-eip"></a>

You can disassociate Elastic IP addresses from the public HCX VLAN subnet after deployment.

**Important**  
Disassociating an Elastic IP address can cause a loss of internet connectivity for the HCX appliances that use the public HCX VLAN subnet.

To disassociate an address in the Amazon EVS console or with the AWS CLI, choose the tab for the method that you use.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment.

1. On the **Networks and connectivity** tab, select the HCX public VLAN.

1. Choose **Disassociate EIP from VLAN**.

1. Select the Elastic IP addresses to disassociate.

1. Choose **Disassociate EIPs**.

1. On the **EIP associations** tab, check that the addresses are no longer listed.

1. Run the `disassociate-eip-from-vlan` command with these values:  
 `environment-id`   
The ID of your environment.  
 `vlan-name`   
Must be `hcx`.  
 `association-id`   
The ID of the association to remove.  

   ```bash
   aws evs disassociate-eip-from-vlan \
     --environment-id <environment-id> \
     --vlan-name "hcx" \
     --association-id "eipassoc-09e966faad7ecc58a"
   ```

1. In the output, check that the association is no longer in the `eipAssociations` array.

You have disassociated the Elastic IP addresses from the public HCX VLAN subnet.

To release the Elastic IP addresses and delete the IPAM resources when you no longer need them, see [Clean up network resources](cleanup.md).