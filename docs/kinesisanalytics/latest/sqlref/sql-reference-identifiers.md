# Identifiers

All identifiers may be up to 128 characters. Identifiers may be quoted (with
case-sensitivity) by enclosing them in double-quote marks ("), or unquoted (with implicit
uppercasing before both storage and lookup).

Unquoted identifiers must start with a letter or underscore, and be followed by letters,
digits or underscores; letters are all converted to upper case.

Quoted identifiers can contain other punctuation too (in fact, any Unicode character except
control characters: codes 0x0000 through 0x001F). You can include a double-quote in an
identifier by escaping it with another double-quote.

In the following example, a stream is created with an unquoted identifier, which is
converted to upper case before the stream definition is stored in the catalog. It can be
referenced using its upper-case name, or by an unquoted identifier which is implicitly converted
to upper case.

```
–- Create a stream. Stream name specified without quotes,
–- which defaults to uppercase.
CREATE OR REPLACE STREAM ExampleStream (col1 VARCHAR(4));

– example 1: OK, stream name interpreted as uppercase.
CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO ExampleStream
    SELECT * FROM SOURCE_SQL_STREAM_001;

– example 2: OK, stream name interpreted as uppercase.
CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO examplestream
    SELECT * FROM   customerdata;

– example 3: Ok.
CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO EXAMPLESTREAM
    SELECT * FROM   customerdata;

– example 2: Not found. Quoted names are case-sensitive.
CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "examplestream"
    SELECT * FROM   customerdata;
```

When objects are created in Amazon Kinesis Data Analytics, their names are implicitly quoted, so it is easy to
create identifiers that contain lowercase characters, spaces, dashes, or other punctuation. If
you reference those objects in SQL statements, you will need to quote their names.

###### Reserved Words and Keywords

Certain identifiers, called keywords, have special meaning if they occur in a particular
place in a streaming SQL statement. A subset of these key words are called reserved words and
may not be used as the name of an object, unless they are quoted. For more information, see
[Reserved Words and Keywords](sql-reference-reserved-words-keywords.md "sql-reference-reserved-words-keywords.md").
