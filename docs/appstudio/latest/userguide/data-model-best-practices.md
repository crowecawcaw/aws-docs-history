# Best practices when designing data models

Use the following best practices to create a robust, scalable, and secure relational data model in AWS for use in your App Studio application
that meets your application's requirements and ensures the long-term reliability and performance of your data infrastructure.

- **Choose the right AWS data service:** Depending on your requirements, choose the appropriate AWS data service.
  For example, for an Online Transaction Processing (OLTP) application, you could consider a database (DB)
  such as Amazon Aurora which is a cloud-native, relational, and fully-managed database service that supports various database engines like MySQL and PostgreSQL. For a full list of
  Aurora versions supported by App Studio, see [Connect to Amazon Aurora](connectors-aurora.md "connectors-aurora.md"). On the other hand, for Online Analytical
  Processing (OLAP) use cases, consider using Amazon Redshift, which is a cloud data warehouse that lets you run complex queries against very large datasets.
  These queries can often take time (many seconds) to complete, making Amazon Redshift less suitable for OLTP applications that require low-latency data access.
- **Design for scalability:** Plan your data model with future growth and scalability in mind.
  Consider factors like expected data volume, access patterns, and performance requirements when choosing an appropriate data service and
  database instance type and configuration (such as provisioned capacity).
  - For more information about scaling with Aurora serverless, see
    [Performance and scaling for Aurora Serverless V2](../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.md").

- **Normalize your data:** Follow the principles of database normalization to minimize
  data redundancy and improve data integrity. This includes creating appropriate tables, defining primary and foreign keys, and establishing
  relationships between entities. In App Studio, when querying data from one entity, you can retrieve related data from another entity by
  specifying a `join` clause on the query.
- **Implement appropriate indexing:** Identify the most important queries and access patterns,
  and create appropriate indexes to optimize performance.
- **Leverage AWS data services features:** Take advantage of the features offered by the AWS data service you choose,
  such as automated backups, multi-AZ deployments, and automatic software updates.
- **Secure your data:** Implement robust security measures, such as IAM (AWS Identity and Access Management) policies,
  creation of database users with restricted permissions to tables and schemas, and enforce encryption at rest and in transit.
- **Monitor and optimize performance:** Continuously monitor your database's performance and
  make adjustments as needed, such as scaling resources, optimizing queries, or tuning database configurations.
- **Automate database management:** Utilize AWS services like Aurora Autoscaling, Performance Insights for Aurora,
  and AWS Database Migration Service to automate database management tasks and reduce operational overhead.
- **Implement disaster recovery and backup strategies:** Ensure that you have a well-defined backup and recovery plan,
  leveraging features like Aurora Automated Backups, point-in-time recovery, and cross-region replica configurations.
- **Follow AWS best practices and documentation:** Stay up-to-date with the latest AWS best practices,
  guidelines, and documentation for your chosen data service to ensure that your data model and implementation are aligned with AWS recommendations.
  For more detailed guidance from each AWS data service, see the following topics:

- [Best practices with Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md")
- [Best practices with Amazon Aurora MySQL](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.md")
- [Amazon Redshift query performance tuning](../../../redshift/latest/dg/c-optimizing-query-performance.md "../../../redshift/latest/dg/c-optimizing-query-performance.md")
- [Best practices for querying and scanning data in Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/bp-query-scan.md "../../../amazondynamodb/latest/developerguide/bp-query-scan.md")
