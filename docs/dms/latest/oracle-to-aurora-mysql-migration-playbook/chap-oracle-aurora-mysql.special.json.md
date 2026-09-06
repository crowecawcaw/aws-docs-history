

# Oracle JSON document support and MySQL JSON
<a name="chap-oracle-aurora-mysql.special.json"></a>

With AWS DMS, you can migrate data between different database platforms, including Oracle and MySQL, while preserving the JSON document structure. Oracle JSON document support and MySQL JSON provide a way to store and query JSON data within the database.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-3.png)  | N/A | Different paradigm and syntax will require application or drivers rewrite. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.special.json.oracle"></a>

JSON documents are based on JavaScript syntax and allow the serialization of objects. Oracle support for JSON document storage and retrieval enables you to extend the database capabilities beyond purely relational use cases and allows an Oracle database to support semi-structured data. Oracle JSON support also includes full-text search and several other functions dedicated to querying JSON documents.

Oracle 19 adds a new `JSON_SERIALIZE` function. You can use this function to serialize JSON objects to text.

For more information, see [Introduction to JSON Data and Oracle Database](https://docs.oracle.com/en/database/oracle/oracle-database/19/adjsn/intro-to-json-data-and-oracle-database.html#GUID-17642E43-7D87-4590-8870-06E9FDE9A6E9) in the *Oracle documentation*.

### Examples
<a name="chap-oracle-aurora-mysql.special.json.oracle.examples"></a>

The following example creates a table to store a JSON document in a data column and insert a JSON document into the table.

```
CREATE TABLE json_docs (id RAW(16) NOT NULL, data CLOB,
CONSTRAINT json_docs_pk PRIMARY KEY (id),
CONSTRAINT json_docs_json_chk CHECK (data IS JSON));

INSERT INTO json_docs (id, data) VALUES (SYS_GUID(),
'{
  "FName" : "John",
  "LName" : "Doe",
  "Address" : {
    "Street" : "101 Street",
    "City" : "City Name",
    "Country" : "US",
    "Pcode" : "90210"}
}');
```

Unlike XML data, which is stored using the `XMLType` SQL data type, JSON data is stored in an Oracle Database using the SQL data types `VARCHAR2`, `CLOB`, and `BLOB`. Oracle recommends that you always use an `is_json` check constraint to ensure the column values are valid JSON instances. Or, add a constraint at the table-level `CONSTRAINT json_docs_json_chk CHECK (data IS JSON)`.

You can query a JSON document directly from a SQL query without the use of special functions. Querying without functions is called Dot Notation.

```
SELECT a.data.FName,a.data.LName,a.data.Address.Pcode AS Postcode
FROM json_docs a;

FNAME  LNAME  POSTCODE
John   Doe    90210

1 row selected.
```

In addition, Oracle provides multiple SQL functions that integrate with the SQL language and enable querying JSON documents (such as `IS JSON`, `JSON_VAUE`, `JSON_EXISTS`, `JSON_QUERY`, and `JSON_TABLE`).

For more information, see [Introduction to JSON Data and Oracle Database](https://docs.oracle.com/en/database/oracle/oracle-database/19/adjsn/intro-to-json-data-and-oracle-database.html#GUID-17642E43-7D87-4590-8870-06E9FDE9A6E9) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.special.json.mysql"></a>

Aurora MySQL 5.7 supports a native JSON data type for storing JSON documents, which provides several benefits over storing the same document as a generic string. All JSON documents stored as a JSON data type are validated for correctness. If the document is not valid JSON, it is rejected and an error condition is raised. In addition, more efficient storage algorithms enable optimized read access to elements within the document. The optimized internal binary representation of the document enables much faster operation on the data without requiring expensive re-parsing.

Consider the following example:

```
CREATE TABLE JSONTable (
  DocumentIdentifier INT NOT NULL PRIMARY KEY,
  JSONDocument JSON);
```

MySQL 5.7.22 also added the JSON utility function `JSON_PRETTY()` which outputs an existing JSON value in an easy-to-read format; each JSON object member or array value is printed on a separate line and a child object or array is indented two spaces with respect to its parent. This function also works with a string that can be parsed as a JSON value. For more information, see [JSON Utility Functions](https://dev.mysql.com/doc/refman/8.0/en/json-utility-functions.html) in the *MySQL documentation*.

MySQL 5.7.22 also added the JSON utility functions `JSON_STORAGE_SIZE()` and `JSON_STORAGE_FREE()`.

 `JSON_STORAGE_SIZE()` returns the storage space in bytes used for the binary representation of a JSON document prior to any partial update.

 `JSON_STORAGE_FREE()` shows the amount of space freed after it has been partially updated using `JSON_SET()` or `JSON_REPLACE()`. This is greater than zero if the binary representation of the new value is less than that of the previous value. Each of these functions also accepts a valid string representation of a JSON document. For such a value `JSON_STORAGE_SIZE()` returns the space used by its binary representation following its conversion to a JSON document. For a variable containing the string representation of a JSON document `JSON_STORAGE_FREE()` returns zero.

These functions produce an error if the non-null argument can’t be parsed as a valid JSON document and NULL if the argument is NULL. For more information, see [JSON Utility Functions](https://dev.mysql.com/doc/refman/8.0/en/json-utility-functions.html) in the *MySQL documentation*.

**Note**  
 Amazon Relational Database Service (Amazon RDS) for MySQL version 8 added two JSON aggregation functions `JSON_ARRAYAGG()` and `JSON_OBJECTAGG()`.  
 `JSON_ARRAYAGG()` takes a column or expression as its argument and aggregates the result as a single JSON array. The expression can evaluate to any MySQL data type; this does not have to be a JSON value.  
 `JSON_OBJECTAGG()` takes two columns or expressions which it interprets as a key and a value; it returns the result as a single JSON object.

**Note**  
 Amazon RDS for MySQL version 8.0.17 adds two functions `JSON_SCHEMA_VALID()` and `JSON_SCHEMA_VALIDATION_REPORT()` for validating JSON documents.  
 `JSON_SCHEMA_VALID()` returns `TRUE (1)` if the document validates against the schema and `FALSE (0)` if it doesn’t.  
 `JSON_SCHEMA_VALIDATION_REPORT()` returns a JSON document containing detailed information about the results of the validation.

### JSON functions
<a name="chap-oracle-aurora-mysql.special.json.mysql.functions"></a>

Aurora MySQL supports a rich set of more than 25 targeted functions for working with JSON data. These functions enable adding, modifying, and searching JSON data. Additionally, spatial JSON functions can be used for GeoJSON documents. For more information, see [Spatial GeoJSON Functions](https://dev.mysql.com/doc/refman/5.7/en/spatial-geojson-functions.html) in the *MySQL documentation*.

The `JSON_ARRAY`, `JSON_OBJECT`, and `JSON_QUOTE` functions all return a JSON document from a list of values, a list of key-value pairs, or a JSON value respectively.

Consider the following example:

```
SELECT JSON_OBJECT('Person', 'John', 'Country', 'USA');
{"Person": "John", "Country": "USA"}
```

The `JSON_CONTAINS`, `JSON_CONTAINS_PATH`, `JSON_EXTRACT`, `JSON_KEYS`, and `JSON_SEARCH` functions are used to query and search the content of a JSON document.

The `CONTAINS` functions are Boolean functions that return 1 or 0 (`TRUE` or `FALSE`).

 `JSON_EXTRACT` returns a subset of the document based on the XPATH expression.

 `JSON_KEYS` returns a JSON array consisting of the top-level key (or path top level) values of a JSON document.

The `JSON_SEARCH` function returns the path to one or all of the instances of the search string.

#### Examples
<a name="chap-oracle-aurora-mysql.special.json.mysql.functions.examples"></a>

```
SELECT JSON_EXTRACT('["Mary", "Paul", ["Jim", "Ryan"]]', '$[1]');

"Paul"

SELECT JSON_SEARCH('["Mary", "Paul", ["Jim", "Ryan"]]', 'one', 'Paul');

"$[1]"
```

Aurora MySQL supports the following functions for adding, deleting, and modifying JSON data: `JSON_INSERT`, `JSON_REMOVE`, `JSON_REPLACE`, and their `ARRAY` counterparts, which are used to create, delete, and replace existing data elements.

```
SELECT JSON_ARRAY_INSERT('["Mary", "Paul", "Jim"]', '$[1]', 'Jack');

["Mary", "Jack", "Paul", "Jim"]
```

 `JSON_SEARCH` is used to find the location of an element value within a JSON document.

```
SELECT JSON_SEARCH('["Mary", "Paul", ["Jim", "Ryan"]]', 'one', 'Paul');

"$[1]"
```

### JSON indexes
<a name="chap-oracle-aurora-mysql.special.json.mysql.indexes"></a>

JSON columns are effectively a BINARY family type, which cannot be indexed. As an alternative, use `CREATE TABLE` or `ALTER TABLE` to add generated columns that represent some value from the JSON document and create an index on the generated column. For more information, see [Oracle Virtual Columns and MySQL Generated Columns](chap-oracle-aurora-mysql.tables.virtual.md).

**Note**  
If indexes on generated columns exist for JSON documents, the query optimizer can use them to match JSON expressions and optimize data access.

## Summary
<a name="chap-oracle-aurora-mysql.special.json.summary"></a>


| Feature | Oracle |  Aurora MySQL | 
| --- | --- | --- | 
| JSON functions |  `IS_JSON`, `IS_NOT_JSON`, `JSON_EXISTS`, `JSON_VALUE`, `JSON_QUERY`, `JSON_TABLE`  | A set of more than 25 dedicated JSON functions. For more information, see [JSON Function Reference](https://dev.mysql.com/doc/refman/5.7/en/json-function-reference.html) in the *MySQL documentation*. | 
| Return the full JSON document or all JSON documents | The `emp_data` column stores json documents:<pre>SELECT emp_data FROM employees;</pre> | The `emp_data` column stores json documents:<pre>SELECT emp_data FROM employees;</pre> | 
| Return a specific element from a JSON document | Return only the address property:<pre>SELECT e.emp_data.address FROM employees e;</pre> | Return only the address property:<pre>SELECT emp_data->>'address' from employees<br />where emp_id = 1;</pre> | 
| Return JSON documents matching a pattern in any field | Return the JSON based on a search of on all JSON properties. Could be returned even if element is equal to the pattern.<pre>SELECT e.emp_data FROM employees e<br />WHERE e.emp_data like '%pattern%';</pre> | Return the JSON based on a search of on all JSON properties. Could be returned even if element is equal to the pattern.<pre>SELECT e.emp_data FROM employees e<br />WHERE e.emp_data like '%pattern%';</pre> | 
| Return JSON documents matching a pattern in specific fields (root level) |  <pre>SELECT e.emp_data.name FROM employees e<br />WHERE e.data.active = 'true';</pre>  |  <pre>SELECT emp_data.name FROM employees<br />WHERE emp_data->>"$.active" = 'true';</pre>  | 

For more information, see [The JSON Data Type](https://dev.mysql.com/doc/refman/5.7/en/json.html) and [JSON Functions](https://dev.mysql.com/doc/refman/5.7/en/json-functions.html) in the *MySQL documentation*.