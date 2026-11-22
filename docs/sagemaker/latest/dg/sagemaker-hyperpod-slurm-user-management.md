

# User management on a SageMaker HyperPod Slurm cluster

HyperPod Slurm clusters are typically used by multiple users — machine learning (ML) researchers, software engineers, data scientists, and cluster administrators — who each edit their own files and run their own jobs. This section describes how to create and manage users across the nodes of a Slurm cluster on SageMaker HyperPod.

To manage users, install the user management extension. You define users and groups as JSON, and HyperPod creates them on every node, including nodes that you add later. The extension also controls SSH and sudo access for each node type, and can connect the cluster to Active Directory. The user management extension requires a Slurm cluster that uses continuous provisioning.

The result is consistent POSIX users with the same user name and UID on every node, home directories on a shared file system, SSH key pairs on the shared file system for passwordless SSH between nodes, and users registered with Slurm accounting so that they can submit jobs. After you create users, map each one to an AWS Identity and Access Management (IAM) principal so that each person connects as their own Linux user. For details, see [Mapping cluster users to IAM principals for access](sagemaker-hyperpod-slurm-user-management-iam-mapping.md).

**Important**  
If your cluster already has users that scripts created, move them to the extension before you install it. An account whose UID or home directory differs from the extension's configuration makes the extension fail on that node with a conflict. For the steps, see [Move users that you created with scripts](sagemaker-hyperpod-slurm-user-management-extension.md#sagemaker-hyperpod-slurm-user-management-extension-move-users-that-you-created-with-scripts).

**Note**  
Granting users access to HyperPod cluster nodes allows them to install and operate user-managed software on the nodes. Make sure that you maintain the principle of least-privilege permissions for users.

To connect the cluster to Active Directory, use the extension's `ldap` source. For details, see [Integrate HyperPod clusters with Active Directory](sagemaker-hyperpod-slurm-user-management-active-directory.md).

**Topics**
+ [User management extension](sagemaker-hyperpod-slurm-user-management-extension.md)
+ [How permissions work in the user management extension](sagemaker-hyperpod-slurm-user-management-permissions.md)
+ [User management extension configuration](sagemaker-hyperpod-slurm-user-management-config.md)
+ [Managing users and groups](sagemaker-hyperpod-slurm-user-management-manage.md)
+ [Creating users on a Slurm cluster on SageMaker HyperPod](sagemaker-hyperpod-slurm-user-management-create-users.md)
+ [Mapping cluster users to IAM principals for access](sagemaker-hyperpod-slurm-user-management-iam-mapping.md)
+ [Integrate HyperPod clusters with Active Directory](sagemaker-hyperpod-slurm-user-management-active-directory.md)