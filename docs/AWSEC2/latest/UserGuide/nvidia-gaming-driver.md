# Install NVIDIA gaming drivers (G7e, G6, G6e, G5, and G4dn

instances)

These drivers are available to AWS customers only. By downloading them, you agree to use the
downloaded software only to develop AMIs for use with the RTX PRO 6000 Blackwell, NVIDIA L4, NVIDIA L40S,
NVIDIA A10G, NVIDIA Tesla T4, or NVIDIA Tesla M60 hardware. You can use the GRID drivers to both
create and use AMIs within the AWS environment. Upon installation of the software, you are bound
by the terms of the [NVIDIA GRID Cloud End User License Agreement](https://aws-nvidia-license-agreement.s3.amazonaws.com/NvidiaGridAWSUserLicenseAgreement.DOCX "https://aws-nvidia-license-agreement.s3.amazonaws.com/NvidiaGridAWSUserLicenseAgreement.DOCX").

###### Considerations

- G3 instances require AWS provided DNS resolution for GRID licensing
  to work.
- [IMDSv2](configuring-instance-metadata-service.md "configuring-instance-metadata-service.md") is
  only supported with NVIDIA driver version 495.x or greater.

###### Prerequisites

- (Linux) Verify that the AWS CLI is installed on your instance and configured
  with default credentials. For more information, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
  in the _AWS Command Line Interface User Guide_.
- Your user or role must have the permissions granted that contains the
  **AmazonS3ReadOnlyAccess** policy.

###### To install the NVIDIA gaming driver on your instance

1. Connect to your instance. Update your package cache and get the package
   updates for your instance.

```
`[ec2-user ~]$` sudo dnf update -y
```

2. Install **gcc** and **make**,
   if they are not already installed.

```
`[ec2-user ~]$` sudo dnf install gcc make
```

3. Reboot your instance to load the latest kernel version.

```
`[ec2-user ~]$` sudo reboot
```

4. Reconnect to your instance after it is rebooted.
5. Install the kernel headers packages.

```
`[ec2-user ~]$` sudo dnf install -y kernel-devel kernel-modules-extra kernel-devel-$(uname -r) kernel-headers-$(uname -r) dkms
```

6. Download the gaming driver installation utility using the
   following command:

```
`[ec2-user ~]$` aws s3 cp --recursive s3://nvidia-gaming/linux/latest/ .
```

Multiple versions of the gaming driver are stored in this
bucket. You can see all of the available versions using the
following command:

```
`[ec2-user ~]$` aws s3 ls --recursive s3://nvidia-gaming/linux/
```

7. Extract the gaming driver installation utility from the
   downloaded `.zip` archive.

```
`[ec2-user ~]$` unzip `latest-driver-name`.zip -d nvidia-drivers
```

8. Add permissions to run the driver installation utility using
   the following command:

```
`[ec2-user ~]$` chmod +x nvidia-drivers/NVIDIA-Linux-x86_64*-grid.run
```

9. Run the installer using the following command:

```
`[ec2-user ~]$` sudo ./nvidia-drivers/NVIDIA-Linux-x86_64*.run
```

When prompted, accept the license agreement and specify the
installation options as required (you can accept the default
options). 10. Use the following command to create the required configuration
file.

```
`[ec2-user ~]$` cat << EOF | sudo tee -a /etc/nvidia/gridd.conf
vGamingMarketplace=2
EOF
```

11. Use the following command to download and rename the certification file.
    - For version 460.39 or later:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertLinux_2024_02_22.cert"
    ```

    - For version 440.68 to 445.48:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2020_04.cert"
    ```

    - For earlier versions:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2019_09.cert"
    ```

12. If you are using NVIDIA driver version 510.x or greater on the
    G4dn, G5, or G5g instances, disable GSP with the following
    commands. For more information about why this is required, see the
    [NVIDIA documentation](https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp "https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp").

```
`[ec2-user ~]$` sudo touch /etc/modprobe.d/nvidia.conf
```

```
`[ec2-user ~]$` echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
```

13. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

14. Verify the NVIDIA Gaming license using the following command.

```
`[ec2-user ~]$` nvidia-smi.exe -q
```

In the output, search for `vGPU Software Licensed Product`. 15. (Optional) To help take advantage of a single display of up to
4K resolution, set up the high-performance display protocol
[Amazon DCV](../../../dcv.md "../../../dcv.md").

###### To install the NVIDIA gaming driver on your instance

1. Connect to your instance. Update your package cache and get the package
   updates for your instance.

```
`[ec2-user ~]$` sudo yum update -y
```

2. Install **gcc** and **make**,
   if they are not already installed.

```
`[ec2-user ~]$` sudo yum install gcc make
```

3. Reboot your instance to load the latest kernel version.

```
`[ec2-user ~]$` sudo reboot
```

4. Reconnect to your instance after it is rebooted.
5. Install the kernel
   headers package for the version of the kernel you are currently
   running.

```
`[ec2-user ~]$` sudo yum install -y kernel-devel-$(uname -r)
```

6. Download the gaming driver installation utility using the
   following command:

```
`[ec2-user ~]$` aws s3 cp --recursive s3://nvidia-gaming/linux/latest/ .
```

Multiple versions of the gaming driver are stored in this
bucket. You can see all of the available versions using the
following command:

```
`[ec2-user ~]$` aws s3 ls --recursive s3://nvidia-gaming/linux/
```

7. Extract the gaming driver installation utility from the
   downloaded `.zip` archive.

```
`[ec2-user ~]$` unzip `latest-driver-name`.zip -d nvidia-drivers
```

8. Add permissions to run the driver installation utility using
   the following command:

```
`[ec2-user ~]$` chmod +x nvidia-drivers/NVIDIA-Linux-x86_64*-grid.run
```

9. Run the installer using the following command:

```
`[ec2-user ~]$` sudo ./nvidia-drivers/NVIDIA-Linux-x86_64*.run
```

If you are using Amazon Linux 2 with kernel version 5.10, use the
following command to install the NVIDIA gaming
drivers.

```
`[ec2-user ~]$` sudo CC=/usr/bin/gcc10-cc ./NVIDIA-Linux-x86_64*.run
```

When prompted, accept the license agreement and specify the
installation options as required (you can accept the default
options). 10. Use the following command to create the required configuration
file.

```
`[ec2-user ~]$` cat << EOF | sudo tee -a /etc/nvidia/gridd.conf
vGamingMarketplace=2
EOF
```

11. Use the following command to download and rename the
    certification file.
    - For version 460.39 or later:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertLinux_2024_02_22.cert"
    ```

    - For version 440.68 to 445.48:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2020_04.cert"
    ```

    - For earlier versions:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2019_09.cert"
    ```

12. If you are using NVIDIA driver version 510.x or greater on the
    G4dn, G5, or G5g instances, disable GSP with the following
    commands. For more information about why this is required, see the
    [NVIDIA documentation](https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp "https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp").

```
`[ec2-user ~]$` sudo touch /etc/modprobe.d/nvidia.conf
```

```
`[ec2-user ~]$` echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
```

13. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

14. Verify the NVIDIA Gaming license using the following command.

```
`[ec2-user ~]$` nvidia-smi.exe -q
```

In the output, search for `vGPU Software Licensed Product`. 15. (Optional) To help take advantage of a single display of up to
4K resolution, set up the high-performance display protocol
[Amazon DCV](../../../dcv.md "../../../dcv.md").

###### To install the NVIDIA gaming driver on your instance

1. Connect to your Linux instance. Install **gcc**
   and **make**, if they are not already
   installed.

```
`[ec2-user ~]$` sudo yum install -y gcc make
```

2. Update your package cache and get the package updates for your
   instance.

```
`[ec2-user ~]$` sudo yum update -y
```

3. Reboot your instance to load the latest kernel version.

```
`[ec2-user ~]$` sudo reboot
```

4. Reconnect to your instance after it has rebooted.
5. Install the kernel
   headers package for the version of the kernel you are currently
   running.

```
`[ec2-user ~]$` sudo yum install -y unzip kernel-devel-$(uname -r)
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

7. Download the gaming driver installation utility using the
   following command:

```
`[ec2-user ~]$` aws s3 cp --recursive s3://nvidia-gaming/linux/latest/ .
```

Multiple versions of the gaming driver are stored in this
bucket. You can see all of the available versions using the
following command:

```
`[ec2-user ~]$` aws s3 ls --recursive s3://nvidia-gaming/linux/
```

8. Extract the gaming driver installation utility from the
   downloaded `.zip` archive.

```
`[ec2-user ~]$` unzip *Gaming-Linux-Guest-Drivers.zip -d nvidia-drivers
```

9. Add permissions to run the driver installation utility using
   the following command:

```
`[ec2-user ~]$` chmod +x nvidia-drivers/NVIDIA-Linux-x86_64*-grid.run
```

10. Run the installer using the following command:

```
`[ec2-user ~]$` sudo nvidia-drivers/NVIDIA-Linux-x86_64*.run
```

When prompted, accept the license agreement and specify the
installation options as required (you can accept the default
options). 11. Use the following command to create the required configuration
file.

```
`[ec2-user ~]$` cat << EOF | sudo tee -a /etc/nvidia/gridd.conf
vGamingMarketplace=2
EOF
```

12. Use the following command to download and rename the
    certification file.
    - For version 460.39 or later:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertLinux_2024_02_22.cert"
    ```

    - For version 440.68 to 445.48:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2020_04.cert"
    ```

    - For earlier versions:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2019_09.cert"
    ```

13. If you are using NVIDIA driver version 510.x or greater on the
    G4dn, G5, or G5g instances, disable GSP with the following
    commands. For more information about why this is required, see the [NVIDIA documentation](https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp "https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp").

```
`[ec2-user ~]$` sudo touch /etc/modprobe.d/nvidia.conf
```

```
`[ec2-user ~]$` echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
```

14. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

15. (Optional) To help take advantage of a single display of up to
    4K resolution, set up the high-performance display protocol
    [Amazon DCV](../../../dcv.md "../../../dcv.md"). If
    you do not require this functionality, do not complete this
    step.

###### To install the NVIDIA gaming driver on your instance

1. Connect to your Linux instance. Install **gcc**
   and **make**, if they are not already
   installed.

```
`[ec2-user ~]$` sudo yum install -y gcc make
```

2. Update your package cache and get the package updates for your
   instance.

```
`[ec2-user ~]$` sudo yum update -y
```

3. Reboot your instance to load the latest kernel version.

```
`[ec2-user ~]$` sudo reboot
```

4. Reconnect to your instance after it has rebooted.
5. Install the kernel
   headers package for the version of the kernel you are currently
   running.

```
`[ec2-user ~]$` sudo yum install -y unzip kernel-devel-$(uname -r)
```

6. Download the gaming driver installation utility using the
   following command:

```
`[ec2-user ~]$` aws s3 cp --recursive s3://nvidia-gaming/linux/latest/ .
```

Multiple versions of the gaming driver are stored in this
bucket. You can see all of the available versions using the
following command:

```
`[ec2-user ~]$` aws s3 ls --recursive s3://nvidia-gaming/linux/
```

7. Extract the gaming driver installation utility from the
   downloaded `.zip` archive.

```
`[ec2-user ~]$` unzip *Gaming-Linux-Guest-Drivers.zip -d nvidia-drivers
```

8. Add permissions to run the driver installation utility using
   the following command:

```
`[ec2-user ~]$` chmod +x nvidia-drivers/NVIDIA-Linux-x86_64*-grid.run
```

9. Run the installer using the following command:

```
`[ec2-user ~]$` sudo nvidia-drivers/NVIDIA-Linux-x86_64*.run
```

When prompted, accept the license agreement and specify the
installation options as required (you can accept the default
options). 10. Use the following command to create the required configuration
file.

```
`[ec2-user ~]$` cat << EOF | sudo tee -a /etc/nvidia/gridd.conf
vGamingMarketplace=2
EOF
```

11. Use the following command to download and rename the
    certification file.
    - For version 460.39 or later:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertLinux_2024_02_22.cert"
    ```

    - For version 440.68 to 445.48:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2020_04.cert"
    ```

    - For earlier versions:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2019_09.cert"
    ```

12. If you are using NVIDIA driver version 510.x or greater on the
    G4dn, G5, or G5g instances, disable GSP with the following
    commands. For more information about why this is required, see the
    [NVIDIA documentation](https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp "https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp").

```
`[ec2-user ~]$` sudo touch /etc/modprobe.d/nvidia.conf
```

```
`[ec2-user ~]$` echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
```

13. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

14. (Optional) To help take advantage of a single display of up to
    4K resolution, set up the high-performance display protocol
    [Amazon DCV](../../../dcv.md "../../../dcv.md").

###### To install the NVIDIA gaming driver on your instance

1. Connect to your Linux instance. Install **gcc**
   and **make**, if they are not already
   installed.

```
`[ec2-user ~]$` sudo yum install -y gcc make
```

2. Update your package cache and get the package updates for your
   instance.

```
`[ec2-user ~]$` sudo yum update -y
```

3. Reboot your instance to load the latest kernel version.

```
`[ec2-user ~]$` sudo reboot
```

4. Reconnect to your instance after it has rebooted.
5. Install the kernel
   headers package for the version of the kernel you are currently
   running.

```
`[ec2-user ~]$` sudo dnf install -y unzip elfutils-libelf-devel libglvnd-devel kernel-devel-$(uname -r)
```

6. Download the gaming driver installation utility using the
   following command:

```
`[ec2-user ~]$` aws s3 cp --recursive s3://nvidia-gaming/linux/latest/ .
```

Multiple versions of the gaming driver are stored in this
bucket. You can see all of the available versions using the
following command:

```
`[ec2-user ~]$` aws s3 ls --recursive s3://nvidia-gaming/linux/
```

7. Extract the gaming driver installation utility from the
   downloaded `.zip` archive.

```
`[ec2-user ~]$` unzip *Gaming-Linux-Guest-Drivers.zip -d nvidia-drivers
```

8. Add permissions to run the driver installation utility using
   the following command:

```
`[ec2-user ~]$` chmod +x nvidia-drivers/NVIDIA-Linux-x86_64*-grid.run
```

9. Run the installer using the following command:

```
`[ec2-user ~]$` sudo nvidia-drivers/NVIDIA-Linux-x86_64*.run
```

When prompted, accept the license agreement and specify the
installation options as required (you can accept the default
options). 10. Use the following command to create the required configuration
file.

```
`[ec2-user ~]$` cat << EOF | sudo tee -a /etc/nvidia/gridd.conf
vGamingMarketplace=2
EOF
```

11. Use the following command to download and rename the
    certification file.
    - For version 460.39 or later:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertLinux_2024_02_22.cert"
    ```

    - For version 440.68 to 445.48:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2020_04.cert"
    ```

    - For earlier versions:

    ```
    `[ec2-user ~]$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2019_09.cert"
    ```

12. If you are using NVIDIA driver version 510.x or greater on the
    G4dn, G5, or G5g instances, disable GSP with the following
    commands. For more information about why this is required, see the
    [NVIDIA documentation](https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp "https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp").

```
`[ec2-user ~]$` sudo touch /etc/modprobe.d/nvidia.conf
```

```
`[ec2-user ~]$` echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
```

13. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

14. (Optional) To help take advantage of a single display of up to
    4K resolution, set up the high-performance display protocol
    [Amazon DCV](../../../dcv.md "../../../dcv.md").

###### To install the NVIDIA gaming driver on your instance

1. Connect to your Linux instance. Install **gcc**
   and **make**, if they are not already
   installed.

```
`$` sudo apt-get install -y gcc make build-essential
```

2. Update your package cache and get the package updates for your
   instance.

```
`$` sudo apt-get update -y
```

3. Upgrade the `linux-aws` package to receive the
   latest version.

```
`$` sudo apt-get upgrade -y linux-aws
```

4. Reboot your instance to load the latest kernel version.

```
`$` sudo reboot
```

5. Reconnect to your instance after it has rebooted.
6. Install the kernel
   headers package for the version of the kernel you are currently
   running.

```
`$` sudo apt install -y unzip dkms linux-headers-$(uname -r)
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

8. Download the gaming driver installation utility using the
   following command:

```
`$` aws s3 cp --recursive s3://nvidia-gaming/linux/latest/ .
```

Multiple versions of the gaming driver are stored in this
bucket. You can see all of the available versions using the
following command:

```
`$` aws s3 ls --recursive s3://nvidia-gaming/linux/
```

9. Extract the gaming driver installation utility from the
   downloaded `.zip` archive.

```
`$` unzip *Gaming-Linux-Guest-Drivers.zip -d nvidia-drivers
```

10. Add permissions to run the driver installation utility using
    the following command:

```
`$` chmod +x nvidia-drivers/NVIDIA-Linux-x86_64*-grid.run
```

11. Run the installer using the following command:

```
`$` sudo nvidia-drivers/NVIDIA-Linux-x86_64*.run
```

When prompted, accept the license agreement and specify the
installation options as required (you can accept the default
options). 12. Use the following command to create the required configuration
file.

```
`$` cat << EOF | sudo tee -a /etc/nvidia/gridd.conf
vGamingMarketplace=2
EOF
```

13. Use the following command to download and rename the
    certification file.
    - For version 460.39 or later:

    ```
    `$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertLinux_2024_02_22.cert"
    ```

    - For version 440.68 to 445.48:

    ```
    `$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2020_04.cert"
    ```

    - For earlier versions:

    ```
    `$` sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2019_09.cert"
    ```

14. If you are using NVIDIA driver version 510.x or greater on the
    G4dn, G5, or G5g instances, disable GSP with the following
    commands. For more information about why this is required, see the
    [NVIDIA documentation](https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp "https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/index.html#disabling-gsp").

```
`$` sudo touch /etc/modprobe.d/nvidia.conf
```

```
`$` echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
```

15. Reboot the instance.

```
`$` sudo reboot
```

16. (Optional) To help take advantage of a single display of up to
    4K resolution, set up the high-performance display protocol
    [Amazon DCV](../../../dcv.md "../../../dcv.md"). If
    you do not require this functionality, do not complete this
    step.
    Before you install an NVIDIA gaming driver on your instance, you
    must ensure that the following prerequisites are met in addition to the
    considerations mentioned for all gaming drivers.

- If you launch your Windows instance using a custom Windows AMI, the
  AMI must be a standardized image created with
  Windows Sysprep to ensure that the gaming driver works. For more
  information, see [Create an Amazon EC2 AMI using Windows Sysprep](ami-create-win-sysprep.md "ami-create-win-sysprep.md").
- Configure default credentials for the AWS Tools for Windows PowerShell on your Windows
  instance. For more information, see [Getting Started with
  the AWS Tools for Windows PowerShell](../../../powershell/latest/userguide/pstools-getting-started.md "../../../powershell/latest/userguide/pstools-getting-started.md") in the
  _AWS Tools for PowerShell User Guide_.

###### To install the NVIDIA gaming driver on your Windows instance

1. Connect to your Windows instance and open a PowerShell window.
2. Download and install the gaming driver using the following PowerShell
   commands.

```
$Bucket = "nvidia-gaming"
$KeyPrefix = "windows/latest"
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

Multiple versions of the NVIDIA GRID driver are stored in this S3
bucket. You can download all of the available versions in the bucket if
you change the value of the `$KeyPrefix` variable from
_"windows/latest"_ to
_"windows"_. 3. Navigate to the desktop and double-click the installation file to
launch it (choose the driver version that corresponds to your instance
OS version). Follow the instructions to install the driver and reboot
your instance as required. To verify that the GPU is working properly,
check Device Manager. 4. Use one of the following methods to register the driver.

Version 527.27 or above
Create the following registry key with the 64-bit version
of PowerShell, or the Command Prompt window.

_key_:
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\nvlddmkm\Global`

_name_: vGamingMarketplace

_type_: DWord

_value_: 2

###### PowerShell

Run the following PowerShell command to create this
registry value. The AWS Tools for PowerShell in AWS Windows AMIs
defaults to the 32-bit version and this command fails.
Instead, use the 64-bit version of PowerShell included
with the operating system.

```
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\nvlddmkm\Global" -Name "vGamingMarketplace" -PropertyType "DWord" -Value "2"
```

###### Command Prompt

Run the following registry command to create this
registry value. You can run it using the Command Prompt
window or a 64-bit version of PowerShell.

```
reg add "HKLM\SYSTEM\CurrentControlSet\Services\nvlddmkm\Global" /v vGamingMarketplace /t REG_DWORD /d 2
```

Earlier versions
Create the following registry key with the 64-bit version
of PowerShell, or the Command Prompt window.

_key_:
`HKEY_LOCAL_MACHINE\SOFTWARE\NVIDIA
 Corporation\Global`

_name_: vGamingMarketplace

_type_: DWord

_value_: 2

###### PowerShell

Run the following PowerShell command to create this
registry value. The AWS Tools for PowerShell in AWS Windows AMIs
defaults to the 32-bit version and this command fails.
Instead, use the 64-bit version of PowerShell included
with the operating system.

```
New-ItemProperty -Path "HKLM:\SOFTWARE\NVIDIA Corporation\Global" -Name "vGamingMarketplace" -PropertyType "DWord" -Value "2"
```

###### Command Prompt

Run the following registry command to create this
registry key with the Command Prompt window. You can
also use this command in the 64-bit version of
PowerShell.

```
reg add "HKLM\SOFTWARE\NVIDIA Corporation\Global" /v vGamingMarketplace /t REG_DWORD /d 2
```

5. Run the following command in PowerShell. This downloads the
   certification file, renames the file
   `GridSwCert.txt`, and moves the file to the Public
   Documents folder on your system drive. Typically, the folder path is
   `C:\Users\Public\Documents`.
   - For version 460.39 or later:

   ```
   Invoke-WebRequest -Uri "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertWindows_2024_02_22.cert" -OutFile "$Env:PUBLIC\Documents\GridSwCert.txt"
   ```

   - For version 445.87:

   ```
   Invoke-WebRequest -Uri "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Windows_2020_04.cert" -OutFile "$Env:PUBLIC\Documents\GridSwCert.txt"
   ```

   - For earlier versions:

   ````
   Invoke-WebRequest -Uri "https://nvidia-gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Windows_2019_09.cert" -OutFile "$Env:PUBLIC\Documents\GridSwCert.txt"
   ```If you receive an error when downloading the file, and you
   are using Windows Server 2016 or earlier, TLS 1.2 might need
   to be enabled for your PowerShell terminal. You can enable
   TLS 1.2 for the current PowerShell session with the
   following command and then try again:
   ````

```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

6. Reboot your instance.
7. Locate the `nvidia-smi.exe` file on the instance.

```
Get-ChildItem -Path C:\ -Recurse -Filter "nvidia-smi.exe"
```

Verify the NVIDIA Gaming license using the following command. Replace
`path` with the name of the folder in the output
from the previous command.

```
C:\Windows\System32\DriverStore\FileRepository\`path`\nvidia-smi.exe -q
```

The output should be similar to the following.

```
vGPU Software Licensed Product
Product Name              : NVIDIA Cloud Gaming
License Status            : Licensed (Expiry: N/A)
```

8. (Optional) To help take advantage of the single display of up to 4K
   resolution, set up the high-performance display protocol [Amazon DCV](../../../dcv.md "../../../dcv.md"). If you do not
   require this functionality, do not complete this step.
