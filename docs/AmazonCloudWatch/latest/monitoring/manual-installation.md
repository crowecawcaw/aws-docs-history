# Manual installation on Amazon EC2

###### Note

Make sure the prerequisites are completed before installing the CloudWatch agent for the
first time.

###### Topics

- [Installing on Amazon Linux using the package
  manager](#amazon-linux-package "#amazon-linux-package")
- [Installing on Amazon Linux using the command line](#linux-manual-install "#linux-manual-install")
- [Installing on Windows](#windows-installation "#windows-installation")
- [Installing on macOS](#macos-installation "#macos-installation")

## Installing on Amazon Linux using the package

manager

The CloudWatch agent is available as a package in Amazon Linux 2023 and Amazon Linux 2.
If you are using one of these operating systems, you can install the package by entering
the following command:

```
sudo yum install amazon-cloudwatch-agent
```

You must also make sure that the IAM role attached to the instance has the
**CloudWatchAgentServerPolicy** attached.

## Installing on Amazon Linux using the command line

On all supported Linux operating systems, you can download and install the CloudWatch agent
using the command line.

1. Download the CloudWatch agent. For a Linux server, enter the following
   command. For `download-link`, use the appropriate download link from the
   table below.

```
wget download-link
```

| Architecture | Platform                             | Download link                                                                                          |
| ------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| x86-64       | Amazon Linux 2023 and Amazon Linux 2 | https://amazoncloudwatch-agent.s3.amazonaws.com/amazon\_linux/amd64/latest/amazon-cloudwatch-agent.rpm |
| ARM64        | Amazon Linux 2023 and Amazon Linux 2 | https://amazoncloudwatch-agent.s3.amazonaws.com/amazon\_linux/arm64/latest/amazon-cloudwatch-agent.rpm |

2. After you have downloaded the package, you can optionally verify the package
   signature. For more information, see [Verifying the signature of the
   CloudWatch agent package](verify-CloudWatch-Agent-Package-Signature.md "verify-CloudWatch-Agent-Package-Signature.md").
3. Install the package. If you downloaded an RPM package on a Linux server, change to
   the directory containing the package and enter the following:

```
sudo rpm -U ./amazon-cloudwatch-agent.rpm
```

If you downloaded a DEB package on a Linux server, change to the directory
containing the package and enter the following:

```
sudo dpkg -i -E ./amazon-cloudwatch-agent.deb
```

## Installing on Windows

On Windows Server, you can download and install the CloudWatch agent using the command
line.

1. Download the following file:

```
https://amazoncloudwatch-agent.s3.amazonaws.com/windows/amd64/latest/amazon-cloudwatch-agent.msi
```

2. After you have downloaded the package, you can optionally verify the package
   signature. For more information, see [Verifying the signature of the
   CloudWatch agent package](verify-CloudWatch-Agent-Package-Signature.md "verify-CloudWatch-Agent-Package-Signature.md").
3. Install the package. Change to the directory containing the package and enter the
   following:

```
msiexec /i amazon-cloudwatch-agent.msi
```

This command also works from within PowerShell. For more information about MSI
command options, see [Command-Line Options](https://docs.microsoft.com/en-us/windows/desktop/Msi/command-line-options "https://docs.microsoft.com/en-us/windows/desktop/Msi/command-line-options") in the Microsoft Windows documentation.

## Installing on macOS

On macOS computers, you can download and install the CloudWatch agent using the command
line.

1. Download the appropriate package for your architecture:

```
https://amazoncloudwatch-agent.s3.amazonaws.com/darwin/amd64/latest/amazon-cloudwatch-agent.pkg
```

For ARM64 architecture:

```
https://amazoncloudwatch-agent.s3.amazonaws.com/darwin/arm64/latest/amazon-cloudwatch-agent.pkg
```

2. After you have downloaded the package, you can optionally verify the package
   signature. For more information, see [Verifying the signature of the
   CloudWatch agent package](verify-CloudWatch-Agent-Package-Signature.md "verify-CloudWatch-Agent-Package-Signature.md").
3. Install the package. Change to the directory containing the package and enter the
   following:

```
sudo installer -pkg ./amazon-cloudwatch-agent.pkg -target /
```
