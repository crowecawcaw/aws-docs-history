Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SUPER configurations

You can configure your SUPER data for specific scenarios. The following sections provide
details on choosing and applying the appropriate SUPER configurations based on your data format requirements.

###### Topics

- [Lax and strict modes for SUPER](#lax-strict-modes "#lax-strict-modes")
- [Accessing JSON fields with uppercase and mixed-case field
  names or attributes](#upper-mixed-case "#upper-mixed-case")
- [Parsing options for SUPER](#parsing-options-super "#parsing-options-super")

## Lax and strict modes for SUPER

When you query SUPER data, the path expression may not match the actual SUPER data
structure. If you try to access a non-existent member of an object or element of an
array, Amazon Redshift returns a NULL value if your query is run in the default lax mode. If you run your query in the strict mode, Amazon Redshift returns an error. The following session parameters can be set to set the lax mode on or off.

The following example uses session parameters to enable lax mode.

```
SET navigate_super_null_on_error=ON;  --default lax mode for navigation

SET cast_super_null_on_error=ON;  --default lax mode for casting

SET parse_super_null_on_error=OFF;  --default strict mode for ingestion
```

## Accessing JSON fields with uppercase and mixed-case field

names or attributes

When your JSON attribute names are in uppercase or mixed-case, you must be able to navigate
SUPER type structures in a case sensitive way. To do that, you can configure
`enable_case_sensitive_identifier` to TRUE and wrap the uppercase and mixed-case
attribute names with double quotation marks.

The following example illustrates how to set `enable_case_sensitive_identifier` to query data.

```
SET enable_case_sensitive_identifier to TRUE;

-- Accessing JSON attribute names with uppercase and mixed-case names
SELECT json_table.data."ITEMS"."Name",
       json_table.data."price"
FROM
  (SELECT json_parse('{"ITEMS":{"Name":"TV"}, "price": 345}') AS data) AS json_table;

 Name | price
------+-------
 "TV" | 345
(1 row)

RESET enable_case_sensitive_identifier;

-- After resetting the above configuration, the following query accessing JSON attribute names with uppercase and mixed-case names should return null (if in lax mode).
SELECT json_table.data."ITEMS"."Name",
       json_table.data."price"
FROM
  (SELECT json_parse('{"ITEMS":{"Name":"TV"}, "price": 345}') AS data) AS json_table;

 name | price
------+-------
      | 345
(1 row)
```

## Parsing options for SUPER

When you use the JSON_PARSE function to parse JSON strings into SUPER values, certain restrictions apply:

- The same attribute name cannot appear in the same object, but can appear in a nested object. The `json_parse_dedup_attributes` configuration option allows JSON_PARSE to keep only the last occurrence of duplicate attributes instead of returning an error.
- Individual string literals in SUPER object have a size limit of 16,000,000 bytes. The `json_parse_truncate_strings` configuration option allows JSON_PARSE() to automatically truncate strings that are longer than this limit without returning an error. This behavior affects string values only and not attribute names.

For more information about the JSON_PARSE function, see [JSON_PARSE function](JSON_PARSE.md "JSON_PARSE.md").

The following example shows how to set the `json_parse_dedup_attributes` configuration option to the default behavior of returning an error for duplicate attributes.

```
SET json_parse_dedup_attributes=OFF;  --default behavior of returning error instead of de-duplicating attributes

```

The following example shows how to set the `json_parse_truncate_strings` configuration option for the default behavior of returning an error for strings that are longer than this limit.

```
SET json_parse_truncate_strings=OFF;  --default behavior of returning error instead of truncating strings
```
