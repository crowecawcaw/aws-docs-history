# Multi-Region Resilience for WorkSpaces Personal

Amazon WorkSpaces Multi-Region Resilience (MRR) enables you to redirect users to a secondary Region when your primary WorkSpaces Region is
unreachable due to disruptive events, without requiring your users to switch registration codes when logging to their
standby WorkSpaces. Standby WorkSpaces is a feature of Amazon WorkSpaces Multi-Region Resilience that streamlines the standby deployment creation and management.
After setting up a user directory in your secondary Region, select the WorkSpace in your primary Region that you want to create a
standby WorkSpace for. The system automatically mirrors the primary WorkSpace bundle images to the secondary Region.
It then automatically provisions a new standby WorkSpace in your secondary Region

Amazon WorkSpaces Multi-Region Resilience is built upon cross-Region redirection that leverages DNS health check and failover capabilities.
It allows you to use a fully qualified domain name (FQDN) as your WorkSpaces registration code. When your users log in to WorkSpaces,
you can redirect them across supported WorkSpaces Regions based on your Domain Name System (DNS) policies for the FQDN.
If you use Amazon Route 53, we recommend using health checks that monitor Amazon CloudWatch alarms when devising a cross-Region redirection strategy
for WorkSpaces. For more information, see [Creating Amazon Route 53 health checks and configuring DNS failover](../../../Route53/latest/DeveloperGuide/dns-failover.md "../../../Route53/latest/DeveloperGuide/dns-failover.md") in the _Amazon Route 53 Developer Guide_.

Data replication is an add-on feature of standby WorkSpaces that replicates data one-way from
the primary Region to the secondary Region. After enabling data replication, EBS snapshots
of the system and user volumes are taken every 12 hours.
Multi-Region Resilience regularly checks for fresh snapshots. When the snapshots are found, it initiates a copy to
the secondary Region. As copies arrive in the secondary Region, they are used to update the
secondary WorkSpace.

###### Contents

