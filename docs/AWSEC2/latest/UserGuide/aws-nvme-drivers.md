# AWS NVMe drivers

Amazon EBS volumes and instance store volumes are exposed as NVMe block devices on
[Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type"). To fully utilize the performance and capabilities of Amazon EBS features
for volumes exposed as NVMe block devices, the instance must have the AWS NVMe driver
installed. All current generation AWS Windows AMIs come with the AWS NVMe driver
installed by default.

For more information about EBS and NVMe, see [Amazon EBS and NVMe](../../../ebs/latest/userguide/nvme-ebs-volumes.md "../../../ebs/latest/userguide/nvme-ebs-volumes.md") in the
_Amazon EBS User Guide_. For more information about SSD instance store and
NVMe, see [SSD instance store volumes for EC2 instances](ssd-instance-store.md "ssd-instance-store.md").

The following AMIs include the required NVMe drivers:

- Amazon Linux 2
- Amazon Linux AMI 2018.03
- Ubuntu 14.04 or later with `linux-aws` kernel

###### Note

AWS Graviton-based instance types require Ubuntu 18.04 or later with
`linux-aws` kernel

- Red Hat Enterprise Linux 7.4 or later
- SUSE Linux Enterprise Server 12 SP2 or later
- CentOS 7.4.1708 or later
- FreeBSD 11.1 or later
- Debian GNU/Linux 9 or later

###### To confirm that your instance has the NVMe driver

You can confirm that your instance has the NVMe
driver using the following command.

- Amazon Linux, RHEL, CentOS, and SUSE Linux Enterprise Server

```
`$` modinfo nvme
```

If the instance has the NVMe driver, the command returns information about
the driver.

- Amazon Linux 2 and Ubuntu

```
`$` ls /sys/module/ | grep nvme
```

If the instance has the NVMe driver, the command returns the installed
drivers.

###### To update the NVMe driver

If your instance has the NVMe driver, you can update the driver to the latest
version using the following procedure.

1. Connect to your instance.
2. Update your package cache to get necessary package updates as
   follows.
   - For Amazon Linux 2, Amazon Linux, CentOS, and Red Hat Enterprise Linux:

   ```
   `[ec2-user ~]$` `sudo yum update -y`
   ```

   - For Ubuntu and Debian:

   ```
   `[ec2-user ~]$` `sudo apt-get update -y`
   ```

3. Ubuntu 16.04 and later include the `linux-aws` package, which
   contains the NVMe and ENA drivers required by Nitro-based instances. Upgrade
   the `linux-aws` package to receive the latest version as
   follows:

```
`[ec2-user ~]$` `sudo apt-get install --only-upgrade -y linux-aws`
```

For Ubuntu 14.04, you can install the latest
`linux-aws` package as follows:

```
`[ec2-user ~]$` `sudo apt-get install linux-aws`
```

4. Reboot your instance to load the latest kernel version.

```
`sudo reboot`
```

5. Reconnect to your instance after it has rebooted.

PowerShell
If you did not launch your instance from one of the latest AWS
Windows AMIs provided by Amazon, use the following procedure to install
the current AWS NVMe driver on your instance. Reboot is required for
this install. Either the install script will reboot your instance or you
must reboot it as the final step.

**Prerequisites**

- PowerShell version 3.0 or later is installed.
- The commands shown in this section must run in the 64-bit
  version of PowerShell. Do not use the `x86` version
  of PowerShell. That is the 32-bit version of the shell, and is
  not supported for these commands.

###### To download and install the latest AWS NVMe driver

1.  We recommend that you create an AMI as a backup as follows, in
    case you need to roll back your changes.
    1. When you stop an instance, the data on any instance
       store volumes is erased. Before you stop an instance,
       verify that you've copied any data that you need from
       your instance store volumes to persistent storage, such
       as Amazon EBS or Amazon S3.
    2. In the navigation pane, choose
       **Instances**.
    3. Select the instance that requires the driver upgrade,
       and choose **Instance state**,
       **Stop instance**.
    4. After the instance is stopped, select the instance,
       choose **Actions**, then
       **Image and templates**, and then
       choose **Create image**.
    5. Choose **Instance state**,
       **Start instance**.

2.  Connect to your instance and log in as the local
    administrator.
3.  Download the drivers to your instance using one of the
    following options:
    - Browser – [Download](https://s3.amazonaws.com/ec2-windows-drivers-downloads/NVMe/Latest/AWSNVMe.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/NVMe/Latest/AWSNVMe.zip")

    the latest driver package to the
    instance and extract the zip archive.
    - PowerShell – Run
      the following commands:

    ```
    Invoke-WebRequest https://s3.amazonaws.com/ec2-windows-drivers-downloads/NVMe/Latest/AWSNVMe.zip -outfile $env:USERPROFILE\nvme_driver.zip
    Expand-Archive $env:userprofile\nvme_driver.zip -DestinationPath $env:userprofile\nvme_driver
    ```

    If you receive an error when downloading the file, and you
    are using Windows Server 2016 or earlier, TLS 1.2 might need
    to be enabled for your PowerShell terminal. You can enable
    TLS 1.2 for the current PowerShell session with the
    following command and then try again:

    ```
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    ```

4.  Install the driver to your instance by running the
    `install.ps1` PowerShell script from the
    `nvme_driver` directory
    (`.\install.ps1`). If you get an error, make sure
    you are using PowerShell 3.0 or later.
    1. (Optional) Starting with AWS NVMe version
       `1.5.0`, Small Computer System Interface
       (SCSI) persistent reservations are supported for Windows
       Server 2016 and later. This feature adds support for
       Windows Server Failover Clustering with shared Amazon EBS
       storage. By default, this feature isn't enabled during
       installation.

    You can enable the feature when running the
    `install.ps1` script to install
    the driver by specifying the
    `EnableSCSIPersistentReservations`
    parameter with a value of `$true`.

    ```
    `PS C:\>` ``.\install.ps1` -EnableSCSIPersistentReservations $true`
    ```

    You can disable the feature when running the
    `install.ps1` script to install
    the driver by specifying the
    `EnableSCSIPersistentReservations`
    parameter with a value of `$false`.

    ```
    `PS C:\>` ``.\install.ps1` -EnableSCSIPersistentReservations $false`
    ```

    2. Starting with AWS NVMe `1.5.0`, the
       `install.ps1` script always
       installs the `ebsnvme-id` tool with the
       driver.

    (Optional) For versions `1.4.0`,
    `1.4.1`, and `1.4.2`, the
    `install.ps1` script allows you
    to specify whether the `ebsnvme-id` tool
    should be installed with the driver.

        1. To install the `ebsnvme-id` tool,
         specify `InstallEBSNVMeIdTool
         ‘Yes’`.
        2. If you don't want to install the tool, specify
         `InstallEBSNVMeIdTool ‘No’`.


        If you don't specify
         `InstallEBSNVMeIdTool`, and the tool is
         already present at
         `C:\ProgramData\Amazon\Tools`, the
         package will upgrade the tool by default. If the
         tool is not present, `install.ps1` will
         not upgrade the tool by default.


        If you don't want to install the tool as part
         of the package, and want to install it later, you
         can find the latest version or the tool in the
         driver package. Alternatively, you can download
         version `1.0.0` from Amazon S3:


        [Download](https://s3.amazonaws.com/ec2-windows-drivers-downloads/EBSNVMeID/Latest/ebsnvme-id.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/EBSNVMeID/Latest/ebsnvme-id.zip") the `ebsnvme-id`
         tool.

5.  If the installer does not reboot your instance, reboot the
    instance.

Distributor
You can use Distributor, a capability of AWS Systems Manager, to install the
NVMe driver package one time or with scheduled updates.

###### To install the latest AWS NVMe driver

1.  For the instructions for how to install the NVMe driver
    package using Distributor, see the procedures in [Install or update packages](../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md "../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md") in the
    _Amazon EC2 Systems Manager User Guide_.
2.  For **Installation Type**, select
    **Uninstall and reinstall**.
3.  For **Name**, choose
    **AWSNVMe**.
4.  (Optional) For **Additional Arguments**, you
    can customize the installation by specifying values. The values
    must be formatted using valid JSON syntax. For examples of how
    to pass additional arguments for the `aws configure`
    package, see the [Command document plugin reference](../../../systems-manager/latest/userguide/documents-command-ssm-plugin-reference.md "../../../systems-manager/latest/userguide/documents-command-ssm-plugin-reference.md").
    1. Starting with AWS NVMe `1.5.0`, the
       driver supports SCSI persistent reservations for Windows
       Server 2016 and later. By default, this feature isn't
       enabled during installation.
       - To enable this feature, specify
         `{"SSM_EnableSCSIPersistentReservations":
"true"}`.
       - If you don't want to enable this feature,
         specify
         `{"SSM_EnableSCSIPersistentReservations":
"false"}`.

    2. Starting with AWS NVMe `1.5.0`, the
       `install.ps1` script will always
       install the `ebsnvme-id` tool.

    (Optional) For versions `1.4.0`,
    `1.4.1`, and `1.4.2`, the
    `install.ps1` script allows you
    to specify whether the ebsnvme-id tool should be
    installed with the driver.

        * To install the ebsnvme-id tool, specify
         `{"SSM_InstallEBSNVMeIdTool":
         "Yes"}`.
        * If you don't want to install the tool, specify
         `{"SSM_InstallEBSNVMeIdTool":
         "No"}`.


        If `SSM_InstallEBSNVMeIdTool` is
         not specified for **Additional
         Arguments**, and the tool is already
         present at
         `C:\ProgramData\Amazon\Tools`, the
         package will upgrade the tool by default. If the
         tool is not present, the package will not upgrade
         the tool by default.


        If you don't want to install the tool as part
         of the package, and want to install it later, you
         can find the latest version of the tool in the
         driver package. Alternatively, you can download
         version `1.0.0` from Amazon S3:


        [Download](https://s3.amazonaws.com/ec2-windows-drivers-downloads/EBSNVMeID/Latest/ebsnvme-id.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/EBSNVMeID/Latest/ebsnvme-id.zip") the `ebsnvme-id`
         tool.

5.  If the installer does not reboot your instance, reboot the
    instance.

## Configure SCSI persistent

reservations for Windows instances

After AWS NVMe driver version `1.5.0` or later has been installed, you
can enable or disable SCSI persistent reservations using the Windows registry for
Windows Server 2016 and later. You must reboot the instance for these registry changes
to take effect.

You can enable SCSI persistent reservations with the following command which sets the
`EnableSCSIPersistentReservations` to a value of `1`.

```
`PS C:\>` `$registryPath = "HKLM:\SYSTEM\CurrentControlSet\Services\AWSNVMe\Parameters\Device"
Set-ItemProperty -Path $registryPath -Name EnableSCSIPersistentReservations -Value 1`
```

You can disable SCSI persistent reservations with the following command which sets the
`EnableSCSIPersistentReservations` to a value of `0`.

```
`PS C:\>` `$registryPath = "HKLM:\SYSTEM\CurrentControlSet\Services\AWSNVMe\Parameters\Device"
Set-ItemProperty -Path $registryPath -Name EnableSCSIPersistentReservations -Value 0`
```
