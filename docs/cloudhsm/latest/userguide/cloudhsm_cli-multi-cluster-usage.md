# Interact with multiple clusters in AWS CloudHSM

After configuring multiple clusters with CloudHSM CLI,
use the `cloudhsm-cli` command to interact with them.

## Examples

###### Example

Use the [Interactive mode](cloudhsm_cli-modes.md#cloudhsm_cli-mode-interactive "cloudhsm_cli-modes.md#cloudhsm_cli-mode-interactive") along with the `cluster-id` parameter to set a default cluster (with the ID of `cluster-1234567`) from your configuration.

Linux

```
`$` `cloudhsm-cli interactive --cluster-id `<cluster-1234567>``
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive --cluster-id `<cluster-1234567>``
```

###### Example

Use the `cluster-id` parameter to set the cluster (with the ID of `cluster-1234567`) to get [List HSMs with CloudHSM CLI](cloudhsm_cli-cluster-hsm-info.md "cloudhsm_cli-cluster-hsm-info.md") from.

Linux

```
`$` `cloudhsm-cli cluster hsm-info --cluster-id `<cluster-1234567>``
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" cluster hsm-info --cluster-id `<cluster-1234567>``
```
