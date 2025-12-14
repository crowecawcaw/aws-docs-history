AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Working with Patch Manager resources and compliance

using the console

To use Patch Manager, a tool in AWS Systems Manager, complete the following tasks. These tasks are
described in more detail in this section.

1. Verify that the AWS predefined patch baseline for each operating system type
   that you use meets your needs. If it doesn't, create a patch baseline that
   defines a standard set of patches for that managed node type and set it as the
   default instead.
2. Organize managed nodes into patch groups by using Amazon Elastic Compute Cloud (Amazon EC2) tags
   (optional, but recommended).
3. Do one of the following:
   - (Recommended) Configure a patch policy in Quick Setup, a tool in Systems Manager,
     that lets you install missing patches on a schedule for an entire
     organization, a subset of organizational units, or a single
     AWS account. For more information, see [Configure patching for instances in an
     organization using a Quick Setup patch policy](quick-setup-patch-manager.md "quick-setup-patch-manager.md").
   - Create a maintenance window that uses the Systems Manager document (SSM
     document) `AWS-RunPatchBaseline` in a Run Command task type. For
     more information, see [Tutorial: Create a
     maintenance window for patching using the console](maintenance-window-tutorial-patching.md "maintenance-window-tutorial-patching.md").
   - Manually run `AWS-RunPatchBaseline` in a Run Command
     operation. For more information, see [Running commands from the console](running-commands-console.md "running-commands-console.md").
   - Manually patch nodes on demand using the **Patch
     now** feature. For more information, see [Patching managed nodes on
     demand](patch-manager-patch-now-on-demand.md "patch-manager-patch-now-on-demand.md").

4. Monitor patching to verify compliance and investigate failures.

###### Topics

- [Creating a patch
  policy](patch-manager-create-a-patch-policy.md "patch-manager-create-a-patch-policy.md")
- [Viewing patch Dashboard
  summaries](patch-manager-view-dashboard-summaries.md "patch-manager-view-dashboard-summaries.md")
- [Working with patch compliance
  reports](patch-manager-compliance-reports.md "patch-manager-compliance-reports.md")
- [Patching managed nodes on
  demand](patch-manager-patch-now-on-demand.md "patch-manager-patch-now-on-demand.md")
- [Working with patch
  baselines](patch-manager-create-a-patch-baseline.md "patch-manager-create-a-patch-baseline.md")
- [Viewing available
  patches](patch-manager-view-available-patches.md "patch-manager-view-available-patches.md")
- [Creating and managing patch
  groups](patch-manager-tag-a-patch-group.md "patch-manager-tag-a-patch-group.md")
- [Integrating Patch Manager with
  AWS Security Hub CSPM](patch-manager-security-hub-integration.md "patch-manager-security-hub-integration.md")
