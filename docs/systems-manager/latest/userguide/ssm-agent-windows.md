# Working with SSM Agent on EC2 instances for

Windows Server

AWS Systems Manager Agent (SSM Agent) is preinstalled, by default, on the Amazon Machine Images (AMIs)
for Windows Server that are provided by AWS. Support is provided for the following operating
system (OS) versions.

- Windows Server 2012 R2 AMIs published in November 2016 or later
- Windows Server 2016, 2019, 2022 (excluding Nano versions), and 2025

###### Support notes for previous versions

Windows Server AMIs published _before_ November 2016 use the
EC2Config service to process requests and configure instances.

Unless you have a specific reason for using the EC2Config service, or an earlier
version of SSM Agent, to process Systems Manager requests, we recommend that you download and
install the latest version of SSM Agent to each of your Amazon Elastic Compute Cloud (Amazon EC2) instances or
non-EC2 machines that are configured for Systems Manager in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment.

###### Keeping SSM Agent up to date

An updated version of SSM Agent is released whenever new tools are added to Systems Manager or
updates are made to existing tools. Failing to use the latest version of the agent can
prevent your managed node from using various Systems Manager tools and features. For that reason, we
recommend that you automate the process of keeping SSM Agent up to date on your machines. For
information, see [Automating updates to SSM Agent](ssm-agent-automatic-updates.md "ssm-agent-automatic-updates.md"). Subscribe to the [SSM Agent
Release Notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md") page on GitHub to get notifications about SSM Agent
updates.

To view details about the different versions of SSM Agent, see the [release
notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md").

###### Topics

- [Manually installing and
  uninstalling SSM Agent on EC2 instances for Windows Server](manually-install-ssm-agent-windows.md "manually-install-ssm-agent-windows.md")
- [Configure SSM Agent to use a
  proxy for Windows Server instances](configure-proxy-ssm-agent-windows.md "configure-proxy-ssm-agent-windows.md")
