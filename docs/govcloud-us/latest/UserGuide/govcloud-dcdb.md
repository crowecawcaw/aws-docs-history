

# Amazon DocumentDB (with MongoDB compatibility) in AWS GovCloud (US)
<a name="govcloud-dcdb"></a>

Amazon DocumentDB (with MongoDB compatibility) is a fast, scalable, highly available, and fully managed document database service that supports MongoDB workloads. As a document database, Amazon DocumentDB makes it easy to store, query, and index JSON data.

Amazon DocumentDB is a non-relational database service designed from the ground-up to give you the performance, scalability, and availability you need when operating mission-critical MongoDB workloads at scale. In Amazon DocumentDB, the storage and compute are decoupled, allowing each to scale independently. You can increase the read capacity to millions of requests per second by adding up to 15 low latency read replicas in minutes, regardless of the size of your data.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon DocumentDB differs
<a name="govcloud-dcdb-diffs"></a>

The following differences apply to Amazon DocumentDB:
+ Copying [cluster snapshots](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-copy_cluster_snapshot.html) from other AWS Regions to the AWS GovCloud (US) Regions or from AWS GovCloud (US) Regions to other Regions is not available.
+ Amazon DocumentDB elastic clusters are not available.
+ The db.t4g and db.r4 instance classes are not available.
+ The db.r8g instance class is available in the AWS GovCloud (US-West) Region only and is not available in the AWS GovCloud (US-East) Region.
+ Amazon DocumentDB Performance Insights is not available.

## Documentation
<a name="govcloud-dcdb-docs"></a>
+  [Amazon DocumentDB documentation](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html) 

## Export-controlled content
<a name="govcloud-dcdb-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Amazon DocumentDB metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your Amazon DocumentDB cluster except the master password.

  Do not enter export-controlled data in the following fields:
  + Cluster Identifier
  + Instance identifier
  + Master user name
  + Database name
  + Snapshot name
  + Security group name
  + Security group description
  + Cluster parameter group name
  + Cluster parameter group description
  + Subnet group name
  + Subnet group description
  + Resource tags

If you are processing export-controlled data with Amazon DocumentDB, follow these guidelines in order to maintain export compliance:
+ When you use the console or the AWS APIs, the only data field that is protected as export-controlled data is the Amazon DocumentDB Master Password.
+ After you create your cluster, change the master password of your Amazon DocumentDB cluster by directly using the AWS Management Console or AWS CLI.
+ You can enter export-controlled data into any data fields by using your database client-side tools. Do not pass export-controlled data by using the web service APIs that are provided by Amazon DocumentDB.
+ To secure export-controlled data in your VPC, set up access control lists (ACLs) to control traffic entering and exiting your VPC. If you have multiple databases configured with different ports, set up ACLs on all the ports.
  + For example, if you’re running an application server on an Amazon EC2 instance that connects to an Amazon DocumentDB cluster, a non-U.S. person could reconfigure the DNS to redirect export-controlled data out of the VPC and into any server that might be outside of the AWS GovCloud (US-West) Region.

    To prevent this type of attack and to maintain export compliance, use network ACLs to prevent network traffic from exiting the VPC on the database port. For more information, see [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) in the *Amazon VPC User Guide*.
  + For each database instance that contains export-controlled data, ensure that only specific CIDR ranges and Amazon EC2 security groups can access the cluster, especially when an Internet gateway is attached to the VPC. Only allow connections that are from the AWS GovCloud (US-West) Region or other export-controlled environments to export-controlled clusters.

If you are processing export-controlled data with this service, use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md).