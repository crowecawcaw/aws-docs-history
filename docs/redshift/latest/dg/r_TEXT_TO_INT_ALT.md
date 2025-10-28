Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TEXT_TO_INT_ALT

TEXT_TO_INT_ALT converts a character string to an integer using Teradata-style formatting. Fraction digits in the result are truncated.

## Syntax

```
TEXT_TO_INT_ALT (*expression* [ , '*format*'])
```

## Arguments

_expression_

An expression that results in one or more CHAR or VARCHAR values, such as a column name or literal string. Converting null values returns nulls. The function converts blank or empty strings to 0.

_format_

A string literal that defines the format of the input expression. For more information about the formatting characters you can specify, see [Teradata-style formatting characters for numeric data](r_Numeric-format-teradata.md "r_Numeric-format-teradata.md").

## Return type

TEXT_TO_INT_ALT returns an INTEGER value.

The fractional portion of the cast result is truncated.

Amazon Redshift returns an error if the conversion to the _format_
phrase that you specify isn't successful.

## Examples

The following example converts the input _expression_ string '123-' to the integer -123.

```
select text_to_int_alt('123-');
```

```
text_to_int_alt
----------
      -123

```

The following example converts the input _expression_ string '2147483647+' to the integer 2147483647.

```
select text_to_int_alt('2147483647+');
```

```
text_to_int_alt
----------
2147483647

```

The following example converts the exponential input _expression_ string '-123E-2' to the integer -1.

```
select text_to_int_alt('-123E-2');
```

```
text_to_int_alt
----------
        -1

```

The following example converts the input _expression_ string '2147483647+' to the integer 2147483647.

```
select text_to_int_alt('2147483647+');
```

```
text_to_int_alt
----------
2147483647

```

The following example converts the input _expression_ string
'123{' with the _format_ phrase '999S' to the integer 1230. The S
character indicates a Signed Zoned Decimal. For more information, see [Teradata-style formatting characters for numeric data](r_Numeric-format-teradata.md "r_Numeric-format-teradata.md").

```
select text_to_int_alt('123{', '999S');
```

```
text_to_int_alt
----------
      1230
```

The following example converts the input _expression_ string 'USD123' with the _format_ phrase 'C9(I)' to the integer 123. See [Teradata-style formatting characters for numeric data](r_Numeric-format-teradata.md "r_Numeric-format-teradata.md").

```
select text_to_int_alt('USD123', 'C9(I)');
```

```
text_to_int_alt
----------
       123
```

The following example specifies a table column as the input _expression_.

```
select text_to_int_alt(a), text_to_int_alt(b) from t_text2int order by 1;
```

```
 text_to_int_alt | text_to_int_alt
-----------------+-----------------
            -123 |            -123
            -123 |            -123
             123 |             123
             123 |             123
```

Following is the table definition and the insert statement for this example.

```
create table t_text2int (a varchar(200), b char(200));
```

```
insert into t_text2int VALUES('123', '123'),('123.123', '123.123'), ('-123', '-123'), ('123-', '123-');

```
