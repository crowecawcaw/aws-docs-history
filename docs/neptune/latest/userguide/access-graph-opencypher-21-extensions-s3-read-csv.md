

# Query examples using CSV
<a name="access-graph-opencypher-21-extensions-s3-read-csv"></a>

In this example, the query returns the number of rows in a given CSV file:

```
CALL neptune.read(
  {
    source: "<s3 path>",
    format: "csv"
  }
)
YIELD row
RETURN count(row)
```

You can run the query example using the execute-open-cypher-query operation in the AWS CLI by executing the following code:

```
aws neptunedata execute-open-cypher-query \
--open-cypher-query "CALL neptune.read({source: '<s3 path>', format: 'csv'}) YIELD row RETURN count(row)" \
--endpoint-url https://my-cluster-name.cluster-abcdefgh1234.us-east-1.neptune.amazonaws.com:8182
```

A query can be flexible in what it does with rows read from a CSV file. For instance, the following query creates a node with a field set to data from a CSV file:

```
CALL neptune.read(
  {
    source: "<s3 path>",
    format: "csv"
  }
)
YIELD row
CREATE (n {someField: row.someCol}) 
RETURN n
```

**Warning**  
It is not considered good practice use a large results-producing clause like MATCH(n) prior to a CALL clause. This would lead to a long-running query due to cross product between incoming solutions from prior clauses and the rows read by neptune.read. It is recommended to start the query with CALL neptune.read.

## Property column headers
<a name="property-column-headers"></a>

You can specify a column (`:`) for a property by using the following syntax. The type names are not case sensitive. If a colon appears within a property name, it must be escaped by preceding it with a backslash: `\:`.

```
propertyname:type
```

**Note**  
Space, comma, carriage return and newline characters are not allowed in the column headers, so property names cannot include these characters.
You can specify a column for an array type by adding `[]` to the type:  

  ```
                          propertyname:type[]
  ```
Edge properties can only have a single value and will cause an error if an array type is specified or a second value is specified. The following example shows the column header for a property named age of type Int:  

  ```
  age:Int
  ```

Every row in the file would be required to have an integer in that position or be left empty. Arrays of strings are allowed, but strings in an array cannot include the semicolon (`;`) character unless it is escaped using a backslash (`\;`).

## Supported CSV column types
<a name="supported-csv-column-types"></a>
+ **BOOL (or BOOLEAN)** - Allowed values: true, false. Indicates a Boolean field. Any value other than true will be treated as false.
+ **FLOAT** - Range: 32-bit IEEE 754 floating point including Infinity, INF, -Infinity, -INF and NaN (not-a-number).
+ **DOUBLE** - Range: 64-bit IEEE 754 floating point including Infinity, INF, -Infinity, -INF and NaN (not-a-number).
+ **STRING** - 
  + Quotation marks are optional. Commas, newline, and carriage return characters are automatically escaped if they are included in a string surrounded by double quotation marks ("). Example: "Hello, World".
  + To include quotation marks in a quoted string, you can escape the quotation mark by using two in a row: Example: "Hello ""World""".
  + Arrays of strings are allowed, but strings in an array cannot include the semicolon (;) character unless it is escaped using a backslash (\\;).
  + If you want to surround strings in an array with quotation marks, you must surround the whole array with one set of quotation marks. Example: "String one; String 2; String 3".
+ **DATE, DATETIME** - The datetime values can be provided in either the XSD format, or one of the following formats: 
  + yyyy-MM-dd
  + yyyy-MM-ddTHH:mm
  + yyyy-MM-ddTHH:mm:ss
  + yyyy-MM-ddTHH:mm:ssZ
  + yyyy-MM-ddTHH:mm:ss.SSSZ
  + yyyy-MM-ddTHH:mm:ss[\+\|-]hhmm
  + yyyy-MM-ddTHH:mm:ss.SSS[\+\|-]hhmm
+ **SIGNED INTEGER** - 
  + Byte: -128 to 127
  + Short: -32768 to 32767
  + Int: -2^31 to 2^31-1
  + Long: -2^63 to 2^63-1

**Neptune-specific column types:**
+ A column type Any is supported in the user columns. An Any type is a type "syntactic sugar" for all of the other types we support. It is extremely useful if a user column has multiple types in it. The payload of an Any type value is a list of json strings as follows: `{"value": "10", "type": "Int"};{"value": "1.0", "type": "Float"}`, which has a value field and a type field in each individual json string. The column header of an Any type is propertyname:Any. The cardinality value of an Any column is set, meaning that the column can accept multiple values. 
  + Neptune supports the following types in an Any type: Bool (or Boolean), Byte, Short, Int, Long, UnsignedByte, UnsignedShort, UnsignedInt, UnsignedLong, Float, Double, Date, dateTime, String, and Geometry.
  + Vector type is not supported in Any type.
  + Nested Any type is not supported. For example, `{"value": {"value": "10", "type": "Int"}, "type": "Any"}`.
+ A Geometry column type is supported in the user columns. The payload of these columns must only contain Geometry primitives of type Point, provided as strings in Well-known text (WKT) format. For example, POINT (30 10) would be a valid Geometry value.

## Sample CSV output
<a name="sample-csv-output"></a>

Given the following CSV file:

```
<s3 path>
colA:byte,colB:short,colC:int,colD:long,colE:float,colF:double,colG:string
-128,-32768,-2147483648,-9223372036854775808,1.23456,1.23457,first
127,32767,2147483647,9223372036854775807,nan,nan,second
0,0,0,0,-inf,-inf,third
0,0,0,0,inf,inf,fourth
```

This example shows the output returned by neptune.read using the following query:

```
aws neptunedata execute-open-cypher-query \
--open-cypher-query "CALL neptune.read({source: '<s3 path>', format: 'csv'}) YIELD row RETURN row" \
--endpoint-url https://my-cluster-name.cluster-abcdefgh1234.us-east-1.neptune.amazonaws.com:8182
```

```
{
  "results": [{
      "row": {
        "colD": -9223372036854775808,
        "colC": -2147483648,
        "colE": 1.23456,
        "colB": -32768,
        "colF": 1.2345699999999999,
        "colG": "first",
        "colA": -128
      }
    }, {
      "row": {
        "colD": 9223372036854775807,
        "colC": 2147483647,
        "colE": "NaN",
        "colB": 32767,
        "colF": "NaN",
        "colG": "second",
        "colA": 127
      }
    }, {
      "row": {
        "colD": 0,
        "colC": 0,
        "colE": "-INF",
        "colB": 0,
        "colF": "-INF",
        "colG": "third",
        "colA": 0
      }
    }, {
      "row": {
        "colD": 0,
        "colC": 0,
        "colE": "INF",
        "colB": 0,
        "colF": "INF",
        "colG": "fourth",
        "colA": 0
      }
    }]
}
```

Currently, there is no way to set a node or edge label to a data field coming from a CSV file. It is recommended that you partition the queries into multiple queries, one for each label/type.

```
CALL neptune.read({source: '<s3 path>', format: 'csv'})
 YIELD row 
WHERE row.`~label` = 'airport'
CREATE (n:airport)

CALL neptune.read({source: '<s3 path>', format: 'csv'})
YIELD row 
WHERE row.`~label` = 'country'
CREATE (n:country)
```