

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Numeric format strings
<a name="r_Numeric_formating"></a>

Following, you can find a reference for numeric format strings. 

The following format strings apply to functions such as TO\_NUMBER and TO\_CHAR. 
+ For examples of formatting strings as numbers, see [TO\_NUMBER](r_TO_NUMBER.md).
+ For examples of formatting numbers as strings, see [TO\_CHAR](r_TO_CHAR.md).


| Format  | Description  | 
| --- | --- | 
| 9  | Numeric value with the specified number of digits.  | 
| 0  | Numeric value with leading zeros.  | 
| . (period), D  | Decimal point.  | 
| , (comma)  | Thousands separator.  | 
| CC  | Century code. For example, the 21st century started on 2001-01-01 (supported for TO\_CHAR only).  | 
| FM | Fill mode. Suppress padding blanks and zeroes. | 
| PR  | Negative value in angle brackets.  | 
| S  | Sign anchored to a number.  | 
| L  | Currency symbol in the specified position.  | 
| G  | Group separator.  | 
| MI  | Minus sign in the specified position for numbers that are less than 0.  | 
| PL  | Plus sign in the specified position for numbers that are greater than 0.  | 
| SG  | Plus or minus sign in the specified position.  | 
| RN  | Roman numeral between 1 and 3999 (supported for TO\_CHAR only).  | 
| TH or th  | Ordinal number suffix. Does not convert fractional numbers or values that are less than zero.  | 