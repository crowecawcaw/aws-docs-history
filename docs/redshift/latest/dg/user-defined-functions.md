Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# User-defined functions in Amazon Redshift

You can create a custom scalar user-defined function (UDF) using either a SQL SELECT clause
or a Python program. The new function is stored in the database and is available for any user
with sufficient privileges to run. You run a custom scalar UDF in much the same way as you run
existing Amazon Redshift functions.

For Python UDFs, in addition to using the standard Python functionality, you can import
your own custom Python modules. For more information, see [Python language support for UDFs](udf-python-language-support.md "udf-python-language-support.md").
Note that Python 3 isn't available for Python UDFs. To get Python 3 support for Amazon Redshift UDFs,
use [Scalar Lambda UDFs](udf-creating-a-lambda-sql-udf.md "udf-creating-a-lambda-sql-udf.md") instead.

You can also create AWS Lambda UDFs that use custom functions defined in Lambda as part of
your SQL queries. Lambda UDFs enable you to write complex UDFs and integrate with third-party
components. They also can help you overcome some of the limitations of current Python and SQL
UDFs. For example, they can help you access network and storage resources and write more
full-fledged SQL statements. You can create Lambda UDFs in any of the programming languages
supported by Lambda, such as Java, Go, PowerShell, Node.js, C#, Python, and Ruby. Or you can
use a custom runtime.

By default, all users can run UDFs. For more information about privileges, see [UDF security and permissions](udf-security-and-privileges.md "udf-security-and-privileges.md").

###### Topics

- [UDF security and permissions](udf-security-and-privileges.md "udf-security-and-privileges.md")
- [Preventing UDF naming conflicts](udf-naming-udfs.md "udf-naming-udfs.md")
- [Scalar SQL UDFs](udf-creating-a-scalar-sql-udf.md "udf-creating-a-scalar-sql-udf.md")
- [Scalar Python UDFs](udf-creating-a-scalar-udf.md "udf-creating-a-scalar-udf.md")
- [Scalar Lambda UDFs](udf-creating-a-lambda-sql-udf.md "udf-creating-a-lambda-sql-udf.md")
- [Use case examples for user-defined functions (UDFs)](udf-example-uses.md "udf-example-uses.md")
