AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Manually installing and

uninstalling SSM Agent on EC2 instances for Windows Server

AWS Systems Manager Agent (SSM Agent) is preinstalled, by default, on the following
Amazon Machine Images (AMIs) for Windows Server provided by Amazon:

- Windows Server 2012 R2 AMIs published in November 2016 or later
- Windows Server 2016, 2019, 2022 (excluding Nano versions), and 2025

###### Important

We strongly recommend that you avoid using OS versions that have reached End-of-Life (EOL).
OS vendors including AWS typically don't provide security patches or other updates for versions that have reached EOL.
Continuing to use an EOL system greatly increases the risk of not being able to apply upgrades, including security
fixes, and other operational problems. AWS does not test Systems Manager functionality on OS versions that have reached EOL.

## Install SSM Agent on EC2 instances for

Windows Server

If necessary, you can manually download and install the latest version of
SSM Agent on your Amazon Elastic Compute Cloud (Amazon EC2) instance for Windows Server by using the following
procedure. The commands provided in this procedure can also be passed to Amazon EC2
instances as scripts through user data.

SSM Agent requires Windows PowerShell 3.0 or later to run certain AWS Systems Manager
documents (SSM documents) on Windows Server instances (for example, the legacy
`AWS-ApplyPatchBaseline` document). Verify that your Windows Server
instances are running Windows Management Framework 3.0 or later. This framework
includes Windows PowerShell. For more information, see [Windows Management Framework 3.0](https://www.microsoft.com/en-us/download/details.aspx?id=34595&751be11f-ede8-5a0c-058c-2ee190a24fa6=True "https://www.microsoft.com/en-us/download/details.aspx?id=34595&751be11f-ede8-5a0c-058c-2ee190a24fa6=True").

###### Installation on other machine types

This procedure in this topic applies specifically to installing or
reinstalling SSM Agent on an EC2 instance for Windows Server. For on-premises
servers, virtual machines, or other non-EC2 environments, use the
`ssm-setup-cli` tool as described in [Install SSM Agent on hybrid
Windows Server nodes](hybrid-multicloud-ssm-agent-install-windows.md "hybrid-multicloud-ssm-agent-install-windows.md").

Using EC2 installation procedures on non-EC2 systems can potentially
result in security vulnerabilities. The `ssm-setup-cli`
tool provides additional security protections for non-EC2 machines.

###### To manually install the latest version of SSM Agent on EC2 instances for

Windows Server

1. Connect to your instance by using Remote Desktop or Windows
   PowerShell. For more information, see [Connect to your instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows") in the
   _Amazon EC2 User Guide_.
2. Download the latest version of SSM Agent to your instance. You can
   download using either PowerShell commands or a direct download link.

###### Note

The URLs in this step let you download SSM Agent from
_any_ AWS Region. If you want to download
the agent from a specific Region, use a Region-specific URL
instead:

`https://amazon-ssm-`region`.s3.`region`.amazonaws.com/latest/windows_amd64/AmazonSSMAgentSetup.exe`

`region` represents the identifier for an AWS Region supported
by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported
`region` values, see the **Region** column in [Systems Manager service endpoints](../../../general/latest/gr/ssm.md#ssm_region "../../../general/latest/gr/ssm.md#ssm_region") in the
_Amazon Web Services General Reference_.

**PowerShell**

Run the following three PowerShell commands in order.
These commands allow you to download SSM Agent without
adjusting Internet Explorer (IE) Enhanced Security settings,
and then install the agent and remove the installation
file.

64-bit

```
[System.Net.ServicePointManager]::SecurityProtocol = 'TLS12'
$progressPreference = 'silentlyContinue'
Invoke-WebRequest `
    https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/windows_amd64/AmazonSSMAgentSetup.exe `
    -OutFile $env:USERPROFILE\Desktop\SSMAgent_latest.exe
```

32-bit

```
[System.Net.ServicePointManager]::SecurityProtocol = 'TLS12'
$progressPreference = 'silentlyContinue'
Invoke-WebRequest `
    https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/windows_386/AmazonSSMAgentSetup.exe `
    -OutFile $env:USERPROFILE\Desktop\SSMAgent_latest.exe
```

```
Start-Process `
    -FilePath $env:USERPROFILE\Desktop\SSMAgent_latest.exe `
    -ArgumentList "/S" `
    -Wait
```

```
rm -Force $env:USERPROFILE\Desktop\SSMAgent_latest.exe
```

**Direct download**

Download the latest version of
SSM Agent to your instance by using the following link. If
you want, update this URL with an AWS Region-specific
URL.

[https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/windows_amd64/AmazonSSMAgentSetup.exe](https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/windows_amd64/AmazonSSMAgentSetup.exe "https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/windows_amd64/AmazonSSMAgentSetup.exe")

Run the downloaded
`AmazonSSMAgentSetup.exe` file to
install SSM Agent. 3. Start or restart SSM Agent by sending the following command in
PowerShell:

```
Restart-Service AmazonSSMAgent
```

###### Note

To uninstall the SSM Agent from a Windows Server instance, open **Control
Panel**, **Programs**. Choose the
**Uninstall a program** option. Open the context
(right-click) menu for **Amazon SSM Agent** and choose
**Uninstall**.
