# Deploying a new cluster

Read this section if you are setting up AWS Elemental Conductor Live, AWS Elemental Live, and (optionally) AWS Elemental Statmux
for the first time.

(If you are grouping existing Elemental Live nodes into a Conductor Live cluster, see [Upgrading standalone
nodes into a cluster](config-conductor-live-checklist-standalone-to-cluster.md "config-conductor-live-checklist-standalone-to-cluster.md").)

###### Warning

You must perform these steps in the specified order. Otherwise, the cluster might not
get set up correctly.

**Step 1: Design the cluster**

As your first step, you should design the cluster. For guidelines, see [Designing the cluster](ready-conductor-live-cg.md "ready-conductor-live-cg.md").

**Step 2: Install software**

You might need to install the AWS Elemental software on the Conductor Live nodes and worker nodes.

- If you have obtained AWS Elemental appliances, you don't need to install software. The
  appliances are delivered with software already installed.

- If you have obtained qualified hardware, you must install the software. See the
  appropriate guide:
  - [_AWS Elemental Conductor Live Install Guide_](../installguide.md "../installguide.md"). Keep in mind
    that Elemental Statmux is installed as part of Conductor Live.
  - [_AWS Elemental Live Install Guide_](../../../elemental-live/latest/installguide.md "../../../elemental-live/latest/installguide.md")

###### Note

Make sure that both Conductor Live nodes have the same software version installed.

**Step 3: Configure connectivity features on the
nodes**

- On each worker node, perform the tasks that are listed in [Configuring nodes for connectivity](config-conductor-live-network.md "config-conductor-live-network.md"). Perform these tasks in any order.
- On the primary Conductor Live node, perform the tasks that are listed in [Configuring nodes for connectivity](config-conductor-live-network.md "config-conductor-live-network.md"). Perform these tasks in any order.
- On the secondary Conductor Live node, perform the following tasks. Perform these tasks in
  any order:

      + Configure [DNS servers](config-cluster-dns.md "config-cluster-dns.md").
      + Configure [Ethernet
       interfaces and bonds](config-conductor-live-config-ethernet-add.md "config-conductor-live-config-ethernet-add.md")(optional).
      + [Enable HTTPS](ssl-config.md "ssl-config.md") on the node.
      + Configure [NTP servers](config-cluster-ntp.md "config-cluster-ntp.md").

  You don't need to configure as many fields on the secondary Conductor Live because the
  secondary Conductor Live will synchronize with the primary Conductor Live.
  **Step 4: Configure features on the worker**

On each worker node, configure the features that apply to that node, from the list in
[Configure worker features](config-conductor-live-features.md "config-conductor-live-features.md").

You can configure these features at any time in this setup procedure.

**Step 5:
Enable
user authentication on the Conductor Live**

We recommend that you set up the nodes so that users must log into the node. For
an overview of
how
user
authentication
works, see
[About
user authentication](config-conductor-live-user-auth-overview.md "config-conductor-live-user-auth-overview.md").

If you do decide to set up in this way, you must enable
the user
authentication feature
on the Conductor Live, before you
recruit
the
nodes to the cluster:

- On the primary Conductor Live, run the configuration script to [enable
  the
  user
  authentication
  feature](conductor-live-config-auth.md "conductor-live-config-auth.md").
  **Step 6: Recruit nodes into the cluster**

Recuit
the
primary Conductor Live nodes and all the workers nodes into the cluster. See [Adding (recruiting) worker nodes to
the cluster](conductor-live-config-nodes-add.md "conductor-live-config-nodes-add.md")

The nodes get added to the cluster, but they don't yet belong to any redundancy
group.

**Step 7: Configure redundancy groups in the cluster**

We recommend that you set up the cluster with Conductor redundancy (a primary and a
secondary Conductor Live node), and with worker node redundancy.

- Design a redundancy plan. For information, see [_AWS Elemental Conductor Live User Guide_](../ug.md "../ug.md")
- [Create the redundancy groups](conductor-live-config-redundancy.md "conductor-live-config-redundancy.md")
  that you identified.
- [Add the worker nodes](conductor-live-config-wrkr-red.md "conductor-live-config-wrkr-red.md") to each
  worker redundancy group.
- [Add the primary and secondary
  Conductor Live nodes](conductor-live-config-redundancy-cl.md "conductor-live-config-redundancy-cl.md") to the Conductor redundancy group.
  **Step 8:
  Apply
  user authentication on
  worker
  nodes**

If you enabled user authentication on the primary
Conductor Live (earlier in this
procedure), you
must
now
apply
user authentication on all the
worker
nodes in the cluster.

- On the primary Conductor Live,
  apply
  user authentication. See [Step 2:
  Apply user
  authentication on worker
  nodes](conductor-live-config-auth-wrkr.md "conductor-live-config-auth-wrkr.md").
  **Step 9: Add users to the nodes**

If you enabled user authentication, you must now add users. For information about
the
types of users that you can add, see [Managing users in
Conductor Live](config-conductor-live-users.md "config-conductor-live-users.md").

Add
these types of users:

- One or two
  _regular administators_ on Conductor Live. For information, see
  [Adding users to Conductor Live](conductor-live-config-users.md "conductor-live-config-users.md").
- _Operators_ and _viewers_ on Conductor Live. For information, see [Adding users to Conductor Live](conductor-live-config-users.md "conductor-live-config-users.md").

- One or two
  _regular administrators_
  on
  each individual worker node. These administrators will access the worker node locally (by
  logging on directly on the web interface of the node) only in order to troubleshoot. For
  information, see
  [Adding users to
  worker nodes](config-conductor-live-users-add-workers.md "config-conductor-live-users-add-workers.md").
  **Step 10: Enable HA**

[Enable HA (high availability)](conductor-live-config-ha.md "conductor-live-config-ha.md") on the
primary Conductor Live.
