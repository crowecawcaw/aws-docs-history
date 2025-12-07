# Using Amazon Aurora delegated extension support for PostgreSQL

Using Amazon Aurora delegated extension support for PostgreSQL, you can delegate the extension management to a user who need not be an `rds_superuser`.
With this delegated extension support, a new role called `rds_extension` is created and you must assign this to a user to manage other extensions.
This role can create, update, and drop extensions.

You can specify the extensions that can be installed on your Aurora PostgreSQL DB instance, by listing them in the `rds.allowed_extensions` parameter. For more information,
see [Using PostgreSQL extensions with Amazon RDS for PostgreSQL](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md").

You can restrict the list of extensions available that can be managed by the user with the `rds_extension` role using `rds.allowed_delegated_extensions` parameter.

The delegated extension support is available in the following versions:

- All higher versions
- 15.5 and higher 15 versions
- 14.10 and higher 14 versions
- 13.13 and higher 13 versions
- 12.17 and higher 12 versions

###### Topics

- [Turning on delegate extension support to a user](#AuroraPostgreSQL.delegated_ext_mgmt "#AuroraPostgreSQL.delegated_ext_mgmt")
- [Configuration used in Aurora delegated extension support for PostgreSQL](#AuroraPostgreSQL.delegated_ext_config "#AuroraPostgreSQL.delegated_ext_config")
- [Turning off the support for the delegated extension](#AuroraPostgreSQL.delegated_ext_disable "#AuroraPostgreSQL.delegated_ext_disable")
- [Benefits of using Amazon Aurora delegated extension support](#AuroraPostgreSQL.delegated_ext_benefits "#AuroraPostgreSQL.delegated_ext_benefits")
- [Limitation of Aurora delegated extension support for PostgreSQL](#AuroraPostgreSQL.delegated_ext_limit "#AuroraPostgreSQL.delegated_ext_limit")
- [Permissions required for certain extensions](#AuroraPostgreSQL.delegated_ext_perm "#AuroraPostgreSQL.delegated_ext_perm")
- [Security Considerations](#AuroraPostgreSQL.delegated_ext_sec "#AuroraPostgreSQL.delegated_ext_sec")
- [Drop extension cascade disabled](#AuroraPostgreSQL.delegated_ext_drop "#AuroraPostgreSQL.delegated_ext_drop")
- [Example extensions that can be added using delegated extension support](#AuroraPostgreSQL.delegated_ext_support "#AuroraPostgreSQL.delegated_ext_support")

## Turning on delegate extension support to a user

You must perform the following to enable delegate extension support to a user:

1. Grant `rds_extension` role to a user –
   Connect to the database as `rds_superuser` and execute the following command:

```
Postgres => grant rds_extension to `user_name`;
```

2. Set the list of extensions available for delegated users to manage – The `rds.allowed_delegated_extensions` allows you to specify
   a subset of the available extensions using `rds.allowed_extensions` in the DB cluster parameter. You can perform this at one of the following levels:
   - In the cluster or the instance parameter group, through the AWS Management Console or API. For more information, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
   - Use the following command at the database level:

   ```
   alter database `database_name` set rds.allowed_delegated_extensions = '`extension_name_1`,
                       `extension_name_2`,...`extension_name_n`';
   ```

   - Use the following command at the user level:

   ```
   alter user `user_name` set rds.allowed_delegated_extensions = '`extension_name_1`,
                       `extension_name_2`,...`extension_name_n`';
   ```

###### Note

You need not restart the database after changing the `rds.allowed_delegated_extensions` dynamic parameter. 3. Allow access to the delegated user to objects created
during the extension creation process – Certain extensions
create objects that require additional permissions to be granted before the user
with `rds_extension` role can access them. The
`rds_superuser` must grant the delegated user access to those
objects. One of the options is to use an event trigger to automatically grant
permission to the delegated user.

Example of event trigger

If you want to allow a delegated user with `rds_extension` to use
extensions that require setting permissions on their objects created by the
extension creation, you can customize the below example of an event trigger and add
only the extensions for which you want the delegated users to have access to the
full functionality. This event trigger can be created on template1 (the default
template), therefore all database created from template1 will have that event
trigger. When a delegated user installs the extension, this trigger will
automatically grant ownership on the objects created by the extension.

```

CREATE OR REPLACE FUNCTION create_ext()

  RETURNS event_trigger AS $$

DECLARE

  schemaname TEXT;
  databaseowner TEXT;

  r RECORD;

BEGIN

  IF tg_tag = 'CREATE EXTENSION' and current_user != 'rds_superuser' THEN
    RAISE NOTICE 'SECURITY INVOKER';
    RAISE NOTICE 'user: %', current_user;
    FOR r IN SELECT * FROM pg_catalog.pg_event_trigger_ddl_commands()
    LOOP
        CONTINUE WHEN r.command_tag != 'CREATE EXTENSION' OR r.object_type != 'extension';

        schemaname = (
            SELECT n.nspname
            FROM pg_catalog.pg_extension AS e
            INNER JOIN pg_catalog.pg_namespace AS n
            ON e.extnamespace = n.oid
            WHERE e.oid = r.objid
        );

        databaseowner = (
            SELECT pg_catalog.pg_get_userbyid(d.datdba)
            FROM pg_catalog.pg_database d
            WHERE d.datname = current_database()
        );
        RAISE NOTICE 'Record for event trigger %, objid: %,tag: %, current_user: %, schema: %, database_owenr: %', r.object_identity, r.objid, tg_tag, current_user, schemaname, databaseowner;
        IF r.object_identity = 'address_standardizer_data_us' THEN
            EXECUTE pg_catalog.format('GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE %I.us_gaz TO %I WITH GRANT OPTION;', schemaname, databaseowner);
            EXECUTE pg_catalog.format('GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE %I.us_lex TO %I WITH GRANT OPTION;', schemaname, databaseowner);
            EXECUTE pg_catalog.format('GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE %I.us_rules TO %I WITH GRANT OPTION;', schemaname, databaseowner);
        ELSIF r.object_identity = 'dict_int' THEN
            EXECUTE pg_catalog.format('ALTER TEXT SEARCH DICTIONARY %I.intdict OWNER TO %I;', schemaname, databaseowner);
        ELSIF r.object_identity = 'pg_partman' THEN
            EXECUTE pg_catalog.format('GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE %I.part_config TO %I WITH GRANT OPTION;', schemaname, databaseowner);
            EXECUTE pg_catalog.format('GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE %I.part_config_sub TO %I WITH GRANT OPTION;', schemaname, databaseowner);
            EXECUTE pg_catalog.format('GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE %I.custom_time_partitions TO %I WITH GRANT OPTION;', schemaname, databaseowner);
        ELSIF r.object_identity = 'postgis_topology' THEN
            EXECUTE pg_catalog.format('GRANT SELECT, UPDATE, INSERT, DELETE ON ALL TABLES IN SCHEMA topology TO %I WITH GRANT OPTION;', databaseowner);
            EXECUTE pg_catalog.format('GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA topology TO %I WITH GRANT OPTION;', databaseowner);
            EXECUTE pg_catalog.format('GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA topology TO %I WITH GRANT OPTION;', databaseowner);
            EXECUTE pg_catalog.format('GRANT USAGE ON SCHEMA topology TO %I WITH GRANT OPTION;', databaseowner);
        END IF;
    END LOOP;
  END IF;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE EVENT TRIGGER log_create_ext ON ddl_command_end EXECUTE PROCEDURE create_ext();

```

## Configuration used in Aurora delegated extension support for PostgreSQL

| Configuration Name                           | Description                                                                                                                                                                                                                                                                                                                                                                                            | Default Value | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Who can modify or grant permission |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| `rds.allowed_delegated_extensions`           | This parameter limits the extensions a rds_extension role can manage in a database. It must be a subset of rds.allowed_extensions.                                                                                                                                                                                                                                                                     | empty string  | • By default, this parameter is empty string, which means that no extensions have been delegated to users with `rds_extension`.<br>• Any supported extension can be added if the user has permission to do so. To do this, set the `rds.allowed_delegated_extensions` parameter to a string of comma-separated extension names.<br>By adding a list of extensions to this parameter, you explicitly identify the extensions that the user with the `rds_extension` role can install.<br>• When set to `*`, it means that all extensions listed in `rds_allowed_extensions` are delegated to users with `rds_extension` role.<br>To learn more about setting up this parameter, see [Turning on delegate extension support to a user](#AuroraPostgreSQL.delegated_ext_mgmt "#AuroraPostgreSQL.delegated_ext_mgmt"). | rds_superuser                      |
| `rds.allowed_extensions`                     | This parameter lets the customer limit the extensions that can be installed in the Aurora PostgreSQL DB instance. For more information, see [Restricting installation of PostgreSQL extensions](../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.Extensions.Restriction "../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.Extensions.Restriction") | "\*"          | By default, this parameter is set to "\*", which means that all extensions supported on RDS for PostgreSQL and Aurora PostgreSQL are allowed to be created by users with necessary privileges.<br>Empty means no extensions can be installed in the Aurora PostgreSQL DB instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | administrator                      |
| `rds-delegated_extension_allow_drop_cascade` | This parameter controls the ability for user with `rds_extension` to drop the extension using a cascade option.                                                                                                                                                                                                                                                                                        | off           | By default, `rds-delegated_extension_allow_drop_cascade` is set to `off`. This means that users with `rds_extension` are not allowed to drop an extension using the cascade option.<br>To grant that ability, the `rds.delegated_extension_allow_drop_cascade` parameter should be set to `on`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | rds_superuser                      |

## Turning off the support for the delegated extension

###### Turning off partially

The delegated users can’t create new extensions but can still update existing extensions.

- Reset `rds.allowed_delegated_extensions` to the default value in the DB cluster parameter group.
- Use the following command at the database level:

```
alter database `database_name` reset rds.allowed_delegated_extensions;
```

- Use the following command at the user level:

```
alter user `user_name` reset rds.allowed_delegated_extensions;
```

###### Turning off fully

Revoking `rds_extension` role from a user will revert the user to standard permissions. The user can no longer create, update, or drop extensions.

```
postgres => revoke rds_extension from `user_name`;
```

## Benefits of using Amazon Aurora delegated extension support

By using Amazon Aurora delegated extension support for PostgreSQL, you securely delegate the extension management to users who do not have the `rds_superuser` role.
This feature provides the following benefits:

- You can easily delegate extension management to users of your choice.
- This doesn’t require `rds_superuser` role.
- Provides ability to support different set of extensions for different databases in the same DB cluster.

## Limitation of Aurora delegated extension support for PostgreSQL

- Objects created during the extension creation process may require additional privileges for the extension to function properly.

## Permissions required for certain extensions

In order to create, use, or update the following extensions, the delegated user should have the necessary privileges on the following functions, tables, and schema.

| Extensions that need ownership or permissions | Function                              | Tables                                               | Schema   | Text Search Dictionary | Comment                                       |
| --------------------------------------------- | ------------------------------------- | ---------------------------------------------------- | -------- | ---------------------- | --------------------------------------------- |
| address_standardizer_data_us                  |                                       | us_gaz, us_lex, us_lex, I.us_rules                   |          |                        |                                               |
| amcheck                                       | bt_index_check, bt_index_parent_check |                                                      |          |                        |                                               |
| dict_int                                      |                                       |                                                      |          | intdict                |                                               |
| pg_partman                                    |                                       | custom_time_partitions, part_config, part_config_sub |          |                        |                                               |
| pg_stat_statements                            |                                       |                                                      |          |                        |                                               |
| PostGIS                                       | st_tileenvelope                       | spatial_ref_sys                                      |          |                        |                                               |
| postgis_raster                                |                                       |                                                      |          |                        |                                               |
| postgis_topology                              |                                       | topology, layer                                      | topology |                        | the delegated user Must be the database owner |
| log_fdw                                       | create_foreign_table_for_log_file     |                                                      |          |                        |                                               |
| rds_tools                                     | role_password_encryption_type         |                                                      |          |                        |                                               |
| postgis_tiger_geocoder                        |                                       | geocode_settings_default, geocode_settings           | tiger    |                        |                                               |
| pg_freespacemap                               | pg_freespace                          |                                                      |          |                        |                                               |
| pg_visibility                                 | pg_visibility                         |                                                      |          |                        |                                               |

## Security Considerations

Keep in mind that a user with `rds_extension` role will be able to manage extensions on all databases they have the connect privilege on. If the intention is to have a delegated user manage
extension on a single database, a good practice is to revoke all privileges from public on each database, then explicitly grant the connect privilege for that specific database to the delegate user.

There are several extensions that can allow a user to access information from multiple database. Ensure the users you grant `rds_extension` has cross database capabilities before adding these
extensions to `rds.allowed_delegated_extensions`. For example, `postgres_fdw` and `dblink` provide functionality to query across databases on the same instance or remote instances.
`log_fdw` reads the postgres engine log files, which are for all databases in the instance, potentially containing slow queries or error messages from multiple databases. `pg_cron` enables running
scheduled background jobs on the DB instance and can configure jobs to run in a different database.

## Drop extension cascade disabled

The ability to drop the extension with cascade option by a user with the `rds_extension` role is controlled by `rds.delegated_extension_allow_drop_cascade` parameter.
By default, `rds-delegated_extension_allow_drop_cascade` is set to `off`. This means that users with the `rds_extension` role are not allowed to drop an extension using the cascade option
as shown in the below query.

```
DROP EXTENSION CASCADE;
```

As this will automatically drop objects that depend on the extension, and in turn all objects that depend on those objects. Attempting to use the cascade option will result in an error.

To grant that ability, the `rds.delegated_extension_allow_drop_cascade` parameter should be set to `on`.

Changing the `rds.delegated_extension_allow_drop_cascade` dynamic parameter doesn't require a database restart. You can do this at one of the following levels:

- In the cluster or the instance parameter group, through the AWS Management Console or API.
- Using the following command at the database level:

```
alter database `database_name` set rds.delegated_extension_allow_drop_cascade = 'on';
```

- Using the following command at the user level:

```
alter role tenant_user set rds.delegated_extension_allow_drop_cascade = 'on';
```

## Example extensions that can be added using delegated extension support

- `rds_tools`

```
extension_test_db=> create extension rds_tools;
CREATE EXTENSION
extension_test_db=> SELECT * from rds_tools.role_password_encryption_type() where rolname = 'pg_read_server_files';
ERROR: permission denied for function role_password_encryption_type
```

- `amcheck`

```
extension_test_db=> CREATE TABLE amcheck_test (id int);
CREATE TABLE
extension_test_db=> INSERT INTO amcheck_test VALUES (generate_series(1,100000));
INSERT 0 100000
extension_test_db=> CREATE INDEX amcheck_test_btree_idx ON amcheck_test USING btree (id);
CREATE INDEX
extension_test_db=> create extension amcheck;
CREATE EXTENSION
extension_test_db=> SELECT bt_index_check('amcheck_test_btree_idx'::regclass);
ERROR: permission denied for function bt_index_check
extension_test_db=> SELECT bt_index_parent_check('amcheck_test_btree_idx'::regclass);
ERROR: permission denied for function bt_index_parent_check
```

- `pg_freespacemap`

```
extension_test_db=> create extension pg_freespacemap;
CREATE EXTENSION
extension_test_db=> SELECT * FROM pg_freespace('pg_authid');
ERROR: permission denied for function pg_freespace
extension_test_db=> SELECT * FROM pg_freespace('pg_authid',0);
ERROR: permission denied for function pg_freespace
```

- `pg_visibility`

```
extension_test_db=> create extension pg_visibility;
CREATE EXTENSION
extension_test_db=> select * from pg_visibility('pg_database'::regclass);
ERROR: permission denied for function pg_visibility

```

- `postgres_fdw`

```
extension_test_db=> create extension postgres_fdw;
CREATE EXTENSION
extension_test_db=> create server myserver foreign data wrapper postgres_fdw options (host 'foo', dbname 'foodb', port '5432');
ERROR: permission denied for foreign-data wrapper postgres_fdw
```
