

# Removing a worker node from the cluster
<a name="conductor-live-config-nodes-remove"></a>

Generally, you remove a node only in these situations:
+ To enable HTTPS in the cluster. For the complete procedure for enabling HTTPS, see [Enabling and disabling HTTPS](ssl-config.md). 
+ To move a node to another Conductor Live cluster.
+ To isolate a node, perhaps for troubleshooting purposes.
+ To retire a node, perhaps because you are upgrading your hardware.

**To remove a node**

1. To remove an Elemental Live node, make sure that no channels are associated with the node:

   1. On the web interface of the primary Conductor Live, go to the **Channels** page. Filter the channels list so only the channels associated with this node are displayed. Make a note of these channels.

   1. Either wait for each channel to complete or manually stop a channel by choosing **Stop** beside the channel.

   1. For channels that are associated with the node that you're moving, change the node association by these steps: Choose **Edit** (pencil icon) on the stopped channel and in **Node**, select **None**.

1. To remove either anElemental Live or AWS Elemental Statmux node, make sure there are no MPTS outputs associated with the node:

   1. On the primary Conductor Live node's web interface, go to the **MPTS** page to verify which node each MPTS output is using.

   1. If an MPTS output is using the node that you're deleting, set the MPTS output to use a different node. See the [AWS Elemental Conductor Live User Guide](https://docs.aws.amazon.com/elemental-cl3/latest/ug/) for details.

1. Go to the **Redundancy** page and find the node that you want to remove. On the row for the node, choose the **Delete** (garbage can). On the dialog that appears, choose **OK**.

1. Go to the **Nodes** page and find the node that want to remove. On the row for the node, choose the downward triangle and select **Remove Node**. At the prompt, choose **Remove**.