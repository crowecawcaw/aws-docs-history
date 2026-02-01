• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Managing EC2 instances with Systems Manager

Complete the tasks in this section to set up and configure roles, permissions, and initial
resources for AWS Systems Manager. The tasks described in this section are typically performed by
AWS account and systems administrators. After these steps are complete, users in your
organization can use Systems Manager to configure, manage, and access Amazon Elastic Compute Cloud (Amazon EC2)
instances.

###### Note

If you plan to use Systems Manager to manage and configure on-premises machines, follow the
setup steps in [Managing nodes in hybrid and multicloud
environments with Systems Manager](systems-manager-hybrid-multicloud.md "systems-manager-hybrid-multicloud.md"). If you plan to use both Amazon EC2
instances _and_ non-EC2 machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types")
environment, follow the steps here first. This section presents steps in the recommended
order for configuring the roles, users, permissions, and initial resources to use in
your Systems Manager operations.

If you already use other AWS services, you have completed some of these steps. However,
other steps are specific to Systems Manager. Therefore, we recommend reviewing this entire section to
ensure that you're ready to use all Systems Manager tools.

###### Contents

- [Configure instance permissions required for
  Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md")
- [Improve the security of EC2 instances by using VPC
  endpoints for Systems Manager](setup-create-vpc.md "setup-create-vpc.md")
