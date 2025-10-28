# About

user authentication

## Summary of procedure

To set up for user authentication, you perform three steps:

- Step 1 — Enable the feature. You must enable the user authentication feature. You
  perform this step on the primary Conductor Live node. This step configures enables user
  authentication at the cluster level. See [Step 1: Enable
  the
  user authentication
  feature](conductor-live-config-auth.md "conductor-live-config-auth.md").
- Step 2 — Apply user authentication on the nodes. You must enable user authentication
  on every node. You perform this step once for all nodes, on the primary Conductor Live node.
  This step configures the individual nodes to require that users log in. See [Step 2:
  Apply user
  authentication on worker
  nodes](conductor-live-config-auth-wrkr.md "conductor-live-config-auth-wrkr.md").
- Step 3 — Create users. You creates user on the primary Conductor Live. These users now work
  from the Conductor Live to perform any work on the cluster. These users can't work on the
  individual worker nodes.

Typically, you also set up one or two users on the individual worker nodes, but only
so that someone can perform troubleshooting tasks on these nodes.

## Types of user authentication

There are two ways to implement user
authentication. For both
types, the first two setup steps are the same. Only the step for adding users is
different.

- Local authentication

With this authentication, you enable authentication on the Conductor Live node.

You then create users for the entire cluster from the primary Conductor Live node. See [Managing users in
Conductor Live](config-conductor-live-users.md "config-conductor-live-users.md"). Users are assigned a role that controls the
user's permissions. These roles are built into Conductor Live. You can't modify the roles or
create new roles.

- PAM authentication

With this authentication, you enable authentication on the Conductor Live node.

You create user credentials from an LDAP server that is external to the AWS Elemental
nodes. The credentials that you assign to the users are stored on the LDAP server.
