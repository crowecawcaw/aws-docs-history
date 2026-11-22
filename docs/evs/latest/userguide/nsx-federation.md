

# Set up NSX Federation

With VMware NSX Federation, you can manage networking and security for several NSX sites from one Global Manager. You can use NSX Federation with Amazon Elastic VMware Service for disaster recovery and multi-site networking across AWS Regions, Availability Zones, and on-premises sites.

For the supported VMware Cloud Foundation (VCF) versions and conditions, see [VCF feature support on Amazon EVS](vcf-feature-support.md). For an example architecture, see [Amazon EVS with NSX Federation for disaster recovery and multi-site networking](https://aws.amazon.com/blogs/migration-and-modernization/amazon-evs-with-nsx-federation-for-disaster-recovery-and-multi-site-networking/) on the AWS blog.

## How NSX Federation fits an Amazon EVS environment
<a name="nsx-federation-design"></a>

Keep the following in mind when you design for NSX Federation.
+ An Amazon EVS environment runs in one Availability Zone. Its VLAN subnets sit in that Availability Zone. You can’t stretch the underlay network across environments. Federation connects separate environments or sites at the NSX layer. For more information, see [VPC and subnets](plan-network-supported.md#plan-network-supported-vpc).
+ Amazon EVS provides expansion VLAN subnets for VCF functions such as NSX Federation. You choose their CIDR blocks when you create the environment, and you can’t add or resize VLAN subnets later. For sizing, see [Plan your VPC and VLAN subnets](plan-network-sizing.md).
+ For stateful failover, NSX Federation uses Active/Standby Tier-0 gateways.
+ To add a site, you register it with the Global Manager.

## Before you begin
<a name="nsx-federation-prereqs"></a>
+ You have an Amazon EVS environment for each Amazon EVS site, with expansion VLAN subnets sized for Federation.
+ Your sites can reach each other. For the connectivity options of an Amazon EVS VPC, see [Supported network configurations](plan-network-supported.md).
+ You have read the NSX Federation requirements in the Broadcom documentation for your NSX version. For NSX 4.2, start with the [VMware NSX Installation Guide](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/installation-guide.html).

## Set up NSX Federation
<a name="nsx-federation-procedure"></a>

To set up Federation in NSX, follow the NSX Federation steps in the Broadcom documentation for the NSX version in your environment.