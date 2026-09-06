

# Remove a cluster with multi-slot functionality for AWS CloudHSM
<a name="pkcs11-multi-slot-remove-cluster"></a>

When [connecting to multiple slots with PKCS\#11](pkcs11-library-configs-multi-slot.md), use the **configure-pkcs11 remove-cluster** command to remove a cluster from available PKCS \#11 slots.

## Syntax
<a name="pkcs11-multi-slot-remove-cluster-syntax"></a>

```
configure-pkcs11 remove-cluster{{ [OPTIONS]}}
        --cluster-id {{<CLUSTER ID>}}
        [-h, --help]
```

## Examples
<a name="pkcs11-multi-slot-remove-cluster-examples"></a>

### Remove a cluster using the `cluster-id` parameter
<a name="w2aac25c21c17c31b7c15b7b3b1"></a>

**Example**  
 Use the **configure-pkcs11 remove-cluster** along with the `cluster-id` parameter to remove a cluster (with the ID of `cluster-1234567`) from your configuration.   

```
$ sudo /opt/cloudhsm/bin/configure-pkcs11 remove-cluster --cluster-id {{<cluster-1234567>}}
```

```
PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" remove-cluster --cluster-id {{<cluster-1234567>}}
```

For more information about the `--cluster-id` parameter, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md).

## Parameter
<a name="pkcs11-multi-slot-remove-cluster-parameters"></a>

**--cluster-id {{<Cluster ID>}}**  
 The ID of the cluster to remove from the configuration  
Required: Yes