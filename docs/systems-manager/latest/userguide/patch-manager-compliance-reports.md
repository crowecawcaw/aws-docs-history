• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Working with patch compliance

reports

Use the information in the following topics to help you generate and work with
patch compliance reports in Patch Manager, a tool in AWS Systems Manager.

The information in the following topics apply no matter which method or type of
configuration you're using for your patching operations:

- A patch policy configured in Quick Setup
- A Host Management option configured in Quick Setup
- A maintenance window to run a patch `Scan` or
  `Install` task
- An on-demand **Patch now** operation

###### Important

Patch compliance reports are point-in-time snapshots generated only by
successful patching operations. Each report contains a capture time that
identifies when the compliance status was calculated.

If you have multiple types of operations in place to scan your instances for
patch compliance, note that each scan overwrites the patch compliance data of
previous scans. As a result, you might end up with unexpected results in your
patch compliance data. For more information, see [Identifying the
execution that created patch compliance data](patch-manager-compliance-data-overwrites.md "patch-manager-compliance-data-overwrites.md").

To verify which patch baseline was used to generate the latest compliance
information, navigate to the **Compliance reporting** tab in
Patch Manager, locate the row for the managed node you want information about, and
then choose the baseline ID in the **Baseline ID used**
column.

###### Topics

- [Viewing patch compliance
  results](patch-manager-view-compliance-results.md "patch-manager-view-compliance-results.md")
- [Generating .csv
  patch compliance reports](patch-manager-store-compliance-results-in-s3.md "patch-manager-store-compliance-results-in-s3.md")
- [Remediating noncompliant
  managed nodes with Patch Manager](patch-manager-noncompliant-nodes.md "patch-manager-noncompliant-nodes.md")
- [Identifying the
  execution that created patch compliance data](patch-manager-compliance-data-overwrites.md "patch-manager-compliance-data-overwrites.md")
