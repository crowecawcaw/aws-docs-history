

# Interact with multiple clusters in AWS CloudHSM
<a name="cloudhsm_cli-multi-cluster-usage"></a>

After configuring multiple clusters with CloudHSM CLI, use the `cloudhsm-cli` command to interact with them.

## Examples
<a name="cloudhsm_cli-multi-cluster-cluster-usage-examples"></a>

### Setting a default `cluster-id` when using interactive mode
<a name="w2aac23c15c19b7c17b5b3b1"></a>

**Example**  
 Use the [Interactive mode](cloudhsm_cli-modes.md#cloudhsm_cli-mode-interactive) along with the `cluster-id` parameter to set a default cluster (with the ID of `cluster-1234567`) from your configuration.   

```
$ cloudhsm-cli interactive --cluster-id {{<cluster-1234567>}}
```

```
PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive --cluster-id {{<cluster-1234567>}}
```

### Setting the `cluster-id` when running a single command
<a name="w2aac23c15c19b7c17b5b5b1"></a>

**Example**  
 Use the `cluster-id` parameter to set the cluster (with the ID of `cluster-1234567`) to get [List HSMs with CloudHSM CLI](cloudhsm_cli-cluster-hsm-info.md) from.   

```
$ cloudhsm-cli cluster hsm-info --cluster-id {{<cluster-1234567>}}
```

```
PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" cluster hsm-info --cluster-id {{<cluster-1234567>}}
```