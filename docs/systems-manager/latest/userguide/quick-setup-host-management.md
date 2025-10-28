# Set up Amazon EC2 host management using

Quick Setup

Use Quick Setup, a tool in AWS Systems Manager, to quickly configure required security roles
and commonly used Systems Manager tools on your Amazon Elastic Compute Cloud (Amazon EC2) instances. You can use
Quick Setup in an individual account or across multiple accounts and AWS Regions by
integrating with AWS Organizations. These tools help you manage and monitor the health of
your instances while providing the minimum required permissions to get started.

If you're unfamiliar with Systems Manager services and features, we recommend that you
review the _AWS Systems Manager User Guide_ before creating a
configuration with Quick Setup. For more information about Systems Manager, see [What is AWS Systems Manager?](what-is-systems-manager.md "what-is-systems-manager.md").

###### Important

Quick Setup might not be the right tool to use for EC2 management if either
of the following applies to you:

- You’re trying to create an EC2 instance for the first time to try
  out AWS capabilities.
- You’re still new to EC2 instance management.
  Instead, we recommend that you explore the following content:

- [Getting Started
  with Amazon EC2](https://aws.amazon.com/ec2/getting-started "https://aws.amazon.com/ec2/getting-started")
- [Launch an instance using the new launch instance wizard](../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md "../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md")
  in the _Amazon EC2 User Guide_
- [Tutorial: Get
  started with Amazon EC2 Linux instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md") in the
  _Amazon EC2 User Guide_
  If you’re already familiar with EC2 instance management and want to
  streamline configuration and management for multiple EC2 instances, use
  Quick Setup. Whether your organization has dozens, thousands, or millions of
  EC2 instances, use the following Quick Setup procedure to configure multiple
  options for them, all at once.

[Show moreShow less](# "#")###### Note

This configuration type lets you set multiple options for an entire
organization defined in AWS Organizations, only some organizational accounts and Regions,
or a single account. One of these options is to check for and apply updates to
SSM Agent every two weeks. If you are an organization administrator, you can also
choose to update _all_ EC2 instances in your organization
with agent updates every two weeks using the Default Host Management
Configuration type. For information, see [Set up the
Default Host Management Configuration for an organization using Quick Setup](quick-setup-default-host-management-configuration.md "quick-setup-default-host-management-configuration.md").

## Configuring host management

options for EC2 instances

To set up host management, perform the following tasks in the AWS Systems Manager
Quick Setup console.

###### To open the Host Management configuration page

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Quick Setup**.
3. On the **Host Management** card, choose
   **Create**.

###### Tip

If you already have one or more configurations in your account,
first choose the **Library** tab or the
**Create** button in the
**Configurations** section to view the
cards.

###### To configure Systems Manager host management options

- To configure Systems Manager functionality, in the **Configuration
  options** section, choose the options in the
  **Systems Manager** group that you want to enable for your
  configuration:

 

**Update Systems Manager (SSM) Agent every two weeks**

Enables Systems Manager to check every two weeks for a new version
of the agent. If there is a new version, then Systems Manager
automatically updates the agent on your managed node to the
latest released version. Quick Setup doesn't install the agent
on instances where it's not already present. For information
about which AMIs have SSM Agent preinstalled, see [Find AMIs with the SSM Agent
preinstalled](ami-preinstalled-agent.md "ami-preinstalled-agent.md").

We encourage you to choose this option to ensure that your
nodes are always running the most up-to-date version of
SSM Agent. For more information about SSM Agent, including
information about how to manually install the agent, see
[Working with SSM Agent](ssm-agent.md "ssm-agent.md").

**Collect inventory from your instances every 30 minutes**

Enables Quick Setup to configure collection of the following
types of metadata:

    + **AWS components**
     – EC2 driver, agents, versions, and
     more.
    + **Applications**
     – Application names, publishers, versions,
     and more.
    + **Node details**
     – System name, operating system (OS) name, OS
     version, last boot, DNS, domain, work group, OS
     architecture, and more.
    + **Network
     configuration** – IP address, MAC
     address, DNS, gateway, subnet mask, and more.
    + **Services** –
     Name, display name, status, dependent services,
     service type, start type, and more (Windows Server nodes
     only).
    + **Windows roles**
     – Name, display name, path, feature type,
     installed state, and more (Windows Server nodes
     only).
    + **Windows updates**
     – Hotfix ID, installed by, installed date,
     and more (Windows Server nodes only).

For more information about Inventory, a tool in AWS Systems Manager,
see [AWS Systems Manager Inventory](systems-manager-inventory.md "systems-manager-inventory.md").

###### Note

The **Inventory collection** option
can take up to 10 minutes to complete, even if you only
selected a few nodes.

**Scan instances for missing patches daily**

Enables Patch Manager, a tool in Systems Manager, to scan your nodes
daily and generate a report in the
**Compliance** page. The report shows
how many nodes are patch-compliant according to the
_default patch baseline_. The report
includes a list of each node and its compliance status.

For information about patching operations and patch
baselines, see [AWS Systems Manager Patch Manager](patch-manager.md "patch-manager.md").

For information about patch compliance, see the Systems Manager
[Compliance](https://console.aws.amazon.com/systems-manager/compliance "https://console.aws.amazon.com/systems-manager/compliance") page.

For information about patching managed nodes in multiple
accounts and Regions in one configuration, see [Patch policy configurations in Quick Setup](patch-manager-policies.md "patch-manager-policies.md") and [Configure patching for instances in an
organization using a Quick Setup patch policy](quick-setup-patch-manager.md "quick-setup-patch-manager.md").

###### Important

Systems Manager supports several methods for scanning managed
nodes for patch compliance. If you implement more than
one of these methods at a time, the patch compliance
information you see is always the result of the most
recent scan. Results from previous scans are
overwritten. If the scanning methods use different patch
baselines, with different approval rules, the patch
compliance information can change unexpectedly. For more
information, see [Identifying the
execution that created patch compliance data](patch-manager-compliance-data-overwrites.md "patch-manager-compliance-data-overwrites.md").

###### To configure Amazon CloudWatch host management options

- To configure CloudWatch functionality, in the **Configuration
  options** section, choose the options in the
  **Amazon CloudWatch** group that you want to enable for your
  configuration:

 

**Install and configure the CloudWatch agent**

Installs the basic configuration of the unified CloudWatch agent on
your Amazon EC2 instances. The agent collects metrics and log
files from your instances for Amazon CloudWatch. This information is
consolidated so you can quickly determine the health of your
instances. For more information about the CloudWatch agent basic
configuration, see [CloudWatch agent predefined metric sets](../../../AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.md#cloudwatch-agent-preset-metrics "../../../AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.md#cloudwatch-agent-preset-metrics"). There
might be added cost. For more information, see [Amazon CloudWatch
pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

**Update the CloudWatch agent once every 30 days**

Enables Systems Manager to check every 30 days for a new version of
the CloudWatch agent. If there is a new version, Systems Manager updates the
agent on your instance. We encourage you to choose this
option to ensure that your instances are always running the
most up-to-date version of the CloudWatch agent.

###### To configure Amazon EC2 Launch Agent host management options

- To configure Amazon EC2 Launch Agent functionality, in the
  **Configuration options** section, choose the
  options in the **Amazon EC2 Launch Agent** group that you
  want to enable for your configuration:

 

**Update the EC2 launch agent once every 30 days**

Enables Systems Manager to check every 30 days for a new version of
the launch agent installed on your instance. If a new
version is available, Systems Manager updates the agent on your
instance. We encourage you to choose this option to ensure
that your instances are always running the most up-to-date
version of the applicable launch agent. For Amazon EC2 Windows
instances, this option supports EC2Launch, EC2Launch v2, and
EC2Config. For Amazon EC2 Linux instances, this option supports
`cloud-init`. For Amazon EC2 Mac instances, this
option supports `ec2-macos-init`. Quick Setup
doesn't support updating launch agents that are installed on
operating systems not supported by the launch agent, or on
AL2023.

For more information about these initialization agents see
the following topics:

    + [Configure a Windows instance using
     EC2Launch v2](../../../AWSEC2/latest/WindowsGuide/ec2launch-v2.md "../../../AWSEC2/latest/WindowsGuide/ec2launch-v2.md")
    + [Configure a Windows instance using
     EC2Launch](../../../AWSEC2/latest/WindowsGuide/ec2launch.md "../../../AWSEC2/latest/WindowsGuide/ec2launch.md")
    + [Configure a Windows instance using the EC2Config
     service](../../../AWSEC2/latest/WindowsGuide/ec2config-service.md "../../../AWSEC2/latest/WindowsGuide/ec2config-service.md")
    + [cloud-init Documentation](https://cloudinit.readthedocs.io/en/22.2.2/index.html "https://cloudinit.readthedocs.io/en/22.2.2/index.html")
    + [ec2-macos-init](https://github.com/aws/ec2-macos-init "https://github.com/aws/ec2-macos-init")

###### To select the EC2 instances to be updated by the host management

configuration

- In the **Targets** section, choose the method to
  determine the accounts and Regions where the configuration is to be
  deployed:

###### Note

You can't create multiple Quick Setup Host Management configurations
that target the same AWS Region.

Entire organization
Your configuration is deployed to all organizational units
(OUs) and AWS Regions in your organization.

###### Note

The **Entire organization** option is
only available if you're configuring host management
from your organization's management account.

Custom

    1. In the **Target OUs** section,
     select the OUs where you want to deploy this host
     management configuration.
    2. In the **Target Regions**
     section, select the Regions where you want to deploy
     this host management configuration.

Current account
Choose one of the Region options and follow the steps for
that option.

 

**Current Region**

Choose how to target instances in the current
Region only:

    + **All instances** –
     The host management configuration automatically
     targets every EC2 in the current Region.
    + **Tag** – Choose
     **Add** and enter the key and
     optional value that is added to the instances to
     be targeted.
    + **Resource group** –
     For **Resource group**, select an
     existing resource group that contains the EC2
     instances to be targeted.
    + **Manual** – In the
     **Instances** section, select the
     check box of each EC2 instance to be
     targeted.

**Choose Regions**

Choose how to target instances in the Region
you specify by choosing one of the
following:

    + **All instances** –
     All instances in the Regions you specify are
     targeted.
    + **Tag** – Choose
     **Add** and enter the key and
     optional value that has been added to the
     instances to be targeted.

In the **Target Regions**
section, select the Regions where you want to
deploy this host management configuration.

###### To specify an instance profile option

- **\*Entire organization** and
  **Custom** targets only.\*

In the **Instance profile options** section, choose
whether you want to add the required IAM policies to the existing
instance profiles attached to your instances, or to allow Quick Setup to
create the IAM policies and instance profiles with the permissions
needed for the configuration you choose.

After specifying all your configuration choices, choose
**Create**.
