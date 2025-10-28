# Managing the NVMe cache

The NVMe cache is enabled by default on your second-generation file system. If your second-generation file system has a throughput-heavy workload, you can disable the NVMe cache to
improve performance. The following procedure explains how to enable, disable, and validate your file system's NVMe cache.

###### To manage the NVMe cache

1. SSH into your ONTAP file system. For more information, see [Using the NetApp ONTAP CLI](managing-resources-ontap-apps.md#netapp-ontap-cli "managing-resources-ontap-apps.md#netapp-ontap-cli").

```
ssh fsxadmin@file-system-management-endpoint-ip-`address`
```

2. Use the [**system node external-cache modify**](https://docs.netapp.com/us-en/ontap-cli-9131/system-node-external-cache-modify.html "https://docs.netapp.com/us-en/ontap-cli-9131/system-node-external-cache-modify.html") ONTAP CLI commnd. Choose `true` to enable the NVMe cache or `false` to disable it.

```
::> system node external-cache modify -node * -is-enabled [`true`|`false`]
```

3. Use the [**system node external-cache show**](https://docs.netapp.com/us-en/ontap-cli-9131/system-node-external-cache-show.html "https://docs.netapp.com/us-en/ontap-cli-9131/system-node-external-cache-show.html")
   ONTAP CLI command to check if the NVMe cache is enabled or disabled.

```
::> system node external-cache show -node * -fields is-enabled
```

The NVMe cache is enabled or disabled on a per-node basis. When you add new high-availability (HA) pairs to your file system, each new node has the same default behavior of a new file system's nodes.
Therefore, the NVMe cache would be enabled for any new nodes on a file system even if the existing nodes have it disabled. For more information, see [Adding high-availability (HA) pairs](adding-HA-pairs.md "adding-HA-pairs.md").
