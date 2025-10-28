# Choosing your database engine for Amazon RDS

To set up your Amazon RDS DB instance, you must first choose the appropriate database engine.
Amazon RDS supports several widely-used relational database engines, each suited to specific use
cases and application requirements.

If you're new to Amazon RDS or relational databases, consider starting with MySQL or
PostgreSQL. Both engines are open-source, cost-effective, and widely supported by the
development community. Choose **MySQL** if your application needs
broad compatibility with existing tools or frameworks, or if your workload involves simple
transactional operations. Choose **PostgreSQL** if your
application requires advanced features such as JSON data handling, complex queries, or support
for custom extensions.

###### Note

This guide primarily uses MySQL for examples, but most steps are similar for PostgreSQL.
By selecting an engine that aligns with your project requirements, you can ensure better
performance and scalability as your database evolves.

Amazon RDS supports the following database engines, each designed for specific use cases and
performance needs.

**MySQL**

- **When to choose**: Best for for web-based applications,
  content management systems, and workloads that require simple transactional operations.
  Its broad compatibility with frameworks and tools makes it an ideal choice for
  general-purpose use cases.
- **Key features**: Read replicas, point-in-time recovery,
  multiple storage engines.
- **Documentation**: [Amazon RDS for MySQL](../UserGuide/CHAP_MySQL.md "../UserGuide/CHAP_MySQL.md")
  **PostgreSQL**

- **When to choose**: Ideal for applications that require
  advanced features like support for JSON, geospatial data, or complex queries. It's also
  well-suited for data analysis and custom application development.
- **Key features**: Extensibility with custom modules, high
  availability, advanced indexing options.
- **Documentation**: [Amazon RDS for
  PostgreSQL](../UserGuide/CHAP_PostgreSQL.md "../UserGuide/CHAP_PostgreSQL.md")
  **Oracle**

- **When to choose**: Designed for enterprise-grade
  workloads that require high performance, advanced analytics, or extensive transactional
  capabilities. Common in financial services and large-scale Enterprise Resource Planning
  (ERP) systems.
- **Key features**: Advanced security, analytics
  capabilities, and database partitioning.
- **Documentation**: [Amazon RDS for Oracle](../UserGuide/CHAP_Oracle.md "../UserGuide/CHAP_Oracle.md")
  **SQL Server**

- **When to choose**: Best suited for organizations that
  use the Microsoft ecosystem or developing applications with tight integration to
  Windows-based services. Common in Business Intelligence (BI) workloads and reporting
  solutions.
- **Key features**: Built-in analytics, data compression,
  and high availability options.
- **Documentation**: [Amazon RDS for Microsoft SQL
  Server](../UserGuide/CHAP_SQLServer.md "../UserGuide/CHAP_SQLServer.md")
  **MariaDB**

- **When to choose**: An open-source alternative to MySQL,
  MariaDB is ideal if you need enterprise-grade performance and features with
  community-driven development.
- **Key features**: Dynamic thread pooling, enhanced
  replication, and compatibility with MySQL.
- **Documentation**: [Amazon RDS for MariaDB](../UserGuide/CHAP_MariaDB.md "../UserGuide/CHAP_MariaDB.md")
  **IBM Db2**

- **When to choose**: Preferred for mission-critical
  applications that require advanced analytics, data integrity, and scalability. Common in
  industries such as finance and healthcare.
- **Key features**: Advanced compression, scalability, and
  high availability.
- **Documentation**: [Amazon RDS for Db2](../UserGuide/CHAP_Db2.md "../UserGuide/CHAP_Db2.md")

## Next steps

Now that you selected the database engine that best suits your needs, it's time to
create your first Amazon RDS DB instance.

**Next step**: [Creating your first DB instance](create-instance-overview.md#create-instance "create-instance-overview.md#create-instance")
