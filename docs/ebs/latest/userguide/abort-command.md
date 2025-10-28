# NVMe Abort command for Amazon EBS volumes

The `Abort` command is an NVMe admin command that is issued to end a specific
command that was previously submitted to the controller. This command is typically issued
by the device driver to storage devices that have exceeded the I/O operation timeout
threshold.

Amazon EC2 instance types that support the `Abort` command by default will end a
specific command that was previously submitted to the controller when an `Abort`
command is issued to attached Amazon EBS volumes. Amazon EC2 instances that do not support the
`Abort` command take no action when an `Abort` command is issued
to attached Amazon EBS volumes.

The `Abort` command is supported with:

- Amazon EBS devices with NVMe device version 1.4 or higher.
- All Amazon EC2 instances, **except** Xen-based instances
  types and the following Nitro-based instance types:

      + General purpose: A1 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6g |
       M6gd | Mac1 | Mac2 | T3 | T3a | T4g
      + Compute optimized: C5 | c5a | C5ad | C5d | C5n | C6g | C6gd
      + Memory optimized: R5 | R5a | R5ad | R5d | R5dn | R5n | R6g | R6gd | U-12tb1 |
       U-18tb1 | U-24tb1 | U-3tb1 | U-6tb1 | U-9tb1 | X2gd | X2iezn | Z1d
      + Storage optimized: D3 | D3en | I3en
      + Accelerated computing: DL1 | G4ad | G4dn | G5 | G5g | Inf1 | P3dn | P4d |
       P4de | VT1

  For more information, see section **5.1 Abort command**
  of the [NVM Express Base Specification](https://nvmexpress.org/wp-content/uploads/NVM-Express-1_4-2019.06.10-Ratified.pdf "https://nvmexpress.org/wp-content/uploads/NVM-Express-1_4-2019.06.10-Ratified.pdf").
