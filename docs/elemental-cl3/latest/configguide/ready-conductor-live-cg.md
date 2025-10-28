# Designing the cluster

You should make some decisions about features you want to configure on the cluster.

**Nodes in the cluster**

For information about deciding about the number of AWS Elemental Conductor Live and worker nodes in the
cluster, see [_AWS Elemental Conductor Live User Guide_](../ug.md "../ug.md").

For information about designing for redundancy in the cluster, see [_Conductor Live User
Guide_](../ug.md "../ug.md").

**Gather network information**

1.  We strongly recommend that, if your deployment involves several Conductor Live clusters, you set
    up each cluster in its own network.
2.  Identify the network interfaces and devices for all the worker nodes, including the
    following:

        * Ethernet interfaces


        * SDI devices


        * DNS servers to connect to
        * NTP servers to connect to
        * Remote servers. For example, servers where files assets are stored that Elemental Live events
         will use

    **User authentication**

Your organization might require that users present credentials in order to work with the
nodes. You can implement a simple built-in user authentication, or you can implement PAM
authentication.

###### Note

We strongly recommend that you enable user authentication, and that you implement it with
HTTPS enabled.

User authentication is a mode in the cluster. If user authentication is enabled, all users
must always log on to any node in the cluster. See [About
user authentication](config-conductor-live-user-auth-overview.md "config-conductor-live-user-auth-overview.md").

**Plan for backup of databases**

Conductor Live is configured by default to back up the data for the Conductor Live nodes and all workers
nodes. You can configure the Conductor Live to back up to a remote server. See [Configuring backup and
restore on Conductor Live](config-conductor-live-backup.md "config-conductor-live-backup.md").

###### Note

We strongly recommend that you back up data to a remote server.

**Notifications**

You can configure the nodes for notifications. Some types of notifications are always
enabled, but you can customize the behavior. Other types of notifications work only if you
enable them. See [Configuring
notifications for messages](conductor-live-config-notifications.md "conductor-live-config-notifications.md").
