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

###### Note

**Important:** Effective June 30, 2026, the
advanced-instances tier has been removed. There is no longer a 1,000-instance limit for
hybrid managed nodes, and you no longer need to enable a paid tier to use Session Manager on
non-EC2 machines. Instead, starting September 30, 2026, Session Manager and Run Command use pay-as-you-go pricing
when used on hybrid managed nodes.

For more information about pricing, see [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

###### Display managed nodes

If you don't see your managed nodes listed in the console, then do the
following:

1. Verify that the console is open in the AWS Region where you created your
   managed nodes. You can switch Regions by using the list in the top, right corner
   of the console.
2. Verify that the setup steps for your managed nodes meet Systems Manager requirements.
   For information, see [Setting up managed nodes for AWS Systems Manager](systems-manager-setting-up-nodes.md "systems-manager-setting-up-nodes.md").
3. For non-EC2 machines, verify that you completed the hybrid activation process.
   For more information, see [Managing nodes in hybrid and multicloud environments with Systems Manager](systems-manager-hybrid-multicloud.md "systems-manager-hybrid-multicloud.md").
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
  resolved. For troubleshooting tips, see [Troubleshooting managed node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md").

###### Verify Systems Manager support on a managed node

AWS Config provides AWS Managed Rules, which are predefined, customizable rules that
AWS Config uses to evaluate whether your AWS resource configurations comply with
common best practices. AWS Config Managed Rules include the [ec2-instance-managed-by-systems-manager](../../../config/latest/developerguide/ec2-instance-managed-by-systems-manager.md "../../../config/latest/developerguide/ec2-instance-managed-by-systems-manager.md") rule. This rule checks whether
the Amazon EC2 instances in your account are managed by Systems Manager. For more information, see
[AWS Config
Managed Rules](../../../config/latest/developerguide/evaluate-config_use-managed-rules.md "../../../config/latest/developerguide/evaluate-config_use-managed-rules.md").

###### Increase security posture on managed nodes

For information about increasing your security posture against unauthorized
root-level commands on your managed nodes, see [Restricting access to root-level commands through SSM Agent](ssm-agent-restrict-root-level-commands.md "ssm-agent-restrict-root-level-commands.md").

###### Deregister managed nodes

You can deregister managed nodes at any time. For example, if you're managing
multiple nodes with the same AWS Identity and Access Management (IAM) role and you notice any kind of
malicious behavior, you can deregister any number of machines at any point. (In
order to re-register the same machine, you must use a different hybrid Activation
Code and Activation ID than previously used to register it.) For information about
deregistering managed nodes, see [Deregistering managed nodes in a hybrid and multicloud environment](fleet-manager-deregister-hybrid-nodes.md "fleet-manager-deregister-hybrid-nodes.md").

###### Topics

- [Resetting passwords on managed nodes](fleet-manager-reset-password.md "fleet-manager-reset-password.md")
- [Deregistering managed nodes in a hybrid and multicloud environment](fleet-manager-deregister-hybrid-nodes.md "fleet-manager-deregister-hybrid-nodes.md")
- [Working with OS file systems using Fleet Manager](fleet-manager-file-system-management.md "fleet-manager-file-system-management.md")
- [Monitoring managed node performance](fleet-manager-monitoring-node-performance.md "fleet-manager-monitoring-node-performance.md")
- [Working with processes](fleet-manager-manage-processes.md "fleet-manager-manage-processes.md")
- [Viewing logs on managed nodes](fleet-manager-view-node-logs.md "fleet-manager-view-node-logs.md")
- [Managing OS user accounts and groups on managed nodes using Fleet Manager](fleet-manager-manage-os-user-accounts.md "fleet-manager-manage-os-user-accounts.md")
- [Managing the Windows registry on managed nodes](fleet-manager-manage-windows-registry.md "fleet-manager-manage-windows-registry.md")
