

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Data type formatting functions
<a name="r_Data_type_formatting"></a>

**Topics**
+ [CAST function](r_CAST_function.md)
+ [CONVERT function](r_CONVERT_function.md)
+ [TEXT\_TO\_INT\_ALT](r_TEXT_TO_INT_ALT.md)
+ [TEXT\_TO\_NUMERIC\_ALT](r_TEXT_TO_NUMERIC_ALT.md)
+ [TO\_CHAR](r_TO_CHAR.md)
+ [TO\_DATE function](r_TO_DATE_function.md)
+ [TO\_NUMBER](r_TO_NUMBER.md)
+ [TRY\_CAST function](r_TRY_CAST.md)
+ [Datetime format strings](r_FORMAT_strings.md)
+ [Numeric format strings](r_Numeric_formating.md)
+ [Teradata-style formatting characters for numeric data](r_Numeric-format-teradata.md)

Data type formatting functions provide an easy way to convert values from one data type to another. For each of these functions, the first argument is always the value to be formatted and the second argument contains the template for the new format. Amazon Redshift supports several data type formatting functions.