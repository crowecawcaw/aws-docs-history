# Oracle XML DB and MySQL XML

With AWS DMS, you can migrate data between different database engines, including Oracle XML DB and MySQL XML. Oracle XML DB is a feature that provides XML support for storing, processing, and managing XML data in an Oracle database. MySQL XML extends the MySQL server by providing an XML data type for storing XML documents, in addition to functions for extracting and searching XML data.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                | Key differences                                                            |
| -------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Three star feature compatibility | Three star automation level        | [XML](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.xml "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.xml") | Different paradigm and syntax will require application or drivers rewrite. |

## Oracle usage

Oracle XML DB is a set of Oracle Database technologies providing XML capabilities for database administrators and developers. It provides native XML support and other features including the native `XMLType` and `XMLIndex`.

`XMLType` represents an XML document in the database that is accessible from SQL. It supports standards such as XML Schema, XPath, XQuery, XSLT, and DOM.

`XMLIndex` supports all forms of XML data from highly structured to completely unstructured.

XML data can be schema-based or non-schema-based. Schema-based XML adheres to an XSD Schema Definition and must be validated. Non-schema-based XML data doesn’t require validation.

According to the Oracle documentation, the aspects you should consider when using XML are:

- The ways that you intend to store your XML data.
- The structure of your XML data.
- The languages used to implement your application.
- The ways you intend to process your XML data.

The most common features are:

- **Storage model** — Binary XML.
- **Indexing** — XML search index, `XMLIndex` with structured component.
- **Database language** — SQL, with SQL/XML functions.
- **XML languages** — XQuery and XSLT.

### Storage model — Binary XML

Also called post-parse persistence, it is the default storage model for Oracle XML DB. It is a post-parse, binary format designed specifically for XML data. Binary XML is XML schema-aware and the storage is very flexible.

You can use it for XML schema-based documents or for documents that are not based on an XML schema. You can use it with an XML schema that allows for high data variability or that evolves considerably or unexpectedly.

This storage model also provides efficient partial updating and streaming query evaluation.

