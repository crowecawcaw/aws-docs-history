# Step J: Fail back the running channels

Move the running channels back to the upgraded active node by failing over the backup
node that they're currently on.

###### To fail-back channels

1. On the web interface for the primary Conductor Live node, access **Cluster** >
   **Redundancy**.
2. Select the worker node redundancy group.
3. On the **Active Nodes** tab, locate the node that the channels failed over to
   and choose the **Initiate Fail over** button (double
   arrows).

The upgraded node is moved to the **Active Nodes** tab and
the running channels are moved from the backup worker. 4. When all channels are moved back to the active worker node, re-designate the backup worker
node as a backup, as described in the next step.
