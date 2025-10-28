# Step F: Remove worker nodes

Remove the worker nodes from the redundancy group, and then from the cluster. Perform
these steps on for all worker nodes in the cluster.

###### Topics

- [Step A: Remove channel
  assignments](#upg-std-remove-w-channels "#upg-std-remove-w-channels")
- [Step B: Remove workers from redundancy
  groups](#upg-std-remove-w-red "#upg-std-remove-w-red")
- [Step C: Remove workers from the
  cluster](#upg-std-remove-w-cluster "#upg-std-remove-w-cluster")

## Step A: Remove channel

assignments

Before you can remove a worker node, first make sure that no channels are assigned
to the node.

###### To remove channels from the node

1. On the primary Conductor Live node's web interface, go to the
   **Channels** page.
2. Ensure that all channels are stopped.
3. Choose **Edit**(pencil icon) on a channel.
4. On the **Edit Channel** page, in
   **Node**, choose **None**.
5. Save the channel. Repeat this procedure to edit the remaining channels to
   have no node assignment.
6. When all of the channels have no node assignments, go to the next
   step.

## Step B: Remove workers from redundancy

groups

Remove all nodes from the worker redundancy groups.

###### To remove workers from redundancy groups

1. On the primary Conductor Live node's web interface, go to the
   **Cluster** page.
2. On the **Cluster** page, choose
   **Redundancy**.
3. In the navigation bar, choose the Elemental Live redundancy group.
4. On the **Backup Nodes** tab, choose
   **Delete** (trash icon) for each node.
5. When you've removed all backup nodes, choose the **Active
   Nodes** tab and choose **Delete** (trash icon)
   for each node.
6. If you have multiple Elemental Live redundancy groups, repeat this procedure on
   each group, then go to the next step.

## Step C: Remove workers from the

cluster

Remove the nodes from the cluster so that you can perform the upgrade
process.

###### To remove workers from the cluster

1. On the **Cluster** page, choose
   **Nodes**.
2. On each worker node, choose the downward triangle and select
   **Remove Node**.
3. Remove all nodes from the cluster, then move on to the upgrade
   process.
