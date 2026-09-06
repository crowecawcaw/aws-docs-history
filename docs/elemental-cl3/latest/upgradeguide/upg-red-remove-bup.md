

# Step C: Remove the backup worker nodes
<a name="upg-red-remove-bup"></a>

Remove the backup worker nodes from the redundancy group before removing them from the cluster. You can then upgrade them while the active workers continue to encode. 

**Topics**
+ [Step A: Remove backup workers from redundancy groups](#upg-std-remove-w-red)
+ [Step B: Remove backup workers from the cluster](#upg-std-remove-w-cluster)

## Step A: Remove backup workers from redundancy groups
<a name="upg-std-remove-w-red"></a>

Remove all backup workers from the worker redundancy groups.

**To remove workers from redundancy groups**

1. On the web interface for the primary Conductor Live node, go to the **Cluster** page. 

1.  On the **Cluster** page, choose **Redundancy**. 

1. In the navigation bar, choose the Elemental Live redundancy group.

1. On the **Backup Nodes** tab, choose **Delete** (trash icon) for each node.

1. If you have multiple Elemental Live redundancy groups, repeat this procedure on each group, then go to the next step.

## Step B: Remove backup workers from the cluster
<a name="upg-std-remove-w-cluster"></a>

Remove the backup workers from the cluster so that you can perform the upgrade process.

**To remove workers from the cluster**

1. On the **Cluster** page, choose **Nodes**.

1.  On each backup worker, choose the downward triangle and select **Remove Node**. 

1. Remove all backup workers from the cluster, then move on to the upgrade process.