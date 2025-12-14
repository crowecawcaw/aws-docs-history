# Oracle XML DB and PostgreSQL XML type and functions

With AWS DMS, you can migrate data from Oracle XML DB and PostgreSQL XML type and functions to other database engines supported by AWS. Oracle XML DB provides the ability to store and manage XML data in an Oracle database, while PostgreSQL XML type and functions offer similar capabilities for working with XML data in a PostgreSQL database.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                            |
| -------------------------------- | ---------------------------------- | ------------------------- | -------------------------------------------------------------------------- |
| Three star feature compatibility | Three star automation level        | N/A                       | Different paradigm and syntax will require application or drivers rewrite. |

## Oracle usage

Oracle XML DB is a set of Oracle Database technologies providing XML capabilities for database administrators and developers. It provides native XML support and other features including the native XMLType and XMLIndex.

XMLType represents an XML document in the database that is accessible from SQL. It supports standards such as XML Schema, XPath, XQuery, XSLT, and DOM.

XMLIndex supports all forms of XML data from highly structured to completely unstructured.

XML data can be schema-based or non-schema-based. Schema-based XML adheres to an XSD Schema Definition and must be validated. Non-schema-based XML data doesn’t require validation.

According to the Oracle documentation, the aspects you should consider when using XML are:

- The ways that you intend to store your XML data.
- The structure of your XML data.
- The languages used to implement your application.
- The ways you intend to process your XML data.

The most common features are:

- Storage Model: Binary XML.
- Indexing: XML search index, XMLIndex with structured component.
- Database language: SQL, with SQL/XML functions.
- XML languages: XQuery and XSLT.

### Storage model — binary XML

Also called post-parse persistence, it is the default storage model for Oracle XML DB. It is a post-parse, binary format designed specifically for XML data. Binary XML is XML schema-aware and the storage is very flexible.

You can use it for XML schema-based documents or for documents that are not based on an XML schema. You can use it with an XML schema that allows for high data variability or that evolves considerably or unexpectedly.

This storage model also provides efficient partial updating and streaming query evaluation.

