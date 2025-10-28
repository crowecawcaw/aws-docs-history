# Step J: Add the secondary Conductor Live node

If you have only one Conductor Live, skip this step and go to [Step K: Start channels](upg-std-start.md "upg-std-start.md").

Add the secondary node back to the cluster, and then to the redundancy group.

To avoid errors when you're adding the secondary Conductor Live back to the cluster, wait
approximately three minutes after the upgrade before performing these steps. This wait
ensures that the elemental_se service has restarted and is running.

###### To add the secondary node to the cluster

1. On the web interface for the primary Conductor Live node, access
   **Cluster** > **Nodes** and choose
   **Add Node**.
2. In the **Add Nodes to Cluster** pop-up, complete the node
   information for the secondary Conductor Live and choose **Add**.
   When the secondary node is added back to the cluster, add it to the Conductor Live redundancy
   group.

###### To add the secondary node to the redundancy group

1. On the web interface for the primary Conductor Live node, access
   **Cluster** > **Redundancy** and select
   the Conductor Live redundancy group.
2. Choose **Add HA Nodes**.
3. In the **Add** pop-up, use the **Node**
   drop-down to select the secondary Conductor Live. Choose
   **Add**.
   When the secondary node is added back to the cluster and redundancy group, you can
   start the channels, as described in the following section.
