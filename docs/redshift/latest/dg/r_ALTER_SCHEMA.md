Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER SCHEMA

Changes the definition of an existing schema. Use this command to rename a schema or
change the owner of a schema. For example, rename an existing schema to preserve a backup
copy of that schema when you plan to create a new version of that schema. For more
information about schemas, see [CREATE SCHEMA](r_CREATE_SCHEMA.md "r_CREATE_SCHEMA.md").

To view the configured schema quotas, see [SVV_SCHEMA_QUOTA_STATE](r_SVV_SCHEMA_QUOTA_STATE.md "r_SVV_SCHEMA_QUOTA_STATE.md").

To view the records where schema quotas were exceeded, see [STL_SCHEMA_QUOTA_VIOLATIONS](r_STL_SCHEMA_QUOTA_VIOLATIONS.md "r_STL_SCHEMA_QUOTA_VIOLATIONS.md").

## Required privileges

Following are required privileges for ALTER SCHEMA:

- Superuser
- User with the ALTER SCHEMA privilege
- Schema owner

When you change a schema name, note that objects using the old name, such as stored
procedures or materialized views, must be updated to use the new name.

## Syntax

```
ALTER SCHEMA *schema\_name*
{
RENAME TO *new\_name* |
OWNER TO *new\_owner* |
QUOTA { quota [MB | GB | TB] | UNLIMITED }
}
```

## Parameters

_schema_name_

The name of the database schema to be altered.

RENAME TO

A clause that renames the schema.

_new_name_

The new name of the schema. For more information about valid names, see
[Names and identifiers](r_names.md "r_names.md").

OWNER TO

A clause that changes the owner of the schema.

_new_owner_

The new owner of the schema.

QUOTA

The maximum amount of disk space that the specified schema can use. This
space is the collective size of all tables under the specified schema. Amazon Redshift
converts the selected value to megabytes. Gigabytes is the default unit of
measurement when you don't specify a value.

For more information about configuring schema quotas, see [CREATE SCHEMA](r_CREATE_SCHEMA.md "r_CREATE_SCHEMA.md").

## Examples

The following example renames the SALES schema to US_SALES.

```
alter schema sales
rename to us_sales;
```

The following example gives ownership of the US_SALES schema to the user
DWUSER.

```
alter schema us_sales
owner to dwuser;
```

The following example changes the quota to 300 GB and removes the quota.

```
alter schema us_sales QUOTA 300 GB;
alter schema us_sales QUOTA UNLIMITED;
```
