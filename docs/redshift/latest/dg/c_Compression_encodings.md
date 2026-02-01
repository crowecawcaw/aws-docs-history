Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Compression encodings

A _compression encoding_ specifies the type of compression
that is applied to a column of data values as rows are added to a table.

ENCODE AUTO is the default for tables. When a table is set to ENCODE AUTO, Amazon Redshift automatically manages compression encoding
for all columns in the table.
For more information, see [CREATE TABLE](r_CREATE_TABLE_NEW.md "r_CREATE_TABLE_NEW.md")
and [ALTER TABLE](r_ALTER_TABLE.md "r_ALTER_TABLE.md").

However, if you specify compression encoding for any column in the table, the table is no longer set to ENCODE AUTO.
Amazon Redshift no longer automatically manages compression encoding for all columns in the table.

When you use CREATE TABLE, ENCODE AUTO is disabled when you specify
compression encoding for any column in the table. If ENCODE AUTO is disabled,
Amazon Redshift automatically assigns compression encoding to columns for which you
don't specify an ENCODE type as follows:

- Columns that are defined as sort keys are assigned RAW compression.
- Columns that are defined as BOOLEAN, REAL, or DOUBLE PRECISION data types
  are assigned RAW compression.
- Columns that are defined as SMALLINT, INTEGER, BIGINT, DECIMAL, DATE, TIMESTAMP, or TIMESTAMPTZ data types are assigned AZ64 compression.
- Columns that are defined as CHAR or VARCHAR data types are assigned LZO compression.
  You can change a table's encoding after creating it by using ALTER TABLE.
  If you disable ENCODE AUTO using ALTER TABLE, Amazon Redshift no longer automatically manages
  compression encodings for your columns. All columns will keep the compression encoding
  types that they had when you disabled ENCODE AUTO until you change them or you
  enable ENCODE AUTO again.

Amazon Redshift supports the following compression encodings:

Raw
Raw encoding is the default encoding for columns that are designated as sort
keys and columns that are defined as BOOLEAN, REAL, or DOUBLE PRECISION data
types. With raw encoding, data is stored in raw, uncompressed form.

AZ64
AZ64 is a proprietary compression encoding algorithm designed by Amazon to
achieve a high compression ratio and improved query processing. At its core, the
AZ64 algorithm compresses smaller groups of data values and uses single
instruction, multiple data (SIMD) instructions for parallel processing. Use AZ64
to achieve significant storage savings and high performance for numeric, date,
and time data types.

You can use AZ64 as the compression encoding when defining columns using
CREATE TABLE and ALTER TABLE statements with the following data types:

- SMALLINT
- INTEGER
- BIGINT
- DECIMAL
- DATE
- TIMESTAMP
- TIMESTAMPTZ

Byte-dictionary
In byte dictionary encoding, a separate dictionary of unique values is created
for each block of column values on disk. (An Amazon Redshift disk block occupies 1 MB.)
The dictionary contains up to 256 one-byte values that are stored as indexes to
the original data values. If more than 256 values are stored in a single block,
the extra values are written into the block in raw, uncompressed form. The
process repeats for each disk block.

This encoding is very effective on low cardinality string columns. This
encoding is optimal when the data domain of a column is fewer than 256 unique
values.

For columns with the string data type (CHAR and VARCHAR) encoded with
BYTEDICT, Amazon Redshift performs vectorized scans and predicate evaluations that
operate over compressed data directly. These scans use hardware-specific single
instruction and multiple data (SIMD) instructions for parallel processing. This
significantly speeds up the scanning of string
columns. Byte-dictionary encoding is especially space-efficient if a CHAR/VARCHAR column holds long character strings.

Suppose that a table has a COUNTRY column with a CHAR(30) data type. As data
is loaded, Amazon Redshift creates the dictionary and populates the COUNTRY column with
the index value. The dictionary contains the indexed unique values, and the
table itself contains only the one-byte subscripts of the corresponding
values.

###### Note

Trailing blanks are stored for fixed-length character columns. Therefore,
in a CHAR(30) column, every compressed value saves 29 bytes of storage when
you use the byte-dictionary encoding.

The following table represents the dictionary for the COUNTRY column.

