# Update the CodeDeploy agent on

Windows Server

You can enable automatic updates of the CodeDeploy agent with AWS Systems Manager. With Systems Manager, you can
configure an update schedule for your Amazon EC2 or on-premises instances by creating an
association with Systems Manager State Manager. You can also manually update the CodeDeploy agent by
uninstalling the current version and installing a newer one.

###### Topics

- [Set up automatic CodeDeploy
  agent update with AWS Systems Manager](#codedeploy-agent-operations-update-windows-ssm "#codedeploy-agent-operations-update-windows-ssm")
- [Update the CodeDeploy agent
  manually](#codedeploy-agent-operations-update-windows-manual "#codedeploy-agent-operations-update-windows-manual")
- [(Deprecated) Update
  the CodeDeploy agent with the Windows Server Updater](#codedeploy-agent-operations-update-windows-updater "#codedeploy-agent-operations-update-windows-updater")

## Set up automatic CodeDeploy

agent update with AWS Systems Manager

To configure Systems Manager and enable automatic updates of the CodeDeploy agent, follow the
instructions in [Install the CodeDeploy agent using AWS Systems Manager](codedeploy-agent-operations-install-ssm.md "codedeploy-agent-operations-install-ssm.md").

## Update the CodeDeploy agent

manually

To update the CodeDeploy agent manually, you can install the latest version from the CLI or
using Systems Manager. Follow the instructions in [Install the CodeDeploy
agent.](codedeploy-agent-operations-install.md "codedeploy-agent-operations-install.md") It is recommended that you uninstall older versions of the CodeDeploy agent by
following the instructions in [Uninstall the CodeDeploy
agent](codedeploy-agent-operations-uninstall.md "codedeploy-agent-operations-uninstall.md").

## (Deprecated) Update

the CodeDeploy agent with the Windows Server Updater

###### Note

The CodeDeploy agent updater for Windows Server is deprecated and will not update to any
version after 1.0.1.1597.

To enable automatic updates of the CodeDeploy agent, install the CodeDeploy agent updater for
Windows Server on new or existing instances. The updater checks periodically for new versions.
When a new version is detected, the updater uninstalls the current version of the agent,
if one is installed, before installing the newest version.

If a deployment is already underway when the updater detects a new version, the
deployment continues to completion. If a deployment attempts to start during the update
process, the deployment fails.

If you want to force an update of the CodeDeploy agent, follow the instructions in [Install the CodeDeploy agent for
Windows Server](codedeploy-agent-operations-install-windows.md "codedeploy-agent-operations-install-windows.md").

On Windows Server instances, you can download and install the CodeDeploy agent updater by running
Windows PowerShell commands, using a direct download link, or running an Amazon S3 copy
command.

###### Topics

- [Use Windows
  PowerShell](#codedeploy-agent-operations-update-windows-powershell "#codedeploy-agent-operations-update-windows-powershell")
- [Use a direct
  link](#codedeploy-agent-operations-update-windows-direct-link "#codedeploy-agent-operations-update-windows-direct-link")
- [Use an Amazon S3 copy
  command](#codedeploy-agent-operations-update-windows-s3-copy "#codedeploy-agent-operations-update-windows-s3-copy")

### Use Windows

PowerShell

Sign in to the instance, and run the following commands in Windows PowerShell, one at
a time:

```
Set-ExecutionPolicy RemoteSigned
```

If you are prompted to change the execution policy, choose `Y`
so Windows PowerShell requires all scripts and configuration files downloaded from the
internet be signed by a trusted publisher.

```
Import-Module AWSPowerShell
```

```
New-Item -Path "c:\temp" -ItemType "directory" -Force
```

```
powershell.exe -Command Read-S3Object -BucketName `bucket-name` -Key latest/codedeploy-agent-updater.msi -File c:\temp\codedeploy-agent-updater.msi
```

```
c:\temp\codedeploy-agent-updater.msi /quiet /l c:\temp\host-agent-updater-log.txt
```

```
powershell.exe -Command Get-Service -Name codedeployagent
```

`bucket-name` is the name of the Amazon S3
bucket that contains the CodeDeploy Resource Kit files for your region. For example, for the
US East (Ohio) Region, replace `bucket-name` with
`aws-codedeploy-us-east-2`. For a list of bucket names, see [Resource kit bucket names by Region](resource-kit.md#resource-kit-bucket-names "resource-kit.md#resource-kit-bucket-names").

If you need to troubleshoot an update process error, type the following command to
open the CodeDeploy agent updater log file:

```
notepad C:\ProgramData\Amazon\CodeDeployUpdater\log\codedeploy-agent.updater.log
```

### Use a direct

link

If the browser security settings on the Windows Server instance
provide the required permissions (for example, to `http://s3.*.amazonaws.com`
), you can use a direct link to download
the CodeDeploy agent updater.

The link is:

```
https://s3.`region`.amazonaws.com/aws-codedeploy-`region`/latest/codedeploy-agent-updater.msi
```

...where `region` is the AWS
Region where you're updating your application.

For example:

```
https://s3.af-south-1.amazonaws.com/aws-codedeploy-af-south-1/latest/codedeploy-agent-updater.msi
```

### Use an Amazon S3 copy

command

If the AWS CLI is installed on the instance, you can use the Amazon S3 [cp](../../../cli/latest/reference/s3/cp.md "../../../cli/latest/reference/s3/cp.md") command to download the CodeDeploy agent updater
and then run the installer manually. For information, see [Install the AWS Command Line Interface on Microsoft
Windows](../../../cli/latest/userguide/awscli-install-windows.md "../../../cli/latest/userguide/awscli-install-windows.md").

The Amazon S3 command is:

```
aws s3 cp s3://aws-codedeploy-`region`/latest/codedeploy-agent-updater.msi codedeploy-agent-updater.msi --region `region`
```

...where `region` is the AWS
Region where you're updating your application.

For example:

```
aws s3 cp s3://aws-codedeploy-af-south-1/latest/codedeploy-agent-updater.msi codedeploy-agent-updater.msi --region af-south-1
```
