# Connecting from the MySQL command-line client (unencrypted) for RDS for MariaDB

###### Important

Only use an unencrypted MySQL connection when the client and server are in the same VPC
and the network is trusted. For information about using encrypted connections, see
[Connecting to your MariaDB DB
instance on Amazon RDS with SSL/TLS from the MySQL command-line client
(encrypted)](USER_ConnectToMariaDBInstanceSSL.md "USER_ConnectToMariaDBInstanceSSL.md").

To connect to a DB instance using the MySQL command-line client, enter the following command at a
command prompt on a client computer. Doing this connects you to a database on a MariaDB
DB instance. Substitute the DNS name (endpoint) for your DB instance for
`<endpoint>` and the master user name that you used for
`<mymasteruser>`. Provide the master password that
you used when prompted for a password.

```
mysql -h `<endpoint>` -P 3306 -u `<mymasteruser>` -p
```

After you enter the password for the user, you see output similar to the
following.

```
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 31
Server version: 10.6.10-MariaDB-log Source distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```
