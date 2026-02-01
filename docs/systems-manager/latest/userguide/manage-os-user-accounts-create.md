• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Creating an OS user or group

using Fleet Manager

###### Note

Fleet Manager uses Session Manager to set passwords for new users. For Amazon EC2
instances, the instance profile attached to your managed instances must
provide permissions for Session Manager to use this feature. For more information
about adding Session Manager permissions to an instance profile, see [Add
Session Manager permissions to an existing IAM role](getting-started-add-permissions-to-existing-profile.md "getting-started-add-permissions-to-existing-profile.md").

Instead of logging on directly to a server to create a user account or group,
you can use the Fleet Manager console to perform the same tasks.

###### To create an OS user account using Fleet Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the button next to the managed node you want to create a new
   user on.
4. Choose **View details**.
5. Choose **Tools, Users and groups**.
6. Choose the **Users** tab, and then choose
   **Create user**.
7. Enter a value for the **Name** of the new
   user.
8. (Recommended) Select the check box next to **Set
   password**. You will be prompted to provide a password for
   the new user at the end of the procedure.
9. Select **Create user**. If you selected the check box
   to create a password for the new user, you will be prompted to enter a
   value for the password and select **Done**. If the
   password you specify doesn't meet the requirements specified by your
   managed node's local or domain policies, an error is returned.

###### To create an OS group using Fleet Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the button next to the managed node you want to create a group
   in.
4. Choose **View details**.
5. Choose **Tools, Users and groups**.
6. Choose the **Groups** tab, and then choose
   **Create group**.
7. Enter a value for the **Name** of the new
   group.
8. (Optional) Enter a value for the **Description** of
   the new group.
9. (Optional) Select users to add to the **Group
   members** for the new group.
10. Select **Create group**.
