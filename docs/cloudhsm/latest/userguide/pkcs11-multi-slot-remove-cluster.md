# Remove a cluster with multi-slot

functionality for AWS CloudHSM

When [connecting to multiple slots with PKCS#11](pkcs11-library-configs-multi-slot.md "pkcs11-library-configs-multi-slot.md"),
use the **configure-pkcs11 remove-cluster** command to remove a cluster from available PKCS #11 slots.

## Syntax

```
`configure-pkcs11 remove-cluster `[OPTIONS]`
 --cluster-id `<CLUSTER ID>`
 [-h, --help]`
```

## Examples

###### Example

Use the **configure-pkcs11 remove-cluster** along with the `cluster-id` parameter to remove a cluster (with the ID of `cluster-1234567`) from your configuration.

Linux

```

`$` `sudo /opt/cloudhsm/bin/configure-pkcs11 remove-cluster --cluster-id `<cluster-1234567>``

```

Windows

```

`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" remove-cluster --cluster-id `<cluster-1234567>``

```

For more information about the `--cluster-id` parameter, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md "configure-tool-params5.md").

## Parameter

**--cluster-id `<Cluster ID>`**

The ID of the cluster to remove from the configuration

Required: Yes
