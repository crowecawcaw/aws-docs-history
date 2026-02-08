Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW TEMPLATE

Displays the complete definition of a template, including the fully qualified name (database, schema, and template name) and all parameters.
The output is a valid CREATE TEMPLATE statement that you can use to recreate the template or create a similar template with modifications.

For more information on template creation, see [CREATE TEMPLATE](r_CREATE_TEMPLATE.md "r_CREATE_TEMPLATE.md").

## Required permissions

To view a template definition, you must have one of the following:

- Superuser privileges
- USAGE privilege on the template and USAGE privilege on the schema containing the template

## Syntax

```
SHOW TEMPLATE [*database\_name*.][*schema\_name*.]*template\_name*;
```

## Parameters

_database_name_

(Optional) The name of the database in which the template is created. If not specified, the current database is used.

_schema_name_

(Optional) The name of the schema in which the template is created. If not specified, the template is searched for in the current search path.

_template_name_

The name of the template.

## Examples

The following is an example of the SHOW TEMPLATE output for the template
`test_template`:

```
CREATE TEMPLATE test_template FOR COPY AS NOLOAD DELIMITER ',' ENCODING UTF16 ENCRYPTED;
```

```
`SHOW TEMPLATE test_template;`

`CREATE OR REPLACE TEMPLATE dev.public.test_template FOR COPY AS ENCRYPTED NOLOAD ENCODING UTF16 DELIMITER ',';`
```

The following example creates template `demo_template` in schema `demo_schema`.

```
CREATE OR REPLACE TEMPLATE demo_schema.demo_template FOR COPY AS
ACCEPTANYDATE ACCEPTINVCHARS DATEFORMAT 'DD-MM-YYYY' EXPLICIT_IDS ROUNDEC
TIMEFORMAT  AS 'DD.MM.YYYY HH:MI:SS' TRUNCATECOLUMNS NULL  AS 'null_string';

```

```
`SHOW TEMPLATE demo_schema.demo_template;`

`CREATE OR REPLACE TEMPLATE dev.demo_schema.demo_template FOR COPY AS TRUNCATECOLUMNS NULL 'null_string' EXPLICIT_IDS TIMEFORMAT 'DD.MM.YYYY HH:MI:SS' ACCEPTANYDATE ROUNDEC ACCEPTINVCHARS DATEFORMAT 'DD-MM-YYYY';`

```
