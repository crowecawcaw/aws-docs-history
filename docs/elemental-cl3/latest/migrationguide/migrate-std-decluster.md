# Step C: Tear down the cluster

Before you can install RHEL 9 and the new software version, you must remove all the
nodes from the cluster.

1. Disable high availability (HA) on the cluster. You must disable HA before you
   can remove the secondary Conductor node. See [Enabling or disabling high
   availability (HA)](migrate-topic-disable-ha.md "migrate-topic-disable-ha.md"). After you disable HA, only the primary Conductor can control the cluster.

If you don't have HA enabled, skip this step. 2. Remove the secondary Conductor node from the cluster. You must remove the secondary
node so that when you shut down the primary Conductor node, control doesn't fail over
to the secondary Conductor node. See [Removing a Conductor node from the
cluster](migrate-topic-remove-c-node.md "migrate-topic-remove-c-node.md").

If you have only one Conductor node, skip this step. 3. 4. Remove the workers from the cluster. You perform this action from the primary
Conductor node. See [Removing a worker node from the
cluster](migrate-topic-remove-worker.md "migrate-topic-remove-worker.md").
After you remove the last worker node, the cluster still exists but it doesn't contain
any worker nodes or a secondary Conductor. The single Conductor exists, but it isn't controlling
any worker nodes.
