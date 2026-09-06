

# Dynamic privileges for RDS for MySQL
<a name="Appendix.MySQL.CommonDBATasks.dynamic-privileges"></a>

Dynamic privileges are MySQL privileges that you can explicitly grant by using the `GRANT` statement. Depending on your version of RDS for MySQL, RDS allows you to grant only specific dynamic privileges. RDS disallows some of these privileges because they can interfere with the specific database operations, such as replication and backup.

The following table shows which of these privileges you can grant for different MySQL versions. If you are upgrading from a MySQL version lower than 8.0.36 to version 8.0.36 or higher, you might have to update your application code if granting a particular privilege is no longer allowed.


| Privilege | MySQL 8.0.35 and lower | MySQL 8.0.36 and higher minor versions | MySQL 8.4.3 and higher | 
| --- | --- | --- | --- | 
| [ALLOW\_NONEXISTENT\_DEFINER](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_allow-nonexistent-definer)  | Not available | Not available | Disallowed | 
| [APPLICATION\_PASSWORD\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_application-password-admin) | Allowed | Allowed | Allowed | 
| [AUDIT\_ABORT\_EXEMPT](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_audit-abort-exempt) | Allowed | Disallowed | Disallowed | 
| [AUDIT\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_audit-admin) | Disallowed | Disallowed | Disallowed | 
| [AUTHENTICATION\_POLICY\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_authentication-policy-admin) | Allowed | Disallowed | Disallowed | 
| [BACKUP\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_backup-admin) | Allowed | Disallowed | Disallowed | 
| [BINLOG\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_binlog-admin) | Allowed | Disallowed | Disallowed | 
| [BINLOG\_ENCRYPTION\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_binlog-encryption-admin) | Disallowed | Disallowed | Disallowed | 
| [CLONE\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_clone-admin) | Disallowed | Disallowed | Disallowed | 
| [CONNECTION\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_connection-admin) | Allowed | Disallowed | Disallowed | 
| [ENCRYPTION\_KEY\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_encryption-key-admin) | Disallowed | Disallowed | Disallowed | 
| [FIREWALL\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_firewall-admin) | Disallowed | Disallowed | Disallowed | 
| [FIREWALL\_EXEMPT](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_firewall-exempt) | Allowed | Disallowed | Disallowed | 
| [FIREWALL\_USER](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_firewall-user) | Disallowed | Disallowed | Disallowed | 
| [FLUSH\_OPTIMIZER\_COSTS](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-optimizer-costs) | Allowed | Allowed | Allowed | 
| [FLUSH\_PRIVILEGES](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_flush-privileges) | Not available | Not available | Allowed | 
| [FLUSH\_STATUS](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-status) | Allowed | Allowed | Allowed | 
| [FLUSH\_TABLES](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-tables) | Allowed | Allowed | Allowed | 
| [FLUSH\_USER\_RESOURCES](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-user-resources) | Allowed | Allowed | Allowed | 
| [GROUP\_REPLICATION\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_group-replication-admin) | Disallowed | Disallowed | Disallowed | 
| [GROUP\_REPLICATION\_STREAM](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_group-replication-stream) | Disallowed | Disallowed | Disallowed | 
| [INNODB\_REDO\_LOG\_ARCHIVE](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_innodb-redo-log-archive) | Disallowed | Disallowed | Disallowed | 
| [INNODB\_REDO\_LOG\_ENABLE](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_innodb-redo-log-enable) | Disallowed | Disallowed | Disallowed | 
| [MASKING\_DICTIONARIES\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_masking-dictionaries-admin) | Disallowed | Disallowed | Disallowed | 
| [NDB\_STORED\_USER](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_ndb-stored-user) | Disallowed | Disallowed | Disallowed | 
| [OPTIMIZE\_LOCAL\_TABLE](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_optimize-local-table) | Not available | Not available | Disallowed | 
| [PASSWORDLESS\_USER\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_passwordless-user-admin) | Disallowed | Disallowed | Disallowed | 
| [PERSIST\_RO\_VARIABLES\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_persist-ro-variables-admin) | Disallowed | Disallowed | Disallowed | 
| [REPLICATION\_APPLIER](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_replication-applier) | Allowed | Disallowed | Disallowed | 
| [REPLICATION\_SLAVE\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_replication-slave-admin) | Disallowed | Disallowed | Disallowed | 
| [RESOURCE\_GROUP\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_resource-group-admin) | Allowed | Disallowed | Disallowed | 
| [RESOURCE\_GROUP\_USER](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_resource-group-user) | Allowed | Disallowed | Disallowed | 
| [ROLE\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_role-admin) | Allowed | Allowed | Allowed | 
| [SENSITIVE\_VARIABLES\_OBSERVER](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_sensitive-variables-observer) | Allowed | Allowed | Allowed | 
| [SERVICE\_CONNECTION\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_service-connection-admin) | Allowed | Disallowed | Disallowed | 
| [SESSION\_VARIABLES\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_session-variables-admin) | Allowed | Allowed | Allowed | 
| [SET\_ANY\_DEFINER](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_set-any-definer) | Not available | Not available | Allowed | 
| [SET\_USER\_ID](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_set-user-id) | Allowed | Allowed | Not available | 
| [SHOW\_ROUTINE](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_show-routine) | Allowed | Allowed | Allowed | 
| [SKIP\_QUERY\_REWRITE](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_skip-query-rewrite) | Disallowed | Disallowed | Disallowed | 
| [SYSTEM\_USER](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_system-user) | Disallowed | Disallowed | Disallowed | 
| [SYSTEM\_VARIABLES\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_system-variables-admin) | Disallowed | Disallowed | Disallowed | 
| [TABLE\_ENCRYPTION\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_table-encryption-admin) | Disallowed | Disallowed | Disallowed | 
| [TELEMETRY\_LOG\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_telemetry-log-admin) | Allowed | Disallowed | Disallowed | 
| [TP\_CONNECTION\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_tp-connection-admin) | Disallowed | Disallowed | Disallowed | 
| [TRANSACTION\_GTID\_TAG](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_transaction-gtid-tag)  | Not available | Not available | Disallowed | 
| [VERSION\_TOKEN\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_version-token-admin) | Disallowed | Disallowed | Disallowed | 
| [XA\_RECOVER\_ADMIN](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_xa-recover-admin) | Allowed | Allowed | Allowed | 