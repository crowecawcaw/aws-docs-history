# Connecting to an Amazon RDS DB instance using a database client

Database clients provide a user-friendly way to connect to and manage your Amazon RDS DB
instance. This section outlines the process of connecting to your DB instance using two
popular database clients: MySQL Workbench and pgAdmin.

Althought the exact steps vary slightly depending on the tool and database engine, the
general process involves configuring the connection with your endpoint, port, and
credentials.

###### Topics

- [Connecting to a MySQL DB instance](#connecting-mysql "#connecting-mysql")
- [Connecting to a PostgreSQL DB instance](#connecting-postgres "#connecting-postgres")
- [Connecting to other database engines](#connecting-other-engines "#connecting-other-engines")
- [Next steps](#connecting-client-next-steps "#connecting-client-next-steps")

## Connecting to a MySQL DB instance

[MySQL Workbench](https://www.mysql.com/products/workbench/ "https://www.mysql.com/products/workbench/") is a
popular database client that allows you to connect to and manage your MySQL DB instance.
Follow these steps to set up a connection and start working with your MySQL database.

###### To connect to a MySQL DB instance

1. Open MySQL Workbench on your local machine.
2. Choose **Database**, **Manage Connections** from
   the menu.
3. Create a new connection and configure the following settings:
   - **Hostname**: Enter the endpoint retrieved from the
     AWS Management Console.
   - **Port**: Use the port number displayed in the
     **Connectivity & security** section (typically 3306).
   - **Username**: Enter the master username you set
     when you created the DB instance.

   ![Database connection settings interface with hostname, port, username, and password fields.](images/connect-mysql.png)

4. Choose **Test Connection** to verify the connection
   settings.
5. When the connection is successful, save the configuration and open the connection to
   access your database.

For comprehensive documentation, see [Connecting to a DB instance
running the MySQL database engine](../UserGuide/USER_ConnectToInstance.md "../UserGuide/USER_ConnectToInstance.md") in the _Amazon RDS User
Guide_.

## Connecting to a PostgreSQL DB instance

[pgAdmin](https://www.pgadmin.org/ "https://www.pgadmin.org/") is a
comprehensive management tool for PostgreSQL databases that simplifies connecting to and
administering your RDS for PostgreSQL DB instance. Use the following steps to configure your
connection and interact with your database.

###### To connect to a PostgreSQL DB instance

1. Launch pgAdmin on your system.
2. Choose **Add New Server**.
3. In the **General** tab, enter a name for the connection. For
   example, "My RDS instance".
4. In the **Connection** tab, configure the following settings:
   - **Host**: Enter the endpoint from the
     AWS Management Console.
   - **Port**: Use the port number provided (typically
     5432).
   - **Username**: Enter the master username for your DB
     instance.
   - **Password**: Provide the password you set during
     instance creation.

   ![Database connection settings form with host, port, database name, and authentication fields.](images/connect-postgres.png)

5. Save the configuration and connect in order to view and manage your database.

For comprehensive documentation, see [Connecting to a DB
instance running the PostgreSQL database engine](../UserGuide/USER_ConnectToPostgreSQLInstance.md "../UserGuide/USER_ConnectToPostgreSQLInstance.md") in the _Amazon RDS User
Guide_.

## Connecting to other database engines

In addition to PostgreSQL and MySQL, Amazon RDS supports several other database engines. To
connect to these databases, see the following documentation in the _Amazon RDS User
Guide_.

- **MariaDB**: [Connecting to your
  MariaDB DB instance](../UserGuide/USER_ConnectToMariaDBInstance.md "../UserGuide/USER_ConnectToMariaDBInstance.md")
- **Microsoft SQL Server**: [Connecting to your Microsoft SQL Server DB instance](../UserGuide/USER_ConnectToMicrosoftSQLServerInstance.md "../UserGuide/USER_ConnectToMicrosoftSQLServerInstance.md")
- **Oracle**: [Connecting to your
  Oracle DB instance](../UserGuide/USER_ConnectToOracleInstance.md "../UserGuide/USER_ConnectToOracleInstance.md")
- **IBM Db2**: [Connecting to your
  Db2 DB instance](../UserGuide/USER_ConnectToDb2DBInstance.md "../UserGuide/USER_ConnectToDb2DBInstance.md")

Each database engine has specific requirements and configuration options. These topics
provide instructions to help you establish a secure connection to your DB instance.

For a comprehensive overview of all supported database engines and their features, see
the [Amazon RDS features](https://aws.amazon.com/rds/features/ "https://aws.amazon.com/rds/features/").

## Next steps

At this stage, you have successfully created and connected to your RDS DB instance. From
here, you can explore management strategies such as backing up, monitoring, optimizing, and
scaling your DB instance.

Additionally, consider reviewing resources that provide practical guidance on advanced
configurations, performance tuning, security enhancements, and cost management
strategies.

**Next steps:**

- [Managing your Amazon RDS DB instance](managing.md "managing.md")
- [Optimizing and scaling your Amazon RDS DB instance](advanced.md "advanced.md")
- [Additional resources for Amazon RDS](additional-resources.md "additional-resources.md")
