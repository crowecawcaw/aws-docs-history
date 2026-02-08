# JSON and XML for T-SQL

This topic provides reference information about XML and JSON support in SQL Server and PostgreSQL, which is relevant for migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. You can understand the similarities and differences in how these database systems handle semi-structured data formats. The topic explores the native support for XML and JSON in both SQL Server and PostgreSQL, including data types, functions, and indexing capabilities.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                    | Key differences                                                                                   |
| ------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Four star feature compatibility | Three star automation level        | [XML](chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.xml "chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.xml") | Syntax and option differences, similar functionality. PostgreSQL doesn’t have a `FOR XML` clause. |

## SQL Server Usage

JavaScript Object Notation (JSON) and eXtensible Markup Language (XML) are the two most common types of semi-structured data documents used by a variety of data interfaces and NoSQL databases. Most REST web service APIs support JSON as their native data transfer format. XML is an older, more mature framework that is still widely used. It provides many extensions such as XQuery, name spaces, schemas, and more.

The following example is a JSON document:

```
[{
  "name": "Robert",
  "age": "28"
}, {
  "name": "James",
  "age": "71"
  "lastname": "Drapers"
}]
```

The following example is the XML counterpart of the preceding example.

```
<?xml version="1.0" encoding="UTF-16" ?>
<root>
  <Person>
    <name>Robert</name>
    <age>28</age>
  </Person>
  <Person>
    <name>James</name>
    <age>71</age>
    <lastname>Drapers</lastname>
  </Person>
</root>
```

SQL Server provides native support for both JSON and XML in the database using the familiar and convenient T-SQL interface.

### XML Data

SQL Server provides extensive native support for working with XML data including XML Data Types, XML Columns, XML Indexes, and XQuery.

#### XML Data Types and Columns

In SQL Server, you can use the following data types to store XML data:

- The Native XML Data Type uses a BLOB structure but preserves the XML Infoset, which consists of the containment hierarchy, document order, and element/attribute values. An XML typed document may differ from the original text; white space is removed and the order of objects may change. XML Data stored as a native XML data type has the additional benefit of schema validation.
- You can use an Annotated Schema (AXSD) to distribute XML documents to one or more tables. Hierarchical structure is maintained, but element order isn’t.
- You can use CLOB or BLOB such as `VARCHAR(MAX)` and `VARBINARY(MAX)` to store the original XML document.

#### XML Indexes

In SQL Server, you can create `PRIMARY` and `SECONDARY` XML indexes on columns with a native XML data type. You can create secondary indexes for `PATH`, `VALUE`, or `PROPERTY`, which are helpful for various types of workload queries.

#### XQuery

SQL Server supports a subset of the W3C XQUERY language specification. You can run queries directly against XML data and use them as expressions or sets in standard T-SQL statements.

The following example uses the XQuery language specification.

```
DECLARE @XMLVar XML = '<Root><Data>My XML Data</Data></Root>';
SELECT @XMLVar.query('/Root/Data');
```

```
Result: <Data>My XML Data</Data>
```

### JSON Data

SQL Server doesn’t support a dedicated JSON data type. However, you can store JSON documents in an `NVARCHAR` column. For more information about BLOBS, see [Data Types](chap-sql-server-aurora-pg.sql.md "chap-sql-server-aurora-pg.sql.md").

SQL Server provides a set of JSON functions. You can use these functions for the following tasks:

- Retrieve and modify values in JSON documents.
- Convert JSON objects to a set (table) format.
- Use standard T-SQL queries with converted JSON objects.
- Convert tabular results of T-SQL queries to JSON format.

The functions are:

- `ISJSON` — Tests if a string contains a valid JSON string. Use in WHERE clause to avoid errors.
- `JSON_VALUE` — Retrieves a scalar value from a JSON document.
- `JSON_QUERY` — Retrieves a whole object or array from a JSON document.
- `JSON_MODIFY` — Modifies values in a JSON document.
- `OPENJSON` — Converts a JSON document to a `SET` that you can use in the `FROM` clause of a T-SQL query.

You can use the `FOR JSON` clause of `SELECT` queries to convert a tabular set to a JSON document.

### Examples

The following example creates a table with a native typed XML column.

```
CREATE TABLE MyTable
(
  XMLIdentifier INT NOT NULL PRIMARY KEY,
  XMLDocument XML NULL
);
```

The following example queries a JSON document.

```
DECLARE @JSONVar NVARCHAR(MAX);
SET @JSONVar = '{"Data":{"Person":[{"Name":"John"},{"Name":"Jane"},
{"Name":"Maria"}]}}';
SELECT JSON_QUERY(@JSONVar, '$.Data');
```

