# Log Parsing Functions

Amazon Kinesis Data Analytics features the following functions for log parsing:

- [FAST_REGEX_LOG_PARSER](sql-reference-fast-regex-log-parser.md "sql-reference-fast-regex-log-parser.md") works similarly to the regex
  parser, but takes several "shortcuts" to ensure faster results. For example, the
  fast regex parser stops at the first match it finds (known as "lazy" semantics.)
- [FIXED_COLUMN_LOG_PARSE](sql-reference-fixed-column-log-parse.md "sql-reference-fixed-column-log-parse.md") parses fixed-width fields and automatically
  converts them to the given SQL types.
- [REGEX_LOG_PARSE](sql-reference-regex-log-parse.md "sql-reference-regex-log-parse.md") uses the default Java regular
  expression parser. For more information about this parser, see [Pattern](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html "https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html") in the Java Platform documentation on the Oracle
  website.
- [SYS_LOG_PARSE](sql-reference-sys-log-parse.md "sql-reference-sys-log-parse.md") processes entries commonly found in UNIX/Linux system logs.
- [VARIABLE_COLUMN_LOG_PARSE](sql-reference-variable-column-log-parse.md "sql-reference-variable-column-log-parse.md") splits an input string (its first argument, <character-expression>) into fields separated by a delimiter character or delimiter string.
- [W3C_LOG_PARSE](sql-reference-w3c-log-parse.md "sql-reference-w3c-log-parse.md") processes entries in W3C-predefined-format logs.
