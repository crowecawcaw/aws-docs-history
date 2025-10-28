# Step 2: Share your directory

Use the following procedures to begin the directory sharing workflow from within the
directory owner account.

###### Note

Directory sharing is a Regional feature of AWS Managed Microsoft AD.
If you are using [Multi-Region replication](ms_ad_configure_multi_region_replication.md "ms_ad_configure_multi_region_replication.md"), the
following procedures must be applied separately in each Region. For more information, see
[Global vs Regional features](multi-region-global-region-features.md "multi-region-global-region-features.md").

###### To share your directory from the directory owner account

1.  Sign into the AWS Management Console with administrator credentials in the directory owner
    account and open the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") at https://console.aws.amazon.com/directoryservicev2/.
2.  In the navigation pane, choose **Directories**.
3.  Choose the directory ID of the AWS Managed Microsoft AD directory that you want to
    share.
4.  On the **Directory details** page, do one of the
    following:
    - If you have multiple Regions showing under **Multi-Region
      replication**, select the Region where you want to share
      your directory, and then choose the **Scale &
      share** tab. For more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
    - If you do not have any Regions showing under **Multi-Region
      replication**, choose the **Scale &
      share** tab.

5.  In the **Shared directories** section, choose
    **Actions**, and then choose **Create new shared
    directory**.
6.  On the **Choose which AWS accounts to share with** page,
    choose one of the following sharing methods depending on your business
    needs:

        1. **Share this directory with AWS accounts inside your
         organization** – With this option you can select the
         AWS accounts you want to share your directory with from a list showing
         all the AWS accounts inside your AWS organization. You must enable
         trusted access with AWS Directory Service before you share a directory. For more
         information, see [How to enable or disable trusted access](../../../organizations/latest/userguide/orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access "../../../organizations/latest/userguide/orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access").


        ###### Note

        To use this option, your organization must have **All
         features** enabled, and your directory must be in the
         organization management account.


        	1. Under **AWS accounts in your
        	 organization**, select the AWS accounts that you want
        	 to share the directory with and click **Add**.
        	2. Review the pricing details, and then choose
        	 **Share**.
        	3. Proceed to [Step 4](step4_test_ec2_access.md "step4_test_ec2_access.md")
        	 in this guide. Because all AWS accounts are in the same
        	 organization, you do not need to follow Step 3.
        2. **Share this directory with other AWS accounts** -
         With this option, you can share a directory with accounts inside or
         outside your AWS organization. You can also use this option when your
         directory is not a member of an AWS organization and you want to share
         with another AWS account.


        	1. In **AWS account ID(s)**, enter all the
        	 AWS account IDs that you want to share the directory with, and
        	 then click **Add**.
        	2. In **Send a note**, type a message to the
        	 administrator in the other AWS account.
        	3. Review the pricing details, and then choose
        	 **Share**.
        	4. Proceed to Step 3.

    **Next Step**

[Step 3: Accept shared directory invite -
Optional](step3_accept_invite.md "step3_accept_invite.md")
