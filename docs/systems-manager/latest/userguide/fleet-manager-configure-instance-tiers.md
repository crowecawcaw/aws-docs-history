• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Configuring instance

tiers

This topic describes the scenarios when you must activate the advanced-instanced
tier.

AWS Systems Manager offers a standard-instances tier and an advanced-instances tier for
non-EC2 machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment.

You can register up to 1,000 standard [hybrid-activated
nodes](activations.md "activations.md") per account per AWS Region at no additional cost. However,
registering more than 1,000 hybrid nodes requires that you activate the
advanced-instances tier. There is a charge to use the advanced-instances tier. For
more information, see [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

Even with fewer than 1,000 registered hybrid-activated nodes, two other scenarios
require the advanced-instances tier:

- You want to use Session Manager to connect to non-EC2 nodes.
- You want to patch applications (not operating systems) released by
  Microsoft on non-EC2 nodes.

###### Note

There is no charge to patch applications released by Microsoft on
Amazon EC2 instances.

## Advanced-instances tier detailed scenarios

The following information provides details on the three scenarios for which
you must activate the advanced-instances tier.

Scenario 1: You want to register more than 1,000 hybrid-activated
nodes

Using the standard-instances tier, you can register a maximum of
1,000 non-EC2 nodes in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment per AWS Region in
a specific account without additional charge. If you need to
register more than 1,000 non-EC2 nodes in a Region, you must use the
advanced-instances tier. You can then activate as many machines for
your hybrid and multicloud environment as you want. Charges for the
advanced-instances tier are based on the number of advanced nodes
activated as Systems Manager managed nodes and the hours those nodes are
running.

All Systems Manager managed nodes that use the activation process described
in [Create a hybrid activation to register nodes with Systems Manager](hybrid-activation-managed-nodes.md "hybrid-activation-managed-nodes.md")
are then subject to charge if you exceed 1,000 on-premises nodes in
a Region in a specific account .

###### Note

You can also activate existing Amazon Elastic Compute Cloud (Amazon EC2) instances
using Systems Manager hybrid activations and work with them as non-EC2
instances, such as for testing. These also qualify as hybrid
nodes. This isn't a common scenario.

Scenario 2: Patching Microsoft-released applications on
hybrid-activated nodes

The advanced-instances tier is also required if you want to patch
Microsoft-released applications on non-EC2 nodes in a hybrid and
multicloud environment. If you activate the advanced-instances tier
to patch Microsoft applications on non-EC2 nodes, charges are then
incurred for all on-premises nodes, even if you have fewer than
1,000.

There is no additional charge to patch applications released by
Microsoft on Amazon Elastic Compute Cloud (Amazon EC2) instances. For more information, see
[Patching applications
released by Microsoft on Windows Server](patch-manager-patching-windows-applications.md "patch-manager-patching-windows-applications.md").

Scenario 3: Connecting to hybrid-activated nodes using Session Manager

Session Manager provides interactive shell access to your instances. To
connect to hybrid-activated managed nodes using Session Manager, you must
activate the advanced-instances tier. Charges are then incurred for
all hybrid-activated nodes, even if you have fewer than
1,000.

###### Summary: When do I need the advanced-instances tier?

Use the following table to review when you must use the advanced-instances
tier, and for which scenarios additional charges apply.

| Scenario                                                                                                                                                                                                                                                                  | Advanced-instances tier required? | Additional charges apply? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------------------------- |
| The number of hybrid-activated nodes in my Region in a<br>specific account is more than 1,000.                                                                                                                                                                            | Yes                               | Yes                       |
| I want to use Patch Manager to patch Microsoft-released<br>applications on any number of hybrid-activated nodes, even<br>less than 1,000.                                                                                                                                 | Yes                               | Yes                       |
| I want to use Session Manager to connect to any number of<br>hybrid-activated nodes, even less than 1,000.                                                                                                                                                                | Yes                               | Yes                       |
| 1. The number of hybrid-activated nodes in a Region<br>in a specific account is 1,000 or less; and<br>2. I am not patching Microsoft applications on any<br>hybrid-activated nodes; and<br>3. I am not connecting to any hybrid-activated nodes<br>using Session Manager. | No                                | No                        |

###### Topics

- [Turning on the
  advanced-instances tier](fleet-manager-enable-advanced-instances-tier.md "fleet-manager-enable-advanced-instances-tier.md")
- [Reverting from the
  advanced-instances tier to the standard-instances tier](fleet-manager-revert-to-standard-tier.md "fleet-manager-revert-to-standard-tier.md")
