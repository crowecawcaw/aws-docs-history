Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# JSON\_TYPEOF function

The JSON\_TYPEOF scalar function returns a `VARCHAR` with values boolean, number,
string, object, array, or null, depending on the dynamic type of the `SUPER` value.

## Syntax

```
JSON_TYPEOF(*super\_expression*)

```

## Arguments

_super\_expression_

A `SUPER` expression or column.

## Return type

`VARCHAR`

## Examples

To check the type of JSON for the array `[1,2]` using the JSON\_TYPEOF function, use the following example.

```
`SELECT JSON_TYPEOF(ARRAY(1,2));`

`+-------------+
| json_typeof |
+-------------+
| array |
+-------------+`
```

To check the type of JSON for the object `{"name":"Joe"}` using the JSON\_TYPEOF function, use the following example.

```
`SELECT JSON_TYPEOF(JSON_PARSE('{"name":"Joe"}'));`

`+-------------+
| json_typeof |
+-------------+
| object |
+-------------+`
```
