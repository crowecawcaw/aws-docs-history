# Using an Amazon Redshift cluster as a target in DMS Schema Conversion

You can use Amazon Redshift databases as a migration target in DMS Schema Conversion.
For information about supported target databases, see
[Target data providers for DMS Schema Conversion](CHAP_Introduction.md#CHAP_Introduction.Targets.SchemaConversion "CHAP_Introduction.md#CHAP_Introduction.Targets.SchemaConversion").

## Privileges for Amazon Redshift as a target

Using Amazon Redshift as a target for DMS Schema Conversion requires the following privileges:

- **CREATE ON DATABASE**: Allows DMS
  to create new schemas in the database.
- **CREATE ON SCHEMA**: Allows DMS to create
  objects in the database schema.
- **GRANT USAGE ON LANGUAGE**: Allows DMS to
  create new functions and procedures in the database.
- **GRANT SELECT ON ALL TABLES IN SCHEMA pg_catalog**:
  Provides the user system information about the Amazon Redshift cluster.
- **GRANT SELECT ON pg_class_info**:
  Provides the user information about the table distribution style.

You can use the following code example to create a database user and grant it permissions. Replace
the example values with your values.

```
CREATE USER `user_name` PASSWORD `your_password`;
GRANT CREATE ON DATABASE `db_name` TO `user_name`;
GRANT CREATE ON SCHEMA `schema_name` TO `user_name`;
GRANT USAGE ON LANGUAGE plpythonu TO `user_name`;
GRANT USAGE ON LANGUAGE plpgsql TO `user_name`;
GRANT SELECT ON ALL TABLES IN SCHEMA pg_catalog TO `user_name`;
GRANT SELECT ON pg_class_info TO `user_name`;
GRANT SELECT ON sys_serverless_usage TO `user_name`;
GRANT SELECT ON pg_database_info TO `user_name`;
GRANT SELECT ON pg_statistic TO `user_name;`
```

Repeat the `GRANT CREATE ON SCHEMA` operation for each target schema where
you will apply the converted code or migrate data.

You can apply an extension pack on your target Amazon Redshift database. An extension pack
is an add-on module that emulates source database functions that are required
when converting objects to Amazon Redshift. For more information, see
[Using extension packs in DMS Schema Conversion](extension-pack.md "extension-pack.md").
