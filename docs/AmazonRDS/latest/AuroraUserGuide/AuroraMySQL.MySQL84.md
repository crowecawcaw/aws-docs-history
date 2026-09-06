

# Aurora MySQL version 8.4 compatible with MySQL 8.4
<a name="AuroraMySQL.MySQL84"></a>

 Aurora MySQL version 8.4 is the latest major version of Amazon Aurora MySQL-Compatible Edition, compatible with MySQL 8.4 Community Edition. You can use Aurora MySQL version 8.4 to get the latest MySQL-compatible features, performance enhancements, and bug fixes. 

 Aurora MySQL version 8.4 supports the same Aurora features as the latest Aurora MySQL version 3 releases, with the following exceptions: 
+ Fast insert is not available in Aurora MySQL version 8.4.

 Aurora MySQL version 8.4 uses a simplified version numbering scheme. The version number follows a `{{major-version}}.{{minor-version}}` format, where the major version (such as `8.4`) represents MySQL compatibility and the minor version represents the feature and bug fix release. For example, `8.4.7` is the first minor version in the 8.4 major version family. For more information, see [Checking Aurora MySQL version numbers](AuroraMySQL.Updates.Versions.md). 

**Topics**
+ [Features from MySQL 8.4 Community Edition](#AuroraMySQL.8.4-features-community)
+ [Features removed in MySQL 8.4](#AuroraMySQL.8.4-features-removed)
+ [Security enhancements in Aurora MySQL version 8.4](#AuroraMySQL.8.4-security-features)
+ [Release notes for Aurora MySQL version 8.4](#AuroraMySQL.8.4-release-notes)
+ [Upgrading to Aurora MySQL version 8.4](AuroraMySQL.mysql84-upgrade-procedure.md)
+ [Post-upgrade cleanup for Aurora MySQL version 8.4](AuroraMySQL.mysql84-post-upgrade.md)
+ [Comparing Aurora MySQL version 3 and Aurora MySQL version 8.4](AuroraMySQL.Compare-v3-v84.md)
+ [Comparing Aurora MySQL version 8.4 and MySQL 8.4 Community Edition](AuroraMySQL.Compare-v84-community.md)
+ [Security considerations for upgrading from Aurora MySQL version 3 to version 8.4](AuroraMySQL.Upgrade-v3-v84-security.md)

## Features from MySQL 8.4 Community Edition
<a name="AuroraMySQL.8.4-features-community"></a>

Aurora MySQL version 8.4 is compatible with MySQL 8.4 Community Edition. MySQL 8.4 is a Long-Term Support (LTS) release that builds on MySQL 8.0 with the following key changes:
+ The `mysql_native_password` authentication plugin is enabled by default but the setting is not modifiable. The default `authentication_policy` is `*:caching_sha2_password`, so new users are created with `caching_sha2_password` by default. Users authenticating with `mysql_native_password` will continue working after upgrading, but we recommend migrating to `caching_sha2_password`.
+ Non-inclusive replication terminology is enforced. Older SQL statements such as `SHOW SLAVE STATUS`, `CHANGE MASTER TO`, and `START SLAVE` now return syntax errors. Use the replacement statements such as `SHOW REPLICA STATUS`, `CHANGE REPLICATION SOURCE TO`, and `START REPLICA` instead.
+ Hash table optimization for `EXCEPT` and `INTERSECT` set operations, improving performance for these queries.
+ In Aurora MySQL version 8.4.7 and higher, automatic histogram updates are disabled. If you specify `AUTO UPDATE` when creating or altering a histogram, Aurora MySQL issues a warning and treats the histogram as `MANUAL UPDATE`. Continue to refresh histogram statistics by running `ANALYZE TABLE {{table_name}} UPDATE HISTOGRAM ON {{column_name}}`.
+ Several parameters now have dynamic defaults that scale based on instance memory and CPU cores, including `temptable_max_ram` (now 3% of total memory) and `innodb_buffer_pool_instances`.
+ The `SET_USER_ID` privilege is replaced by two new privileges: `SET_ANY_DEFINER` and `ALLOW_NONEXISTENT_DEFINER`. Two additional new privileges are also introduced: `FLUSH_PRIVILEGES` and `OPTIMIZE_LOCAL_TABLE`.
+ Foreign keys referencing non-unique keys are now blocked by default, controlled by the `restrict_fk_on_non_standard_key` parameter.

For the full list of changes in MySQL 8.4, see [What Is New in MySQL 8.4](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html) in the *MySQL Reference Manual*.

**Important**  
Before upgrading to Aurora MySQL version 8.4, review your database users and ensure they are using the `caching_sha2_password` authentication plugin. In Aurora MySQL version 8.4, the `mysql_native_password` plugin is enabled by default and this setting is not modifiable by customers. When you upgrade from version 3, existing accounts that use `mysql_native_password` continue to work. However, the default `authentication_policy` is `*:caching_sha2_password`, so we recommend migrating users to `caching_sha2_password` before upgrading. For more information about the `authentication_policy` parameter, see [Authentication plugin management](AuroraMySQL.Compare-v3-v84.md#AuroraMySQL.Compare-v3-v84.auth-plugin) and [Authentication policy (new in 8.4)](AuroraMySQL.Upgrade-v3-v84-security.md#AuroraMySQL.Upgrade-v3-v84-security.auth-policy).

## Features removed in MySQL 8.4
<a name="AuroraMySQL.8.4-features-removed"></a>

The following features that were deprecated in MySQL 8.0 have been removed in MySQL 8.4:
+ The `mysql_native_password` authentication plugin is enabled by default in Aurora MySQL version 8.4, and this setting is not modifiable. The default `authentication_policy` is `*:caching_sha2_password`, so new users are created with `caching_sha2_password` by default. In community MySQL 8.4, `mysql_native_password` is disabled by default. Aurora MySQL 8.4 differs in that the plugin remains enabled to preserve compatibility with existing users.
+ Non-inclusive replication SQL statements are removed. Statements such as `CHANGE MASTER TO`, `SHOW SLAVE STATUS`, `START SLAVE`, `STOP SLAVE`, `SHOW SLAVE HOSTS`, `RESET SLAVE`, `RESET MASTER`, `SHOW MASTER STATUS`, and `PURGE MASTER LOGS` now return syntax errors. Use the replacement statements instead.
+ The `INFORMATION_SCHEMA.TABLESPACES` table has been removed.
+ The `LOW_PRIORITY` modifier with `LOCK TABLES ... WRITE` now causes a syntax error.
+ The `AUTO_INCREMENT` modifier with `FLOAT` and `DOUBLE` columns is no longer supported.
+ The `SET_USER_ID` privilege has been removed. Use `SET_ANY_DEFINER` and `ALLOW_NONEXISTENT_DEFINER` instead.
+ The `expire_logs_days` parameter has been removed. Use `binlog_expire_logs_seconds` instead.
+ Weak TLS ciphers that do not provide perfect forward secrecy or do not use SHA2 are no longer allowed for encrypted connections.

For the full list of removals, see [Features Removed in MySQL 8.4](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html#mysql-nutshell-removals) in the *MySQL Reference Manual*.

## Security enhancements in Aurora MySQL version 8.4
<a name="AuroraMySQL.8.4-security-features"></a>

Aurora MySQL version 8.4 introduces several security enhancements and changes, including the following:
+ Enhanced authentication with the `authentication_policy` parameter, replacing the `default_authentication_plugin` parameter. For more information, see [Comparing Aurora MySQL version 3 and Aurora MySQL version 8.4](AuroraMySQL.Compare-v3-v84.md).
+ Aurora MySQL version 8.4 enforces stricter cryptographic standards aligned with the latest security requirements on the `ssl_ciphers` (TLS 1.2) and `tls_ciphersuites` (TLS 1.3) DB cluster parameters. For more information, see [Security with Amazon Aurora MySQL](AuroraMySQL.Security.md).
+ Comprehensive password policy support and improved password validation. For more information, see [Password policies and Password validation in Aurora MySQL](AuroraMySQL.PasswordPolicies.md).
+ New dynamic privileges and changes to master user behavior. For more information, see [Master user account privileges](UsingWithRDS.MasterAccounts.md).

For the full list of changes in MySQL 8.4 community edition, see [MySQL 8.4 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/) in the *MySQL Reference Manual*.

## Release notes for Aurora MySQL version 8.4
<a name="AuroraMySQL.8.4-release-notes"></a>

 For the release notes for all Aurora MySQL version 8.4 releases, see [ Database engine updates for Amazon Aurora MySQL version 8.4](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.84Updates.html) in the *Release Notes for Aurora MySQL*. 