# Removing a

Conductor Live node from the cluster

Generally, you remove a node only in these situations:

- As one of
  the steps when you enable HTTPS in the cluster. For the complete procedure to
  enable HTTPS, see [Enabling and disabling HTTPS](ssl-config.md "ssl-config.md").
- To retire a node, perhaps because you are upgrading your
  hardware.

###### To remove a Conductor Live node

Follow this procedure to remove either the primary or the
secondary Conductor Live. In both cases, you perform the procedure on
the primary Conductor Live web interface.

1. [Disable
   HA](conductor-live-config-ha-chg.md "conductor-live-config-ha-chg.md") on the cluster.
2. Still on the **Redundancy** page, find
   the node that you're removing. On the row for the node,
   choose the **Delete** (garbage can). On the
   dialog that appears, choose **OK**.
3. Go to the **Nodes** page and find the
   node that you're removing. On the row for the node, choose
   the downward triangle and select **Remove
   Node**. At the prompt, choose
   **Remove**.
