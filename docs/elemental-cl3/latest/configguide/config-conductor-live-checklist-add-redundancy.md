# Adding

Conductor redundancy to an existing cluster

You might have originally deployed the cluster with only one AWS Elemental Conductor Live node. You might
now want to add a secondary Conductor Live node, to implement node redundancy on the Conductor
nodes.

Perform the following steps in the specified order:

1.  As your first step, you should identify your redundancy requirements. See [Designing the cluster](ready-conductor-live-cg.md "ready-conductor-live-cg.md").
2.  [Verify the firewall setup](network-firewall.md "network-firewall.md") is the primary
    Conductor Live:
    - Make sure that the firewall is enabled on both Conductor Live nodes.
    - Accept port 5432 TCP.

3.  Configure the secondary Conductor Live, perform the following tasks. Perform these tasks in
    any order:

        * [Configure DNS servers](config-cluster-dns.md "config-cluster-dns.md").
        * [Configure Ethernet
         interfaces](config-conductor-live-config-ethernet-add.md "config-conductor-live-config-ethernet-add.md") and bonds (optional).
        * [Enable HTTPS](ssl-config.md "ssl-config.md") on the node..
        * Configure [NTP servers](config-cluster-ntp.md "config-cluster-ntp.md").

    You don't need to configure as many fields on the secondary Conductor Live because the
    secondary Conductor Live will synchronize with the primary Conductor Live.

4.  [Recruit
    (add)](conductor-live-config-nodes-add.md "conductor-live-config-nodes-add.md") the secondary Conductor Live
    into
    the existing cluster.
5.  Create a redundancy group for the two Conductor Live nodes, and add the nodes to that group.
    See [Creating a
    Conductor Live redundancy group](conductor-live-config-redundancy-cl.md "conductor-live-config-redundancy-cl.md").
6.  [Enable HA (high availability)](conductor-live-config-ha.md "conductor-live-config-ha.md") on the
    primary Conductor Live. When you enable HA, the secondary Conductor Live synchronizes itself with the
    primary Conductor Live.
