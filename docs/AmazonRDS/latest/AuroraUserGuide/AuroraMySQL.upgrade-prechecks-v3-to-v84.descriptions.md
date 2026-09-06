

# Precheck descriptions for upgrading Aurora MySQL version 3 to version 8.4
<a name="AuroraMySQL.upgrade-prechecks-v3-to-v84.descriptions"></a>

The following prechecks run when you upgrade from Aurora MySQL version 3 (compatible with MySQL 8.0) to Aurora MySQL version 8.4 (compatible with MySQL 8.4). These prechecks identify potential compatibility issues before the upgrade begins.

**Contents**
+ [Errors](#precheck-v84-errors)
  + [MySQL prechecks that report errors](#precheck-v84-errors.mysql)
  + [Aurora MySQL prechecks that report errors](#precheck-v84-errors.aurora)
+ [Warnings](#precheck-v84-warnings)
  + [MySQL prechecks that report warnings](#precheck-v84-warnings.mysql)
  + [Aurora MySQL prechecks that report warnings](#precheck-v84-warnings.aurora)
+ [Notices](#precheck-v84-notices)
+ [Errors, warnings, or notices](#precheck-v84-all)

## Errors
<a name="precheck-v84-errors"></a>

The following prechecks generate errors when the precheck fails, and the upgrade can't proceed.

**Topics**
+ [MySQL prechecks that report errors](#precheck-v84-errors.mysql)
+ [Aurora MySQL prechecks that report errors](#precheck-v84-errors.aurora)

### MySQL prechecks that report errors
<a name="precheck-v84-errors.mysql"></a>

The following prechecks are from Community MySQL:
+ [deprecatedRouterAuthMethod](#v84-deprecatedRouterAuthMethod)
+ [partitionsWithPrefixKeys](#v84-partitionsWithPrefixKeys)
+ [columnDefinition](#v84-columnDefinition)

**deprecatedRouterAuthMethod**  
**Precheck level: Error**  
**Check for deprecated or invalid authentication methods in use by MySQL Router internal accounts**  
This precheck validates that MySQL Router internal accounts are not using deprecated or invalid authentication methods that may be removed or changed in MySQL 8.4. MySQL Router accounts are automatically created at bootstrap time when the Router is not instructed to use an existing account.  
**Example output:**  

```
{
  "id": "deprecatedRouterAuthMethod",
  "title": "Check for deprecated or invalid authentication methods in use by MySQL Router internal accounts.",
  "status": "OK",
  "description": "Warning: The following accounts are MySQL Router accounts that use a deprecated authentication method.\nThose accounts are automatically created at bootstrap time when the Router is not instructed to use an existing account. Please upgrade MySQL Router to the latest version to ensure deprecated authentication methods are no longer used.\nSince version 8.0.19 it's also possible to instruct MySQL Router to use a dedicated account. That account can be created using the AdminAPI.",
  "documentationLink": "https://dev.mysql.com/doc/mysql-shell/en/configuring-router-user.html https://dev.mysql.com/doc/mysql-router/en/mysqlrouter.html#option_mysqlrouter_account",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "mysql_router_test@%",
        "description": " - router user with deprecated authentication method."
      }
  ]
}
```
The precheck returns an error because the `mysql_router_test` account is using a deprecated authentication method such as `mysql_native_password` or `sha256_password`.  
To verify the authentication method in use:  

```
SELECT user, host, plugin FROM mysql.user WHERE user = 'mysql_router_test';
```
**Resolution:**  
Update the MySQL Router account to use `caching_sha2_password` authentication:  

```
ALTER USER 'mysql_router_test'@'%' IDENTIFIED WITH caching_sha2_password BY '{{new_password}}';
```
Alternatively, upgrade MySQL Router to the latest version to ensure deprecated authentication methods are no longer used. Since version 8.0.19, you can also instruct MySQL Router to use a dedicated account created using the AdminAPI.

**partitionsWithPrefixKeys**  
**Precheck level: Error**  
**Checks for partitions by key using columns with prefix key indexes**  
This precheck identifies partitioned tables that use columns with prefix key indexes in their partitioning key. Indexes on column prefixes are not supported for key partitioning—they are ignored by the partition function and are not allowed as of MySQL 8.4.0.  
For more information, see [Restrictions and limitations on partitioning](https://dev.mysql.com/doc/refman/en/partitioning-limitations.html) in the MySQL documentation.  
**Example output:**  

```
{
  "id": "partitionsWithPrefixKeys",
  "title": "Checks for partitions by key using columns with prefix key indexes",
  "status": "OK",
  "description": "Indexes on column prefixes are not supported for key partitioning, they are ignored by the partition function and so they are not allowed as of 8.4.0. This check identifies tables with partitions defined this way, they should be fixed before upgrading to 8.4.0.",
  "documentationLink": "https://dev.mysql.com/doc/refman/en/partitioning-limitations.html",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.test_partition_prefix",
        "description": "Error: the `test`.`test_partition_prefix` table uses partition by KEY using the following columns with prefix index: name."
      }
  ]
}
```
**Resolution:**  

```
-- Check for prefix indexes (Sub_part column shows prefix length)
SHOW INDEX FROM test.test_partition_prefix;

-- Option 1: Change partition to use non-prefix columns only
ALTER TABLE test.test_partition_prefix PARTITION BY KEY (id) PARTITIONS 4;

-- Option 2: Remove prefix from index
ALTER TABLE test.test_partition_prefix
  DROP PRIMARY KEY,
  ADD PRIMARY KEY (id, name);  -- Full column, no prefix

-- Option 3: Remove partitioning
ALTER TABLE test.test_partition_prefix REMOVE PARTITIONING;
```

**columnDefinition**  
**Precheck level: Error**  
**Checks for errors in column definitions**  
This precheck validates that all column definitions are compatible with MySQL 8.4 requirements. It specifically identifies columns of type `FLOAT` or `DOUBLE` with the `AUTO_INCREMENT` flag set, which is no longer supported in MySQL 8.4.  
**Example output:**  

```
{
  "id": "columnDefinition",
  "title": "Checks for errors in column definitions",
  "status": "OK",
  "description": "Identifies column definitions that may not be supported in future versions of MySQL",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.test_column_def.id",
        "description": "The column is of type FLOAT and has the AUTO_INCREMENT flag set, this is no longer supported."
      }
  ]
}
```
**Resolution:**  
Change the column type from `FLOAT` or `DOUBLE` to an integer type:  

```
-- Check current definition
SHOW CREATE TABLE test.test_column_def\G

-- Change FLOAT AUTO_INCREMENT to BIGINT AUTO_INCREMENT
ALTER TABLE test.test_column_def MODIFY COLUMN id BIGINT NOT NULL AUTO_INCREMENT;

-- Verify
SHOW CREATE TABLE test.test_column_def\G
```

### Aurora MySQL prechecks that report errors
<a name="precheck-v84-errors.aurora"></a>

The following prechecks are specific to Aurora MySQL:
+ [auroraUnsupportedPluginsCheck](#v84-auroraUnsupportedPluginsCheck)
+ [auroraUnsupportedComponentsCheck](#v84-auroraUnsupportedComponentsCheck)
+ [auroraUpgradeCheckForSysSchemaObjectTypeMismatch](#v84-auroraUpgradeCheckForSysSchemaObjectTypeMismatch)

**auroraUnsupportedPluginsCheck**  
**Precheck level: Error**  
**Check for unsupported plugins**  
This Aurora-specific precheck identifies plugins that are not supported in Aurora MySQL version 8.4. Aurora has specific plugin compatibility requirements that differ from community MySQL.  
**Example output:**  

```
{
  "id": "auroraUnsupportedPluginsCheck",
  "title": "Check for unsupported plugins",
  "status": "OK",
  "description": "Checks for unsupported plugins installed in the database",
  "documentationLink": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "all",
        "description": "Plugin simple_parser loaded in the engine. To proceed with the upgrade, remove this plugin."
      }
  ]
}
```
**Resolution:**  
Uninstall the unsupported plugins:  

```
UNINSTALL PLUGIN {{plugin_name}};
```

**auroraUnsupportedComponentsCheck**  
**Precheck level: Error**  
**Check for unsupported components**  
This precheck validates that no MySQL components that are unsupported in Aurora MySQL version 8.4 are currently installed or active. Components are different from plugins and provide extended functionality through the component infrastructure.  
**Example output:**  

```
{
  "id": "auroraUnsupportedComponentsCheck",
  "title": "Check for unsupported components",
  "status": "OK",
  "description": "Checks for unsupported components installed in the database",
  "documentationLink": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "all",
        "description": "Component file://component_log_sink_json loaded in the engine. To proceed with the upgrade, uninstall this component."
      }
  ]
}
```
**Resolution:**  
Uninstall the unsupported components:  

```
UNINSTALL COMPONENT '{{component_name}}';
```

**auroraUpgradeCheckForSysSchemaObjectTypeMismatch**  
**Precheck level: Error**  
**Check object type mismatch for sys schema**  
This precheck validates that all objects in the `sys` schema have the correct object types and definitions. The sys schema is a system schema that provides views and procedures for database monitoring and diagnostics. Mismatches can occur if the schema was manually modified or corrupted.  
**Example output:**  

```
{
  "id": "auroraUpgradeCheckForSysSchemaObjectTypeMismatch",
  "title": "Check object type mismatch for sys schema.",
  "status": "OK",
  "description": "Database contains objects with type mismatch for sys schema.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "sys.host_summary",
        "description": "Your object sys.host_summary has a type mismatch. To fix the inconsistency we recommend to rename or remove the object before upgrading (use RENAME TABLE command)."
      }
  ]
}
```
**Resolution:**  

```
-- Check the object type
SELECT TABLE_NAME, TABLE_TYPE FROM information_schema.tables
WHERE TABLE_SCHEMA = 'sys' AND TABLE_NAME = 'host_summary';

-- Option 1: Rename the mismatched object
RENAME TABLE sys.host_summary TO sys.host_summary_backup;

-- Option 2: Drop the mismatched object
DROP TABLE sys.host_summary;
```

## Warnings
<a name="precheck-v84-warnings"></a>

The following prechecks generate warnings when the precheck fails, but the upgrade can proceed.

**Topics**
+ [MySQL prechecks that report warnings](#precheck-v84-warnings.mysql)
+ [Aurora MySQL prechecks that report warnings](#precheck-v84-warnings.aurora)

### MySQL prechecks that report warnings
<a name="precheck-v84-warnings.mysql"></a>

The following prechecks are from Community MySQL:
+ [deprecatedDefaultAuth](#v84-deprecatedDefaultAuth)
+ [foreignKeyReferences](#v84-foreignKeyReferences)

**deprecatedDefaultAuth**  
**Precheck level: Warning**  
**Check for deprecated or invalid default authentication methods in system variables**  
This precheck validates that the `default_authentication_plugin` system variable is not set to deprecated authentication methods.  
MySQL 8.4.0 removes the deprecated `default_authentication_plugin` option entirely. The `mysql_native_password` plugin is disabled by default as of MySQL 8.4.0 and is subject to removal in a future version.
For more information about authentication changes in version 8.4, see [Security considerations for upgrading from Aurora MySQL version 3 to version 8.4](AuroraMySQL.Upgrade-v3-v84-security.md).  
**Example output:**  

```
{
  "id": "deprecatedDefaultAuth",
  "title": "Check for deprecated or invalid default authentication methods in system variables.",
  "status": "OK",
  "description": "The following variables have problems with their set authentication method:",
  "detectedProblems": [
      {
        "level": "Warning",
        "dbObject": "default_authentication_plugin",
        "description": "mysql_native_password authentication method is deprecated and it should be considered to correct this before upgrading to 8.4.0 release."
      },
      {
        "level": "Warning",
        "dbObject": "authentication_policy",
        "description": "mysql_native_password authentication method is deprecated and it should be considered to correct this before upgrading to 8.4.0 release."
      }
  ]
}
```
**Resolution:**  
Update the authentication system variables to use `caching_sha2_password`:  

1. Go to the Amazon RDS console and navigate to **Parameter groups**.

1. Select your DB cluster parameter group.

1. Modify the following parameters:
   + `default_authentication_plugin` = `caching_sha2_password`
   + `authentication_policy` = `caching_sha2_password,*,`

1. Apply the changes. A reboot may be required.
Ensure your application clients support `caching_sha2_password` authentication before making this change. Some older MySQL client libraries may not support this authentication method.

**foreignKeyReferences**  
**Precheck level: Warning**  
**Checks for foreign keys not referencing a full unique index**  
This precheck ensures that all foreign key constraints reference complete unique or primary key indexes. Foreign keys to partial indexes may be forbidden as of MySQL 8.4.0.  
**Example output:**  

```
{
  "id": "foreignKeyReferences",
  "title": "Checks for foreign keys not referencing a full unique index",
  "status": "OK",
  "description": "Foreign keys to partial indexes may be forbidden as of 8.4.0, this check identifies such cases to warn the user.",
  "detectedProblems": [
      {
        "level": "Warning",
        "dbObject": "sample.child_table_ibfk_1",
        "description": "invalid foreign key defined as 'child_table(parent_name)' references a non unique key at table 'parent_table'."
      }
  ]
}
```
**Resolution:**  
Choose the option that works best with your application:  

```
-- Option 1: Add unique index on parent table (if values are unique)
ALTER TABLE test.parent_table ADD UNIQUE INDEX idx_parent_name_unique (parent_name);

-- Option 2: Drop the foreign key if not needed
ALTER TABLE test.child_table DROP FOREIGN KEY child_table_ibfk_1;
```

### Aurora MySQL prechecks that report warnings
<a name="precheck-v84-warnings.aurora"></a>

The following prechecks are specific to Aurora MySQL:
+ [auroraValidatePasswordPluginCheck](#v84-auroraValidatePasswordPluginCheck)

**auroraValidatePasswordPluginCheck**  
**Precheck level: Warning**  
**Check for deprecated validate\_password plugin**  
This precheck identifies usage of the deprecated `validate_password` plugin. In MySQL 8.0\+, the validate\_password functionality was reimplemented as a component (`component_validate_password`). Aurora MySQL version 8.4 requires migration to the component-based implementation.  
For more information, see [Password validation component migration](AuroraMySQL.Upgrade-v3-v84-security.md#AuroraMySQL.Upgrade-v3-v84-security.validate-password).  
**Example output:**  

```
{
  "id": "auroraValidatePasswordPluginCheck",
  "title": "Check for deprecated validate_password plugin",
  "status": "OK",
  "description": "The validate_password plugin is deprecated in Aurora MySQL 8.4",
  "detectedProblems": [
      {
        "level": "Warning",
        "dbObject": "validate_password",
        "description": "The validate_password plugin is deprecated and will be removed in a future release. It is recommended to transition to the validate_password component."
      }
  ]
}
```
**Resolution:**  

```
-- Check current plugin status
SELECT plugin_name, plugin_status FROM information_schema.plugins
WHERE plugin_name = 'validate_password';

-- Uninstall the plugin
UNINSTALL PLUGIN validate_password;

-- Install the component replacement
INSTALL COMPONENT 'file://component_validate_password';

-- Verify
SELECT * FROM mysql.component WHERE component_urn LIKE '%validate_password%';
```

## Notices
<a name="precheck-v84-notices"></a>

The following precheck generates a notice when the precheck fails, but the upgrade can proceed.
+ [invalidPrivileges](#v84-invalidPrivileges)

**invalidPrivileges**  
**Precheck level: Notice**  
**Checks for user privileges that will be removed**  
This precheck identifies user accounts with privileges that are being removed or modified in MySQL 8.4. The `SET_USER_ID` privilege is being removed as part of the upgrade process. If the privileges are not being used, no action is required. Otherwise, ensure they stop being used before the upgrade because they will be lost.  
**Example output:**  

```
{
  "id": "invalidPrivileges",
  "title": "Checks for user privileges that will be removed",
  "status": "OK",
  "description": "Verifies for users containing grants to be removed as part of the upgrade process.",
  "detectedProblems": [
      {
        "level": "Notice",
        "dbObject": "'test_user'@'localhost'",
        "description": "The user 'test_user'@'localhost' has the following privileges that will be removed as part of the upgrade process: SET_USER_ID"
      }
  ]
}
```
**Resolution:**  
This is an informational notice—no action is required. The `SET_USER_ID` privilege will be automatically removed during the upgrade process.  
However, if your application relies on the `SET_USER_ID` privilege, review and update your application before upgrading.

## Errors, warnings, or notices
<a name="precheck-v84-all"></a>

The following prechecks can return an error, warning, or notice depending on the precheck output.
+ [authMethodUsage](#v84-authMethodUsage)
+ [pluginUsage](#v84-pluginUsage)
+ [checkTableCommand](#v84-checkTableCommand)

**authMethodUsage**  
**Precheck level: Error, Warning, or Notice**  
**Check for deprecated or invalid user authentication methods**  
This precheck identifies user accounts using authentication methods that are deprecated or will be removed in MySQL 8.4. The `mysql_native_password` authentication plugin is deprecated and disabled by default as of MySQL 8.4.0. The plugin is subject to removal in a future version.  
The severity level is dynamic based on the feature lifecycle—Notice before deprecation, Warning after deprecation, Error after removal.  
**Example output:**  

```
{
  "id": "authMethodUsage",
  "title": "Check for deprecated or invalid user authentication methods.",
  "status": "OK",
  "description": "Some users are using authentication methods that may be deprecated or removed, please review the details below.",
  "detectedProblems": [
      {
        "level": "Warning",
        "dbObject": "testuser@localhost",
        "description": ""
      }
  ]
}
```
**Resolution:**  
Update the user accounts to use `caching_sha2_password` authentication:  

```
ALTER USER '{{username}}'@'{{host}}' IDENTIFIED WITH caching_sha2_password BY '{{new_password}}';
```
No action is required for Aurora internal system accounts. They are automatically updated during the upgrade process. Attempting to modify these accounts manually may cause issues with Aurora functionality.

**pluginUsage**  
**Precheck level: Error, Warning, or Notice**  
**Check for deprecated or removed plugin usage**  
This precheck identifies plugins that have been deprecated or removed in MySQL 8.4. It examines all active plugins and reports their deprecation status. The severity level is dynamic based on the feature lifecycle.  
**Example output:**  

```
{
  "id": "pluginUsage",
  "title": "Check for deprecated or removed plugin usage.",
  "status": "OK",
  "description": "The following plugins are ACTIVE and they have been deprecated or removed.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "keyring_file",
        "description": "The 'keyring_file' plugin is removed as of MySQL 8.4.0. It must not be used anymore, please use the 'component_keyring_file' component instead."
      }
  ]
}
```
**Resolution:**  
Uninstall deprecated plugins and install their component replacements:  

```
-- Check installed plugins
SELECT plugin_name, plugin_status FROM information_schema.plugins
WHERE plugin_name IN ('keyring_file', 'keyring_encrypted_file', 'keyring_oci', 'authentication_fido');

-- Uninstall and replace (example for keyring_file)
UNINSTALL PLUGIN keyring_file;
INSTALL COMPONENT 'file://component_keyring_file';

-- Verify
SELECT * FROM mysql.component WHERE component_urn LIKE '%keyring%';
```
The following table lists deprecated plugins and their replacements:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.upgrade-prechecks-v3-to-v84.descriptions.html)

**checkTableCommand**  
**Precheck level: Error, Warning, or Notice**  
**Issues reported by the `check table x for upgrade` command**  
This precheck runs the `CHECK TABLE ... FOR UPGRADE` command on all user tables to identify structural issues, deprecated features, or incompatibilities with MySQL 8.4. The command performs a comprehensive validation of table structure and metadata.  
Unlike other prechecks, it can return an error, warning, or notice depending on the `CHECK TABLE` output. If this precheck returns any tables, review them carefully along with the return code and message before initiating the upgrade.  
**Example output:**  

```
{
  "id": "checkTableCommand",
  "title": "Issues reported by 'check table x for upgrade' command",
  "status": "OK",
  "description": "Issues reported by 'check table x for upgrade' command",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.orphaned_view",
        "description": "View 'test.orphaned_view' references invalid table(s) or column(s) or function(s) or definer/invoker of view lack rights to use them"
      },
      {
        "level": "Error",
        "dbObject": "test.orphaned_view",
        "description": "Corrupt"
      }
  ]
}
```
**Resolution:**  
Review the reported objects and fix or remove them before upgrading. Common issues include:  
+ Views referencing invalid tables or columns—drop or re-create the view.
+ Corrupt tables—run `REPAIR TABLE` or re-create the table.
+ Triggers with missing `CREATED` attribute—re-create the trigger.
For more information, see [CHECK TABLE statement](https://dev.mysql.com/doc/refman/8.4/en/check-table.html) in the MySQL documentation.