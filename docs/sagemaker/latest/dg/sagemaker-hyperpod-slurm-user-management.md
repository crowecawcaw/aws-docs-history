

# User management on a SageMaker HyperPod Slurm cluster
<a name="sagemaker-hyperpod-slurm-user-management"></a>

HyperPod Slurm clusters are typically used by multiple users — machine learning (ML) researchers, software engineers, data scientists, and cluster administrators — who each edit their own files and run their own jobs. This section describes how to create and manage users across the nodes of a Slurm cluster on SageMaker HyperPod.

If you configured your Slurm cluster with Amazon FSx during HyperPod cluster creation, a shared file system is a good option for setting up workspaces for your cluster users. Setting up a user creates consistent POSIX users (same user name and UID on every node), sets up home directories on the shared file system, generates SSH keypairs on the shared file system for passwordless inter-node SSH, and registers users with Slurm accounting so they can submit jobs.

After you create the POSIX users, complete the setup by mapping each user to an IAM principal so they can connect to the cluster as their own account. For details, see [Mapping cluster users to IAM principals for access](sagemaker-hyperpod-slurm-user-management-iam-mapping.md).

Alternatively, instead of statically creating users on each instance, you can integrate the cluster with a directory service. For details, see [Integrate HyperPod clusters with Active Directory](sagemaker-hyperpod-slurm-user-management-active-directory.md).

**Note**  
Granting users access to HyperPod cluster nodes allows them to install and operate user-managed software on the nodes. Make sure that you maintain the principle of least-privilege permissions for users.

There are three ways to create users on a Slurm cluster, plus options for mapping those users to IAM principals and integrating with a directory service. For a comparison of the user-creation options and guidance on choosing one, see [Creating users on a Slurm cluster on SageMaker HyperPod](sagemaker-hyperpod-slurm-user-management-create-users.md).

**Topics**
+ [Creating users on a Slurm cluster on SageMaker HyperPod](sagemaker-hyperpod-slurm-user-management-create-users.md)
+ [Mapping cluster users to IAM principals for access](sagemaker-hyperpod-slurm-user-management-iam-mapping.md)
+ [Integrate HyperPod clusters with Active Directory](sagemaker-hyperpod-slurm-user-management-active-directory.md)