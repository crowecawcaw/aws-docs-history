# Troubleshooting: gateway offline

issues

Use the following troubleshooting information to determine what to do if the AWS Storage Gateway
console shows that your gateway is offline.

Your gateway might be showing as offline for one or more of the following reasons:

- The gateway can't reach the Storage Gateway service endpoints.
- The gateway shut down unexpectedly.
- A cache disk associated with the gateway has been disconnected or modified, or has
  failed.
  To bring your gateway back online, identify and resolve the issue that caused your gateway
  to go offline.

## Check the associated firewall or proxy

If you configured your gateway to use a proxy, or you placed your gateway behind a
firewall, then review the access rules of the proxy or firewall. The proxy or firewall
must allow traffic to and from the network ports and service endpoints required by
Storage Gateway. For more information, see [Network and firewall
requirements](Requirements.md#networks "Requirements.md#networks").

## Check for an ongoing SSL or deep-packet inspection of your gateway's

traffic

If an SSL or deep-packet inspection is currently being performed on the network
traffic between your gateway and AWS, then your gateway might not be able to
communicate with the required service endpoints. To bring your gateway back online, you
must disable the inspection.

## Check for a power outage or hardware failure on the hypervisor host

A power outage or hardware failure on the hypervisor host of your gateway can cause
your gateway to shut down unexpectedly and become unreachable. After you restore the
power and network connectivity, your gateway will become reachable again.

After your gateway is back online, be sure to take steps to recover your data. For
more information, see [Best practices for
recovering your data](recover-data-from-gateway.md "recover-data-from-gateway.md").

## Check for issues with an associated cache disk

Your gateway can go offline if at least one of the cache disks associated with your
gateway was removed, changed, or resized, or if it is corrupted.

###### If a working cache disk was removed from the hypervisor host:

1. Shut down the gateway.
2. Re-add the disk.

###### Note

Make sure you add the disk to the same disk node. 3. Restart the gateway.

###### If a cache disk is corrupted, was replaced, or was resized:

1. Shut down the gateway.
2. Reset the cache disk.
3. Reconfigure the disk for cache storage.
4. Restart the gateway.

For more information on troubleshooting a corrupted cache disk for a
tape gateway, see [You need to recover a virtual tape from a malfunctioning cache disk](Main_TapesIssues-vtl.md#creating-recovery-tape-vtl "Main_TapesIssues-vtl.md#creating-recovery-tape-vtl").
