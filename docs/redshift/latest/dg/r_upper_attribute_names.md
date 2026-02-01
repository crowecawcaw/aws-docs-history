Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# UPPER_ATTRIBUTE_NAMES function

Converts all applicable attribute names in a SUPER value to uppercase,
using the same case conversion routine as the [UPPER function](r_UPPER.md "r_UPPER.md").
UPPER_ATTRIBUTE_NAMES supports UTF-8 multibyte characters, up to a maximum of
four bytes per character.

To convert SUPER attribute names to lowercase, use the [LOWER_ATTRIBUTE_NAMES function](r_lower_attribute_names.md "r_lower_attribute_names.md").

## Syntax

```
UPPER_ATTRIBUTE_NAMES(super_expression)
```

## Arguments

_super_expression_

A SUPER expression.

## Return type

`SUPER`

## Examples

###### Converting SUPER attribute names to uppercase

The following example uses UPPER_ATTRIBUTE_NAMES to convert the attribute names of all SUPER values in a table.

```
-- Create a table and insert several SUPER values.
CREATE TABLE t (i INT, s SUPER);

INSERT INTO t VALUES
  (1, NULL),
  (2, 'a'::SUPER),
  (3, JSON_PARSE('{"AttributeName": "b"}')),
  (4, JSON_PARSE(
     '[{"Subobject": {"c": "c"},
        "Subarray": [{"d": "d"}, "e"]
      }]'));

-- Convert all attribute names to uppercase.
UPDATE t SET s = UPPER_ATTRIBUTE_NAMES(s);

SELECT i, s FROM t ORDER BY i;

 `i | s
---+--------------------------------------------------
 1 | NULL
 2 | "a"
 3 | {"ATTRIBUTENAME":"B"}
 4 | [{"SUBOBJECT":{"C":"c"},"SUBARRAY":[{"D":"d"}, "e"]}]`
```

Observe how UPPER_ATTRIBUTE_NAMES functions.

- NULL values and scalar SUPER values such as `"a"` are unchanged.
- In a SUPER object, all attribute names are changed to uppercase, but attribute values such as `"b"` remain unchanged.
- UPPER_ATTRIBUTE_NAMES applies recursively to any SUPER object that is nested inside a SUPER array or inside another object.

###### Using UPPER_ATTRIBUTE_NAMES on a SUPER object with duplicate attribute names

If a SUPER object contains attributes whose names differ only in their case, UPPER_ATTRIBUTE_NAMES will raise an error. Consider the following example.

```
SELECT UPPER_ATTRIBUTE_NAMES(JSON_PARSE('{"A": "A", "a": "a"}'));

`error: Invalid input
code: 8001
context: SUPER value has duplicate attributes after case conversion.`
```
