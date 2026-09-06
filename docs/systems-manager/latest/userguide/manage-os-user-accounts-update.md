

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Updating user or group membership using Fleet Manager
<a name="manage-os-user-accounts-update"></a>

You don't need to log on directly to a server to update a user account or group. You can use the Fleet Manager console to perform these tasks.

**To add an OS user account to a new group using Fleet Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Choose the button next to the managed node where the user account exists that you want to update.

1. Choose **View details**.

1. Choose **Tools, Users and groups**.

1. Choose the **Users** tab.

1. Choose the button next to the user you want to update.

1. Choose **Actions, Add user to group**.

1. Choose the group you want to add the user to under **Add to group**.

1. Select **Add user to group**.

**To edit an OS group's membership using Fleet Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Choose the button next to the managed node where the group exists that you want to update.

1. Choose **View details**.

1. Choose **Tools, Users and groups**.

1. Choose the **Groups** tab.

1. Choose the button next to the group you want to update.

1. Choose **Actions, Modify group**.

1. Choose the users you want to add or remove under **Group members**.

1. Select **Modify group**.