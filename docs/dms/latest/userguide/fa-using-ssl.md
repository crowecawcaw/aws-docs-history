# Using SSL with AWS DMS Fleet Advisor

###### Important

End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service Fleet
Advisor. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet
Advisor console or AWS DMS Fleet Advisor resources. For more information, see [AWS DMS Fleet
Advisor end of support](dms_fleet.md "dms_fleet.md").

To protect your data, AWS DMS Fleet Advisor can use SSL to access your databases.

## Supported databases

AWS DMS Fleet Advisor supports using SSL to access following databases:

- Microsoft SQL Server
- MySQL
- PostgreSQL

## Setting up SSL

To use SSL to access your database, configure your database server to support SSL.
For more information, see the following documentation for your database:

- SQL Server: [Enable encrypted connections to the Database Engine](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine?view=sql-server-2017")
- MySQL: [Configuring MySQL to Use Encrypted Connections](https://dev.mysql.com/doc/refman/5.7/en/using-encrypted-connections.html "https://dev.mysql.com/doc/refman/5.7/en/using-encrypted-connections.html")
- PostgreSQL: [Secure TCP/IP Connections with SSL](https://www.postgresql.org/docs/current/ssl-tcp.html "https://www.postgresql.org/docs/current/ssl-tcp.html")

To use SSL to connect to your database, select **Trust server
certificate** and **Use SSL** when adding a server
manually. For a MySQL database, you can use a custom certificate. To use a
custom certificate, select the **Verify CA** check box. For
information about adding a server, see [Managing monitored objects](fa-managing-objects.md "fa-managing-objects.md").

## Checking the Server Certificate Authority (CA)

Certificate for SQL Server

If you want to validate your Server Certificate Authority (CA) Certificate for SQL
Server, then clear **Trust server certificate** when you add the
server. If your server uses a well-known CA, and the CA is installed by default on
your OS, then verification should work normally. If DMS Fleet Advisor can't connect to your
database server, install the CA certificate that your database server uses. For more
information, see [Configure client](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine?view=sql-server-2017#configure-client "https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine?view=sql-server-2017#configure-client").
