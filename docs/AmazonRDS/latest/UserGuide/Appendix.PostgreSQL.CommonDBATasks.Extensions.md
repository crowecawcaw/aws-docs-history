# Working with the supported foreign data wrappers for Amazon RDS for PostgreSQL

A foreign data wrapper (FDW) is a specific type of extension that provides access to external data. For example, the
`oracle_fdw` extension allows your
RDS for PostgreSQL DB cluster to work with Oracle databases.
As another example, by using the PostgreSQL native
`postgres_fdw` extension you can access data stored in PostgreSQL DB instances external to your
RDS for PostgreSQL DB instance.

Following, you can find information about several supported PostgreSQL foreign data wrappers.

###### Topics

- [Using the log_fdw extension to access the DB log using SQL](CHAP_PostgreSQL.Extensions.md "CHAP_PostgreSQL.Extensions.md")
- [Using the postgres_fdw extension to access external data](postgresql-commondbatasks-fdw.md "postgresql-commondbatasks-fdw.md")
- [Working with MySQL databases by using the mysql_fdw extension](postgresql-mysql-fdw.md "postgresql-mysql-fdw.md")
- [Working with Oracle databases by using the oracle_fdw extension](postgresql-oracle-fdw.md "postgresql-oracle-fdw.md")
- [Working with SQL Server databases by using the tds_fdw extension](postgresql-tds-fdw.md "postgresql-tds-fdw.md")
