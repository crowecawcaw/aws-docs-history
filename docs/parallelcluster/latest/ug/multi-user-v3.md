

# Multiple user access to clusters
<a name="multi-user-v3"></a>

Learn to implement and manage multiple user access to a single cluster.

In this topic, an AWS ParallelCluster user refers to a system user for compute instances. An example is an `ec2-user` for an Amazon EC2 instance.

AWS ParallelCluster multi-user access support is available in all the AWS Regions where AWS ParallelCluster is currently available. It works with other AWS services, including [Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html) and [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html).

You can use an [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) or [Simple AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_simple_ad.html) to manage cluster access. Make sure to check [AWS Region availability](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/regions.html) for these services. To set up a cluster, specify an [AWS ParallelCluster DirectoryService](DirectoryService-v3.md) configuration. AWS Directory Service directories can be connected to multiple clusters. This allows for centralized management of identities across multiple environments and a unified login experience.

When you use AWS Directory Service for AWS ParallelCluster multiple user access, you can log in to the cluster with user credentials that are defined in the directory. These credentials consist of a user name and password. After you log in to the cluster for the first time, a user SSH key is automatically generated. You can use it to log in without a password.

You can create, delete, and modify a cluster’s users or groups after your directory service is deployed. With AWS Directory Service, you can do this in the AWS Management Console or by using the *Active Directory Users and Computers* tool. This tool is accessible from any Amazon EC2 instance that's joined to your Active Directory. For more information, see [Installing the Active Directory administration tools](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_install_ad_tools.html).

If you plan to use AWS ParallelCluster in a single subnet with no internet access, see [AWS ParallelCluster in a single subnet with no internet access](aws-parallelcluster-in-a-single-public-subnet-no-internet-v3.md) for additional requirements.

**Topics**
+ [Create an Active Directory](create-addir-v3.md)
+ [Create a cluster with an AD domain](create-addircluster-v3.md)
+ [Log in to a cluster integrated with an AD domain](login-addircluster-v3.md)
+ [Running MPI jobs](addircluster-MPI-v3.md)
+ [Example AWS Managed Microsoft AD over LDAP(S) cluster configurations](examples-addir-v3.md)