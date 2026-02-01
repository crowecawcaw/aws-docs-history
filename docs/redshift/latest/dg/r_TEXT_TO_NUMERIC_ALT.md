Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TEXT_TO_NUMERIC_ALT

TEXT_TO_NUMERIC_ALT performs a Teradata-style cast operation to convert a character string to a numeric data
format.

## Syntax

```
TEXT_TO_NUMERIC_ALT (*expression* [, '*format*'] [, *precision*, *scale*])
```

## Arguments

_expression_

An expression that evaluates to one or more CHAR or VARCHAR values, such as a column name or a literal. Converting null values returns nulls. Blank or empty strings are converted to 0.

_format_

A string literal that defines the format of the input expression. For more information, see [Teradata-style formatting characters for numeric data](r_Numeric-format-teradata.md "r_Numeric-format-teradata.md").

_precision_

The number of digits in the numeric result. The default is 38.

_scale_

The number of digits to the right of the decimal point in the numeric
result. The default is 0.

## Return type

TEXT_TO_NUMERIC_ALT returns a DECIMAL number.

Amazon Redshift returns an error if the conversion to the _format_
phrase that you specify isn't successful.

Amazon Redshift casts the input _expression_ string to the numeric
type with the highest precision that you specify for that type in the
_precision_ option. If the length of the numeric value exceeds the
value that you specify for _precision_, Amazon Redshift rounds the
numeric value according to the following rules:

- If the length of the cast result exceeds the length that you specify in the
  _format_ phrase, Amazon Redshift returns an error.
- If the result is cast to a numeric value, the result is rounded to the closest value. If the fractional portion is exactly midway between the upper and lower cast result, the result is rounded to the nearest even value.

## Examples

The following example converts the input _expression_ string '1.5' to the numeric value '2'. Because the statement doesn't specify _scale_, the _scale_ defaults to 0 and the cast result doesn't include a fraction result. Because .5 is midway between 1 and 2, the cast result is rounded to the even value of 2.

```
select text_to_numeric_alt('1.5');
```

```
 text_to_numeric_alt
---------------------
                   2
```

The following example converts the input _expression_ string '2.51' to the numeric value 3. Because the statement doesn't specify a _scale_ value, the _scale_ defaults to 0 and the cast result doesn't include a fraction result. Because .51 is closer to 3 than 2, the cast result is rounded to the value of 3.

```
select text_to_numeric_alt('2.51');
```

```
 text_to_numeric_alt
---------------------
                   3
```

The following example converts the input _expression_ string 123.52501 with a _precision_ of 10 and a _scale_ of 2 to the numeric value 123.53.

```
select text_to_numeric_alt('123.52501', 10, 2);
```

```
 text_to_numeric_alt
---------------------
               123.53
```

The following example converts the input _expression_ string
'123{' with the _format_ phrase '999S' to the numeric 1230. The S
character indicates a Signed Zoned Decimal. For more information, see [Teradata-style formatting characters for numeric data](r_Numeric-format-teradata.md "r_Numeric-format-teradata.md").

```
select text_to_numeric_alt('123{', '999S');
```

```
text_to_int_alt
----------
      1230
```

The following example converts the input _expression_ string 'USD123' with the _format_ phrase 'C9(I)' to the numeric 124. See [Teradata-style formatting characters for numeric data](r_Numeric-format-teradata.md "r_Numeric-format-teradata.md").

```
select text_to_numeric_alt('USD123.9', 'C9(I)');
```

```
text_to_numeric_alt
----------
       124
```

The following example specifies a table column as the input _expression_.

```
select text_to_numeric_alt(a), text_to_numeric_alt(b) from t_text2numeric order by 1;
```

```
           text_to_numeric_alt           |           text_to_numeric_alt
-----------------------------------------+-----------------------------------------
 -99999999999999999999999999999999999999 | -99999999999999999999999999999999999999
                                  -12300 |                                  -12300
                                     123 |                                     123
                                     123 |                                     123
  99999999999999999999999999999999999999 |  99999999999999999999999999999999999999
```

Following is the table definition and the insert statement for this example.

```
create table  t_text2numeric (a varchar(200), b char(200));
```

```
insert into  t_text2numeric values
('123', '123'),
('+123.456', '+123.456'),
('-' || repeat('9', 38), '-' || repeat('9', 38)),
(repeat('9', 38) || '+', repeat('9', 38) || '+'),
('-123E2', '-123E2');

```
