# Amazon DocumentDB migration runbook

This runbook provides a comprehensive guide for migrating a MongoDB database to Amazon DocumentDB using AWS Database Migration Service (DMS).
It is designed to support database administrators, cloud engineers, and developers throughout the end-to-end migration journey—from initial discovery to post-migration validation.

Given the differences in implementation and supported features between MongoDB and Amazon DocumentDB, this runbook emphasizes a structured and systematic approach.
It outlines essential pre-migration assessments, highlights compatibility considerations, and details the key tasks required to ensure a successful migration with minimal disruption.

The runbook is organized into the following topics:

- **[Compatibility](#mig-runbook-compatibility "#mig-runbook-compatibility")** — Understand the supported MongoDB features and data types in Amazon DocumentDB, and identify potential incompatibilities.
- **[Workload discovery](#mig-runbook-workload "#mig-runbook-workload")** — Analyze existing MongoDB workloads, including read/write patterns, data volumes, and performance baselines.
- **[Index migration](#mig-runbook-index "#mig-runbook-index")** — Analyze strategies for extracting and transforming MongoDB indexes for optimal performance in Amazon DocumentDB.
- **[User migration](#mig-runbook-user "#mig-runbook-user")** — Detail the approach for migrating database users, roles, and access controls to Amazon DocumentDB.
- **[Data migration](#mig-runbook-data "#mig-runbook-data")** — Cover various methods for data migration using AWS DMS, including full load and change data capture (CDC).
- **[Monitoring](#mig-runbook-monitoring "#mig-runbook-monitoring")** — Detail various monitoring approaches when migrating using DMS or native tools.
- **[Validation](#mig-runbook-validation "#mig-runbook-validation")** — Provide procedures for data integrity checks, functional validation, and performance comparison post-migration.
  By following the guidance in this runbook, teams can ensure a smooth, secure, and efficient transition to Amazon DocumentDB, while preserving application functionality and minimizing risk.

## Compatibility

###### Topics

- [Core feature compatibility](#w5aac23b9c13c13 "#w5aac23b9c13c13")
- [Amazon DocumentDB compatibility assessment tool](#w5aac23b9c13c15 "#w5aac23b9c13c15")

When migrating from MongoDB to Amazon DocumentDB, a thorough initial assessment and feature compatibility check is essential for a successful migration.
This process begins with a comprehensive inventory of your MongoDB features, including aggregation pipeline operators, query patterns, indexes, and data models.

Since Amazon DocumentDB is compatible with MongoDB 3.6, 4.0, and 5.0 API's, applications using newer MongoDB-specific features may require refactoring.
Critical areas to evaluate include sharding mechanisms(Amazon DocumentDB uses a different approach), transaction implementations, change streams functionality, and index types (particularly sparse and partial indexes).

Performance characteristics also differ, with Amazon DocumentDB optimized for enterprise workloads with predictable performance.
Testing should involve running representative workloads against both systems to identify query patterns that might need optimization.

Monitoring execution plans to detect potential performance gaps is important during the assessment phase.
This helps create a clear migration roadmap, identifying necessary application changes and establishing realistic timelines for a smooth transition.

### Core feature compatibility

#### Comprehensive feature support

- **CRUD operations** — Enjoy full support for all basic create, read, update, and delete operations, including bulk and query operators - providing seamless application compatibility.
- **Rich indexing capabilities** — Leverage comprehensive support for single field, compound, TTL, partial, sparse, and 2dsphere indexes, to optimize your query performance and text indexes (version 5) for text-based lookups.
- **Enterprise-grade replication** — Benefit from a robust automatic failover mechanism with read replicas for superior high availability without operational overhead.
- **Advanced backup solutions** — Rest easy with automated backup system featuring Point-in-Time Recovery (PITR) and on-demand manual snapshots for data protection.

#### Enhanced AWS-integrated features

- **Streamlined aggregation** — Take advantage of the most commonly used aggregation stages (`$match`, `$group`, `$sort`, `$project`, etc.) with optimized performance for enterprise workloads.
- **Transaction support** — Implement multi-document and multi-collection transactions, perfect for most business application needs.
- **Real-time data tracking** — Enable change streams by a simple command and increase change stream retention period through a simple parameter group setting for real-time data change monitoring.
- **Location-based services** — Implement geospatial applications with support for `$geoNear` operator and 2dsphere indexes.
- **Text search capabilities** — Utilize built-in text search functionality for content discovery needs.

#### Modern architecture advantages

- **Cloud-native design** — Enjoy AWS-optimized architecture that replaces legacy features like MapReduce with more efficient aggregation pipeline operations.
- **Enhanced security** — Benefit from AWS Identity and Access Management (IAM), SCRAM-SHA-1, SCRAM-SHA-256, X.509 certificate authentication, and password-based authentication.
- **Predictable performance** — Experience consistent performance optimized specifically for enterprise workloads.

For a comprehensive overview of Amazon DocumentDB's capabilities, refer to the [Supported MongoDB APIs, operations, and data types in Amazon DocumentDB](mongo-apis.md "mongo-apis.md") and [Functional differences: Amazon DocumentDB and MongoDB](functional-differences.md "functional-differences.md") to maximize your database's potential.

Amazon DocumentDB does not support all the indexes offered by MongoDB. We provide a free [index tool](https://github.com/awslabs/amazon-documentdb-tools/blob/master/index-tool/README.md "https://github.com/awslabs/amazon-documentdb-tools/blob/master/index-tool/README.md") to check the compatibility.
We recommend running the index tool to assess incompatibility and plan workarounds accordingly.

### Amazon DocumentDB compatibility assessment tool

The [MongoDB to Amazon DocumentDB Compatibility Tool](https://github.com/awslabs/amazon-documentdb-tools/blob/master/compat-tool/README.md "https://github.com/awslabs/amazon-documentdb-tools/blob/master/compat-tool/README.md") is an open-source utility available on GitHub that helps evaluate MongoDB workload compatibility with Amazon DocumentDB by analyzing MongoDB logs or application source code.

**Key features**

- Identifies MongoDB API usage patterns in your workload
- Flags potential compatibility issues before migration
- Generates detailed compatibility reports with recommendations
- Available as a standalone utility that can be run locally

#### Assessment methods

**Log-based assessment**

- Pros:
  - Captures actual runtime behavior and query patterns
  - Identifies real-world usage frequencies and performance characteristics
  - Detects dynamic queries that might not be visible in source code
  - No access to application source code required

- Cons:
  - Requires access to MongoDB logs with profiling enabled
  - Only captures operations that occurred during the logging period
  - May miss infrequently used features or seasonal workloads

**Source code analysis**

- Pros:
  - Comprehensive coverage of all potential MongoDB operations in the codebase
  - Can identify issues in rarely executed code paths
  - Detects client-side logic that might be affected by Amazon DocumentDB differences
  - No need to run the application to perform assessment

- Cons:
  - May flag code that exists but is never executed in production
  - Requires access to complete application source code
  - Limited ability to analyze dynamically constructed queries

For best results, we recommend using both assessment methods when possible to get a complete picture of compatibility challenges before migration.

## Workload discovery

Migrating from MongoDB to Amazon DocumentDB requires a thorough understanding of the existing database workload.
Workload discovery is the process of analyzing your database usage patterns, data structures, query performance, and operational dependencies to ensure a seamless transition with minimal disruption.
This section outlines the key steps involved in workload discovery to facilitate an effective migration from MongoDB to Amazon DocumentDB.

###### Topics

- [Assessing the existing MongoDB deployment](#w5aac23b9c15b7 "#w5aac23b9c15b7")
- [Identifying data model differences](#w5aac23b9c15b9 "#w5aac23b9c15b9")
- [Query and performance analysis](#w5aac23b9c15c11 "#w5aac23b9c15c11")
- [Security and access control review](#w5aac23b9c15c13 "#w5aac23b9c15c13")
- [Operational and monitoring considerations](#w5aac23b9c15c15 "#w5aac23b9c15c15")

### Assessing the existing MongoDB deployment

Before migration, it is crucial to evaluate the current MongoDB environment, including:

- **Cluster architecture** — Identify the number of nodes, replica sets, and sharding configurations.
  When migrating from MongoDB to Amazon DocumentDB, understanding your MongoDB sharding configuration is important because Amazon DocumentDB does not support user-controlled sharding.
  Applications designed for a sharded MongoDB environment will need architectural changes, as Amazon DocumentDB uses a different scaling approach with its storage-based architecture.
  You'll need to adapt your data distribution strategy and possibly consolidate sharded collections when moving to Amazon DocumentDB.
- **Storage and data volume** — Measure the total data size and index size of your cluster.
  Complement this with the [Oplog review tool](https://github.com/awslabs/amazon-documentdb-tools/tree/master/migration/mongodb-oplog-review "https://github.com/awslabs/amazon-documentdb-tools/tree/master/migration/mongodb-oplog-review") to understand write patterns and data growth velocity.
  For more information about sizing your cluster, see [Instance sizing](best_practices.md#best_practices-instance_sizing "best_practices.md#best_practices-instance_sizing").
- **Workload patterns** — Analyze read and write throughput, query execution frequency, and indexing efficiency.
- **Operational dependencies** — Document all applications, services, and integrations relying on MongoDB.

### Identifying data model differences

Although Amazon DocumentDB is MongoDB-compatible, there are differences in supported features, such as:

- **Transactions** — Amazon DocumentDB supports ACID transactions but with some [Limitations](transactions.md#transactions-limitations "transactions.md#transactions-limitations").
- **Schema design** — Ensure that document structures, embedded documents, and references align with [Amazon DocumentDB’s best practices](https://d1.awsstatic.com/product-marketing/Data%20modeling%20with%20Amazon%20DocumentDB.pdf "https://d1.awsstatic.com/product-marketing/Data%20modeling%20with%20Amazon%20DocumentDB.pdf").

### Query and performance analysis

Understanding query behavior helps optimize migration and post-migration performance. Key areas to analyze include:

- **Slow queries** — Identify queries with high execution time using MongoDB’s profiling tools.
- **Query patterns** — Categorize common query types, including CRUD operations and aggregations.
- **Index usage** — Assess whether indexes are effectively utilized or need optimization in Amazon DocumentDB.
  To assess index usage and optimize performance in Amazon DocumentDB, use the `$indexStats` aggregation pipeline stage combined with the `explain()` method on your critical queries.
  Start by running `db.collection.aggregate([{$indexStats{}}])` to identify which indexes are being used.
  You can do more detailed analysis by executing you most frequent queries with `explainPlan`.
- **Concurrency & workload distribution** — Evaluate read and write ratios, connection pooling, and performance bottlenecks.

### Security and access control review

**Authentication and authorization**

- **MongoDB RBAC to Amazon DocumentDB IAM and RBAC** — Map MongoDB's role-based access control users and roles to AWS Identity and Access Management (IAM) policies and Amazon DocumentDB SCRAM authentication users.
- **User migration strategy** — Plan for migrating database users, custom roles, and privileges to Amazon DocumentDB's supported authentication mechanisms.
- **Privilege differences** — Identify MongoDB privileges without direct Amazon DocumentDB equivalents (for example, cluster administration roles).
- **Application authentication** — Update connection strings and credential management for Amazon DocumentDB's password policies.
  You can use secrets manager to store your credentials and rotate passwords.
- **Service account management** — Establish processes for managing service account credentials in AWS Secrets Manager.
- **Least privilege implementation** — Review and refine access controls to implement least privilege principles in the new environment.

**Encryption**

Ensure encryption at rest and in transit aligns with compliance requirements.

**Network configuration**

Plan for [Virtual Private Cloud (VPC)](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") setup and security group rules.

### Operational and monitoring considerations

To maintain system reliability, workload discovery should also include:

- **Backup and restore strategy** — Evaluate existing backup methods and Amazon DocumentDB’s backup capabilities.
- **AWS Backup integration** — Leverage AWS Backup for centralized backup management across AWS services including Amazon DocumentDB.
- **CloudWatch metrics** — Map MongoDB monitoring metrics to Amazon DocumentDB CloudWatch metrics for CPU, memory, connections, and storage.
- **Performance Insights** — Implement Amazon DocumentDB Performance Insights to visualize database load and analyze performance issues with detailed query analytics.
- **Profiler** — Configure Amazon DocumentDB profiler to capture slow-running operations (similar to MongoDB's profiler but with Amazon DocumentDB-specific settings).
  - Enable through parameter groups with appropriate thresholds.
  - Analyze profiler data to identify optimization opportunities

- **CloudWatch Events** — Set up event-driven monitoring for Amazon DocumentDB cluster events.
  - Configure notifications for backup events, maintenance windows, and failovers.
  - Integrate with Amazon SNS for alerting and AWS Lambda for automated responses.

- **Audit logging** — Plan for audit logging configuration to track user activity and security-relevant events.
- **Enhanced monitoring** — Enable enhanced monitoring for granular OS-level metrics at 1-second intervals.

## Index migration

Migrating from MongoDB to Amazon DocumentDB involves transferring not just data but also indexes to maintain query performance and optimize database operations.
This section outlines the detailed step-by-step process for migrating indexes from MongoDB to Amazon DocumentDB while ensuring compatibility and efficiency.

### Using the Amazon DocumentDB index tool

**Clone the [index tool](https://github.com/awslabs/amazon-documentdb-tools/blob/master/index-tool/README.md "https://github.com/awslabs/amazon-documentdb-tools/blob/master/index-tool/README.md")**

```
git clone https://github.com/aws-samples/amazon-documentdb-tools.git
cd amazon-documentdb-tools/index-tool
```

```
pip install -r requirements.txt
```

**Export indexes from MongoDB (if migrating from MongoDB)**

```
python3 migrationtools/documentdb_index_tool.py --dump-indexes --dir mongodb_index_export --uri
'mongodb://localhost:27017'
```

**Export indexes from Amazon DocumentDB (if migrating from Amazon DocumentDB)**

```
python3 migrationtools/documentdb_index_tool.py --dump-indexes --dir docdb_index_export --uri
'mongodb://user:password@mydocdb.cluster-cdtjj00yfi95.eu-west-
2.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=rds-combined-ca-
bundle.pem&replicaSet=rs0&retryWrites=false'
```

**Import indexes**

```
python3 migrationtools/documentdb_index_tool.py --restore-indexes --skip-incompatible --dir
mongodb_index_export --uri 'mongodb://user:password@mydocdb.cluster-cdtjj00yfi95.eu-west-
2.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=rds-combined-ca-
bundle.pem&replicaSet=rs0&retryWrites=false'
```

**Verify indexes**

```
python3 migrationtools/documentdb_index_tool.py --show-issues --dir mongodb_index_export
```

## User migration

Migrating users from MongoDB to Amazon DocumentDB is essential for maintaining access control, authentication, and database security.
This section outlines detailed steps to successfully migrate MongoDB users while preserving their roles and permissions using the Amazon DocumentDB export user tool.

### Using Amazon DocumentDB export users tool

The [`Export Users tool`](https://github.com/awslabs/amazon-documentdb-tools/tree/master/migration/export-users "https://github.com/awslabs/amazon-documentdb-tools/tree/master/migration/export-users") exports users and roles from MongoDB or Amazon DocumentDB to JavaScript files, which can then be used to recreate them in another cluster.

**Prerequisites**

```
# Clone the repository
git clone https://github.com/awslabs/amazon-documentdb-tools.git
cd amazon-documentdb-tools/migration/export-users
```

```
# Install required dependencies
pip install pymongo
```

**Step 1: Export users and roles**

```
# Export users and roles to JavaScript files
python3 docdbExportUsers.py \
--users-file mongodb-users.js \
--roles-file mongodb-roles.js \
--uri "mongodb://admin:password@source-host:27017/"
```

**Step 2: Edit the Users File**

```
// Example of how to update the users.js file
// Find each user creation statement and add the password
db.getSiblingDB("admin").createUser({
user: "appuser",
// Add password here
pwd: "newpassword",
roles: [
{ role: "readWrite", db: "mydb" }
]
})
```

**Step 3: Restore Custom Roles to Amazon DocumentDB**

```
# Import roles first
mongo --ssl \
--host target-host:27017 \
--sslCAFile rds-combined-ca-bundle.pem \
--username admin \
--password password \
mongodb-roles.js
```

**Step 4: Restore Users to Amazon DocumentDB**

```
# Import users after roles are created
mongo --ssl \
--host target-host:27017 \
--sslCAFile rds-combined-ca-bundle.pem \
--username admin \
--password password \
mongodb-users.js
```

**Important notes**

- Passwords are not exported for security reasons and must be manually added to the users.js file.
- Roles must be imported before users to ensure proper role assignments.
- The tool generates JavaScript files that can be directly executed with the mongo shell.
- Custom roles and their privileges are preserved during migration.
- This approach allows for review and modification of user permissions before importing.

This method provides a secure and flexible approach to migrating users and roles from MongoDB to Amazon DocumentDB while allowing for password resets during the migration process.

## Data migration

###### Topics

- [Online migration](#w5aac23b9c21b5 "#w5aac23b9c21b5")
- [Offline migration](#w5aac23b9c21b7 "#w5aac23b9c21b7")
- [Prerequisites](#w5aac23b9c21c11 "#w5aac23b9c21c11")
- [Prepare an Amazon DocumentDB cluster](#w5aac23b9c21c13 "#w5aac23b9c21c13")
- [Perform the data dump (mongodump)](#w5aac23b9c21c15 "#w5aac23b9c21c15")
- [Transfer dump files to restoration environment](#w5aac23b9c21c17 "#w5aac23b9c21c17")
- [Restore data to Amazon DocumentDB (mongorestore)](#w5aac23b9c21c19 "#w5aac23b9c21c19")

### Online migration

This section provides detailed steps to perform an online migration from MongoDB to Amazon DocumentDB using AWS DMS to enable minimal downtime and continuous replication.
To begin, you set up an Amazon DocumentDB cluster as the target and ensure your MongoDB instance is properly configured as the source, typically requiring replica set mode for change data capture.
Next, you create a DMS replication instance and define source and target endpoints with the necessary connection details.
After validating the endpoints, you configure and start a migration task that can include full data load, ongoing replication, or both.

#### Configure target (Amazon DocumentDB)

###### Note

If you already have provisioned a Amazon DocumentDB cluster to migrate to, you can skip this step.

**Create a custom parameter group**

See the AWS Management Console or AWS CLI procedures in [Creating Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-create.md "cluster_parameter_groups-create.md").

**Create an Amazon DocumentDB cluster**

###### Note

While there are other procedures for creating an Amazon DocumentDB cluster in this guide, the steps in this section apply specifically to the task of migrating large amounts of data to a new cluster.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Clusters**.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. On the Amazon DocumentDB management console, under **Clusters**, choose **Create**. 4. On the **Create Amazon DocumentDB cluster** page, in the **Cluster type** section, choose **Instance-based cluster** (this is the default option). 5. In the Cluster configuration section:

    * For **Cluster identifier**, enter a unique name, such as `mydocdbcluster`.
     Note that the console will change all cluster names to lower-case regardless of how they are entered.
    * For **Engine version**, choose 5.0.0.

6.  In the **Cluster storage configuration** section, leave the **Amazon DocumentDB Standard** setting as is (this is the default option).
7.  In the **Instance configuration** section:
    - For **DB instance class**, choose **Memory optimized classes (include r classes)** (this is default).
    - For **Instance class**, choose an instance class based on workload. For example:

          + db.r6g.large: for smaller workloads
          + db.r6g.4xlarge: for larger workloads

      As a best practice, we recommend choosing as big an instance as you are able to for best full-load throughput, and scale down after migration is complete.

    - For **Number of instances**, choose 1 instance. Choosing one instance helps minimize costs. We recommend that you scale to three instances for high availability after the full-load migration is complete.

8.  In the **Authentication** section, enter a username for the primary user, and then choose **Self managed**. Enter a password, then confirm it.
9.  In the **Network settings** section, choose a VPC and subnet group, and then configure the VPC security group.
    Make sure your Amazon DocumentDB security group allows inbound connection from the DMS instance’s security group by updating inbound rules.
10. In the **Encryption-at-rest** section, enable encryption (recommended) and choose or enter a KMS key.
11. In the **Backup** section, set the backup retention period (1-35 days).
12. Review your configuration and choose **Create cluster**.

The deployment time typically takes between 10 an 15 minutes,

#### Configure source

MongoDB and Amazon DocumentDB can both serve as migration sources, depending on your scenario:

- **MongoDB as source** — Common when migrating from an on-premises or a self-managed MongoDB to an Amazon DocumentDB or other AWS database services.
  Requires running in replica set mode with an adequately sized oplog (make sure it is sized to hold all operations during Full Load) to support change data capture during migration.
- **Amazon DocumentDB as source** — Typically used for cross-region replication, version upgrades, or migrating to other database services like MongoDB Atlas.
  Requires [Enabling change streams](change_streams.md#change_streams-enabling "change_streams.md#change_streams-enabling") by setting the `change_stream_log_retention_duration` parameter in the cluster parameter group to capture ongoing changes during migration.
  Make sure your `change_stream_log_retention_duration` setting is large enough to cover the time needed to complete the Full Load.

Before starting migration, configure your source to allow AWS DMS access.

Create a MongoDB user with proper permissions:

```
db.createUser({
user: "`dmsUser`",
pwd: "`yourSecurePassword`",
roles: [{ role: "readAnyDatabase", db: "admin" }]
})
```

Configure network and authentication.

When configuring network connectivity for MongoDB to DMS migration:

**EC2-hosted MongoDB source**

- Modify the EC2 security group to allow inbound traffic from the DMS replication instance security group.
- Add a rule for TCP port 27017 (or your custom MongoDB port).
- Use the DMS replication instance's security group ID as the source for precise access control.
- Ensure the EC2 instance's subnet has a route to the DMS replication instance's subnet.

**On-premises MongoDB source**

- Configure your firewall to allow inbound connections from the DMS replication instance's public IP addresses.
- If using AWS Direct Connect or a VPN, ensure proper routing between your network and the VPC containing the DMS instance.
- Test connectivity using telnet or nc commands from the DMS subnet to your MongoDB server.

**MongoDB Atlas source**

- Add a DMS replication instance IP addresses to the MongoDB Atlas IP allowlist.
- Configure VPC peering between AWS VPC and MongoDB Atlas VPC if Atlas is running on AWS.
- Set up AWS PrivateLink for private connectivity (Enterprise tier), if running on another cloud provider.
- Create a dedicated user with appropriate read/write permissions.
- Use a MongoDB Atlas connection string with SSL Mode set to "verify-full".
- Ensure sufficient oplog size for migration duration.

**Amazon DocumentDB source**

Configure your source Amazon DocumentDB security group to allow inbound traffic from the DMS replication instance security group.

#### Create DMS replication instance

We recommend using [DMS Buddy](https://github.com/awslabs/amazon-documentdb-tools/tree/master/migration/dms_buddy "https://github.com/awslabs/amazon-documentdb-tools/tree/master/migration/dms_buddy") to provision your DMS infrastructure as it creates optimal migration infrastructure with optimal DMS settings and instance sizes.

If you prefer to configure manually, follow these steps:

1. Open the AWS DMS console and choose **Create replication instance**.
2. Enter replication instance details:
   - **Instance name**: Choose a unique name.
   - **Instance class**: Select based on workload. Example: dms.r5.large (small workloads), dms.r5.4xlarge (large workloads).
   - **Engine version**: 3.5.4
   - **Allocated storage**: Default is 100GB (increase if needed). This is determined by document size, updates/second and full load duration.
   - **Multi-AZ Deployment**: Enable for high availability, if needed.
   - Choose the same VPC as Amazon DocumentDB.
   - Ensure **Security groups** allow inbound traffic from source and Amazon DocumentDB.

3. Click **Create replication instance** and wait for the status to be available.

#### Create DMS endpoints

##### Create a source endpoint

**For a MongoDB source**

1. In the DMS console, in the navigation pane, choose **Migrate or replicate**, then choose **Endpoints**.
2. Choose **Create endpoint**.
3. On the **Create endpoint** page, choose **Source endpoint**.
4. In the **Endpoint configuration** section:
   - Enter a unique and meaningful **Endpoint identifier** (for example, "mongodb-source").
   - Choose **MongoDB** as the **Source engine**.
   - For **Access to endpoint database**, choose **Provide access information manually**.
   - For **Server name**, enter your `MongoDB server DNS name/IP address`.
   - For **Port**, enter **27017** (default MongoDB port).
   - For **Authentication mode**, choose the appropriate mode for your application (password/SSL) (default is secrets manager).
   - If **Authentication mode** is **Password**, provide:
     - **Username** and **Password**: Enter MongoDB credentials.
     - **Database name**: Your source database name.
     - **Authentication mechanism**: SCRAM-SHA-1 (default) or appropriate mechanism

5. For **Metadata mode**, leave the default setting of **document**.
6. Additional connection attributes:
   - authSource=admin (if authentication database is different)
   - replicaSet=<your-replica-set-name> (required for CDC)

**For an Amazon DocumentDB source**

1. In the DMS console, in the navigation pane, choose **Migrate or replicate**, then choose **Endpoints**.
2. Choose **Create endpoint**.
3. On the **Create endpoint** page, choose **Source endpoint**.
4. In the **Endpoint configuration** section:
   - Enter a unique and meaningful **Endpoint identifier** (for example, "docdb-source").
   - Choose **Amazon DocumentDB** as the **Source engine**.
   - For **Access to endpoint database**, choose **Provide access information manually**.
   - For **Server name**, enter your `source Amazon DocumentDB cluster endpoint`.
   - For **Port**, enter **27017** (default Amazon DocumentDB port).
   - For **SSL mode**, choose **verify-full** (recommended for Amazon DocumentDB).
   - For **CA Certificate**, choose the Amazon RDS root CA certificate.
   - For **Authentication mode**, choose the appropriate mode for your application (password/SSL) (default is secrets manager).
   - If **Authentication mode** is **Password**, provide:
     - **Username** and **Password**: Enter Amazon DocumentDB credentials.
     - **Database name**: Your source database name.
     - **Authentication mechanism**: SCRAM-SHA-1 (default) or appropriate mechanism

5. For **Metadata mode**, leave the default setting of **document**.

##### Create a target endpoint (Amazon DocumentDB)

1. In the DMS console, in the navigation pane, choose **Migrate or replicate**, then choose **Endpoints**.
2. Choose **Create endpoint**.
3. On the **Create endpoint** page, choose **Target endpoint**.
4. In the **Endpoint configuration** section:
   - Enter a unique and meaningful **Endpoint identifier** (for example, "docdb-target").
   - Choose **Amazon DocumentDB** as the **Target engine**.
   - For **Access to endpoint database**, choose the method you want to use to authenticate access to the database:
     - If you choose **AWS Secrets Manager**, choose the secret where you store your Amazon DocumentDB credentials in the **Secret** field.
     - If you choose **Provide access information manually**:
       - For **Server name**, enter your `target Amazon DocumentDB cluster endpoint`.
       - For **Port**, enter **27017** (default Amazon DocumentDB port).
       - For **SSL mode**, choose **verify-full** (recommended for Amazon DocumentDB).
       - For **CA Certificate**, download and specify the CA certificate bundle for SSL verification.
       - For **Authentication mode**, choose the appropriate mode for your application (password/SSL) (default is secrets manager).
       - If **Authentication mode** is **Password**, provide:
         - **Username** and **Password**: Enter Amazon DocumentDB credentials.
         - **Database name**: Your source database name.
         - **Authentication mechanism**: SCRAM-SHA-1 (default) or appropriate mechanism

5. For **Metadata mode**, leave the default setting of **document**.

#### Create replication task

1. In the DMS console, in the navigation pane, choose **Migrate or replicate**, then choose **Tasks**.
2. Choose **Create task**.
3. On the **Create task** page, in the **Task configuration** section:
   - Enter a unique and meaningful **Task identifier** (for example, "mongodb-docdb-replication").
   - Choose the source endpoint you created previously in the **Source database endpoint** drop-down menu.
   - Choose the target endpoint you created previously in the **Target database endpoint** drop-down menu.
   - For **Task type**, choose **Migrate and replicate**.

4. In the **Settings** section:
   - For **Target table preparation mode**, leave the default setting.
   - For **Stop task after full load completes**, leave the default setting.
   - For **LOB column settings**, leave the **Limited LOB mode** setting as is.
   - For **Data validation**, leave the default setting of **Turn off**.
   - For **Task logs**, check the **Turn on CloudWatch** logs box.
   - For **Batch-optimized apply**, leave the default setting of unchecked (off).

5. Back at the top of the **Task settings** section, in **Editing mode**, choose **JSON editor** and set the following attributes:

```
{
  "TargetMetadata": {
    "ParallelApplyThreads": 5
  },
  "FullLoadSettings": {
    "MaxFullLoadSubTasks": 16
  }
}
```

6. In the **Table mappings** section, add a new selection rule:
   - For **Schema name**, add the source database to migrate. Use % to specify multiple databases.
   - For **Schema table** name, add the source collection to migrate. Use % to specify multiple collections.
   - For **Action**, leave the default setting of **Include**

7. For large collections (over 100GB), add **Table settings rule**:
   - For **Schema name**, add the source database to migrate. Use % to specify multiple databases.
   - For **Schema table** name, add the source collection to migrate. Use % to specify multiple collections.
   - For **Number of partitions**, enter 16 (should be less than `MaxFullLoadSubTask`).

8. In the **Premigration assessment** section, make sure it is turned off.

### Offline migration

This section outlines the process to perform an offline migration from a self-managed MongoDB instance to Amazon DocumentDB using native MongoDB tools: `mongodump` and `mongorestore`.

### Prerequisites

**Source MongoDB requirements**

- Access to the source MongoDB instance with appropriate permissions.
- Install `mongodump`. if needed (it is installed during a MongoDB installation).
- Make sure there is enough disk space for the dump files.

**Target Amazon DocumentDB requirements**

- Make sure you have an Amazon DocumentDB cluster provisioned.
- Ensure there is an EC2 instance in the same VPC as Amazon DocumentDB to facilitate the migration.
- Network connectivity must be available between your source environment and Amazon DocumentDB.
- **mongorestore** must be installed on the migration EC2 instance.
- Appropriate IAM permissions must be configured to access Amazon DocumentDB,

**General requirements**

- AWS CLI must be configured (if using AWS services for intermediate storage)
- Sufficient bandwidth must be available for data transfer.
- Downtime window should be approved (if doing a live migration, consider other approaches)

### Prepare an Amazon DocumentDB cluster

Create an Amazon DocumentDB cluster in AWS:

- Appropriate an instance size based on your workload.
- Configure a VPC, subnets, and security groups.
- Enable necessary parameters via parameter groups.

### Perform the data dump (mongodump)

Choose one of the following options to create a dump file:

- **Option 1: Basic**

```
mongodump --
uri="mongodb://`<source_user>`:`<source_password>`@`<source_host>`:`<source_port>`/`<database>`" --
out=/path/to/dump
```

- **Option 2: Better control and performance**

```
mongodump \
--uri="mongodb://`<source_user>`:`<source_password>`@`<sourcehost>`:`<source_port>`" \
--out=/path/to/dump \
--gzip \# Compress output
--numParallelCollections=4 \# Parallel collections dump
--ssl \# If using SSL
--authenticationDatabase=admin \ # If auth is required
--readPreference=secondaryPreferred # If replica set
```

- **Option 3: Large databases**

```
mongodump \
--host=`<source_host>` \
--port=`<source_port>` \
--username=`<source_user>` \
--password=`<source_password>` \
--db=`<specific_db>` \# Only dump specific DB
--collection=`<specific_collection>` \ # Only dump specific collection
--query='{ "date": { "$gt": "2020-01-01" } }' \ # Filter documents
--archive=/path/to/archive.gz \# Single archive output
--gzip \
--ssl
```

### Transfer dump files to restoration environment

Choose an appropriate method based on your dump size:

- **Small** — Directly copy to your migration machine (EC2 instance you created earlier):

```
scp -r /path/to/dump user@migration-machine:/path/to/restore
```

- **Medium** — Use Amazon S3 as intermediate storage:

```
aws s3 cp --recursive /path/to/dump s3://your-bucket/mongodb-dump/
```

- **Large** — For very large databases, consider AWS DataSync or a physical transfer.

### Restore data to Amazon DocumentDB (mongorestore)

Before starting the restore process, create the indexes in Amazon DocumentDB.
You can utilize the [Amazon DocumentDB Index tool](https://github.com/awslabs/amazon-documentdb-tools/tree/master/index-tool "https://github.com/awslabs/amazon-documentdb-tools/tree/master/index-tool") to export and import indexes.

Choose one of the following options to restore data:

- **Option 1: Basic restore**

```
mongorestore --uri="mongodb://`<docdb_user>`:`<docdb_password>`@`<docdb_endpoint>`:27017"
/path/to/dump
```

- **Option 2: Better control and performance**

```
mongorestore \
--uri="mongodb://`<docdb_user>`:`<docdb_password>`@`<docdb_endpoint>`:27017" \
--ssl \
--sslCAFile=/path/to/rds-combined-ca-bundle.pem \ # DocumentDB CA cert
--gzip \# If dumped with gzip
--numParallelCollections=4 \# Parallel restoration
--numInsertionWorkersPerCollection=4 \# Parallel documents insertion
--noIndexRestore \# skip indexes as they are pre-created
/path/to/dump
```

- **Option 3: Large databases or specific controls**

```
mongorestore \
--host=`<docdb_endpoint>` \
--port=27017 \
--username=`<docdb_user>` \
--password=`<docdb_password>` \
--ssl \
--sslCAFile=/path/to/rds-combined-ca-bundle.pem \
--archive=/path/to/archive.gz \# If using archive format
--gzip \
--nsInclude="db1.*" \# Only restore specific namespaces
--nsExclude="db1.sensitive_data" \ # Exclude specific collections if needed
--noIndexRestore \# skip indexes as they are pre-created
--writeConcern="{w: 'majority'}" # Ensure write durability
```

## Monitoring

This section provides a detailed monitoring process to track the progress, performance, and health of an ongoing migration from:

**MongoDB** to **Amazon DocumentDB**

or

**Amazon DocumentDB** to **Amazon DocumentDB**

The monitoring steps apply regardless of the migration method (AWS DMS, mongodump/mongorestore, or other tools).

### AWS DMS Migration monitoring (if applicable)

Monitor the following key CloudWatch metrics:

**Full load phase metrics**

- **FullLoadThroughputBandwidthTarget** — Network bandwidth (KB/second) during full load
- **FullLoadThroughputRowsTarget** — Number of rows/documents loaded per second
- **FullLoadThroughputTablesTarget** — Number of tables/collections completed per minute
- **FullLoadProgressPercent** — Percentage of full load completed
- **TablesLoaded** — Number of tables/collections successfully loaded
- **TablesLoading** — Number of tables/collections currently loading
- **TablesQueued** — Number of tables/collections waiting to be loaded
- **TablesErrored** — Number of tables/collections that failed to load

**CDC phase metrics**

- **CDCLatencyTarget** — Time delay (seconds) between source change and target application
- **CDCLatencySource** — Time delay (seconds) between change in source and DMS reading it
- **CDCThroughputRowsTarget** — Rows per second applied during ongoing replication
- **CDCThroughputBandwidthTarget** — Network bandwidth (KB/second) during CDC
- **CDCIncomingChanges** — Number of change events received from source
- **CDCChangesMemoryTarget** — Memory used (MB) for storing changes on target side

**Resource metrics**

- **CPUUtilization** — CPU usage of the replication instance
- **FreeableMemory** — Available memory on the replication instance
- **FreeStorageSpace** — Available storage on the replication instance
- **NetworkTransmitThroughput** — Network throughput for the replication instance
- **NetworkReceiveThroughput** — Network throughput for the replication instance

**Error metrics**

- **ErrorsCount** — Total number of errors during migration
- **TableErrorsCount** — Number of table-specific errors
- **RecordsErrorsCount** — Number of record-specific errors

Create CloudWatch alarms for critical metrics like `CDCLatencyTarget` and `CPUUtilization` to receive notifications if migration performance degrades.

#### DMS logs (CloudWatch logs)

1. Go to Amazon CloudWatch Logs console.
2. Find and choose on your log group. It will look similar to "dms-tasks –".
3. Look for log streams that might contain error information:
   - Streams with "error" in the name
   - Streams with task IDs or endpoint names
   - The most recent log streams during the time of your migration

4. Within these streams, search for keywords like:
   - "error"
   - "exception"
   - "failed"
   - "warning"

#### DMS task status (using AWS CLI)

```
aws dms describe-replication-tasks --filters Name=replication-task id,Values=`<task_id>` --query
"ReplicationTasks[0].Status"
```

Expected status flow:

creating → ready → running → stopping → stopped (or failed)

#### Monitor using `docdb-dashboarder`

The `docdb-dashboarder` tool provides comprehensive monitoring for Amazon DocumentDB clusters by automatically generating CloudWatch dashboards with essential performance metrics.
These dashboards display critical cluster-level metrics (replica lag, operation counters), instance-level metrics (CPU, memory, connections), and storage metrics (volume usage, backup storage).
For migration scenarios, the tool offers specialized dashboards that track migration progress with metrics like CDC replication lag and operation rates.
The dashboards can monitor multiple clusters simultaneously and include support for NVMe-backed instances.
By visualizing these metrics, teams can proactively identify performance bottlenecks, optimize resource allocation, and ensure smooth operation of their Amazon DocumentDB deployments.
The tool eliminates the need for manual dashboard creation while providing consistent monitoring across all environments.
For setup instructions and advanced configuration options, refer to the [Amazon DocumentDB Dashboarder Tool](https://github.com/awslabs/amazon-documentdb-tools/tree/master/monitoring/docdb-dashboarder "https://github.com/awslabs/amazon-documentdb-tools/tree/master/monitoring/docdb-dashboarder") GitHub repository.

## Validation

###### Topics

- [Validation checklist](#w5aac23b9c25c15 "#w5aac23b9c25c15")
- [Schema and index validation](#w5aac23b9c25c17 "#w5aac23b9c25c17")
- [Data sampling and field-level validation](#w5aac23b9c25c19 "#w5aac23b9c25c19")
- [Validation using DataDiffer tool](#w5aac23b9c25c21 "#w5aac23b9c25c21")

This section provides a detailed validation process to ensure data consistency, integrity, and application compatibility after migrating from:

**MongoDB** to **Amazon DocumentDB**

or

**Amazon DocumentDB** to **Amazon DocumentDB**

The validation steps apply regardless of the migration method (AWS DMS, mongodump/mongorestore, or other tools).

### Validation checklist

Verify that the number of documents in each collection matches between source and target:

**MongoDB source**

```
mongo --host `<source_host>` --port `<port>` --username `<user>` -- password `<password>` --eval
"db.`<collection>`.count()"
```

**Amazon DocumentDB target**

```
mongo --host `<target_host>` --port `<port>` --username `<user>` -- password `<password>` --eval
"db.`<collection>`.count()"
```

### Schema and index validation

Ensure that:

- all collections exist in the target.
- indexes are correctly replicated.
- schema definitions (if enforced) are identical.

**Check collections (source vs. target)**

```
mongo --host `<source_host>` --eval "show collections"
mongo --host `<target_host>` --ssl --eval "show collections"
```

**check indexes (Source vs. Target)**

```
mongo --host `<source_host>` --eval" db.`<collection>`.getIndexes()"
mongo --host `<target_host>` --ssl –eval" db.`<collection>`.getIndexes()"
```

Compare the list of collections to ensure there are no missing or extra collections.

Verify indexes by checking index names, key definitions, unique constraints, and TTL indexes (if any).

**Check schema validation rules (if using schema validation in MongoDB)**

```
mongo --host `<source_host>` --eval" db.getCollectionInfos({name: '`<collection>`'})
[0].options.validator"
   mongo --host `<target_host>` --ssl –eval" db.getCollectionInfos({name: '`<collection>`'})[0].options.validator"
```

### Data sampling and field-level validation

You can randomly sample documents and compare fields between source and target.

**Manual sampling**

Fetch five random documents (source):

```
mongo --host `<source_host>` --eval "db.`<collection>`.aggregate([{ \$sample: { size: 5 } }])"
```

Fetch the same document IDs (target):

```
mongo --host `<target_host>` --ssl –eval "db.`<collection>`.find({ _id: { \$in: [`<list_of_ids>`] } })"
```

**Automatic sampling**

```
import pymongo
# Connect to source and target
source_client = pymongo.MongoClient("`<source_uri>`")
target_client = pymongo.MongoClient("`<target_uri>`", ssl=True)
source_db = source_client["`<db_name>`"]
target_db = target_client["`<db_name>`"]
# Compare 100 random documents
for doc in source_db.`<collection>`.aggregate([{ "$sample":
{ "size": 100 } }]):
target_doc = target_db.`<collection>`.find_one({ "_id":
doc["_id"] })
if target_doc != doc:
print(f"❌ Mismatch in _id: {doc['_id']}")
else:
print(f"✅ Match: {doc['_id']}")
```

### Validation using DataDiffer tool

The [DataDiffer tool](https://github.com/awslabs/amazon-documentdb-tools/tree/master/migration/data-differ "https://github.com/awslabs/amazon-documentdb-tools/tree/master/migration/data-differ") provides a reliable way to compare data between source and target databases.

#### Prerequisites

The following prerequisites must be met before installing the DataDiffer tool:

- Python 3.7+
- PyMongo library
- Network connectivity to both source MongoDB and target Amazon DocumentDB clusters

#### Setup and installation

**Clone the repository and navigate to the DataDiffer directory**

```
git clone https://github.com/awslabs/amazon-documentdb-tools.git
cd amazon-documentdb-tools/migration/data-differ
```

**Install required dependencies**

```
pip install -r requirements.txt
```

#### Running data validation

**Create a configuration file (e.g., config.json) with connection details**

```
{
"source": {
"uri": "mongodb://username:password@source-mongodb-
host:27017/?replicaSet=rs0",
"db": "your_database",
"collection": "your_collection"
},
"target": {
"uri": "mongodb://username:password@target-docdb-
cluster.region.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-
bundle.pem&replicaSet=rs0",
"db": "your_database",
"collection": "your_collection"
},
"options": {
"batch_size": 1000,
"threads": 4,
"sample_size": 0,
"verbose": true
}
}
```

**Run the DataDiffer tool**

```
python differ.py --config config.json
```

**For large collections, use sampling to validate a subset of data**

```
python differ.py --config config.json --sample-size 10000
```

**To validate multiple collections, create separate configuration files or use the batch mode**

```
python differ.py --batch-config batch_config.json
```

#### Interpreting results

The tool will output:

- Total documents in source and target
- Number of matching documents
- Number of missing documents
- Number of documents with differences
- Detailed report of differences (if any)

#### Best practices

The following are best practices when using the DataDiffer tool:

- **Run in phases** — First validate document counts, then sample key documents, and finally run a full comparison, if needed.
- **Check for schema differences** — Amazon DocumentDB has some limitations compared to MongoDB.
  The tool will highlight incompatible data types or structures.
- **Validate during quiet periods** — Run validation when write operations are minimal to ensure consistency.
- **Monitor resource usage** — The comparison process can be resource-intensive.
  Adjust batch size and thread count accordingly.
- **Validate indexes** — After data validation, ensure all required indexes have been created on the target Amazon DocumentDB cluster.
- **Document validation results** — Keep a record of validation results for each collection as part of your migration documentation.
