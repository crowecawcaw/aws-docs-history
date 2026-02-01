• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Edit Distributor package tags

in the console

After you have added a package to Distributor, a tool in AWS Systems Manager, you can edit the
package's tags in the Systems Manager console. These tags are applied to the package, and
aren't connected to tags on the managed node on which you want to deploy the
package. Tags are case sensitive key and value pairs that can help you group and
filter your packages by criteria that are relevant to your organization. If you
don't want to add tags, you're ready to install your package or add a new
version.

###### To edit package tags in the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Distributor**.
3. On the **Packages** page, choose the package for which
   you want to edit tags.
4. On the **Package details** tab, in
   **Tags**, choose **Edit**.
5. For **Add tags**, enter a tag key, or a tag key and value
   pair, and then choose **Add**. Repeat if you want to add
   more tags. To delete tags, choose **X** on the tag at the
   bottom of the window.
6. When you're finished adding tags to your package, choose
   **Save**.