| Unique data value        | Dictionary index | Size (fixed length, 30 bytes per value) |
| ------------------------ | ---------------- | --------------------------------------- |
| England                  | 0                | 30                                      |
| United States of America | 1                | 30                                      |
| Venezuela                | 2                | 30                                      |
| Sri Lanka                | 3                | 30                                      |
| Argentina                | 4                | 30                                      |
| Japan                    | 5                | 30                                      |
| Total                    |                  | 180                                     |

The following table represents the values in the COUNTRY column.

| Original data value      | Original size (fixed length, 30 bytes per<br>value) | Compressed value (index) | New size (bytes) |
| ------------------------ | --------------------------------------------------- | ------------------------ | ---------------- |
| England                  | 30                                                  | 0                        | 1                |
| England                  | 30                                                  | 0                        | 1                |
| United States of America | 30                                                  | 1                        | 1                |
| United States of America | 30                                                  | 1                        | 1                |
| Venezuela                | 30                                                  | 2                        | 1                |
| Sri Lanka                | 30                                                  | 3                        | 1                |
| Argentina                | 30                                                  | 4                        | 1                |
| Japan                    | 30                                                  | 5                        | 1                |
| Sri Lanka                | 30                                                  | 3                        | 1                |
| Argentina                | 30                                                  | 4                        | 1                |
| Total                    | 300                                                 |                          | 10               |

The total compressed size in this example is calculated as follows: 6
different entries are stored in the dictionary (6 \* 30 = 180), and the table
contains 10 1-byte compressed values, for a total of 190 bytes.

Delta
Delta encodings are very useful for date time columns.

Delta encoding compresses data by recording the difference between values that
follow each other in the column. This difference is recorded in a separate
dictionary for each block of column values on disk. (An Amazon Redshift disk block
occupies 1 MB.) For example, suppose that the column contains 10 integers in
sequence from 1 to 10. The first are stored as a 4-byte integer (plus a 1-byte
flag). The next nine are each stored as a byte with the value 1, indicating that
it is one greater than the previous value.

Delta encoding comes in two variations:

- DELTA records the differences as 1-byte values (8-bit integers)
- DELTA32K records differences as 2-byte values (16-bit integers)

If most of the values in the column could be compressed by using a single
byte, the 1-byte variation is very effective. However, if the deltas are larger,
this encoding, in the worst case, is somewhat less effective than storing the
uncompressed data. Similar logic applies to the 16-bit version.

If the difference between two values exceeds the 1-byte range (DELTA) or
2-byte range (DELTA32K), the full original value is stored, with a leading
1-byte flag. The 1-byte range is from -127 to 127, and the 2-byte range is from
-32K to 32K.

The following table shows how a delta encoding works for a numeric
column.

| Original data value | Original size (bytes) | Difference (delta) | Compressed value | Compressed size (bytes)      |
| ------------------- | --------------------- | ------------------ | ---------------- | ---------------------------- |
| 1                   | 4                     |                    | 1                | 1+4 (flag + actual<br>value) |
| 5                   | 4                     | 4                  | 4                | 1                            |
| 50                  | 4                     | 45                 | 45               | 1                            |
| 200                 | 4                     | 150                | 150              | 1+4 (flag + actual<br>value) |
| 185                 | 4                     | -15                | -15              | 1                            |
| 220                 | 4                     | 35                 | 35               | 1                            |
| 221                 | 4                     | 1                  | 1                | 1                            |
| Totals              | 28                    |                    |                  | 15                           |

LZO
LZO encoding provides a very high compression ratio with good performance. LZO
encoding works especially well for CHAR and VARCHAR columns that store very long
character strings. They are especially good for free-form text, such as product
descriptions, user comments, or JSON strings.

Mostly
Mostly encodings are useful when the data type for a column is larger than
most of the stored values require. By specifying a mostly encoding for this type
of column, you can compress the majority of the values in the column to a
smaller standard storage size. The remaining values that cannot be compressed
are stored in their raw form. For example, you can compress a 16-bit column,
such as an INT2 column, to 8-bit storage.

In general, the mostly encodings work with the following data types:

