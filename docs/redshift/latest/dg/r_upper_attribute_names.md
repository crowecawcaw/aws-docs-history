

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# UPPER\_ATTRIBUTE\_NAMES function
<a name="r_upper_attribute_names"></a>

Converts all applicable attribute names in a SUPER value to uppercase, using the same case conversion routine as the [UPPER function](r_UPPER.md). UPPER\_ATTRIBUTE\_NAMES supports UTF-8 multibyte characters, up to a maximum of four bytes per character. 

 To convert SUPER attribute names to lowercase, use the [LOWER\_ATTRIBUTE\_NAMES function](r_lower_attribute_names.md). 

## Syntax
<a name="r_upper_attribute_names-synopsis"></a>

```
UPPER_ATTRIBUTE_NAMES( super_expression )
```

## Arguments
<a name="r_upper_attribute_names-arguments"></a>

*super\_expression*  
A SUPER expression.

## Return type
<a name="r_upper_attribute_names-return-type"></a>

`SUPER`

## Examples
<a name="r_upper_attribute_names_examples"></a>

**Converting SUPER attribute names to uppercase**  
The following example uses UPPER\_ATTRIBUTE\_NAMES to convert the attribute names of all SUPER values in a table.

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

 i |                        s
---+--------------------------------------------------
 1 | NULL
 2 | "a"
 3 | {"ATTRIBUTENAME":"B"}
 4 | [{"SUBOBJECT":{"C":"c"},"SUBARRAY":[{"D":"d"}, "e"]}]
```

Observe how UPPER\_ATTRIBUTE\_NAMES functions.
+  NULL values and scalar SUPER values such as `"a"` are unchanged. 
+  In a SUPER object, all attribute names are changed to uppercase, but attribute values such as `"b"` remain unchanged. 
+  UPPER\_ATTRIBUTE\_NAMES applies recursively to any SUPER object that is nested inside a SUPER array or inside another object. 

**Using UPPER\_ATTRIBUTE\_NAMES on a SUPER object with duplicate attribute names**  
If a SUPER object contains attributes whose names differ only in their case, UPPER\_ATTRIBUTE\_NAMES will raise an error. Consider the following example.

```
SELECT UPPER_ATTRIBUTE_NAMES(JSON_PARSE('{"A": "A", "a": "a"}'));      

error:   Invalid input
code:    8001
context: SUPER value has duplicate attributes after case conversion.
```