

# Step 2: Apply user authentication on worker nodes
<a name="conductor-live-config-auth-wrkr"></a>

The following steps describe how to enable *node authentication* in the cluster. Before you enable node authentication, you must [enable user authentication](conductor-live-config-auth.md).

This procedure applies to both types of user authentication—local authentication and PAM authentication. 

**Where to perform the configuration**

Make sure you perform the configuration on the correct nodes.



| Node | Node where you perform this task | 
| --- | --- | 
| Primary Conductor Live node | Yes | 
| Secondary Conductor Live node | No | 
| Each worker node | No | 

**To enable user authentication**

To enable user authentication on all the worker nodes, you log onto the primary Conductor Live node and display the **Cluster Nodes** page.

1. Make sure you have followed the procedure in [Step 1: Enable the user authentication feature](conductor-live-config-auth.md).

1. Go to the Conductor Live web interface by entering the IP address of the primary Conductor Live node in a web browser. Log into the web interface as the API admin (*apiadmin*). You created this user when you enabled user authentication on the Conductor Live node (in the [previous step](conductor-live-config-auth.md)). 

1. On the main menu, choose **Cluster**, then **Nodes**. Choose **Tasks** (in the top left corner) and select **Enable Node Authentication**.

1. On the **Select a user name** page, choose **apiadmin** and choose **Next**. 

   In this step, you are identifying the administrator that will serve as the reserved API user. When you use this name, you set up so that the API administrator has the same name (*apiadmin*) on all nodes. This practice reduces confusion. For more information about this user, see [Types of users](users-types.md).

1. On the **Enter a password** page, enter the existing a password for *apiadmin*. When you enter the same password, you keep the password for *apiadmin* aligned on all the nodes in the cluster. This practice reduces confusion.

1. Choose **Next**.

1. On the **Enter the SSH credentials to access nodes page**, enter the default user (*elemental*) and its password. Then choose **Next**.

1. Choose **Configure Now**.

   Conductor Live enables user authentication on each node. It also creates the API admin (*apiadmin*) on each worker node. 

   Refresh the page to track the progress of the action. When all the nodes are ready, the Nodes page displays each node with a lock icon to indicate user authentication is enabled.

**Result of this procedure**

You have enabled user authentication on the secondary Conductor Live node and each worker node. You have also propagated the [API admin (*apiadmin*)](users-types.md) to all these nodes. 