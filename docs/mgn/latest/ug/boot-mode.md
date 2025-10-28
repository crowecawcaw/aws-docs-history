NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Boot mode

Choose the boot mode for the test or cutover instance.

You can either choose the **Legacy BIOS**, **UEFI** or **Use source boot mode**. By
default, the boot mode is set to **Use source boot mode**. When
this option is selected, MGN launches the test or cutover instance using the same boot mode
as the source server.

**Note**: When the BIOS option is chosen, Application Migration Service converts
any non-BIOS instance type to BIOS. As such, the server is limited to four partitions
that cannot equal more than 2TiB due to BIOS limitations.

###### Note

You must choose the **UEFI** boot mode for any BYOL source
server that is UEFI, as Application Migration Service is unable to convert BYOL source servers that boot in UEFI to
BIOS.

###### Note

UEFI boot is only available for Nitro instances.

All Nitro based instance types can also run on UEFI instead of Legacy BIOS.

UEFI is not supported in CentOS 6 and Rhel 6.

Refer to [this page for a list of supported instance types](../../../AWSEC2/latest/UserGuide/ami-boot.md "../../../AWSEC2/latest/UserGuide/ami-boot.md").
