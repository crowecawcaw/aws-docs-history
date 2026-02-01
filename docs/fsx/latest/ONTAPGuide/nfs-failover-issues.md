# Troubleshooting I/O errors and NFS lock reclaim failures

This section describes issues related to I/O errors and NFS lock reclaim failures during failover events
on FSx for ONTAP file systems and resolutions for each of them.

## You are experiencing I/O errors during failover events

During failovers on FSx for ONTAP Single-AZ file systems, NFS clients may experience transient I/O errors or extended pauses.
For NFSv4+ clients, you may see kernel log messages like:

```
NFS: __nfs4_reclaim_open_state: Lock reclaim failed!
```

These messages indicate that the client was unable to successfully reclaim NFS locks during the failover window.

###### To reduce I/O errors during failover events

On Linux, you can configure network settings on your clients to reduce failover detection time from 55-60 seconds to 15-20 seconds.

###### Important

Always test these configurations in a non-production environment first. These settings increase Address Resolution Protocol (ARP) traffic,
which is used to map IP addresses to physical (MAC) addresses on a local network, and may not be suitable for network-constrained environments.

###### To configure optimized network settings for NFS clients

1. Create a sysctl configuration file on each NFS client. The following example uses `default` to apply settings to all network interfaces.
   If your instance has multiple network interfaces, you can replace `default` with the specific interface name
   (for example, `eth0` or `ens5`) used to connect to your FSx for ONTAP Single-AZ file system:

```
`$` `sudo tee /etc/sysctl.d/99-fsx-failover.conf > /dev/null << 'EOF'
# NFS client optimizations for faster failover detection
# Replace 'default' with your interface name (e.g., eth0, ens5) to target a specific interface
net.ipv4.neigh.default.base_reachable_time_ms=5000
net.ipv4.neigh.default.delay_first_probe_time=1
net.ipv4.neigh.default.ucast_solicit=0
net.ipv4.tcp_syn_retries=3
EOF`
```

2. Apply the settings immediately:

```
`$` `sudo sysctl -p /etc/sysctl.d/99-fsx-failover.conf`
```

3. Verify the configuration is active. If you used `default`, you can verify with the following commands.
   If you specified a specific interface, replace `default` with your interface name (for example, `eth0` or `ens5`):

```
`$` `sysctl net.ipv4.neigh.default.base_reachable_time_ms`
`$` `sysctl net.ipv4.neigh.default.delay_first_probe_time`
`$` `sysctl net.ipv4.neigh.default.ucast_solicit`
`$` `sysctl net.ipv4.tcp_syn_retries`
```

Ensure that these settings are applied consistently across all NFS clients that connect to your FSx for ONTAP file system
within the same Availability Zone. When using these network optimizations, keep the following in mind:

- **base_reachable_time_ms=5000** – Reduces ARP cache entry validity from 30 seconds to 5 seconds,
  allowing clients to detect IP ownership changes more quickly during a failover event.
- **delay_first_probe_time=1** – Reduces the delay before probing a stale network entry from 5 seconds to 1 second.
- **ucast_solicit=0** – Skips unicast neighbor probes and immediately issues broadcast ARP requests,
  accelerating rediscovery of the active file server.
- **tcp_syn_retries=3** – Reduces TCP connection retry duration from 127 seconds to 15 seconds.

After the network settings are in place, you should monitor your environment to validate the changes. You can test a failover event
by modifying throughput capacity of your file system. For more information, see [Testing failover on a file system](high-availability-AZ.md#testing-failover "high-availability-AZ.md#testing-failover").

###### Monitoring your environment after applying changes

- **Monitor system logs for NFS errors** to view NFS-related kernel log messages.

```
`$` `sudo journalctl -f | grep -i nfs`
```

Verify that there are fewer occurrences of messages such as `Lock reclaim failed`.

- **Monitor application logs** to confirm fewer I/O timeouts, connection errors, and retry-related failures during failover events.
- **Validate network impact** to ensure that the increased ARP traffic does not adversely affect network performance in your environment.

## Alternative approaches for NFSv4 environments

In NFSv4 environments where modifying client-side configuration is not feasible, consider the following alternatives:

- **Extend NFSv4 lease timeouts.** Work with your storage administrator to increase NFSv4 lease timeouts.
  Extending these timeouts gives clients additional time to reclaim locks during failover events. For more information, see
  [Specify the NFSv4 locking grace period](https://docs.netapp.com/us-en/ontap/nfs-admin/specify-nfsv4-locking-grace-period-task.html "https://docs.netapp.com/us-en/ontap/nfs-admin/specify-nfsv4-locking-grace-period-task.html")
  in the NetApp ONTAP documentation.
