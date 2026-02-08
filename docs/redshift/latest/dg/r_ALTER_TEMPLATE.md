Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER TEMPLATE

Changes the definition of an existing template. Use this command to rename a template,
change the owner of a template, add or remove parameters from the template definition, or set parameter values.

## Required privileges

To alter a template, you must have one of the following:

- Superuser privileges
- ALTER TEMPLATE privilege and USAGE privilege on the schema containing the template

## Syntax

```
ALTER TEMPLATE [*database\_name*.][*schema\_name*.]*template\_name*
{
RENAME TO *new\_name*
| OWNER TO *new\_owner*
| ADD  *parameter* [AS] [*value*]
| DROP *parameter*
| SET *parameter* TO *value1* [, *parameter2* TO *value2* , ...]
};
```

## Parameters

_database_name_

(Optional) The name of the database in which the template is created. If not specified, the current database is used.

_schema_name_

(Optional) The name of the schema in which the template is created. If not specified, the template is searched for in the current search path.

_template_name_

The name of the template to be altered.

RENAME TO

A clause that renames the template.

_new_name_

The new name of the template. For more information about valid names, see
[Names and identifiers](r_names.md "r_names.md").

OWNER TO

A clause that changes the owner of the template.

_new_owner_

The new owner of the template.

ADD _parameter_ [AS] [*value*]

Adds a new parameter to the template.

- For keyword-only parameters (such as CSV or GZIP), specify just the parameter name.
- For parameters that require values, specify the parameter name followed by the value. You can optionally include AS between the parameter and value.

DROP _parameter_

Removes the specified parameter from the template. Cannot drop multiple parameters with a single DROP command.

SET _parameter_ TO _value1_ [, *parameter2* TO *value2* , ...]

Updates the values of existing template parameters. Only use for parameters that already have values. Multiple parameters can be updated in a single command.

## Examples

The following example renames the test_template template to demo_template.

```
ALTER TEMPLATE test_template
RENAME TO demo_template;
```

The following example gives ownership of the demo_template schema to the user
bob.

```
ALTER TEMPLATE demo_template
OWNER TO bob;
```

The following example adds parameter `CSV` to template demo_template

```
ALTER TEMPLATE demo_template
ADD CSV;
```

The following example adds parameter `TIMEFORMAT 'auto'` to template demo_template

```
ALTER TEMPLATE demo_template
ADD TIMEFORMAT 'auto';
```

The following example drops parameter `ENCRYPTED` from template demo_template

```
ALTER TEMPLATE demo_template
DROP ENCRYPTED;
```

The following example sets the `DELIMITER` parameter to `'|'` and the `TIMEFORMAT` parameter to `'epochsecs'`:

```
ALTER TEMPLATE demo_template
SET DELIMITER TO '|', TIMEFORMAT TO 'epochsecs';
```