- SMALLINT/INT2 (16-bit)
- INTEGER/INT (32-bit)
- BIGINT/INT8 (64-bit)
- DECIMAL/NUMERIC (64-bit)

Choose the appropriate variation of the mostly encoding to suit the size of
the data type for the column. For example, apply MOSTLY8 to a column that is
defined as a 16-bit integer column. Applying MOSTLY16 to a column with a 16-bit
data type or MOSTLY32 to a column with a 32-bit data type is disallowed.

Mostly encodings might be less effective than no compression when a relatively
high number of the values in the column can't be compressed. Before applying one
of these encodings to a column, perform a check. _Most_ of
the values that you are going to load now (and are likely to load in the future)
should fit into the ranges shown in the following table.

| Encoding | Compressed storage size | Range of values that can be compressed<br>(values outside the range are stored raw) |
| -------- | ----------------------- | ----------------------------------------------------------------------------------- |
| MOSTLY8  | 1 byte (8 bits)         | -128 to 127                                                                         |
| MOSTLY16 | 2 bytes (16 bits)       | -32768 to 32767                                                                     |
| MOSTLY32 | 4 bytes (32 bits)       | -2147483648 to +2147483647                                                          |

###### Note

For decimal values, ignore the decimal point to determine whether the
value fits into the range. For example, 1,234.56 is treated as 123,456 and
can be compressed in a MOSTLY32 column.

For example, the VENUEID column in the VENUE table is defined as a raw integer
column, which means that its values consume 4 bytes of storage. However, the
current range of values in the column is `0` to
`309`. Therefore, recreating and reloading this table
with MOSTLY16 encoding for VENUEID would reduce the storage of every value in
that column to 2 bytes.

If the VENUEID values referenced in another table were mostly in the range of
0 to 127, it might make sense to encode that foreign-key column as MOSTLY8.
Before making the choice, run several queries against the referencing table data
to find out whether the values mostly fall into the 8-bit, 16-bit, or 32-bit
range.

The following table shows compressed sizes for specific numeric values when
the MOSTLY8, MOSTLY16, and MOSTLY32 encodings are used:

| Original value | Original INT or BIGINT size (bytes) | MOSTLY8 compressed size (bytes) | MOSTLY16 compressed size (bytes) | MOSTLY32 compressed size (bytes) |
| -------------- | ----------------------------------- | ------------------------------- | -------------------------------- | -------------------------------- |
| 1              | 4                                   | 1                               | 2                                | 4                                |
| 10             | 4                                   | 1                               | 2                                | 4                                |
| 100            | 4                                   | 1                               | 2                                | 4                                |
| 1000           | 4                                   | Same as raw data size           | 2                                | 4                                |
| 10000          | 4                                   | 2                               | 4                                |
| 20000          | 4                                   | 2                               | 4                                |
| 40000          | 8                                   | Same as raw data size           | 4                                |
| 100000         | 8                                   | 4                               |
| 2000000000     | 8                                   | 4                               |

Run length
Run length encoding replaces a value that is repeated consecutively with a
token that consists of the value and a count of the number of consecutive
occurrences (the length of the run). A separate dictionary of unique values is
created for each block of column values on disk. (An Amazon Redshift disk block
occupies 1 MB.) This encoding is best suited to a table in which data values are
often repeated consecutively, for example, when the table is sorted by those
values.

For example, suppose that a column in a large dimension table has a
predictably small domain, such as a COLOR column with fewer than 10 possible
values. These values are likely to fall in long sequences throughout the table,
even if the data is not sorted.

We don't recommend applying run length encoding on any column that is
designated as a sort key. Range-restricted scans perform better when blocks
contain similar numbers of rows. If sort key columns are compressed much more
highly than other columns in the same query, range-restricted scans might
perform poorly.

The following table uses the COLOR column example to show how the run length
encoding works.

| Original data value | Original size (bytes) | Compressed value (token) | Compressed size (bytes) |
| ------------------- | --------------------- | ------------------------ | ----------------------- |
| Blue                | 4                     | {2,Blue}                 | 5                       |
| Blue                | 4                     | 0                        |
| Green               | 5                     | {3,Green}                | 6                       |
| Green               | 5                     | 0                        |
| Green               | 5                     | 0                        |
| Blue                | 4                     | {1,Blue}                 | 5                       |
| Yellow              | 6                     | {4,Yellow}               | 7                       |
| Yellow              | 6                     | 0                        |
| Yellow              | 6                     | 0                        |
| Yellow              | 6                     | 0                        |
| Total               | 51                    |                          | 23                      |

