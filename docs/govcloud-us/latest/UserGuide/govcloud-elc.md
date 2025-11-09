# Amazon ElastiCache in AWS GovCloud (US)

Amazon ElastiCache makes it easy to set up, manage, and scale distributed in-memory cache environments in the AWS Cloud. It provides a high performance, resizable, and cost-effective in-memory cache, while removing complexity associated with deploying and managing a distributed cache environment. ElastiCache works with the Valkey, Memcached and Redis OSS engines. To see which works best for you, see the Comparing Valkey, Memcached, and Redis OSS self-designed caches topic in the ElastiCache user guide.

## How Amazon ElastiCache differs for AWS GovCloud (US)

- All ElastiCache instances must be launched in an Amazon VPC.
- ElastiCache clusters have a preferred weekly maintenance window. For information about the time blocks, see [Cache Engine Version Management](../../../AmazonElastiCache/latest/UserGuide/VersionManagement.md "../../../AmazonElastiCache/latest/UserGuide/VersionManagement.md").
- The r6gd node type and data-tiering are not available in AWS GovCloud (US).

## Documentation for Amazon ElastiCache

[Amazon ElastiCache documentation](../../../elasticache.md "../../../elasticache.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Unencrypted data stored in a cache cluster may not contain export-controlled data.
- ElastiCache metadata is not permitted to contain export-controlled data. This metadata includes all the configuration data that you enter when creating and maintaining your ElastiCache clusters.
- Do not enter export-controlled data in the following fields:
  - Cluster instance identifier
  - Cluster name
  - Cluster snapshot name
  - Cluster security group name
  - Cluster security group description
  - Cluster parameter group name
  - Cluster parameter group description
  - Cluster subnet group name
  - Cluster subnet group description
  - Replication group name
  - Replication group description

If you are processing export-controlled data with ElastiCache, follow these guidelines in order to maintain export compliance:

- To secure export-controlled data in your VPC, set up access control lists (ACLs) to control traffic entering and exiting your VPC. If you have multiple databases configured with different ports, set up ACLs on all the ports.
  - For example, if you’re running an application server on an Amazon EC2 instance that connects to an ElastiCache cluster, a non-U.S. person could reconfigure the DNS to redirect export-controlled data out of the VPC and into any server that could possibly be outside of AWS GovCloud (US) Regions
  - To prevent this type of attack and to maintain export compliance, use network ACLs to prevent network traffic from exiting the VPC on the database port. For more information, see [Network ACLs](../../../vpc/latest/userguide/VPC_ACLs.md "../../../vpc/latest/userguide/VPC_ACLs.md") in the Amazon VPC User Guide.

- For each cluster that contains export-controlled data, ensure that only specific CIDR ranges and Amazon EC2 security groups can access the database instance, especially when an Internet gateway is attached to the VPC. Only allow connections that are from AWS GovCloud (US) Regions or other export-controlled environments to export-controlled clusters.

ElastiCache requires the use of the SSL (HTTPS) endpoint for service API calls. For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").
