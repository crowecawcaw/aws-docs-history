NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Boot mode

Boot mode is automatically discovered from the source server. The target instance
will launch using the same boot mode as the source. Changing this setting may cause the
target instance to fail to boot.

UEFI limitations:

- UEFI boot is only available for Nitro instances.
- You must choose UEFI for any BYOL source server that is UEFI.
- UEFI is not supported on CentOS 6 and RHEL 6.
