

# Launching a Neptune DB cluster using the AWS Management Console
<a name="manage-console-launch-console"></a>

The easiest way to launch a new Neptune DB cluster is to use an CloudFormation template that creates all the required resources for you, as explained in [Create Neptune cluster](get-started-create-cluster.md).

If you prefer, you can also use the Neptune console to launch a new DB cluster manually, as explained here.

**Note**  
 Before you can access the Neptune console to create a Neptune cluster, you must have a user with sufficent permissions. If your current user does not have these permissions then you can create an IAM user with the necessary permissions to do so, as explained in [Creating an IAM user with permissions for Neptune](manage-console-iam-user.md). 

Once you have verified that your user has the correct permissions, or you have created a user with the correct permissions, log into the AWS Management Console as that IAM user and follow the steps below to create a new DB cluster:

**To launch a Neptune DB cluster using the console**

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home).

1. Navigate to the **Clusters** page under **Databases** and choose **Create database**, which opens the **Create database** page.

1. Under **Settings**, enter a name for your new DB cluster or accept the default name that is supplied there. This name is used in the endpoint address of the instance, and must satisfy the following constraints:
   + It must contain from 1 to 63 alphanumeric characters or hyphens.
   + Its first character must be a letter.
   + It cannot end with a hyphen or contain two consecutive hyphens.
   + It must be unique across all DB instances in your AWS account in a given AWS Region.

1. Under **Templates**, choose either **Production** or **Development and Testing**.

1. Under **DB instance size**, choose an instance size. This will determine the processing and memory capacity of the primary write instance of your new DB cluster.

   If you selected the **Production** template, you can only choose from among the available memory-optimized classes listed, but if you selected the **Development and testing**, you can also choose from among the more economical burstable classes (see [T3 Burstable Instances](manage-console-instances-t3.md) for a discussion of burstable classes).
**Note**  
Neptune no longer supports `R4` instance types.

1. Under **Availability and durability**, you can choose whether or not to enable multi-availability-zone (multi-AZ) deployment. The production template enables multi-AZ deployment by default, whereas the development and testing template does not. If multi-AZ deployment is enabled, Neptune locates read-replica instances that you create in different availability zones (AZs) to improve availability.

1. Under **Connectivity**, select the virtual private cloud (VPC) that will host your new DB cluster from among the available choices. Here you can choose **Create new VPC** if you want Neptune to create the VPC for you. You must create an Amazon EC2 instance in this same VPC to access the Neptune instance (for more information, see [Securing your Amazon Neptune database with Amazon VPC](security-vpc.md)). Note that you can't change the VPC after the DB cluster has been created.

   If you need to, you can further configure connectivity for your cluster under **Additional connectivity configuration**:

   1. Under **Subnet group**, you can choose the Neptune DB subnet group to use for the new DB cluster. If your VPC does not yet have any subnet groups, Neptune creates a DB subnet group for you (see [Securing your Amazon Neptune database with Amazon VPC](security-vpc.md)).

   1. Under **VPC security groups**, choose one or more existing VPC security groups to secure network access to the new DB cluster, or choose **Create new** if you want Neptune to create one for you, and then supply a name for the new VPC security group (see [Create a security group using the VPC console](get-started-vpc.md#security-vpc-security-group)).

   1. Under **Database port**, enter the TCP/IP port that the database will use for application connections. Neptune uses port number `8182` as the default.

   1. Under **Network type**, choose **IPv4** to allow only IPv4 addresses to communicate with the DB cluster, or choose **Dual-stack** to allow both IPv4 and IPv6 addresses to communicate with the DB cluster. For more information, see [Dual-stack mode](neptune-dualstack-db-cluster.md).

1. Under **Notebook configuration**, choose **Create notebook** if you want Neptune to create Jupyter notebooks for you in the Neptune workbench (see [Using Amazon Neptune with graph notebooks](graph-notebooks.md) and [Using the Neptune workbench to host Neptune notebooks](graph-notebooks.md#graph-notebooks-workbench)). You can then choose how the new notebooks should be configured:

   1. Under **Notebook instance type**, choose from among the available instance classes for your notebook.

   1. Under **Notebook name**, enter a name for your notebook.

   1. If you want, you can also enter a description of the notebook under **Description - optional**.

   1. Under **IAM role name**, either choose to have Neptune create an IAM role for the notebook, and enter a name for the new role, or choose to select an existing IAM role from among the available roles.

   1. Finally, choose whether your notebook connects to the internet directly or through Amazon SageMaker AI or through a VPC with a NAT gateway. See [Connect a Notebook Instance to Resources in a VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-notebook-and-internet-access.html) for more information.

1. Under **Tags**, you can associate up to 50 tags with your new DB cluster.

1. Under **Additional configuration**, there are more settings that you can make for your new DB cluster (in many cases, you can skip them and accept default values for now):    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/neptune/latest/userguide/manage-console-launch-console.html)

1. Choose **Create database** to launch your new Neptune DB cluster and its primary instance.

   On the Amazon Neptune console, the new DB cluster appears in the list of Databases. The DB cluster has a status of **Creating** until it is created and ready for use. When the state changes to **Available**, you can connect to the primary instance for your DB cluster. Depending on the DB instance class and store allocated, it can take several minutes for the new instances to be available.

   To view the newly created cluster, choose the **Databases** view in the Neptune console. 
**Note**  
If you delete all Neptune DB instances in a DB cluster using the AWS Management Console, the console automatically deletes the DB cluster itself. If you are using the AWS CLI or SDK, you must delete the DB cluster manually after you delete its last instance.

   Make note of the **Cluster endpoint** value. You need this to connect to your Neptune DB cluster.