The other storage option is Object-relational storage and is more efficient when using XML as structured data with a minimum amount of changes and different queries. For more information, see [Oracle XML DB Developer’s Guide](https://docs.oracle.com/en/database/oracle/oracle-database/19/adxdb/xml-db-developers-guide.pdf "https://docs.oracle.com/en/database/oracle/oracle-database/19/adxdb/xml-db-developers-guide.pdf").

### Indexing — XML search index, XMLIndex with structured component

XML Search Index provides full-text search over XML data. Oracle recommends storing XMLType data as Binary XML and to use XQuery Full Text (XQFT).

If you are not using binary storage and your data is structured XML, you can use the Oracle text indexes, use the regular string functions such as contains, or use XPath `ora:contains`.

If you want to use predicates such as `XMLExists` in your `WHERE` clause, you must create an XML search index.

**Examples**

The following example creates a SQL directory object, which is a logical name in the database for a physical directory on the host computer. This directory contains XML files. The example inserts XML content from the `purOrder.xml` file into the orders table.

Create an XMLType table.

```
CREATE TABLE orders OF XMLType;
CREATE DIRECTORY xmldir AS path_to_folder_containing_XML_file;
INSERT INTO orders VALUES (XMLType(BFILENAME('XMLDIR',
  'purOrder.xml'),NLS_CHARSET_ID('AL32UTF8')));
```

Create table with an XMLType column.

```
CREATE TABLE xwarehouses (warehouse_id NUMBER, warehouse_spec XMLTYPE);
```

Create an XMLType view.

```
CREATE VIEW warehouse_view AS
SELECT VALUE(p) AS warehouse_xml FROM xwarehouses p;
```

Insert data into an XMLType column.

```
INSERT INTO xwarehouses
VALUES(100, '<?xml version="1.0"?>
<PO pono="1">
<PNAME>Po_1</PNAME>
<CUSTNAME>John</CUSTNAME>
<SHIPADDR>
<STREET>1033, Main Street</STREET>
<CITY>Sunnyvale</CITY>
<STATE>CA</STATE>
</SHIPADDR></PO>')
```

Create an XML search index and query it with XQuery:

1. After the user gets all the privileges needed and set the right parameter in the Oracle text schema.
2. Create Oracle text section and preference.
3. Create the XML search index (regular index associated with the objects).

```
BEGIN
CTX_DDL.create_section_group('secgroup', 'PATH_SECTION_GROUP');
CTX_DDL.set_sec_grp_attr('secgroup', 'XML_ENABLE', 'T');
CTX_DDL.create_preference('pref', 'BASIC_STORAGE');
CTX_DDL.set_attribute('pref','D_TABLE_CLAUSE', 'TABLESPACE ts_name LOB(DOC) STORE AS
SECUREFILE(TABLESPACE ts_name COMPRESS MEDIUM CACHE)');
CTX_DDL.set_attribute('pref','I_TABLE_CLAUSE','TABLESPACE ts_name LOB(TOKEN_INFO)
STORE AS SECUREFILE(TABLESPACE ts_name NOCOMPRESS CACHE)');
END;
/
CREATE INDEX po_ctx_idx ON po_binxml(OBJECT_VALUE)
INDEXTYPE IS CTXSYS.CONTEXT
PARAMETERS('storage pref section group secgroup');
```

Query using the preceding index in XQuery. XQuery is W3C standard for generating, querying and updating XML, Natural query language for XML.

Content, very like SQL in the relational world, advanced form of XPath and XSLT (as read in the begging of the topic, are for structured data and like regular Oracle text indexes).

Search in the PATH `/PurchaseOrder/LineItems/LineItem/Description` for values containing **Big** and **Street** and then return their **Title** tag (only in the select).

```
SELECT XMLQuery('for $i in /PurchaseOrder/LineItems/LineItem/Description where $i[.
contains text "Big" ftand "Street"] return <Title>{$i}</Title>'
PASSING OBJECT_VALUE RETURNING CONTENT)
FROM po_binxml
WHERE XMLExists('/PurchaseOrder/LineItems/LineItem/Description [. contains
text "Big" ftand "Street"]'
```

XMLIndex with structured component is used for queries that project fixed structured islands of XML content, even if the surrounding data is relatively unstructured. A structured XMLIndex component organizes such islands in a relational format.

You must define the parts of XML data that you search in queries (applies to both XML schema-based and non-schema-based data).

Create an XMLIndex with structured component:

1. Create the base XMLIndex on `po_binxml` table. `OBJECT_VALUE` is the XML data stored in the table. All definitions of XML types and Objects are from the XDB schema in the database.
2. Use `DBMS_XMLINDEX.register` parameter to add another structure to the index.
3. Create tables (`po_idx_tab` and `po_index_lineitem`) to store index data as structured data. Next to each table name there is the root of the PATH in the XML data (/PurchaseOrder and /LineItem). After that, each column is another PATH in this root. Note that in the `po_idx_tab` table the last column is XMLType. It takes everything under this PATH and saves it in XML datatype.
4. Add the group of structure to the index.

```
CREATE INDEX po_xmlindex_ix ON po_binxml (OBJECT_VALUE)
INDEXTYPE IS XDB.XMLIndex PARAMETERS ('PATH TABLE path_tab');
BEGIN
DBMS_XMLINDEX.registerParameter(
'myparam',
'ADD_GROUP GROUP po_item
XMLTable po_idx_tab ''/PurchaseOrder''
COLUMNS reference VARCHAR2(30) PATH ''Reference'',
requestor VARCHAR2(30) PATH ''Requestor'',
username VARCHAR2(30) PATH ''User'',
lineitem XMLType PATH ''LineItems/LineItem'' VIRTUAL
XMLTable po_index_lineitem ''/LineItem'' PASSING lineitem
COLUMNS itemno BINARY_DOUBLE PATH ''@ItemNumber'',
description VARCHAR2(256) PATH ''Description'',
partno VARCHAR2(14) PATH ''Part/@Id'',
quantity BINARY_DOUBLE PATH ''Part/@Quantity'',
unitprice BINARY_DOUBLE PATH ''Part/@UnitPrice''');
END;
/

ALTER INDEX po_xmlindex_ix PARAMETERS('PARAM myparam');
```

For more information, see [Indexes for XMLType Data](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLQUERY.html#GUID-9E8D3220-2CF5-4C63-BDC2-0526D57B9CDB "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLQUERY.html#GUID-9E8D3220-2CF5-4C63-BDC2-0526D57B9CDB") in the _Oracle documentation_.

### SQL/XML functions

Oracle Database provides two main SQL/XML groups:

- SQL/XML publishing functions.
- SQL/XML query and update functions.

#### SQL/XML publishing functions

SQL/XML publishing functions are SQL results generated from XML data (also called SQL/XML generation functions).

**XMLQuery** is used in `SELECT` clauses to return the result as XMLType data (See the previous example for creating an XML search index).

**XMLTable** is used in `FROM` clauses to get results using XQuery, and insert the results into a virtual table (can insert into existing database table).

**Example**

Use XMLTable to generate virtual table from the xml value (`OBJECT_VALUE`). Generate columns under the root (`/PurchaseOrder`).

One of the columns is XMLType and then another XMLTable call insert deeper into the XML data calling the virtual table (po) and create another virtual table. When using `@` the path is looking in the inner tag.

```
SELECT po.reference, li.*
FROM po_binaryxml p,
XMLTable('/PurchaseOrder' PASSING p.OBJECT_VALUE
COLUMNS
reference VARCHAR2(30) PATH 'Reference',
lineitem XMLType PATH 'LineItems/LineItem') po,
XMLTable('/LineItem' PASSING po.lineitem
COLUMNS
itemno NUMBER(38) PATH '@ItemNumber',
description VARCHAR2(256) PATH 'Description',
partno VARCHAR2(14) PATH 'Part/@Id',
quantity NUMBER(12, 2) PATH 'Part/@Quantity',
unitprice NUMBER(8, 4) PATH 'Part/@UnitPrice') li;
```

**XMLExists** is used in `WHERE` clauses to check if an XQuery expression returns a non-empty query sequence. If it does, it returns `TRUE`. Otherwise, it returns `FALSE`. In the following example, the query searches the `purchaseorder` table for `PurchaseOrders` that where the `SpecialInstructions` tag is set to `Expedite`.

```
SELECT OBJECT_VALUE FROM purchaseorder
  WHERE XMLExists('/PurchaseOrder[SpecialInstructions="Expedite"]'
  PASSING OBJECT_VALUE);
```

**XMLCast** is used in `SELECT` clauses to convert scalar values returned from XQuery to `NUMBER`, `VARCHAR2`, `CHAR`, `CLOB`, `BLOB`, `REF`, or `XMLType`. For example, after finding the objects that have `SpecialInstructions` set to `Expedite`, XMLCast returns the Reference in each item as `VARCHAR2(100)`.

```
SELECT XMLCast(XMLQuery('/PurchaseOrder/Reference'
  PASSING OBJECT_VALUE
  RETURNING CONTENT) AS VARCHAR2(100)) "REFERENCE"
  FROM purchaseorder
  WHERE XMLExists('/PurchaseOrder[SpecialInstructions="Expedite"]'
  PASSING OBJECT_VALUE);
```

For more information, see [XMLELEMENT](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLELEMENT.html#GUID-DEA75423-00EA-4034-A246-4A774ADC988E "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLELEMENT.html#GUID-DEA75423-00EA-4034-A246-4A774ADC988E") in the _Oracle documentation_.

#### SQL/XML query and update functions

SQL/XML query and update functions are used to query and update XML content as part of regular SQL operations.

For XMLQuery, see the example preceding.

Where in the `SET` clause there is XMLType instance, SQL functions or XML constructors that return an XML instance. In the following example, after finding the relevant item with XMLExists in the `SET` clause, the command sets the `OBJECT_VALUE` to a new file ('NEW-DAUSTIN-20021009123335811PDT.xml') located in the `XMLDIR` directory.

```
UPDATE purchaseorder po
SET po.OBJECT_VALUE = XMLType(bfilename('XMLDIR','NEW-DAUSTIN-20021009123335811PDT.xml'),
  nls_charset_id('AL32UTF8'))
WHERE XMLExists('$p/PurchaseOrder[Reference="DAUSTIN-20021009123335811PDT"]'
  PASSING po.OBJECT_VALUE AS "p");
```

For more information, see [XMLQUERY](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLQUERY.html#GUID-9E8D3220-2CF5-4C63-BDC2-0526D57B9CDB "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLQUERY.html#GUID-9E8D3220-2CF5-4C63-BDC2-0526D57B9CDB") in the _Oracle documentation_.

### SQL and PL/SQL

Conversion of SQL and PL/SQL is covered in the [SQL and PL/SQL](chap-oracle-aurora-pg.md "chap-oracle-aurora-pg.md") topic.

## PostgreSQL usage

The data type xml in PostgreSQL can be used when creating tables, the main advantage to keep the xml data in xml type column and not in regular text column is the xml type check the input to alert if we try to insert wrong data format, in additional, there are support functions to perform type-safe operations on it. XML can store well-formed “documents” as defined by XML standard or “content” fragments that are defined by the production XMLDecl, this means that content fragments can have more than one top-level element or character node.

You can use `IS DOCUMENT` to evaluate whether a particular xml value is a full document or only a content fragment.

The `xmltable()` and `xpath()` functions that may not work with non-ASCII data when the server encoding is not UTF-8.

**Examples**

Create XML data and insert it to the table.

The first insert is Document and the second is just content, the two types of the data can be inserted to the same column.

If you insert wrong XML (for example, with a missing tag), the insert will fail with relevant error.

The following query retrieves only the `DOCUMENT RECORDS`.

```
CREATE TABLE test (a xml);

insert into test values (XMLPARSE (DOCUMENT '<?xml vesion=" 1.0"?><Series><title>Simpsons</title><chapter>...</chapter></Series>'));

insert into test values (XMLPARSE (CONTENT 'note<tag>value</tag><tag>value</tag>'));

select * from test where a IS DOCUMENT;
```

Convert XML data to rows will be a new feature in PostgreSQL 10, this can be very helpful to read XML data using table equivalent.

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

| Description                                                                                | PostgreSQL                                                                                                                                                                                                                                                                          | Oracle                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Create table with XML                                                                      | `<br>CREATE TABLE test (a xml);<br>`                                                                                                                                                                                                                                                | `<br>CREATE TABLE test OF XMLType;<br>or<br>CREATE TABLE test (doc XMLType);<br>`                                                                                                                                                                                                                                                                                  |
| Insert data into xml column                                                                | `<br>INSERT INTO test<br>VALUES (XMLPARSE (DOCUMENT<br>'<?xml version="1.0"?><br><PO pono="1"><br><PNAME>Po_1</PNAME><br><CUSTNAME>John</CUSTNAME><br><SHIPADDR><br><STREET>1033, Main Street</STREET><br><CITY>Sunnyvale</CITY><br><STATE>CA</STATE><br></SHIPADDR> </PO>'));<br>` | `<br>INSERT INTO test<br>VALUES ('<?xml version="1.0"?><br><PO pono="1"> <PNAME>Po_1</PNAME><br><CUSTNAME>John</CUSTNAME><br><SHIPADDR><br><STREET>1033, Main Street</STREET><br><CITY>Sunnyvale</CITY><br><STATE>CA</STATE><br></SHIPADDR> </PO>')<br>`                                                                                                           |
| Create Index                                                                               | We index a specific path so the queries must be the same<br>`<br>CREATE INDEX test_isbn ON test<br>(((((xpath('/path/tag/text()', a))[1])::text)));<br>`                                                                                                                            | `<br>CREATE INDEX test_idx ON test (OBJECT_VALUE)<br>INDEXTYPE IS XDB.XMLIndex<br>PARAMETERS ('PATH TABLE path_tab');<br>BEGIN<br>DBMS_XMLINDEX.registerParameter(<br>'myparam', 'ADD_GROUP GROUP a_item<br>XMLTable test_idx_tab ''/Path'' COLUMNS tag<br>VARCHAR2(30) PATH ''tag''');<br>END;<br>/<br>ALTER INDEX test_idx PARAMETERS<br>('PARAM myparam');<br>` |
| Create Fulltext Index                                                                      | We index a specific path so the queries must be the same<br>`<br>CREATE INDEX my_funcidx ON<br>test USING GIN ( CAST(xpath('/PNAME/-<br>text()', a) AS TEXT[]) );<br>`                                                                                                              | After preference and section created in Oracle Text<br>`<br>CREATE INDEX test_idx ON test (OBJECT_<br>VALUE) INDEXTYPE IS CTXSYS.CONTEXT<br>PARAMETERS('storage pref section group secgroup');<br>`                                                                                                                                                                |
| Query using XQuery                                                                         | Not Supported                                                                                                                                                                                                                                                                       | `<br>SELECT XMLQuery('for $i in<br>/PurchaseOrder/LineItems/LineItem/Description<br>where $i[. contains text "Big"]<br>return <Title>{$i}</Title>'<br>PASSING OBJECT_VALUE RETURNING CONTENT)<br>FROM xml_tbl;<br>`                                                                                                                                                |
| Query using XPath                                                                          | `<br>SELECT xpath('//student/firstname/text()', a) FROM test<br>`                                                                                                                                                                                                                   | `<br>select sys.XMLType.extract<br>(doc,'/student/firstname/text()') firstname from test;<br>`                                                                                                                                                                                                                                                                     |
| Function to check if tag exists and function to cast and return another data type (string) | `<br>SELECT XMLCast(XMLQuery<br>('/PurchaseOrder/Reference'<br>PASSING OBJECT_VALUE<br>RETURNING CONTENT) AS VARCHAR2(100))<br>"REFERENCE"<br>FROM purchaseorder<br>WHERE XMLExists('/PurchaseOrder[SpecialInstructions="Expedite"]'<br>PASSING OBJECT_VALUE);<br>`                 | `<br>select cast (xpath('//book/title/text()', a) as text[])<br>as BookTitle from test where xmlexists('//book/title' PASSING by ref a);<br>`                                                                                                                                                                                                                      |
| Validate schema using XSD                                                                  | Not out-of-the-box but can create trigger before insert or delete and find tag with XPATH and try to cast the type of the value to know if it’s OK, then if something is wrong stop the insert or delete command                                                                    | Supported                                                                                                                                                                                                                                                                                                                                                          |

For more information, see [XML Type](https://www.postgresql.org/docs/13/datatype-xml.html "https://www.postgresql.org/docs/13/datatype-xml.html") and [XML Functions](https://www.postgresql.org/docs/13/functions-xml.html "https://www.postgresql.org/docs/13/functions-xml.html") in the _PostgreSQL documentation_.
