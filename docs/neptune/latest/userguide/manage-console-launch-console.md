# Launching a Neptune DB cluster using the AWS Management Console

The easiest way to launch a new Neptune DB cluster is to use an CloudFormation template
that creates all the required resources for you, as explained in [Create Neptune cluster](get-started-create-cluster.md "get-started-create-cluster.md").

If you prefer, you can also use the Neptune console to launch
a new DB cluster manually, as explained here.

###### Note

Before you can access the Neptune console to create a Neptune cluster, you must have a user with sufficent permissions.
If your current user does not have these permissions then you can create an IAM user with the necessary permissions to
do so, as explained in [Creating an IAM user with permissions for Neptune](manage-console-iam-user.md "manage-console-iam-user.md").

Once you have verified that your user has the correct permissions, or you have created a user with the correct permissions,
log into the AWS Management Console as that IAM user and follow the steps below to create a new DB cluster:

###### To launch a Neptune DB cluster using the console

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. Navigate to the **Clusters** page under **Databases** and choose
   **Create database**, which opens the **Create database** page.
3. Under **Settings**, enter a name for your new DB cluster
   or accept the default name that is supplied there. This name is used in the
   endpoint address of the instance, and must satisfy the following constraints:
   - It must contain from 1 to 63 alphanumeric characters or hyphens.
   - Its first character must be a letter.
   - It cannot end with a hyphen or contain two consecutive hyphens.
   - It must be unique across all DB instances in your AWS account in a given AWS Region.

4. Under **Templates**, choose either **Production**
   or **Development and Testing**.
5. Under **DB instance size**, choose an instance size. This will
   determine the processing and memory capacity of the primary write instance of your
   new DB cluster.

If you selected the **Production** template, you can only choose
from among the available memory-optimized classes listed, but if you selected the
**Development and testing**, you can also choose from among the more
economical burstable classes (see [T3 Burstable Instances](manage-console-instances-t3.md "manage-console-instances-t3.md") for a discussion of burstable
classes).

###### Note

Starting with [Neptune engine release 1.1.0.0](engine-releases-1.1.0.md "engine-releases-1.1.0.md")
Neptune no longer supports `R4` instance types. 6. Under **Availability and durability**, you can choose whether or
not to enable multi-availability-zone (multi-AZ) deployment. The production template
enables multi-AZ deployment by default, whereas the development and testing template
does not. If multi-AZ deployment is enabled, Neptune locates read-replica instances
that you create in different availability zones (AZs) to improve availability. 7. Under **Connectivity**, select the virtual private cloud (VPC)
that will host your new DB cluster from among the available choices. Here you can choose
**Create new VPC** if you want Neptune to create the VPC for you.
You must create an Amazon EC2 instance in this same VPC to access the Neptune instance (for more
information, see [Securing your Amazon Neptune database with Amazon VPC](security-vpc.md "security-vpc.md")). Note
that you can't change the VPC after the DB cluster has been created.

