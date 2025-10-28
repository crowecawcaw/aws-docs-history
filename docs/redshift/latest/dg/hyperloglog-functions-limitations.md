Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Limitations

This topic describes limitations for HyperLogLog in Amazon Redshift.

The following are limitations for using HyperLogLog in Amazon Redshift:

- Amazon Redshift tables don't support an HLLSKETCH column as a sort key or a distribution key for
  an Amazon Redshift table.
- Amazon Redshift doesn't support HLLSKETCH columns in ORDER BY, GROUP BY, or DISTINCT
  clauses.
- You can only
  UNLOAD HLLSKETCH columns to text or CSV format. Amazon Redshift then writes the HLLSKETCH
  data in either a JSON format or a Base64 format. For more information about
  UNLOAD, see [UNLOAD](r_UNLOAD.md "r_UNLOAD.md").
- Amazon Redshift only supports HyperLogLog sketches with a precision (logm value) of 15.
- JDBC and ODBC drivers don't support the HLLSKETCH data type. Therefore, the result set
  uses VARCHAR to represent the HLLSKETCH values.
- Amazon Redshift Spectrum doesn't natively support the HLLSKETCH data. Therefore, you can't create
  or alter an external table with an HLLSKETCH column.
- Data types for Python user-defined functions (UDFs) don't support the HLLSKETCH data
  type. For more information about Python UDFs, see [Scalar Python UDFs](udf-creating-a-scalar-udf.md "udf-creating-a-scalar-udf.md").

###### Note

Starting November 1, 2025,
Amazon Redshift will no longer support the creation of new Python UDFs.
Existing Python UDFs will continue to function until June 30, 2026.
Starting July 1, 2026, Amazon Redshift will no longer support Python
UDFs. We recommend that you migrate your existing Python UDFs to Lambda UDFs before November 1, 2025.
For information on creating and using Lambda UDFs, see [Scalar Lambda UDFs](udf-creating-a-lambda-sql-udf.md "udf-creating-a-lambda-sql-udf.md").
For information on converting existing Python UDFs to
Lambda UDFs, see the [blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .
