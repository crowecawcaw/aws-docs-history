# Requirements to launch an EC2 instance in UEFI boot mode

The boot mode of an instance is determined by the configuration of the AMI, the operating system
contained in it, and the instance type. To launch an instance in UEFI boot mode, you must meet
the following requirements.

**AMI**

The AMI must be configured for UEFI as follows:

- **Operating system** – The operating system
  contained in the AMI must be configured to use UEFI; otherwise,
  the instance launch will fail. For more information, see [Determine the boot mode of the operating system for your EC2 instance](os-boot-mode.md "os-boot-mode.md").
- **AMI boot mode parameter** – The boot mode
  parameter of the AMI must be set to `uefi` or
  `uefi-preferred`. For more information, see [Determine the boot mode parameter of an Amazon EC2 AMI](ami-boot-mode.md "ami-boot-mode.md").

**Linux** – The following Linux AMIs support
UEFI:

- Amazon Linux 2023
- Amazon Linux 2 (Graviton instance types only)

For other Linux AMIs, you must [configure the AMI](set-ami-boot-mode.md "set-ami-boot-mode.md"), import the AMI through [VM Import/Export](../../../vm-import/latest/userguide.md "../../../vm-import/latest/userguide.md"), or
import the AMI through [CloudEndure](https://docs.cloudendure.com/ "https://docs.cloudendure.com/").

**Windows** – The following Windows AMIs support
UEFI:

- Windows_Server-2025-\* (except for AMIs with the
  `BIOS-` name prefix)
- TPM-Windows_Server-2022-English-Full-Base
- TPM-Windows_Server-2022-English-Core-Base
- TPM-Windows_Server-2019-English-Full-Base
- TPM-Windows_Server-2019-English-Core-Base
- TPM-Windows_Server-2016-English-Full-Base
- TPM-Windows_Server-2016-English-Core-Base

**Instance type**

All instances built on the AWS Nitro System support both UEFI and Legacy BIOS,
except the following: bare metal instances, DL1, G4ad, P4, u-3tb1, u-6tb1, u-9tb1,
u-12tb1, u-18tb1, u-24tb1, and VT1. For more information, see [Determine the supported boot modes of an EC2 instance type](instance-type-boot-mode.md "instance-type-boot-mode.md").

The following table shows that the boot mode of an instance (indicated by the **Resulting instance boot mode** column) is
determined by a combination of the boot mode parameter of the AMI (column 1), the
boot mode configuration of the operating system contained in the AMI (column 2), and
the boot mode support of the instance type (column 3).

| AMI boot mode parameter         | Operating system boot mode configuration | Instance type boot mode support | Resulting instance boot mode |
| ------------------------------- | ---------------------------------------- | ------------------------------- | ---------------------------- |
| UEFI                            | UEFI                                     | UEFI                            | UEFI                         |
| Legacy BIOS                     | Legacy BIOS                              | Legacy BIOS                     | Legacy BIOS                  |
| UEFI Preferred                  | UEFI                                     | UEFI                            | UEFI                         |
| UEFI Preferred                  | UEFI                                     | UEFI and Legacy BIOS            | UEFI                         |
| UEFI Preferred                  | Legacy BIOS                              | Legacy BIOS                     | Legacy BIOS                  |
| UEFI Preferred                  | Legacy BIOS                              | UEFI and Legacy BIOS            | Legacy BIOS                  |
| No boot mode specified<br>• ARM | UEFI                                     | UEFI                            | UEFI                         |
| No boot mode specified<br>• x86 | Legacy BIOS                              | UEFI and Legacy BIOS            | Legacy BIOS                  |
