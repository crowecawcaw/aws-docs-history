# Query examples using CSV

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

You can run the query using the `execute-query` operation in the AWS CLI:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string 'CALL neptune.read({source: "<s3 path>",
    format: "csv"}) YIELD row RETURN count(row)' \
  --language open_cypher \
  /tmp/out.txt
```

A query can be flexible in what it does with rows read from a Parquet file. For instance, the following query creates
a node with a field set to data from a CSV file:

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

###### Warning

It is not considered good practice use a large results-producing clause like `MATCH(n)` prior to a
`CALL` clause. This would lead to a long-running query due to cross product between incoming solutions
from prior clauses and the rows read by neptune.read. It is recommended to start the query with CALL neptune.read.