Text255 and Text32k
Text255 and text32k encodings are useful for compressing VARCHAR columns in
which the same words recur often. A separate dictionary of unique words is
created for each block of column values on disk. (An Amazon Redshift disk block
occupies 1 MB.) The dictionary contains the first 245 unique words in the
column. Those words are replaced on disk by a one-byte index value representing
one of the 245 values, and any words that are not represented in the dictionary
are stored uncompressed. The process repeats for each 1-MB disk block. If the
indexed words occur frequently in the column, the column yields a high
compression ratio.

For the text32k encoding, the principle is the same, but the dictionary for
each block does not capture a specific number of words. Instead, the dictionary
indexes each unique word it finds until the combined entries reach a length of
32K, minus some overhead. The index values are stored in two bytes.

For example, consider the VENUENAME column in the VENUE table. Words such as
`Arena`, `Center`, and
`Theatre` recur in this column and are likely to be
among the first 245 words encountered in each block if text255 compression is
applied. If so, this column benefits from compression. This is because every
time those words appear, they occupy only 1 byte of storage (instead of 5, 6, or
7 bytes, respectively).

ZSTD
Zstandard (ZSTD) encoding provides a high compression ratio with very good
performance across diverse datasets. ZSTD works especially well with CHAR and
VARCHAR columns that store a wide range of long and short strings, such as
product descriptions, user comments, logs, and JSON strings. Where some
algorithms, such as Delta encoding or Mostly encoding, can potentially use
more storage space than no compression, ZSTD is
unlikely to increase disk usage.

ZSTD supports SMALLINT, INTEGER, BIGINT, DECIMAL, REAL, DOUBLE PRECISION, BOOLEAN,
CHAR, VARCHAR, DATE, TIMESTAMP, and TIMESTAMPTZ data types.

The following table identifies the supported compression encodings and the data
types that support the encoding.

| Encoding type        | Keyword in CREATE TABLE and ALTER TABLE | Data types                                                                                                                    |
| -------------------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Raw (no compression) | RAW                                     | All                                                                                                                           |
| AZ64                 | AZ64                                    | SMALLINT, INTEGER, BIGINT, DECIMAL, DATE, TIMESTAMP, TIMESTAMPTZ                                                              |
| Byte dictionary      | BYTEDICT                                | SMALLINT, INTEGER, BIGINT, DECIMAL, REAL, DOUBLE PRECISION, CHAR, VARCHAR, DATE, TIMESTAMP, TIMESTAMPTZ                       |
| Delta                | DELTA<br>DELTA32K                       | SMALLINT, INT, BIGINT, DATE, TIMESTAMP,<br>DECIMAL<br>INT, BIGINT, DATE, TIMESTAMP, DECIMAL                                   |
| LZO                  | LZO                                     | SMALLINT, INTEGER, BIGINT, DECIMAL, CHAR, VARCHAR,<br>DATE, TIMESTAMP, TIMESTAMPTZ, SUPER                                     |
| Mostly*n*            | MOSTLY8<br>MOSTLY16<br>MOSTLY32         | SMALLINT, INT, BIGINT, DECIMAL<br>INT, BIGINT, DECIMAL<br>BIGINT, DECIMAL                                                     |
| Run-length           | RUNLENGTH                               | SMALLINT, INTEGER, BIGINT, DECIMAL, REAL, DOUBLE PRECISION, BOOLEAN, CHAR, VARCHAR, DATE, TIMESTAMP, TIMESTAMPTZ              |
| Text                 | TEXT255<br>TEXT32K                      | VARCHAR only<br>VARCHAR only                                                                                                  |
| Zstandard            | ZSTD                                    | SMALLINT, INTEGER, BIGINT, DECIMAL, REAL, DOUBLE<br>PRECISION, BOOLEAN, CHAR, VARCHAR, DATE, TIMESTAMP, TIMESTAMPTZ,<br>SUPER |
