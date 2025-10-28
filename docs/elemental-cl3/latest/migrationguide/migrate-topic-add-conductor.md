# Adding the secondary Conductor node to the

cluster

Add the secondary node back to the cluster, and then to the redundancy group.

To avoid errors when you're adding the secondary Conductor back to the cluster, wait
approximately three minutes after the upgrade before performing these steps. This wait
ensures that the elemental_se service has restarted and is running.

**Add the secondary node to the cluster**

1. On the web interface for the primary Conductor node, choose
   **Cluster** > **Nodes**, then choose
   **Add Node**.
2. In the **Add Nodes to Cluster** pop-up, complete the node
   information for the secondary Conductor and choose **Add**.
   **Add the secondary node to the redundancy group**

3. On the web interface for the primary Conductor node, choose
   **Cluster** > **Redundancy**, then select
   the Conductor Live redundancy group.
4. Choose **Add HA Nodes**.
5. In the **Add** pop-up, use the **Node**
   drop-down to select the secondary Conductor. Choose **Add**.
