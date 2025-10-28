# SYS_LOG_PARSE

Parses the standard syslog format:

```
 Mon DD HH:MM:SS server message
```

SYS_LOG_PARSE processes entries commonly found in UNIX/Linux system logs. System log entries
start with a timestamp and are followed with a free form text field. SYS_LOG_PARSE output
consists of two columns. The first column is named "COLUMN1" and is SQL data type TIMESTAMP. The
second column is named "COLUMN2" and is SQL type VARCHAR().

###### Note

For more information about SYSLOG, see [IETF RFC3164](https://tools.ietf.org/html/rfc3164 "https://tools.ietf.org/html/rfc3164"). For more information about date-time patterns and matching, see [Date and Time Patterns](sql-reference-parse-timestamp-format.md "sql-reference-parse-timestamp-format.md").
