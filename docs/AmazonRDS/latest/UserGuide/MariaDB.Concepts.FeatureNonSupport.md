

# MariaDB features not supported by Amazon RDS
<a name="MariaDB.Concepts.FeatureNonSupport"></a>

The following MariaDB features are not supported on Amazon RDS:
+ S3 storage engine
+ Authentication plugin – GSSAPI
+ Authentication plugin – Unix Socket
+ AWS Key Management encryption plugin
+ Delayed replication for MariaDB versions lower than 10.6
+ Native MariaDB encryption at rest for InnoDB and Aria

  You can enable encryption at rest for a MariaDB DB instance by following the instructions in [Encrypting Amazon RDS resources](Overview.Encryption.md).
+ HandlerSocket
+ JSON table type for MariaDB versions lower than 10.6
+ MariaDB ColumnStore
+ MariaDB Galera Cluster
+ Multisource replication
+ MyRocks storage engine for MariaDB versions lower than 10.6
+ Password validation plugin, `simple_password_check`, and `cracklib_password_check` for MariaDB versions lower than 11.4 
+ New binary log implementation in InnoDB for MariaDB version 12.3

  RDS for MariaDB doesn't support the binary log implementation in InnoDB that MariaDB 12.3 introduces. The `binlog_storage_engine` parameter isn't available in the `mariadb12.3` parameter group family. For more information about this community feature, see [New binlog implementation in MariaDB 12.3](https://mariadb.org/new-binlog-implementation-in-mariadb-12-3/) on the MariaDB website.
+ The `PATH` variable isn't available in the `mariadb12.3` parameter group family, and you can't set it as a global variable. You can still set `PATH` at the session level.
+ Replication user information in the output of `SHOW REPLICA HOSTS`

  The `show_slave_auth_info` variable isn't available in the `mariadb12.3` parameter group family, so the output of `SHOW REPLICA HOSTS` doesn't include user and password information.
+ Spider storage engine
+ Sphinx storage engine
+ TokuDB storage engine
+ Storage engine-specific object attributes, as described in [ Engine-defined new Table/Field/Index attributes](http://mariadb.com/kb/en/mariadb/engine-defined-new-tablefieldindex-attributes/) in the MariaDB documentation
+ Table and tablespace encryption
+ Hashicorp Key Management plugin
+ Running two upgrades in parallel

To deliver a managed service experience, Amazon RDS doesn't provide shell access to DB instances, and it restricts access to certain system procedures and tables that require advanced privileges. Amazon RDS supports access to databases on a DB instance using any standard SQL client application. Amazon RDS doesn't allow direct host access to a DB instance by using Telnet, Secure Shell (SSH), or Windows Remote Desktop Connection. 