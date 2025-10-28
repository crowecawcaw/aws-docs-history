# Working with MySQL replication in Amazon RDS

You usually use read replicas to configure replication between Amazon RDS DB instances. For
general information about read replicas, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md"). For specific information about working with read
replicas on Amazon RDS for MySQL, see [Working with MySQL read replicas](USER_MySQL.Replication.md "USER_MySQL.Replication.md").

You can use global transaction identifiers (GTIDs) for replication with RDS for MySQL. For more information, see
[Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

You can also set up replication between an RDS for MySQL DB instance and a
MariaDB or MySQL instance that is external to Amazon RDS. For information about configuring replication with an external source, see
[Configuring binary log file position replication with an external source instance](MySQL.Procedural.Importing.External.md "MySQL.Procedural.Importing.External.md").

For any of these replication options, you can use either row-based replication, statement-based, or mixed replication. Row-based replication
only replicates the changed rows that result from a SQL statement. Statement-based replication replicates the entire SQL statement. Mixed replication
uses statement-based replication when possible, but switches to row-based replication when SQL statements that are unsafe for statement-based replication
are run. In most cases, mixed replication is recommended. The binary log format of the DB instance determines whether replication is row-based,
statement-based, or mixed. For information about setting the binary log format, see [Configuring RDS for MySQL binary logging for Single-AZ databases](USER_LogAccess.MySQL.md "USER_LogAccess.MySQL.md").

###### Note

You can configure replication to import databases from a MariaDB or MySQL instance that is external to Amazon RDS, or to export
databases to such instances. For more information, see [Importing data to an Amazon RDS for MySQL
database with reduced downtime](mysql-importing-data-reduced-downtime.md "mysql-importing-data-reduced-downtime.md")
and [Exporting data from a MySQL DB instance by using replication](MySQL.Procedural.Exporting.md "MySQL.Procedural.Exporting.md").

After you restore your DB instance from a snapshot or perform a point-in-time recovery,
you can view the last recovered binlog position from the source database in the RDS console.
Under **Logs & events**, enter **binlog**. The binlog position appears under **System
notes**.

###### Topics

- [Working with MySQL read replicas](USER_MySQL.Replication.md "USER_MySQL.Replication.md")
- [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md")
- [Configuring binary log file position replication with an external source instance](MySQL.Procedural.Importing.External.md "MySQL.Procedural.Importing.External.md")
- [Configuring multi-source-replication for Amazon RDS for MySQL](mysql-multi-source-replication.md "mysql-multi-source-replication.md")
