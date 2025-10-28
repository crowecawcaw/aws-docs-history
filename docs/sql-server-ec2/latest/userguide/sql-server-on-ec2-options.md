# Options to run SQL Server on the AWS Cloud

AWS provides the option to run Microsoft SQL Server in a cloud environment. For developers and database
administrators, running SQL Server in the AWS Cloud is similar to running SQL Server databases in a
data center. There are three primary options to run SQL Server on AWS:

- Microsoft SQL Server on Amazon EC2
- Amazon RDS for Microsoft SQL Server
- Amazon RDS Custom for Microsoft SQL Server
  Your application requirements, database features, functionality, growth capacity, and
  overall architecture complexity will determine which option to choose. Many AWS customers run multiple SQL Server
  database workloads across Amazon RDS and Amazon EC2. For more information on
  how to choose how to run SQL Server on the AWS Cloud, see [Decision
  matrix](../../../prescriptive-guidance/latest/saas-multitenant-managed-postgresql/matrix.md "../../../prescriptive-guidance/latest/saas-multitenant-managed-postgresql/matrix.md") on the AWS Prescriptive Guidance website.

If you are migrating multiple SQL Server databases to AWS, some of them might be a great fit
for Amazon RDS, whereas others might be better suited to run directly on Amazon EC2. You might have
databases that are running on SQL Server Enterprise edition but are a good fit for SQL Server Standard
edition. You may also want to modernize your SQL Server database running on Windows to run on a
Linux operating system to save on cost and licenses.

###### Options

- [SQL Server on Amazon EC2](#sql-server-on-ec2-options-ec2 "#sql-server-on-ec2-options-ec2")
- [RDS for SQL Server](#sql-server-on-ec2-options-rds "#sql-server-on-ec2-options-rds")
- [Amazon RDS Custom](#sql-server-on-ec2-options-rds-custom "#sql-server-on-ec2-options-rds-custom")

## Microsoft SQL Server on Amazon EC2

When to choose Microsoft SQL Server on Amazon EC2:

- You want full control over the database and access to its underlying operating system,
  database installation, and configuration.
- You want to administer your database, including backups and recovery, patching the
  operating system and the database, tuning the operating system and database parameters,
  managing security, and configuring high availability or replication.
- You want to use features and options that aren’t currently supported by Amazon RDS. For more
  information, see [Features not supported and features with limited support](../../../AmazonRDS/latest/UserGuide/CHAP_SQLServer.md#SQLServer.Concepts.General.FeatureNonSupport "../../../AmazonRDS/latest/UserGuide/CHAP_SQLServer.md#SQLServer.Concepts.General.FeatureNonSupport") in the Amazon RDS
  documentation.
- You require a specific SQL Server version that isn’t supported by Amazon RDS. For a list of
  supported versions and editions, see [SQL Server versions on Amazon RDS](../../../AmazonRDS/latest/UserGuide/CHAP_SQLServer.md#SQLServer.Concepts.General.VersionSupport "../../../AmazonRDS/latest/UserGuide/CHAP_SQLServer.md#SQLServer.Concepts.General.VersionSupport") in the _RDS for Microsoft SQL Server User Guide_.
- Your database size and performance requirements exceed the current RDS for Microsoft SQL Server offerings.
  For more information, see [Amazon RDS DB instance storage](../../../AmazonRDS/latest/UserGuide/CHAP_Storage.md "../../../AmazonRDS/latest/UserGuide/CHAP_Storage.md") in the
  _Amazon RDS User Guide_.
- You want to avoid automatic software patches that might not be compliant with your
  applications.
- You want to bring your own license instead of using the RDS for Microsoft SQL Server license-included
  model.
- You want to achieve higher IOPS and storage capacity than the current limits. For more
  information, see [Amazon RDS DB instance storage](../../../AmazonRDS/latest/UserGuide/CHAP_Storage.md "../../../AmazonRDS/latest/UserGuide/CHAP_Storage.md") in the _Amazon RDS User Guide_.

## Amazon RDS for Microsoft SQL Server

RDS for Microsoft SQL Server is a managed database service that simplifies the provisioning and management
of SQL Server on AWS. With Amazon RDS, you can quickly deploy multiple versions and editions of SQL Server ,
with cost-efficient and resizeable compute capacity. You can provision Amazon RDS for SQL Server DB
instances with either General Purpose SSD or Provisioned IOPS SSD storage. Provisioned IOPS SSD
is optimized for I/O-intensive, transactional (OLTP) database workloads.

Amazon RDS manages database administration tasks, including provisioning, backups, software
patching, monitoring, and hardware scaling. Amazon RDS also offers Multi-AZ deployments and read
replicas (for SQL Server Enterprise edition) to provide high availability, performance,
scalability, and reliability for production workloads. For more information, see [Amazon RDS for Microsoft SQL Server](../../../AmazonRDS/latest/UserGuide/CHAP_SQLServer.md "../../../AmazonRDS/latest/UserGuide/CHAP_SQLServer.md").

When to choose RDS for Microsoft SQL Server:

- You want to focus on your business and applications, and you want AWS to take care of
  undifferentiated heavy lifting tasks, such as the provisioning of the database, management of
  backup and recovery tasks, management of security patches, minor SQL Server version upgrades, and
  storage management.
- You want a highly available database solution, and you want to take advantage of the
  push-button, synchronous Multi-AZ replication offered by Amazon RDS, without having to manually set
  up and maintain database mirroring, failover clusters, or Always On availability
  groups.
- You want to pay for the SQL Server license as part of the instance cost on an hourly basis,
  instead of making a large, up front investment.
- Your database size and IOPS requirements are supported by Amazon RDS for SQL Server. See [Amazon RDS DB Instance
  Storage](../../../AmazonRDS/latest/UserGuide/CHAP_Storage.md "../../../AmazonRDS/latest/UserGuide/CHAP_Storage.md") in the AWS documentation for the current maximum limits.
- You don’t want to manage backups or point-in-time recoveries of your database.
- You want to focus on high-level tasks, such as performance tuning and schema
  optimization, instead of the daily administration of the database.
- You want to scale the instance type up or down based on your workload patterns without
  being concerned about licensing complexities.

## Amazon RDS Custom for SQL Server

Amazon RDS Custom for SQL Server is a managed database service for legacy, custom, and packaged
applications that require access to the underlying operating system and database
environment. Amazon RDS Custom for SQL Server automates setup, operation, and scaling of databases in
the AWS Cloud while granting you access to the database and underlying operating system on
Amazon EC2 to configure settings, install patches, and enable native features to meet the
dependent application's requirements. For more information, see [Working with RDS
Custom for SQL Server](../../../AmazonRDS/latest/UserGuide/working-with-custom-sqlserver.md "../../../AmazonRDS/latest/UserGuide/working-with-custom-sqlserver.md") in the _Amazon Relational Database Service User
Guide_.

When to choose Amazon RDS Custom for SQL Server:

- You want the benefits of Amazon RDS, but your requirements include the need to customize
  the underlying operating system and database environment for legacy, custom, and
  packaged applications.
- You need administrative rights to the database and underlying operating
  system.
- You need to install custom database and OS patches and packages.
- You need to configure file systems to share files directly with their
  applications.
