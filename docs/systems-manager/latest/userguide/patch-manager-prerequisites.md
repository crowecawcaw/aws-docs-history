AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Patch Manager prerequisites

Make sure that you have met the required prerequisites before using Patch Manager, a tool
in AWS Systems Manager.

###### Topics

- [SSM Agent version](#agent-versions "#agent-versions")
- [Python version](#python-version "#python-version")
- [Connectivity to the patch source](#source-connectivity "#source-connectivity")
- [S3 endpoint access](#s3-endpoint-access "#s3-endpoint-access")
- [Permissions to install patches
  locally](#local-installation-permissions "#local-installation-permissions")
- [Supported operating systems for Patch Manager](#supported-os "#supported-os")

## SSM Agent version

Version 2.0.834.0 or later of SSM Agent is running on the
managed node you want to manage with Patch Manager.

###### Note

An updated version of SSM Agent is released whenever new tools are added to Systems Manager or
updates are made to existing tools. Failing to use the latest version of the agent can
prevent your managed node from using various Systems Manager tools and features. For that reason, we
recommend that you automate the process of keeping SSM Agent up to date on your machines. For
information, see [Automating updates to SSM Agent](ssm-agent-automatic-updates.md "ssm-agent-automatic-updates.md"). Subscribe to the [SSM Agent
Release Notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md") page on GitHub to get notifications about SSM Agent
updates.

## Python version

For macOS and most Linux operating systems (OSs), Patch Manager currently supports
Python versions 2.6 - 3.12. The AlmaLinux,
Debian Server, and Ubuntu Server OSs require a supported version of Python 3 (3.0 -
3.12).

## Connectivity to the patch source

If your managed nodes don't have a direct connection to the Internet and you're
using an Amazon Virtual Private Cloud (Amazon VPC) with a VPC endpoint, you must ensure that the nodes have
access to the source patch repositories (repos). On Linux nodes, patch updates are
typically downloaded from the remote repos configured on the node. Therefore, the
node must be able to connect to the repos so the patching can be performed. For more
information, see [How security patches are
selected](patch-manager-selecting-patches.md "patch-manager-selecting-patches.md").

When patching a node that is running in an IPv6 only environment, ensure that the
node has connectivity to the patch source. You can check the Run Command output from
the patching execution to check for warnings about inaccessible repositories. For
DNF-based operating systems, it is possible to configure unavailable repositories to
be skipped during patching if the `skip_if_unavailable` option is set to
`True` under `/etc/dnf/dnf.conf`. DNF-based
operating systems include Amazon Linux 2023, Red Hat Enterprise Linux 8 and later versions, Oracle Linux
8 and later versions, Rocky Linux, AlmaLinux, & CentOS 8 and later versions. On
Amazon Linux 2023, the `skip_if_unavailable` option is set to
`True` by default.

###### CentOS Stream: Enable the `EnableNonSecurity`

flag

CentOS Stream nodes uses DNF as the package manager, which uses
the concept of an update notice. An update notice is simply a collection of
packages that fix specific problems.

However, CentOS Stream default repos aren't configured with an
update notice. This means that Patch Manager doesn't detect packages on default
CentOS Stream repos. To allow Patch Manager to process packages that
aren't contained in an update notice, you must turn on the
`EnableNonSecurity` flag in the patch baseline rules.

###### Windows Server: Ensure connectivity to Windows Update Catalog or Windows Server

Update Services (WSUS)

Windows Server managed nodes must be able to connect to the Windows Update Catalog
or Windows Server Update Services (WSUS). Confirm that your nodes have
connectivity to the [Microsoft Update
Catalog](https://www.catalog.update.microsoft.com/home.aspx "https://www.catalog.update.microsoft.com/home.aspx") through an internet gateway, NAT gateway, or NAT instance.
If you are using WSUS, confirm that the node has connectivity to the WSUS server
in your environment. For more information, see [Issue: managed
node doesn't have access to Windows Update Catalog or WSUS](patch-manager-troubleshooting.md#patch-manager-troubleshooting-instance-access "patch-manager-troubleshooting.md#patch-manager-troubleshooting-instance-access").

## S3 endpoint access

Whether your managed nodes operate in a private or public network, without access
to the required AWS managed Amazon Simple Storage Service (Amazon S3) buckets, patching operations fail. For
information about the S3 buckets your managed nodes must be able to access, see
[SSM Agent communications with
AWS managed S3 buckets](ssm-agent-technical-details.md#ssm-agent-minimum-s3-permissions "ssm-agent-technical-details.md#ssm-agent-minimum-s3-permissions") and [Improve the security of EC2 instances by using VPC
endpoints for Systems Manager](setup-create-vpc.md "setup-create-vpc.md").

## Permissions to install patches

locally

On Windows Server and Linux operating systems, Patch Manager assumes the Administrator and
root user accounts, respectively, to install patches.

On macOS, however, for Brew and Brew Cask, Homebrew doesn't support its commands
running under the root user account. As a result, Patch Manager queries for and runs
Homebrew commands as either the owner of the Homebrew directory, or as a valid user
belonging to the Homebrew directory’s owner group. Therefore, in order to install
patches, the owner of the `homebrew` directory also needs
recursive owner permissions for the `/usr/local`
directory.

###### Tip

The following command provides this permission for the specified user:

```
sudo chown -R `$USER`:admin /usr/local
```

## Supported operating systems for Patch Manager

The Patch Manager tool might not support all the same operating systems versions that
are supported by other Systems Manager tools. (For the full list of Systems Manager-supported operating
systems, see [Supported operating systems for
Systems Manager](operating-systems-and-machine-types.md#prereqs-operating-systems "operating-systems-and-machine-types.md#prereqs-operating-systems").) Therefore, ensure that the managed
nodes you want to use with Patch Manager are running one of the operating systems listed
in the following table.

###### Note

Patch Manager relies on the patch repositories that are configured on a managed
node, such as Windows Update Catalog and Windows Server Update Services for
Windows, to retrieve available patches to install. Therefore, for end of life
(EOL) operating system versions, if no new updates are available, Patch Manager might
not be able to report on the new updates. This can be because no new updates are
released by the Linux distribution maintainer, Microsoft, or Apple, or because
the managed node does not have the proper license to access the new
updates.

We strongly recommend that you avoid using OS versions that have reached End-of-Life (EOL).
OS vendors including AWS typically don't provide security patches or other updates for versions that have reached EOL.
Continuing to use an EOL system greatly increases the risk of not being able to apply upgrades, including security
fixes, and other operational problems. AWS does not test Systems Manager functionality on OS versions that have reached EOL.

Patch Manager reports compliance status against the available patches on the
managed node. Therefore, if an instance is running an EOL operating system, and
no updates are available, Patch Manager might report the node as Compliant, depending
on the patch baselines configured for the patching operation.

| Operating system | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux            | • AlmaLinux 8*.x*,<br>9*.x*<br>• Amazon Linux 2 version 2.0 and all later versions<br>• Amazon Linux 2023<br>• CentOS Stream 9<br>• Debian Server 11*.x*,<br>and 12*.x*<br>• Oracle Linux 7.5–8*.x*, 9*.x*<br>• Red Hat Enterprise Linux (RHEL) 7.x–8*.x*, 9*.x*, 10._x_<br>• Rocky Linux 8*.x*,<br>9*.x*<br>• SUSE Linux Enterprise Server 15.3 and later<br>• Ubuntu Server 16.04 LTS, 18.04 LTS, 20.04 LTS, 22.04<br>LTS, 24.04 LTS, and 25.04                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| macOS            | _macOS is supported for Amazon EC2<br>instances only._<br>13.0–13.7 (Ventura)<br>14*.x<br>• (Sonoma)<br>15.*x<br>• (Sequoia)<br>macOS OS updates<br>Patch Manager doesn't support operating system (OS) updates or<br>upgrades for macOS, such as from 13.1 to 13.2. To perform<br>OS version updates on macOS, we recommend using Apple's<br>built-in OS upgrade mechanisms. For more information, see<br>[Device Management](https://developer.apple.com/documentation/devicemanagement "https://developer.apple.com/documentation/devicemanagement") on the Apple Developer<br>Documentation website.<br>Homebrew support<br>Patch Manager requires Homebrew, the open-source software<br>package management system, to be installed at either of the<br>following default install locations:<br>• `/usr/local/bin`<br>• `/opt/homebrew/bin`<br>Patching operations using Patch Manager fail to function correctly<br>when Homebrew is not installed.<br>Region support<br>macOS is not supported in all AWS Regions. For more<br>information about Amazon EC2 support for macOS, see [Amazon EC2 Mac instances](../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md "../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md") in the<br>_Amazon EC2 User Guide_.<br>macOS edge devices<br>SSM Agent for AWS IoT Greengrass core devices is not supported on<br>macOS. You can't use Patch Manager to patch macOS edge<br>devices. |
| Windows          | Windows Server 2012 through Windows Server 2025, including R2<br>versions.<br>NoteSSM Agent for AWS IoT Greengrass core devices is not supported on<br>Windows 10. You can't use Patch Manager to patch Windows 10 edge<br>devices.<br>Windows Server 2012 and 2012 R2 support<br>Windows Server 2012 and 2012 R2 reached end of support on<br>October 10, 2023. To use Patch Manager with these versions, we<br>recommend also using Extended Security Updates (ESUs) from<br>Microsoft. For more information, see [Windows Server 2012 and 2012 R2 reaching end of<br>support](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-server-2012-r2-end-of-support "https://learn.microsoft.com/en-us/lifecycle/announcements/windows-server-2012-r2-end-of-support") on the Microsoft website.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
