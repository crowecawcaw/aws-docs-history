# JSON and XML for T-SQL

This topic provides reference information about XML and JSON support in Microsoft SQL Server 2019 and Amazon Aurora MySQL. It compares how these two database systems handle semi-structured data formats, highlighting their respective strengths and limitations. You can understand the differences in native data type support, available functions, and indexing capabilities for XML and JSON between SQL Server and Aurora MySQL.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                         | Key differences                                                                             |
| ------------------------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Two star feature compatibility | Four star automation level         | [XML and JSON](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.xml "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.xml") | Minimal XML support, extensive JSON support. No XQUERY support, optionally convert to JSON. |

## SQL Server Usage

Java Script Object Notation (JSON) and eXtensible Markup Language (XML) are the two most common types of semi-structured data documents used by a variety of data interfaces and NoSQL databases. Most REST web service APIs support JSON as their native data transfer format. XML is an older, more mature framework still widely used. It also provides many extensions such as XQuery, name spaces, schemas, and more.

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

Its XML counterpart is show following:

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

SQL Server provides native support for XML and JSON in the database using the familiar and convenient T-SQL interface.

### XML Data

SQL Server provides extensive native support for working with XML data including XML data types, XML columns, XML indexes, and XQuery.

### XML Data Types and Columns

XML data can be stored using the following data types:

- The native XML data type uses a BLOB structure but preserves the XML infoset, which consists of the containment hierarchy, document order, and element or attribute values. An XML typed document may differ from the original text; whitespace is removed and the order of objects may change. XML data stored as a native XML data type has the additional benefit of schema validation.
- You can use an annotated schema (AXSD) to distribute XML documents to one or more tables. Hierarchical structure is maintained, but element order is not.
- CLOB or BLOB such as `VARCHAR(MAX)` and `VARBINARY(MAX)` can be used to store the original XML document.

### XML Indexes

In SQL Server, you can create `PRIMARY` and `SECONDARY` XML indexes on columns with a native XML data type. You can create secondary indexes for `PATH`, `VALUE`, or `PROPERTY`, which are helpful for various types of workload queries.

### XQuery

SQL Server supports a sub set of the W3C XQUERY language specification. In SQL Server, you can run queries directly against XML data and use them as expressions or sets in standard T-SQL statements. Consider the following example:

```
DECLARE @XMLVar XML = '<Root><Data>My XML Data</Data></Root>';
SELECT @XMLVar.query('/Root/Data');
```

For the preceding example, the result looks as shown following.

```
Result: <Data>My XML Data</Data>
```

### JSON Data

