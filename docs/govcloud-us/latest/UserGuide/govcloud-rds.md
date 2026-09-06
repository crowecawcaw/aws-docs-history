

# Amazon Relational Database Service (Amazon RDS) in AWS GovCloud (US)
<a name="govcloud-rds"></a>

Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon Relational Database Service differs
<a name="govcloud-rds-diffs"></a>

The following differences apply to Amazon Relational Database Service:
+ Multi-AZ DB clusters are not available. However, Multi-AZ DB instances are available.
+  Amazon RDS Custom for SQL Server isn’t available.
+ Creation of [cross-Region read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.XRgn.html) from other AWS Regions to the AWS GovCloud (US) Regions or from AWS GovCloud (US) Regions to other AWS Regions is not available.
+ Copying of [DB snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html) from other AWS Regions to the AWS GovCloud (US) Regions or from AWS GovCloud (US) Regions to other AWS Regions is not available.
+ Oracle Management Agent versions 12.1 and 13.1 are not available.
+ Intermediate SSL certificates must be used to connect to the AWS GovCloud (US) Regions using SSL. For more information related to Intermediate certificates, see [Using SSL/TLS to Encrypt a Connection](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html).
+ Instance types and engine versions might vary in the AWS GovCloud (US) Regions. To determine instance and engine availability, see the [RDS Management Console](https://console.amazonaws-us-gov.com/rds/) or CLI tools.
+ Since the AWS GovCloud (US) Regions use a unique certificate authority (CA), update your DB instances for the AWS GovCloud (US) Regions to use the Region-specific certificate identified by `rds-ca-rsa4096-g1` in [DescribeCertificates](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeCertificates.html) calls as soon as possible. The remaining instructions described in the [Rotating your SSL/TLS certificate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html) topic are the same, except for the certificate identifier.
+ Copying an option group isn’t available.
+ Performance Insights [proactive recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.InsightsRecommendationViewDetails.html) are not available.
+ Zero-ETL integration with SageMaker Lakehouse isn’t available.
+ Amazon RDS for Db2 is available with Bring Your Own License (BYOL) only. Db2 licensing through AWS Marketplace is not available in the AWS GovCloud (US) Regions.

## Documentation
<a name="govcloud-rds-docs"></a>
+  [Amazon RDS documentation](http://aws.amazon.com/documentation/rds/) 

## Export-controlled content
<a name="rds-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Amazon RDS metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your Amazon RDS instances except the master password.
+ Do not enter export-controlled data in the following fields:
  + Database instance identifier
  + Master user name
  + Database name
  + Database snapshot name
  + Database security group name
  + Database security group description
  + Database parameter group name
  + Database parameter group description
  + Option group name
  + Option group description
  + Database subnet group name
  + Database subnet group description
  + Event subscription name
  + Resource tags

If you are processing export-controlled data with Amazon RDS, follow these guidelines in order to maintain export compliance:
+ When you use the console or the AWS APIs, the only data field that is protected as export-controlled data is the Amazon RDS master password.
+ After you create your database, change the master password of your Amazon RDS instance by directly using the database client.
+ You can enter export-controlled data into any data fields by using your database client-side tools. Do not pass export-controlled data by using the web service APIs that are provided by Amazon RDS.
+ To secure export-controlled data in your VPC, set up access control lists (ACLs) to control traffic entering and exiting your VPC. If you have multiple databases configured with different ports, set up ACLs on all the ports.
  + To prevent this type of attack and to maintain export compliance, use network ACLs to prevent network traffic from exiting the VPC on the database port. For more information, see [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html) in the *Amazon VPC User Guide*.
+ For each database instance that contains export-controlled data, ensure that only specific CIDR ranges and Amazon EC2 security groups can access the database instance, especially when an Internet gateway is attached to the VPC. Only allow connections that are from the AWS GovCloud (US) Regions or other export-controlled environments to export-controlled database instances.

If you are processing export-controlled data with this service, use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md).