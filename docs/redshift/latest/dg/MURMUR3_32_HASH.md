Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# MURMUR3_32_HASH

The MURMUR3_32_HASH function computes the 32-bit Murmur3A non-cryptographic hash for
all common data types including numeric and string types.

## Syntax

```
MURMUR3_32_HASH(value [, seed])
```

## Arguments

_value_

The input value to hash. Amazon Redshift hashes the binary representation of the input value. This
behavior is similar to [FNV_HASH function](r_FNV_HASH.md "r_FNV_HASH.md"), but the value is
converted to the binary representation specified
by the [Apache Iceberg 32-bit Murmur3 hash specification](https://iceberg.apache.org/spec/#appendix-b-32-bit-hash-requirements "https://iceberg.apache.org/spec/#appendix-b-32-bit-hash-requirements").

_seed_

The INT seed of the hash
function. This argument is optional. If not given, Amazon Redshift
uses the default seed of 0. This enables combining the hash of
multiple columns without any conversions or concatenations.

## Return type

The function returns an INT.

## Example

The following examples return the Murmur3 hash of a number, the string 'Amazon Redshift', and the concatenation of the two.

```
select MURMUR3_32_HASH(1);

    MURMUR3_32_HASH
----------------------
 1392991556
(1 row)
```

```
select MURMUR3_32_HASH('Amazon Redshift');

    MURMUR3_32_HASH
----------------------
 -1563580564
(1 row)
```

```
select MURMUR3_32_HASH('Amazon Redshift', MURMUR3_32_HASH(1));

    MURMUR3_32_HASH
----------------------
 -1346554171
(1 row)
```

## Usage notes

To compute the hash of a table with multiple columns, you can compute the Murmur3 hash
of the first column and pass it as a seed to the hash of the second column. Then,
it passes the Murmur3 hash of the second column as a seed to the hash of the third
column.

The following example creates seeds to hash a table with multiple columns.

```
select MURMUR3_32_HASH(column_3, MURMUR3_32_HASH(column_2, MURMUR3_32_HASH(column_1))) from sample_table;
```

The same property can be used to compute the hash of a concatenation of strings.

```
select MURMUR3_32_HASH('abcd');

   MURMUR3_32_HASH
---------------------
 1139631978
(1 row)

```

```
select MURMUR3_32_HASH('cd', MURMUR3_32_HASH('ab'));

   MURMUR3_32_HASH
---------------------
 1711522338
(1 row)

```

The hash function uses the type of the input to determine the number of bytes to hash. Use casting to enforce a specific type, if necessary.

The following examples use different input types to produce different
results.

```
select MURMUR3_32_HASH(1, MURMUR3_32_HASH(1));

   MURMUR3_32_HASH
--------------------
 -1193428387
(1 row)
```

```
select MURMUR3_32_HASH(1);

   MURMUR3_32_HASH
----------------------
 1392991556
(1 row)
```

```
select MURMUR3_32_HASH(1, MURMUR3_32_HASH(2));

   MURMUR3_32_HASH
----------------------
 1179621905
(1 row)
```
