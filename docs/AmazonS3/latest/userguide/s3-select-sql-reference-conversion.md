# Conversion functions

###### Important

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/ "https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/")

Amazon S3 Select supports the following conversion function.

###### Topics

- [CAST](#s3-select-sql-reference-cast "#s3-select-sql-reference-cast")

## CAST

The `CAST` function converts an entity, such as an expression that
evaluates to a single value, from one type to another.

### Syntax

```
CAST ( `expression` AS `data_type` )
```

### Parameters

_`expression`_

A combination of one or more values, operators, and SQL
functions that evaluate to a value.

_`data_type`_

The target data type, such as `INT`, to cast the
expression to. For a list of supported data types, see [Data types](s3-select-sql-reference-data-types.md "s3-select-sql-reference-data-types.md").

### Examples

```
CAST('2007-04-05T14:30Z' AS TIMESTAMP)
CAST(0.456 AS FLOAT)
```
