# Use `ListMfaDevices` with a CLI

The following code examples show how to use `ListMfaDevices`.

CLI

**AWS CLI**

**To list all MFA devices for a specified user**

This example returns details about the MFA device assigned to the IAM user `Bob`.

```
`aws iam list-mfa-devices \
 --user-name `Bob``

```

Output:

```
{
    "MFADevices": [
        {
            "UserName": "Bob",
            "SerialNumber": "arn:aws:iam::123456789012:mfa/Bob",
            "EnableDate": "2019-10-28T20:37:09+00:00"
        },
        {
            "UserName": "Bob",
            "SerialNumber": "GAKT12345678",
            "EnableDate": "2023-02-18T21:44:42+00:00"
        },
        {
            "UserName": "Bob",
            "SerialNumber": "arn:aws:iam::123456789012:u2f/user/Bob/fidosecuritykey1-7XNL7NFNLZ123456789EXAMPLE",
            "EnableDate": "2023-09-19T02:25:35+00:00"
        },
        {
            "UserName": "Bob",
            "SerialNumber": "arn:aws:iam::123456789012:u2f/user/Bob/fidosecuritykey2-VDRQTDBBN5123456789EXAMPLE",
            "EnableDate": "2023-09-19T01:49:18+00:00"
        }
    ]
}
```

For more information, see [Using multi-factor authentication (MFA) in AWS](id_credentials_mfa.md "id_credentials_mfa.md") in the _AWS IAM User Guide_.

- For API details, see
  [ListMfaDevices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-mfa-devices.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-mfa-devices.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns details about the MFA device assigned to the IAM user `David`. In this example you can tell that it is a virtual device because the `SerialNumber` is an ARN instead of a physical device's actual serial number.**

```
Get-IAMMFADevice -UserName David

```

**Output:**

```
EnableDate                  SerialNumber                           UserName
----------                  ------------                           --------
4/8/2015 9:41:10 AM         arn:aws:iam::123456789012:mfa/David    David
```

- For API details, see
  [ListMfaDevices](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns details about the MFA device assigned to the IAM user `David`. In this example you can tell that it is a virtual device because the `SerialNumber` is an ARN instead of a physical device's actual serial number.**

```
Get-IAMMFADevice -UserName David

```

**Output:**

```
EnableDate                  SerialNumber                           UserName
----------                  ------------                           --------
4/8/2015 9:41:10 AM         arn:aws:iam::123456789012:mfa/David    David
```

- For API details, see
  [ListMfaDevices](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
