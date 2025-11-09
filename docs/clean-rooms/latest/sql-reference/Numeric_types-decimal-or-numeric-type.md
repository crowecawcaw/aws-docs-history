# DECIMAL or NUMERIC type

Use the DECIMAL or NUMERIC data type to store values with a _user-defined
precision_. The DECIMAL and NUMERIC keywords are interchangeable. In this
document, _decimal_ is the preferred term for this data type. The
term _numeric_ is used generically to refer to integer, decimal, and
floating-point data types.

| Storage                                                  | Range                                                         |
| -------------------------------------------------------- | ------------------------------------------------------------- |
| Variable, up to 128 bits for uncompressed DECIMAL types. | 128-bit signed integers with up to 38 digits of<br>precision. |

Define a DECIMAL column in a table by specifying a
`precision` and `scale`:

```
decimal(`precision`, `scale`)
```

`precision`

The total number of significant digits in the whole value: the number of
digits on both sides of the decimal point. For example, the number
`48.2891` has a precision of 6 and a scale of 4. The default
precision, if not specified, is 18. The maximum precision is 38.

If the number of digits to the left of the decimal point in an input value
exceeds the precision of the column minus its scale, the value can't be copied
into the column (or inserted or updated). This rule applies to any value that
falls outside the range of the column definition. For example, the allowed
range of values for a `numeric(5,2)` column is `-999.99`
to `999.99`.

`scale`

The number of decimal digits in the fractional part of the value, to the
right of the decimal point. Integers have a scale of zero. In a column
specification, the scale value must be less than or equal to the precision
value. The default scale, if not specified, is 0. The maximum scale is 37.

If the scale of an input value that is loaded into a table is greater than
the scale of the column, the value is rounded to the specified scale. For
example, the PRICEPAID column in the SALES table is a DECIMAL(8,2) column. If a
DECIMAL(8,4) value is inserted into the PRICEPAID column, the value is rounded
to a scale of 2.

```
insert into sales
values (0, 8, 1, 1, 2000, 14, 5, 4323.8951, 11.00, null);

select pricepaid, salesid from sales where salesid=0;

pricepaid | salesid
-----------+---------
4323.90 |       0
(1 row)
```

However, results of explicit casts of values selected from tables are not
rounded.

###### Note

The maximum positive value that you can insert into a DECIMAL(19,0) column is
`9223372036854775807` (263 -1). The maximum
negative value is `-9223372036854775807`. For example, an attempt to
insert the value `9999999999999999999` (19 nines) will cause an overflow
error. Regardless of the placement of the decimal point, the largest string that
AWS Clean Rooms can represent as a DECIMAL number is `9223372036854775807`. For
example, the largest value that you can load into a DECIMAL(19,18) column is
`9.223372036854775807`.

These rules are because of the following:

- DECIMAL values with 19 or fewer significant digits of precision are stored
  internally as 8-byte integers.
- DECIMAL values with 20 to 38 significant digits of precision are stored as
  16-byte integers.

## Notes about using 128-bit DECIMAL or NUMERIC columns

Do not arbitrarily assign maximum precision to DECIMAL columns unless you are
certain that your application requires that precision. 128-bit values use twice as
much disk space as 64-bit values and can slow down query execution time.
