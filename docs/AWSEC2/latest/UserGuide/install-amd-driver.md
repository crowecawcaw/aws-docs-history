# AMD drivers for your EC2 instance

An instance with an attached AMD GPU, such as a G4ad instance, must have the
appropriate AMD driver installed. Depending on your requirements, you can either use an
AMI with the driver preinstalled or download a driver from Amazon S3.

To install NVIDIA drivers on an instance with an attached NVIDIA GPU, such as a G4dn
instance, see [NVIDIA drivers](install-nvidia-driver.md "install-nvidia-driver.md") instead.

###### Contents

- [AMD Radeon Pro
  Software for Enterprise Driver](install-amd-driver.md#amd-radeon-pro-software-for-enterprise-driver "install-amd-driver.md#amd-radeon-pro-software-for-enterprise-driver")
- [AMIs with the AMD driver installed](install-amd-driver.md#preinstalled-amd-driver "install-amd-driver.md#preinstalled-amd-driver")
- [AMD driver download](install-amd-driver.md#download-amd-driver "install-amd-driver.md#download-amd-driver")

## AMD Radeon Pro

Software for Enterprise Driver

The AMD Radeon Pro Software for Enterprise Driver is built to deliver support for
professional-grade graphics use cases. Using the driver, you can configure your
instances with two 4K displays per GPU.

###### Supported APIs

- OpenGL, OpenCL
- Vulkan
- AMD Advanced Media Framework
- Video Acceleration API
- DirectX 9 and later
- Microsoft Hardware Media Foundation Transform

## AMIs with the AMD driver installed

AWS offers different Amazon Machine Images (AMIs) that come with the AMD drivers
installed. Open [Marketplace offerings with the AMD driver](https://aws.amazon.com/marketplace/search/results?page=1&filters=VendorId&VendorId=e6a5002c-6dd0-4d1e-8196-0a1d1857229b&searchTerms=AMD+Radeon+Pro+Driver "https://aws.amazon.com/marketplace/search/results?page=1&filters=VendorId&VendorId=e6a5002c-6dd0-4d1e-8196-0a1d1857229b&searchTerms=AMD+Radeon+Pro+Driver").

## AMD driver download

If you aren't using an AMI with the AMD driver installed, you can download the AMD
driver and install it on your instance. Only the following operating system versions
support AMD drivers:

- Amazon Linux 2 with kernel version 5.4
- Ubuntu 20.04
- Ubuntu 22.04
- Ubuntu 24.04
- Windows Server 2016
- Windows Server 2019
- Windows Server 2022

These downloads are available to AWS customers only. By downloading, you agree
to use the downloaded software only to develop AMIs for use with the AMD Radeon
Pro V520 hardware. Upon installation of the software, you are bound by the terms of
the [AMD End User License Agreement](https://www.amd.com/en/legal/eula.html "https://www.amd.com/en/legal/eula.html").

1. Connect to your Linux instance.
2. Install the AWS CLI on your Linux instance and configure default
   credentials. For more information, see [Installing the
   AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

###### Important

Your user or role must have the permissions granted that contains the
**AmazonS3ReadOnlyAccess** policy. For more
information, see [AWS managed policy: AmazonS3ReadOnlyAccess](../../../AmazonS3/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-amazons3readonlyaccess "../../../AmazonS3/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-amazons3readonlyaccess") in the _Amazon Simple Storage Service User Guide_. 3. Install kernel 5.4

```
`$` `sudo amazon-linux-extras disable kernel-5.10`
`$` `sudo amazon-linux-extras enable kernel-5.4`
`$` `sudo yum install -y kernel`
```

4. Install **gcc** and **make**, if they are not already installed.

```
`$` `sudo yum install gcc make`
```

5. Update your package cache and get the package updates for your
   instance.

```
`$` `sudo amazon-linux-extras install epel -y`
`$` `sudo yum update -y`
```

6. Reboot the instance.

```
`$` `sudo reboot`
```

7. Reconnect to the instance after it reboots.
8. Download the latest AMD driver.

```
`$` `aws s3 cp --recursive s3://ec2-amd-linux-drivers/latest/ .`
```

9. Extract the file.

```
`$` `tar -xf amdgpu-pro-*rhel*.tar.xz`
```

10. Change to the folder for the extracted driver.
11. Run the self install script to install the full graphics stack.

```
`$` `./amdgpu-pro-install -y --opencl=pal,legacy`
```

12. Reboot the instance.

```
`$` `sudo reboot`
```

13. Confirm that the driver is functional.

```
`$` `sudo dmesg | grep amdgpu`
```

The response should look like the following:

```
`Initialized amdgpu`
```

1. Connect to your Linux instance.
2. Update your package cache and get the package updates for your instance.

```
`$` `sudo apt-get update --fix-missing && sudo apt-get upgrade -y`
```

3. Install **gcc** and **make**, if they are not already installed.

```
`$` `sudo apt install build-essential -y`
```

4. Install Linux firmware and kernel modules

```
`$` `sudo apt install linux-firmware linux-modules-extra-aws -y`
```

5. Reboot instance

```
`$` `sudo reboot`
```

6. Reconnect to the instance after it reboots.
7. Install the AMD Linux driver package
   - For Ubuntu 20.04:

   ```
   `$` `wget https://repo.radeon.com/.preview/afe3e25b8f1beff0bb312e27924d63b5/amdgpu-install/5.4.02.01/ubuntu/focal/amdgpu-install_5.4.02.01.50402-1_all.deb`
   `$` `sudo dpkg --add-architecture i386`
   `$` `sudo apt install ./amdgpu-install_5.4.02.01.50402-1_all.deb`
   ```

   - For later Ubuntu versions go to [Linux® Drivers for AMD Radeon™ Graphics](https://www.amd.com/en/support/download/linux-drivers.html "https://www.amd.com/en/support/download/linux-drivers.html") and
     download the latest Ubuntu package and install it.

   ```
   `$` `sudo apt install ./amdgpu-install_{version-you-downloaded}.deb`
   ```

8. Run the self install script to install the full graphics stack.

```
`$` `amdgpu-install --usecase=workstation --vulkan=pro -y`
```

9. Reboot the instance.

```
`$` `sudo reboot`
```

10. Confirm that the driver is functional.

```
`$` `sudo dmesg | grep amdgpu`
```

The response should look like the following:

```
`Initialized amdgpu`
```

1. Connect to your Windows instance and open a PowerShell window.
2. Configure default credentials for the AWS Tools for Windows PowerShell on your Windows instance.
   For more information, see [Getting Started with the
   AWS Tools for Windows PowerShell](../../../powershell/latest/userguide/pstools-getting-started.md "../../../powershell/latest/userguide/pstools-getting-started.md") in the _AWS Tools for PowerShell User Guide_.

###### Important

Your user or role must have the permissions granted that contains the
**AmazonS3ReadOnlyAccess** policy. For more
information, see [AWS managed policy: AmazonS3ReadOnlyAccess](../../../AmazonS3/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-amazons3readonlyaccess "../../../AmazonS3/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-amazons3readonlyaccess") in the _Amazon Simple Storage Service User Guide_. 3. Set the key prefix according to your version of Windows:

    * Windows 10 and Windows 11



    ```
    $KeyPrefix = "latest/AMD_GPU_WINDOWS10"
    ```
    * Windows Server 2016



    ```
    $KeyPrefix = "archives"
    ```
    * Windows Server 2019



    ```
    $KeyPrefix = "latest/AMD_GPU_WINDOWS_2K19" # use "archives" for Windows Server 2016
    ```
    * Windows Server 2022



    ```
    $KeyPrefix = "latest/AMD_GPU_WINDOWS_2K22"
    ```

4. Download the drivers from Amazon S3 to your desktop using the following
   PowerShell commands.

```
$Bucket = "ec2-amd-windows-drivers"
$LocalPath = "$home\Desktop\AMD"
$Objects = Get-S3Object -BucketName $Bucket -KeyPrefix $KeyPrefix -Region us-east-1
foreach ($Object in $Objects) {
$LocalFileName = $Object.Key
if ($LocalFileName -ne '' -and $Object.Size -ne 0) {
    $LocalFilePath = Join-Path $LocalPath $LocalFileName
    Copy-S3Object -BucketName $Bucket -Key $Object.Key -LocalFile $LocalFilePath -Region us-east-1
    }
}
```

5. Unzip the downloaded driver file and run the installer using the following
   PowerShell commands.

```
Expand-Archive $LocalFilePath -DestinationPath "$home\Desktop\AMD\$KeyPrefix" -Verbose

```

Now, check the content of the new directory. The directory name can be
retrieved using the `Get-ChildItem` PowerShell command.

```
Get-ChildItem "$home\Desktop\AMD\$KeyPrefix"
```

The output should be similar to the following:

```
Directory: C:\Users\Administrator\Desktop\AMD\latest

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       10/13/2021  12:52 AM                210414a-365562C-Retail_End_User.2
```

Install the drivers:

```
pnputil /add-driver $home\Desktop\AMD\$KeyPrefix\*.inf /install /subdirs
```

6. Follow the instructions to install the driver and reboot your instance as
   required.
7. To verify that the GPU is working properly, check Device Manager. You
   should see "AMD Radeon Pro V520 MxGPU" listed as a display adapter.
8. To help take advantage of the four displays of up to 4K resolution, set up
   the high-performance display protocol, [Amazon DCV](../../../dcv.md "../../../dcv.md").
