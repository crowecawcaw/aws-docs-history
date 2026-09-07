

# Quick VPC Setup (1 minute)
<a name="vpc-step1"></a>

Complete the following steps to quickly create a dedicated VPC for WorkSpaces Secure Browser with public and private subnets for internet access. If you want to use an existing VPC, see [VPC requirements for Amazon WorkSpaces Secure Browser](vpc-reqs.md) to verify it meets the requirements.

**Note**  
Make sure you're in your desired AWS Region. You can change the region in the console if needed.

**To quickly set up a VPC**

1. Open the VPC creation wizard: [Create VPC with resources](https://console.aws.amazon.com/vpcconsole/home#CreateVpc:createMode=vpcWithResources). Keep all settings as default unless specified below:
   + For **Resource to create**, select **VPC and more**.
   + For **Name tag**, select **auto-generate** and enter a descriptive name for your VPC (e.g., **WSB-VPC**).
   + For **IPv4 CIDR block**, by default, the VPC uses **10.0.0.0/16**. You can specify a different IPv4 CIDR block if needed.
   + For **Tenancy**, select **Default** (VPCs with dedicated tenancy are not supported).
   + For **Number of Availability Zones (AZs)**, select **2**.
     + Expand **Customize AZs** and select 2 different Availability Zones that are supported by WorkSpaces Secure Browser. For the list of supported AZs, see [Supported Availability Zones for Amazon WorkSpaces Secure Browser](availability-zones.md).
   + For **Number of public subnets**, select **2**.
   + For **Number of private subnets**, select **2**.
   + For **Subnet CIDR blocks**, if you need to customize the CIDR blocks in your subnets, expand **Customize subnets CIDR blocks**. Ensure each subnet has sufficient IP addresses for your expected traffic.
   + For **NAT gateways**, select **Regional** to enable internet access for private subnets across all Availability Zones.
   + For **VPC endpoints**, select **None**. If you need direct S3 access without going through the NAT gateway, select **S3 Gateway**.
   + For **DNS options**, keep **DNS options** enabled (default) to ensure proper name resolution within your VPC.

1. Review the Preview pane, then choose **Create VPC**.

**Note**  
Additional charges apply for NAT gateways and VPC endpoints. For more information, see the [VPC pricing page](https://aws.amazon.com/vpc/pricing/).