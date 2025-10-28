# Step F: Fail over an active node

Fail over the running channels from the first active worker node that you're upgrading
to a backup node. To reduce impact on your worker nodes, perform this step through [Step K: Re-designate the backup worker
node](upg-red-redesignate.md "upg-red-redesignate.md") all for the same
active worker node before moving on to the next node.

###### To fail-over a node

1. On the web interface for the primary Conductor Live node, access **Cluster** >
   **Redundancy**.
2. Select the worker node redundancy group which contains the node that you're failing
   over.
3. On the **Active Nodes** tab, locate the node that you're upgrading and choose the
   **Initiate Failover** button (double arrows).

The backup node is moved to the **Active Nodes** tab and the running channels
are moved from the failed worker. 4. When all channels are failed to a backup worker node, upgrade the failed active node as
described in the next step.

###### Warning

Your worker redundancy group will persist in an N+0 redundancy type until you've upgraded all worker nodes. In a production
scenario, this is _not a valid configuration_. An
alert will persist until you are back to an N+1, 1+1, or N+M redundancy
type.
