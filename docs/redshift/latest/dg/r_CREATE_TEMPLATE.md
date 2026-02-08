Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE TEMPLATE

Creates reusable templates for Amazon Redshift commands like [COPY](r_COPY.md "r_COPY.md").
Templates store commonly used parameters that can be referenced across multiple
command executions, improving consistency and reducing manual parameter specification.

Templates eliminate the need to repeatedly specify the same formatting parameters across multiple operations,
while source paths, target tables, and authorization may vary between operations.

## Required privileges

To create a template, you must have one of the following:

- Superuser privileges
- CREATE permission on the schema where you want to create the template, or CREATE scoped permission on schemas in the database where you want to create the template

## Syntax

```
CREATE [ OR REPLACE ] TEMPLATE [*database\_name*.][*schema\_name*.]*template\_name*
FOR *COPY* [ AS ]
[ [ FORMAT ] [ AS ] *data\_format* ]
[ *parameter* [ argument ] [ , ... ] ];

```

## Parameters

_OR REPLACE_

If a template of the same name already exists in the specified database and schema,
the existing template is replaced. You can only replace a template with a new template that defines the same operation type, for example, COPY.
You must have the necessary privileges to replace a template.

_database_name_

(Optional) The name of the database where the template will be created. If not specified, the template is created in the current database.

If the database or schema doesn't exist, the template isn't created,
and the statement returns an error. You can't create templates in
the system databases `template0`, `template1`,
`padb_harvest` , or `sys:internal`.

_schema_name_

(Optional) The name of the schema where the template will be created. If not specified, the template is created in the current schema.

If a schema name is given, the new template is created in that schema (assuming
the creator has access to the schema). The template name must be a unique name for
that schema.

_template_name_

The name of the template to be created. Optionally, the template name can be qualified
with the database and schema name. In the following example, the database name is `demo_database`,
the schema name is `demo_schema`, and the template name is `test`. For more information about valid names, see [Names and identifiers](r_names.md "r_names.md").

```
CREATE TEMPLATE demo_database.demo_schema.test FOR COPY AS CSV;
```

COPY

Specifies the Redshift command type for which the template is created. Currently, only the COPY command is supported.

[ [ FORMAT ] [ AS ] _data_format_ ]

This is an optional parameter. This specifies the data format for COPY operations.

[ _parameter_ [ argument ]]

Any valid parameter for the specified redshift command.

For example, templates for the COPY command can include:

- [Data format parameters](copy-parameters-data-format.md "copy-parameters-data-format.md")
- [File compression
  parameters](copy-parameters-file-compression.md "copy-parameters-file-compression.md")
- [Data conversion parameters](copy-parameters-data-conversion.md "copy-parameters-data-conversion.md")
- [Data load operations](copy-parameters-data-load.md "copy-parameters-data-load.md")

For a complete list of supported parameters, see [COPY](r_COPY.md "r_COPY.md") command.

### Usage notes

- By default, all users have CREATE and USAGE privileges on the PUBLIC schema. To
  disallow users from creating objects in the PUBLIC schema of a database, use the
  REVOKE command to remove that privilege.
- When a parameter exists in both the template and the command, the command parameter takes precedence.
- Templates are database objects and follow standard Redshift object naming and permission rules.
  For more information about valid names, see [Names and identifiers](r_names.md "r_names.md").
- Templates cannot contain manifest file specifications for [COPY](r_COPY.md "r_COPY.md") command.

### Limitations

- At least one parameter must be specified when creating a template.
- Excluded parameters – Command-specific parameters such as source paths, target tables, authorization credentials, and manifest file specifications
  cannot be included in templates. These parameters must be specified in the actual command.
- Maximum templates per cluster – You can create a maximum of 1,000 templates per cluster.
  This limit applies to the total number of templates across all databases and schemas in the cluster.
- Cross-database references – Templates cannot be referenced across databases.
- Data sharing – Templates cannot be included in data shares. Templates
  must be created separately in each cluster where they are needed.

## Examples

The following example creates a template for COPY command

```
CREATE TEMPLATE test_schema.demo_template
FOR COPY
AS
FORMAT JSON 'auto'
NULL AS ''
MAXERROR 100;

```

Use [SHOW TEMPLATE](r_SHOW_TEMPLATE.md "r_SHOW_TEMPLATE.md") to get the definition of the template:

```

`SHOW TEMPLATE test_schema.demo_template;`
`CREATE OR REPLACE TEMPLATE dev.test_schema.demo_template FOR COPY AS FORMAT AS JSON 'auto' NULL '' MAXERROR 100;`
```

Query the [SYS_REDSHIFT_TEMPLATE](SYS_REDSHIFT_TEMPLATE.md "SYS_REDSHIFT_TEMPLATE.md") system view to get more details about a template.

```
`SELECT * FROM SYS_REDSHIFT_TEMPLATE;`

`database_name | schema_name | template_name | template_type | create_time | last_modified_time | owner_id | last_modified_by | template_parameters
---------------+-------------+---------------+---------------+----------------------------+----------------------------+----------+------------------+---------------------
 dev | test_schema | demo_template | 1 | 2025-12-17 20:06:01.944171 | 2025-12-17 20:06:01.944171 | 1 | 1 | {
 "JSON": "auto",
 "MAXERROR": 100,
 "NULL": ""
}`
```
