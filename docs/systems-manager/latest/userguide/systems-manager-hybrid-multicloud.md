• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Managing nodes in hybrid and multicloud

environments with Systems Manager

You can use AWS Systems Manager to manage both Amazon Elastic Compute Cloud (EC2) instances and a number of non-EC2
machine types. This section describes the setup tasks that account and system administrators
perform to manage non-EC2 machines using Systems Manager in a _[hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types")
environment_. After these steps are complete, users who have been granted
permissions by the AWS account administrator can use Systems Manager to configure and manage their
organization's non-EC2 machines.

Any machine that has been configured for use with Systems Manager is called a _managed node_.

###### Note

- You can register edge devices as managed nodes using the same
  hybrid-activation steps used for other non-EC2 machines. These types of edge
  devices include both AWS IoT devices and devices other than AWS IoT devices. Use
  the process described in this section to set up these types of edge
  devices.

Systems Manager also supports edge devices that use AWS IoT Greengrass Core software. The setup
process and requirements for AWS IoT Greengrass core devices are different from those for
AWS IoT and edge devices other than AWS edge devices. For information about
registering AWS IoT Greengrass devices for use with Systems Manager, see [Managing edge devices with
Systems Manager](systems-manager-setting-up-edge-devices.md "systems-manager-setting-up-edge-devices.md").

- Non-EC2 macOS machines aren't supported for Systems Manager hybrid and multicloud
  environments.
  If you plan to use Systems Manager to manage Amazon Elastic Compute Cloud (Amazon EC2) instances, or to use both Amazon EC2
  instances and non-EC2 machines in hybrid and multicloud environment, follow the steps in
  [Managing EC2 instances with Systems Manager](systems-manager-setting-up-ec2.md "systems-manager-setting-up-ec2.md") first.

After configuring your hybrid and multicloud environment for Systems Manager, you can do the
following:

- Create a consistent and secure way to remotely manage your hybrid and multicloud
  workloads from one location using the same tools or scripts.
- Centralize access control for actions that can be performed on your machines by
  using AWS Identity and Access Management (IAM).
- Centralize auditing of the operations performed on your machines by viewing the
  API activity recorded in AWS CloudTrail.

For information about using CloudTrail to monitor Systems Manager actions, see [Logging AWS Systems Manager API calls with AWS CloudTrail](monitoring-cloudtrail-logs.md "monitoring-cloudtrail-logs.md").

- Centralize monitoring by configuring Amazon EventBridge and Amazon Simple Notification Service (Amazon SNS) to send
  notifications about service execution success.

For information about using EventBridge to monitor Systems Manager events, see [Monitoring Systems Manager events with
Amazon EventBridge](monitoring-eventbridge-events.md "monitoring-eventbridge-events.md").

###### About managed nodes

After you finish configuring your non-EC2 machines for Systems Manager as described in this
section, your hybrid-activated machines are listed in the AWS Management Console and described as
_managed nodes_. In the console, the IDs of your hybrid-activated
managed nodes are distinguished from Amazon EC2 instances with the prefix "mi-". Amazon EC2
instance IDs use the prefix "i-".

A managed node is any machine configured for Systems Manager. Previously, managed nodes were all
referred to as managed instances. The term _instance_ now
refers to EC2 instances only. The [deregister-managed-instance](../../../cli/latest/reference/ssm/deregister-managed-instance.md "../../../cli/latest/reference/ssm/deregister-managed-instance.md") command was named before this terminology
change.

For more information, see [Working with managed nodes](fleet-manager-managed-nodes.md "fleet-manager-managed-nodes.md").

###### Important

We strongly recommend that you avoid using OS versions that have reached End-of-Life (EOL).
OS vendors including AWS typically don't provide security patches or other updates for versions that have reached EOL.
Continuing to use an EOL system greatly increases the risk of not being able to apply upgrades, including security
fixes, and other operational problems. AWS does not test Systems Manager functionality on OS versions that have reached EOL.

###### About instance tiers

Systems Manager offers a standard-instances tier and an advanced-instances tier for non-EC2
managed nodes in your hybrid and multicloud environment. The standard-instances tier
allows you to register a maximum of 1,000 hybrid-activated machines per AWS account
per AWS Region. If you need to register more than 1,000 non-EC2 machines in a single
account and Region, then use the advanced-instances tier. Advanced instances also allow
you to connect to your non-EC2 machines by using AWS Systems Manager Session Manager. Session Manager provides
interactive shell access to your managed nodes.

For more information, see [Configuring instance
tiers](fleet-manager-configure-instance-tiers.md "fleet-manager-configure-instance-tiers.md").

###### Topics

- [Create the IAM service role required
  for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md")
- [Create a hybrid activation to register
  nodes with Systems Manager](hybrid-activation-managed-nodes.md "hybrid-activation-managed-nodes.md")
- [Install SSM Agent on hybrid
  Linux nodes](hybrid-multicloud-ssm-agent-install-linux.md "hybrid-multicloud-ssm-agent-install-linux.md")
- [Install SSM Agent on hybrid
  Windows Server nodes](hybrid-multicloud-ssm-agent-install-windows.md "hybrid-multicloud-ssm-agent-install-windows.md")
