

# Upgrading to Aurora MySQL version 8.4
<a name="AuroraMySQL.mysql84-upgrade-procedure"></a>

You can upgrade from Aurora MySQL version 3 to version 8.4 using an in-place major version upgrade. Direct upgrades from Aurora MySQL version 2 to version 8.4 are not supported. If you are running version 2, you must first upgrade to version 3.

For general information about the major version upgrade process, see [Upgrading the major version of an Amazon Aurora MySQL DB cluster](AuroraMySQL.Updates.MajorVersionUpgrade.md).

## Before upgrading to version 8.4
<a name="AuroraMySQL.mysql84-upgrade-before"></a>

Before you upgrade, complete the following preparation steps:

Aurora runs upgrade prechecks automatically before the upgrade begins. These prechecks identify compatibility issues that can block the upgrade. For details about each precheck, see [Precheck descriptions for upgrading Aurora MySQL version 3 to version 8.4](AuroraMySQL.upgrade-prechecks-v3-to-v84.descriptions.md).

1. **Migrate authentication plugins.** Review all database users and migrate any users using `mysql_native_password` to `caching_sha2_password`. In Aurora MySQL version 8.4, the `mysql_native_password` plugin is still supported but deprecated. The default `authentication_policy` is `*:caching_sha2_password`, so new users are created with `caching_sha2_password` by default.

   ```
   -- Find users using mysql_native_password
   SELECT user, host, plugin FROM mysql.user WHERE plugin = 'mysql_native_password';
   
   -- Migrate a user to caching_sha2_password
   ALTER USER '{{username}}'@'{{host}}' IDENTIFIED WITH caching_sha2_password BY '{{new_password}}';
   ```

1. **Update replication SQL statements.** If your applications or scripts use deprecated replication statements (such as `SHOW SLAVE STATUS` or `CHANGE MASTER TO`), update them to use the replacement statements. These old statements return syntax errors in version 8.4. For the full list, see [Comparing Aurora MySQL version 3 and Aurora MySQL version 8.4](AuroraMySQL.Compare-v3-v84.md).

1. **Check for removed parameters.** If your custom parameter groups use parameters removed in version 8.4 (such as `expire_logs_days` or `default_authentication_plugin`), create new MySQL 8.4–compatible parameter groups with the replacement parameters. Apply any necessary custom parameter values to the new parameter groups. For details, see [Comparing Aurora MySQL version 3 and Aurora MySQL version 8.4](AuroraMySQL.Compare-v3-v84.md).

1. **Check for incompatible SQL syntax.** Review your application code for removed syntax such as `LOW_PRIORITY` with `LOCK TABLES ... WRITE`, and `AUTO_INCREMENT` on `FLOAT` or `DOUBLE` columns.

1. **Check foreign key constraints.** If your schema uses foreign keys that reference non-unique keys, note that creating new such foreign keys is blocked by default in version 8.4. Existing foreign keys continue to work, but new ones require setting `restrict_fk_on_non_standard_key=OFF`.

1. **Check for new reserved keywords.** Verify that your database objects don't use any of the new reserved keywords added in MySQL 8.4 as unquoted identifiers.

1. **Test the upgrade.** We recommend testing the upgrade on a clone of your production cluster before upgrading the production cluster itself.

1. **Review security considerations.** Review authentication plugin changes, TLS and cipher changes, password policies, the `validate_password` component, and new dynamic privileges before upgrading. For details about these changes and upgrade prechecks, see [Security considerations for upgrading from Aurora MySQL version 3 to version 8.4](AuroraMySQL.Upgrade-v3-v84-security.md).

## How to upgrade to version 8.4
<a name="AuroraMySQL.mysql84-upgrade-how"></a>

To perform the upgrade, follow the in-place major version upgrade procedure described in [Upgrading the major version of an Amazon Aurora MySQL DB cluster](AuroraMySQL.Updates.MajorVersionUpgrade.md). Select the target version 8.4 engine version when modifying your DB cluster.

Alternatively, you can use a [Using Amazon Aurora Blue/Green Deployments for database updates](blue-green-deployments.md) to upgrade with minimal downtime. A Blue/Green deployment creates a staging environment that runs the new version alongside your current production environment, allowing you to test and validate before switching over.

After the upgrade completes, perform the post-upgrade cleanup steps described in [Post-upgrade cleanup for Aurora MySQL version 8.4](AuroraMySQL.mysql84-post-upgrade.md).