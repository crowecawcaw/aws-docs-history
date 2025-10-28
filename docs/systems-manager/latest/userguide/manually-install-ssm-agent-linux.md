# Manually installing and

uninstalling SSM Agent on EC2 instances for Linux

Before you manually install AWS Systems Manager Agent (SSM Agent) on an Amazon Elastic Compute Cloud (Amazon EC2)
Linux operating system, review the following information.

###### Installation on other machine types

The procedures in this section are designed specifically for Amazon EC2 instances.
For on-premises servers, virtual machines, or other non-EC2 environments, use
the `ssm-setup-cli` tool as described in [How to install the SSM Agent on hybrid Linux nodes](hybrid-multicloud-ssm-agent-install-linux.md "hybrid-multicloud-ssm-agent-install-linux.md").

Using EC2 installation procedures on non-EC2 systems can potentially result in
security vulnerabilities. The `ssm-setup-cli` tool provides
additional security protections for non-EC2 machines.

We strongly recommend that you avoid using OS versions that have reached End-of-Life (EOL).
OS vendors including AWS typically don't provide security patches or other updates for versions that have reached EOL.
Continuing to use an EOL system greatly increases the risk of not being able to apply upgrades, including security
fixes, and other operational problems. AWS does not test Systems Manager functionality on OS versions that have reached EOL.

###### SSM Agent installation file URLs

You can access the installation files for SSM Agent that are stored in any
commercial AWS Region. We also provide installation files in a globally
available Amazon Simple Storage Service (Amazon S3) bucket that you can use as an alternative or backup
source of files.

If you're manually installing the agent on a instance or two, you can use the
commands in the **Quick installation** procedures we
provide to save time. The commands provided in these procedures can also be passed
to Amazon EC2 instances as scripts through user data.

If you're creating a script or template to use for installing the agent on
multiple instances, we recommend that you use the installation files in or near an
AWS Region where you're geographically located. For bulk installations, this can
increase the speed of your downloads and reduce latency. In these cases, we
recommend using the **Create custom installation
commands** procedures in the installation topics.

###### Amazon Machine Images with the agent preinstalled

SSM Agent is preinstalled on some Amazon Machine Images (AMIs) provided by AWS.
For information, see [Find AMIs with the SSM Agent
preinstalled](ami-preinstalled-agent.md "ami-preinstalled-agent.md").

###### Keeping the agent up to date

An updated version of SSM Agent is released whenever new tools are added to Systems Manager or
updates are made to existing tools. Failing to use the latest version of the agent can
prevent your managed node from using various Systems Manager tools and features. For that reason, we
recommend that you automate the process of keeping SSM Agent up to date on your machines. For
information, see [Automating updates to SSM Agent](ssm-agent-automatic-updates.md "ssm-agent-automatic-updates.md"). Subscribe to the [SSM Agent
Release Notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md") page on GitHub to get notifications about SSM Agent
updates.

###### Choose your operating system

To view the procedure for manually installing SSM Agent on the specified
operating system, choose a link from the following list:

###### Note

For a list of supported versions of each of the following operating systems,
see [Supported operating systems for
Systems Manager](operating-systems-and-machine-types.md#prereqs-operating-systems "operating-systems-and-machine-types.md#prereqs-operating-systems").

- [AlmaLinux](agent-install-alma.md "agent-install-alma.md")
- [Amazon Linux 2 and Amazon Linux 2023](agent-install-al2.md "agent-install-al2.md")
- [Debian Server](agent-install-deb.md "agent-install-deb.md")
- [Oracle Linux](agent-install-oracle.md "agent-install-oracle.md")
- [Red Hat Enterprise Linux](agent-install-rhel.md "agent-install-rhel.md")
- [Rocky Linux](agent-install-rocky.md "agent-install-rocky.md")
- [Ubuntu Server](agent-install-ubuntu.md "agent-install-ubuntu.md")

## Uninstalling SSM Agent from Linux

instances

Use the package manager for your operating system to uninstall SSM Agent from
Linux instances. Depending on the operating system, the uninstall command will
be similar to the following example command:

```
sudo dpkg -r amazon-ssm-agent
```
