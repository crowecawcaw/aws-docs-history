• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Exploring nodes

You can use the **Explore nodes** page in Systems Manager to review details of
managed nodes in your organization or account according to the criteria you specify in
filters. You can also use Systems Manager integration with Amazon Q Developer (Amazon Q), an AWS generative AI
solution, to search using text prompts.

###### Before you begin

In order to use the **Explore nodes** feature, you must first onboard
your organization or account to the unified Systems Manager console. For more information, see
[Setting up Systems Manager unified console
for an organization](systems-manager-setting-up-organizations.md "systems-manager-setting-up-organizations.md").

After onboarding, open the [Systems Manager
console](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/") and choose **Explore nodes**.

###### Note

If you've created an aggregator index for Resource Explorer in a Region different than your home
Region, Systems Manager demotes the current index. Then, Systems Manager promotes the local index in your
home Region as the new aggregator index. During this time, only nodes for your home
Region are displayed. This process can take up to 24 hours to complete.

###### Topics

- [Exploring nodes using console
  filters](view-aggregated-node-details-console.md "view-aggregated-node-details-console.md")
- [Exploring nodes using text prompts in
  Amazon Q](view-aggregated-node-details-Q.md "view-aggregated-node-details-Q.md")
- [Viewing individual node details and taking action
  on a node](node-detail-actions.md "node-detail-actions.md")
- [Downloading or exporting a managed node
  report](explore-nodes-download-report.md "explore-nodes-download-report.md")
- [Managing node report content and
  appearance](explore-nodes-manage-report-display.md "explore-nodes-manage-report-display.md")
