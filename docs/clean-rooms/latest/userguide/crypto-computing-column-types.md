# Column types in Cryptographic Computing for Clean Rooms

This topic provides information about column types in Cryptographic Computing for Clean Rooms.

###### Topics

- [Fingerprint columns](#fingerprint-columns "#fingerprint-columns")
- [Sealed columns](#sealed-columns "#sealed-columns")
- [Cleartext columns](#cleartext-columns "#cleartext-columns")

## Fingerprint columns

_Fingerprint columns_ are columns that are
protected cryptographically for use in JOIN statements.

Data from fingerprint columns can't be decrypted. Only data from sealed
columns can be decrypted.

Fingerprint columns must only be used in the following SQL clauses and
functions:

- JOIN (INNER, OUTER, LEFT, RIGHT, or FULL) against other
  fingerprint columns:
  - If the value of the `allowJoinsOnColumnsWithDifferentNames` parameter is set
    to `false`, both fingerprint columns of the JOIN
    must also have the same name.

- `SELECT COUNT()`
- `SELECT COUNT(DISTINCT )`
- `GROUP BY` (Only use if the collaboration has set the value of the
  `preserveNulls` parameter to `true`.)

Queries that violate these constraints might yield incorrect results.

## Sealed columns

_Sealed columns_ are columns that are protected
cryptographically for use in SELECT statements.

Sealed columns must only be used in the following SQL clauses and functions:

- `SELECT`
- `SELECT ... AS`
- `SELECT COUNT()`

###### Note

`SELECT COUNT(DISTINCT )` is not supported.

Queries that violate these constraints might yield incorrect results.

### Padding data for a sealed column before

encryption

When you specify that a column should be a sealed column, C3R
asks you what kind of _padding_ to choose. Padding data before
encryption is optional. Without padding (a pad type of `none`), the encrypted data’s
length indicates the size of the cleartext. In some circumstances, the size of
the cleartext could expose the plaintext. With padding (a pad type of
`fixed` or `max`), all values are first padded to a common size and then
encrypted. With padding, the length of the encrypted data provides no information about the
original cleartext length, other than giving an upper bound on its size.

If you want padding for a column and the maximal byte length of data in that column is
known, use `fixed` padding. Use a `length` value that is at least as large
as the byte-length of the longest value in that column.

###### Note

An error occurs and encryption fails if a value is longer than the provided
`length`.

If you want padding for a column and the maximal byte length of data in that column isn't
known, use `max` padding. This padding mode pads all data to the length of the
longest value plus additional `length` bytes.

###### Note

You might want to encrypt data in batches, or update your tables with new data
periodically. Be aware that `max` padding will pad entries to the length (plus
`length` byte) of the longest plaintext entry in a given batch. This means that the
ciphertext length may vary from batch to batch. Therefore, if you know the maximum byte-length
for a column, then you should use `fixed` instead of `max`.

## Cleartext columns

_Cleartext columns_ are columns that
aren't
protected cryptographically for use in JOIN or SELECT
statements.

Cleartext columns can be used in any part of the SQL query.
