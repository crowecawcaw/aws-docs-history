

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/). 

# Reconnecting an unavailable cluster node
<a name="reconnectingclusternodefortpoint"></a>

A *node*, or device within a cluster, can become temporarily unavailable due to an issue like power or network loss without damaging the data on the node. When this happens, it affects the status of your cluster. A node's network reachability and lock status is reported in the Snowball Edge client by using the `snowballEdge describe-cluster` command.

We recommend that you physically position your cluster so you have access to the front, back, and top of all nodes. This way, you can access power and network cables on the back, shipping labels on the top for node IDs, and LCD screens on the front of the devices for the IP addresses and other administrative information.

When you detect that a node is unavailable, we recommend that you try one of the following procedures, depending on the scenario that caused the node to become unavailable.

**To reconnect an unavailable node**

1. Ensure that the node is powered on.

1. Ensure that the node is connected to the same internal network that the rest of the cluster is connected to.

1. If you need to power up the node, wait up to 20 minutes for it to finish.

1. Run the `snowballEdge unlock-cluster` command or the `snowballEdge associate-device` command. For an example, see [Unlocking Snowball Edge devices](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-client-commands.html#setting-up-client).

**To reconnect an unavailable node that lost network connectivity, but didn't lose power**

1. Ensure that the node is connected to the same internal network that the rest of the cluster is on.

1. Run the `snowballEdge describe-device` command to see when the previously unavailable node is added back to the cluster. For an example, see [Getting Device Status](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-client-commands.html#client-status).

After you perform the preceding procedures, your nodes should be working normally. You should also have a read/write quorum. If that's not the case, then one or more of your nodes might have a more serious issue and might need to be removed from the cluster.