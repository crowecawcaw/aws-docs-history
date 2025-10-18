# Remove a cluster from your AWS CloudHSM configuration

When connecting to multiple clusters with CloudHSM CLI,
 use the `configure-cli remove-cluster` command to remove a cluster from your configuration.


## Syntax



```
`configure-cli remove-cluster `[OPTIONS]`
 --cluster-id `<CLUSTER ID>`
 [-h, --help]`
```

## Examples



 Use the `configure-cli remove-cluster` along with the `cluster-id` parameter to remove a cluster (with the ID of `cluster-1234567`) from your configuration.
 


Linux

```
`$` `sudo /opt/cloudhsm/bin/configure-cli remove-cluster --cluster-id `<cluster-1234567>``
```


Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-cli.exe" remove-cluster --cluster-id `<cluster-1234567>``
```



For more information about the `--cluster-id` parameter, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md "configure-tool-params5.md").


## Parameter




**--cluster-id `<Cluster ID>`**

The ID of the cluster to remove from the configuration.


Required: Yes
