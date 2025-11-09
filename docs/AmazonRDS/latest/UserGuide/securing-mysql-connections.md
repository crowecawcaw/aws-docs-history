# Securing MySQL DB instance connections

You can implement robust security measures to protect MySQL DB instances from unauthorized
access and potential threats. Security groups, SSL/TLS encryption, and IAM database
authentication work together to create multiple layers of connection security for your MySQL
DB instances. These security controls help you meet compliance requirements, prevent data
breaches, and maintain secure communication channels between applications and databases. You
can secure your MySQL DB instances by encrypting data in transit, restricting access to
specific IP ranges, and managing user authentication through IAM roles rather than database
passwords.

Security for MySQL DB instances is managed at three levels:

- AWS Identity and Access Management controls who can perform Amazon RDS management actions on DB instances. When
  you connect to AWS using IAM credentials, your IAM account must have IAM
  policies that grant the permissions required to perform Amazon RDS management operations.
  For more information, see [Identity and access management for Amazon RDS](UsingWithRDS.md "UsingWithRDS.md").
- When you create a DB instance, you use a VPC security group to control which
  devices and Amazon EC2 instances can open connections to the endpoint and port of the DB
  instance. These connections can be made using Secure Sockets Layer (SSL) and
  Transport Layer Security (TLS). In addition, firewall rules at your company can
  control whether devices running at your company can open connections to the DB
  instance.
- To authenticate login and permissions for a MySQL DB instance, you can take either
  of the following approaches, or a combination of them:
  - You can take the same approach as with a stand-alone instance of MySQL. Commands
    such as `CREATE USER`, `RENAME USER`, `GRANT`,
    `REVOKE`, and `SET PASSWORD` work just as they do in
    on-premises databases, as does directly modifying database schema tables. However,
    directly modifying the database schema tables isn't a best practice, and starting
    from RDS for MySQL version 8.0.36, it isn't supported. For information, see [Access
    control and account management](https://dev.mysql.com/doc/refman/8.0/en/access-control.html "https://dev.mysql.com/doc/refman/8.0/en/access-control.html") in the MySQL documentation.
  - You can also use IAM database authentication. With IAM database authentication,
    you authenticate to your DB instance by using an IAM user or IAM role and an
    authentication token. An _authentication token_ is a unique value
    that is generated using the Signature Version 4 signing process. By using IAM
    database authentication, you can use the same credentials to control access to your
    AWS resources and your databases. For more information, see [IAM database authentication for MariaDB, MySQL, and PostgreSQL](UsingWithRDS.md "UsingWithRDS.md").
  - Another option is Kerberos authentication for RDS for MySQL. The DB instance works
    with AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) to enable Kerberos authentication. When users
    authenticate with a MySQL DB instance joined to the trusting domain, authentication
    requests are forwarded. Forwarded requests go to the domain directory that you
    create with AWS Directory Service. For more information, see [Using Kerberos authentication for Amazon RDS for MySQL](mysql-kerberos.md "mysql-kerberos.md").
    When you create an Amazon RDS DB instance, the master user has the following default
    privileges:

| Engine version                           | System privilege                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Database role                                                                                                                                                                                     |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RDS for MySQL version 8.4.3 and higher   | `GRANT SELECT`, `INSERT`, `UPDATE`,<br>`DELETE`, `CREATE`, `DROP`,<br>`RELOAD`, `PROCESS`,<br>`REFERENCES`,`INDEX`, `ALTER`,<br>`SHOW DATABASES`, `CREATE TEMPORARY TABLES`,<br>`LOCK TABLES`, `EXECUTE`, `REPLICATION<br>SLAVE`, `REPLICATION CLIENT`, `CREATE<br>VIEW`, `SHOW VIEW`, `CREATE ROUTINE`,<br>`ALTER ROUTINE`, `CREATE USER`,<br>`EVENT`, `TRIGGER`, `CREATE ROLE`,<br>`DROP ROLE`, `APPLICATION_PASSWORD_ADMIN`,<br>`FLUSH_OPTIMIZER_COSTS`, `FLUSH_PRIVILEGES`,<br>`FLUSH_STATUS`, `FLUSH_TABLES`,<br>`FLUSH_USER_RESOURCES`, `ROLE_ADMIN`,<br>`SENSITIVE_VARIABLES_OBSERVER`,<br>`SESSION_VARIABLES_ADMIN`, `SET_ANY_DEFINER`,<br>`SHOW_ROUTINE`, `XA_RECOVER_ADMIN` | `rds_superuser_role`<br>For more information about `rds_superuser_role`, see [Role-based privilege model for RDS for MySQL](Appendix.MySQL.CommonDBATasks.md "Appendix.MySQL.CommonDBATasks.md"). |
| RDS for MySQL version 8.0.36 and higher  | `SELECT`, `INSERT`, `UPDATE`,<br>`DELETE`, `CREATE`, `DROP`,<br>`RELOAD`, `PROCESS`, `REFERENCES`,<br>`INDEX`, `ALTER`, `SHOW DATABASES`,<br>`CREATE TEMPORARY TABLES`, `LOCK TABLES`,<br>`EXECUTE`, `REPLICATION SLAVE`,<br>`REPLICATION CLIENT`, `CREATE VIEW`,<br>`SHOW VIEW`, `CREATE ROUTINE`, `ALTER<br>ROUTINE`, `CREATE USER`, `EVENT`,<br>`TRIGGER`, `CREATE ROLE`, `DROP<br>ROLE`, `APPLICATION_PASSWORD_ADMIN`,<br>`ROLE_ADMIN`, `SET_USER_ID`,<br>`XA_RECOVER_ADMIN`                                                                                                                                                                                                      | `rds_superuser_role`<br>For more information about `rds_superuser_role`, see [Role-based privilege model for RDS for MySQL](Appendix.MySQL.CommonDBATasks.md "Appendix.MySQL.CommonDBATasks.md"). |
| RDS for MySQL versions lower than 8.0.36 | `SELECT`, `INSERT`, `UPDATE`,<br>`DELETE`, `CREATE`, `DROP`,<br>`RELOAD`, `PROCESS`, `REFERENCES`,<br>`INDEX`, `ALTER`, `SHOW DATABASES`,<br>`CREATE TEMPORARY TABLES`, `LOCK TABLES`,<br>`EXECUTE`, `REPLICATION CLIENT`, `CREATE<br>VIEW`, `SHOW VIEW`, `CREATE ROUTINE`,<br>`ALTER ROUTINE`, `CREATE USER`,<br>`EVENT`, `TRIGGER`, `REPLICATION<br>SLAVE`                                                                                                                                                                                                                                                                                                                          | None                                                                                                                                                                                              |

###### Note

Although it is possible to delete the master user on the DB instance, it is not
recommended. To recreate the master user, use the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") RDS API
operation or run the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") AWS CLI command and specify a new master user password
with the appropriate parameter. If the master user does not exist in the instance, the
master user is created with the specified password.

To provide management services for each DB instance, the `rdsadmin` user is
created when the DB instance is created. Attempting to drop, rename, change the password, or
change privileges for the `rdsadmin` account will result in an error.

To allow management of the DB instance, the standard `kill` and
`kill_query` commands have been restricted. The Amazon RDS commands
`rds_kill` and `rds_kill_query` are provided to allow you to end
user sessions or queries on DB instances.
