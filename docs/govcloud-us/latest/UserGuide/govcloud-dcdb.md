# Amazon DocumentDB (with MongoDB compatibility) in AWS GovCloud (US)

Amazon DocumentDB (with MongoDB compatibility) is a fast, scalable, highly available, and fully managed document database service that supports MongoDB workloads. As a document database, Amazon DocumentDB makes it easy to store, query, and index JSON data.

Amazon DocumentDB is a non-relational database service designed from the ground-up to give you the performance, scalability, and availability you need when operating mission-critical MongoDB workloads at scale. In Amazon DocumentDB, the storage and
compute are decoupled, allowing each to scale independently. You can increase the read capacity to millions of requests per second by adding up to 15 low latency read replicas in minutes, regardless of the size of your data.

## How Amazon DocumentDB differs for AWS GovCloud (US)

- Copying [cluster snapshots](../../../documentdb/latest/developerguide/backup_restore-copy_cluster_snapshot.md "../../../documentdb/latest/developerguide/backup_restore-copy_cluster_snapshot.md") from other AWS Regions to the AWS GovCloud (US) Regions or from AWS GovCloud (US) Regions to other Regions is not supported.

## Documentation for Amazon DocumentDB

[Amazon DocumentDB documentation](../../../documentdb/latest/developerguide/what-is.md "../../../documentdb/latest/developerguide/what-is.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon DocumentDB metadata is not permitted to contain export-controlled data. This
  metadata includes all configuration data that you enter when creating and
  maintaining your Amazon DocumentDB cluster except the master password.

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

- When you use the console or the AWS APIs, the only data field that is protected as export-controlled data is the Amazon DocumentDB Master Password.
- After you create your cluster, change the master password of your Amazon DocumentDB cluster by directly using the AWS Management Console or AWS CLI.
- You can enter export-controlled data into any data fields by using your database client-side tools. Do not pass export-controlled data by using the web service APIs that are provided by Amazon DocumentDB.
- To secure export-controlled data in your VPC, set up access control lists (ACLs) to control traffic entering and exiting your VPC. If you have multiple databases configured with
  different ports, set up ACLs on all the ports.
  - For example, if you're running an application server on an Amazon EC2 instance that connects to an Amazon DocumentDB cluster, a non-U.S. person could reconfigure the DNS to redirect export-controlled data out of the VPC and into any
    server that might be outside of the AWS GovCloud (US-West) Region.

  To prevent this type of attack and to maintain export compliance, use network ACLs to prevent network traffic from exiting the VPC on the database port. For more
  information, see [Network ACLs](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the _Amazon VPC User Guide_.
  - For each database instance that contains export-controlled data, ensure that only specific CIDR ranges and Amazon EC2 security groups can access the cluster, especially when an Internet gateway is attached to the VPC. Only allow connections
    that are from the AWS GovCloud (US-West) Region or other export-controlled environments to export-controlled clusters.

If you are processing export-controlled data with this service, use the SSL (HTTPS)
endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").
