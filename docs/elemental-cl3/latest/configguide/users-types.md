# Types of users

In a cluster, there are several types of users, as described in the
following sections.

###### Topics

- [Users on Conductor Live
  nodes](#conductor-live-user-types-cl "#conductor-live-user-types-cl")
- [Users on worker
  nodes](#config-conductor-live-user-types-workers "#config-conductor-live-user-types-workers")
- [Summary](#config-conductor-live-user-types-summary "#config-conductor-live-user-types-summary")

## Users on Conductor Live

nodes

You can set up several different types of users on Conductor Live
nodes.

### The _elemental_ user

- Purpose: When you start an SSH session to work on the software
  through the operating system, you log in using this user. You
  can't log into SSH using any other user.
- How created: This user is built into the software. You are
  prompted to change the password for this user either the first
  time you installed the software on the node, or the first time
  that you ran the configure script on the node.

###### Warning

You are prompted to change the password for this user. Make sure
that you assign the same password on every node. Otherwise, you
won't be able to enable user authentication on some nodes.

### The default user on

Conductor Live

- Purpose: This user is the default administrator.
- How created: You might have created this user when you
  installed the software. You might have enabled user authentication
  when you installed the software. In this case, you probably
  accepted the suggested name of _admin_ for the default user.

Or you might have created this user when you followed the
procedure in [Step 1: Enable
the
user authentication
feature](conductor-live-config-auth.md "conductor-live-config-auth.md") to
enable user authentication on Conductor Live. In this case, the default
user has the role of the API admin. You should have called this
user _api-admin_.

### The _API admin_ user on Conductor Live

- Purpose on the Conductor Live nodes: When the cluster is running
  (after you've configured it), Conductor Live uses the API key of the API
  administrator for authentication when sending commands to worker
  nodes. For security reasons, you should not use this administrator
  for regular administrative tasks.

Purpose on worker nodes: This administrator is the boot strap
administrator on Conductor Live. After you've first enabled user
authentication, you log into worker nodes using this
administrator's credentials, and [create
regular administrators](#config-conductor-live-user-types-workers "#config-conductor-live-user-types-workers") on the worker nodes.

- How created on the primary Conductor Live node: You should have
  created this user when you ran the configuration script or the
  installer to [enable
  user authentication](conductor-live-config-auth.md "conductor-live-config-auth.md").

How created on other nodes: You created the user when you
[enabled node
authentication](conductor-live-config-auth-wrkr.md "conductor-live-config-auth-wrkr.md") on all the other nodes in the cluster.
Conductor Live then creates this user on every worker node.

- Username for this user: You should assign the name _api-admin_.
- Working with this user: After you've set up user
  authentication on the cluster, don't log in as this user. Instead,
  reserve it for its main role, which is to authenticate API
  commands between nodes in the cluster. To perform regular
  administration tasks, log in as a regular administrator.

### Regular administrators on

Conductor Live

- Purpose: Regular administrators have the same access as the
  default admin user. They have full read-write access, including
  the ability to create and manage users.
- How created: Any administrator creates these administrators on
  the primary Conductor Live. These users are pushed to the secondary Conductor Live
  when you [enable HA (high
  availability)](conductor-live-config-ha.md "conductor-live-config-ha.md") on the cluster. They aren't pushed to
  worker nodes.
- Username for this user: Typically, assign the person's name as
  the username.

### Operators on Conductor Live

- Purpose: Operators have full read-write access, except that
  they can't create or manage users.
- How created. Any administrator creates these operators on the primary Conductor Live.
  These users are pushed to the secondary Conductor Live when you [enable HA (high availability)](conductor-live-config-ha.md "conductor-live-config-ha.md") on the
  cluster. They aren't pushed to worker nodes.

- Username for this user: Typically, assign the person's name as
  the username.

### Viewers on Conductor Live

- Purpose: Operators have read-only access to all functions,
  except that they have no access to users.
- How created. Any administrator creates these operators on the
  primary Conductor Live. These users are pushed to the secondary Conductor Live
  when you [enable HA (high
  availability)](conductor-live-config-ha.md "conductor-live-config-ha.md") on the cluster. They aren't pushed to
  worker nodes.
- Username for this user: Typically, assign the person's name as
  the username.

## Users on worker

nodes

When workers are in a Conductor Live cluster, you only need to set up one or
two users, to let you log on directly to the node in order to
troubleshoot.

### Regular

administrators on worker nodes

- Purpose: Set up people as regular administrators only if they will perform
  troubleshooting on worker nodes.
  Typically, you set
  up the same person (for example, a manager) as a regular administrator on every worker
  node. Make sure that these people understand that they should log
  into an individual node only to troubleshoot. They should perform all regular
  activities on Conductor Live.
- How created: You should create these administrators on each node (Conductor Live and the
  worker nodes).
- Username for this user: Typically, assign the person's name as
  the username.

### Regular users on

worker nodes

Only standalone
setups of Elemental Live have
regular
users — managers, operators, and viewers.

###### Note

Don't set up
regular
users on worker nodes when your organization is using a Conductor Live
cluster.

## Summary

Following is a summary of the users that you must explicitly create.

| Type of user                             | How created                                                                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Regular administrators on Conductor Live | You manually add these users by [working on the primary Conductor Live](conductor-live-config-users.md "conductor-live-config-users.md")               |
| Operators on Conductor Live              | You manually add these users by [working on the primary Conductor Live](conductor-live-config-users.md "conductor-live-config-users.md")               |
| Viewers on Conductor Live                | You manually add these users by [working on the primary Conductor Live](conductor-live-config-users.md "conductor-live-config-users.md")               |
| Regular administrators on worker nodes   | You manually add these users by [working on each worker node](config-conductor-live-users-add-workers.md "config-conductor-live-users-add-workers.md") |
