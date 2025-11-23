# Assigning users or groups to an existing IAM

role

You can assign an existing IAM role to an AWS Managed Microsoft AD user or group. To do this,
make sure you have completed the following.

###### Prerequisites

- [Create an AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory").
- [Create an IAM user](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") or [create a IAM
  group](../../../IAM/latest/UserGuide/id_groups_create.md "../../../IAM/latest/UserGuide/id_groups_create.md").
- [Create a
  role](create_role.md "create_role.md") that has a trust relationship with Directory Service. For existing IAM
  roles, you will need to [edit the trust
  relationship for an existing role](edit_trust.md "edit_trust.md").

###### Important

Access for AWS Managed Microsoft AD users in nested groups within your directory are not
supported. Members of the parent group have console access, but members of child
groups do not.

###### To assign AWS Managed Microsoft AD users or groups to an existing IAM role

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, under **Active
   Directory**, choose **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, do one of the
   following:
   1. If you do not have any Regions showing under **Multi-Region
      replication**, choose the **Application
      management** tab.
   2. If you have multiple Regions showing under **Multi-Region
      replication**, select the Region where you want to make
      your assignments, and then choose the **Application
      management** tab. For more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").

4. Scroll down to the **AWS Management Console** section, choose
   **Actions** and **Enable**.
5. Under the **Delegate console access** section, choose the
   IAM role name for the existing IAM role that you want to assign users
   to.
6. On the **Selected role** page, under **Manage users
   and groups for this role**, choose **Add**.
7. On the **Add users and groups to the role** page, under
   **Select Active Directory Forest**, choose either the
   AWS Managed Microsoft AD forest (this forest) or the on-premises forest (trusted forest),
   whichever contains where the accounts that need access to the AWS Management Console. For
   more information about how to set up a trusted forest, see [Tutorial: Create a trust relationship between your
   AWS Managed Microsoft AD and your self-managed Active Directory domain](ms_ad_tutorial_setup_trust.md "ms_ad_tutorial_setup_trust.md").
8. Under **Specify which users or groups to add**, select either
   **Find by user** or **Find by group**, and
   then type the name of the user or group. In the list of possible matches, choose
   the user or group that you want to add.
9. Choose **Add** to finish assigning the users and groups to
   the role.
