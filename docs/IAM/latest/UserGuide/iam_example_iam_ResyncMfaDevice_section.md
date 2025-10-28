# Use `ResyncMfaDevice` with a CLI

The following code examples show how to use `ResyncMfaDevice`.

CLI

**AWS CLI**

**To synchronize an MFA device**

The following `resync-mfa-device` example synchronizes the MFA device that is associated with the IAM user `Bob` and whose ARN is `arn:aws:iam::123456789012:mfa/BobsMFADevice` with an authenticator program that provided the two authentication codes.

```
`aws iam resync-mfa-device \
 --user-name `Bob` \
 --serial-number `arn:aws:iam::210987654321:mfa/BobsMFADevice` \
 --authentication-code1 `123456` \
 --authentication-code2 `987654``

```

This command produces no output.

For more information, see [Using multi-factor authentication (MFA) in AWS](id_credentials_mfa.md "id_credentials_mfa.md") in the _AWS IAM User Guide_.

- For API details, see
  [ResyncMfaDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/resync-mfa-device.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/resync-mfa-device.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example synchronizes the MFA device that is associated with the IAM user `Bob` and whose ARN is `arn:aws:iam::123456789012:mfa/bob` with an authenticator program that provided the two authentication codes.**

```
Sync-IAMMFADevice -SerialNumber arn:aws:iam::123456789012:mfa/theresa -AuthenticationCode1 123456 -AuthenticationCode2 987654 -UserName Bob

```

**Example 2: This example synchronizes the IAM MFA device that is associated with the IAM user `Theresa` with a physical device that has the serial number `ABCD12345678` and that provided the two authentication codes.**

```
Sync-IAMMFADevice -SerialNumber ABCD12345678 -AuthenticationCode1 123456 -AuthenticationCode2 987654 -UserName Theresa

```

- For API details, see
  [ResyncMfaDevice](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example synchronizes the MFA device that is associated with the IAM user `Bob` and whose ARN is `arn:aws:iam::123456789012:mfa/bob` with an authenticator program that provided the two authentication codes.**

```
Sync-IAMMFADevice -SerialNumber arn:aws:iam::123456789012:mfa/theresa -AuthenticationCode1 123456 -AuthenticationCode2 987654 -UserName Bob

```

**Example 2: This example synchronizes the IAM MFA device that is associated with the IAM user `Theresa` with a physical device that has the serial number `ABCD12345678` and that provided the two authentication codes.**

```
Sync-IAMMFADevice -SerialNumber ABCD12345678 -AuthenticationCode1 123456 -AuthenticationCode2 987654 -UserName Theresa

```

- For API details, see
  [ResyncMfaDevice](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
