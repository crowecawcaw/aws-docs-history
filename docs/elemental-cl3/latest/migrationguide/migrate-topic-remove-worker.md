

# Removing a worker node from the cluster
<a name="migrate-topic-remove-worker"></a>

To remove a worker node from the cluster, first you remove channel assignments from the node. Then you remove the worker node from its redundancy group, if it is in one. Finally, you remove the node from the cluster.

You perform all these steps on the primary Conductor node, using the web interface.

## Step A: Stop running channels
<a name="migrate-topic-channel-stop"></a>

**To stop one channel**

Choose the **Channels** page, then select the stop button for the channel to stop.

**To stop several channels or all channels**

1. On the web interface for the primary Conductor node, choose the **Channels** page. 

1. Toward the top of the page, choose **Tasks**, then choose **Stop Channels**. Or if you want to stop only some channels, select the box next to each channel you want to stop.

1. Choose **Next**, then choose **Process Now**.

   Wait for all the channels to stop.

## Step B: Remove node assignments
<a name="migrate-topic-remove-worker-node-assignments"></a>

1.  On the web interface for the primary Conductor node, choose the **Channels** page. 

1. Toward the top of the page, choose **Tasks**, then choose **Change Channel Node Assignments**. The list of channels on all nodes in the cluster appears.

1. Select the channels that you want to de-assign from the worker node. There are several ways to select the channels. 
   + If you want to de-assign all channels from all nodes, choose **Select all channels**.
   + To de-assign the channels from one node, filter the list by node then select all the channels. 

1. Choose **Next**.

1. On the **Select a new node** page, in **New Node**, choose **None**.

1. Choose **Process Now**.

## Step C: Remove node from redundancy group
<a name="migrate-topic-remove-worker-remove-redundancy-groups"></a>

1. On the web interface for the primary Conductor node, choose the **Cluster** page. 

1. On the **Cluster** page, choose **Redundancy**. In the navigation bar, choose the Elemental Live redundancy group.

1. On the **Active Nodes** tab, choose **Delete** (trash icon) for the node.

## Step D: Remove node from cluster
<a name="migrate-topic-remove-worker-remove-cluster"></a>

1. On the **Cluster** page, choose **Nodes**.

1. Find the worker node, choose the downward triangle and select **Remove Node**. 