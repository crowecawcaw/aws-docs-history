# Key concepts and architecture of Amazon RDS

Amazon RDS is a fully managed service that simplifies the deployment and management of relational
databases in the cloud. It supports multiple database engines and automates tasks like
provisioning, patching, backups, and scaling so you can focus on application development.

RDS includes features such as Multi-AZ deployments, automated backups, and resource scaling.
Understanding these key concepts and architectural components is important for optimizing
performance, security, and availability.

###### Topics

- [Architecture](#architecture "#architecture")
- [Features](#features "#features")
- [Supported database engines](#supported-engines "#supported-engines")

## Architecture

Amazon RDS is built on a distributed architecture designed to provide scalability, availability,
and reliability for your database workloads.

**Database instances**

A database instance (DB instance) provides the underlying infrastructure for your
database. It includes compute (CPU and memory), storage, and IOPS, all managed by AWS.
You're responsible for your database software and configurations, while AWS handles
hardware provisioning, maintenance, and backups.

For more information, see [Amazon RDS DB instances](../UserGuide/Overview.md "../UserGuide/Overview.md").

**Multi-Availability Zone deployments**

For high availability, RDS can deploy a database across multiple Availability Zones
(AZs). RDS replicates the primary database instance in one AZ to a standby instance in
another AZ. In the event of failure, RDS automatically switches to the standby instance,
which ensures minimal downtime.

For more information, see [Configuring and managing a Multi-AZ
deployment for Amazon RDS](../UserGuide/Concepts.md "../UserGuide/Concepts.md").

**Storage**

RDS provides multiple storage options, including General Purpose, Provisioned IOPS, and
Magnetic storage, to meet different performance needs. Storage automatically scales as
needed, and replication provides data durability.

For more information, see [Amazon RDS DB instance storage](../UserGuide/CHAP_Storage.md "../UserGuide/CHAP_Storage.md").

**Network integration**

You can launch RDS instances within a Virtual Private Cloud (VPC), which lets you define
network configurations and isolate your database in a secure environment. VPC integration
also provides secure communication with other AWS resources like EC2 instances, Lambda
functions, and S3 buckets.

For more information, see [Amazon VPC and Amazon RDS](../UserGuide/USER_VPC.md "../UserGuide/USER_VPC.md").

## Features

RDS includes a broad set of features that make database management easier and more
efficient.

**Automated backups and snapshots**

RDS automatically takes daily backups of your DB instance, retaining backup data for a
configurable retention period. You can take manual snapshots in order to preserve a
point-in-time backup of your database, which you can later restore to create a new
instance.

For more information, see [Introduction to backups](../UserGuide/USER_WorkingWithAutomatedBackups.md "../UserGuide/USER_WorkingWithAutomatedBackups.md").

**Scalability**

RDS supports both vertical and horizontal scaling. To scale vertically, modify your
instance type to handle increased database load. To scale horizontally, create read replicas
to distribute read traffic across multiple instances and improve performance.

For more information, see [Working with storage for Amazon RDS DB instances](../UserGuide/USER_PIOPS.md "../UserGuide/USER_PIOPS.md").

**Security**

RDS provides security features to safeguard your data and manage access. It supports
encryption at rest and in transit using SSL and AWS Key Management Service (AWS KMS). RDS integrates with
AWS Identity and Access Management (IAM) to control access to DB instances. It also supports Kerberos authentication
for centralized and secure user authentication. Additionally, RDS integrates with AWS Secrets Manager
to securely manage and rotate database credentials, which minimizes the risks of hard-coded
secrets. You can isolate RDS instances within a Virtual Private Cloud (VPC), and use security
groups and network access control lists (ACLs) for fine-grained network access
control.

For more information, see [Security in Amazon RDS](../UserGuide/UsingWithRDS.md "../UserGuide/UsingWithRDS.md").

**Blue/Green Deployments**

RDS Blue/Green Deployments help you safely deploy application updates or new
configurations by running two separate environments (blue and green). This method reduces
downtime and minimizes risks during the deployment process.

For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](../UserGuide/blue-green-deployments.md "../UserGuide/blue-green-deployments.md").

**RDS Custom**

With RDS Custom, you can run custom database engines on Amazon RDS. It provides full control
over database configurations and extensions while benefiting from the scalability and
management features of RDS. It’s ideal for workloads that require more flexibility than
standard RDS instances.

For more information, see [Amazon RDS Custom](../UserGuide/rds-custom.md "../UserGuide/rds-custom.md").

**RDS Proxy**

RDS Proxy is a fully managed, highly available database proxy that sits between your
application and the RDS database. It helps improve application scalability, availability, and
security by managing database connections efficiently, reducing the load on your database and
minimizing connection overhead.

For more information, see [Amazon RDS Proxy](../UserGuide/rds-proxy.md "../UserGuide/rds-proxy.md").

**Zero-ETL integrations**

RDS supports zero-ETL integrations, which provide data movement between your RDS
databases and Amazon Redshift without the need for complex extraction, transformation, and loading (ETL)
processes. This simplifies data integration workflows and accelerates analytics.

For more information, see [Amazon RDS zero-ETL integrations with Amazon Redshift](../UserGuide/zero-etl.md "../UserGuide/zero-etl.md").

**Monitoring and Performance Insights**

RDS provides monitoring through Amazon CloudWatch, which tracks key metrics such as CPU usage,
storage space, and I/O activity. RDS Performance Insights offers deeper visibility into
database performance, helping you identify bottlenecks and optimize queries.

For more information, see [Monitoring metrics in an Amazon RDS instance](../UserGuide/CHAP_Monitoring.md "../UserGuide/CHAP_Monitoring.md").

**Maintenance and patching**

RDS manages software patching automatically within a specified maintenance window. This
ensures that your DB instances stay up-to-date with the latest security patches and feature
improvements without requiring manual intervention.

For more information, see [Maintaining a DB instance](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md").

**Cross-Region replication**

RDS supports cross-Region replication, so you can replicate your data to a different
AWS Region for disaster recovery, data locality, and compliance purposes. You can use this
feature to create global, low-latency applications.

For more information, see [Creating a read replica in a
different AWS Region](../UserGuide/USER_ReadRepl.md "../UserGuide/USER_ReadRepl.md").

## Supported database engines

Amazon RDS supports the following database engines, so you can choose the right database
technology for your application needs.

- [MySQL](https://www.mysql.com/ "https://www.mysql.com/") – Popular for web applications,
  offering compatibility with many tools and frameworks.
- [PostgreSQL](https://www.postgresql.org/ "https://www.postgresql.org/") – Known for advanced
  features, strong standards compliance, and extensibility.
- [MariaDB](https://mariadb.org/ "https://mariadb.org/") – An open-source fork of MySQL,
  offering additional features and high compatibility.
- [Oracle](https://www.oracle.com/database/ "https://www.oracle.com/database/") – Provides
  enterprise-grade capabilities, including advanced performance, security, and high
  availability.
- [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server "https://www.microsoft.com/en-us/sql-server")
  – Suited for organizations relying on Microsoft technologies, offering analytics and
  Business Intelligence (BI) integration.
- [IBM Db2](https://www.ibm.com/db2 "https://www.ibm.com/db2") – A database for enterprise
  applications, known for its scalability and advanced analytics.

Each engine comes with multiple versions and configurations, so you can align with your
existing application requirements or take advantage of newer features.

This guide helps you select and configure a database engine during the setup process and
provides links to resources for engine-specific optimization and features.
