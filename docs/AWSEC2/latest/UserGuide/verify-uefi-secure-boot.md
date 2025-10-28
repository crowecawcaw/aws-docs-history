# Verify whether an Amazon EC2 instance is enabled for

UEFI Secure Boot

You can use the following procedures to determine whether an Amazon EC2 is enabled for
UEFI Secure Boot.

You can use the `mokutil` utility to verify whether a Linux instance
is enabled for UEFI Secure Boot. If `mokutil` is not installed on your
instance, you must install it. For the installation instructions for Amazon Linux 2,
see [Find and install software packages on an Amazon Linux 2 instance](../../../linux/al2/ug/find-install-software.md "../../../linux/al2/ug/find-install-software.md").
For other Linux distributions, see their specific documentation.

###### To verify whether a Linux instance is enabled for UEFI Secure Boot

Connect to your instance and run the following command as `root`
in a terminal window.

```
mokutil --sb-state
```

The following is example output.

- If UEFI Secure Boot is enabled, the output contains `SecureBoot
enabled`.
- If UEFI Secure Boot is not enabled, the output contains `SecureBoot disabled`
  or `Failed to read SecureBoot`.

###### To verify whether a Windows instance is enabled for UEFI Secure Boot

1. Connect to your instance.
2. Open the msinfo32 tool.
3. Check the **Secure Boot State** field.
   If UEFI Secure Boot is enabled, the value is **Supported**,
   as shown in the following image.

![Secure Boot State within System Information.](images/secure-boot-state-win.png)
You can also use the Windows PowerShell Cmdlet
`Confirm-SecureBootUEFI` to check the Secure Boot status. For more
information about the cmdlet, see
[Confirm-SecureBootUEFI](https://learn.microsoft.com/en-us/powershell/module/secureboot/confirm-securebootuefi "https://learn.microsoft.com/en-us/powershell/module/secureboot/confirm-securebootuefi") in the Microsoft Documentation.
