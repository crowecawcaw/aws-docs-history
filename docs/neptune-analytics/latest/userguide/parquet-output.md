# Sample Parquet output

Given a Parquet file like this:

````
<s3 path>

Parquet Type:
    int8     int16       int32             int64              float      double    string
+--------+---------+-------------+----------------------+------------+------------+----------+
|   Byte |   Short |       Int   |                Long  |     Float  |    Double  | String   |
|--------+---------+-------------+----------------------+------------+------------+----------|
|   -128 |  -32768 | -2147483648 | -9223372036854775808 |    1.23456 |    1.23457 | first    |
|    127 |   32767 |  2147483647 |  9223372036854775807 |  nan       |  nan       | second   |
|      0 |       0 |           0 |                    0 | -inf       | -inf       | third    |
|      0 |       0 |           0 |                    0 |  inf       |  inf       | fourth   | +--------+---------+-------------+----------------------+------------+------------+----------+ ``` Here is an example of the output returned by `neptune.read` using the following query: ``` aws neptune-graph execute-query \ --graph-identifier ${graphIdentifier} \ --query-string "CALL neptune.read({source: '<s3 path>', format: 'parquet'}) YIELD row RETURN row" \ --language open_cypher \ /tmp/out.txt cat /tmp/out.txt { "results": [{ "row": { "Float": 1.23456, "Byte": -128, "Int": -2147483648, "Long": -9223372036854775808, "String": "first", "Short": -32768, "Double": 1.2345678899999999 } }, { "row": { "Float": "NaN", "Byte": 127, "Int": 2147483647, "Long": 9223372036854775807, "String": "second", "Short": 32767, "Double": "NaN" } }, { "row": { "Float": "-INF", "Byte": 0, "Int": 0, "Long": 0, "String": "third", "Short": 0, "Double": "-INF" } }, { "row": { "Float": "INF", "Byte": 0, "Int": 0, "Long": 0, "String": "fourth", "Short": 0, "Double": "INF" } }] }% ``` Currently, there is no way to set a node or edge label to a data field coming from a Parquet file. It is recommended that you partition the queries into multiple queries, one for each label/Type. ``` CALL neptune.read({source: '<s3 path>', format: 'parquet'}) YIELD row WHERE row.`~label` = 'airport' CREATE (n:airport) CALL neptune.read({source: '<s3 path>', format: 'parquet'}) YIELD row WHERE row.`~label` = 'country' CREATE (n:country) ```
````
