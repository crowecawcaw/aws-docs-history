# Connecting to your Db2 DB instance

After Amazon RDS provisions your Amazon RDS for Db2 DB instance, you can use any standard SQL client
application to connect to the DB instance. Because Amazon RDS is a managed service, you can't
sign in as `SYSADM`, `SYSCTRL`, `SECADM`, or
`SYSMAINT`.

You can connect to a DB instance that is running the IBM Db2 database engine by using
IBM Db2 CLP, IBM CLPPlus, DBeaver, or IBM Db2 Data Management Console.

###### Note

Connecting to a Db2 database can fail if your RDS for Db2 DB instance doesn't have
sufficient memory. For more information, see [Database connection error](db2-troubleshooting.md#db2-database-connection-error "db2-troubleshooting.md#db2-database-connection-error").

###### Topics

- [Finding the endpoint of your Amazon RDS for Db2 DB instance](db2-finding-instance-endpoint.md "db2-finding-instance-endpoint.md")
- [Connecting to your Amazon RDS for Db2 DB instance with IBM Db2 CLP](db2-connecting-with-clp-client.md "db2-connecting-with-clp-client.md")
- [Connecting to your Amazon RDS for Db2 DB instance with IBM CLPPlus](db2-connecting-with-ibm-clpplus-client.md "db2-connecting-with-ibm-clpplus-client.md")
- [Connecting to your Amazon RDS for Db2 DB instance with DBeaver](db2-connecting-with-dbeaver.md "db2-connecting-with-dbeaver.md")
- [Connecting to your Amazon RDS for Db2 DB instance with IBM Db2 Data Management Console](db2-connecting-with-ibm-data-management-console.md "db2-connecting-with-ibm-data-management-console.md")
- [Considerations for security groups with Amazon RDS for Db2](db2-security-groups-considerations.md "db2-security-groups-considerations.md")
