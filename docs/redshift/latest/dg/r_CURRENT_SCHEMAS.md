Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CURRENT_SCHEMAS

Returns an array of the names of any schemas in the current search path. The current
search path is defined in the search_path parameter.

## Syntax

###### Note

This is a leader-node function. This function returns an error if it references
a user-created table, an STL or STV system table, or an SVV or SVL system
view.

```
current_schemas(*include\_implicit*)
```

## Argument

_include_implicit_

If true, specifies that the search path should include any implicitly
included system schemas. Valid values are `true` and
`false`. Typically, if `true`, this parameter
returns the `pg_catalog` schema in addition to the current
schema.

## Return type

Returns a CHAR or VARCHAR string.

## Examples

The following example returns the names of the schemas in the current search path,
not including implicitly included system schemas:

```
select current_schemas(false);

current_schemas
-----------------
{public}
(1 row)
```

The following example returns the names of the schemas in the current search path,
including implicitly included system schemas:

```
select current_schemas(true);

current_schemas
---------------------
{pg_catalog,public}
(1 row)
```
