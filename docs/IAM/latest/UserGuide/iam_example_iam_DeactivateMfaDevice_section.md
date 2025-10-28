# Use `DeactivateMfaDevice` with a CLI

The following code examples show how to use `DeactivateMfaDevice`.

CLI

**AWS CLI**

**To deactivate an MFA device**

This command deactivates the virtual MFA device with the ARN `arn:aws:iam::210987654321:mfa/BobsMFADevice` that is associated with the user `Bob`.

```
`aws iam deactivate-mfa-device \
 --user-name `Bob` \
 --serial-number `arn:aws:iam::210987654321:mfa/BobsMFADevice``

```

This command produces no output.

For more information, see [Using multi-factor authentication (MFA) in AWS](id_credentials_mfa.md "id_credentials_mfa.md") in the _AWS IAM User Guide_.

- For API details, see
  [DeactivateMfaDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/deactivate-mfa-device.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/deactivate-mfa-device.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This command disables the hardware MFA device associated with the user `Bob` that has the serial number `123456789012`.**

```
Disable-IAMMFADevice -UserName "Bob" -SerialNumber "123456789012"

```

**Example 2: This command disables the virtual MFA device associated with the user `David` that has the ARN `arn:aws:iam::210987654321:mfa/David`.
Note that virtual MFA device is not deleted from the account. The virtual device is still present and appears in the output of the `Get-IAMVirtualMFADevice` command. Before you can create a new virtual MFA device for the same user, you must delete the old one by using the `Remove-IAMVirtualMFADevice` command.**

```
Disable-IAMMFADevice -UserName "David" -SerialNumber "arn:aws:iam::210987654321:mfa/David"

```

- For API details, see
  [DeactivateMfaDevice](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This command disables the hardware MFA device associated with the user `Bob` that has the serial number `123456789012`.**

```
Disable-IAMMFADevice -UserName "Bob" -SerialNumber "123456789012"

```

**Example 2: This command disables the virtual MFA device associated with the user `David` that has the ARN `arn:aws:iam::210987654321:mfa/David`.
Note that virtual MFA device is not deleted from the account. The virtual device is still present and appears in the output of the `Get-IAMVirtualMFADevice` command. Before you can create a new virtual MFA device for the same user, you must delete the old one by using the `Remove-IAMVirtualMFADevice` command.**

```
Disable-IAMMFADevice -UserName "David" -SerialNumber "arn:aws:iam::210987654321:mfa/David"

```

- For API details, see
  [DeactivateMfaDevice](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
