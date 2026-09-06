

# Oracle JSON document support and PostgreSQL JSON support
<a name="chap-oracle-aurora-pg.special.json"></a>

With AWS DMS, you can migrate data between different database platforms, including Oracle and PostgreSQL, while preserving the JSON document structure. Oracle JSON document support and PostgreSQL JSON provide a way to store and query JSON data within the database.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-2.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-3.png)  | N/A | Different paradigm and syntax will require application or drivers rewrite. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.special.json.ora"></a>

JSON documents are based on JavaScript syntax and allow the serialization of objects. Oracle support for JSON document storage and retrieval enables you to extend the database capabilities beyond purely relational usecases and allows an Oracle database to support semi-structured data. Oracle JSON support also includes fulltext search and several other functions dedicated to querying JSON documents.

Oracle 19 adds a new function, `JSON_SERIALIZE`. You can use this function to serialize JSON objects to text.

For more information, see [Introduction to JSON Data and Oracle Database](https://docs.oracle.com/en/database/oracle/oracle-database/19/adjsn/intro-to-json-data-and-oracle-database.html#GUID-17642E43-7D87-4590-8870-06E9FDE9A6E9) in the *Oracle documentation*.

 **Examples** 

Create a table to store a JSON document in a data column and insert a JSON document into the table.

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

Unlike XML data, which is stored using the SQL data type XMLType, JSON data is stored in an Oracle Database using the SQL data types `VARCHAR2`, `CLOB`, and `BLOB`. Oracle recommends that you always use an `is_json` check constraint to ensure the column values are valid JSON instances. Or, add a constraint at the table-level `CONSTRAINT json_docs_json_chk CHECK (data IS JSON)`.

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

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.special.json.pg"></a>

PostgreSQL provides native JSON Document support using the JSON data types JSON and JSONB.

 **JSON** stores an exact copy of the input text, which processing functions must re-parse on each run. It also preserves semantically-insignificant white space between tokens and the order of keys within JSON objects.

 **JSONB** stores data in a decomposed binary format causing slightly slower input performance due to added conversion to binary overhead. But, it is significantly faster to process since no re-parsing is needed on reads.
+ Doesn’t preserve white space.
+ Doesn’t preserve the order of object keys.
+ Doesn’t keep duplicate object keys. If duplicate keys are specified in the input, only the last value is retained.

Most applications store JSON data as JSONB unless there are specialized needs.

Starting with PostgreSQL 10, both JSON and JSONB are compatible with full-text search.

For more information, see [JSON Types](https://www.postgresql.org/docs/13/datatype-json.html) in the *PostgreSQL documentation*.

To comply with the full JSON specification, database encoding must be set to UTF8. If the database code page is not set to UTF8, then non-UTF8 characters are allowed and the database encoding will be non-compliant with the full JSON specification.

 **Examples** 

Because querying JSON data in PostgreSQL uses different query syntax from Oracle, change application queries. The following examples use PostgreSQL-native JSON query syntax.

Return the JSON document stored in the emp\_data column associated with `emp_id=1`:

```
SELECT emp_data FROM employees WHERE emp_id = 1;
```

Return all JSON documents stored in the emp\_data column having a key named address.

```
SELECT emp_data FROM employees WHERE emp_data ? ' address';
```

Return all JSON items that have an address key or a hobbies key.

```
SELECT * FROM employees WHERE emp_data ?| array['address', 'hobbies'];
```

Return all JSON items that have both an address key and a hobbies key.

```
SELECT * FROM employees WHERE emp_data ?& array['a', 'b'];
```

Return the value of home key in the phone numbers array.

```
SELECT emp_data ->'phone numbers'->>'home' FROM employees;
```

Return all JSON documents where the address key is equal to a specified value and return all JSON documents where address key contains a specific string using like.

```
SELECT * FROM employees WHERE emp_data->>'address' = '1234 First Street, Capital City';

SELECT * FROM employees WHERE emp_data->>'address' like '%Capital City%';
```

Using operators with JSON values:

```
select '{"id":132, "name":"John"}'::jsonb @> '{"id":132}'::jsonb;
```

Concatenating two JSON values.

```
select '{"id":132, "fname":"John"}'::jsonb || '{"lname":"Doe"}'::jsonb;
```

Removing keys from JSON.

```
select '{"id":132, "fname":"John", "salary":999999,
  "bank_account":1234}'::jsonb - '{salary,bank_account}'::text[];
```

For more information, see [JSON Functions and Operators](https://www.postgresql.org/docs/13/functions-json.html) in the *PostgreSQL documentation*.

### Indexing and constraints with JSONB columns
<a name="chap-oracle-aurora-pg.special.json.pg.index"></a>

You can use the `CREATE UNIQUE INDEX` statement to enforce constraints on values inside JSON documents stored in PostgreSQL. For example, you can create a unique index that forces values of the address key to be unique.

```
CREATE UNIQUE INDEX employee_address_uq ON employees( (emp_data->>'address') ) ;
```

This index allows the first SQL insert statement to work and causes the second to fail.

```
INSERT INTO employees VALUES (2, 'Second Employee','{ "address": "1234 Second Street, Capital City"}');
INSERT INTO employees VALUES (3, 'Third Employee', '{ "address": "1234 Second Street, Capital City"}');
ERROR: duplicate key value violates unique constraint "employee_address_uq" SQL state:
23505 Detail: Key ((emp_data ->> 'address'::text))=(1234 Second Street, Capital City) already exists.
```

For JSON data, PostgreSQL supports B-Tree, HASH, and GIN indexes ([Generalized Inverted Index](https://www.postgresql.org/docs/current/static/gin.html)). A GIN index is a special inverted index structure that is useful when an index must map many values to a row (such as indexing JSON documents).

When using GIN indexes, you can efficiently and quickly query data using only the following JSON operators: `@>`, `?`, `?&`, `?|`.

Without indexes, PostgreSQL is forced to perform a full table scan when filtering data. This condition applies to JSON data and will most likely have a negative impact on performance since PostgreSQL has to step into each JSON document.

Create an index on the address key of emp\_data.

```
CREATE idx1_employees ON employees ((emp_data->>'address'));
```

Create a GIN index on a specific key or the entire emp\_data column.

```
CREATE INDEX idx2_employees ON cards USING gin ((emp_data->'tags'));
CREATE INDEX idx3_employees ON employees USING gin (emp_data);
```

## Summary
<a name="chap-oracle-aurora-pg.special.json.summary"></a>


| Feature | Oracle |  Aurora PostgreSQL | 
| --- | --- | --- | 
| Return the full JSON document or all JSON documents | The `emp_data` column stores json documents:<pre>SELECT emp_data FROM employees;</pre> | The `emp_data` column stores json documents:<pre>SELECT emp_data FROM employees;</pre> | 
| Return a specific element from a JSON document | Return only the address property:<pre>SELECT e.emp_data.address FROM employees e;</pre> | Return only the address property, for `emp_id=1` from the `emp_data` JSON column in the employees table:<pre>SELECT emp_data->>'address' from employees<br />where emp_id = 1;</pre> | 
| Return JSON documents matching a pattern in any field | Return the JSON based on a search of on all JSON properties. Could be returned even if element is equal to the pattern.<pre>SELECT e.emp_data FROM employees e<br />WHERE e.emp_data like '%pattern%';</pre> | Either use `jsonb_pretty` to flatten the JSON and search or, preferably, convert it to text and make the `like` search on value:<pre>SELECT * from (select jsonb_pretty(emp_data)<br />as raw_data from employees) raw_jason where<br />raw_data like '%1234%';</pre><pre>SELECT key, value FROM card, lateral jsonb_<br />each_text(data) WHERE value LIKE '%pattern%';</pre> | 
| Return JSON documents matching a pattern in specific fields (root level) |  <pre>SELECT e.emp_data.name FROM employees e<br />WHERE e.data.active = 'true';</pre>  | Only return results where the “finished” property in the JSON document is true:<pre>SELECT * FROM employees WHERE emp_<br />data->>'active' = 'true';</pre> | 
| Define a column in a table that supports JSONB documents | Create a table with a CLOB column. Define an `IS JSON` constraint on the column.<pre>CREATE TABLE json_docs (id RAW(16) NOT NULL,<br />data CLOB, CONSTRAINT json_docs_pk PRIMARY KEY (id),<br />CONSTRAINT json_docs_json_chk CHECK (data IS JSON));</pre> | Create a table with a column defined as JSON:<pre>CREATE TABLE json_docs ( id integer NOT<br />NULL, data jsonb );</pre> | 

For more information, see [JSON Types](https://www.postgresql.org/docs/13/datatype-json.html) and [JSON Functions and Operators](https://www.postgresql.org/docs/13/functions-json.html) in the *PostgreSQL documentation*.