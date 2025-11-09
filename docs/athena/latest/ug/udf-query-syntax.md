# Query using UDF query syntax

The `USING EXTERNAL FUNCTION` clause specifies a UDF or multiple UDFs that
can be referenced by a subsequent `SELECT` statement in the query. You need
the method name for the UDF and the name of the Lambda function that hosts the UDF. In
place of the Lambda function name, you can use the Lambda ARN. In cross-account scenarios,
the Lambda ARN is required.

## Synopsis

```
USING EXTERNAL FUNCTION `UDF_name`(`variable1` `data_type`[, `variable2` `data_type`][,...])
RETURNS `data_type`
LAMBDA '`lambda_function_name_or_ARN`'
[, EXTERNAL FUNCTION `UDF_name2`(`variable1` `data_type`[, `variable2` `data_type`][,...])
RETURNS `data_type`
LAMBDA '`lambda_function_name_or_ARN`'[,...]]
SELECT  [...] `UDF_name`(`expression`) [, `UDF_name2`(`expression`)] [...]
```

## Parameters

**USING EXTERNAL FUNCTION
`UDF_name`(`variable1`
`data_type`[, `variable2`
`data_type`][,...])**

`UDF_name` specifies the name of the UDF,
which must correspond to a Java method within the referenced Lambda
function. Each `variable data_type` specifies a
named variable and its corresponding data type that the UDF accepts as
input. The `data_type` must be one of the
supported Athena data types listed in the following table and map to the
corresponding Java data type.

| Athena data type             | Java data type                |
| ---------------------------- | ----------------------------- |
| TIMESTAMP                    | java.time.LocalDateTime (UTC) |
| DATE                         | java.time.LocalDate (UTC)     |
| TINYINT                      | java.lang.Byte                |
| SMALLINT                     | java.lang.Short               |
| REAL                         | java.lang.Float               |
| DOUBLE                       | java.lang.Double              |
| DECIMAL (see `RETURNS` note) | java.math.BigDecimal          |
| BIGINT                       | java.lang.Long                |
| INTEGER                      | java.lang.Int                 |
| VARCHAR                      | java.lang.String              |
| VARBINARY                    | byte[]                        |
| BOOLEAN                      | java.lang.Boolean             |
| ARRAY                        | java.util.List                |
| ROW                          | java.util.Map<String, Object> |

**RETURNS `data_type`**

`data_type` specifies the SQL data type that the UDF
returns as output. Athena data types listed in the table above are
supported. For the `DECIMAL` data type, use the syntax
`RETURNS DECIMAL(`precision`,
 `scale`)` where
`precision` and
`scale` are integers.

**LAMBDA '`lambda_function`'**

`lambda_function` specifies the name of the
Lambda function to be invoked when running the UDF.

**SELECT [...]
`UDF_name`(`expression`)
[...]**

The `SELECT` query that passes values to the UDF and
returns a result. `UDF_name` specifies the UDF
to use, followed by an `expression` that is
evaluated to pass values. Values that are passed and returned must match
the corresponding data types specified for the UDF in the `USING
 EXTERNAL FUNCTION` clause.

### Examples

For example queries based on the [AthenaUDFHandler.java](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-udfs/src/main/java/com/amazonaws/athena/connectors/udfs/AthenaUDFHandler.java "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-udfs/src/main/java/com/amazonaws/athena/connectors/udfs/AthenaUDFHandler.java") code on GitHub, see the GitHub [Amazon Athena UDF connector](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-udfs "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-udfs") page.
