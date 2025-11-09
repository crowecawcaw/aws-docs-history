AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Working with managed nodes

A _managed node_ is any machine configured for AWS Systems Manager. You can
configure the following machine types as managed nodes:

- Amazon Elastic Compute Cloud (Amazon EC2) instances
- Servers on your own premises (on-premises servers)
- AWS IoT Greengrass core devices
- AWS IoT and non-AWS edge devices
- Virtual machines (VMs), including VMs in other cloud environments
  In the Systems Manager console, any machine prefixed with "mi-" has been configured as a managed
  node using a [hybrid
  activation](activations.md "activations.md"). Edge devices display their AWS IoT Thing
  name.

###### Note

The only supported feature for macOS instances is viewing the file system.

###### About Systems Manager instances tiers

AWS Systems Manager offers a standard-instances tier and an advanced-instances tier. Both
support managed nodes in your [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment. The standard-instances tier
allows you to register a maximum of 1,000 machines per AWS account per AWS Region.
If you need to register more than 1,000 machines in a single account and Region, then
use the advanced-instances tier. You can create as many managed nodes as you like in the
advanced-instances tier. All managed nodes configured for Systems Manager are priced on a
pay-per-use basis. For more information about enabling the advanced instances tier, see
[Turning on the
advanced-instances tier](fleet-manager-enable-advanced-instances-tier.md "fleet-manager-enable-advanced-instances-tier.md"). For more information
about pricing, see [AWS Systems Manager
Pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

Note the following additional information about the standard-instances tier and
advanced-instances tier:

- Advanced instances also allow you to connect to your non-EC2 nodes in a
  [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment by using AWS Systems Manager Session Manager. Session Manager provides interactive
  shell access to your instances. For more information, see [AWS Systems Manager Session Manager](session-manager.md "session-manager.md").
- The standard-instances quota also applies to EC2 instances that use a Systems Manager
  on-premises activation (which isn't a common scenario).
- To patch applications released by Microsoft on virtual machines (VMs) on-premises
  instances, activate the advanced-instances tier. There is a charge to use the
  advanced-instances tier. There is no additional charge to patch applications
  released by Microsoft on Amazon Elastic Compute Cloud (Amazon EC2) instances. For more information, see
  [Patching applications
  released by Microsoft on Windows Server](patch-manager-patching-windows-applications.md "patch-manager-patching-windows-applications.md").

###### Display managed nodes

If you don't see your managed nodes listed in the console, then do the
following:

1. Verify that the console is open in the AWS Region where you created your
   managed nodes. You can switch Regions by using the list in the top, right corner
   of the console.
2. Verify that the setup steps for your managed nodes meet Systems Manager requirements.
   For information, see [Setting up managed nodes for
   AWS Systems Manager](systems-manager-setting-up-nodes.md "systems-manager-setting-up-nodes.md").
3. For non-EC2 machines, verify that you completed the hybrid activation process.
   For more information, see [Managing nodes in hybrid and multicloud
   environments with Systems Manager](systems-manager-hybrid-multicloud.md "systems-manager-hybrid-multicloud.md").
   Note the following additional information:

- The Fleet Manager console does not display Amazon EC2 nodes that have been
  terminated.
- Systems Manager requires accurate time references in order to perform operations on your
  machines. If the date and time aren't set correctly on your managed nodes, the
  machines might not match the signature date of your API requests. For more
  information, see [Use cases and best practices](systems-manager-best-practices.md "systems-manager-best-practices.md").
- When you create or edit tags, the system can take up to one hour to display
  changes in the table filter.
- After the status of a managed node has been `Connection Lost` for
  at least 30 days, the node might no longer be listed in the Fleet Manager console. To
  restore it to the list, the issue that caused the lost connection must be
  resolved. For troubleshooting tips, see [Troubleshooting managed
  node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md").

###### Verify Systems Manager support on a managed node

AWS Config provides AWS Managed Rules, which are predefined, customizable rules that
AWS Config uses to evaluate whether your AWS resource configurations comply with
common best practices. AWS Config Managed Rules include the [ec2-instance-managed-by-systems-manager](../../../config/latest/developerguide/ec2-instance-managed-by-systems-manager.md "../../../config/latest/developerguide/ec2-instance-managed-by-systems-manager.md") rule. This rule checks whether
the Amazon EC2 instances in your account are managed by Systems Manager. For more information, see
[AWS Config
Managed Rules](../../../config/latest/developerguide/evaluate-config_use-managed-rules.md "../../../config/latest/developerguide/evaluate-config_use-managed-rules.md").

###### Increase security posture on managed nodes

For information about increasing your security posture against unauthorized
root-level commands on your managed nodes, see [Restricting access to
root-level commands through SSM Agent](ssm-agent-restrict-root-level-commands.md "ssm-agent-restrict-root-level-commands.md").

###### Deregister managed nodes

You can deregister managed nodes at any time. For example, if you're managing
multiple nodes with the same AWS Identity and Access Management (IAM) role and you notice any kind of
malicious behavior, you can deregister any number of machines at any point. (In
order to re-register the same machine, you must use a different hybrid Activation
Code and Activation ID than previously used to register it.) For information about
deregistering managed nodes, see [Deregistering managed nodes
in a hybrid and multicloud environment](fleet-manager-deregister-hybrid-nodes.md "fleet-manager-deregister-hybrid-nodes.md").

###### Topics

- [Configuring instance
  tiers](fleet-manager-configure-instance-tiers.md "fleet-manager-configure-instance-tiers.md")
- [Resetting passwords on managed
  nodes](fleet-manager-reset-password.md "fleet-manager-reset-password.md")
- [Deregistering managed nodes
  in a hybrid and multicloud environment](fleet-manager-deregister-hybrid-nodes.md "fleet-manager-deregister-hybrid-nodes.md")
- [Working with OS file systems
  using Fleet Manager](fleet-manager-file-system-management.md "fleet-manager-file-system-management.md")
- [Monitoring managed node
  performance](fleet-manager-monitoring-node-performance.md "fleet-manager-monitoring-node-performance.md")
- [Working with processes](fleet-manager-manage-processes.md "fleet-manager-manage-processes.md")
- [Viewing logs on managed nodes](fleet-manager-view-node-logs.md "fleet-manager-view-node-logs.md")
- [Managing OS user accounts
  and groups on managed nodes using Fleet Manager](fleet-manager-manage-os-user-accounts.md "fleet-manager-manage-os-user-accounts.md")
- [Managing the Windows
  registry on managed nodes](fleet-manager-manage-windows-registry.md "fleet-manager-manage-windows-registry.md")
