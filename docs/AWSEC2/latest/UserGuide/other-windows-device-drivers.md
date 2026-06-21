# Other Windows device drivers

The AWS VMClock device is a virtual clock device that is present on Nitro-based
instances. The device appears in Device Manager under **System devices**
as `AWS VMClock Device`. AWS provides a null (no-function) driver package
for Windows that allows the operating system to recognize the device.

## Supported instances

The AWS VMClock device is available on Nitro-based instance types. For a list of
Nitro-based instance types, see [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type").

## Supported operating systems

The driver package supports the following versions of Windows Server:

- Windows Server 2016
- Windows Server 2019
- Windows Server 2022
- Windows Server 2025

## Driver installation

If the AWS VMClock device shows a warning icon in Device Manager, which indicates
that no driver is installed, you can install the null driver package manually.

###### To install the AWS VMClock driver

1. [Download](https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSVMClock/Latest/AWSVMClock.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSVMClock/Latest/AWSVMClock.zip") and extract the driver package from Amazon S3.

```
Invoke-WebRequest https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSVMClock/Latest/AWSVMClock.zip -OutFile $env:USERPROFILE\AWSVMClock.zip
Expand-Archive $env:USERPROFILE\AWSVMClock.zip -DestinationPath $env:USERPROFILE\AWSVMClock
```

2. Install the driver using `pnputil`.

```
pnputil /add-driver $env:USERPROFILE\AWSVMClock\aws_vmclock.inf /install
```

3. Verify the device status in Device Manager. You don't need to reboot the instance.
