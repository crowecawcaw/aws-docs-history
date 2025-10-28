# Install the latest version of

EC2Launch v2

You can use one of the following methods to install the
EC2Launch v2 agent on your EC2 instance:

- Download the agent from Amazon S3 and install with Windows PowerShell.
  For download URLs, see [EC2Launch v2 downloads on Amazon S3](#lv2-download-s3 "#lv2-download-s3").
- Install with SSM Distributor.
- Install from an EC2 Image Builder component when you create a custom image.
- Launch your instance from an AMI that has EC2Launch v2 pre-installed.

###### Warning

AmazonEC2Launch.msi uninstalls previous versions of the EC2 launch services, such
as EC2Launch (v1) and EC2Config.

For install steps, select the tab that matches your preferred method.

PowerShell
To install the latest version of EC2Launch v2 agent with Windows PowerShell,
follow these steps.

1. Create your local directory.

```
New-Item -Path "$env:USERPROFILE\Desktop\EC2Launchv2" -ItemType Directory
```

2. Set the URL for your download location. Run the following command
   with the Amazon S3 URL you'll use. For download URLs, see [EC2Launch v2 downloads on Amazon S3](#lv2-download-s3 "#lv2-download-s3")

```
$Url = "`Amazon S3 URL`/AmazonEC2Launch.msi"
```

3. Use the following compound command to download the agent and run the
   install

```
$DownloadFile = "$env:USERPROFILE\Desktop\EC2Launchv2\" + $(Split-Path -Path $Url -Leaf)
Invoke-WebRequest -Uri $Url -OutFile $DownloadFile
msiexec /i "$DownloadFile"
```

###### Note

If you receive an error when downloading the file, and you
are using Windows Server 2016 or earlier, TLS 1.2 might need
to be enabled for your PowerShell terminal. You can enable
TLS 1.2 for the current PowerShell session with the
following command and then try again:

```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

4. The **msiexec** command installs EC2Launch v2 in the following location
   on Windows Server instances: `%ProgramFiles%\Amazon\EC2Launch`. To
   verify that the install ran, you can check the local file system on your instance.

AWS Systems Manager Distributor
To configure automatic updates for EC2Launch v2 with AWS Systems Manager Quick Setup, see
[Automatically install and update with Distributor Quick Setup](#lv2-distributor-quick-setup "#lv2-distributor-quick-setup").

You can also perform a one-time install of the `AWSEC2Launch-Agent` package from AWS Systems Manager
Distributor. For instructions on how to install a package from Systems Manager Distributor,
see [Install or update packages](../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md "../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md") in the _AWS Systems Manager User
Guide_.

EC2 Image Builder component
You can install the `ec2launch-v2-windows` component when you build a
custom image with EC2 Image Builder. For instructions on how to build a custom image with
EC2 Image Builder, see [Create an
image pipeline using the EC2 Image Builder console wizard](../../../imagebuilder/latest/userguide/start-build-image-pipeline.md "../../../imagebuilder/latest/userguide/start-build-image-pipeline.md") in the
_EC2 Image Builder User Guide_.

AMI
EC2Launch v2 is preinstalled by default on AMIs for the Windows Server 2022 and
above operating systems:

- Windows_Server-`version`-English-Full-Base
- Windows_Server-`version`-English-Core-Base
- Windows_Server-`version`-English-Core-EKS_Optimized
- Windows Server `version` AMIs with all other languages
- Windows Server `version` AMIs with SQL installed

EC2Launch v2 is also preinstalled on the following Windows Server AMIs. You can
find these AMIs from the Amazon EC2 console, or by using the following search
prefix: `EC2LaunchV2-` in the AWS CLI.

- EC2LaunchV2-Windows_Server-2019-English-Core-Base
- EC2LaunchV2-Windows_Server-2019-English-Full-Base
- EC2LaunchV2-Windows_Server-2016-English-Core-Base
- EC2LaunchV2-Windows_Server-2016-English-Full-Base

## Automatically install and update EC2Launch v2 with AWS Systems Manager Distributor Quick Setup

With AWS Systems Manager Distributor Quick Setup, you can set up automatic updates for EC2Launch v2. The
following process sets up a Systems Manager Association on your instance that automatically updates
the EC2Launch v2 agent at a frequency that you specify. The Association that the Distributor
Quick Setup creates can include instances within an AWS account and Region, or instances
within an AWS Organization. For more information about setting up an organization,
see [Tutorial: Creating and configuring an organization](../../../organizations/latest/userguide/orgs_tutorials_basic.md "../../../organizations/latest/userguide/orgs_tutorials_basic.md") in the _AWS Organizations User
Guide_.

Before you begin, make sure that your instances meet all of the prerequisites.

### Prerequisites

To set up automatic updates with Distributor Quick Setup, your instances must meet
the following prerequisites.

- You have at least one running instance that supports EC2Launch v2. See supported
  operating systems for [EC2Launch v2](ec2launch-v2.md "ec2launch-v2.md").
- You've performed the Systems Manager set-up tasks on your instances. For more information, see
  [Setting up Systems Manager](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md") in the _AWS Systems Manager User
  Guide_.
- EC2Launch v2 must be the only launch agent installed on your instance. If you have more
  than one launch agent installed, your Distributor Quick Setup configuration will fail.
  Before you configure EC2Launch v2 with a Distributor Quick Setup, uninstall
  EC2Config or EC2Launch v1 launch agents, if they exist.

### Configure Distributor Quick Setup for EC2Launch v2

To create a configuration for EC2Launch v2 with Distributor Quick Setup, use the following
settings when you complete the steps for [Distributor package deployment](../../../systems-manager/latest/userguide/quick-setup-distributor.md "../../../systems-manager/latest/userguide/quick-setup-distributor.md"):

- **Software packages:** Amazon EC2Launch v2 agent.
- **Update frequency:** Select a frequency from the list.
- **Targets:** Choose from the available deployment options.

To check the status of your configuration, navigate to the Systems Manager Quick Setup
**Configurations** tab in the AWS Management Console.

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Quick Setup**.
3. In the **Configurations** tab, select the row that's
   associated with the configuration that you created. The **Configurations**
   tab lists your configurations, and includes a summary of key details, such as
   **Region**, **Deployment status**,
   and **Association status**.

###### Note

The association name for every EC2Launch v2 Distributor configuration begins
with the following prefix:
`AWS-QuickSetup-Distributor-EC2Launch-Agent-`. 4. To view details, select the configuration and choose
**View details**.

For more information and troubleshooting steps, see [Troubleshooting Quick Setup results](../../../systems-manager/latest/userguide/quick-setup-results-troubleshooting.md "../../../systems-manager/latest/userguide/quick-setup-results-troubleshooting.md") in the _AWS Systems Manager User
Guide_.

## EC2Launch v2 downloads on Amazon S3

To install the latest version of EC2Launch v2, download the installer from the following location:

- [https://s3.amazonaws.com/amazon-ec2launch-v2/windows/amd64/latest/AmazonEC2Launch.msi](https://s3.amazonaws.com/amazon-ec2launch-v2/windows/amd64/latest/AmazonEC2Launch.msi "https://s3.amazonaws.com/amazon-ec2launch-v2/windows/amd64/latest/AmazonEC2Launch.msi")

## Configure install options

When you install or upgrade EC2Launch v2, you can configure installation options
with the EC2Launch v2 install dialog or with the **msiexec** command
in a command line shell.

The first time the EC2Launch v2 installer runs on an instance, it initializes
launch agent settings on your instance as follows:

- It creates the local path and writes the launch agent file to it.
  This is sometimes referred to as a _clean install_.
- It creates the `EC2LAUNCH_TELEMETRY` environment variable
  if it doesn't already exist, and sets it based on your configuration.

For configuration details, select the tab that matches the configuration method
that you'll use.

Amazon EC2Launch Setup dialog
When you install or upgrade EC2Launch v2, you can configure the following
installation options through the EC2Launch v2 install dialog.

###### **Basic Install** options

**Send Telemetry**

When you include this feature in the setup dialog, the installer sets
the `EC2LAUNCH_TELEMETRY` environment variable to a value of
`1`. If you disable **Send Telemetry**,
the installer sets the environment variable to a value of `0`.

When the EC2Launch v2 agent runs, it reads the `EC2LAUNCH_TELEMETRY`
environment variable to determine whether to upload telemetry data. If the value
equals `1`, it uploads the data. Otherwise, it doesn't upload.

**Default configuration**

The default configuration for EC2Launch v2 is to overwrite the
local launch agent if it exists already. The first time you run
an install on an instance, the default configuration performs a
clean install. If you disable the default configuration on the
initial install, the installation fails.

If you run the install again on the instance, you can disable the
default configuration to perform an upgrade that doesn't replace the
`%ProgramData%/Amazon/EC2Launch/config/agent-config.yml`
file.

###### Example: Upgrade EC2Launch v2 with telemetry

The following example shows the EC2Launch v2 setup dialog configured to upgrade
the current installation and enable telemetry. This configuration performs an
install without replacing the agent configuration file, and sets the
`EC2LAUNCH_TELEMETRY` environment variable to a value of `1`.

![EC2Launch v2 upgrade configuration.](images/ec2launchv2-clean-default-config.png)

Command line
When you install or upgrade EC2Launch v2, you can configure the following installation
options with the **msiexec** command in a command line shell.

###### `ADDLOCAL` parameter values

**Basic** (required)

Install the launch agent. If this value is not present in the
`ADDLOCAL` parameter, the installation ends.

**Clean**

When you include the `Clean` value in the
`ADDLOCAL` parameter, the installer writes the agent configuration
file to the following location:
`%ProgramData%/Amazon/EC2Launch/config/agent-config.yml`.
If the agent configuration file already exists, it overwrites the file.

When you leave the `Clean` value out of the `ADDLOCAL`
parameter, the installer performs an upgrade that doesn't replace the agent
configuration file.

**Telemetry**

When you include the `Telemetry` value in the `ADDLOCAL`
parameter, the installer sets the `EC2LAUNCH_TELEMETRY` environment
variable to a value of `1`.

When you leave the `Telemetry` value out of the `ADDLOCAL`
parameter, the installer sets the environment variable to a value of `0`.

When the EC2Launch v2 agent runs, it reads the `EC2LAUNCH_TELEMETRY`
environment variable to determine whether to upload telemetry data. If the value
equals `1`, it uploads the data. Otherwise, it doesn't upload.

**Example: install EC2Launch v2 with telemetry**

```
& msiexec /i "C:\Users\Administrator\Desktop\EC2Launchv2\AmazonEC2Launch.msi" ADDLOCAL="Basic,Clean,Telemetry" /q
```

## Verify the EC2Launch v2 version

Use one of the following procedures to verify the version of EC2Launch v2 that is
installed on your instances.

PowerShell
Verify the installed version of EC2Launch v2 with Windows PowerShell,
as follows.

1. Launch an instance from your AMI and connect to it.
2. Run the following command in PowerShell to verify the installed version of
   EC2Launch v2:

```
& "C:\Program Files\Amazon\EC2Launch\EC2Launch.exe" version
```

Windows Control Panel
Verify the installed version of EC2Launch v2 in the Windows Control Panel, as follows.

1. Launch an instance from your AMI and connect to it.
2. Open the Windows Control Panel and choose **Programs and
   Features**.
3. Look for `Amazon EC2Launch` in the list of installed programs. Its
   version number appears in the **Version** column.

To view the latest updates for the AWS Windows AMIs, see [Windows AMI
version history](../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md "../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md") in the _AWS Windows AMI Reference_.

For the latest version of EC2Launch v2, see [EC2Launch v2 version history](ec2launchv2-versions.md#ec2launchv2-version-history "ec2launchv2-versions.md#ec2launchv2-version-history").

You can receive notifications when new versions of the EC2Launch v2 service are
released. For more information, see [Subscribe to EC2 Windows launch agent notifications](launch-agents-subscribe-notifications.md "launch-agents-subscribe-notifications.md").
