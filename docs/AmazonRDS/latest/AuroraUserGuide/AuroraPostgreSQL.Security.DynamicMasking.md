# Pre-defined data masking functions

`pg_columnmask` extension provides built-in utility functions written in C language
(for faster execution) which can be used as masking expression for `pg_columnmask` policies.

**mask_text**

A function to mask text data with configurable visibility options.

**Arguments**

| Parameter        | Datatype | Description                                                                                   |
| ---------------- | -------- | --------------------------------------------------------------------------------------------- |
| `input`          | TEXT     | The original text string to be masked                                                         |
| `mask_char`      | CHAR(1)  | Character used for masking (default: 'X')                                                     |
| `visible_prefix` | INT      | Number of characters at the beginning of input text that will<br>remain unmasked (default: 0) |
| `visible_suffix` | INT      | Number of characters at the end of input text that will remain<br>unmasked (default: 0)       |
| `use_hash_mask`  | BOOLEAN  | If TRUE, uses a hash-based masking instead of mask_char (default: FALSE)                      |

###### Example of using different masking options

Mask the entire input string with the default 'X' character

```
postgres=> SELECT pgcolumnmask.mask_text('Hello World');
  mask_text
-------------
 XXXXXXXXXXX
```

Use the `mask_char` argument to mask text input using a different character

```
postgres=> SELECT pgcolumnmask.mask_text('Hello World', '*');
  mask_text
-------------
 ***********
```

Use `visible_prefix` and `visible_suffix` parameters to control how many characters remain unmasked at the start and end of the text

```
postgres=> SELECT pgcolumnmask.mask_text('Hello World', '*', 5, 1);
  mask_text
-------------
 Hello*****d
```

When `use_hash_mask` is true the input string is masked using random characters
`mask_char` argument is ignored but `visible_prefix` and `visible_suffix` are still honored

```
postgres=> SELECT pgcolumnmask.mask_text('Hello World', '*', 2, 2, true);
  mask_text
-------------
 Hex36dOHild
```

**mask_timestamp**

| Parameter    | Datatype  | Description                                                                                                                            |
| ------------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `ts_to_mask` | TIMESTAMP | The original timestamp to be masked                                                                                                    |
| `mask_part`  | TEXT      | Specifies which part of the timestamp to mask (default: 'all') Valid values: 'year', 'month', 'day', 'hour', 'minute', 'second', 'all' |
| `mask_value` | TIMESTAMP | The timestamp value to use for masking (default: '1900-01-01 00:00:00')                                                                |

###### Example of using `mask_timestamps`

These examples demonstrate complete timestamp masking to a default value, partial masking
of specific timestamp components (year only), and masking with a custom replacement value.

Completely mask input value to the default timestamp

```
postgres=> SELECT pgcolumnmask.mask_timestamp('2023-06-15 14:30:00');
   mask_timestamp
---------------------
 1900-01-01 00:00:00
```

To mask only one part of the timestamp from example only the year

```
postgres=> SELECT pgcolumnmask.mask_timestamp('2023-06-15 14:30:00', 'year');
   mask_timestamp
---------------------
 1900-06-15 14:30:00
```

To change the masked value for timestamp use the `mask_value` argument

```
postgres=> SELECT pgcolumnmask.mask_timestamp('2023-06-15 14:30:00', 'all', '2012-12-12 12:12:12');
   mask_timestamp
---------------------
 2012-12-12 12:12:12
```

**mask_timestamp**

A function to mask email addresses while preserving email structure.

| Parameter     | Datatype | Description                                                       |
| ------------- | -------- | ----------------------------------------------------------------- |
| `input`       | TEXT     | The original email address to be masked                           |
| `mask_char`   | CHAR(1)  | Character used for masking (default: 'X')                         |
| `mask_local`  | BOOLEAN  | If TRUE, masks the local part of email (before @) (default: TRUE) |
| `mask_domain` | BOOLEAN  | If TRUE, masks the domain part of email (after @) (default: TRUE) |

###### Example of using `mask_email`

These examples demonstrate complete email masking, custom mask characters, and selective masking of either the local part or domain part of the email address.

Complete masking

```
postgres=> SELECT pgcolumnmask.mask_email('user@example.com');
    mask_email
------------------
 XXXX@XXXXXXX.com
```

Use `mask_char` to change the character used for masking

```
postgres=> SELECT pgcolumnmask.mask_email('user@example.com', '*');
    mask_email
------------------
 ****@*******.com
```

Use `mask_local` and `mask_domain` to control masking on local and domain

```
postgres=> SELECT pgcolumnmask.mask_email('user@example.com', '*', true, false);
    mask_email
------------------
 ****@example.com

postgres=> SELECT pgcolumnmask.mask_email('user@example.com', '*', false, true);
    mask_email
------------------
 user@*******.com
```
