Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# String functions

###### Topics

- [|| (Concatenation) operator](r_concat_op.md "r_concat_op.md")
- [ASCII function](r_ASCII.md "r_ASCII.md")
- [BPCHARCMP function](r_BPCHARCMP.md "r_BPCHARCMP.md")
- [BTRIM function](r_BTRIM.md "r_BTRIM.md")
- [BTTEXT_PATTERN_CMP function](r_BTTEXT_PATTERN_CMP.md "r_BTTEXT_PATTERN_CMP.md")
- [CHAR_LENGTH function](r_CHAR_LENGTH.md "r_CHAR_LENGTH.md")
- [CHARACTER_LENGTH function](r_CHARACTER_LENGTH.md "r_CHARACTER_LENGTH.md")
- [CHARINDEX function](r_CHARINDEX.md "r_CHARINDEX.md")
- [CHR function](r_CHR.md "r_CHR.md")
- [COLLATE function](r_COLLATE.md "r_COLLATE.md")
- [CONCAT function](r_CONCAT.md "r_CONCAT.md")
- [CRC32 function](crc32-function.md "crc32-function.md")
- [DIFFERENCE function](DIFFERENCE.md "DIFFERENCE.md")
- [INITCAP function](r_INITCAP.md "r_INITCAP.md")
- [LEFT and RIGHT functions](r_LEFT.md "r_LEFT.md")
- [LEN function](r_LEN.md "r_LEN.md")
- [LENGTH function](r_LENGTH.md "r_LENGTH.md")
- [LOWER function](r_LOWER.md "r_LOWER.md")
- [LPAD and RPAD functions](r_LPAD.md "r_LPAD.md")
- [LTRIM function](r_LTRIM.md "r_LTRIM.md")
- [OCTETINDEX function](OCTETINDEX.md "OCTETINDEX.md")
- [OCTET_LENGTH function](r_OCTET_LENGTH.md "r_OCTET_LENGTH.md")
- [POSITION function](r_POSITION.md "r_POSITION.md")
- [QUOTE_IDENT function](r_QUOTE_IDENT.md "r_QUOTE_IDENT.md")
- [QUOTE_LITERAL function](r_QUOTE_LITERAL.md "r_QUOTE_LITERAL.md")
- [REGEXP_COUNT function](REGEXP_COUNT.md "REGEXP_COUNT.md")
- [REGEXP_INSTR function](REGEXP_INSTR.md "REGEXP_INSTR.md")
- [REGEXP_REPLACE function](REGEXP_REPLACE.md "REGEXP_REPLACE.md")
- [REGEXP_SUBSTR function](REGEXP_SUBSTR.md "REGEXP_SUBSTR.md")
- [REPEAT function](r_REPEAT.md "r_REPEAT.md")
- [REPLACE function](r_REPLACE.md "r_REPLACE.md")
- [REPLICATE function](r_REPLICATE.md "r_REPLICATE.md")
- [REVERSE function](r_REVERSE.md "r_REVERSE.md")
- [RTRIM function](r_RTRIM.md "r_RTRIM.md")
- [SOUNDEX function](SOUNDEX.md "SOUNDEX.md")
- [SPLIT_PART function](SPLIT_PART.md "SPLIT_PART.md")
- [STRPOS function](r_STRPOS.md "r_STRPOS.md")
- [STRTOL function](r_STRTOL.md "r_STRTOL.md")
- [SUBSTRING function](r_SUBSTRING.md "r_SUBSTRING.md")
- [TEXTLEN function](r_TEXTLEN.md "r_TEXTLEN.md")
- [TRANSLATE function](r_TRANSLATE.md "r_TRANSLATE.md")
- [TRIM function](r_TRIM.md "r_TRIM.md")
- [UPPER function](r_UPPER.md "r_UPPER.md")
  String functions process and manipulate character strings or expressions that evaluate
  to character strings. When the _string_ argument in these functions is a
  literal value, it must be enclosed in single quotation marks. Supported data types include CHAR and
  VARCHAR.

The following section provides the function names, syntax, and descriptions for
supported functions. All offsets into strings are one-based.

###### Deprecated leader node-only functions

The following string functions are deprecated because they run only on the leader
node. For more information, see [Leader node–only
functions](c_SQL_functions_leader_node_only.md "c_SQL_functions_leader_node_only.md")

- GET_BYTE
- SET_BIT
- SET_BYTE
- TO_ASCII
