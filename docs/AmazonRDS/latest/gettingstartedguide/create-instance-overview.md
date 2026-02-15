# Creating your first Amazon RDS DB instance

Amazon RDS simplifies the process of setting up and managing relational databases in the cloud.
This walkthrough guides you through creating your first DB instance. By the end, you'll
understand how to configure and manage your RDS DB instance.

###### Topics

- [Creating your first DB instance](#create-instance "#create-instance")
- [Other important settings](#create-instance-important-settings "#create-instance-important-settings")
- [Next steps](#create-instance-next-steps "#create-instance-next-steps")

## Creating your first DB instance

A DB instance in Amazon RDS is the foundational building block for running a managed
relational database in the cloud. This section helps you set up your first RDS DB
instance.

This tutorial walks you through the steps to create a simple RDS for MySQL DB instance
using the **Easy create** option. For comprehensive instructions to
create a production DB instance, see [Creating an Amazon RDS DB
instance](../UserGuide/USER_CreateDBInstance.md "../UserGuide/USER_CreateDBInstance.md") in the _Amazon RDS User Guide_.

###### To create a DB instance using Easy create

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Create database**.

![Orange button labeled "Create database" for setting up an Amazon RDS instance.](images/create-database.png) 3. For the creation method, choose **Easy create**. This method
simplifies database provisioning by automatically configuring settings such as instance
class, storage type, and networking settings.

![Database creation method options: Standard create with full configuration or Easy create with recommended settings.](images/creation-method.png) 4. In this tutorial, we create a MySQL DB instance. For **Engine
type**, choose **MySQL**.

MySQL is a good starting point because it's open-source, cost-effective, and widely
supported by the development community. For a full list of supported database engines,
see [Choosing your database engine for Amazon RDS](choosing-engine.md "choosing-engine.md"). 5. For **DB instance size**, choose **Free tier**
or **Sandbox**. **Free
tier** appears for free plan accounts. **Sandbox** appears for paid plan accounts. The **Free
tier** option lets you complete the tutorial without incurring costs, so
it's ideal for learning and experimentation.

If you were an AWS Free Tier customer before July 17, 2025 and your usage
exceeds the free tier limits or you select resources not covered by the free tier,
you're billed at the listed hourly rate.

The following screenshot shows the **Free tier** option.

![DB instance size options showing Production, Dev/Test, and Free tier with specifications.](images/instance-size.png) 6. (Optional) For **DB instance identifier**, enter a name for the
DB instance. Alternately, keep the name that Amazon RDS generates for you. 7. For **Credentials management**, select
**Self-managed**. This option lets you manage your own master user
credentials.

![Credentials management options: AWS Secrets Manager or self-managed master user credentials.](images/cred-management.png) 8. For **Master password**, enter a password for the master user and
confirm the password. 9. Expand **View default settings for Easy create** and review the
settings that Amazon RDS automatically configures for you. You can modify some settings, such
as public access and the engine version, after you create the DB instance. 10. Choose **Create database**.

The database appears in the **Databases** list with a status of
`Creating`. When the status changes to `Available`, the DB
instance is ready to use.
The following command creates a simple RDS for MySQL DB instance using the AWS CLI. The
command replicates the **Easy create** option from the RDS
console, which default settings for development and experimentation. For
production-ready configurations, see [Creating an Amazon RDS DB
instance](../UserGuide/USER_CreateDBInstance.md "../UserGuide/USER_CreateDBInstance.md") in the _Amazon RDS User Guide_.

First, install and configure the AWS CLI. For instructions, see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the
_AWS Command Line Interface User Guide_.

Then, run the following command:

###### Example

```
aws rds create-db-instance \
  --db-instance-identifier `my-db-instance` \
  --db-instance-class db.t4g.micro \
  --engine mysql \
  --master-username `my-username` \
  --master-user-password `my-password` \
  --allocated-storage 20 \
  --no-publicly-accessible \
  --backup-retention-period 7 \
  --storage-type gp2 \
  --engine-version 8.0.39
```

Replace the placeholders values for the instance identifier, username, and
password with your own values.

## Other important settings

Although the **Easy create** option simplifies the process of creating
a DB instance, using the **Standard create** workflow offers more control
and customization over your DB instance configuration. Consider the following important
settings when you create a production DB instance.

###### Topics

- [Storage allocation](#create-instance-important-storage "#create-instance-important-storage")
- [Instance class](#create-instance-important-class "#create-instance-important-class")
- [Public access](#create-instance-important-public "#create-instance-important-public")

### Storage allocation

In the Standard create workflow, you must specify the amount of storage for your DB
instance. The type of storage, such as General Purpose SSD, Provisioned IOPS, or Magnetic,
and the allocated size directly affect your database performance and cost.

- For most workloads, General Purpose SSD provides a balance between cost and
  performance.
- High-performance transactional applications benefit from Provisioned IOPS
  SSD.

![Storage options including Provisioned IOPS SSD (io2) and General Purpose SSD (gp3) with descriptions.](images/storage.png)

For more information, see [Amazon RDS DB instance
storage](../UserGuide/CHAP_Storage.md "../UserGuide/CHAP_Storage.md") in the _Amazon RDS User Guide_.

### Instance class

The instance class determines the allocated compute and memory capacity for your
database. Selecting the right class depends on factors such as the expected workload,
query volume, and application requirements.

- **Standard classes** are ideal for general-purpose
  workloads.
- **Memory-optimized classes** are best for
  applications that require high memory throughput.
- **Burstable classes** work well for applications with
  intermittent workloads.

![Instance configuration options for DB class selection, including standard and optimized classes.](images/instance-class.png)

For detailed guidance, see [DB instance
classes](../UserGuide/Concepts.md "../UserGuide/Concepts.md") in the _Amazon RDS User Guide_.

### Public access

Public access controls whether users or applications can access your DB instance from
outside the VPC. This setting is critical for managing connectivity and security.

- **Enable public access** to make your database
  accessible from external networks, such as for web applications or remote access.
  Configure security group rules to restrict unwanted access.
- **Disable public access** for internal applications
  or enhanced security, limiting connectivity to instances within your VPC.

![Public access options for RDS cluster with Yes and No choices and their implications.](images/public-access.png)

For more information about configuring public or private access and related network
settings, see [Working with
a DB instance in a VPC](../UserGuide/USER_VPC.md "../UserGuide/USER_VPC.md") in the _Amazon RDS User Guide_.

## Next steps

Now that you created your first RDS DB instance, the next step is to make sure that it's
secure. Proper security configurations help protect your database and its data from
unauthorized access.

In the next section, you'll learn about the following:

- Setting up public or private access.
- Configuring security groups and network settings.
- Managing database authentication and access controls.

**Next step**: [Securing your Amazon RDS DB instance](security.md "security.md")
