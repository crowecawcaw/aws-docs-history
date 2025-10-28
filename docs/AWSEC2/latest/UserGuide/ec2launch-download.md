# Install the latest version of EC2Launch

Use the following procedure to download and install the latest version of EC2Launch on
your instances.

###### To download and install the latest version of EC2Launch

1. If you have already installed and configured EC2Launch on an instance, make a
   backup of the EC2Launch configuration file. The installation process does not
   preserve changes in this file. By default, the file is located in the
   `C:\ProgramData\Amazon\EC2-Windows\Launch\Config`
   directory.
2. Download [EC2-Windows-Launch.zip](https://s3.amazonaws.com/ec2-downloads-windows/EC2Launch/latest/EC2-Windows-Launch.zip "https://s3.amazonaws.com/ec2-downloads-windows/EC2Launch/latest/EC2-Windows-Launch.zip") to a directory on the instance.
3. Download [install.ps1](https://s3.amazonaws.com/ec2-downloads-windows/EC2Launch/latest/install.ps1 "https://s3.amazonaws.com/ec2-downloads-windows/EC2Launch/latest/install.ps1") to the same directory where you downloaded
   `EC2-Windows-Launch.zip`.
4. Run `install.ps1`
5. If you made a backup of the EC2Launch configuration file, copy it to the
   `C:\ProgramData\Amazon\EC2-Windows\Launch\Config`
   directory.

###### To download and install the latest version of EC2Launch using PowerShell

If you have already installed and configured EC2Launch on an instance, make a
backup of the EC2Launch configuration file. The installation process does not
preserve changes in this file. By default, the file is located in the
`C:\ProgramData\Amazon\EC2-Windows\Launch\Config`
directory.

To install the latest version of EC2Launch using PowerShell, run the following
commands from a PowerShell window as an administrator:

```
mkdir $env:USERPROFILE\Desktop\EC2Launch
$Url = "https://s3.amazonaws.com/ec2-downloads-windows/EC2Launch/latest/EC2-Windows-Launch.zip"
$DownloadZipFile = "$env:USERPROFILE\Desktop\EC2Launch\" + $(Split-Path -Path $Url -Leaf)
Invoke-WebRequest -Uri $Url -OutFile $DownloadZipFile
$Url = "https://s3.amazonaws.com/ec2-downloads-windows/EC2Launch/latest/install.ps1"
$DownloadZipFile = "$env:USERPROFILE\Desktop\EC2Launch\" + $(Split-Path -Path $Url -Leaf)
Invoke-WebRequest -Uri $Url -OutFile $DownloadZipFile
& $env:USERPROFILE\Desktop\EC2Launch\install.ps1
```

###### Note

If you receive an error when downloading the file, and you
are using Windows Server 2016, TLS 1.2 might need
to be enabled for your PowerShell terminal. You can enable
TLS 1.2 for the current PowerShell session with the
following command and then try again:

```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

Verify the installation by checking the launch agent. Run the following commands from
a PowerShell window as an administrator:

```
Import-Module C:\ProgramData\Amazon\EC2-Windows\Launch\Module\Ec2Launch.psm1
Import-LocalizedData -BaseDirectory C:\ProgramData\Amazon\EC2-Windows\Launch\Module\ -FileName 'Ec2Launch.psd1' -BindingVariable moduleManifest
$moduleManifest.Get_Item('ModuleVersion')
```
