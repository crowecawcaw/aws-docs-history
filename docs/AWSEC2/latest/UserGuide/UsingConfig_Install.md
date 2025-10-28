# Install the latest version of EC2Config

###### Note

The latest launch agent for Windows Server 2022 and later operating system versions is
[EC2Launch v2](ec2launch-v2.md "ec2launch-v2.md"), which replaces both EC2Config and EC2Launch.
EC2Launch v2 comes pre-installed on AWS Windows Server 2022 and 2025 AMIs. You can also
manually install and configure the agent on Windows Server 2016 and 2019. For more information,
see [Install EC2Launch v2](ec2launch-v2-install.md "ec2launch-v2-install.md").

For information about how to receive notifications for EC2Config updates, see
[Subscribe to EC2 Windows launch agent notifications](launch-agents-subscribe-notifications.md "launch-agents-subscribe-notifications.md").
For information about the changes in each version, see the
[EC2Config version history](ec2config-version-details.md "ec2config-version-details.md").

## Before you begin

- Verify that you have .NET framework 3.5 SP1 or greater.
- By default, Setup replaces your settings files with default settings files
  during installation and restarts the EC2Config service when the installation is
  completed. If you changed EC2Config service settings, copy the
  `config.xml` file from the `%Program
Files%\Amazon\Ec2ConfigService\Settings` directory. After you
  update the EC2Config service, you can restore this file to retain your
  configuration changes.

## Verify the EC2Config version

Use the following procedure to verify the version of EC2Config that is installed
on your instances.

###### To verify the installed version of EC2Config

1. Launch an instance from your AMI and connect to it.
2. In Control Panel, select **Programs and Features**.
3. In the list of installed programs, look for `Ec2ConfigService`. Its
   version number appears in the **Version** column.

## Update EC2Config

Use the following procedure to download and install the latest version of EC2Config
on your instances.

###### To download and install the latest version of EC2Config

1. Download and unzip the [EC2Config installer](https://s3.amazonaws.com/ec2-downloads-windows/EC2Config/EC2Install.zip "https://s3.amazonaws.com/ec2-downloads-windows/EC2Config/EC2Install.zip").
2. Run `EC2Install.exe`. For a complete list of options, run
   `EC2Install` with the `/?` option. By default,
   setup displays prompts. To run the command with no prompts, use the
   `/quiet` option.

###### Important

To keep the custom settings from the `config.xml` file
that you saved, run `EC2Install` with the
`/norestart` option, restore your settings, and then restart
the EC2Config service manually. 3. If you are running EC2Config version 4.0 or later, you must restart
SSM Agent on the instance from the Microsoft Services snap-in.

###### Note

The updated EC2Config version information will not appear in the instance System Log or
Trusted Advisor check until you reboot or stop and start your
instance.

###### To download and install the latest version of EC2Config using PowerShell

To download, unzip, and install the latest version of EC2Config using PowerShell, run the
following commands from a PowerShell window:

```
$Url = "https://s3.amazonaws.com/ec2-downloads-windows/EC2Config/EC2Install.zip"
$DownloadZipFile = "$env:USERPROFILE\Desktop\" + $(Split-Path -Path $Url -Leaf)
$ExtractPath = "$env:USERPROFILE\Desktop\"
Invoke-WebRequest -Uri $Url -OutFile $DownloadZipFile
$ExtractShell = New-Object -ComObject Shell.Application
$ExtractFiles = $ExtractShell.Namespace($DownloadZipFile).Items()
$ExtractShell.NameSpace($ExtractPath).CopyHere($ExtractFiles)
Start-Process $ExtractPath
Start-Process `
    -FilePath $env:USERPROFILE\Desktop\EC2Install.exe `
    -ArgumentList "/S"
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

Verify the installation by checking `C:\Program Files\Amazon\` for the
`Ec2ConfigService` directory.
