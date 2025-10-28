# Enabling user authentication

This section applies only if you had previously enabled user authentication on the
cluster. User authentication is already set up in the cluster, because the configuration
information was included when you restored the database. But you must apply it (enable
it) again, to push user authentication to every worker node.

We assume that you are familiar with the user authentication process, described in the
[AWS Elemental Conductor Live Configuration Guide](../configguide.md "../configguide.md").

We also assume that you created the recommended administrator users, including the
_api-admin_ user). For information about the role
of this user, see the information about types of users in the Reference: Manage users
section of the [AWS Elemental Conductor Live Configuration Guide](../configguide.md "../configguide.md").

###### To enable user authentication

This procedure involves working with two users (that should already exist in the
cluster). When you are logged in as the _api-admin_
user on the primary Conductor, you copy the _api-admin_
user to each worker node. As part of the copy action, you must specify the
credentials for a user that has SSH access. We recommend that you specify the
_elemental_ user,

1. Log into the web interface on the primary Conductor node as the API admin
   (_api-admin_).
2. On the main menu, choose **Cluster**, then choose
   **Nodes**. Choose **Tasks** (in the top
   left corner) and select **Enable Node Authentication**.
3. On the **Select a user name** page, choose
   `api-admin`.
4. Choose **Next**.
5. On the **Enter a password** page, enter the existing password
   for the _api-admin_ user. When you enter the
   same password, you are setting up _api-admin_
   with the same password on every node in the cluster. Setting up with the same
   password reduces effort with password management.
6. Choose **Next**.
7. On the **Enter the SSH credentials to access nodes page**,
   enter the default user (_elemental_) and its password. Then
   choose **Next**.
8. Choose **Configure Now**.

Refresh the page to track the progress of the action. When all the action has
finished, the **Nodes** page displays each node with a lock
icon. 9. Verify that enabling has succeeded. Enabling succeeds only if the _elemental_ user on the primary Conductor and on the
worker node have the same password. The lock icon might not be a valid indicator
that user authentication succeeded on a worker node.

If your organization has the policy of setting a different _elemental_ password on every node, you must repeat
this process. Each time that you display the **Enter the SSH credentials
to access nodes page**, enter the password for another worker node,
until you have set up all the worker nodes.
