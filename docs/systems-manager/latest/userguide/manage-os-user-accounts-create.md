

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Creating an OS user or group using Fleet Manager
<a name="manage-os-user-accounts-create"></a>

**Note**  
Fleet Manager uses Session Manager to set passwords for new users. For Amazon EC2 instances, the instance profile attached to your managed instances must provide permissions for Session Manager to use this feature. For more information about adding Session Manager permissions to an instance profile, see [Add Session Manager permissions to an existing IAM role](getting-started-add-permissions-to-existing-profile.md).

Instead of logging on directly to a server to create a user account or group, you can use the Fleet Manager console to perform the same tasks.

**To create an OS user account using Fleet Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Choose the button next to the managed node you want to create a new user on.

1. Choose **View details**.

1. Choose **Tools, Users and groups**.

1. Choose the **Users** tab, and then choose **Create user**.

1. Enter a value for the **Name** of the new user.

1. (Recommended) Select the check box next to **Set password**. You are prompted to provide a password for the new user at the end of the procedure.

1. Select **Create user**. If you selected the check box to create a password for the new user, you are prompted to enter a value for the password and select **Done**. If the password you specify doesn't meet the requirements specified by your managed node's local or domain policies, an error is returned.

**To create an OS group using Fleet Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Choose the button next to the managed node you want to create a group in.

1. Choose **View details**.

1. Choose **Tools, Users and groups**.

1. Choose the **Groups** tab, and then choose **Create group**.

1. Enter a value for the **Name** of the new group.

1. (Optional) Enter a value for the **Description** of the new group.

1. (Optional) Select users to add to the **Group members** for the new group.

1. Select **Create group**.