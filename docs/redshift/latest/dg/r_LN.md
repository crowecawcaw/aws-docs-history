Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# LN function

Returns the natural logarithm of the input parameter.

Synonym of [DLOG1 function](r_DLOG1.md "r_DLOG1.md").

## Syntax

```
LN(*expression*)
```

## Argument

_expression_

The target column or expression that the function operates on.

###### Note

This function returns an error for some data types if the expression
references an Amazon Redshift user-created table or an Amazon Redshift STL or STV
system table.

Expressions with the following data types produce an error if they
reference a user-created or system table. Expressions with these data types
run exclusively on the leader node:

- `BOOLEAN`
- `CHAR`
- `DATE`
- `DECIMAL` or `NUMERIC`
- `TIMESTAMP`
- `VARCHAR`

Expressions with the following data types run successfully on
user-created tables and STL or STV system tables:

- `BIGINT`
- `DOUBLE PRECISION`
- `INTEGER`
- `REAL`
- `SMALLINT`

## Return type

The LN function returns the same type as the input _expression_.

## Examples

To return the natural logarithm or base `e` logarithm of the
number 2.718281828, use the following example.

```
`SELECT LN(2.718281828);`

`+--------------------+
| ln |
+--------------------+
| 0.9999999998311267 |
+--------------------+`
```

Note that the answer is nearly equal to 1.

The following example uses the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To return the natural logarithm of the values in the userid column in
the USERS table, use the following example.

```
`SELECT username, LN(userid) FROM users ORDER BY userid LIMIT 10;`

`+----------+--------------------+
| username | ln |
+----------+--------------------+
| JSG99FHE | 0 |
| PGL08LJI | 0.6931471805599453 |
| IFT66TXU | 1.0986122886681098 |
| XDZ38RDD | 1.3862943611198906 |
| AEB55QTM | 1.6094379124341003 |
| NDQ15VBM | 1.791759469228055 |
| OWY35QYB | 1.9459101490553132 |
| AZG78YIP | 2.0794415416798357 |
| MSD36KVR | 2.1972245773362196 |
| WKW41AIW | 2.302585092994046 |
+----------+--------------------+`
```
