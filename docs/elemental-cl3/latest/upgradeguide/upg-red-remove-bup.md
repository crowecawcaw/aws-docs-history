# Step C: Remove the backup worker

nodes

Remove the backup worker nodes from the redundancy group before removing them from
the cluster. You can then upgrade them while the active workers continue to encode.

###### Topics

- [Step A: Remove backup
  workers from redundancy groups](#upg-std-remove-w-red "#upg-std-remove-w-red")
- [Step B: Remove backup workers from
  the cluster](#upg-std-remove-w-cluster "#upg-std-remove-w-cluster")

## Step A: Remove backup

workers from redundancy groups

Remove all backup workers from the worker redundancy groups.

###### To remove workers from redundancy groups

1. On the web interface for the primary Conductor Live node, go to the
   **Cluster** page.
2. On the **Cluster** page, choose
   **Redundancy**.
3. In the navigation bar, choose the Elemental Live redundancy group.
4. On the **Backup Nodes** tab, choose
   **Delete** (trash icon) for each node.
5. If you have multiple Elemental Live redundancy groups, repeat this procedure on
   each group, then go to the next step.

## Step B: Remove backup workers from

the cluster

Remove the backup workers from the cluster so that you can perform the upgrade process.

###### To remove workers from the cluster

1. On the **Cluster** page, choose **Nodes**.
2. On each backup worker, choose the downward triangle and select **Remove Node**.
3. Remove all backup workers from the cluster, then move on to the upgrade process.
