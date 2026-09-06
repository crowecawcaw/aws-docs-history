

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# LOWER\_ATTRIBUTE\_NAMES function
<a name="r_lower_attribute_names"></a>

Converts all applicable attribute names in a SUPER value to lowercase, using the same case conversion routine as the [LOWER function](r_LOWER.md). LOWER\_ATTRIBUTE\_NAMES supports UTF-8 multibyte characters, up to a maximum of four bytes per character. 

 To convert SUPER attribute names to uppercase, use the [UPPER\_ATTRIBUTE\_NAMES function](r_upper_attribute_names.md). 

## Syntax
<a name="r_lower_attribute_names-synopsis"></a>

```
LOWER_ATTRIBUTE_NAMES( super_expression )
```

## Arguments
<a name="r_lower_attribute_names-arguments"></a>

*super\_expression*  
A SUPER expression.

## Return type
<a name="r_lower_attribute_names-return-type"></a>

`SUPER`

## Usage notes
<a name="r_lower_attribute_names-usage-notes"></a>

In Amazon Redshift, column identifiers are traditionally case-insensitive and converted to lowercase. If you ingest data from case-sensitive data formats such as JSON, the data might contain mixed-case attribute names.

Consider the following example.

```
CREATE TABLE t1 (s) AS SELECT JSON_PARSE('{"AttributeName": "Value"}');


SELECT s.AttributeName FROM t1;  

attributename
-------------
NULL


SELECT s."AttributeName" FROM t1;

attributename
-------------
NULL
```

Amazon Redshift returns NULL for both queries. To query `AttributeName`, use LOWER\_ATTRIBUTE\_NAMES to convert the data’s attribute names to lowercase. Consider the following example.

```
CREATE TABLE t2 (s) AS SELECT LOWER_ATTRIBUTE_NAMES(s) FROM t1;


SELECT s.attributename FROM t2;

attributename
-------------
"Value"


SELECT s.AttributeName FROM t2; 

attributename
-------------
"Value"


SELECT s."attributename" FROM t2;

attributename
-------------
"Value"


SELECT s."AttributeName" FROM t2;

attributename
-------------
"Value"
```

A related option for working with mixed-case object attribute names is the `enable_case_sensitive_super_attribute` configuration option, which lets Amazon Redshift recognize case in SUPER attribute names. This can be an alternative solution to using LOWER\_ATTRIBUTE\_NAMES. For more information about `enable_case_sensitive_super_attribute`, go to [enable\_case\_sensitive\_super\_attribute](r_enable_case_sensitive_super_attribute.md).

## Examples
<a name="r_lower_attribute_names_examples"></a>

**Converting SUPER attribute names to lowercase**  
The following example uses LOWER\_ATTRIBUTE\_NAMES to convert the attribute names of all SUPER values in a table.

```
-- Create a table and insert several SUPER values.
CREATE TABLE t (i INT, s SUPER);

INSERT INTO t VALUES
  (1, NULL), 
  (2, 'A'::SUPER),
  (3, JSON_PARSE('{"AttributeName": "B"}')),
  (4, JSON_PARSE(
     '[{"Subobject": {"C": "C"},
        "Subarray": [{"D": "D"}, "E"]
      }]'));

-- Convert all attribute names to lowercase.
UPDATE t SET s = LOWER_ATTRIBUTE_NAMES(s);

SELECT i, s FROM t ORDER BY i;

 i |                        s
---+--------------------------------------------------
 1 | NULL
 2 | "A"
 3 | {"attributename":"B"}
 4 | [{"subobject":{"c":"C"},"subarray":[{"d":"D"}, "E"]}]
```

Observe how LOWER\_ATTRIBUTE\_NAMES functions.
+  NULL values and scalar SUPER values such as `"A"` are unchanged. 
+  In a SUPER object, all attribute names are changed to lowercase, but attribute values such as `"B"` remain unchanged. 
+  LOWER\_ATTRIBUTE\_NAMES applies recursively to any SUPER object that is nested inside a SUPER array or inside another object. 

**Using LOWER\_ATTRIBUTE\_NAMES on a SUPER object with duplicate attribute names**  
If a SUPER object contains attributes whose names differ only in their case, LOWER\_ATTRIBUTE\_NAMES will raise an error. Consider the following example.

```
SELECT LOWER_ATTRIBUTE_NAMES(JSON_PARSE('{"A": "A", "a": "a"}'));      

error:   Invalid input
code:    8001
context: SUPER value has duplicate attributes after case conversion.
```