The other storage option is object-relational storage and is more efficient when using XML as structured data with a minimum amount of changes and different queries. For more information, see [Oracle XML DB Developer’s Guide](https://docs.oracle.com/en/database/oracle/oracle-database/19/adxdb/xml-db-developers-guide.pdf "https://docs.oracle.com/en/database/oracle/oracle-database/19/adxdb/xml-db-developers-guide.pdf").

### Indexing — XML search index, XMLIndex with structured component

XML Search Index provides full-text search over XML data. Oracle recommends storing XMLType data as Binary XML and to use XQuery Full Text (XQFT).

If you are not using binary storage and your data is structured XML, you can use the Oracle text indexes, use the regular string functions such as contains, or use XPath `ora:contains`.

If you want to use predicates such as `XMLExists` in your `WHERE` clause, you must create an XML search index.

#### Examples

The following example creates a SQL directory object, which is a logical name in the database for a physical directory on the host computer. This directory contains XML files. The example inserts XML content from the `purOrder.xml` file into the orders table.

Create an XMLType table.

```
CREATE TABLE orders OF XMLType;
CREATE DIRECTORY xmldir AS path_to_folder_containing_XML_file;
INSERT INTO orders VALUES (XMLType(BFILENAME('XMLDIR',
  'purOrder.xml'),NLS_CHARSET_ID('AL32UTF8')));
```

Create a table with an `XMLType` column.

```
CREATE TABLE xwarehouses (warehouse_id NUMBER, warehouse_spec XMLTYPE);
```

Create an `XMLType` view.

```
CREATE VIEW warehouse_view AS
SELECT VALUE(p) AS warehouse_xml FROM xwarehouses p;
```

Insert data into an `XMLType` column.

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

Search in the `PATH /PurchaseOrder/LineItems/LineItem/Description` for values containing **Big** and **Street** and then return their **Title** tag (only in the select).

```
SELECT XMLQuery('for $i in /PurchaseOrder/LineItems/LineItem/Description
where $i[.contains text "Big" ftand "Street"] return <Title>{$i}</Title>'
PASSING OBJECT_VALUE RETURNING CONTENT)
FROM po_binxml
WHERE XMLExists('/PurchaseOrder/LineItems/LineItem/Description
  [. contains text "Big" ftand "Street"]'
```

`XMLIndex` with structured component is used for queries that project fixed structured islands of XML content, even if the surrounding data is relatively unstructured. A structured `XMLIndex` component organizes such islands in a relational format.

Make sure that you define the parts of XML data that you search in queries. This applies to XML schema-based and non-schema-based data.

Create an `XMLIndex` with a structured component:

1. Create the base `XMLIndex` on `po_binxml` table. `OBJECT_VALUE` is the XML data stored in the table. All definitions of XML types and Objects are from the XDB schema in the database.
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

SQL/XML publishing functions are SQL results generated from XML data. They are also called SQL/XML generation functions.

**XMLQuery** is used in `SELECT` clauses to return the result as XMLType data. See the previous example for creating an XML search index.

**XMLTable** is used in `FROM` clauses to get results using XQuery, and insert the results into a virtual table. This function can insert data into existing database table.

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

`XMLExists` is used in `WHERE` clauses to check if an XQuery expression returns a non-empty query sequence. If it does, it returns `TRUE`. Otherwise, it returns `FALSE`. In the following example, the query searches the `purchaseorder` table for `PurchaseOrders` that where the `SpecialInstructions` tag is set to `Expedite`.

```
SELECT OBJECT_VALUE FROM purchaseorder
  WHERE XMLExists('/PurchaseOrder[SpecialInstructions="Expedite"]'
  PASSING OBJECT_VALUE);
```

`XMLCast` is used in `SELECT` clauses to convert scalar values returned from XQuery to `NUMBER`, `VARCHAR2`, `CHAR`, `CLOB`, `BLOB`, `REF`, or `XMLType`. For example, after finding the objects that have `SpecialInstructions` set to `Expedite`, `XMLCast` returns the Reference in each item as `VARCHAR2(100)`.

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

For `XMLQuery`, see the example preceding.

In the following example, after finding the relevant item with `XMLExists` in the set clause, the command sets the `OBJECT_VALUE` to a new `NEW-DAUSTIN-20021009123335811PDT.xml` file located in the `XMLDIR` directory.

```
UPDATE purchaseorder po
SET po.OBJECT_VALUE = XMLType(bfilename('XMLDIR','NEW-DAUSTIN-20021009123335811PDT.xml'),
  nls_charset_id('AL32UTF8'))
WHERE XMLExists('$p/PurchaseOrder[Reference="DAUSTIN-20021009123335811PDT"]'
  PASSING po.OBJECT_VALUE AS "p");
```

For more information, see [XMLQUERY](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLQUERY.html#GUID-9E8D3220-2CF5-4C63-BDC2-0526D57B9CDB "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLQUERY.html#GUID-9E8D3220-2CF5-4C63-BDC2-0526D57B9CDB") in the _Oracle documentation_.

### SQL and PL/SQL

Conversion of SQL and PL/SQL is covered in the [SQL and PL/SQL](chap-oracle-aurora-mysql.md "chap-oracle-aurora-mysql.md") topic.

## MySQL usage

Aurora MySQL support for unstructured data is the opposite of Oracle. There is minimal support for XML, but a native JSON data type and more than 25 dedicated JSON functions.

### XML support

Aurora MySQL supports two XML functions: `ExtractValue` and `UpdateXML`.

`ExtractValue` accepts an XML document, or fragment, and an XPATH expression. The function returns the character data of the child or element matched by the `XPATH` expression. If there is more than one match, the function returns the content of child nodes as a space delimited character string. `ExtractValue` returns only `CDATA` and doesn’t return tags and sub-tags contained within a matching tag or its content.

Consider the following example.

```
SELECT ExtractValue('<Root><Person>John</Person>
<Person>Jim</Person></Root>','/Root/Person');
```

For the preceding example, the result looks as shown following.

```
John Jim
```

You can use `UpdateXML` to replace an XML fragment with another fragment using `XPATH` expressions similar to `ExtractValue`. If a match is found, it returns the new, updated XML. If there are no matches, or multiple matches, the original XML is returned.

Consider the following example.

```
SELECT UpdateXML('<Root><Person>John</Person>
<Person>Jim</Person></Root>', '/Root','<Person>Jack</Person>')
```

For the preceding example, the result looks as shown following.

```
<Person>Jack</Person>
```

###### Note

Aurora MySQL doesn’t support MySQL `LOAD XML` syntax. For more information, see [Loading data into an Aurora MySQL DB cluster from text files in an Amazon S3 bucket](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md") in the _User Guide for Aurora_.

## Summary

| Description                                                                        | Oracle                                                                                                                                                                                                                                                                                                                                                             | Aurora MySQL                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| XML functions                                                                      | `XMLQuery`, `XPath`, `XMLTable`, `XMLExists`, and `XMLCast`                                                                                                                                                                                                                                                                                                        | `ExtractValue` and `UpdateXML`                                                                                                                                                                                                                                                                                                                   |
| Create a table with XML                                                            | `CREATE TABLE test OF XMLType;` or `CREATE TABLE test (doc XMLType);`                                                                                                                                                                                                                                                                                              | Not supported                                                                                                                                                                                                                                                                                                                                    |
| Insert data into xml column                                                        | `<br>INSERT INTO test<br>VALUES ('<?xml version="1.0"?><br><PO pono="1"> <PNAME>Po_1</PNAME><br><CUSTNAME>John</CUSTNAME><br><SHIPADDR><br><STREET>1033, Main Street</STREET><br><CITY>Sunnyvale</CITY><br><STATE>CA</STATE><br></SHIPADDR> </PO>')<br>`                                                                                                           | XML data can be loaded into regular tables from S3. For more information, see [Loading data into an Aurora MySQL DB cluster from text files in an Amazon S3 bucket](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md") in the _User Guide for Aurora_. |
| Create Index                                                                       | `<br>CREATE INDEX test_idx ON test (OBJECT_VALUE)<br>INDEXTYPE IS XDB.XMLIndex<br>PARAMETERS ('PATH TABLE path_tab');<br>BEGIN<br>DBMS_XMLINDEX.registerParameter(<br>'myparam', 'ADD_GROUP GROUP a_item<br>XMLTable test_idx_tab ''/Path'' COLUMNS tag<br>VARCHAR2(30) PATH ''tag''');<br>END;<br>/<br>ALTER INDEX test_idx PARAMETERS<br>('PARAM myparam');<br>` | Requires adding always generated computed and persisted columns with JSON expressions and indexing them explicitly. The optimizer can make use of JSON expressions only.                                                                                                                                                                         |
| Create a full-text index                                                           | After preference and section created in Oracle Text<br>`<br>CREATE INDEX test_idx ON test (OBJECT_VALUE)<br>INDEXTYPE IS CTXSYS.CONTEXT<br>PARAMETERS('storage pref section group secgroup');<br>`                                                                                                                                                                 | N/A                                                                                                                                                                                                                                                                                                                                              |
| Query using XQuery                                                                 | `<br>SELECT XMLQuery('for $i in<br>/PurchaseOrder/LineItems/LineItem/Description<br>where $i[. contains text "Big"]<br>return <Title>{$i}</Title>'<br>PASSING OBJECT_VALUE RETURNING CONTENT)<br>FROM xml_tbl;<br>`                                                                                                                                                | N/A                                                                                                                                                                                                                                                                                                                                              |
| Query using XPath                                                                  | `<br>select sys.XMLType.extract<br>(doc,'/student/firstname/text()') firstname<br>from test;<br>`                                                                                                                                                                                                                                                                  | Because there is no XML data type, doc uses `VARCHAR` to store the XML content<br>[source]<br>----<br>select ExtractValue<br>(doc,'//student//firstname')<br>firstname from test;<br>----                                                                                                                                                        |
| Function to check if tag exists and function to cast and return a string data type | `<br>SELECT XMLCast(XMLQuery<br>('/PurchaseOrder/Reference'<br>PASSING OBJECT_VALUE<br>RETURNING CONTENT) AS VARCHAR2(100))<br>"REFERENCE"<br>FROM purchaseorder<br>WHERE XMLExists('/PurchaseOrder[SpecialInstructions="Expedite"]'<br>PASSING OBJECT_VALUE);<br>`                                                                                                | N/A                                                                                                                                                                                                                                                                                                                                              |
| Validate schema using XSD                                                          | Supported                                                                                                                                                                                                                                                                                                                                                          | Not supported                                                                                                                                                                                                                                                                                                                                    |

For more information, see [XML Functions](https://dev.mysql.com/doc/refman/5.7/en/xml-functions.html "https://dev.mysql.com/doc/refman/5.7/en/xml-functions.html") in the _MySQL documentation_.
