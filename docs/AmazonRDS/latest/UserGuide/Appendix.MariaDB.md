# MariaDB on Amazon RDS SQL reference

Following, you can find descriptions of system stored procedures that are available for Amazon RDS
instances running the MariaDB DB engine.

You can use the system stored procedures that are available for MySQL DB
instances and MariaDB DB instances. These stored procedures are documented at
[RDS for MySQL stored procedure reference](Appendix.MySQL.md "Appendix.MySQL.md"). MariaDB DB instances support all
of the stored procedures, except for `mysql.rds_start_replication_until` and
`mysql.rds_start_replication_until_gtid`.

Additionally, the following system stored procedures are supported only for Amazon RDS DB
instances running MariaDB:

- [mysql.rds_replica_status](mysql_rds_replica_status.md "mysql_rds_replica_status.md")
- [mysql.rds_set_external_master_gtid](mysql_rds_set_external_master_gtid.md "mysql_rds_set_external_master_gtid.md")
- [mysql.rds_kill_query_id](mysql_rds_kill_query_id.md "mysql_rds_kill_query_id.md")
- [mysql.rds_execute_operation](mysql_rds_execute_operation.md "mysql_rds_execute_operation.md")
