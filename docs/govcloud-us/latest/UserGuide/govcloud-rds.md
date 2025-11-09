# Amazon RDS in AWS GovCloud (US)

Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

## How Amazon Relational Database Service differs for AWS GovCloud (US)

- Multi-AZ DB clusters aren’t available. However, Multi-AZ DB instances are available.
- Amazon RDS Custom for SQL Server isn’t available.
- Amazon RDS Kerberos authentication for PostgreSQL DB instances is not available.
- Creation of [cross-Region read replicas](../../../AmazonRDS/latest/UserGuide/USER_ReadRepl.md "../../../AmazonRDS/latest/UserGuide/USER_ReadRepl.md") from other AWS Regions to the AWS GovCloud (US) Regions or from AWS GovCloud (US) Regions to other AWS Regions isn’t supported.
- Copying of [DB snapshots](../../../AmazonRDS/latest/UserGuide/USER_CopySnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_CopySnapshot.md") from other AWS Regions to the AWS GovCloud (US) Regions or from AWS GovCloud (US) Regions to other AWS Regions isn’t supported.
- Oracle Management Agent versions 12.1 and 13.1 aren’t available in the AWS GovCloud (US) Regions.
- Intermediate SSL certificates must be used to connect to the AWS GovCloud (US) Regions using SSL. For more information related to Intermediate certificates, see [Using SSL/TLS to Encrypt a Connection](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md").
- Instance types and engine versions might vary in the AWS GovCloud (US) Regions. To determine instance and engine availability, see the [RDS Management Console](../../../https:/console.amazonaws-us-gov.com/rds.md "../../../https:/console.amazonaws-us-gov.com/rds.md") or CLI tools.
- Since the AWS GovCloud (US) Regions use a unique certificate authority (CA), update your DB instances for the AWS GovCloud (US) Regions to use the Region-specific certificate identified by `rds-ca-rsa4096-g1` in [DescribeCertificates](../../../AmazonRDS/latest/APIReference/API_DescribeCertificates.md "../../../AmazonRDS/latest/APIReference/API_DescribeCertificates.md") calls as soon as possible. The remaining instructions described in the [Rotating your SSL/TLS certificate](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md") topic are the same, except for the certificate identifier.
- Copying an option group isn’t available.
- Performance Insights [proactive recommendations](../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.md") and [on-demand analysis](../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.md") aren’t available.
- Zero-ETL integration with SageMaker Lakehouse isn’t available.

## Documentation for Amazon Relational Database Service

[Amazon RDS documentation](http://aws.amazon.com/documentation/rds/ "http://aws.amazon.com/documentation/rds/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon RDS metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your Amazon RDS instances except the master password.
- Do not enter export-controlled data in the following fields:
  - Database instance identifier
  - Master user name
  - Database name
  - Database snapshot name
  - Database security group name
  - Database security group description
  - Database parameter group name
  - Database parameter group description
  - Option group name
  - Option group description
  - Database subnet group name
  - Database subnet group description
  - Event subscription name
  - Resource tags

If you are processing export-controlled data with Amazon RDS, follow these guidelines in order to maintain export compliance:

- When you use the console or the AWS APIs, the only data field that is protected as export-controlled data is the Amazon RDS master password.
- After you create your database, change the master password of your Amazon RDS instance by directly using the database client.
- You can enter export-controlled data into any data fields by using your database client-side tools. Do not pass export-controlled data by using the web service APIs that are provided by Amazon RDS.
- To secure export-controlled data in your VPC, set up access control lists (ACLs) to control traffic entering and exiting your VPC. If you have multiple databases configured with different ports, set up ACLs on all the ports.
  - To prevent this type of attack and to maintain export compliance, use network ACLs to prevent network traffic from exiting the VPC on the database port. For more information, see [Network ACLs](../../../vpc/latest/userguide/VPC_ACLs.md "../../../vpc/latest/userguide/VPC_ACLs.md") in the _Amazon VPC User Guide_.

- For each database instance that contains export-controlled data, ensure that only specific CIDR ranges and Amazon EC2 security groups can access the database instance, especially when an Internet gateway is attached to the VPC. Only allow connections that are from the AWS GovCloud (US) Regions or other export-controlled environments to export-controlled database instances.

If you are processing export-controlled data with this service, use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").
