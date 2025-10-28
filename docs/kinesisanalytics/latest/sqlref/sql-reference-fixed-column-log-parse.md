# FIXED_COLUMN_LOG_PARSE

Parses fixed-width fields and automatically converts them to the given SQL types.

```
FIXED_COLUMN_LOG_PARSE ( <string value expression>, <column description string expression> )
 <column description string expression> := '<column description> [,...]'
 <column description> :=
   <identifier> TYPE <data type> [ NOT NULL ]
   START <numeric value expression> [FOR <numeric constant expression>]
```

Starting position of column is 0. Column specifications for types DATE,TIME and TIMESTAMP
support a format parameter allowing the user to specify exact time component layout. The
parser uses the Java class [java.lang.SimpleDateFormat](http://docs.oracle.com/javase/1.5.0/docs/api/java/text/SimpleDateFormat.html "http://docs.oracle.com/javase/1.5.0/docs/api/java/text/SimpleDateFormat.html") to parse the strings for types DATE, TIME and
TIMESTAMP. The [Date and Time Patterns](sql-reference-parse-timestamp-format.md "sql-reference-parse-timestamp-format.md") topic gives a full description and
examples of timestamp format strings. The following is an example of a column definition
with a format string:

```
"name" TYPE TIMESTAMP 'dd/MMM/yyyy:HH:mm:ss'
```

###### Related Topics

[REGEX_LOG_PARSE](sql-reference-regex-log-parse.md "sql-reference-regex-log-parse.md")
