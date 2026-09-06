

# Enabling user authentication
<a name="migrate-topic-user-auth"></a>

This section applies only if you had previously enabled user authentication on the cluster. User authentication is already set up in the cluster, because the configuration information was included when you restored the database. But you must apply it (enable it) again, to push user authentication to every worker node.

We assume that you are familiar with the user authentication process, described in the [AWS Elemental Conductor Live Configuration Guide](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/).

We also assume that you created the recommended administrator users, including the *api-admin* user). For information about the role of this user, see the information about types of users in the Reference: Manage users section of the [AWS Elemental Conductor Live Configuration Guide](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/).

**To enable user authentication**

This procedure involves working with two users (that should already exist in the cluster). When you are logged in as the *api-admin* user on the primary Conductor, you copy the *api-admin* user to each worker node. As part of the copy action, you must specify the credentials for a user that has SSH access. We recommend that you specify the *elemental* user,

1. Log into the web interface on the primary Conductor node as the API admin (*api-admin*). 

1. On the main menu, choose **Cluster**, then choose **Nodes**. Choose **Tasks** (in the top left corner) and select **Enable Node Authentication**.

1. On the **Select a user name** page, choose **api-admin**.

1. Choose **Next**. 

1. On the **Enter a password** page, enter the existing password for the *api-admin* user. When you enter the same password, you are setting up *api-admin* with the same password on every node in the cluster. Setting up with the same password reduces effort with password management.

1. Choose **Next**.

1. On the **Enter the SSH credentials to access nodes page**, enter the default user (*elemental*) and its password. Then choose **Next**.

1. Choose **Configure Now**.

   Refresh the page to track the progress of the action. When all the action has finished, the **Nodes** page displays each node with a lock icon.

1. Verify that enabling has succeeded. Enabling succeeds only if the *elemental* user on the primary Conductor and on the worker node have the same password. The lock icon might not be a valid indicator that user authentication succeeded on a worker node.

   If your organization has the policy of setting a different *elemental* password on every node, you must repeat this process. Each time that you display the **Enter the SSH credentials to access nodes page**, enter the password for another worker node, until you have set up all the worker nodes.