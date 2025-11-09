# Using Amazon DocumentDB elastic clusters

Amazon DocumentDB elastic clusters support workloads with millions of reads/writes per second and petabytes of storage capacity.
Elastic clusters also simplify how developers interact with Amazon DocumentDB by eliminating the need to choose, manage or upgrade instances.

Amazon DocumentDB elastic clusters were created to:

- Provide a solution for customers looking for a database that provides virtually limitless scale with rich query capabilities and MongoDB API compatibility.
- Give customers higher connection limits, and to reduce downtime from patching.
- Continue investing in a cloud-native, elastic, and class leading architecture for JSON workloads.

###### Topics

- [Elastic cluster use cases](#elastic-use-cases "#elastic-use-cases")
- [Advantages of elastic clusters](#elastic-advantages "#elastic-advantages")
- [Elastic cluster region and version availability](#elastic-region-version "#elastic-region-version")
- [Limitations](#elastic-limitations "#elastic-limitations")
- [Amazon DocumentDB elastic clusters: how it works](elastic-how-it-works.md "elastic-how-it-works.md")
- [Get started with Amazon DocumentDB elastic clusters](elastic-get-started.md "elastic-get-started.md")
- [Amazon DocumentDB elastic cluster best practices](elastic-best-practices.md "elastic-best-practices.md")
- [Managing Amazon DocumentDB elastic clusters](elastic-managing.md "elastic-managing.md")
- [Data encryption at rest for Amazon DocumentDB elastic clusters](elastic-encryption.md "elastic-encryption.md")
- [Service-linked roles in elastic clusters](elastic-service-linked-roles.md "elastic-service-linked-roles.md")

## Elastic cluster use cases

Document databases are useful for workloads that require a flexible schema for fast, iterative development.
For example Amazon DocumentDB use cases, see [Document database use Cases](document-database-use-cases.md "document-database-use-cases.md").

The following are some examples of use cases for which elastic clusters can provide significant advantages:

### User profiles

Because document databases have a flexible schema, they can store documents that have different attributes and data values at scale.
Elastic clusters are a practical solution to online profiles in which different users provide different types of information.
Suppose that your applications support hundreds of millions of user profiles.
You can use elastic clusters to support such applications because they can be scaled up and out to support millions of writes and reads to these user profiles.
You can also scale down for off-peak hours to reduce cost.

### Content management and historical records

To effectively manage content, you must be able to collect and aggregate content from a variety of sources, and then deliver it to the customer.
Due to their flexible schema, document databases are perfect for collecting and storing any type of data.
You can use them to create and incorporate new types of content, including user-generated content such as images, comments, and videos.
Over time, your database may require more storage.
With elastic clusters, you can distribute your data over more storage volumes enabling you to store petabytes of data in a single cluster.

## Advantages of elastic clusters

### AWS service integration

Amazon DocumentDB elastic clusters integrate with other AWS services in the same way Amazon DocumentDB does:

- **Migration** — You can use AWS Database Migration Service (DMS) to migrate from MongoDB and other relational databases to Amazon DocumentDB elastic clusters.
- **Monitoring** — You can monitor the health and performance of your elastic cluster using Amazon CloudWatch.
- **Security** — You can set up authentication and authorization through AWS Identity and Access Management (IAM) to manage your elastic cluster resources such as creating and updating an elastic cluster, and use Amazon VPC for secure VPC-only connections.
  IAM authentication login for elastic clusters is not supported.
- **Data management** — You can use AWS Glue to import and export data from/to other AWS services such as Amazon S3, Amazon Redshift and Amazon OpenSearch Service.

## Elastic cluster region and version availability

### Region availability for elastic clusters

The following table shows the AWS regions where Amazon DocumentDB elastic clusters are currently available and the endpoint for each region.

| Region name               | Region           | Availability zones |
| ------------------------- | ---------------- | ------------------ |
| US East (N. Virginia)     | `us-east-1`      | 5                  |
| US East (Ohio)            | `us-east-2`      | 3                  |
| US West (Oregon)          | `us-west-2`      | 3                  |
| Asia Pacific (Hong Kong)  | `ap-east-1`      | 3                  |
| Asia Pacific (Mumbai)     | `ap-south-1`     | 3                  |
| Asia Pacific (Seoul)      | `ap-northeast-2` | 3                  |
| Asia Pacific (Singapore)  | `ap-southeast-1` | 3                  |
| Asia Pacific (Sydney)     | `ap-southeast-2` | 3                  |
| Asia Pacific (Tokyo)      | `ap-northeast-1` | 3                  |
| Canada (Central)          | `ca-central-1`   | 3                  |
| South America (São Paulo) | `sa-east-1`      | 3                  |
| Europe (Frankfurt)        | `eu-central-1`   | 3                  |
| Europe (Ireland)          | `eu-west-1`      | 3                  |
| Europe (London)           | `eu-west-2`      | 3                  |
| Europe (Milan)            | `eu-south-1`     | 3                  |
| Europe (Paris)            | `eu-west-3`      | 3                  |

### Version availability

Elastic clusters support the MongoDB 5.0-compatable wire protocol.
For differences between Amazon DocumentDB 4.0 instance-based clusters and elastic clusters, see [Functional differences between Amazon DocumentDB 4.0 and elastic clusters](elastic-how-it-works.md#elastic-functional-differences "elastic-how-it-works.md#elastic-functional-differences").

## Limitations

### Elastic cluster management

The following cluster management features and capabilities are not supported in this release:

- Custom port (only 27017 is supported)
- Ability to use IAM users and roles to authenticate into the database
- Ability to create global clusters
- Existing Amazon DocumentDB events and subscribing to events
- Range sharding
- Shard existing collection
- Multi-field shard key
- Change shard key
- Point-in-time restore
- Cloning
- Performance Insights

###### Note

For information about elastic cluster limits, see [Amazon DocumentDB Quotas and limits](limits.md "limits.md").

### Query and write operations

The following query and write operation commands and capabilities are not supported in this release:

- DDL commands during scaling operations
- Profiler
- Parameter groups
- AWS Config
- AWS Backup

### Collection and index management

The following collection and index management features are not supported in this release:

- Unique indexes
- Partial indexes
- Text indexes
- Vector indexes
- Document compression

### Administration and diagnostics

The following administration and diagnostic commands and capabilities are not supported in this release:

- AWS Secrets Manager
- Role-based-access-control (RBAC) custom roles.
- When connecting, write concern of 0 is not supported.
- Changing subnets belonging to an VPC that is not currently assigned to an existing elastic cluster.

### Opt-in features

The following Amazon DocumentDB opt-in features are not supported in this release:

- ACID transactions
- DDL/DML auditing
- Change streams
- Session commands
