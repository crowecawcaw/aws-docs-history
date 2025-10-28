# Centralized management

Conductor Live lets you control both Elemental Live nodes and AWS Elemental Statmux
nodes. These workers nodes must be in a Conductor Live cluster.

With Conductor Live, you do not work on each individual Elemental Live or
AWS Elemental Statmux node. Instead, you work on all nodes from one centralized web
interface on the Conductor Live.

**Conductor Live and Live Nodes**

Centralization via Conductor Live has several advantages for encoding
work:

- You create and run events (referred to as _channels_) from Conductor Live, specifying which node the
  channel is to run on. It is possible to move channels from one node to
  another.
- You create profiles (which hold most of the data for channels) in
  Conductor Live. Any channel on any node can use the same profile. With
  Elemental Live as standalone, there is no profile sharing across nodes.
- You can view the activity on all nodes in a cluster. The Elemental Live
  interface lets you view activity only for the individual standalone
  node.
- You can start and stop channels on any node in the cluster. You can
  add or delete a channel on any node.
- You can perform some changes on several channels at once, even if
  those channels are not on the same node. For example, if several channels
  (distributed across several nodes) all use the same profile, you can change
  all those channels so that they use a new profile (that is a revised
  version of the original profile).
  **Conductor Live and AWS Elemental Statmux**

Centralization via the Conductor Live also has several advantages for
creation of an MPTS:

- You can create an MPTS and add channels to that MPTS from
  Conductor Live.
- You can start and stop an MPTS.
- You can add or remove a channel on any AWS Elemental Statmux node.
- You can change properties of an MPTS in order to change the behavior
  of the MPTS.
- You can view the activity on all AWS Elemental Statmux nodes in a
  cluster
