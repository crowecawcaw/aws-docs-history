# Use `EnableMfaDevice` with a CLI

The following code examples show how to use `EnableMfaDevice`.

CLI

**AWS CLI**

**To enable an MFA device**

After you use the `create-virtual-mfa-device` command to create a new virtual MFA device, you can assign the MFA device to a user. The following `enable-mfa-device` example assigns the MFA device with the serial number `arn:aws:iam::210987654321:mfa/BobsMFADevice` to the user `Bob`. The command also synchronizes the device with AWS by including the first two codes in sequence from the virtual MFA device.

```
`aws iam enable-mfa-device \
 --user-name `Bob` \
 --serial-number `arn:aws:iam::210987654321:mfa/BobsMFADevice` \
 --authentication-code1 `123456` \
 --authentication-code2 `789012``

```

This command produces no output.

For more information, see [Enabling a virtual multi-factor authentication (MFA) device](id_credentials_mfa_enable_virtual.md "id_credentials_mfa_enable_virtual.md") in the _AWS IAM User Guide_.

- For API details, see
  [EnableMfaDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-mfa-device.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-mfa-device.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This command enables the hardware MFA device with the serial number `987654321098` and associates the device with the user `Bob`. It includes the first two codes in sequence from the device.**

```
Enable-IAMMFADevice -UserName "Bob" -SerialNumber "987654321098" -AuthenticationCode1 "12345678" -AuthenticationCode2 "87654321"

```

**Example 2: This example creates and enables a virtual MFA device. The first command creates the virtual device and returns the device's object representation in the variable `$MFADevice`. You can use the `.Base32StringSeed` or `QRCodePng` properties to configure the user's software application.
The final command assigns the device to the user `David`, identifying the device by its serial number. The command also synchronizes the device with AWS by including the first two codes in sequence from the virtual MFA device.**

```
$MFADevice = New-IAMVirtualMFADevice -VirtualMFADeviceName "MyMFADevice"
# see example for New-IAMVirtualMFADevice to see how to configure the software program with PNG or base32 seed code
Enable-IAMMFADevice -UserName "David" -SerialNumber -SerialNumber $MFADevice.SerialNumber -AuthenticationCode1 "24681357" -AuthenticationCode2 "13572468"

```

- For API details, see
  [EnableMfaDevice](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This command enables the hardware MFA device with the serial number `987654321098` and associates the device with the user `Bob`. It includes the first two codes in sequence from the device.**

```
Enable-IAMMFADevice -UserName "Bob" -SerialNumber "987654321098" -AuthenticationCode1 "12345678" -AuthenticationCode2 "87654321"

```

**Example 2: This example creates and enables a virtual MFA device. The first command creates the virtual device and returns the device's object representation in the variable `$MFADevice`. You can use the `.Base32StringSeed` or `QRCodePng` properties to configure the user's software application.
The final command assigns the device to the user `David`, identifying the device by its serial number. The command also synchronizes the device with AWS by including the first two codes in sequence from the virtual MFA device.**

```
$MFADevice = New-IAMVirtualMFADevice -VirtualMFADeviceName "MyMFADevice"
# see example for New-IAMVirtualMFADevice to see how to configure the software program with PNG or base32 seed code
Enable-IAMMFADevice -UserName "David" -SerialNumber -SerialNumber $MFADevice.SerialNumber -AuthenticationCode1 "24681357" -AuthenticationCode2 "13572468"

```

- For API details, see
  [EnableMfaDevice](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