If you need to, you can further configure connectivity for your cluster under
**Additional connectivity configuration**:

    1. Under **Subnet group**, you can choose the Neptune
     DB subnet group to use for the new DB cluster. If your VPC does not yet have any
     subnet groups, Neptune creates a DB subnet group for you (see [Securing your Amazon Neptune database with Amazon VPC](security-vpc.md "security-vpc.md")).
    2. Under **VPC security groups**, choose one or more
     existing VPC security groups to secure network access to the new DB cluster,
     or choose **Create new** if you want Neptune to create one
     for you, and then supply a name for the new VPC security group (see
     [Create a security group using the VPC console](get-started-vpc.md#security-vpc-security-group "get-started-vpc.md#security-vpc-security-group")).
    3. Under **Database port**, enter the TCP/IP port that
     the database will use for application connections. Neptune uses port number
     `8182` as the default.

8. Under **Notebook configuration**, choose **Create
   notebook** if you want Neptune to create Jupyter notebooks for you
   in the Neptune workbench (see
   [Using Amazon Neptune with graph notebooks](graph-notebooks.md "graph-notebooks.md")
   and [Using the Neptune workbench to host Neptune notebooks](graph-notebooks.md#graph-notebooks-workbench "graph-notebooks.md#graph-notebooks-workbench")).
   You can then choose how the new notebooks should be configured:
   1. Under **Notebook instance type**, choose from among
      the available instance classes for your notebook.
   2. Under **Notebook name**, enter a name for your notebook.
   3. If you want, you can also enter a description of the notebook under
      **Description - optional**.
   4. Under **IAM role name**, either choose to have
      Neptune create an IAM role for the notebook, and enter a name for the new
      role, or choose to select an existing IAM role from among the available roles.
   5. Finally, choose whether your notebook connects to the internet directly
      or through Amazon SageMaker AI or through a VPC with a NAT gateway. See [Connect a Notebook
      Instance to Resources in a VPC](../../../sagemaker/latest/dg/appendix-notebook-and-internet-access.md "../../../sagemaker/latest/dg/appendix-notebook-and-internet-access.md") for more information.

9. Under **Tags**, you can associate up to 50 tags with
   your new DB cluster.
10. Under **Additional configuration**, there are more settings
    that you can make for your new DB cluster (in many cases, you can skip them and
    accept default values for now):

| Option                                | What you can do                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DB instance identifier**            | You can provide a name for the writer instance of<br>the cluster. If you don't, a default identifier based on the cluster<br>name is used. If you do, specify a name that is unique for all DB instances<br>owned by your AWS account in the current region. The DB instance<br>identifier is case insensitive, but stored as all lower-case.                                                                                                                                                                                                                                         |
| **DB cluster parameter group**        | Select a DB cluster parameter group to define the default<br>configuration for all DB instances in the cluster. Unless you choose<br>otherwise, Neptune uses a default DB cluster parameter group.<br>For more information about parameter groups, see [Amazon Neptune parameter groups](parameter-groups.md "parameter-groups.md").                                                                                                                                                                                                                                                  |
| **DB parameter group**                | Select a DB parameter group to define the configuration of<br>the primary DB instance in the cluster. Unless you choose otherwise,<br>Neptune uses a default parameter group. For more information<br>about parameter groups, see [Parameter groups](parameter-groups.md "parameter-groups.md").                                                                                                                                                                                                                                                                                      |
| **IAM DB authentication**             | If you check **Enable IAM DB authentication**, all<br>access to your database will be authenticated using AWS Identity and Access Management (IAM).<br>ImportantThis requires that you sign all requests with AWS Signature<br>Version 4 signing. For more information, see [Authenticating your Amazon Neptune database with AWS Identity and Access Management](iam-auth.md "iam-auth.md").                                                                                                                                                                                         |
| **Failover priority**                 | Choose `No preference` or a priority tier for failover.<br>If you choose a tier and there is contention within it, the<br>replica that is the same size as the primary instance is selected.                                                                                                                                                                                                                                                                                                                                                                                          |
| **Backup retention period**           | Choose the length of time, from 1 to 35 days, that Neptune<br>should retain automatic backups of this DB instance. You can only perform a<br>point-in-time restore (PITR) to a time within the backup retention period.                                                                                                                                                                                                                                                                                                                                                               |
| **Copy tags to snapshots**            | (_Enabled by default_) This option causes all tags<br>associated with your DB cluster to be copied to any snapshots of it.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Enable encryption**                 | (_Enabled by default_) This option causes the data<br>in your DB cluster to be encrypted at rest.<br>If you do, choose the master key used to protect the key that is used<br>to encrypt this database volume. You can select the default `aws/rds`<br>key, or choose from master keys in your account, or enter the ARN of a key<br>from a different account. You can create a new master encryption key on the<br>\*_Encryption Keys_<br>• tab of the IAM console. For more<br>information, see [Encrypting data at rest in your Amazon Neptune database](encrypt.md "encrypt.md"). |
| **Audit log**                         | Check this if you want audit logs from your DB cluster published<br>to CloudWatch Logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Enable auto minor version upgrade** | (_Enabled by default_) This option causes<br>your DB cluster to be automatically upgraded to new minor engine versions<br>after they are released. The automatic upgrades occur during the maintenance<br>window for the database. See [Using AutoMinorVersionUpgrade](engine-maintenance-management.md#using-amvu "engine-maintenance-management.md#using-amvu").                                                                                                                                                                                                                    |
| **Maintenance window**                | You can select a specific period during which you want pending<br>modifications to your DB cluster to happen, such as a change to a DB instance<br>class or an automatic engine patch. Any such maintenance operations are<br>started and completed within the selected period. If you do not select<br>a period, Neptune assigns a maintenance period arbitrarily.                                                                                                                                                                                                                   |
| **Enable deletion protection**        | (_Enabled by default_) Deletion protection<br>blocks your DB cluster from being deleted. You must explicitly disable it<br>in order to delete the DB cluster.                                                                                                                                                                                                                                                                                                                                                                                                                         |

11. Choose **Create database** to launch your new Neptune DB cluster
    and its primary instance.

On the Amazon Neptune console, the new DB cluster appears in the list of Databases.
The DB cluster has a status of **Creating** until it is
created and ready for use. When the state changes to **Available**,
you can connect to the primary instance for your DB cluster. Depending on the DB
instance class and store allocated, it can take several minutes for the new instances
to be available.

To view the newly created cluster, choose the **Databases** view
in the Neptune console.

###### Note

If you delete all Neptune DB instances in a DB cluster using the AWS Management Console, the
console automatically deletes the DB cluster itself. If you are using the AWS CLI or SDK,
you must delete the DB cluster manually after you delete its last instance.

Make note of the **Cluster endpoint** value. You need this
to connect to your Neptune DB cluster.