For more information, see [JSON data in SQL Server](https://docs.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver15") and [XML Data (SQL Server)](https://docs.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

PostgreSQL provides native JSON Document support using the JSON data types `JSON` and `JSONB`.

`JSON` stores an exact copy of the input text that processing functions must re-parse on each run. It also preserves semantically-insignificant white space between tokens and the order of keys within JSON objects.

`JSONB` stores data in a decomposed binary format causing slightly slower input performance due to added conversion to binary overhead. But it is significantly faster to process, since no re-parsing is needed on reads.

- Doesn’t preserve white space.
- Doesn’t preserve the order of object keys.
- Doesn’t keep duplicate object keys. If duplicate keys are specified in the input, only the last value is retained.

Most applications store JSON data as `JSONB` unless there are specialized needs. For more information, see [JSON Types](https://www.postgresql.org/docs/13/static/datatype-json.html "https://www.postgresql.org/docs/13/static/datatype-json.html") in the _PostgreSQL documentation_.

To comply with the full JSON specification, database encoding must be set to UTF8. If the database code page isn’t set to UTF8, then non-UTF8 characters are allowed and the database encoding will be non-compliant with the full JSON specification.

In PostgreSQL version 10 and higher, JSON and JSONB are compatible with full-text search.

### Examples

**Querying JSON data in PostgreSQL uses different syntax than SQL Server**

The following example returns the JSON document stored in the emp_data column associated with emp_id=1.

```
SELECT emp_data FROM employees WHERE emp_id = 1;
```

The following example returns all JSON documents stored in the emp_data column having a key named address.

```
SELECT emp_data FROM employees WHERE emp_data ? ' address';
```

The following example returns all JSON items that have an address key or a hobbies key.

```
SELECT * FROM employees WHERE emp_data ?| array['address', 'hobbies'];
```

The following example returns all JSON items that have both an address key and a hobbies key.

```
SELECT * FROM employees WHERE emp_data ?& array['a', 'b'];
```

The following example returns the value of home key in the phone numbers array.

```
SELECT emp_data ->'phone numbers'->>'home' FROM employees;
```

The following example returns all JSON documents where the address key is equal to a specified value and return all JSON documents
where address key contains a specific string (using like).

```
SELECT * FROM employees WHERE emp_data->>'address' = '1234 First Street, Capital City';
SELECT * FROM employees WHERE emp_data->>'address' like '%Capital City%';
```

The following example removes keys from JSON. You can remove more than one key in PostgreSQL 10 only.

```
select '{"id":132, "fname":"John", "salary":999999, "bank_account":1234}'::jsonb - '{salary,bank_account}'::text[];
```

For more information, see [JSON Functions and Operators](https://www.postgresql.org/docs/10/functions-json.html "https://www.postgresql.org/docs/10/functions-json.html") in the _PostgreSQL documentation_.

**Indexing and Constraints with JSONB Columns**

You can use the CREATE UNIQUE INDEX statement to enforce constraints on values inside JSON documents.

The following example creates a unique index that forces values of the address key to be unique.

```
CREATE UNIQUE INDEX employee_address_uq ON employees( (emp_data->>'address') ) ;
```

This index allows the first SQL insert statement to work and causes the second to fail.

```
INSERT INTO employees VALUES
(2, 'Second Employee','{ "address": "1234 Second Street, Capital City"}');
INSERT INTO employees VALUES
(3, 'Third Employee', '{ "address": "1234 Second Street, Capital City"}');
ERROR: duplicate key value violates unique constraint "employee_address_uq" SQL state:
23505 Detail: Key ((emp_data ->> 'address'::text))=(1234 Second Street, Capital City)
already exists.
```

For JSON data, PostgreSQL supports B-tree, hash, and Generalized Inverted Indexes (GIN). A GIN index is a special inverted index structure that is useful when an index must map many values to a row (such as indexing JSON documents).

When you use GIN indexes, you can efficiently and quickly query data using only the following JSON operators: `@>, ?, ?&, ?|`.

Without indexes, PostgreSQL is forced to perform a full table scan when filtering data. This condition applies to JSON data and will most likely have a negative impact on performance since Postgres has to step into each JSON document.

The following example creates an index on the address key of emp_data.

```
CREATE idx1_employees ON employees ((emp_data->>'address'));
```

The following example creates a GIN index on a specific key or the entire emp_data column.

```
CREATE INDEX idx2_employees ON cards USING gin ((emp_data->'tags'));
CREATE INDEX idx3_employees ON employees USING gin (emp_data);
```

### XML Examples

PostgreSQL provides an XML data type for table columns. The primary advantage of using XML columns, rather than placing XML data in text columns, is that the XML data is type checked when inserted. Additionally, there are support functions to perform type-safe operations.

XML can store well-formed documents as defined by the XML standard or content fragments that defined by the production XMLDecl. Content fragments can have more than one top-level element or character node.

You can use `IS DOCUMENT` to evaluate whether a particular XML value is a full document or only a content fragment.

The following example demonstrates how to create XML data and insert it into a table.

Insert a document, and then insert a content fragment. You can insert both types of XML data into the same column. If the XML is incorrect (such as a missing tag), the insert fails with the relevant error. The query retrieves only document records.

```
CREATE TABLE test (a xml);

insert into test values (XMLPARSE (DOCUMENT '<?xml version="1.0"?><Series><title>Simpsons</title><chapter>...</chapter></Series>'));

insert into test values (XMLPARSE (CONTENT 'note<tag>value</tag><tag>value</tag>'));

select * from test where a IS DOCUMENT;
```

Converting XML data to rows was a feature added in PostgreSQL 10. This can be very helpful reading XML data using a table equivalent.

```
CREATE TABLE xmldata_sample AS SELECT
xml $$
<ROWS>
  <ROW id="1">
    <EMP_ID>532</EMP_ID>
    <EMP_NAME>John</EMP_NAME>
  </ROW>
  <ROW id="5">
    <EMP_ID>234</EMP_ID>
    <EMP_NAME>Carl</EMP_NAME>
    <EMP_DEP>6</EMP_DEP>
    <SALARY unit="dollars">10000</SALARY>
  </ROW>
  <ROW id="6">
    <EMP_ID>123</EMP_ID>
    <EMP_DEP>8</EMP_DEP>
    <SALARY unit="dollars">5000</SALARY>
  </ROW>
</ROWS>
$$ AS data;

SELECT xmltable.*
  FROM xmldata_sample,
    XMLTABLE('//ROWS/ROW'
      PASSING data
      COLUMNS id int PATH '@id',
        ordinality FOR ORDINALITY,
        "EMP_NAME" text,
        "EMP_ID" text PATH 'EMP_ID',
        SALARY_USD float PATH 'SALARY[@unit = "dollars"]',
        MANAGER_NAME text PATH 'MANAGER_NAME' DEFAULT 'not specified');

id  ordinality  EMP_NAME  EMP_ID  salary_usd  manager_name
1   1           John      532                 not specified
5   2           Carl      234     10000       not specified
6   3                     123     5000        not specified
```

## Summary

The following table identifies similarities, differences, and key migration considerations.

| Feature                         | SQL Server                                                                     | Aurora PostgreSQL                                                                                                                                                                                                                                                                             |
| ------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| XML and JSON native data types. | XML with schema collections.                                                   | JSON.                                                                                                                                                                                                                                                                                         |
| JSON functions.                 | `IS_JSON`, `JSON_VALUE`, `JSON_QUERY`, `JSON_MODFIY`, `OPEN_JSON`, `FOR JSON`. | A set of more than 20 dedicated JSON functions. For more information, see [JSON Functions and Operators](https://www.postgresql.org/docs/13/functions-json.html "https://www.postgresql.org/docs/13/functions-json.html") in the _PostgreSQL documentation_.                                  |
| XML functions                   | `XQUERY` and `XPATH`, `OPEN_XML`, `FOR XML`.                                   | Many XML functions. For more information, see [XML Functions](https://www.postgresql.org/docs/13/functions-xml.html "https://www.postgresql.org/docs/13/functions-xml.html") in the _PostgreSQL documentation_. PostgreSQL doesn’t have a `FOR XML` clause. You can use `string_agg` instead. |
| XML and JSON indexes.           | Primary and Secondary `PATH`, `VALUE` and `PROPERTY` indexes.                  | Supported.                                                                                                                                                                                                                                                                                    |

For more information, see [XML Type](https://www.postgresql.org/docs/13/datatype-xml.html "https://www.postgresql.org/docs/13/datatype-xml.html"), [XML Functions](https://www.postgresql.org/docs/13/functions-xml.html "https://www.postgresql.org/docs/13/functions-xml.html"), [JSON Types](https://www.postgresql.org/docs/13/datatype-json.html "https://www.postgresql.org/docs/13/datatype-json.html"), and [JSON Functions and Operators](https://www.postgresql.org/docs/13/functions-json.html "https://www.postgresql.org/docs/13/functions-json.html") in the _PostgreSQL documentation_.
