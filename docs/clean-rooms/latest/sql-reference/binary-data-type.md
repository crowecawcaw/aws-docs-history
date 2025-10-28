# Binary type

Use the BINARY data type to store and manage fixed-length, uninterpreted binary data,
providing efficient storage and comparison capabilities for specific use cases.

The BINARY data type stores a fixed number of bytes, regardless of the actual length of
the data being stored. The maximum length is typically 255 bytes.

BINARY is used to store raw, uninterpreted binary data, such as images, documents, or
other types of files. The data is stored exactly as it is provided, without any character
encoding or interpretation. Binary data stored in BINARY columns is compared and sorted
byte-by-byte, based on the actual binary values, rather than any character encoding or
collation rules.

The following example query shows the binary representation of the string
`"abc"`. Each character in the string is represented by its ASCII code in
hexadecimal format: "a" is 0x61, "b" is 0x62, and "c" is 0x63. When combined, these
hexadecimal values form the binary representation `"616263"`.

```
SELECT 'abc'::binary;
binary
---------
 616263
```
