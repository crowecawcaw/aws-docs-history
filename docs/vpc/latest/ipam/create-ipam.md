# Create an IPAM

Follow the steps in this section to create your IPAM. If you have delegated an IPAM
administrator, these steps should be completed by the IPAM account.

###### Important

When you create an IPAM, you will be asked to allow IPAM to replicate data from source
accounts into an IPAM delegate account. To integrate IPAM with AWS Organizations, IPAM
needs your permission to replicate resource and IP usage details across accounts (from
member accounts to the delegated IPAM member account) and across AWS Regions (from
operating Regions to the home Region of your IPAM). For single account IPAM users, IPAM
needs your permission to replicate resource and IP usage details across operating
Regions to the home Region of your IPAM.

When you create the IPAM, you choose the AWS Regions where the IPAM is allowed to manage
IP address CIDRs. These AWS Regions are called _operating
Regions_. IPAM discovers and monitors resources only in the AWS Regions that
you select as operating Regions. IPAM doesn't store any data outside of the operating
Regions that you select.

The following example hierarchy shows how the AWS Regions that you assign when you
create the IPAM will impact the Regions that will be available for pools that you create
later.

- **IPAM operating in AWS Region 1 and AWS Region 2**

      + Private scope




      	- Top-level IPAM pool




      		* Regional IPAM pool in **AWS Region
      		 2**





      			+ Development pool




      				- Allocation for a VPC in **AWS Region 2**

  You can only create one IPAM. For more information about increasing quotas related to
  IPAM, see [Quotas for your IPAM](quotas-ipam.md "quotas-ipam.md").

AWS Management Console

###### To create an IPAM

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the AWS Management Console, choose the AWS Region in which you
   want to create the IPAM. Create the IPAM in your main Region of
   operations.
3. On the service home page, choose **Create IPAM**.
4. Select **Allow Amazon VPC IP Address Manager to
   replicate data from source account(s) into the IPAM delegate
   account**. If you do not select this option, you cannot
   create an IPAM.
5. Choose an **IPAM tier**. For more information about
   the features available in each tier and the costs associated with the
   tiers, see the IPAM tab on the [Amazon VPC
   pricing page](https://aws.amazon.com//vpc/pricing/ "https://aws.amazon.com//vpc/pricing/").
6. Under **Operating regions**, select the AWS Regions
   in which this IPAM can manage and discover resources. The AWS Region
   in which you are creating your IPAM is selected as one of the operating
   Regions by default. For example, if you’re creating this IPAM in AWS
   Region `us-east-1` but you want to create Regional IPAM pools later that
   provide CIDRs to VPCs in `us-west-2`, select `us-west-2` here. If you forget
   an operating Region, you can return at a later time and edit your IPAM
   settings.

###### Note

If you are creating an IPAM in the Free Tier, you can select multiple operating Regions for
your IPAM, but the only IPAM feature that will be available across
operating Regions is [Public
IP insights](view-public-ip-insights.md "view-public-ip-insights.md"). You cannot use other features in the Free
Tier, like BYOIP, across the IPAM's operating Regions. You can only
use them in the IPAM's home Region. To use all IPAM features across
operating Regions, [create an IPAM in
the Advanced Tier](mod-ipam-tier.md "mod-ipam-tier.md"). 7. Choose if you want to enable **Private IPv6 GUA
CIDRs**. For more information about this option, see [Enable provisioning private IPv6 GUA CIDRs](enable-prov-ipv6-gua.md "enable-prov-ipv6-gua.md"). 8. Choose if you want to enable **Metering mode**. For
more information about this option, see [Enable cost distribution](ipam-enable-cost-distro.md "ipam-enable-cost-distro.md"). 9. Choose **Create IPAM**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to create, modify, and view details related to your IPAM:

1. Create the IPAM: [create-ipam](../../../cli/latest/reference/ec2/create-ipam.md "../../../cli/latest/reference/ec2/create-ipam.md")
2. View the IPAM that you've created: [describe-ipams](../../../cli/latest/reference/ec2/describe-ipams.md "../../../cli/latest/reference/ec2/describe-ipams.md")
3. View the scopes that are created automatically: [describe-ipam-scopes](../../../cli/latest/reference/ec2/describe-ipam-scopes.md "../../../cli/latest/reference/ec2/describe-ipam-scopes.md")
4. Modify an existing IPAM: [modify-ipam](../../../cli/latest/reference/ec2/modify-ipam.md "../../../cli/latest/reference/ec2/modify-ipam.md")

When you have completed these steps, IPAM has done the following:

- Created your IPAM. You can see the IPAM and the currently selected operating Regions by
  choosing IPAMs in the left navigation pane of the console.
- Created one private and one public scope. You can see the scopes by choosing
  **Scopes** in the navigation pane. For more information about
  scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
