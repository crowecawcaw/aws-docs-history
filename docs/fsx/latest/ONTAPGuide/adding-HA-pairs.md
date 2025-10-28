# Adding high-availability (HA) pairs

FSx for ONTAP file systems are composed of one or more HA pairs of file servers. First-generation file systems and second-generation Multi-AZ file systems
support one HA pair whereas second-generation Single-AZ file systems support up to 12 HA pairs. You can also add more HA pairs after creating a second-generation Single-AZ file system
(up to the maximum of 12). Adding HA pairs isn't disruptive and typically takes only a few minutes to complete.

Consider the following points when adding HA pairs to your file system:

- Adding HA pairs to your file system introduces new file servers with their own storage (or aggregate). The new HA pairs have the same throughput capacity and storage
  capacity as your file system's existing HA pairs. For example, assume that your file system has two HA pairs with a total of 12 GBps of throughput capacity and 2 tebibytes (TiB)
  of SSD storage. If you add one new HA pair, then your file system will have 18 GBps of throughput capacity and 3 TiB of SSD storage.
- To benefit from the additional performance of the new HA pairs, you need to move some of your existing volumes to the new HA pairs and remount clients to connect to them.
  For more information, see [Balancing workloads across HA pairs](monitor-workload-balance.md "monitor-workload-balance.md").
- You can't modify your file system's throughput capacity, SSD storage capacity, or provisioned SSD IOPS when adding HA pairs or while an update to add HA pairs is in progress.
- You can't remove HA pairs after you add them. We recommend scaling the throughput capacity of your file system if you need more performance temporarily (assuming that your file system
  isn't at the highest throughput capacity). This increases the throughput capacity of your file system's existing HA pairs.
- The iSCSI protocol is available on file systems that have six or fewer high-availability pairs (HA pairs). The NVMe/TCP protocol is available on second-generation file systems that have six or fewer HA pairs.
  For more information, see [Accessing your FSx for ONTAP data](supported-fsx-clients.md "supported-fsx-clients.md").
- When you add new HA pairs to your file system, the NVMe cache is enabled by default for the new file system nodes. We recommend disabling it for throughput-heavy workloads.
  For more information, see [Managing the NVMe cache](nvme-cache.md "nvme-cache.md").

###### To add HA pairs

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. To display the file system details page, in the left navigation pane,
   choose **File systems**, and then choose the
   FSx for ONTAP file system that you want to update.
3. On the **Summary** panel, for **Number of HA pairs**, choose **Update**.
4. From the **HA Pairs** dropdown, select the number of HA pairs that you want to add to your file system.
5. Choose the **Update** button.
   After you add HA pairs, it's important to rebalance your existing data to ensure that your I/O remains evenly distributed across your file system's HA pairs.
   For more information, see [Balancing workloads across HA pairs](monitor-workload-balance.md "monitor-workload-balance.md").
