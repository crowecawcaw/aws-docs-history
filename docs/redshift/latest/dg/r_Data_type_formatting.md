Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Data type formatting functions

###### Topics

- [CAST function](r_CAST_function.md "r_CAST_function.md")
- [CONVERT function](r_CONVERT_function.md "r_CONVERT_function.md")
- [TEXT_TO_INT_ALT](r_TEXT_TO_INT_ALT.md "r_TEXT_TO_INT_ALT.md")
- [TEXT_TO_NUMERIC_ALT](r_TEXT_TO_NUMERIC_ALT.md "r_TEXT_TO_NUMERIC_ALT.md")
- [TO_CHAR](r_TO_CHAR.md "r_TO_CHAR.md")
- [TO_DATE function](r_TO_DATE_function.md "r_TO_DATE_function.md")
- [TO_NUMBER](r_TO_NUMBER.md "r_TO_NUMBER.md")
- [TRY_CAST function](r_TRY_CAST.md "r_TRY_CAST.md")
- [Datetime format strings](r_FORMAT_strings.md "r_FORMAT_strings.md")
- [Numeric format strings](r_Numeric_formating.md "r_Numeric_formating.md")
- [Teradata-style formatting characters for numeric data](r_Numeric-format-teradata.md "r_Numeric-format-teradata.md")
  Data type formatting functions provide an easy way to convert values from one data type
  to another. For each of these functions, the first argument is always the value to be
  formatted and the second argument contains the template for the new format. Amazon Redshift
  supports several data type formatting functions.
