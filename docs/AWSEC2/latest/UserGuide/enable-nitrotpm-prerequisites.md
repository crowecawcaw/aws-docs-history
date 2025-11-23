# Requirements for using NitroTPM with Amazon EC2

instances

To launch an instance with NitroTPM enabled, you must meet the following requirements.

###### Topics

- [AMIs](#nitrotpm-ami "#nitrotpm-ami")
- [Instance types](#nitrotpm-instancetypes "#nitrotpm-instancetypes")
- [Considerations](#nitrotpm-considerations "#nitrotpm-considerations")

## AMIs

The AMI must have NitroTPM enabled.

###### Linux AMIs

There are no preconfigured AMIs. You must configure your own AMI.
For more information, see [Enable a Linux AMI for NitroTPM](enable-nitrotpm-support-on-ami.md "enable-nitrotpm-support-on-ami.md").

###### Windows AMIs

To find an AWS Windows AMI that's preconfigured for NitroTPM and UEFI Secure
Boot with Microsoft keys, see [Find
Windows Server AMIs configured with NitroTPM and UEFI Secure Boot](../../../ec2/latest/windows-ami-reference/ami-windows-tpm.md#ami-windows-tpm-find "../../../ec2/latest/windows-ami-reference/ami-windows-tpm.md#ami-windows-tpm-find") in the
_AWS Windows AMIs Reference_.

###### Note

**Operating system** — The AMI must include
an operating system with a TPM 2.0 Command Response Buffer (CRB) driver. Most current
operating systems include a TPM 2.0 CRB driver.

**UEFI boot mode** — The AMI must be configured
for UEFI boot mode. For more information, see [UEFI Secure Boot for Amazon EC2 instances](uefi-secure-boot.md "uefi-secure-boot.md").

## Instance types

You must use one of the following virtualized instance types:

- **General purpose**: M5, M5a, M5ad, M5d, M5dn, M5n, M5zn, M6a, M6g, M6gd, M6i, M6id, M6idn, M6in, M7a, M7g, M7gd, M7i, M7i-flex, M8a, M8g, M8gd, M8i, M8i-flex, T3, T3a, T4g
- **Compute optimized**:
  C5, C5a, C5ad, C5d, C5n, C6a, C6g, C6gd, C6gn, C6i, C6id, C6in, C7a, C7g, C7gd, C7gn, C7i, C7i-flex, C8g, C8gd, C8gn, C8i, C8i-flex
- **Memory optimized**: R5, R5a, R5ad, R5b, R5d, R5dn, R5n, R6a, R6g, R6gd, R6i, R6id, R6idn, R6in, R7a, R7g, R7gd, R7i, R7iz, R8a, R8g, R8gb, R8gd, R8gn, R8i, R8i-flex, U7i-6tb, U7i-8tb, U7i-12tb, U7in-16tb, U7in-24tb, U7in-32tb, X2idn, X2iedn, X2iezn, X8g, z1d
- **Storage optimized**:
  D3, D3en, I3en, I4i, I7i, I7ie, I8g, I8ge, Im4gn
- **Accelerated computing**:
  F2, G4dn, G5, G6, G6e, G6f, Gr6, Gr6f, Inf1, Inf2, P5, P5e, P5en, P6-B200, P6-B300, Trn2, Trn2u
- **High-performance computing**:
  Hpc6a, Hpc6id

## Considerations

The following considerations apply when using NitroTPM:

- After you launch an instance using an AMI with NitroTPM enabled, if you want
  to change the instance type, the new instance type that you choose must also
  support NitroTPM.
- BitLocker volumes that are encrypted with NitroTPM-based keys can only be used on the
  original instance.
- The NitroTPM state is not displayed in the Amazon EC2 console.
- The NitroTPM state is not included in [Amazon EBS snapshots](../../../ebs/latest/userguide/ebs-snapshots.md "../../../ebs/latest/userguide/ebs-snapshots.md").
- The NitroTPM state is not included in [VM Import/Export](../../../vm-import/latest/userguide.md "../../../vm-import/latest/userguide.md") images.
- NitroTPM is not supported on AWS Outposts., Local Zones, or Wavelength Zones.
