• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# AWS Systems Manager Hybrid Activations

To configure non-EC2 machines for use with AWS Systems Manager in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment, you
create a _hybrid activation_. Non-EC2 machine types
supported as managed nodes include the following:

- Servers on your own premises (on-premises servers)
- AWS IoT Greengrass core devices
- AWS IoT and non-AWS edge devices
- Virtual machines (VMs), including VMs in other cloud environments
  When you run the [create-activation](../../../cli/latest/reference/ssm/create-activation.md "../../../cli/latest/reference/ssm/create-activation.md") command to start a hybrid activation
  process, you receive an activation code and ID in the command response. You then include the
  activation code and ID with the command to install SSM Agent on the machine, as described in
  step 3 of [Install SSM Agent on hybrid
  Linux nodes](hybrid-multicloud-ssm-agent-install-linux.md "hybrid-multicloud-ssm-agent-install-linux.md") and step 4 of [Install SSM Agent on hybrid
  Windows Server nodes](hybrid-multicloud-ssm-agent-install-windows.md "hybrid-multicloud-ssm-agent-install-windows.md").

This activation process applies to all non-EC2 machine types _except_ AWS IoT Greengrass core devices. For information about configuring AWS IoT Greengrass
core devices for Systems Manager, see [Managing edge devices with
Systems Manager](systems-manager-setting-up-edge-devices.md "systems-manager-setting-up-edge-devices.md").

###### Note

Support isn't currently provided for non-EC2 macOS machines.

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
