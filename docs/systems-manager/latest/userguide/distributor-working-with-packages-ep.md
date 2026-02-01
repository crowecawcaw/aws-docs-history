• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Edit Distributor package

permissions in the console

After you add a package to Distributor, a tool in AWS Systems Manager, you can edit the
package's permissions in the Systems Manager console. You can add other AWS accounts to a
package's permissions. Packages can be shared with other accounts in the same
AWS Region only. Cross-Region sharing isn't supported. By default, packages are
set to **Private**, meaning only those with access to the package
creator's AWS account can view package information and update or delete the
package. If **Private** permissions are acceptable, you can skip
this procedure.

###### Note

You can update the permissions of packages that are shared with 20 or fewer
accounts.

###### To edit package permissions in the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Distributor**.
3. On the **Packages** page, choose the package for which
   you want to edit permissions.
4. On the **Package details** tab, choose **Edit
   permissions** to change permissions.
5. For **Edit permissions**, choose **Shared with
   specific accounts**.
6. Under **Shared with specific accounts**, add
   AWS account numbers, one at a time. When you're finished, choose
   **Save**.
