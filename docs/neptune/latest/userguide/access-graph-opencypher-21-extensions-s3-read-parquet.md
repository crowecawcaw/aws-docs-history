

# Query examples using parquet
<a name="access-graph-opencypher-21-extensions-s3-read-parquet"></a>

The following example query returns the number of rows in a given Parquet file:

```
CALL neptune.read(
  {
    source: "<s3 path>",
    format: "parquet"
  }
)
YIELD row
RETURN count(row)
```

You can run the query example using the `execute-open-cypher-query` operation in the AWS CLI by executing the following code:

```
aws neptunedata execute-open-cypher-query \
--open-cypher-query "CALL neptune.read({source: '<s3 path>', format: 'parquet'}) YIELD row RETURN count(row)" \
--endpoint-url https://my-cluster-name.cluster-abcdefgh1234.us-east-1.neptune.amazonaws.com:8182
```

A query can be flexible in what it does with rows read from a Parquet file. For example, the following query creates a node with a field being set to data found in the Parquet file:

```
CALL neptune.read(
  {
    source: "<s3 path>",
    format: "parquet"
  }
)
YIELD row
CREATE (n {someField: row.someCol}) 
RETURN n
```

**Warning**  
It is not considered good practice to use a large results-producing clause like `MATCH(n)` prior to a `CALL` clause. This would lead to a long-running query, due to cross product between incoming solutions from prior clauses and the rows read by neptune.read. It's recommended to start the query with `CALL` neptune.read.

## Supported Parquet column types
<a name="access-graph-opencypher-21-extensions-s3-read-parquet-column-types"></a>

**Parquet Data Types:**
+ NULL
+ BOOLEAN
+ FLOAT
+ DOUBLE
+ STRING
+ SIGNED INTEGER: UINT8, UINT16, UINT32, UINT64
+ MAP: Only supports one-level. Does not support nested.
+ LIST: Only supports one-level. Does not support nested.

**Neptune-specific data types:**

Unlike the property column headers of the CSV format, the property column headers of the Parquet format only need to have the property names, so there is no need to have the type names nor the cardinality.

There are however, some special column types in the Parquet format that require annotation in the metadata, including the Any type, Date type, dateTime type, and Geometry type. The following object is an example of the required metadata annotation for files containing columns of these special types:

```
"metadata": {
    "anyTypeColumns": ["UserCol1"],
    "dateTypeColumns": ["UserCol2"],
    "dateTimeTypeColumns": ["UserCol3"],
    "geometryTypeColumns": ["UserCol4"]
}
```

Below are details on the expected payload associated with these types:
+ A column type Any is supported in the user columns. An Any type is a type "syntactic sugar" for all of the other types we support. It is extremely useful if a user column has multiple types in it. The payload of an Any type value is a list of json strings as follows: `{"value": "10", "type": "Int"};{"value": "1.0", "type": "Float"}`, which has a value field and a type field in each individual json string. The cardinality value of an Any column is set, meaning that the column can accept multiple values. 
  + Neptune supports the following types in an Any type: Bool (or Boolean), Byte, Short, Int, Long, UnsignedByte, UnsignedShort, UnsignedInt, UnsignedLong, Float, Double, Date, dateTime, String, and Geometry.
  + Vector type is not supported in Any type.
  + Nested Any type is not supported. For example, `{"value": {"value": "10", "type": "Int"}, "type": "Any"}`.
+ Columns of type Date and Datetime are supported in the user columns. The payload of these columns must be provided as strings following the XSD format or one of the formats below: 
  + yyyy-MM-dd
  + yyyy-MM-ddTHH:mm
  + yyyy-MM-ddTHH:mm:ss
  + yyyy-MM-ddTHH:mm:ssZ
  + yyyy-MM-ddTHH:mm:ss.SSSZ
  + yyyy-MM-ddTHH:mm:ss[\+\|-]hhmm
  + yyyy-MM-ddTHH:mm:ss.SSS[\+\|-]hhmm
+ A Geometry column type is supported in the user columns. The payload of these columns must only contain Geometry primitives of type Point, provided as strings in Well-known text (WKT) format. For example, POINT (30 10) would be a valid Geometry value.

## Sample parquet output
<a name="sample-parquet-output"></a>

Given a Parquet file like this:

```
<s3 path>

Parquet Type:
    int8     int16       int32             int64              float      double    string
+--------+---------+-------------+----------------------+------------+------------+----------+
|   Byte |   Short |       Int   |                Long  |     Float  |    Double  | String   |
|--------+---------+-------------+----------------------+------------+------------+----------|
|   -128 |  -32768 | -2147483648 | -9223372036854775808 |    1.23456 |    1.23457 | first    |
|    127 |   32767 |  2147483647 |  9223372036854775807 |  nan       |  nan       | second   |
|      0 |       0 |           0 |                    0 | -inf       | -inf       | third    |
|      0 |       0 |           0 |                    0 |  inf       |  inf       | fourth   |
+--------+---------+-------------+----------------------+------------+------------+----------+
```

Here is an example of the output returned by neptune.read using the following query:

```
aws neptunedata execute-open-cypher-query \
--open-cypher-query "CALL neptune.read({source: '<s3 path>', format: 'parquet'}) YIELD row RETURN row" \
--endpoint-url https://my-cluster-name.cluster-abcdefgh1234.us-east-1.neptune.amazonaws.com:8182
```

```
{
 "results": [{
 "row": {
 "Float": 1.23456,
 "Byte": -128,
 "Int": -2147483648,
 "Long": -9223372036854775808,
 "String": "first",
 "Short": -32768,
 "Double": 1.2345678899999999
 }
 }, {
 "row": {
 "Float": "NaN",
 "Byte": 127,
 "Int": 2147483647,
 "Long": 9223372036854775807,
 "String": "second",
 "Short": 32767,
 "Double": "NaN"
 }
 }, {
 "row": {
 "Float": "-INF",
 "Byte": 0,
 "Int": 0,
 "Long": 0,
 "String": "third",
 "Short": 0,
 "Double": "-INF"
 }
 }, {
 "row": {
 "Float": "INF",
 "Byte": 0,
 "Int": 0,
 "Long": 0,
 "String": "fourth",
 "Short": 0,
 "Double": "INF"
 }
 }]
}
```

Currently, there is no way to set a node or edge label to a data field coming from a Parquet file. It is recommended that you partition the queries into multiple queries, one for each label/Type.

```
CALL neptune.read({source: '<s3 path>', format: 'parquet'})
 YIELD row 
WHERE row.`~label` = 'airport'
CREATE (n:airport)

CALL neptune.read({source: '<s3 path>', format: 'parquet'})
YIELD row 
WHERE row.`~label` = 'country'
CREATE (n:country)
```