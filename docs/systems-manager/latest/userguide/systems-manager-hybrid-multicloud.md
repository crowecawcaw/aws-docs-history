# Managing nodes in hybrid and multicloud environments with Systems Manager

You can use AWS Systems Manager to manage Amazon Elastic Compute Cloud (Amazon EC2) instances alongside non-EC2
machines in hybrid and multicloud environments. Systems Manager supports on-premises servers, edge
devices, and virtual machines running in other cloud environments, including Microsoft
Azure.

This section describes the setup tasks that account and system administrators perform to
configure non-EC2 machines for use with Systems Manager in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment. After these
steps are complete, users who have been granted permissions by the AWS account
administrator can use Systems Manager to configure and manage their organization's non-EC2
machines.

Any machine that has been configured for use with Systems Manager is called a _managed node_.

Systems Manager provides two methods to onboard non-EC2 machines:

- **Cloud Connectors** – Automatically onboard
  and manage Azure virtual machines at scale from the AWS Management Console. Cloud Connectors
  handle identity federation, agent installation, and VM registration without
  requiring direct access to your Azure VMs. For more information, see [Set up a Cloud Connector for Microsoft Azure in Systems Manager](systems-manager-cloud-connector.md "systems-manager-cloud-connector.md").
- **Hybrid activations** – Register individual
  on-premises servers, edge devices, and VMs from any environment by manually
  installing SSM Agent and activating each machine. For more information, see [Create a hybrid activation to register nodes with Systems Manager](hybrid-activation-managed-nodes.md "hybrid-activation-managed-nodes.md").

###### Note

- You can register edge devices as managed nodes using the same
  hybrid-activation steps used for other non-EC2 machines. These types of edge
  devices include both AWS IoT devices and devices other than AWS IoT devices.
  Systems Manager also supports edge devices that use AWS IoT Greengrass Core software. The setup
  process and requirements for AWS IoT Greengrass core devices are different. For information
  about registering AWS IoT Greengrass devices for use with Systems Manager, see [Managing edge devices with Systems Manager](systems-manager-setting-up-edge-devices.md "systems-manager-setting-up-edge-devices.md").
- Non-EC2 macOS machines aren't supported for Systems Manager hybrid and multicloud
  environments.

###### Note

**Important:** Effective June 30, 2026, the
advanced-instances tier has been removed. There is no longer a 1,000-instance limit for
hybrid managed nodes, and you no longer need to enable a paid tier to use Session Manager on
non-EC2 machines. Instead, starting September 30, 2026, Session Manager and Run Command use pay-as-you-go pricing
when used on hybrid managed nodes.

For more information about pricing, see [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

If you plan to use Systems Manager to manage Amazon Elastic Compute Cloud (Amazon EC2) instances, or to use both Amazon EC2
instances and non-EC2 machines in hybrid and multicloud environment, follow the steps in
[Managing EC2 instances with Systems Manager](systems-manager-setting-up-ec2.md "systems-manager-setting-up-ec2.md") first.

After configuring your hybrid and multicloud environment for Systems Manager, you can do the
following:

- Create a consistent and secure way to remotely manage your hybrid and multicloud
  workloads from one location using the same tools or scripts.
- Centralize access control for actions that can be performed on your machines by
  using AWS Identity and Access Management (IAM).
- Centralize auditing and logging of the operations performed on your machines by
  viewing the API activity recorded in AWS CloudTrail.

For information about using CloudTrail to monitor Systems Manager actions, see [Logging AWS Systems Manager API calls with AWS CloudTrail](monitoring-cloudtrail-logs.md "monitoring-cloudtrail-logs.md").

- Centralize monitoring by configuring Amazon EventBridge and Amazon Simple Notification Service (Amazon SNS) to send
  notifications about service execution success.

For information about using EventBridge to monitor Systems Manager events, see [Monitoring Systems Manager events with Amazon EventBridge](monitoring-eventbridge-events.md "monitoring-eventbridge-events.md").

###### Onboarding with Cloud Connectors

A Cloud Connector is a Systems Manager resource that establishes a trust relationship between
your AWS account and a third-party cloud provider. With Cloud Connectors, you can
onboard and manage virtual machines from other cloud environments at scale directly from
the AWS Management Console without signing in to individual VMs, running scripts, or manually
installing agents.

When you create a Cloud Connector, Systems Manager discovers associated VMs, and installs SSM Agent on each VM. New
VMs that come online are enrolled automatically. After onboarding, VMs appear as managed
nodes in the unified Systems Manager console alongside your Amazon EC2 instances, and you can manage them
using the same Systems Manager capabilities you use for Amazon EC2.

Cloud Connectors currently support Microsoft Azure. For more information, see [Set up a Cloud Connector for Microsoft Azure in Systems Manager](systems-manager-cloud-connector.md "systems-manager-cloud-connector.md").

###### Onboarding with hybrid activations

A hybrid activation allows you to register individual on-premises servers, edge
devices, and VMs from any environment as managed nodes. With hybrid activations, you
create an activation in the Systems Manager console, install SSM Agent on each machine manually,
and register it using the activation code and ID.

Hybrid activations give you flexibility to onboard machines from any environment, including
on-premises data centers, edge locations, and cloud providers that aren't yet supported by
Cloud Connectors. After registration, the machines appear as managed nodes and support the
same Systems Manager capabilities as Amazon EC2 instances.

For more information, see [Create a hybrid activation to register nodes with Systems Manager](hybrid-activation-managed-nodes.md "hybrid-activation-managed-nodes.md").

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

Effective June 30, 2026, the Advanced Instances Tier has been removed. There is no
longer a 1,000-instance limit for hybrid managed nodes, and you no longer need to enable
a paid tier to use Session Manager on non-EC2 machines. Instead, Session Manager, Run
Command, and Patch Manager use pay-as-you-go pricing when used on hybrid managed
nodes.

For more information about pricing, see [AWS Systems Manager
pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

###### Topics

- [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md")
- [Create a hybrid activation to register nodes with Systems Manager](hybrid-activation-managed-nodes.md "hybrid-activation-managed-nodes.md")
- [Install SSM Agent on hybrid Linux nodes](hybrid-multicloud-ssm-agent-install-linux.md "hybrid-multicloud-ssm-agent-install-linux.md")
- [Install SSM Agent on hybrid Windows Server nodes](hybrid-multicloud-ssm-agent-install-windows.md "hybrid-multicloud-ssm-agent-install-windows.md")
- [Set up Systems Manager for Microsoft Azure virtual machines](hybrid-multicloud-ssm-agent-install-azure.md "hybrid-multicloud-ssm-agent-install-azure.md")
