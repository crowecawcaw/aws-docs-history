# Troubleshooting Amazon FSx for OpenZFS issues

Use the following sections to help troubleshoot file system, volume mounting, and storage related issues that you have with FSx for OpenZFS.

###### Topics

- [Troubleshooting file system issues](#troubleshooting-file-system-issues "#troubleshooting-file-system-issues")
- [Troubleshooting volume mounting issues](#fs-mount-fails "#fs-mount-fails")
- [Troubleshooting storage issues](#storage-issues "#storage-issues")
- [Troubleshooting I/O errors and NFS lock reclaim failures](#nfs-failover-issues "#nfs-failover-issues")

## Troubleshooting file system issues

This section describes symptoms causes, and resolutions for when you are unable to create or access a file system.

### Cannot create a file system because of misconfigured security group

Creating an FSx for OpenZFS file system fails with the following error message:

```
The file system cannot be created because the default security group in the
subnet provided or the provided security groups do not permit inbound NFSv4
traffic on TCP port 2049
```

Make sure that the VPC security group you are using for the creation operation is configured as described in
[Managing file system access with with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md"). You must set up the
security group to allow inbound traffic on port 2049 from the security group itself or the full subnet CIDR. This
is required to allow the file system hosts to communicate with each other.

### The Elastic IP address attached to the file system elastic network interface was deleted

Amazon FSx doesn't support accessing file systems from the public Internet. Amazon FSx automatically
detaches any public Elastic IP addresses (an IP address that is reachable from the public Internet),
that gets attached to a file system's elastic network interface.

### The file system's elastic network interface was modified or

deleted

You must not modify or delete any of the file system's elastic network interfaces.
Modifying or deleting a network interface can cause a permanent loss of connection between your
virtual private cloud (VPC) and your file system. To resolve this issue, you must create a new
file system, and do not modify or delete the Amazon FSx network interface. For more information, see [Managing file system access with with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md").

### The compute instance's subnet doesn't use any of the route tables

associated with your file system

FSx for OpenZFS creates an endpoint for accessing your file system in a VPC route table. We recommend
that you configure your file system to use all of the VPC route tables that are associated with the subnets
in which your clients are located. By default, Amazon FSx uses your VPC's main route table. You can optionally
specify one or more route tables for Amazon FSx to use when you create your file system.

If your client is in a subnet that's not associated with any of your file system's route tables,
you need to update your file system's route tables. For information about updating your file system's
Amazon VPC route tables, see
[Updating an Amazon FSx for OpenZFS file system](updating-file-system.md "updating-file-system.md").

## Troubleshooting volume mounting issues

This section describes symptoms, causes, and resolutions for when mounting a file system fails.

### Mounting a volume fails right away

Using the `mount` command fails right away, as shown in the following example.

```
`mount.nfs: access denied by server while mounting fs-02b568bbca05a9129.fsx.us-east-1.amazonaws.com:/abc`
```

This error can occur if you are using an invalid `volume_path` for the volume you are mounting in the mount command.
The `volume_path` must match the fully-qualified path to the volume you want to mount.
For example, to mount the root volume, specify the `volume_path` in the mount command using the following format:
``file-system-DNS-name`:/fsx`. A file system's DNS name is viewable in the Amazon FSx
console on the file system detail page, in the **Network & security tab.**

You can view and copy the exact commands to mount any OpenZFS volume in the Amazon FSx console by choosing **Attach**
on that volume’s details page. For more information, see [Step 2: Mount your file system from an Amazon EC2 instance](getting-started.md#getting-started-step2 "getting-started.md#getting-started-step2").

### Mounting a volume hangs and then fails with timeout error

The `mount` command hangs for a minute or two, and then fails with a timeout error similar to the following example:

```
`mount.nfs: Connection timed out`
```

This error can occur because the security groups for the Amazon EC2 instance or the file system aren't configured properly.
Make sure that the security groups assigned to the file system have the inbound rules described in
[Managing file system access with with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md").

### Mounting a volume using a DNS name fails

A misconfigured Domain Name Service (DNS) name can cause volume mount failures with the following message:

```
H`ost `filesystem_dns_name` not found: 3(NXDOMAIN)`
```

When this occurs, you will need to check your virtual private cloud (VPC) configuration. If you are using a custom VPC,
make sure that DNS settings are enabled. For more information, see [DNS attributes for your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md")
in the _Amazon VPC User Guide_.

Here are some considerations when using a DNS name in the mount command:

- Ensure that the Amazon EC2 instance is in the same VPC as your FSx for OpenZFS file system.
- Connect your Amazon EC2 instance inside a VPC configured to use the DNS server provided by AWS.
  For more information, see [DHCP Options Sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md")
  in the _Amazon VPC User Guide_.
- Ensure that the VPC of the connecting Amazon EC2 instance has DNS host names enabled. For more information, see
  [Updating DNS Support for Your VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating")
  in the _Amazon VPC User Guide_.
- Ensure that DHCP option set has `AmazonProvidedDNS` configured as a domain name server. Amazon FSx uses Route53
  private hosted zones for DNS. For more information, see
  [What is Amazon Route 53 Resolver](../../../Route53/latest/DeveloperGuide/resolver.md "../../../Route53/latest/DeveloperGuide/resolver.md") in the _Amazon Route 53 Resolver Developer Guide_.

## Troubleshooting storage issues

This section describes symptoms, causes, and resolutions for storage issues on your file system.

### Deleting files does not reduce used storage capacity

If deleting a file does not reduce used storage capacity, it's likely that the file's data is part of an
OpenZFS snapshot that you created previously. Snapshots minimize the amount of storage capacity they consume by
only storing each data block once, including blocks used in the most recent version of the file. This means that
if you delete the file but the data blocks are still part of a non-deleted snapshot, those data blocks will be
retained. To reduce your used storage capacity, consider deleting snapshots that you no longer need.

## Troubleshooting I/O errors and NFS lock reclaim failures

During failovers on FSx for OpenZFS Single-AZ (HA) file systems, NFS clients may experience transient I/O errors or extended pauses.
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
   (for example, `eth0` or `ens5`) used to connect to your FSx for OpenZFS Single-AZ (HA) file system:

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

Ensure that these settings are applied consistently across all NFS clients that connect to your FSx for OpenZFS file system
within the same Availability Zone. When using these network optimizations, keep the following in mind:

- **base_reachable_time_ms=5000** – Reduces ARP cache entry validity from 30 seconds to 5 seconds,
  allowing clients to detect IP ownership changes more quickly during a failover event.
- **delay_first_probe_time=1** – Reduces the delay before probing a stale network entry from 5 seconds to 1 second.
- **ucast_solicit=0** – Skips unicast neighbor probes and immediately issues broadcast ARP requests,
  accelerating rediscovery of the active file server.
- **tcp_syn_retries=3** – Reduces TCP connection retry duration from 127 seconds to 15 seconds.

After the network settings are in place, you should monitor your environment to validate the changes.

###### Monitoring your environment after applying changes

- **Monitor system logs for NFS errors** to view NFS-related kernel log messages.

```
`$` `sudo journalctl -f | grep -i nfs`
```

Verify that there are fewer occurrences of messages such as `Lock reclaim failed`.

- **Monitor application logs** to confirm fewer I/O timeouts, connection errors, and retry-related failures during failover events.
- **Validate network impact** to ensure that the increased ARP traffic does not adversely affect network performance in your environment.
