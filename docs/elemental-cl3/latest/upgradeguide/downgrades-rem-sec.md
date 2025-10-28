# Step E: Remove the secondary

Conductor node

If you have only one Conductor Live, skip this step and go to [Step F: Downgrade the nodes](downgrades-cl3-upg-dg-cond.md "downgrades-cl3-upg-dg-cond.md").

Prior to upgrading, you must remove the secondary Conductor Live node first from the
redundancy group, and then from the cluster. You can't remove the node from the cluster
if it's still in the redundancy group.

###### To remove the secondary node from the redundancy group

1. On the web interface for the primary Conductor Live node, access **Cluster** > **Redundancy** and ensure that you have the Conductor Live redundancy group selected.
2. Locate the secondary Conductor Live and click Delete (trash icon) to delete it from the redundancy group.
   When the secondary Conductor Live node is removed from the redundancy group, remove it from the cluster.

###### To remove the secondary node from the cluster

1. On the web interface for the primary Conductor Live node, access **Cluster** > **Nodes**.
2. Locate the secondary Conductor Live node and display the options by choosing the down-facing arrow.
3. Select **Remove Node**.
   When the node is removed from the redundancy group and the cluster, you can move forward with the downgrade process.
