# Migration

###### Topics

- [How do I migrate a MySQL database to Amazon Aurora (and back)?](#aurora-faq-how-do-i-migrate-a-mysql-database-to-amazon-aurora-and-back "#aurora-faq-how-do-i-migrate-a-mysql-database-to-amazon-aurora-and-back")
- [How do I migrate a PostgreSQL database to Amazon Aurora (and back)?](#aurora-faq-how-do-i-migrate-a-postgresql-database-to-amazon-aurora-and- "#aurora-faq-how-do-i-migrate-a-postgresql-database-to-amazon-aurora-and-")

## How do I migrate a MySQL database to Amazon Aurora (and back)?

You can migrate between MySQL and Amazon Aurora using several reliable methods. The most straightforward approach is using standard MySQL utilities: mysqldump to export data from MySQL and mysqlimport to import data into Aurora, with the same tools working in reverse for migration back to MySQL.

Alternatively, you can use the [Amazon RDS DB snapshot migration feature](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.RDSMySQL.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.RDSMySQL.md") to migrate an Amazon RDS for MySQL DB Snapshot directly to Aurora through the Amazon RDS console. For large-scale migrations with minimal downtime, [AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/") supports continuous replication while your source database remains operational. Most customers complete their Aurora migration in under an hour, though migration duration depends on your database format and dataset size. For comprehensive migration strategies, review the [Best Practices for Migrating MySQL Databases to Amazon Aurora](https://d1.awsstatic.com/whitepapers/RDS/Migrating%20your%20databases%20to%20Amazon%20Aurora.pdf "https://d1.awsstatic.com/whitepapers/RDS/Migrating%20your%20databases%20to%20Amazon%20Aurora.pdf") documentation.

## How do I migrate a PostgreSQL database to Amazon Aurora (and back)?

You can migrate between PostgreSQL and Amazon Aurora using several proven methods. The most common approach is using standard PostgreSQL utilities: pg\_dump to export data from PostgreSQL and pg\_restore to import data into Aurora, with the same tools working in reverse for migration back to PostgreSQL.

Alternatively, you can use the [RDS DB snapshot migration feature](../../../AmazonRDS/latest/UserGuide/USER_CreateSnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_CreateSnapshot.md") to migrate an Amazon RDS for PostgreSQL DB snapshot directly to Aurora through the Amazon RDS console. For organizations migrating SQL Server databases to Aurora PostgreSQL, [AWS Transform for SQL Server](https://aws.amazon.com/transform/windows/sql-server/ "https://aws.amazon.com/transform/windows/sql-server/") is an AI-powered service that modernizes your SQL Server workloads to Aurora PostgreSQL. Most customers complete their Aurora migration in under an hour, though migration duration depends on your database format and dataset size. For detailed guidance, consult the [Amazon Aurora User Guide](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.md "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.md").
