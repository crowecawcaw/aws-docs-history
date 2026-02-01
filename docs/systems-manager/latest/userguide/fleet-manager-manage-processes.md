• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Working with processes

You can use Fleet Manager, a tool in AWS Systems Manager, to work with processes on your managed
nodes. Using Fleet Manager, you can view information about processes. For example, you
can see the CPU utilization and memory usage of processes in addition to their
handles and threads. With Fleet Manager, you can start and terminate processes from the
console.

###### Note

Fleet Manager uses Session Manager, a tool in AWS Systems Manager, to retrieve process data. For
Amazon Elastic Compute Cloud (Amazon EC2) instances, the instance profile attached to your managed
instances must provide permissions for Session Manager to use this feature. For more
information about adding Session Manager permissions to an instance profile, see [Add
Session Manager permissions to an existing IAM role](getting-started-add-permissions-to-existing-profile.md "getting-started-add-permissions-to-existing-profile.md").

###### Topics

- [Viewing details about OS
  processes using Fleet Manager](fleet-manager-view-process-details.md "fleet-manager-view-process-details.md")
- [Starting an OS process on a
  managed node using Fleet Manager](fleet-manager-start-process.md "fleet-manager-start-process.md")
- [Terminating an OS process
  using Fleet Manager](fleet-manager-terminate-process.md "fleet-manager-terminate-process.md")
