# Adding (recruiting) worker nodes to

the cluster

You can add nodes into the
cluster. Here are
some scenarios where you add nodes:

- When you initially configure the cluster, you must add the secondary
  AWS Elemental Conductor Live node and all the worker nodes into the cluster. You perform this step
  after you have installed the software on the primary Conductor Live node. At this point,
  the cluster exists but it contains only the primary node.
- You might remove a node and then want to add it back into the cluster. For
  example, if you decide to add user authentication to an existing cluster, one of
  the steps is to remove nodes. In this case, you must remove all the nodes,
  including the primary Conductor Live, and then must add all of them back into the
  cluster.
- You can add a newly obtained worker node into an existing cluster. In this
  case, there is no need to make any preliminary changes to the cluster. You
  simply add the new worker node.
  **Step 1: Get ready to add a secondary Conductor Live**

If you are adding a secondary Conductor Live, make sure that the primary and secondary Conductor Live
nodes have the same [firewall settings](network-firewall.md "network-firewall.md"). If they
don't, you won't be able to add the secondary Conductor Live.

**Step 2: Get ready to add a worker node**

This preliminary step applies only in the following situation:

- You are adding worker nodes to an existing cluster.
- The Conductor Live node or nodes in the cluster have Conductor Live version 3.25.2 or lower.
  The existing worker nodes have version 2.25.2 or lower installed.
- The new worker node or nodes you want to add have version 2.25.3 or
  higher.
  For example, the Conductor Live nodes have version 3.23.0. You want to add workers that have
  version 2.25.5. You can do this, because the versions are within two major versions of
  each other.

The preliminary step is to set the LEGACY_RECRUIT environment variable to True on each
worker node. Perform this step now.

**Step 3: Add a node to the cluster**

Perform the following steps on the primary Conductor Live node.

1. On the primary Conductor Live web interface, choose the **Cluster**
   page, then choose **Nodes**.
2. On the **Nodes** page, choose **Add Node**.
   The **Add Nodes to Cluster** dialog appears showing two
   fields:
   - **Node IP Addresses**
   - **Lookup Node IP Address**

3. Specify the addresses of the nodes to add. You can enter one address, several
   comma-delimited addresses, or a range of addresses. If your network has a DNS
   server, you can look up an address by entering a hostname.
4. When you've entered all the nodes to add, choose **Add**.
5. If an Elemental Live node has SDI cards, you must import the devices so that Conductor Live
   recognizes them. (You [configured
   these devices](conductor-live-config-sdi-dev.md "conductor-live-config-sdi-dev.md") when you configured each worker for the
   network.)

Choose the down arrow beside the node and select **Import
Devices**.
