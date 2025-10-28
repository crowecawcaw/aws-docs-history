# Adding user

authentication to an existing cluster

The procedure to add user authentication to the AWS Elemental Conductor Livecluster includes multiple steps.
You must remove the nodes from the cluster, enable user authentication, and then add the nodes
back to the cluster:

- On each worker node, perform these tasks in the specified order:
  - Remove each worker node from the cluster. See [Removing a
    worker node from the cluster](conductor-live-config-nodes-remove.md "conductor-live-config-nodes-remove.md")
  - [Enable HTTPS](ssl-config.md "ssl-config.md")
  - Recruit
    (add) the node back into the cluster See [Adding (recruiting) worker nodes to
    the cluster](conductor-live-config-nodes-add.md "conductor-live-config-nodes-add.md").

- On the primary Conductor Live node, perform these tasks in the specified
  order:
  - [Disable HTTPS](ssl-config.md "ssl-config.md")
  - [Remove the primary Conductor Live
    node](conductor-live-config-nodes-remove.md "conductor-live-config-nodes-remove.md") from the cluster.

  - [Enable
    the user
    authentication
    feature](conductor-live-config-auth.md "conductor-live-config-auth.md").
  - [Recruit
    (add) the primary Conductor Live node](conductor-live-config-nodes-add.md "conductor-live-config-nodes-add.md") back into the cluster, then
    [add it](conductor-live-config-redundancy-cl.md "conductor-live-config-redundancy-cl.md") back into its
    redundancy group.
  - [Apply
    user authentication](conductor-live-config-auth-wrkr.md "conductor-live-config-auth-wrkr.md") on the cluster.
  - [Add
    users](config-conductor-live-users.md "config-conductor-live-users.md").
  - [Enable
    HA](conductor-live-config-ha.md "conductor-live-config-ha.md").
  - [Enable HTTPS](ssl-config.md "ssl-config.md").
