Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Scalar Python UDFs

A scalar Python UDF incorporates a Python program that runs when the function is
called and returns a single value. The [CREATE FUNCTION](r_CREATE_FUNCTION.md "r_CREATE_FUNCTION.md") command defines the following parameters:

- (Optional) Input arguments. Each argument must have a name and a data type.
- One return data type.
- One executable Python program.
  The input and return data types for Python UDFs can be any of the following types:

- SMALLINT
- INTEGER
- BIGINT
- DECIMAL
- REAL
- DOUBLE PRECISION
- BOOLEAN
- CHAR
- VARCHAR
- DATE
- TIMESTAMP
- ANYELEMENT
  The aliases for these types are also valid. For a full list of data types and their aliases,
  see [Data types](c_Supported_data_types.md "c_Supported_data_types.md").

When Python UDFs use the data type ANYELEMENT, Amazon Redshift automatically
converts to a standard data type based on the arguments supplied at runtime. For more
information, see [ANYELEMENT data type](udf-data-types.md#udf-anyelement-data-type "udf-data-types.md#udf-anyelement-data-type").

When an Amazon Redshift query calls a scalar UDF, the following steps occur at runtime:

1. The function converts the input arguments to Python data types.

For a mapping of Amazon Redshift data types to Python data types, see [Python UDF data types](udf-data-types.md "udf-data-types.md"). 2. The function runs the Python program, passing the converted input
arguments. 3. The Python code returns a single value. The data type of the return value must
correspond to the RETURNS data type specified by the function definition. 4. The function converts the Python return value to the specified Amazon Redshift data type,
then returns that value to the query.

###### Note

Python 3 isn’t available for Python UDFs.
To get Python 3 support for Amazon Redshift UDFs, use
[Scalar Lambda UDFs](udf-creating-a-lambda-sql-udf.md "udf-creating-a-lambda-sql-udf.md") instead.