SQL Server doesn’t support a dedicated JSON data type. However, you can store JSON documents in an `NVARCHAR` column. For more information, see [Data Types](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md").

SQL Server provides a set of JSON functions that can be used for the following tasks:

- Retrieve and modify values in JSON documents.
- Convert JSON objects to a set (table) format.
- Use standard T-SQL queries with converted JSON objects.
- Convert tabular results of T-SQL queries to JSON format.

The functions are:

- `ISJSON` tests whether a string contains a valid JSON string. Use in the `WHERE` clause to avoid errors.
- `JSON_VALUE` retrieves a scalar value from a JSON document.
- `JSON_QUERY` retrieves a whole object or array from a JSON document.
- `JSON_MODIFY` modifies values in a JSON document.
- `OPENJSON` converts a JSON document to a `SET` that can be used in the `FROM` clause of a T-SQL query.

The `FOR JSON` clause of `SELECT` queries can be used to convert a tabular set to a JSON document.

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

For more information, see [JSON data in SQL Server](https://docs.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver15") and [XML Data](https://docs.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) support for unstructured data is the opposite of SQL Server.

There is minimal support for XML, but a native JSON data type and more than 25 dedicated JSON functions.

MySQL 5.7.22 also added the JSON utility function `JSON_PRETTY()` which outputs an existing JSON value in an easy-to-read format; each JSON object member or array value is printed on a separate line and a child object or array is indented 2 spaces with respect to its parent. This function also works with a string that can be parsed as a JSON value. For more information, see [JSON Utility Functions](https://dev.mysql.com/doc/refman/8.0/en/json-utility-functions.html "https://dev.mysql.com/doc/refman/8.0/en/json-utility-functions.html") in the _MySQL documentation_.

MySQL 5.7.22 also added the JSON utility functions `JSON_STORAGE_SIZE()` and `JSON_STORAGE_FREE()`. `JSON_STORAGE_SIZE()` returns the storage space in bytes used for the binary representation of a JSON document prior to any partial update.

`JSON_STORAGE_FREE()` shows the amount of space freed after it has been partially updated using `JSON_SET()` or `JSON_REPLACE();` this is greater than zero if the binary representation of the new value is less than that of the previous value. Each of these functions also accepts a valid string representation of a JSON document.

For such a value `JSON_STORAGE_SIZE()` returns the space used by its binary representation following its conversion to a JSON document. For a variable containing the string representation of a JSON document `JSON_STORAGE_FREE()` returns zero. Either function produces an error if its (non-null) argument can’t be parsed as a valid JSON document and NULL if the argument is NULL. For more information, see [JSON Utility Functions](https://dev.mysql.com/doc/refman/8.0/en/json-utility-functions.html "https://dev.mysql.com/doc/refman/8.0/en/json-utility-functions.html") in the _MySQL documentation_.

###### Note

Amazon Relational Database Service (Amazon RDS) for MySQL 8 added two JSON aggregation functions `JSON_ARRAYAGG()` and `JSON_OBJECTAGG()`. `JSON_ARRAYAGG()` takes a column or expression as its argument and aggregates the result as a single JSON array. The expression can evaluate to any MySQL data type; this doesn’t have to be a JSON value. `JSON_OBJECTAGG()` takes two columns or expressions which it interprets as a key and a value; it returns the result as a single JSON object. For more information, see [Aggregate Functions](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions-and-modifiers.html "https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions-and-modifiers.html") in the _MySQL documentation_.

###### Note

Amazon RDS for MySQL 8.0.17 adds two functions `JSON_SCHEMA_VALID()` and `JSON_SCHEMA_VALIDATION_REPORT()` for validating JSON documents. `JSON_SCHEMA_VALID()` returns `TRUE` or `1` if the document validates against the schema and `FALSE` or `0` if it doesn’t. `JSON_SCHEMA_VALIDATION_REPORT()` returns a JSON document containing detailed information about the results of the validation.

### XML Support

Aurora MySQL supports two XML functions: `ExtractValue` and `UpdateXML`.

`ExtractValue` accepts an XML document, or fragment, and an `XPATH` expression. The function returns the character data of the child or element matched by the `XPATH` expression. If there is more than one match, the function returns the content of child nodes as a space delimited character string. `ExtractValue` returns only `CDATA`. It doesn’t return tags sub-tags contained within a matching tag or its content.

Consider the following example.

```
SELECT ExtractValue('<Root><Person>John</Person><Person>Jim</Person></Root>', '/Root/Person');
```

```
Results: John Jim
```

You can use `UpdateXML` to replace an XML fragment with another fragment using `XPATH` expressions similar to `ExtractValue`. If a match is found, it returns the new, updated XML. If there are no matches, or multiple matches, the original XML is returned.

Consider the following example.

```
SELECT UpdateXML('<Root><Person>John</Person><Person>Jim</Person></Root>', '/Root', '<Person>Jack</Person>')
```

```
Results: <Person>Jack</Person>
```

###### Note

Aurora MySQL doesn’t support MySQL `LOAD XML` syntax. For more information, see [Loading data into an Amazon Aurora MySQL DB cluster from text files in an Amazon S3 bucket](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md") in the _User Guide for Aurora_.

### JSON Data Type

Aurora MySQL 5.7 supports a native JSON data type for storing JSON documents, which provides several benefits over storing the same document as a generic string. The first major benefit is that all JSON documents stored as a JSON data type are validated for correctness. If the document isn’t valid JSON, it is rejected and an error condition is raised.

In addition, more efficient storage algorithms enable optimized read access to elements within the document. The optimized internal binary representation of the document enables much faster operation on the data without requiring expensive re-parsing.

Consider the following example.

```
CREATE TABLE JSONTable (DocumentIdentifier INT NOT NULL PRIMARY KEY, JSONDocument JSON);
```

### JSON Functions

Aurora MySQL supports a rich set of more than 25 targeted functions for working with JSON data. These functions enable adding, modifying, and searching JSON data. Additionally, you can use spatial JSON functions for GeoJSON documents. For more information, see [Spatial GeoJSON Functions](https://dev.mysql.com/doc/refman/5.7/en/spatial-geojson-functions.html "https://dev.mysql.com/doc/refman/5.7/en/spatial-geojson-functions.html") in the _MySQL documentation_.

The `JSON_ARRAY`, `JSON_OBJECT`, and `JSON_QUOTE` functions return a JSON document from a list of values, a list of key-value pairs, or a JSON value respectively.

Consider the following example.

```
SELECT JSON_OBJECT('Person', 'John', 'Country', 'USA');
```

```
{"Person": "John", "Country": "USA"}
```

You can use The `JSON_CONTAINS`, `JSON_CONTAINS_PATH`, `JSON_EXTRACT`, `JSON_KEYS`, and `JSON_SEARCH` functions to query and search the content of a JSON document.

The `CONTAINS` functions are Boolean functions that return 1 or 0 (`TRUE` or `FALSE`). `JSON_EXTRACT` returns a subset of the document based on the XPATH expression.

`JSON_KEYS` returns a JSON array consisting of the top-level key or path top-level values of a JSON document.

The `JSON_SEARCH` function returns the path to one or all of the instances of the search string.

Consider the following example.

```
SELECT JSON_EXTRACT('["Mary", "Paul", ["Jim", "Ryan"]]', '$[1]');
```

```
"Paul"
```

```
SELECT JSON_SEARCH('["Mary", "Paul", ["Jim", "Ryan"]]', 'one', 'Paul');
```

```
"$[1]"
```

Aurora MySQL supports the following functions for adding, deleting, and modifying JSON data: `JSON_INSERT`, `JSON_REMOVE`, `JSON_REPLACE`, and their `ARRAY` counterparts, which are used to create, delete, and replace existing data elements.

Consider the following example.

```
SELECT JSON_ARRAY_INSERT('["Mary", "Paul", "Jim"]', '$[1]', 'Jack');
```

```
["Mary", "Jack", "Paul", "Jim"]
```

You can use `JSON_SEARCH` to find the location of an element value within a JSON document.

Consider the following example.

```
SELECT JSON_SEARCH('["Mary", "Paul", ["Jim", "Ryan"]]', 'one', 'Paul');
```

```
"$[1]"
```

### JSON Indexes

JSON columns are effectively a `BINARY` family type, which can’t be indexed.

To index JSON data, use `CREATE TABLE` or `ALTER TABLE` to add generated columns that represent some value from the JSON document and create an index on this generated column.

For more information, see [Indexes](chap-sql-server-aurora-mysql.md "chap-sql-server-aurora-mysql.md").

###### Note

If indexes on generated columns exist for JSON documents, the query optimizer can use them to match JSON expressions and optimize data access.

## Summary

The following table identifies similarities, differences, and key migration considerations.

| Feature                        | SQL Server                                                                    | Aurora MySQL                                                                                                                                                                                                                                                              |
| ------------------------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| XML and JSON native data types | XML with schema collections                                                   | JSON                                                                                                                                                                                                                                                                      |
| JSON functions                 | `IS_JSON`, `JSON_VALUE`, `JSON_QUERY`, `JSON_MODFIY`, `OPEN_JSON`, FOR `JSON` | A set of over 25 dedicated JSON functions. For more information, see [JSON Function Reference](https://dev.mysql.com/doc/refman/5.7/en/json-function-reference.html "https://dev.mysql.com/doc/refman/5.7/en/json-function-reference.html") in the _MySQL documentation_. |
| XML functions                  | `XQUERY` and `XPATH`, `OPEN_XML`, `FOR XML`                                   | `ExtractValue` and `UpdateXML`.                                                                                                                                                                                                                                           |
| XML and JSON indexes           | Primary and secondary `PATH`, `VALUE`, and `PROPERTY` indexes                 | Requires adding always-generated (computed and persisted) columns with JSON expressions and indexing them explicitly. The optimizer can make use of JSON expressions only.                                                                                                |

For more information, see [XML Functions](https://dev.mysql.com/doc/refman/5.7/en/xml-functions.html "https://dev.mysql.com/doc/refman/5.7/en/xml-functions.html"), [The JSON Data Type](https://dev.mysql.com/doc/refman/5.7/en/json.html "https://dev.mysql.com/doc/refman/5.7/en/json.html"), and [JSON Functions](https://dev.mysql.com/doc/refman/5.7/en/json-functions.html "https://dev.mysql.com/doc/refman/5.7/en/json-functions.html") in the _MySQL documentation_.
