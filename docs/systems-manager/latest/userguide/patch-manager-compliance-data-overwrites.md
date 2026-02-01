• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Identifying the

execution that created patch compliance data

Patch compliance data represents a point-in-time snapshot from the latest
successful patching operation. Each compliance report includes both an execution
ID and a capture time that help you identify which operation created the
compliance data and when it was generated.

If you have multiple types of operations in place to scan your instances for
patch compliance, each scan overwrites the patch compliance data of previous
scans. As a result, you might end up with unexpected results in your patch
compliance data.

For example, suppose you create a patch policy that scans for patch compliance
each day at 2 AM local time. That patch policy uses a patch baseline that
targets patches with severity marked as `Critical`,
`Important`, and `Moderate`. This patch baseline also
specifies a few specifically rejected patches.

Also suppose that you already had a maintenance window set up to scan the same
set of managed nodes each day at 4 AM local time, which you don't delete or
deactivate. That maintenance window’s task uses a different patch baseline, one
that targets only patches with a `Critical` severity and doesn’t
exclude any specific patches.

When this second scan is performed by the maintenance window, the patch
compliance data from the first scan is deleted and replaced with patch
compliance from the second scan.

Therefore, we strongly recommend using only one automated method for scanning
and installing in your patching operations. If you're setting up patch policies,
you should delete or deactivate other methods of scanning for patch compliance.
For more information, see the following topics:

- To remove a patching operation task from a maintenance window –
  [Updating or deregistering
  maintenance window tasks using the console](sysman-maintenance-update.md#sysman-maintenance-update-tasks "sysman-maintenance-update.md#sysman-maintenance-update-tasks")
- To delete a State Manager association – [Deleting
  associations](systems-manager-state-manager-delete-association.md "systems-manager-state-manager-delete-association.md").
  To deactivate daily patch compliance scans in a Host Management configuration,
  do the following in Quick Setup:

1. In the navigation pane, choose **Quick Setup**.
2. Select the Host Management configuration to update.
3. Choose **Actions, Edit configuration**.
4. Clear the **Scan instances for missing patches
   daily** check box.
5. Choose **Update**.

###### Note

Using the **Patch now** option to scan a managed node for
compliance also results in an overwrite of patch compliance data.
