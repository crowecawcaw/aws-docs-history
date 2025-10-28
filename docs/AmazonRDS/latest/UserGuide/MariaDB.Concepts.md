# MariaDB features not supported by Amazon RDS

The following MariaDB features are not supported on Amazon RDS:

- S3 storage engine
- Authentication plugin – GSSAPI
- Authentication plugin – Unix Socket
- AWS Key Management encryption plugin
- Delayed replication for MariaDB versions lower than 10.6
- Native MariaDB encryption at rest for InnoDB and Aria

You can enable encryption at rest for a MariaDB DB instance by following the instructions in
[Encrypting Amazon RDS
resources](Overview.md "Overview.md").

- HandlerSocket
- JSON table type for MariaDB versions lower than 10.6
- MariaDB ColumnStore
- MariaDB Galera Cluster
- Multisource replication
- MyRocks storage engine for MariaDB versions lower than 10.6
- Password validation plugin, `simple_password_check`, and
  `cracklib_password_check` for MariaDB versions lower than 11.4
- Spider storage engine
- Sphinx storage engine
- TokuDB storage engine
- Storage engine-specific object attributes, as described in [Engine-defined new Table/Field/Index attributes](http://mariadb.com/kb/en/mariadb/engine-defined-new-tablefieldindex-attributes/ "http://mariadb.com/kb/en/mariadb/engine-defined-new-tablefieldindex-attributes/") in the MariaDB documentation
- Table and tablespace encryption
- Hashicorp Key Management plugin
- Running two upgrades in parallel
  To deliver a managed service experience, Amazon RDS doesn't provide shell access to DB
  instances, and it restricts access to certain system procedures and tables that
  require advanced privileges. Amazon RDS supports access to databases on a DB instance
  using any standard SQL client application. Amazon RDS doesn't allow direct host access to
  a DB instance by using Telnet, Secure Shell (SSH), or Windows Remote Desktop
  Connection.
