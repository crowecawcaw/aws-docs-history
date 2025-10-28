# Creating a DAX cluster using the

AWS Management Console

This section describes how to create an Amazon DynamoDB Accelerator (DAX) cluster using the
AWS Management Console.

###### Topics

- [Step 1: Create a subnet group](#DAX.create-cluster.console.create-subnet-group "#DAX.create-cluster.console.create-subnet-group")
- [Step 2: Create a DAX cluster](#DAX.create-cluster.console.create-cluster "#DAX.create-cluster.console.create-cluster")
- [Step 3: Configure security group inbound rules](#DAX.create-cluster.console.configure-inbound-rules "#DAX.create-cluster.console.configure-inbound-rules")

## Step 1: Create a subnet

group using the AWS Management Console

Follow this procedure to create a subnet group for your Amazon DynamoDB Accelerator (DAX)
cluster using the AWS Management Console.

###### Note

If you already created a subnet group for your default VPC, you can skip this
step.

DAX is designed to run within an Amazon Virtual Private Cloud (Amazon VPC) environment. If you created your
AWS account after December 4, 2013, you already have a default VPC in each AWS
Region. For more information, see [Default
VPC and default subnets](../../../vpc/latest/userguide/default-vpc.md "../../../vpc/latest/userguide/default-vpc.md") in the _Amazon VPC User Guide_.

As part of the creation process for a DAX cluster, you must specify a
_subnet group_. A subnet group is a collection of one or more
subnets within your VPC. When you create your DAX cluster, the nodes are deployed to
the subnets within the subnet group.

###### Note

The VPC having this DAX cluster can contain other resources and even VPC endpoints
for the other services except VPC endpoint for ElastiCache and can result in error
for the DAX cluster operations.

###### To create a subnet group

1. Open the DynamoDB console at
   [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2. In the navigation pane, under **DAX**, choose
   **Subnet groups**.
3. Choose **Create subnet group**.
4. In the **Create subnet group** window, do the
   following:
   1. **Name**—Enter a short name for the subnet
      group.
   2. **Description**—Enter a description for the
      subnet group.
   3. **VPC ID**—Choose the identifier for your Amazon VPC
      environment.
   4. **Subnets**—Choose one or more subnets from the
      list.

   ###### Note

   The subnets are distributed among multiple Availability Zones. If
   you plan to create a multi-node DAX cluster (a primary node and
   one or more read replicas), we recommend that you choose multiple
   subnet IDs. Then DAX can deploy the cluster nodes into multiple
   Availability Zones. If an Availability Zone becomes unavailable,
   DAX automatically fails over to a surviving Availability Zone.
   Your DAX cluster will continue to function without
   interruption.When the settings are as you want them, choose **Create subnet
   group**.

To create the cluster, see [Step 2: Create a DAX
cluster using the AWS Management Console](#DAX.create-cluster.console.create-cluster "#DAX.create-cluster.console.create-cluster").

## Step 2: Create a DAX

cluster using the AWS Management Console

Follow this procedure to create an Amazon DynamoDB Accelerator (DAX) cluster in your default
Amazon VPC.

###### To create a DAX cluster

1.  Open the DynamoDB console at
    [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2.  In the navigation pane, under **DAX**, choose
    **Clusters**.
3.  Choose **Create cluster**.
4.  In the **Create cluster** window, do the following:
    1. **Cluster name**—Enter a short name for your
       DAX cluster.

    ###### Note

    Since `sudo` and `grep` are reserved
    keywords, you cannot create a DAX cluster with these words in the
    cluster name. For example, `sudo` and
    `sudocluster` are invalid cluster names. 2. **Cluster description**—Enter a description for
    the cluster. 3. **Node types**—Choose the node type for all of
    the nodes in the cluster. 4. **Cluster size**—Choose the number of nodes in
    the cluster. A cluster consists of one primary node and up to nine read
    replicas.

    ###### Note

    If you want to create a single-node cluster, choose
    **1**. Your cluster will consist of one primary
    node.

    If you want to create a multi-node cluster, choose a number
    between **3** (one primary and two read replicas)
    and **10** (one primary and nine read
    replicas).

    ###### Important

    For production usage, we strongly recommend using DAX with
    at least three nodes, where each node is placed in a different
    Availability Zone. Three nodes are required for a DAX cluster
    to be fault-tolerant.

    A DAX cluster can be deployed with one or two nodes for
    development or test workloads. One- and two-node clusters are
    not fault-tolerant, and we don't recommend using fewer than
    three nodes for production use. If a one- or two-node cluster
    encounters software or hardware errors, the cluster can become
    unavailable or lose cached data. 5. Choose **Next**. 6. **Subnet group**—Select **Choose
    existing** and choose the subnet group that you created in
    [Step 1: Create a subnet
    group using the AWS Management Console](#DAX.create-cluster.console.create-subnet-group "#DAX.create-cluster.console.create-subnet-group"). 7. **Access control**—Choose the
    **default** security group. 8. **Availability Zones (AZ)**—Choose
    **Automatic**. 9. Choose next. 10. **IAM service role for DynamoDB access**—Choose
    **Create new**, and enter the following
    information:

        * **IAM role name**—Enter a name for an
         IAM role, for example, `DAXServiceRole`. The
         console creates a new IAM role, and your DAX cluster assumes
         this role at runtime.
        * Select the box next to **Create
         policy**.
        * **IAM role policy**—Choose
         **Read/Write**. This allows the DAX
         cluster to perform read and write operations in DynamoDB.
        * **New IAM policy name**—This field will
         populate as you enter the IAM role name. You can also enter a name
         for an IAM policy, for example, `DAXServicePolicy`.
         The console creates a new IAM policy and attaches the policy
         to the IAM role.
        * **Access to DynamoDB tables**—Choose
         **All tables**.

    11. **Encryption**—Choose **Turn on
        encryption at rest** and **Turn on encryption in
        transit** For more information, see [DAX encryption at rest](DAXEncryptionAtRest.md "DAXEncryptionAtRest.md")
        and [DAX encryption in transit](DAXEncryptionInTransit.md "DAXEncryptionInTransit.md").A separate service role for DAX to access Amazon EC2 is also required. DAX
        automatically creates this service role for you. For more information, see
        [Using service-linked roles for DAX](using-service-linked-roles.md "using-service-linked-roles.md").

5.  When the settings are as you want them, choose **Next**.
6.  **Parameter group**—Choose **Choose existing**.
7.  **Maintenance window**—Choose **No preference** if you
    don't have a preference when software upgrades are applied, or choose **Specify time window**
    and provide the **Weekday**, **Time(UTC)** and **Start within (hours)**
    options to schedule your maintenance window.
8.  **Tags**—Choose **Add new tag** to enter a key/value pair for tagging purposes.
9.  Choose **Next**.

On the **Review and create** screen, you can review all of the settings. If you are ready to create the cluster,
choose **Create cluster**.

On the **Clusters** screen, your DAX cluster will be listed with a
status of **Creating**.

###### Note

Creating the cluster takes several minutes. When the cluster is ready, its status
changes to **Available**.

In the meantime, proceed to [Step 3: Configure
security group inbound rules using the AWS Management Console](#DAX.create-cluster.console.configure-inbound-rules "#DAX.create-cluster.console.configure-inbound-rules") and follow
the instructions there.

## Step 3: Configure

security group inbound rules using the AWS Management Console

Your Amazon DynamoDB Accelerator (DAX) cluster communicates via TCP port 8111 (for unencrypted
clusters) or 9111 (for encrypted clusters), so you must authorize inbound traffic on
that port. This allows Amazon EC2 instances in your Amazon VPC to access your DAX
cluster.

###### Note

If you launched your DAX cluster with a different security group (other than
`default`), you must perform this procedure for that group
instead.

###### To configure security group inbound rules

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Security Groups**.
3. Choose the **default** security group. On the
   **Actions** menu, choose **Edit inbound
   rules**.
4. Choose **Add Rule**, and enter the following
   information:
   - **Port Range**—Enter **8111**
     (if your cluster is unencrypted) or **9111** (if your cluster is encrypted).
   - **Source**—Leave this as **Custom**, and choose
     the search field to the right. A drop-down menu will be displayed.
     Choose the identifier for your default security group.

5. Choose **Save rules** to save your changes.
6. To update the name in the console, go to the **Name** property and choose the
   **Edit** option that is displayed.
