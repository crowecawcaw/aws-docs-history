

# Migration support
<a name="aurora-features-migration"></a>

**Topics**
+ [MySQL migration](#aurora-features-mysql-migration)
+ [PostgreSQL migration](#aurora-features-postgresql-migration)
+ [Commercial database migrations](#aurora-features-commercial-migration)

## MySQL migration
<a name="aurora-features-mysql-migration"></a>

Standard MySQL import and export tools (mysqldump, mysqlimport) work with Aurora. You can also create a new Aurora database from an RDS for MySQL DB snapshot, and migration operations based on DB snapshots typically complete in under an hour. Alternatively, AWS Database Migration Service (AWS DMS) offers [built-in native tooling](https://docs.aws.amazon.com/dms/latest/userguide/data-migrations.html) for seamless migration with no replication instances to provision or scale. You can initiate a database migration with a few simple clicks and only pay on an hourly basis for the time used. Finally, you can also set up binlog-based replication between an Aurora MySQL database and an external MySQL database running inside or outside of AWS.

## PostgreSQL migration
<a name="aurora-features-postgresql-migration"></a>

Standard PostgreSQL import and export tools (pg\_dump, pg\_restore) work with Aurora. Aurora also supports snapshot import from RDS for PostgreSQL, and replication with [AWS DMS](https://aws.amazon.com/dms/).

## Commercial database migrations
<a name="aurora-features-commercial-migration"></a>

[AWS DMS](https://aws.amazon.com/dms/) accelerates migrations from commercial database to Aurora with DMS Schema Conversion, which automatically assesses and converts schemas and source objects to be compatible with the target Aurora cluster. [DMS Serverless](https://aws.amazon.com/dms/features/) automates provisioning, monitoring, and scaling of migration resources.