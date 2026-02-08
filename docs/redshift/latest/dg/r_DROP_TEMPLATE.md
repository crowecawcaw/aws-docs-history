Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP TEMPLATE

Drops a template from a database.

## Required privileges

To drop a template, you must have one of the following:

- Superuser privileges
- DROP TEMPLATE privilege and USAGE privilege on the schema containing the template

## Syntax

```
DROP TEMPLATE [*database\_name*.][*schema\_name*.]*template\_name*;
```

## Parameters

_database_name_

(Optional) The name of the database in which the template is created. If not specified, the current database is used.

_schema_name_

(Optional) The name of the schema in which the template is created. If not specified, the template is searched for in the current search path.

_template_name_

The name of the template to remove. In the following example, the database name is `demo_database`,
the schema name is `demo_schema`, and the template name is `test`.

```
DROP TEMPLATE demo_database.demo_schema.test;
```

## Examples

The following example drops the template test_template from the current schema:

```
DROP TEMPLATE test_template;
```

The following example drops the template test_template from the schema test_schema:

```
DROP TEMPLATE test_schema.test_template;
```
