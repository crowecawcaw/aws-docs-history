# Install NVIDIA GRID drivers (G6, Gr6, G6e, G6f, Gr6f, G5,

G4dn, and G3 instances)

These downloads are available to AWS customers only. By downloading, in order to adhere
to requirements of the AWS solution referred to in the NVIDIA GRID Cloud End User
License Agreement (EULA), you agree to use the downloaded software only to develop
AMIs for use with the NVIDIA L4, NVIDIA L40S, NVIDIA A10G, NVIDIA Tesla T4, or
NVIDIA Tesla M60 hardware. You can use the GRID drivers to both create and use
AMIs within the AWS environment. Upon installation of the software, you are
bound by the terms of the [NVIDIA GRID Cloud End User License Agreement](https://aws-nvidia-license-agreement.s3.amazonaws.com/NvidiaGridAWSUserLicenseAgreement.DOCX "https://aws-nvidia-license-agreement.s3.amazonaws.com/NvidiaGridAWSUserLicenseAgreement.DOCX"). For information about the
version of the NVIDIA GRID driver for your operating system, see the [NVIDIA Virtual GPU (vGPU) Software](https://docs.nvidia.com/vgpu/ "https://docs.nvidia.com/vgpu/")
on the NVIDIA website.

###### Considerations

- G6f and Gr6f instances do not support GRID 19.0 or later.
- G6f and Gr6f instances require GRID 18.4 or later.
- G6e instances require GRID 17.4 or later.
- G6 and Gr6 instances require GRID 17.1 or later.
- G5 instances require GRID 13.1 or later (or GRID 12.4 or
  later).
- G3 instances require AWS provided DNS resolution for GRID licensing
  to work.
- [IMDSv2](configuring-instance-metadata-service.md "configuring-instance-metadata-service.md") is
  only supported with NVIDIA driver version 14.0 or greater.
- For Windows instances, if you launch your instance from a custom Windows AMI,
  the AMI must be a standardized image created with
  Windows Sysprep to ensure that the GRID driver works. For more
  information, see [Create an Amazon EC2 AMI using Windows Sysprep](ami-create-win-sysprep.md "ami-create-win-sysprep.md").
- GRID 17.0 and later do not support Windows Server 2019.
- GRID 14.2 and later do not support Windows Server 2016.
- GRID 17.0 and later is not supported with G3 instances.
- For Linux instances, you might need to install or update packages,
  such as gcc, if the NVIDIA installer fails with an error message. The
  specifics depend on the versions of the operating system and the kernel.
  For more information, see the NVIDIA Enterprise Support Portal.

###### Prerequisites

- (Linux) Verify that the AWS CLI is installed on your instance and configured
  with default credentials. For more information, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
  in the _AWS Command Line Interface User Guide_.
- (Windows) Configure default credentials for the AWS Tools for Windows PowerShell on your instance.
  For more information, see [Getting started with
  the AWS Tools for Windows PowerShell](../../../powershell/latest/userguide/pstools-getting-started.md "../../../powershell/latest/userguide/pstools-getting-started.md") in the _AWS Tools for PowerShell User Guide_.
- Your user or role must have the permissions granted that contains the
  **AmazonS3ReadOnlyAccess** policy.

###### To install the NVIDIA GRID driver on your instance

1. Connect to your instance. Update your package cache and get the package
   updates for your instance.

```
`[ec2-user ~]$` sudo dnf update -y
```

2. Install **gcc** and **make**, if they are not
   already installed.

```
`[ec2-user ~]$` sudo dnf install gcc make
```

3. Reboot your instance to load the latest kernel version.

```
`[ec2-user ~]$` sudo reboot
```

4. Reconnect to your instance after it has rebooted.
5. Install the kernel headers packages.

```
`[ec2-user ~]$` sudo dnf install -y kernel-devel kernel-modules-extra
```

6. Download the GRID driver installation utility using the following command:

```
`[ec2-user ~]$` aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
```

Multiple versions of the GRID driver are stored in this
bucket. You can see all of the available versions using the
following command.

```
`[ec2-user ~]$` aws s3 ls --recursive s3://ec2-linux-nvidia-drivers/
```

7. Add permissions to run the driver installation utility using
   the following command.

```
`[ec2-user ~]$` chmod +x NVIDIA-Linux-x86_64*.run
```

8. Run the self-install script as follows to install the GRID
   driver that you downloaded. For example:

```
`[ec2-user ~]$` sudo /bin/sh ./NVIDIA-Linux-x86_64*.run
```

When prompted, accept the license agreement and specify the
installation options as required (you can accept the default
options). 9. Confirm that the driver is functional. The response for the
following command lists the installed version of the NVIDIA
driver and details about the GPUs.

```
`[ec2-user ~]$` nvidia-smi -q | head
```

10. If you are using NVIDIA vGPU software version 14.x or greater
    on the G4dn, G5, or G5g instances, disable GSP with the
    following commands. For more information about why this is required, see the
    [NVIDIA documentation](https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp "https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp").

```
`[ec2-user ~]$` sudo touch /etc/modprobe.d/nvidia.conf
```

```
`[ec2-user ~]$` echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
```

11. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

12. (Optional) Depending on your use case, you might complete the
    following optional steps. If you do not require this
    functionality, do not complete these steps.
    1.  To help take advantage of the four displays of up to
        4K resolution, set up the high-performance display
        protocol [Amazon DCV](../../../dcv.md "../../../dcv.md").
    2.  NVIDIA Quadro Virtual Workstation mode is enabled by
        default. To activate GRID Virtual Applications for RDSH
        Application hosting capabilities, complete the GRID
        Virtual Application activation steps in [Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances](activate_grid.md "activate_grid.md").

###### To install the NVIDIA GRID driver on your instance

1. Connect to your instance. Update your package cache and get the package
   updates for your instance.

```
`[ec2-user ~]$` sudo yum update -y
```

2. Install **gcc** and **make**, if they are not
   already installed.

```
`[ec2-user ~]$` sudo yum install gcc make
```

3. Reboot your instance to load the latest kernel version.

```
`[ec2-user ~]$` sudo reboot
```

4. Reconnect to your instance after it has rebooted.
5. Install the kernel headers package for the version of the kernel that is
   running.

```
`[ec2-user ~]$` sudo yum install -y kernel-devel-$(uname -r)
```

6. Download the GRID driver installation utility using the following command:

```
`[ec2-user ~]$` aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
```

Multiple versions of the GRID driver are stored in this
bucket. You can see all of the available versions using the
following command.

```
`[ec2-user ~]$` aws s3 ls --recursive s3://ec2-linux-nvidia-drivers/
```

7. Add permissions to run the driver installation utility using
   the following command.

```
`[ec2-user ~]$` chmod +x NVIDIA-Linux-x86_64*.run
```

8. Run the self-install script as follows to install the GRID
   driver that you downloaded. For example:

```
`[ec2-user ~]$` sudo /bin/sh ./NVIDIA-Linux-x86_64*.run
```

If you are using Amazon Linux 2 with kernel version 5.10, use the
following command to install the GRID driver.

```
`[ec2-user ~]$` sudo CC=/usr/bin/gcc10-cc ./NVIDIA-Linux-x86_64*.run
```

When prompted, accept the license agreement and specify the
installation options as required (you can accept the default
options). 9. Confirm that the driver is functional. The response for the
following command lists the installed version of the NVIDIA
driver and details about the GPUs.

```
`[ec2-user ~]$` nvidia-smi -q | head
```

10. If you are using NVIDIA vGPU software version 14.x or greater
    on the G4dn, G5, or G5g instances, disable GSP with the
    following commands. For more information about why this is required, see the
    [NVIDIA documentation](https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp "https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp").

```
`[ec2-user ~]$` sudo touch /etc/modprobe.d/nvidia.conf
```

```
`[ec2-user ~]$` echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
```

11. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

12. (Optional) Depending on your use case, you might complete the
    following optional steps. If you do not require this
    functionality, do not complete these steps.
    1.  To help take advantage of the four displays of up to
        4K resolution, set up the high-performance display
        protocol [Amazon DCV](../../../dcv.md "../../../dcv.md").
    2.  NVIDIA Quadro Virtual Workstation mode is enabled by
        default. To activate GRID Virtual Applications for RDSH
        Application hosting capabilities, complete the GRID
        Virtual Application activation steps in [Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances](activate_grid.md "activate_grid.md").

###### To install the NVIDIA GRID driver on your instance

1. Connect to your instance. Update your package cache and get the package
   updates for your instance.

```
`[ec2-user ~]$` sudo yum update -y
```

2. Install **gcc** and **make**, if they are not
   already installed.

```
`[ec2-user ~]$` sudo yum install -y gcc make
```

3. Reboot your instance to load the latest kernel version.

```
`[ec2-user ~]$` sudo reboot
```

4. Reconnect to your instance after it has rebooted.
5. Install the kernel headers package for the version of the kernel that you are
   running.

```
`[ec2-user ~]$` sudo yum install -y kernel-devel-$(uname -r)
```

6. Disable the `nouveau` open source driver for NVIDIA
   graphics cards.
   1. Add `nouveau` to the
      `/etc/modprobe.d/blacklist.conf`
      blacklist file. Copy the following code block and paste
      it into a terminal.

   ```
   `[ec2-user ~]$` cat << EOF | sudo tee --append /etc/modprobe.d/blacklist.conf
   blacklist vga16fb
   blacklist nouveau
   blacklist rivafb
   blacklist nvidiafb
   blacklist rivatv
   EOF
   ```

   2. Edit the `/etc/default/grub` file
      and add the following line:

   ```
   GRUB_CMDLINE_LINUX="rdblacklist=nouveau"
   ```

   3. Rebuild the Grub configuration.

   ```
   `[ec2-user ~]$` sudo grub2-mkconfig -o /boot/grub2/grub.cfg
   ```

7. Download the GRID driver installation utility using the
   following command:

```
`[ec2-user ~]$` aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
```

Multiple versions of the GRID driver are stored in this
bucket. You can see all of the available versions using the
following command.

```
`[ec2-user ~]$` aws s3 ls --recursive s3://ec2-linux-nvidia-drivers/
```

8. Add permissions to run the driver installation utility using
   the following command.

```
`[ec2-user ~]$` chmod +x NVIDIA-Linux-x86_64*.run
```

9. Run the self-install script as follows to install the GRID
   driver that you downloaded. For example:

```
`[ec2-user ~]$` sudo /bin/sh ./NVIDIA-Linux-x86_64*.run
```

When prompted, accept the license agreement and specify the
installation options as required (you can accept the default
options). 10. Confirm that the driver is functional. The response for the
following command lists the installed version of the NVIDIA
driver and details about the GPUs.

```
`[ec2-user ~]$` nvidia-smi -q | head
```

11. If you are using NVIDIA vGPU software version 14.x or greater
    on the G4dn, G5, or G5g instances, disable GSP with the
    following commands. For more information about why this is required, see the [NVIDIA documentation](https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp "https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp").

```
`[ec2-user ~]$` sudo touch /etc/modprobe.d/nvidia.conf
```

```
`[ec2-user ~]$` echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
```

12. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

13. (Optional) Depending on your use case, you might complete the
    following optional steps. If you do not require this
    functionality, do not complete these steps.
    1.  To help take advantage of the four displays of up to
        4K resolution, set up the high-performance display
        protocol [Amazon DCV](../../../dcv.md "../../../dcv.md").
    2.  NVIDIA Quadro Virtual Workstation mode is enabled by
        default. To activate GRID Virtual Applications for RDSH
        Application hosting capabilities, complete the GRID
        Virtual Application activation steps in [Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances](activate_grid.md "activate_grid.md").
    3.  Install the GUI desktop/workstation package.

    ```
    `[ec2-user ~]$` sudo yum groupinstall -y "Server with GUI"
    ```

###### To install the NVIDIA GRID driver on your instance

1. Connect to your instance. Update your package cache and get the package
   updates for your instance.

```
`[ec2-user ~]$` sudo yum update -y
```

2. Install **gcc** and **make**, if they are not
   already installed.

```
`[ec2-user ~]$` sudo yum install -y gcc make
```

3. Reboot your instance to load the latest kernel version.

```
`[ec2-user ~]$` sudo reboot
```

4. Reconnect to your instance after it has rebooted.
5. Install the kernel headers package for the version of the kernel that you are
   running.

```
`[ec2-user ~]$` sudo dnf install -y elfutils-libelf-devel libglvnd-devel kernel-devel-$(uname -r)
```

6. Download the GRID driver installation utility using the
   following command:

```
`[ec2-user ~]$` aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
```

Multiple versions of the GRID driver are stored in this
bucket. You can see all of the available versions using the
following command.

```
`[ec2-user ~]$` aws s3 ls --recursive s3://ec2-linux-nvidia-drivers/
```

7. Add permissions to run the driver installation utility using
   the following command.

```
`[ec2-user ~]$` chmod +x NVIDIA-Linux-x86_64*.run
```

8. Run the self-install script as follows to install the GRID
   driver that you downloaded. For example:

```
`[ec2-user ~]$` sudo /bin/sh ./NVIDIA-Linux-x86_64*.run
```

When prompted, accept the license agreement and specify the
installation options as required (you can accept the default
options). 9. Confirm that the driver is functional. The response for the
following command lists the installed version of the NVIDIA
driver and details about the GPUs.

```
`[ec2-user ~]$` nvidia-smi -q | head
```

10. If you are using NVIDIA vGPU software version 14.x or greater
    on the G4dn, G5, or G5g instances, disable GSP with the
    following commands. For more information about why this is required, see the [NVIDIA documentation](https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp "https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp").

```
`[ec2-user ~]$` sudo touch /etc/modprobe.d/nvidia.conf
```

```
`[ec2-user ~]$` echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
```

11. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

12. (Optional) Depending on your use case, you might complete the
    following optional steps. If you do not require this
    functionality, do not complete these steps.
    1.  To help take advantage of the four displays of up to
        4K resolution, set up the high-performance display
        protocol [Amazon DCV](../../../dcv.md "../../../dcv.md").
    2.  NVIDIA Quadro Virtual Workstation mode is enabled by
        default. To activate GRID Virtual Applications for RDSH
        Application hosting capabilities, complete the GRID
        Virtual Application activation steps in [Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances](activate_grid.md "activate_grid.md").
    3.  Install the GUI workstation package.

    ```
    `[ec2-user ~]$` sudo dnf groupinstall -y workstation
    ```

###### To install the NVIDIA GRID driver on your Linux instance

1. Connect to your instance. Update your package cache and get the package
   updates for your instance.

```
`[ec2-user ~]$` sudo yum update -y
```

2. Install **gcc** and **make**, if they are not
   already installed.

```
`[ec2-user ~]$` sudo yum install -y gcc make
```

3. Reboot your instance to load the latest kernel version.

```
`[ec2-user ~]$` sudo reboot
```

4. Reconnect to your instance after it has rebooted.
5. Install the kernel headers package for the version of the kernel that you are
   running.

```
`[ec2-user ~]$` sudo dnf install -y elfutils-libelf-devel libglvnd-devel kernel-devel-$(uname -r)
```

6. Download the GRID driver installation utility using the
   following command:

```
`[ec2-user ~]$` aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
```

Multiple versions of the GRID driver are stored in this
bucket. You can see all of the available versions using the
following command.

```
`[ec2-user ~]$` aws s3 ls --recursive s3://ec2-linux-nvidia-drivers/
```

7. Add permissions to run the driver installation utility using
   the following command.

```
`[ec2-user ~]$` chmod +x NVIDIA-Linux-x86_64*.run
```

8. Run the self-install script as follows to install the GRID
   driver that you downloaded. For example:

```
`[ec2-user ~]$` sudo /bin/sh ./NVIDIA-Linux-x86_64*.run
```

When prompted, accept the license agreement and specify the
installation options as required (you can accept the default
options). 9. Confirm that the driver is functional. The response for the
following command lists the installed version of the NVIDIA
driver and details about the GPUs.

```
`[ec2-user ~]$` nvidia-smi -q | head
```

10. If you are using NVIDIA vGPU software version 14.x or greater
    on the G4dn, G5, or G5g instances, disable GSP with the
    following commands. For more information about why this is required, see the [NVIDIA documentation](https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp "https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp").

```
`[ec2-user ~]$` sudo touch /etc/modprobe.d/nvidia.conf
```

```
`[ec2-user ~]$` echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
```

11. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

12. (Optional) Depending on your use case, you might complete the
    following optional steps. If you do not require this
    functionality, do not complete these steps.
    1.  To help take advantage of the four displays of up to
        4K resolution, set up the high-performance display
        protocol [Amazon DCV](../../../dcv.md "../../../dcv.md").
    2.  NVIDIA Quadro Virtual Workstation mode is enabled by
        default. To activate GRID Virtual Applications for RDSH
        Application hosting capabilities, complete the GRID
        Virtual Application activation steps in [Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances](activate_grid.md "activate_grid.md").

###### To install the NVIDIA GRID driver on your instance

1. Connect to your instance. Update your package cache and get the package
   updates for your instance.

```
`$` sudo apt-get update -y
```

2. Install **gcc** and **make**, if they are not
   already installed.

```
`[ec2-user ~]$` sudo apt-get install -y gcc make
```

3. (Ubuntu) Upgrade the `linux-aws` package to receive
   the latest version.

```
`$` sudo apt-get upgrade -y linux-aws
```

(Debian) Upgrade package to receive the latest version.

```
`$` sudo apt-get upgrade -y
```

4. Reboot your instance to load the latest kernel version.

```
`$` sudo reboot
```

5. Reconnect to your instance after it has rebooted.
6. Install the kernel headers package for the version of the kernel you are
   currently running.

```
`$` sudo apt-get install -y linux-headers-$(uname -r) linux-modules-extra-$(uname -r)
```

7. Disable the `nouveau` open source driver for NVIDIA
   graphics cards.
   1. Add `nouveau` to the
      `/etc/modprobe.d/blacklist.conf`
      blacklist file. Copy the following code block and paste
      it into a terminal.

   ```
   `$` cat << EOF | sudo tee --append /etc/modprobe.d/blacklist.conf
   blacklist vga16fb
   blacklist nouveau
   blacklist rivafb
   blacklist nvidiafb
   blacklist rivatv
   EOF
   ```

   2. Edit the `/etc/default/grub` file
      and add the following line:

   ```
   GRUB_CMDLINE_LINUX="rdblacklist=nouveau"
   ```

   3. Rebuild the Grub configuration.

   ```
   `$` sudo update-grub
   ```

8. Download the GRID driver installation utility using the
   following command:

```
`$` aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
```

Multiple versions of the GRID driver are stored in this
bucket. You can see all of the available versions using the
following command.

```
`$` aws s3 ls --recursive s3://ec2-linux-nvidia-drivers/
```

9. Add permissions to run the driver installation utility using
   the following command.

```
`$` chmod +x NVIDIA-Linux-x86_64*.run
```

10. Run the self-install script as follows to install the GRID
    driver that you downloaded. For example:

```
`$` sudo /bin/sh ./NVIDIA-Linux-x86_64*.run
```

When prompted, accept the license agreement and specify the
installation options as required (you can accept the default
options). 11. Confirm that the driver is functional. The response for the
following command lists the installed version of the NVIDIA
driver and details about the GPUs.

```
`$` nvidia-smi -q | head
```

12. If you are using NVIDIA vGPU software version 14.x or greater
    on the G4dn, G5, or G5g instances, disable GSP with the following commands.
    For more information about why this is required, see the [NVIDIA documentation](https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp "https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp").

```
`$` sudo touch /etc/modprobe.d/nvidia.conf
```

```
`$` echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
```

13. Reboot the instance.

```
`$` sudo reboot
```

14. (Optional) Depending on your use case, you might complete the
    following optional steps. If you do not require this
    functionality, do not complete these steps.
    1.  To help take advantage of the four displays of up to
        4K resolution, set up the high-performance display
        protocol [Amazon DCV](../../../dcv.md "../../../dcv.md").
    2.  NVIDIA Quadro Virtual Workstation mode is enabled by
        default. To activate GRID Virtual Applications for RDSH
        Application hosting capabilities, complete the GRID
        Virtual Application activation steps in [Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances](activate_grid.md "activate_grid.md").
    3.  Install the GUI desktop/workstation package.

    ```
    `$` sudo apt-get install -y lightdm ubuntu-desktop
    ```

###### To install the NVIDIA GRID driver on your Windows instance

1. Connect to your Windows instance and open a PowerShell window.
2. Download the drivers and the [NVIDIA GRID Cloud End User License Agreement](https://aws-nvidia-license-agreement.s3.amazonaws.com/NvidiaGridAWSUserLicenseAgreement.DOCX "https://aws-nvidia-license-agreement.s3.amazonaws.com/NvidiaGridAWSUserLicenseAgreement.DOCX") from Amazon S3 to
   your desktop using the following PowerShell commands.

```
$Bucket = "ec2-windows-nvidia-drivers"
$KeyPrefix = "latest"
$LocalPath = "$home\Desktop\NVIDIA"
$Objects = Get-S3Object -BucketName $Bucket -KeyPrefix $KeyPrefix -Region us-east-1
foreach ($Object in $Objects) {
$LocalFileName = $Object.Key
if ($LocalFileName -ne '' -and $Object.Size -ne 0) {
$LocalFilePath = Join-Path $LocalPath $LocalFileName
Copy-S3Object -BucketName $Bucket -Key $Object.Key -LocalFile $LocalFilePath -Region us-east-1
}
}
```

Multiple versions of the NVIDIA GRID driver are stored in this bucket.
You can download all of the available Windows versions in the bucket by
removing the `-KeyPrefix $KeyPrefix` option. For information
about the version of the NVIDIA GRID driver for your operating system,
see the [NVIDIA Virtual GPU
(vGPU) Software](https://docs.nvidia.com/vgpu/ "https://docs.nvidia.com/vgpu/") on the NVIDIA website.

Starting with GRID version 11.0, you can use the drivers under
`latest` for both G3 and G4dn instances. We will
not add versions later than 11.0 to `g4/latest`, but
will keep version 11.0 and the earlier versions specific to G4dn under
`g4/latest`.

G5 instances require GRID 13.1 or later (or GRID 12.4 or
later). 3. Navigate to the desktop and double-click the installation file to
launch it (choose the driver version that corresponds to your instance
OS version). Follow the instructions to install the driver and reboot
your instance as required. To verify that the GPU is working properly,
check Device Manager. 4. (Optional) Use the following command to disable the licensing page in
the control panel to prevent users from accidentally changing the
product type (NVIDIA GRID Virtual Workstation is enabled by default).
For more information, see the [GRID Licensing User Guide](https://docs.nvidia.com/vgpu/4.6/grid-licensing-user-guide/index.html "https://docs.nvidia.com/vgpu/4.6/grid-licensing-user-guide/index.html").

###### PowerShell

Run the following PowerShell commands to create the registry value
to disable the licensing page in the control panel. The AWS Tools for PowerShell
in AWS Windows AMIs defaults to the 32-bit version and this
command fails. Instead, use the 64-bit version of PowerShell
included with the operating system.

```
New-Item -Path "HKLM:\SOFTWARE\NVIDIA Corporation\Global" -Name GridLicensing
New-ItemProperty -Path "HKLM:\SOFTWARE\NVIDIA Corporation\Global\GridLicensing" -Name "NvCplDisableManageLicensePage" -PropertyType "DWord" -Value "1"
```

###### Command Prompt

Run the following registry command to create the registry value to
disable the licensing page in the control panel. You can run it
using the Command Prompt window or a 64-bit version of
PowerShell.

```
reg add "HKLM\SOFTWARE\NVIDIA Corporation\Global\GridLicensing" /v NvCplDisableManageLicensePage /t REG_DWORD /d 1
```

5. (Optional) Depending on your use case, you might complete the
   following optional steps. If you do not require this functionality, do
   not complete these steps.
   1. To help take advantage of the four displays of up to 4K
      resolution, set up the high-performance display protocol, [Amazon DCV](../../../dcv.md "../../../dcv.md").
   2. NVIDIA Quadro Virtual Workstation mode is enabled by default.
      To activate GRID Virtual Applications for RDSH Application
      hosting capabilities, complete the GRID Virtual Application
      activation steps in [Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances](activate_grid.md "activate_grid.md").
