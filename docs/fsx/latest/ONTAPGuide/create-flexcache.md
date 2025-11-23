# Creating a FlexCache

Using the following procedures, you will create a FlexCache volume on an Amazon FSx for NetApp ONTAP file system,
that is backed by an origin volume located in an on-premises NetApp ONTAP cluster.

## Using the ONTAP CLI

You will use the ONTAP CLI to create and manage a FlexCache configuration on your
FSx for ONTAP file system.

The commands in these procedures use the following aliases for the cluster, SVM, and volume :

- `Cache_ID` – the cache cluster's ID (in the format FSxIdabcdef1234567890a)
- `Origin_ID` – the origin cluster's ID
- `CacheSVM` – the cache SVM name
- `OriginSVM` – the origin SVM name
- `OriginVol` – the origin volume name
- `CacheVol` – the FlexCache volume name

The procedures in this section use the following NetApp ONTAP CLI commands.

- [`network interfaces show`](https://docs.netapp.com/us-en/ontap-cli-9141/network-interface-show.html "https://docs.netapp.com/us-en/ontap-cli-9141/network-interface-show.html")
- [`cluster peer`](https://docs.netapp.com/us-en/ontap-cli-9141/cluster-peer-create.html "https://docs.netapp.com/us-en/ontap-cli-9141/cluster-peer-create.html") commands
- [`volume flexcache create`](https://docs.netapp.com/us-en/ontap-cli-9141/volume-flexcache-create.html "https://docs.netapp.com/us-en/ontap-cli-9141/volume-flexcache-create.html")

## Prerequisites

Before you begin using the procedures in the following sections, be sure that you have met the following prerequisites:

- The source and destination file systems are connected in the same VPC, or are in networks that are peered using
  Amazon VPC, AWS Transit Gateway, Direct Connect, or Site-to-Site VPN. For more information, see [Accessing data from within the AWS Cloud](supported-fsx-clients.md#access-environments "supported-fsx-clients.md#access-environments")
  and [What is VPC peering?](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") in the Amazon VPC Peering Guide.
- The VPC security group for the FSx for ONTAP file system has inbound and outbound rules allowing ICMP as well as TCP on ports
  11104 and 11105 for your inter-cluster endpoints (LIFs).
- You have created a destination FSx for ONTAP file system with an SVM, but you have not created the volume that will be used as a FlexCache.
  For more information, see [Creating file systems](creating-file-systems.md "creating-file-systems.md").

## Record the source and destination inter-cluster LIFs

1. For the FSx for ONTAP file system that is the destination cluster:
   1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
   2. Choose **File systems**, then choose the FSx for ONTAP file system that is the destination cluster to open
      the file system details page.
   3. In **Administration**, find the **Inter-cluster endpoint - IP addresses**, and record the
      value.###### Note

For scale-out file systems, there are two inter-cluster endpoint IP addresses for each high-availability (HA) pair. 2. For the on-premises source cluster, retrieve the inter-cluster LIF IP addresses using the following ONTAP CLI command:

```
`Origin::>` `network interface show -role intercluster`
`Logical Network
Vserver Interface Status Address/Mask
----------- ---------- ------- ------------
OriginSVM
 inter_1 up/up 10.0.0.36/24
 inter_2 up/up 10.0.1.69/24`
```

3. Save the `inter_1` and `inter_2 IP` addresses. They are referenced in the
   `OriginSVM` alias as `origin_inter_1` and `origin_inter_2` and the
   `CacheSVM` alias as `cache_inter_1` and `cache_inter_2`.

## Establish cluster peering between the origin and cache

Establish a cluster peer relationship on the **Cache** and **Source** cluster using the
[**cluster peer create**](https://docs.netapp.com/us-en/ontap-cli-9141/cluster-peer-create.html "https://docs.netapp.com/us-en/ontap-cli-9141/cluster-peer-create.html") ONTAP
CLI command. You will provide the inter-cluster IP addresses that you saved previously in the [Record the source and destination inter-cluster LIFs](#record-lifs "#record-lifs") procedure.
When prompted, you will be asked to create a `cluster-peer-passphrase` that you will need to enter in when you establish
cluster peering on the **Origin** cluster.

1. Set up cluster peering on the `Cache` cluster (your FSx for ONTAP file system).
   1. To access the ONTAP CLI, establish an SSH session on the management port of the
      Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
      `management_endpoint_ip` with the IP address of the file system's
      management port.

   ```
   `[~]$` `ssh fsxadmin@`management_endpoint_ip``
   ```

   For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Use the following command, and record the password that you create. For scale-out file systems, provide the `inter_1` and `inter_2` IP addresses for each HA pair.

   ```
   `FSx-Cache::>` `cluster peer create -address-family ipv4 -peer-addrs `origin_inter_1`,`origin_inter_2``
    `Enter the passphrase: ``cluster-peer-passphrase``
   Confirm the passphrase: ``cluster-peer-passphrase``
   Notice: Now use the same passphrase in the "cluster peer create" command in the other cluster.`
   ```

2. Use the following command to set up cluster peering on the `source` (on-premises) cluster. You’ll need to enter
   the passphrase you created in the previous step to authenticate. For scale-out file systems, you'll need to provide the inter-cluster IP address for each HA pair.

```
`Origin::>` `cluster peer create -address-family ipv4 -peer-addrs `cache_inter_1`,`cache_inter_2``
 `Enter the passphrase:` ``cluster-peer-passphrase``
`Confirm the passphrase:` ``cluster-peer-passphrase``
```

3. On the `source` cluster, verify that cluster peering was set up successfully using the following command. In the output,
   `Availability` should be set to `Available`.

```
`Origin::>` `cluster peer show`
 `Peer Cluster Name Availability Authentication
------------------- ------------- --------------
Cache_ID Available ok`
```

If the output does not show `Available`, repeat the previous steps on the `source` and `cache` clusters.

## Configure storage virtual machine (SVM) peering

After you have established cluster peering successfully, the next step is to create an SVM peering relationship on
the cache cluster (Cache) using the **vserver peer** command. Additional aliases used in the following procedure are as follows:

- `CacheLocalName` – the name used to identify the `cache` SVM when configuring SVM peering on the `origin` SVM.
- `OriginLocalName` – the name used to identify the `origin` SVM when configuring SVM peering on the `cache` SVM.

1. On the `cache` SVM, use the following command to create an SVM peering relationship.

```
`FSx-Cache::>` `vserver peer create -vserver `CacheSVM` -peer-vserver `OriginSVM` -peer-cluster `Origin_ID` -local-name `OriginLocalName` -application flexcache`
```

2. On the source cluster, use the following command to accept the SVM peering relationship.

```
`Origin::>` `vserver peer accept -vserver `OriginSVM` -peer-vserver `CacheSVM` -local-name `CacheLocalName``

```

3. On the source cluster, accept the peering relationship.

```
`Origin::>` `vserver peer accept -vserver `OriginSVM` -peer-vserver `CacheSVM` -local-name `CacheLocalName``

```

4. Verify that the SVM peering was successful using the following command; `Peer State` should be set to `peered` in the response.

```
`Origin::>` `vserver peer show`
 `Vserver Peer Vserver Peer State Peering Cluster Remote Applications
------------ --------------- ------------- ------------------ -----------------------
OriginSVM CacheSVM peered FSx-Cache flexcache`
```

## Create the FlexCache volume

After successfully creating the SVM peering relationship, the next step is to create the FlexCache volume on the cache SVM.
The FlexCache volume must be a FlexGroup. You will also choose a mode of operation for your FlexCache volume.
For more information, see [FlexCache write modes](using-flexcache.md#flexcache_write-around-write-back "using-flexcache.md#flexcache_write-around-write-back").

1. On the cache cluster, use the following ONTAP CLI command to create your FlexCache volume. The example creates a 2 TB FlexCache volume
   named `CacheVol`.
   - To create a write-around FlexCache volume, use the following command.

   ```
   `FSx-Cache::>` `volume flexcache create -vserver `CacheSVM` -size 2t -volume `CacheVol` -origin-volume `OriginVol` -origin-vserver `OriginSVM` -junction-path `/flexcache` -aggr-list `aggr1``

   ```

   - To create a write-back FlexCache volume, use the following command.

   ```
   `FSx-Cache::>` `volume flexcache create -vserver `CacheSVM` -size 2t -volume `CacheVol` -origin-volume `OriginVol` -origin-vserver `OriginSVM` -junction-path `/flexcache` -aggr-list `aggr1` -is-writeback-enabled true`

   ```

###### Note

You can use the [`volume flexcache config modify -is-writeback-enabled {true|false}`](https://docs.netapp.com/us-en/ontap-cli-9151/volume-flexcache-config-modify.html#description "https://docs.netapp.com/us-en/ontap-cli-9151/volume-flexcache-config-modify.html#description")
command to modify the write mode. Before using this command, make sure you enter ONTAP CLI advanced mode by using the
[`set -privilege advanced`](https://docs.netapp.com/us-en/ontap/system-admin/set-privilege-level-task.html "https://docs.netapp.com/us-en/ontap/system-admin/set-privilege-level-task.html") command. 2. Verify the FlexCache relationship between the FlexCache volume and the origin volume.

    * For a FlexCache write-around volume, your output will look similar to the following example.



    ```
    `FSx-Cache::>` `volume flexcache show`
     `Vserver Volume Size Origin-Vserver Origin-Volume Origin-Cluster
    ------- ---------- ------- -------------- ------------- --------------
    CacheSVM CacheVol 2TB OriginSVM OriginVol Origin`
    ```
    * For a FlexCache write-back volume, your output will look similar to the following example.



    ```
    `FSx-Cache::>` `volume flexcache show`
     `Vserver Volume Size Origin-Vserver Origin-Volume Origin-Cluster Writeback
    ------- ---------- ------- -------------- ------------- -------------- ---------
    CacheSVM CacheVol 2TB OriginSVM OriginVol Origin true`
    ```

## Mount the FlexCache volume

Once the FlexCache volume becomes AVAILABLE, NFSv3, NFSv4, and SMB clients can mount it. Once the FlexCache is mounted, clients have access to the
entire dataset on the on-premise origin volume.

- To create a mount point and mount the FlexCache, run the following commands on the client:

```
`$` `sudo mkdir -p /fsx/CacheVol`
`$` `sudo mount -t nfs management.fs-01d2f606463087f6d.fsx.us-east-1.amazonaws.com:/CacheVol /fsx/CacheVol`
```
