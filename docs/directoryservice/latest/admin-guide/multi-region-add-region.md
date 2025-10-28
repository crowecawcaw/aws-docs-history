# Adding a replicated Region for AWS Managed Microsoft AD

When you add a Region using the [Configure Multi-Region
replication for AWS Managed Microsoft AD](ms_ad_configure_multi_region_replication.md "ms_ad_configure_multi_region_replication.md") feature, AWS Managed Microsoft AD creates two
domain controllers in the selected AWS Region, Amazon Virtual Private Cloud (VPC), and
subnet. AWS Managed Microsoft AD also creates the related security groups that enable Windows workloads to
connect to your directory in the new Region. It also creates these resources using the same
AWS account where your directory is already deployed. You do this by choosing the Region,
specifying the VPC, and providing the configurations for the new Region.

Multi-Region replication is only supported for the **Enterprise Edition**
of AWS Managed Microsoft AD.

## Prerequisites

Before you proceed with the steps to add a new replication Region, we recommend that you
first review the following prerequisite tasks.

- Verify that you have the necessary AWS Identity and Access Management (IAM) permissions, Amazon VPC setup, and
  the subnet setup in the new Region to which you want to replicate the directory.
- If you want to use your existing on-premises Active Directory credentials to access
  and manage Active Directory-aware workloads in AWS, you must create an Active
  Directory trust between AWS Managed Microsoft AD and your on-premises AD infrastructure. For more
  information about trusts, see [Connect AWS Managed Microsoft AD to your existing Active Directory infrastructure](ms_ad_connect_existing_infrastructure.md "ms_ad_connect_existing_infrastructure.md").
- If you have an existing trust relationship between your on-premises Active Directory
  and you want to add a replicated region, you need to verify you have the necessary Amazon VPC
  and subnet setup in the new Region to which you want to replicate the directory.

You can also create a trust between your AWS Managed Microsoft AD and on-premise AD infrastructure,
so you can use existing on-premises Active Directory credentials to manage AD-aware
workloads. For more information, see [Connect AWS Managed Microsoft AD to your existing Active Directory infrastructure](ms_ad_connect_existing_infrastructure.md "ms_ad_connect_existing_infrastructure.md").

## Add a Region

Use the following procedure to add a replicated Region for your AWS Managed Microsoft AD
directory.

###### To add a replicated Region

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, choose
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, under **Multi-Region
   replication**, choose the **Primary** Region from the list,
   and then choose **Add Region**.

###### Note

You can only add Regions while the **Primary** Region is
selected. For more information, see [Primary Region](multi-region-global-primary-additional.md#multi-region-primary "multi-region-global-primary-additional.md#multi-region-primary"). 4. On the **Add Region** page, under **Region**,
choose the Region you want to add from the list. 5. Under **VPC**, choose the VPC to use for this Region.

###### Note

This VPC must not have a Classless Inter-Domain Routing (CIDR) that overlaps with
a VPC used by this directory in another Region. 6. Under **Subnets**, choose the subnet to use for this Region. 7. Review the information under **Pricing**, and then choose
**Add**. 8. When AWS Managed Microsoft AD completes the domain controller deployment process, the Region
will display **Active** status. You can now make updates to
this Region as needed.

## Next steps

After you add your new Region, you should consider doing the following next
steps:

- Deploy additional domain controllers (up to 20) to your new Region as needed. The
  number of domain controllers when you add a new Region is 2 by default, which is the
  minimum required for fault-tolerance and high availability purposes. For more
  information, see [Adding or removing additional domain controllers with the
  AWS Management Console](ms_ad_deploy_additional_dcs.md#addremovedcs "ms_ad_deploy_additional_dcs.md#addremovedcs").

###### Note

When you add a replicated AWS Region to your AWS Managed Microsoft AD, two domain
controllers are created by default, which is the minimum number of domain controllers
required for fault-tolerance and high availability.

- Share your directory with more AWS accounts per Region. Directory sharing
  configurations are not replicated from the primary Region automatically. For more
  information, see [Share your AWS Managed Microsoft AD](ms_ad_directory_sharing.md "ms_ad_directory_sharing.md").

###### Note

Directory sharing configurations aren't automatically replicated in the primary
AWS Region.

- Enable log forwarding to retrieve your directory's security logs using Amazon CloudWatch Logs
  from the new Region. When you enable log forwarding, you must provide a log group name
  in each Region where you replicated your directory. For more information, see [Enabling Amazon CloudWatch Logs log forwarding for
  AWS Managed Microsoft AD](ms_ad_enable_log_forwarding.md "ms_ad_enable_log_forwarding.md").

###### Note

When you enable log forwarding, you must provide a name for the log group in each
AWS Region where you replicated your directory.

- Enable Amazon Simple Notification Service (Amazon SNS) monitoring for the new Region to track your directory
  health status per Region. For more information, see [Enabling AWS Managed Microsoft AD directory status
  notifications with Amazon Simple Notification Service](ms_ad_enable_notifications.md "ms_ad_enable_notifications.md").
