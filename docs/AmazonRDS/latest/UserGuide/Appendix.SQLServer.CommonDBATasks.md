# Transitioning a

Amazon RDS for SQL Server database from OFFLINE to ONLINE

You can transition your Microsoft SQL Server database on an Amazon RDS DB instance from `OFFLINE` to `ONLINE`.

| SQL Server method                    | Amazon RDS method                                   |
| ------------------------------------ | --------------------------------------------------- |
| ALTER DATABASE `db_name` SET ONLINE; | EXEC rdsadmin.dbo.rds_set_database_online `db_name` |
