# Checking the SSM Agent version number

Certain AWS Systems Manager functionalities have prerequisites that include a minimum Systems Manager
Agent (SSM Agent) version be installed on your managed nodes. You can get the currently
installed SSM Agent version on your managed nodes using the Systems Manager console, or by logging
in to your managed nodes.

###### Note

To view details about earlier versions, see the [SSM Agent release notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md") on GitHub.

The following procedures describe how to get the currently installed SSM Agent version
on your managed nodes.

###### To check the version number of SSM Agent installed on a managed node

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. In the **SSM Agent version** column, note the **Agent
   version** number.

###### To get the currently installed SSM Agent version from within the operating

system

Choose from the following tabs to get the currently installed SSM Agent version
from within an operating system.

Amazon Linux 2 and Amazon Linux 2023

###### Note

This command varies depending on the package manager for your
operating system.

1. Log in to your managed node.
2. Run the following command.

```
yum info amazon-ssm-agent
```

This command returns output similar to the following.

```
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
Installed Packages
Name        : amazon-ssm-agent
Arch        : x86_64
Version     : 3.0.655.0
```

Debian Server

1. Log in to your managed node.
2. Run the following command.

```
apt list amazon-ssm-agent
```

This command returns output similar to the following.

```
apt list amazon-ssm-agent
Listing... Done
amazon-ssm-agent/now 3.0.655.0-1 amd64 [installed,local]

3.0.655.0 is the version of SSM agent
```

macOS

1. Log in to your managed node.
2. Run the following command.

```
pkgutil --pkg-info com.amazon.aws.ssm
```

RHEL

1. Log in to your managed node.
2. Run the following command for RHEL 7, 8, 9, and 10.

```
yum info amazon-ssm-agent
```

This command returns output similar to the following.

```
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
Installed Packages
Name        : amazon-ssm-agent
Arch        : x86_64
Version     : 3.0.655.0
```

Run the following command for the DNF package utility.

```
dnf info amazon-ssm-agent
```

SLES

1. Log in to your managed node.
2. Run the following command for SLES 15._x_.

```
zypper info amazon-ssm-agent
```

This command returns output similar to the following.

```
Loading repository data...
Reading installed packages...
Information for package amazon-ssm-agent:
‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐
Repository : @System
Name : amazon-ssm-agent
Version : 3.0.655.0-1
```

Ubuntu Server

###### Note

To check if your Ubuntu Server 16.04 instance uses deb or Snap
packages, see [Manually installing SSM Agent on
Ubuntu Server instances](agent-install-ubuntu.md "agent-install-ubuntu.md").

1. Log in to your managed node.
2. Run the following command for Ubuntu Server 16.04 64-bit (with deb
   installer package).

```
apt list amazon-ssm-agent
```

This command returns output similar to the following.

```
apt list amazon-ssm-agent
Listing... Done
amazon-ssm-agent/now 3.0.655.0-1 amd64 [installed,local]

3.0.655.0 is the version of SSM agent
```

Run the following command for Ubuntu Server 16.04 LTS 64-bit (Snap),
18.04, 20.04, 22.04 LTS, 23.10, 24.04 LTS, 24.0, and 25.04.

```
sudo snap list amazon-ssm-agent
```

This command returns output similar to the following.

```
snap list amazon-ssm-agent
Name Version Rev Tracking Publisher Notes
amazon-ssm-agent 3.0.529.0 3552 latest/stable/… aws✓ classic-

3.0.529.0 is the version of SSM agent
```

Windows

1. Log in to your managed node.
2. Run the following PowerShell command.

```
& "C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe" -version

```

This command returns output similar to the following.

```
SSM Agent version: 3.1.804.0
```

We recommend using the latest version of the SSM Agent so you can benefit from new or
updated capabilities. To ensure your managed instances are always running the most
up-to-date version of the SSM Agent, you can automate the process of updating the
SSM Agent. For more information, see [Automating updates to SSM Agent](ssm-agent-automatic-updates.md "ssm-agent-automatic-updates.md").
