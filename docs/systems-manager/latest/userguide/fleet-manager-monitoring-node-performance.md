• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Monitoring managed node

performance

You can use Fleet Manager, a tool in AWS Systems Manager, to view performance data about your
managed nodes in real time. The performance data is retrieved from performance
counters.

The following performance counters are available in Fleet Manager:

- CPU utilization
- Disk input/output (I/O) utilization
- Network traffic
- Memory usage

###### Note

Fleet Manager uses Session Manager, a tool in AWS Systems Manager, to retrieve performance data. For
Amazon Elastic Compute Cloud (Amazon EC2) instances, the instance profile attached to your managed
instances must provide permissions for Session Manager to use this feature. For more
information about adding Session Manager permissions to an instance profile, see [Add
Session Manager permissions to an existing IAM role](getting-started-add-permissions-to-existing-profile.md "getting-started-add-permissions-to-existing-profile.md").

###### To view performance data with Fleet Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the button next to the managed node whose performance you want to
   monitor.
4. Choose **View details**.
5. Choose **Tools, Performance counters**.
