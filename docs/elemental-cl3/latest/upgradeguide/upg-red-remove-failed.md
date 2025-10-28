# Step G: Remove the failed worker

node

Remove the failed worker node from the redundancy group and then from the cluster. It
can then be upgraded while the backup worker continues to encode.

###### Topics

- [Step A: Remove failed worker from
  redundancy groups](#upg-std-remove-w-red "#upg-std-remove-w-red")
- [Step B: Remove failed worker from the
  cluster](#upg-std-remove-w-cluster "#upg-std-remove-w-cluster")

## Step A: Remove failed worker from

redundancy groups

Remove the active worker that you just failed over from the worker redundancy
group.

###### To remove the failed worker from a redundancy group

1. On the web interface for the primary Conductor Live node, go to the **Cluster** page.
2. On the **Cluster** page, choose **Redundancy**.
3. In the navigation bar, choose the Elemental Live redundancy group.
4. On the **Backup Nodes** tab, choose **Delete** (trash icon) for the failed worker.

## Step B: Remove failed worker from the

cluster

Remove the failed worker from the cluster so that you can perform the upgrade process.

###### To remove the failed worker from the cluster

1. On the **Cluster** page, choose **Nodes**.
2. On each the failed worker, choose the downward triangle and select **Remove Node**.
3. Move on to the upgrade process for this worker.
