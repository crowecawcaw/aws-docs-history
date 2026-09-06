

# Amazon Aurora with MySQL and PostgreSQL compatibility in AWS GovCloud (US)
<a name="govcloud-aurora"></a>

Amazon Aurora (Aurora) is a fully managed relational database engine that’s compatible with MySQL and PostgreSQL. You already know how MySQL and PostgreSQL combine the speed and reliability of high-end commercial databases with the simplicity and cost-effectiveness of open-source databases. The code, tools, and applications you use today with your existing MySQL and PostgreSQL databases can be used with Aurora. With some workloads, Aurora can deliver up to five times the throughput of MySQL and up to three times the throughput of PostgreSQL without requiring changes to most of your existing applications.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon Aurora differs
<a name="govcloud-aur-diffs"></a>

The following differences apply to Amazon Aurora:
+ Publishing [Amazon Aurora MySQL Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Integrating.CloudWatch.html) to Amazon CloudWatch Logs is not available.
+ Creation of [cross-Region read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Replication.CrossRegion.html) from other AWS Regions to the AWS GovCloud (US) Regions or from AWS GovCloud (US) Regions to other AWS Regions is not available.
+  Aurora PostgresSQL cross-Region read replicas is not available.
+ Copying of [DB Snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html) from other AWS Regions to the AWS GovCloud (US) Regions or from AWS GovCloud (US) Regions to other AWS Regions is not available.
+ Instance types and engine versions might vary in the AWS GovCloud (US) Regions. To determine instance and engine availability, see the [RDS Management Console](https://console.aws.amazon.com/rds/) or CLI tools.
+ Database activity streams are not available.
+ Intermediate SSL certificates must be used to connect to the AWS GovCloud (US) Regions using SSL. For more information related to Intermediate certificates, see [Using SSL/TLS to Encrypt a Connection](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html).
+  [Backtracking](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Managing.Backtrack.html) is not available.
+  [Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html) is not available.
+  [Aurora MySQL binlog replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.html) from other AWS Regions to the AWS GovCloud (US) Regions or from AWS GovCloud (US) Regions to other AWS Regions is not available.
+ Since the AWS GovCloud (US) Regions use a unique certificate authority (CA), update your DB clusters for the AWS GovCloud (US) Regions to use the Region-specific certificate identified by `rds-ca-rsa4096-g1` in [DescribeCertificates](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeCertificates.html) calls as soon as possible. The remaining instructions described in the [Rotating your SSL/TLS certificate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html) topic are the same, except for the certificate identifier.
+ Scaling to 0 capacity with Amazon Aurora Serverless v2 is not available.
+ Zero-ETL integration with SageMaker Lakehouse isn’t available.

The following Amazon Aurora editions are supported in AWS GovCloud (US) Regions:
+  Amazon Aurora MySQL-compatible edition
+  Amazon Aurora PostgreSQL-compatible edition

## Documentation
<a name="govcloud-aur-docs"></a>
+  [Amazon Aurora documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) 

## Export-controlled content
<a name="govcloud-aurora-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Amazon RDS metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your Amazon RDS instances except the master password.
+ Do not enter export-controlled data in the following fields:
  + Database Cluster Identifier
  + Database instance identifier
  + Master user name
  + Database name
  + Database snapshot name
  + Database security group name
  + Database security group description
  + Database cluster parameter group name
  + Database cluster parameter group description
  + Database subnet group name
  + Database subnet group description
  + Event subscription name
  + Resource tags

If you are processing export-controlled data with Amazon RDS, follow these guidelines in order to maintain export compliance:
+ When you use the console or the AWS APIs, the only data field that is protected as export-controlled data is the Amazon RDS Master Password.
+ After you create your database, change the master password of your Amazon RDS instance by directly using the database client.
+ You can enter export-controlled data into any data fields by using your database client-side tools. Do not pass export-controlled data by using the web service APIs that are provided by Amazon RDS.
+ To secure export-controlled data in your VPC, set up access control lists (ACLs) to control traffic entering and exiting your VPC. If you have multiple databases configured with different ports, set up ACLs on all the ports.
  + For example, if you’re running an application server on an Amazon EC2 instance that connects to an Amazon RDS database instance, a non-U.S. person could reconfigure the DNS to redirect export-controlled data out of the VPC and into any server that might be outside of the AWS GovCloud (US-West) Region.

    To prevent this type of attack and to maintain export compliance, use network ACLs to prevent network traffic from exiting the VPC on the database port. For more information, see [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html) in the *Amazon VPC User Guide*.
  + For each database instance that contains export-controlled data, ensure that only specific CIDR ranges and Amazon EC2 security groups can access the database instance, especially when an Internet gateway is attached to the VPC. Only allow connections that are from the AWS GovCloud (US-West) Region or other export-controlled environments to export-controlled database instances.

If you are processing export-controlled data with this service, use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md).