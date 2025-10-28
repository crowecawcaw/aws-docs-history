# Viewing users and groups assigned to a role

To view the AWS Managed Microsoft AD users and groups assigned to an IAM role, perform the
following steps.

###### Prerequisites

- [Create an AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory").
- [Create an IAM user](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") or [create a IAM
  group](../../../IAM/latest/UserGuide/id_groups_create.md "../../../IAM/latest/UserGuide/id_groups_create.md").
- [Create a
  role](create_role.md "create_role.md") that has a trust relationship with AWS Directory Service. For existing IAM
  roles, you will need to [edit the trust
  relationship for an existing role](edit_trust.md "edit_trust.md").
- [Assign your
  users or groups to an existing IAM role](assign_role.md "assign_role.md").

###### To view AWS Managed Microsoft AD users and group assigned to an IAM role

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, under **Active Directory**,
   choose **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, do one of the
   following:
   1. If you have multiple Regions showing under **Multi-Region
      replication**, select the Region where you want to view
      your assignments, and then choose the **Application
      management** tab. For more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
   2. If you do not have any Regions showing under **Multi-Region
      replication**, choose the **Application
      management** tab.

4. Scroll down to the **AWS Management Console** section. The
   **Status** should be **Enabled**. If not,
   choose **Actions** and **Enable**. For more
   information, see [Enabling AWS Management Console access with AWS Managed Microsoft AD
   credentials](ms_ad_management_console_access.md "ms_ad_management_console_access.md").

###### Note

You won't see any groups or users if the AWS Management Console is
disabled. 5. Under the **Delegate Console Access** section, select the
hyperlink of the IAM role you want to view. Alternatively, you can select
**View policy in IAM** to view the IAM policy in the
IAM console. 6. On the **Selected role** page, under the **Manage
users and groups for this role** section, you can view the users
and groups assigned to the IAM role.
