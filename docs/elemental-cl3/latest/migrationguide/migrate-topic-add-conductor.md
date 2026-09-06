

# Adding the secondary Conductor node to the cluster
<a name="migrate-topic-add-conductor"></a>

Add the secondary node back to the cluster, and then to the redundancy group.

To avoid errors when you're adding the secondary Conductor back to the cluster, wait approximately three minutes after the upgrade before performing these steps. This wait ensures that the elemental\_se service has restarted and is running.

**Add the secondary node to the cluster**

1. On the web interface for the primary Conductor node, choose **Cluster** > **Nodes**, then choose **Add Node**.

1. In the **Add Nodes to Cluster** pop-up, complete the node information for the secondary Conductor and choose **Add**.

**Add the secondary node to the redundancy group**

1. On the web interface for the primary Conductor node, choose **Cluster** > **Redundancy**, then select the Conductor Live redundancy group.

1. Choose **Add HA Nodes**.

1. In the **Add** pop-up, use the **Node** drop-down to select the secondary Conductor. Choose **Add**.