# VARBYTE type

Use a VARBYTE, VARBINARY, or BINARY VARYING column to store variable-length binary value
with a fixed limit.

```
varbyte [ (*n*) ]
```

The maximum number of bytes (_n_) can range from 1 –
1,024,000. The default is 64,000.

Some examples where you might want to use a VARBYTE data type are as follows:

- Joining tables on VARBYTE columns.
- Creating materialized views that contain VARBYTE columns. Incremental refresh of
  materialized views that contain VARBYTE columns is supported. However, aggregate
  functions other than COUNT, MIN, and MAX and GROUP BY on VARBYTE columns don't
  support incremental refresh.
  To ensure that all bytes are printable characters, AWS Clean Rooms uses the hex format to print
  VARBYTE values. For example, the following SQL converts the hexadecimal string
  `6162` into a binary value. Even though the returned value is a binary value,
  the results are printed as hexadecimal `6162`.

```
select from_hex('6162');

 from_hex
----------
 6162
```

AWS Clean Rooms supports casting between VARBYTE and the following data types:

- CHAR
- VARCHAR
- SMALLINT or SHORT
- INTEGER
- BIGINT or LONG
  The following SQL statement casts a VARCHAR string to a VARBYTE. Even though the
  returned value is a binary value, the results are printed as hexadecimal
  `616263`.

```
select 'abc'::varbyte;

 varbyte
---------
 616263
```

The following SQL statement casts a CHAR value in a column to a VARBYTE. This example
creates a table with a CHAR(10) column (c), inserts character values that are shorter than
the length of 10. The resulting cast pads the result with a space characters (hex'20') to
the defined column size. Even though the returned value is a binary value, the results are
printed as hexadecimal.

```
create table t (c char(10));
insert into t values ('aa'), ('abc');
select c::varbyte from t;
          c
----------------------
 61612020202020202020
 61626320202020202020

```

The following SQL statement casts a SMALLINT string to a VARBYTE. Even though the
returned value is a binary value, the results are printed as hexadecimal `0005`,
which is two bytes or four hexadecimal characters.

```
select 5::smallint::varbyte;

 varbyte
---------
 0005
```

The following SQL statement casts an INTEGER to a VARBYTE. Even though the returned
value is a binary value, the results are printed as hexadecimal `00000005`,
which is four bytes or eight hexadecimal characters.

```
select 5::int::varbyte;

 varbyte
----------
 00000005
```

The following SQL statement casts a BIGINT to a VARBYTE. Even though the returned value
is a binary value, the results are printed as hexadecimal `0000000000000005`,
which is eight bytes or 16 hexadecimal characters.

```
select 5::bigint::varbyte;

     varbyte
------------------
 0000000000000005
```

## Limitations when using the VARBYTE data type with

AWS Clean Rooms

The following are limitations when using the VARBYTE data type with AWS Clean Rooms:

- AWS Clean Rooms supports the VARBYTE data type only for Parquet and ORC files.
- AWS Clean Rooms query editor don't yet fully support VARBYTE data type. Therefore, use a
  different SQL client when working with VARBYTE expressions.

As a workaround to use the query editor, if the length of your data is below 64
KB and the content is valid UTF-8, you can cast the VARBYTE values to VARCHAR, for
example:

```
select to_varbyte('6162', 'hex')::varchar;
```

- You can't use VARBYTE data types with Python or Lambda user-defined functions
  (UDFs).
- You can't create a HLLSKETCH column from a VARBYTE column or use APPROXIMATE
  COUNT DISTINCT on a VARBYTE column.
