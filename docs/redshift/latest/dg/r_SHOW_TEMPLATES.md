Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW TEMPLATES

Shows a list of templates in a schema, along with their attributes.

Each output row consists of template name, template id, template type, template owner, database name, schema name, create time, last modified time, and last modified by.

For complete template details, including template parameters, see [SYS_REDSHIFT_TEMPLATE](SYS_REDSHIFT_TEMPLATE.md "SYS_REDSHIFT_TEMPLATE.md").

## Required permissions

To view templates in an Amazon Redshift schema, you must have one of the following:

- Superuser privileges
- USAGE privilege on the schema containing the templates

## Syntax

```
SHOW TEMPLATES FROM SCHEMA [*database\_name*.]*schema\_name* [LIKE '*filter\_pattern*'] [LIMIT *row\_limit* ];
```

## Parameters

_database_name_

(Optional) The name of the database containing the templates to list. If not provided, uses the current database.

_schema_name_

The name of the schema that contains the templates to list.

_filter_pattern_

(Optional) A valid UTF-8 character expression with a pattern to match template names. The
LIKE option performs a case-sensitive match that supports the following
pattern-matching metacharacters:

| Metacharacter | Description                                         |
| ------------- | --------------------------------------------------- |
| `%`           | Matches any sequence of zero or more<br>characters. |
| `_`           | Matches any single character.                       |

If _filter_pattern_ does not contain metacharacters, then
the pattern only represents the string itself; in that case LIKE acts the same
as the equals operator.

_row_limit_

The maximum number of rows to return. Valid range is 0 to the template limit on the cluster (default is 1000).

## Examples

```
`SHOW TEMPLATES FROM SCHEMA s1;`
`template_name | template_id | template_type | template_owner | database_name | schema_name | create_time | last_modified_time | last_modified_by
------------------------+-------------+---------------+----------------+---------------+-------------+----------------------------+----------------------------+------------------
 template_maxerror | 107685 | COPY | alice | dev | s1 | 2025-12-16 19:31:10.514076 | 2025-12-16 19:31:10.514076 | 100
 json_template | 107687 | COPY | alice | dev | s1 | 2025-12-16 19:31:33.229566 | 2025-12-16 19:31:33.229567 | 100
 noload_template | 107686 | COPY | alice | dev | s1 | 2025-12-16 19:31:17.370547 | 2025-12-16 19:31:17.370547 | 100
 csv_delimiter_template | 107688 | COPY | alice | dev | s1 | 2025-12-16 19:31:42.354044 | 2025-12-16 19:31:42.354045 | 100`
```

```
`SHOW TEMPLATES FROM SCHEMA dev.s1 LIKE '%template' LIMIT 1;`
`template_name | template_id | template_type | template_owner | database_name | schema_name | create_time | last_modified_time | last_modified_by
-----------------+-------------+---------------+----------------+---------------+-------------+----------------------------+----------------------------+------------------
 noload_template | 107686 | COPY | alice | dev | s1 | 2025-12-16 19:31:17.370547 | 2025-12-16 19:31:17.370547 | 100`
```
