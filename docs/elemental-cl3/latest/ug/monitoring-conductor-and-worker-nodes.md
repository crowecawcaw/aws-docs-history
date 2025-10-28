# Monitoring

nodes

You should monitor the nodes regularly to ensure that they are still
all online.

1. On the Conductor Live main menu, choose **Status**,
   then choose the **Overview** tab.

This page shows a summary of the status of the nodes,
channels, and MPTSes in the cluster. 2. If a node is shown as failed or offline, you can obtain more
information. On the Conductor Live main menu, choose
**Cluster**, then choose
**Nodes**. 3. To identify the problem node or nodes, look for nodes that
have a red or yellow background and an orange icon in the Status
column. 4. Choose an orange icon to go to the **Status**

- **Alerts & Messages** page to display
  detailed information about the alerts and messages. The
  **Alerts & Message**s page appears with
  the filter set to show only the information for this
  channel.

5. Review the alerts and messages to determine why the channel
   failed.
6. For detailed information on dealing with problems, see the
   following topics.

###### Topics

- [Offline nodes](#offline-nodes "#offline-nodes")
- [Failed
  worker nodes with worker redundancy](#failed-worker-nodes-with-worker-redundancy "#failed-worker-nodes-with-worker-redundancy")
- [Failed worker nodes without worker redundancy](#failed-worker-nodes-without-worker-redundancy "#failed-worker-nodes-without-worker-redundancy")
- [Failed Conductor Live nodes
  with Conductor Live redundancy](#failed-conductor-nodes-with-conductor-redundancy "#failed-conductor-nodes-with-conductor-redundancy")
- [Failed Conductor Live nodes without Conductor Live redundancy](#failed-conductor-nodes-without-conductor-redundancy "#failed-conductor-nodes-without-conductor-redundancy")

## Offline nodes

Investigate an offline node if you were not expecting nodes to be
offline. Try to determine why the node has been taken offline (speak
to other engineers and operators) and, if necessary, take steps to
bring the node back online.

## Failed

worker nodes with worker redundancy

When worker redundancy is implemented on the cluster and a node
switches to the failed status, any channels that are running on the
worker node move to a backup node, as described in “How Worker Node
Failover Occurs” below.

### Setting up for

Notification

We recommend that you set up Conductor Live so that it sends you an
email or hits your webserver when the following alerts or
messages are raised:

- 4009
- 4010
- 4018

See the [AWS Elemental Conductor Live Configuration Guide](../configguide.md "../configguide.md") for information on setting up
notifications.

### Dealing with a failed

node

When a node goes to failed, follow this procedure to deal with
the failed node and with the redundancy setup.

1. Go to the **Cluster** -
   **Redundancy** page and look for the
   redundancy group that the failed node belongs to: choose
   each group in the **Redundancy Groups**
   section and look for the node in the **Active
   Nodes** tab and the **Backup
   Nodes** tab.

If the node appears in the **Backup
Nodes** tab, see _If a
Reserve Node Fails_, below. Otherwise,
continue this procedure. 2. Verify if there is still at least one node listed in the
Backup tab.

    * If yes, then there is no immediate need to deal
     with the failed node, but you should still deal with
     it in a timely manner.
    * If not, you can assume that when the failed node
     failed over, it used up the last of your backup
     nodes. You should solve the problem on the failed
     node as soon as possible and bring it back into
     service so that you can get back to the state of
     having at least one backup node.


    You receive an alert if you have a redundancy
     group set up but do not have any backup nodes
     available.

3. To investigate the failed node (either now or later):
   - Go to the **Status** -
     **Nodes** page. The node should
     have an orange icon in the
     **Status** column. Choose this
     icon; the **Status** -
     **Alerts & Messages** page
     appears, filtered to show only the information for
     that node.
   - Review the alerts and messages to determine why
     the node failed.

4. Make sure you have the desired number of backup nodes
   set up.

### How worker node

failover occurs

1. Conductor Live determines the action to attempt:
   - If the node was online/idle before it failed,
     Conductor Live takes no fail over action. The node simply
     goes to the failed status.
   - If the node was online/running, Conductor Live attempts to
     failover this node to one of the reserve nodes, as
     described in the following steps.

2. Conductor Live identifies the redundancy group that the failed
   node belongs to and selects a reserve node in that
   group.
3. Conductor Live then attempts to move all channels (in the case
   of a failed Elemental Live node) or MPTSes (in the case of a failed
   Elemental Statmux node) to node_Y and restart the previously running
   channels or MPTS outputs on this new node. The role for
   node_Y changes from **reserve** to
   **active**. This node is no longer
   eligible to be selected as a failover node if another
   active node fails.

### If a reserve node

fails

If a reserve node fails when it is currently in reserve, it
stays as a reserve node but its status changes to
**offline**.

If a reserve node switches to **active** and
then fails, it will be eligible to fail over to another reserve,
in the same way as any other active node is eligible.

### When a failed node

recovers

When a node that is failed is brought back into service, it
returns to the status it had when it failed: Active or Backup.

### Dealing with a false

failure

Conductor Live may determine that node_X has failed, when in fact it
has only become disconnected from the management network (and is
continuing to run channels) but has not shut down.

Meanwhile, because Conductor Live has determined that a failure has
occurred, it attempts to perform a fail over. The fail over
routine does not include any attempt to stop the channels running
on node_X. If the fail over succeeds, the channels are running on
both node_X and the fail over node.

However, if the network connection is later re-established (so
that Conductor Live can now view activity on node_X), Conductor Live attempts to
shut down the channels or MPTSes that are running there.

### If a node does not

fail over

If a node fails but there is no reserve node ready to take
over for it, the node remains active/offline. When the node
problem is resolved and the node goes back online, it still has
its original channels. Channels that were running before the
failure start running again.

### Monitoring

the distribution of nodes in a redundancy group

After a fail over, you should check the state of the
redundancy group and take steps to ensure that the distribution
of active nodes to reserve nodes matches the desired redundancy
type (distribution of active versus backup nodes).

For example, you need to make sure that there is always at
least one reserve node in each redundancy group. Each time a node
fails, a reserve node switches to **active**. It
is possible for all nodes to become active, in which case you
need to re-assign at least one node to reserve in order to be
prepared for a possible new fail over.

On the Redundancy page, make sure that the Redundancy type has
a non-zero number as the second number:

### Redundancy Status

Alert

Alerts
are raised if a redundancy group has one or more active, online
nodes but has no backup, online nodes. The alert persists until a
node is restored to a backup role, or a node without channels is
manually moved to a backup role.

For more information about alerts and messages, see [Monitoring alerts and
messages](monitoring-alerts-and-messages.md "monitoring-alerts-and-messages.md").

## Failed worker nodes without worker redundancy

When worker redundancy is not implemented on the cluster and a
worker node has failed, you must do the following:

- Determine if failure of the node has caused channels to
  fail and then take steps to re-start those failed
  channels.
- Deal with the problem node.

###### To troubleshoot nodes

1. Go to the **Channels** page and determine
   if any channels have failed. If they have, then move the
   channels to other nodes as soon as possible. See [Modifying a channel](modifying-a-channel.md "modifying-a-channel.md") and change the associated
   node.
2. Go to the **Status** -
   **Nodes** page. The node should have an
   orange icon in the **Status** column. Choose
   this icon; the **Status** - **Alerts
   & Messages** page appears, filtered to show
   only the information for that node.
3. Review the alerts and messages to determine why the node
   failed.
4. Take the necessary steps to resolve the problem and bring
   the node back into service.

## Failed Conductor Live nodes

with Conductor Live redundancy

When you have redundant Conductor Live nodes set
up
and
the
primary node
fails, the
secondart
node automatically takes over management of the cluster. This change
in role takes a few seconds.

If
you resolve the problem with the failed primary Conductor Live node and bring it back into the
cluster, that primary node will take back the leadership role from the secondary Conductor Live
node.

## Failed Conductor Live nodes without Conductor Live redundancy

When your cluster has only one Conductor Live node, then when it fails,
you are not able to use Conductor Live to control worker nodes. The worker
nodes are not affected by the Conductor Live node failure.

###### To troubleshoot a Conductor Live node

1. Go to the **Status** -
   **Nodes** page. The Conductor Live node should
   have an orange icon in the **Status** column.
   Choose this icon; the **Status** -
   **Alerts & Messages** page appears,
   filtered to show only the information for that node.
2. Review the alerts and messages to determine why the node
   failed.
3. Take the necessary steps to resolve the problem and bring
   the node back into service.

**Returning a Node from
Failure**

When the Conductor Live node comes back online, it automatically takes
over management of the cluster again. It brings itself up to date in
terms of activity and status of all the nodes:

- If an alert was active when the node failed and the problem
  no longer exists, the alert is automatically cleared.
- If an alert was active and the problem still exists, the
  alert is not cleared.
- If a problem occurred on a worker node while the Conductor Live
  node was offline, the Conductor Live now detects this problem and
  displays a new alert or message.
- If a problem occurred and got resolved on a worker node
  while the Conductor node was offline, the Conductor Live has no
  knowledge of that problem ever having existed. This is really
  the only missing information from the outage.
