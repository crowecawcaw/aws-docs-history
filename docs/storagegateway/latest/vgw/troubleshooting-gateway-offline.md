

# Troubleshooting: gateway offline issues
<a name="troubleshooting-gateway-offline"></a>

Use the following troubleshooting information to determine what to do if the AWS Storage Gateway console shows that your gateway is offline.

Your gateway might be showing as offline for one or more of the following reasons:
+ The gateway can't reach the Storage Gateway service endpoints.
+ The gateway shut down unexpectedly.
+ A cache disk associated with the gateway has been disconnected or modified, or has failed.

To bring your gateway back online, identify and resolve the issue that caused your gateway to go offline.

## Check the associated firewall or proxy
<a name="w2ab1c40c12c11"></a>

If you configured your gateway to use a proxy, or you placed your gateway behind a firewall, then review the access rules of the proxy or firewall. The proxy or firewall must allow traffic to and from the network ports and service endpoints required by Storage Gateway. For more information, see [Network and firewall requirements](https://docs.aws.amazon.com/storagegateway/latest/vgw/Requirements.html#networks).

## Check for an ongoing SSL or deep-packet inspection of your gateway's traffic
<a name="w2ab1c40c12c13"></a>

If an SSL or deep-packet inspection is currently being performed on the network traffic between your gateway and AWS, then your gateway might not be able to communicate with the required service endpoints. To bring your gateway back online, you must disable the inspection.

## Check for a power outage or hardware failure on the hypervisor host
<a name="w2ab1c40c12c17"></a>

A power outage or hardware failure on the hypervisor host of your gateway can cause your gateway to shut down unexpectedly and become unreachable. After you restore the power and network connectivity, your gateway will become reachable again.

After your gateway is back online, be sure to take steps to recover your data. For more information, see [Best practices for recovering your data](https://docs.aws.amazon.com/storagegateway/latest/vgw/recover-data-from-gateway.html).

## Check for issues with an associated cache disk
<a name="w2ab1c40c12c19"></a>

Your gateway can go offline if at least one of the cache disks associated with your gateway was removed, changed, or resized, or if it is corrupted.

**If a working cache disk was removed from the hypervisor host:**

1. Shut down the gateway.

1. Re-add the disk.
**Note**  
Make sure you add the disk to the same disk node.

1. Restart the gateway.

**If a cache disk is corrupted, was replaced, or was resized:**

1. Shut down the gateway.

1. Reset the cache disk.

1. Reconfigure the disk for cache storage.

1. Restart the gateway.