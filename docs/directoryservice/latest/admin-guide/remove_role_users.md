# Removing a user or group from an IAM role

To remove an AWS Managed Microsoft AD user or group from an IAM role, perform the following
steps.

###### To remove a user or group from an IAM role

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, choose
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, do one of the
   following:
   1. If you have multiple Regions showing under **Multi-Region
      replication**, select the Region where you want to remove
      your assignments, and then choose the **Application
      management** tab. For more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
   2. If you do not have any Regions showing under **Multi-Region
      replication**, choose the **Application
      management** tab.

4. Under the **AWS Management Console** section, choose the IAM role you
   want to remove users and groups from.
5. On the **Selected role** page, under **Manage users
   and groups for this role**, select the users or groups to remove
   the role from and choose **Remove**. The role is removed from
   the specified users and groups, but the role is not removed from your
   account.

###### Note

If you want to delete a role, see [Delete roles or
instance profiles](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md").
