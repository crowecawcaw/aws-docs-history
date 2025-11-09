# Amazon Aurora with MySQL and PostgreSQL compatibility in AWS GovCloud (US)

Amazon Aurora (Aurora) is a fully managed relational database engine that’s compatible with MySQL and PostgreSQL. You already know how MySQL and PostgreSQL combine the speed and reliability of high-end commercial databases with the simplicity and cost-effectiveness of open-source databases. The code, tools, and applications you use today with your existing MySQL and PostgreSQL databases can be used with Aurora. With some workloads, Aurora can deliver up to five times the throughput of MySQL and up to three times the throughput of PostgreSQL without requiring changes to most of your existing applications.

## How Amazon Aurora differs for AWS GovCloud (US)

- Publishing [Amazon Aurora MySQL Logs](../../../AmazonRDS/latest/UserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/UserGuide/AuroraMySQL.Integrating.md") to Amazon CloudWatch Logs is not supported.
- Creation of [cross-Region read replicas](../../../AmazonRDS/latest/UserGuide/AuroraMySQL.Replication.md "../../../AmazonRDS/latest/UserGuide/AuroraMySQL.Replication.md") from other AWS Regions to the AWS GovCloud (US) Regions or from AWS GovCloud (US) Regions to other AWS Regions isn’t supported.
- Aurora PostgresSQL cross-Region read replicas is not available in AWS GovCloud (US) Regions.
- Copying of [DB Snapshots](../../../AmazonRDS/latest/UserGuide/USER_CopySnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_CopySnapshot.md") from other AWS Regions to the AWS GovCloud (US) Regions or from AWS GovCloud (US) Regions to other AWS Regions isn’t supported.
- Instance types and engine versions might vary in the AWS GovCloud (US) Regions. To determine instance and engine availability, see the [RDS Management Console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") or CLI tools.
- Database activity streams are not supported in AWS GovCloud (US).
- Intermediate SSL certificates must be used to connect to the AWS GovCloud (US) Regions using SSL. For more information related to Intermediate certificates, see [Using SSL/TLS to Encrypt a Connection](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md").
- [Backtracking](../../../AmazonRDS/latest/UserGuide/AuroraMySQL.Managing.md "../../../AmazonRDS/latest/UserGuide/AuroraMySQL.Managing.md") is not available.
- [Aurora Serverless v1](../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless.md") is not available.
- [Aurora MySQL binlog replication](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.md") from other AWS Regions to the AWS GovCloud (US) Regions or from AWS GovCloud (US) Regions to other AWS Regions isn’t supported.
- Since the AWS GovCloud (US) Regions use a unique certificate authority (CA), update your DB clusters for the AWS GovCloud (US) Regions to use the Region-specific certificate identified by `rds-ca-rsa4096-g1` in [DescribeCertificates](../../../AmazonRDS/latest/APIReference/API_DescribeCertificates.md "../../../AmazonRDS/latest/APIReference/API_DescribeCertificates.md") calls as soon as possible. The remaining instructions described in the [Rotating your SSL/TLS certificate](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md") topic are the same, except for the certificate identifier.
- Scaling to 0 capacity with Amazon Aurora Serverless v2 is not available in AWS GovCloud (US) Regions.
- Zero-ETL integration with SageMaker Lakehouse isn’t available.

The following Amazon Aurora editions are supported in AWS GovCloud (US) Regions:

- Amazon Aurora MySQL-compatible edition
- Amazon Aurora PostgreSQL-compatible edition

## Documentation for Amazon Aurora

For more information about Amazon Aurora, see the [Amazon Aurora documentation](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.md "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon RDS metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your Amazon RDS instances except the master password.
- Do not enter export-controlled data in the following fields:
  - Database Cluster Identifier
  - Database instance identifier
  - Master user name
  - Database name
  - Database snapshot name
  - Database security group name
  - Database security group description
  - Database cluster parameter group name
  - Database cluster parameter group description
  - Database subnet group name
  - Database subnet group description
  - Event subscription name
  - Resource tags

If you are processing export-controlled data with Amazon RDS, follow these guidelines in order to maintain export compliance:

- When you use the console or the AWS APIs, the only data field that is protected as export-controlled data is the Amazon RDS Master Password.
- After you create your database, change the master password of your Amazon RDS instance by directly using the database client.
- You can enter export-controlled data into any data fields by using your database client-side tools. Do not pass export-controlled data by using the web service APIs that are provided by Amazon RDS.
- To secure export-controlled data in your VPC, set up access control lists (ACLs) to control traffic entering and exiting your VPC. If you have multiple databases configured with different ports, set up ACLs on all the ports.
  - For example, if you’re running an application server on an Amazon EC2 instance that connects to an Amazon RDS database instance, a non-U.S. person could reconfigure the DNS to redirect export-controlled data out of the VPC and into any server that might be outside of the AWS GovCloud (US-West) Region.

  To prevent this type of attack and to maintain export compliance, use network ACLs to prevent network traffic from exiting the VPC on the database port. For more information, see [Network ACLs](../../../vpc/latest/userguide/VPC_ACLs.md "../../../vpc/latest/userguide/VPC_ACLs.md") in the _Amazon VPC User Guide_.
  - For each database instance that contains export-controlled data, ensure that only specific CIDR ranges and Amazon EC2 security groups can access the database instance, especially when an Internet gateway is attached to the VPC. Only allow connections that are from the AWS GovCloud (US-West) Region or other export-controlled environments to export-controlled database instances.

If you are processing export-controlled data with this service, use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").