- [Prerequisites](#multi-region-resilience-prerequisites "#multi-region-resilience-prerequisites")
- [Limitations](#multi-region-resilience-limitations "#multi-region-resilience-limitations")
- [Configure your Multi-Region Resilience standby WorkSpace](#w25aac11c35c19c15 "#w25aac11c35c19c15")
- [Create a standby WorkSpace](#create-standby-workspace "#create-standby-workspace")
- [Manage a standby WorkSpace](#manage-standby-workspace "#manage-standby-workspace")
- [Delete a standby WorkSpace](#delete-standby-workspace "#delete-standby-workspace")
- [One-way data replication for standby WorkSpaces](#one-way-data-replication "#one-way-data-replication")
- [Plan to reserve Amazon EC2 capacity for recovery](#mrr-ec2-recovery "#mrr-ec2-recovery")

## Prerequisites

- You must create WorkSpaces for your users in the primary Region before creating
  standby WorkSpaces. For more information about creating WorkSpaces, see
  [Create a directory for WorkSpaces Personal](launch-workspaces-tutorials.md "launch-workspaces-tutorials.md").
- To enable data replication on standby WorkSpaces, you should have either a self-
  managed Active Directory or an AWS Managed Microsoft AD configured to replicate to
  your standby Regions. For more information, see
  [Create your AWS Managed Microsoft AD directory](../../../directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.md") and
  [Add a replicated Region](../../../directoryservice/latest/admin-guide/multi-region-add-region.md "../../../directoryservice/latest/admin-guide/multi-region-add-region.md").
- Ensure you update networking dependency drivers like ENA, NVMe, and PV drivers on your primary WorkSpaces. You should do this at least once every 6 months.
  For more information, see
  [Install or upgrade Elastic Network Adapter (ENA) driver](../../../AWSEC2/latest/WindowsGuide/enhanced-networking-ena.md#ena-adapter-driver-install-upgrade-win "../../../AWSEC2/latest/WindowsGuide/enhanced-networking-ena.md#ena-adapter-driver-install-upgrade-win") ,
  [AWS NVMe drivers for Windows instances](../../../AWSEC2/latest/WindowsGuide/aws-nvme-drivers.md "../../../AWSEC2/latest/WindowsGuide/aws-nvme-drivers.md"),
  and [Upgrade PV drivers on Windows instances](../../../AWSEC2/latest/WindowsGuide/Upgrading_PV_drivers.md "../../../AWSEC2/latest/WindowsGuide/Upgrading_PV_drivers.md").
- Ensure you update the EC2Config, EC2Launch, and EC2Launch V2 agents to the latest versions periodically. You should do this at least once every 6 months. For more information, see
  [Update EC2Config and EC2Launch](../../../AWSEC2/latest/WindowsGuide/migrating-latest-types.md#upgdate-ec2config-ec2launch "../../../AWSEC2/latest/WindowsGuide/migrating-latest-types.md#upgdate-ec2config-ec2launch").
- To ensure proper data replication, ensure the Active Directories in the primary and secondary regions are in sync for FQDN, OU, and user SID.
- The default quota (limit) for standby WorkSpaces is 0. You need to request a
  service quota increase before creating a standby WorkSpace. For more
  information, see [Amazon WorkSpaces quotas](workspaces-limits.md "workspaces-limits.md").
- Ensure you are using [customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") to
  encrypt both your primary and standby WorkSpaces. You can either use single Region keys or
  [multi-Region keys](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md") to encrypt your primary and standby WorkSpaces.

## Limitations

- Standby WorkSpaces only copies the bundle image of your primary WorkSpaces but it doesn't copy the system volume
  (drive C) or user volume (drive D) from your primary WorkSpaces. To copy the system volume (drive C) or user volume
  (drive D) from your primary WorkSpaces to standby WorkSpaces, you have to enable data replication.
- You cannot directly modify, rebuild, restore, or migrate a standby WorkSpace.
- Failover for cross-Region redirection is controlled by your DNS settings. To implement an automatic failover scenario,
  you must use a different mechanism in conjunction with cross-Region redirection. For example, you can use an Amazon Route 53 failover
  DNS routing policy paired with a Route 53 health check that monitors a CloudWatch alarm in the primary Region. If the CloudWatch alarm in the
  primary Region is invoked, your DNS failover routing policy then redirects your WorkSpaces users to the WorkSpaces that you've set up for
  them in the failover Region.
- Data replication only goes one way, copying data from primary Region to secondary Region. During standby WorkSpaces failover,
  you can access the data and application between 12 and 24 hours. After an outage, manually back up any data that you created
  on the secondary WorkSpace and log out. We recommend saving your work to external drives, such as your network drive,
  so that you can access your data from the primary WorkSpace.
- Data replication does not support AWS Simple AD.
- When you enable data replication on standby WorkSpaces, EBS snapshots of the primary WorkSpaces (both root and system volumes) are
  taken every 12 hours. The initial snapshot for a particular data volume is full and subsequent snapshots are incremental.
  As a result, the first replication for a given WorkSpace will take longer than subsequent ones. Snapshots are initiated
  on a schedule that is internal to WorkSpaces and you cannot control the timing.
- If the primary WorkSpace and standby WorkSpace join using the same domain, we recommend that you only connect to either the
  primary WorkSpace or standby WorkSpace at a given point in time to avoid losing connection with the domain controller.
- If you configure your AWS Managed Microsoft AD for Multi-Region replication, only the directory in the
  primary Region can be registered for use with WorkSpaces. If you try to register the directory in a replicated Region for use with WorkSpaces, it will fail.
  Multi-Region replication with AWS Managed Microsoft AD isn't supported for use with WorkSpaces within replicated Regions.
- If you’ve already set up your cross-Region redirection and created WorkSpaces in both your primary and secondary Regions
  without using standby WorkSpaces, you cannot convert the existing WorkSpace in the secondary Region to a standby WorkSpace directly.
  Instead, you need to shut down the WorkSpace in your secondary Region, select the WorkSpace in your primary Region that you want to
  create a standby WorkSpace for, and use standby WorkSpaces to create the standby WorkSpace.
- After an outage, manually back up any data that you
  created on the secondary WorkSpace and log out. We recommend saving your
  work to external drives, such as your network drive, so that you can access your data from
  the primary WorkSpace.
- WorkSpaces Multi-Region Resilience is currently available in the following Regions:
  - US East (N. Virginia) Region
  - US West (Oregon) Region
  - Europe (Frankfurt) Region
  - Europe (Ireland) Region

- WorkSpaces Multi-Region Resilience is only supported on version 3.0.9 or later of the Linux, macOS, and Windows WorkSpaces
  client applications. You can also use Multi-Region Resilience with Web Access.
- WorkSpaces Multi-Region Resilience supports Windows and Bring Your Own License (BYOL) WorkSpaces.
  It doesn't support Amazon Linux 2, Ubuntu WorkSpaces, Red Hat Enterprise Linux, GeneralPurpose.4xlarge, GeneralPurpose.8xlarge,
  or GPU-enabled WorkSpaces (e.g. Graphics, GraphicsPro, Graphics.g4dn, or GraphicsPro.g4dn).
- After failover or failback completes, wait 15 to 30 minutes before connecting to your WorkSpace.

## Configure your Multi-Region Resilience standby WorkSpace

###### To configure your Multi-Region Resilience standby WorkSpace

1. Set up user directories in both your primary and secondary Regions. Ensure that you use
   the same user names in each WorkSpaces directory in each Region.

To keep your Active Directory user data in sync, we recommend using AD Connector to point to the
same Active Directory in each Region where you've set up WorkSpaces for your users. For more information
about creating a directory, see
[Register a directory with WorkSpaces](register-deregister-directory.md "register-deregister-directory.md").

###### Important

If you configure your AWS Managed Microsoft AD directory for multi-Region replication,
only the directory in the primary Region can be registered for use with WorkSpaces. Attempts to register
the directory in a replicated Region for use with WorkSpaces will fail. Multi-Region replication with
AWS Managed Microsoft AD isn't supported for use with WorkSpaces within replicated Regions. 2. Create WorkSpaces for your users in the primary Region. For more information about creating WorkSpaces,
see [Launch WorkSpaces](launch-workspaces-tutorials.md "launch-workspaces-tutorials.md"). 3. Create a standby WorkSpace in the secondary Region. For more information about creating a standby WorkSpace,
see [Create a standby WorkSpace](multi-region-resilience.md#create-standby-workspace "multi-region-resilience.md#create-standby-workspace"). 4. Create and associate connection strings (FQDN) with user directories in primary and secondary Regions.

You must enable cross-Region redirection in your account because standby WorkSpaces is built upon cross-Region redirection.
Follow step 1 - 3 of the instructions for
[Cross-Region redirection for Amazon WorkSpaces](cross-region-redirection.md#cross-region-redirection-create-connection-aliases "cross-region-redirection.md#cross-region-redirection-create-connection-aliases"). 5. Configure DNS service and set up DNS routing policies.

You must set up your [DNS service and configure the necessary DNS routing policies](cross-region-redirection.md#cross-region-redirection-configure-DNS-routing "cross-region-redirection.md#cross-region-redirection-configure-DNS-routing"). Cross-Region redirection
works in conjunction with your DNS routing policies to redirect your WorkSpaces users as needed. 6. When you've finished setting up cross-Region redirection, you must send your users an email with a FQDN connection
string. For more information see
[Step 5: Send the connection string to your WorkSpaces users](cross-region-redirection.md#cross-region-redirection-send-connection-string-to-users "cross-region-redirection.md#cross-region-redirection-send-connection-string-to-users"). Ensure your WorkSpaces users are using the
FQDN-based registration code instead of the Region-based registration code (for example, WSpdx+ABC12D) for
their primary Region.

###### Important

    * If you create your users in the WorkSpaces console instead of creating them in Active Directory,
     WorkSpaces automatically sends an invitation email to your users with a Region-based registration code
     whenever you launch a new WorkSpace. This means that when you set up WorkSpaces for your users in the
     secondary Region, your users will also automatically receive emails for these secondary WorkSpaces. You
     will need to instruct your users to ignore emails with Region-based registration codes.
    * The Region-specific registration codes remain valid; however, for cross-
     Region redirection to work, your users must use the FQDN instead as their
     registration code.

## Create a standby WorkSpace

Before you create a standby WorkSpace, ensure you have completed the prerequisites, including creating a user directory in
both primary and secondary Regions, provisioning WorkSpaces for your users in your primary Region, configuring cross-Region
redirection in your account, and requesting standby WorkSpaces limit increase through the service quota.

###### To create a standby WorkSpace

1.  Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2.  In the upper-right corner of the console, select the primary AWS Region for your WorkSpaces.
3.  In the navigation pane, choose **WorkSpaces**.
4.  Select a WorkSpace you want to create a standby WorkSpace for.
5.  Choose **Actions** and then choose **Create standby WorkSpace**.
6.  Select the secondary Region, where you will create your standby WorkSpace, and then choose
    **Next**.
7.  Select the user directory in your secondary Region and then choose **Next**.
8.  (Optional) Add encryption key, enable data encryption, and manage tags.

        * To add an encryption key, enter it under Input encryption key.
        * To enable data replication, choose **Enable data replication**.
         Then, check the checkbox to confirm that you authorize additional monthly charge.
        * To add a new tag, choose **Add new tag**.

    Then, choose **Next**.

###### Note

    * If the original WorkSpace is encrypted, this field is prepopulated. However, you can choose to replace
     it with your own encryption key.
    * It takes a few minutes to update the data replication status.
    * After the standby WorkSpace is successfully updated with the snapshots from the
     primary WorkSpace, you can find the times stamps of the snapshots under **Recovery
     Snapshot**.

9. Review the settings of your standby WorkSpaces and then choose **Create**.

###### Note

    * To view information about your standby WorkSpaces, go to the primary WorkSpace detail page.
    * The standby WorkSpace only copies the bundle image of your primary WorkSpace but it does not copy the
     system volume (drive C) or user volume (drive D) from your primary WorkSpaces. By
     default, data replication is off. To copy the system volume
     (drive C) or user volume (drive D) from your primary WorkSpaces to standby
     WorkSpaces, you have to enable data replication.

## Manage a standby WorkSpace

You cannot directly modify, rebuild, restore, or migrate a standby WorkSpace.

###### To enable data replication for your standby WorkSpace

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. Go to your primary Region, select the primary WorkSpace ID.
3. Scroll down to the Standby WorkSpace section and choose **Edit Standby WorkSpace**.
4. Choose **Enable data replication**. Then, check the checkbox to confirm that you
   authorize additional monthly charge. Then, choose **Save**.

###### Note

- Standby WorkSpaces cannot hibernate. If you stop the standby WorkSpace, it does not preserve your unsaved work.
  We recommend users to always save their work before exiting their standby WorkSpaces.
- To enable data replication on standby WorkSpaces, you should have either a self-
  managed Active Directory or an AWS Managed Microsoft AD configured to replicate to
  your standby Regions. To set up your directories, follow steps 1 to 3 in the Walkthrough section of
  [Building for business continuity with Amazon WorkSpaces and AWS Directory Services](<https://aws.amazon.com/blogs/desktop-and-application-streaming/building-for-business-continuity-with-amazon-workspaces-and-aws-directory-services/#:~:text=Region(s).-,Walkthrough,-Step%201%3A%20Provision> "https://aws.amazon.com/blogs/desktop-and-application-streaming/building-for-business-continuity-with-amazon-workspaces-and-aws-directory-services/#:~:text=Region(s).-,Walkthrough,-Step%201%3A%20Provision") or see [Using multi-Region AWS Managed Active Directory with Amazon WorkSpaces](../../../whitepapers/latest/best-practices-deploying-amazon-workspaces/using-multi-region-aws-managed-active-directory-with-amazon-workspaces.md "../../../whitepapers/latest/best-practices-deploying-amazon-workspaces/using-multi-region-aws-managed-active-directory-with-amazon-workspaces.md") . Multi-Region replication is only supported for the Enterprise Edition of AWS
  Managed Microsoft AD.
- It takes a few minutes to update the data replication status.
- After the standby WorkSpace is successfully updated with the snapshots from the
  primary WorkSpace, you can find the times stamps of the snapshots under **Recovery
  Snapshot**.

## Delete a standby WorkSpace

You can terminate a standby WorkSpace the same way you terminate a regular WorkSpace.

###### To delete a standby WorkSpace

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the upper-right corner of the console, select the primary AWS Region for your WorkSpaces.
3. In the navigation pane, choose **WorkSpaces**.
4. Select the standby WorkSpace and choose **Delete**. It takes approximately 5 minutes to delete a
   standby WorkSpace. During deletion, the status of the standby WorkSpace will be set to **Terminating**.
   When the deletion is complete, the standby WorkSpace disappears from the console.

###### Note

Deleting a standby WorkSpace is a permanent action and cannot be undone. The standby WorkSpace user's data does not persist
and is destroyed. For help with backing up user data, contact AWS Support.

## One-way data replication for standby WorkSpaces

Enabling data replication in Multi-Region Resilience allows you to replicate data from a primary Region to a secondary Region.
During steady state, Multi-Region Resilience captures snapshots of the system (C drive) and data (D drive) of primary WorkSpaces every 12 hours.
These snapshots are transferred to the secondary Region and used to update the standby WorkSpaces. By default, data replication is disabled for standby WorkSpaces.

After data replication is enabled for the standby WorkSpaces, the initial snapshot for a particular data volume is complete, while subsequent snapshots are incremental.
As a consequence, the first replication for a given WorkSpace will take longer than subsequent ones. Snapshots are triggered at predetermined intervals within
WorkSpaces and the timing cannot be controlled by users.

![One-way data replication for standby WorkSpaces](images/Doppel-admin-LT-one-way.png)

During failover, when users are redirected to the secondary Region, they can access their standby WorkSpaces with data and applications that
are between 12 and 24 hours old. While users are using standby WorkSpaces, Multi-Region Resilience will not force them to log out of their standby WorkSpaces
or update the standby WorkSpaces with the snapshots from the primary Region.

After an outage, users should manually back up any data they have created on their secondary WorkSpaces before logging out of their standby WorkSpaces.
When they log in again, they will be directed to the primary Region and their primary WorkSpaces.

## Plan to reserve Amazon EC2 capacity for recovery

Amazon Multi-Region Resilience(MRR) relies on Amazon EC2 On-Demand pools by default. If a specific Amazon EC2 instance
type is unavailable to support your recovery, MRR will automatically attempt to scale up the instance repeatedly
until an available instance type is found, but in extreme circumstances, instances may not always be available.
To improve the availability of the required instance types you need for your most critical WorkSpaces, contact
AWS Support and we will assist you on capacity planning.
