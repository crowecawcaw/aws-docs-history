# Removing a Conductor node from the

cluster

You can remove a Conductor node that is not acting as the primary Conductor node — that isn't
controlling the cluster. To remove a Conductor node, you first remove the node from the
redundancy group, and then remove the node from the cluster.

1. Disable HA. On the web interface for the Conductor node, choose
   **Cluster** then choose **Redundancy**.
   Make sure that the Conductor Live redundancy group is selected. In the High Availability
   field, choose Disable. To verify that high availability is disabled, see the
   instructions in [Enabling or disabling high
   availability (HA)](migrate-topic-disable-ha.md "migrate-topic-disable-ha.md").
2. Locate the Conductor to remove and click **Delete** (trash icon)
   to delete it from the redundancy group.
3. On the web interface for the primary Conductor node, choose
   **Cluster**, then choose **Nodes**.
4. Locate the Conductor node and display the options by choosing the down arrow.
   Select **Remove Node**.
