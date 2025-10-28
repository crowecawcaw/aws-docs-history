# Step K: Re-designate the backup worker

node

Re-designate the backup worker as a backup so that it only runs active channels that
have failed over from an active worker node.

###### To designate a backup worker node

1. On the web interface for the primary Conductor Live node, access
   **Cluster** > **Redundancy**.
2. Select the worker node redundancy group.
3. On the **Active Nodes** tab, locate the backup node that the
   channels failed over to and choose the **Move** button
   (circle).

The node is moved back to the **Backup Nodes** tab. 4. When the backup node is moved back to the backup tab, choose a different
active worker node and perform the steps [Step F: Fail over an active node](upg-red-fail.md "upg-red-fail.md") through this step for the same node. Repeat
this entire process for each active worker node in the cluster until all have
been processed.
