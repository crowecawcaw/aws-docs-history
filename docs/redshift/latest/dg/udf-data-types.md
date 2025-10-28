Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Python UDF data types

Python UDFs can use any standard Amazon Redshift data type for the input arguments and the
function's return value. In addition to the standard data types, UDFs support the data
type _ANYELEMENT_, which Amazon Redshift automatically
converts to a standard data type based on the arguments supplied at runtime. Scalar UDFs
can return a data type of ANYELEMENT.
For more information, see [ANYELEMENT data type](#udf-anyelement-data-type "#udf-anyelement-data-type").

During execution, Amazon Redshift converts the arguments from Amazon Redshift data types to Python
data types for processing. It then converts the return value from the Python data type
to the corresponding Amazon Redshift data type. For more information about Amazon Redshift data types,
see [Data types](c_Supported_data_types.md "c_Supported_data_types.md").

The following table maps Amazon Redshift data types to Python data types.

| Amazon Redshift data type          | Python data type |
| ---------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| smallint integer bigint short long | int              |
| decimal or numeric                 | decimal          |
| double real                        | float            |
| boolean                            | bool             |
| char varchar                       | string           |
| timestamp                          | datetime         | ## ANYELEMENT data type ANYELEMENT is a _polymorphic data type_. This means that if a function is declared using ANYELEMENT for an argument's data type, the function can accept any standard Amazon Redshift data type as input for that argument when the function is called. The ANYELEMENT argument is set to the data type actually passed to it when the function is called. If a function uses multiple ANYELEMENT data types, they must all resolve to the same actual data type when the function is called. All ANYELEMENT argument data types are set to the actual data type of the first argument passed to an ANYELEMENT. For example, a function declared as `f_equal(anyelement, anyelement)` will take any two input values, so long as they are of the same data type. If the return value of a function is declared as ANYELEMENT, at least one input argument must be ANYELEMENT. The actual data type for the return value is the same as the actual data type supplied for the ANYELEMENT input argument. |
