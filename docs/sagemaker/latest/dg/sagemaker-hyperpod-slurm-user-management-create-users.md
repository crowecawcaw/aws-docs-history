

# Creating users on a Slurm cluster on SageMaker HyperPod

To create POSIX users across the nodes of a Slurm cluster, use the user management extension. You declare users and groups in the extension's `localUsers` configuration, and HyperPod creates them on every node, including nodes that you add later and nodes that HyperPod replaces. Each user gets the same user name and UID on every node, a home directory on the shared file system, SSH key pairs for passwordless SSH between nodes, and a Slurm accounting association so that the user can submit jobs.

The following procedure creates users on every node of your Slurm cluster and maps each one to an IAM principal.

**To create users**

1. Add the users and the groups that they belong to in the user management extension's configuration. If the extension isn't installed yet, install it with them, as described in [Installing the extension](sagemaker-hyperpod-slurm-user-management-extension.md#sagemaker-hyperpod-slurm-user-management-extension-installing-the-extension).
**Note**  
If the extension is already installed, add the users to `localUsers.users` and update the extension instead. For more information, see [Add a user](sagemaker-hyperpod-slurm-user-management-manage.md#sagemaker-hyperpod-slurm-user-management-manage-add-a-user).

1. Map each user to an IAM principal so that each person connects as their own Linux user. For more information, see [Mapping cluster users to IAM principals for access](sagemaker-hyperpod-slurm-user-management-iam-mapping.md).

Each user can then log in to the cluster nodes as their own Linux user.

For all the settings, see [User management extension configuration](sagemaker-hyperpod-slurm-user-management-config.md). If your cluster already has users that scripts created, move them to the extension before you install it. For more information, see [Move users that you created with scripts](sagemaker-hyperpod-slurm-user-management-extension.md#sagemaker-hyperpod-slurm-user-management-extension-move-users-that-you-created-with-scripts).