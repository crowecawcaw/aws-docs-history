

# 1-to-1 redundancy
<a name="redundancy-11"></a>

## Setup
<a name="redundancy-11-setup"></a>

The redundancy group contains one pair of nodes that are both active. You designate one node as the primary node, and the other as the secondary node.

When you create a channel or MPTS, you assign the node to the primary node. As soon as you save the channel, Conductor Live automatically duplicates the channel (or MPTS) onto the secondary node. If you later make changes to the channel or MPTS, Conductor Live automatically applies those changes to the channel or MPTS on the secondary node.

You start the channel or MPTS on the primary node. Conductor Live automatically starts the channel or MPTS on the secondary node. In this way, the two nodes are both *hot.*

This diagram is an example of a 1-to-1 redundancy group for Elemental Live nodes. The same design applies to Elemental Statmux nodes.

![Two live active nodes connected vertically in a 1-to-1 redundancy group configuration.](http://docs.aws.amazon.com/elemental-cl3/latest/ug/images/Live_resil_node_1-1.png)


## What happens in a failure
<a name="redundancy-11-failure"></a>

If one of the nodes fails, the other node continues to process the content. There is a delay of a few seconds before the output resumes.

This diagram illustrates the change in the group after one node fails. This diagram is for Elemental Live but the same pattern applies to Elemental Statmux.

![Two nodes in a group: one failed node shown in gray, one live active node shown in green.](http://docs.aws.amazon.com/elemental-cl3/latest/ug/images/Live_resil_node_1-1-failed.png)


## Considerations
<a name="redundancy-11-considerations"></a>
+ The two nodes must have identical capabilities.
+ You should have a policy in place for recovering after a node failure. Decide whether you will immediately try to get the failed node back into production. 
+ When you get a failed node back into production, you must restart each channel or MPTS that was running on that node. You will then be back to a redundant setup for the nodes.