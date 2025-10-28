# Requirements for UEFI Secure Boot on Amazon EC2

When you [launch an Amazon EC2 instance](LaunchingAndUsingInstances.md "LaunchingAndUsingInstances.md")
with a supported AMI and a supported instance type, that instance will
automatically validate UEFI boot binaries against its UEFI Secure Boot database. No
additional configuration is required. You can also configure UEFI Secure Boot on an
instance after launch.

###### Note

UEFI Secure Boot protects your instance and its operating system against boot
flow modifications. If you create a new AMI from a source AMI that has UEFI Secure
Boot enabled and modify certain parameters during the copy process, such as
changing the `UefiData` within the AMI, you can disable UEFI Secure
Boot.

###### Contents

- [Supported AMIs](#uefi-amis "#uefi-amis")
- [Supported instance types](#uefi-instance "#uefi-instance")

## Supported AMIs

###### Linux AMIs

To launch a Linux instance, the Linux AMI must have UEFI Secure Boot enabled.

Amazon Linux supports UEFI Secure Boot starting with AL2023 release 2023.1. However, UEFI
Secure Boot isn't enabled in the default AMIs. For more information,
see [UEFI Secure Boot](../../../linux/al2023/ug/uefi-secure-boot.md "../../../linux/al2023/ug/uefi-secure-boot.md")
in the _AL2023 User Guide_. Older versions of Amazon Linux
AMIs aren't enabled for UEFI Secure Boot. To use a supported AMI, you
must perform a number of configuration steps on your own Linux AMI. For
more information, see [Create a Linux AMI with custom UEFI Secure
Boot keys](create-ami-with-uefi-secure-boot.md "create-ami-with-uefi-secure-boot.md").

###### Windows AMIs

To launch a Windows instance, the Windows AMI must have UEFI Secure
Boot enabled. To find an AWS Windows AMI that's preconfigured for UEFI Secure Boot with
Microsoft keys, see [Find
Windows Server AMIs configured with NitroTPM and UEFI Secure Boot](../../../ec2/latest/windows-ami-reference/ami-windows-tpm.md#ami-windows-tpm-find "../../../ec2/latest/windows-ami-reference/ami-windows-tpm.md#ami-windows-tpm-find") in the
_AWS Windows AMIs Reference_.

Currently, we do not support importing Windows with UEFI Secure Boot by using the
[import-image](../../../cli/latest/reference/ec2/import-image.md "../../../cli/latest/reference/ec2/import-image.md") command.

## Supported instance types

All virtualized instance types that support UEFI also support UEFI
Secure Boot. For the instance types that support UEFI Secure Boot, see
[Requirements for UEFI boot mode](launch-instance-boot-mode.md "launch-instance-boot-mode.md").

###### Note

Bare metal instance types do not support UEFI Secure Boot.
