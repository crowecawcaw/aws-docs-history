# CHAR or CHARACTER

Use a CHAR or CHARACTER column to store fixed-length strings. These strings are
padded with blanks, so a CHAR(10) column always occupies 10 bytes of storage.

```
char(10)
```

A CHAR column without a length specification results in a CHAR(1) column.

CHAR data types are defined in terms of bytes, not characters. A CHAR column can only
contain single-byte characters, so a CHAR(10) column can contain a string with a maximum
length of 10 bytes.

| Name              | Storage                                              | Range (width of column) |
| ----------------- | ---------------------------------------------------- | ----------------------- |
| CHAR or CHARACTER | Length of string, including trailing blanks (if any) | 4096 bytes              |
