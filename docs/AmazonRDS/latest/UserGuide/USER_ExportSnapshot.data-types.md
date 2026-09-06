

# Data conversion when exporting to an Amazon S3 bucket for Amazon RDS
<a name="USER_ExportSnapshot.data-types"></a>

When you export a DB snapshot to an Amazon S3 bucket, Amazon RDS converts data to, exports data in, and stores data in the Parquet format. For more information about Parquet, see the [Apache Parquet](https://parquet.apache.org/docs/) website.

Parquet stores all data as one of the following primitive types:
+ BOOLEAN
+ INT32
+ INT64
+ INT96
+ FLOAT
+ DOUBLE
+ BYTE\_ARRAY – A variable-length byte array, also known as binary
+ FIXED\_LEN\_BYTE\_ARRAY – A fixed-length byte array used when the values have a constant size

The Parquet data types are few to reduce the complexity of reading and writing the format. Parquet provides logical types for extending primitive types. A *logical type* is implemented as an annotation with the data in a `LogicalType` metadata field. The logical type annotation explains how to interpret the primitive type. 

When the `STRING` logical type annotates a `BYTE_ARRAY` type, it indicates that the byte array should be interpreted as a UTF-8 encoded character string. After an export task completes, Amazon RDS notifies you if any string conversion occurred. The underlying data exported is always the same as the data from the source. However, due to the encoding difference in UTF-8, some characters might appear different from the source when read in tools such as Athena.

For more information, see [Parquet logical type definitions](https://github.com/apache/parquet-format/blob/master/LogicalTypes.md) in the Parquet documentation.

**Topics**
+ [MySQL and MariaDB data type mapping to Parquet](#USER_ExportSnapshot.data-types.MySQL)
+ [PostgreSQL data type mapping to Parquet](#USER_ExportSnapshot.data-types.PostgreSQL)

## MySQL and MariaDB data type mapping to Parquet
<a name="USER_ExportSnapshot.data-types.MySQL"></a>

The following table shows the mapping from MySQL and MariaDB data types to Parquet data types when data is converted and exported to Amazon S3.


<table>
<thead>
  <tr><th>Source data type</th><th>Parquet primitive type</th><th>Logical type annotation</th><th>Conversion notes</th></tr>
</thead>
<tbody>
  <tr><td colspan="4"><b>Numeric data types</b></td></tr>
  <tr><td>BIGINT</td><td>INT64</td><td></td><td> </td></tr>
  <tr><td>BIGINT UNSIGNED</td><td>FIXED_LEN_BYTE_ARRAY(9) </td><td>DECIMAL(20,0)</td><td>Parquet supports only signed types, so the mapping requires an additional byte (8 plus 1) to store the BIGINT_UNSIGNED type.</td></tr>
  <tr><td>BIT</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td rowspan="4">DECIMAL</td><td>INT32</td><td>DECIMAL(p,s)</td><td>If the source value is less than 231, it's stored as INT32. </td></tr>
  <tr><td>INT64</td><td>DECIMAL(p,s)</td><td>If the source value is 231 or greater, but less than 263, it's stored as INT64.</td></tr>
  <tr><td>FIXED_LEN_BYTE_ARRAY(N)</td><td>DECIMAL(p,s)</td><td>If the source value is 263 or greater, it's stored as FIXED_LEN_BYTE_ARRAY(N).</td></tr>
  <tr><td>BYTE_ARRAY</td><td>STRING</td><td>Parquet doesn't support Decimal precision greater than 38. The Decimal value is converted to a string in a BYTE_ARRAY type and encoded as UTF8.</td></tr>
  <tr><td>DOUBLE</td><td>DOUBLE</td><td></td><td> </td></tr>
  <tr><td>FLOAT</td><td>DOUBLE</td><td></td><td> </td></tr>
  <tr><td>INT</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>INT UNSIGNED</td><td>INT64</td><td></td><td> </td></tr>
  <tr><td>MEDIUMINT</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>MEDIUMINT UNSIGNED</td><td>INT64</td><td></td><td> </td></tr>
  <tr><td rowspan="4"> NUMERIC</td><td>INT32</td><td>DECIMAL(p,s)</td><td>If the source value is less than 231, it's stored as INT32.</td></tr>
  <tr><td>INT64</td><td>DECIMAL(p,s)</td><td>If the source value is 231 or greater, but less than 263, it's stored as INT64.</td></tr>
  <tr><td>FIXED_LEN_ARRAY(N)</td><td>DECIMAL(p,s)</td><td>If the source value is 263 or greater, it's stored as FIXED_LEN_BYTE_ARRAY(N).</td></tr>
  <tr><td>BYTE_ARRAY</td><td>STRING</td><td>Parquet doesn't support Numeric precision greater than 38. This Numeric value is converted to a string in a BYTE_ARRAY type and encoded as UTF8.</td></tr>
  <tr><td>SMALLINT</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>SMALLINT UNSIGNED</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>TINYINT</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>TINYINT UNSIGNED</td><td>INT32</td><td>INT(16, true)</td><td> </td></tr>
  <tr><td colspan="4"><b>String data types</b></td></tr>
  <tr><td>BINARY</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>BLOB</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>CHAR</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>ENUM</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>LINESTRING</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>LONGBLOB</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>LONGTEXT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>MEDIUMBLOB</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>MEDIUMTEXT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>MULTILINESTRING</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>SET</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>TEXT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>TINYBLOB</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>TINYTEXT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>VARBINARY</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>VARCHAR</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td colspan="4"><b>Date and time data types</b></td></tr>
  <tr><td>DATE</td><td>BYTE_ARRAY</td><td>STRING</td><td>A date is converted to a string in a BYTE_ARRAY type and encoded as UTF8.</td></tr>
  <tr><td>DATETIME</td><td>INT64 </td><td>TIMESTAMP_MICROS</td><td> </td></tr>
  <tr><td>TIME</td><td>BYTE_ARRAY</td><td>STRING</td><td>A TIME type is converted to a string in a BYTE_ARRAY and encoded as UTF8.</td></tr>
  <tr><td>TIMESTAMP</td><td>INT64 </td><td>TIMESTAMP_MICROS</td><td> </td></tr>
  <tr><td>YEAR</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td colspan="4"><b>Geometric data types</b></td></tr>
  <tr><td>GEOMETRY</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>GEOMETRYCOLLECTION</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>MULTIPOINT</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>MULTIPOLYGON</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>POINT</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>POLYGON</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td colspan="4"><b>JSON data type</b></td></tr>
  <tr><td>JSON </td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
</tbody>
</table>


## PostgreSQL data type mapping to Parquet
<a name="USER_ExportSnapshot.data-types.PostgreSQL"></a>

The following table shows the mapping from PostgreSQL data types to Parquet data types when data is converted and exported to Amazon S3.


<table>
<thead>
  <tr><th>PostgreSQL data type</th><th>Parquet primitive type</th><th>Logical type annotation</th><th>Mapping notes</th></tr>
</thead>
<tbody>
  <tr><td colspan="4"><b>Numeric data types</b></td></tr>
  <tr><td>BIGINT</td><td>INT64</td><td></td><td> </td></tr>
  <tr><td>BIGSERIAL</td><td>INT64</td><td></td><td> </td></tr>
  <tr><td>DECIMAL</td><td>BYTE_ARRAY</td><td>STRING</td><td>A DECIMAL type is converted to a string in a BYTE_ARRAY type and encoded as UTF8.This conversion is to avoid complications due to data precision and data values that are not a number (NaN).</td></tr>
  <tr><td>DOUBLE PRECISION</td><td>DOUBLE</td><td></td><td> </td></tr>
  <tr><td>INTEGER</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>MONEY</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>REAL</td><td>FLOAT</td><td></td><td> </td></tr>
  <tr><td>SERIAL</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>SMALLINT</td><td>INT32</td><td>INT(16, true)</td><td> </td></tr>
  <tr><td>SMALLSERIAL</td><td>INT32</td><td>INT(16, true)</td><td> </td></tr>
  <tr><td colspan="3"><b>String and related data types</b></td><td></td></tr>
  <tr><td>ARRAY</td><td>BYTE_ARRAY</td><td>STRING</td><td>An array is converted to a string and encoded as BINARY (UTF8).<br />This conversion is to avoid complications due to data precision, data values that are not a number (NaN), and time data values.</td></tr>
  <tr><td>BIT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>BIT VARYING</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>BYTEA</td><td>BINARY</td><td></td><td> </td></tr>
  <tr><td>CHAR</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>CHAR(N)</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>ENUM</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>NAME</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>TEXT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>TEXT SEARCH</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>VARCHAR(N)</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>XML</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td colspan="4"><b>Date and time data types</b></td></tr>
  <tr><td>DATE</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>INTERVAL</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>TIME</td><td>BYTE_ARRAY</td><td>STRING</td><td></td></tr>
  <tr><td>TIME WITH TIME ZONE</td><td>BYTE_ARRAY</td><td>STRING</td><td></td></tr>
  <tr><td>TIMESTAMP</td><td>BYTE_ARRAY</td><td>STRING</td><td></td></tr>
  <tr><td>TIMESTAMP WITH TIME ZONE</td><td>BYTE_ARRAY</td><td>STRING</td><td></td></tr>
  <tr><td colspan="4"><b>Geometric data types</b></td></tr>
  <tr><td>BOX</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>CIRCLE</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>LINE</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>LINESEGMENT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>PATH</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>POINT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>POLYGON</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td colspan="4"><b>JSON data types</b></td></tr>
  <tr><td>JSON</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>JSONB</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td colspan="4"><b>Other data types</b></td></tr>
  <tr><td>BOOLEAN</td><td>BOOLEAN</td><td></td><td> </td></tr>
  <tr><td>CIDR</td><td>BYTE_ARRAY</td><td>STRING</td><td> Network data type</td></tr>
  <tr><td>COMPOSITE</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>DOMAIN</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>INET</td><td>BYTE_ARRAY</td><td>STRING</td><td> Network data type</td></tr>
  <tr><td>MACADDR</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>OBJECT IDENTIFIER</td><td>N/A</td><td></td><td></td></tr>
  <tr><td>PG_LSN</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>RANGE</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>UUID</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
</tbody>
</table>
