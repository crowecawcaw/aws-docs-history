# Querying in Amazon DocumentDB

This section explains all aspects of querying with Amazon DocumentDB.

###### Topics

- [Querying documents](#querying.docs "#querying.docs")
- [Query plan](#querying.queryplan "#querying.queryplan")
- [Explain results](#querying.explainresults "#querying.explainresults")
- [Query planner v2](query-planner.md "query-planner.md")
- [Query planner v3](query-planner-v3.md "query-planner-v3.md")
- [Geospatial data](geospatial.md "geospatial.md")
- [Partial index](partial-index.md "partial-index.md")
- [Text search](text-search.md "text-search.md")

## Querying documents

At times, you might need to look up your online store's inventory so that customers can see and purchase what you're selling. Querying a collection is relatively easy, whether you want all documents in the collection or only those documents that satisfy a particular criterion.

To query for documents, use the `find()` operation. The `find()` command has a single document parameter that defines the criteria to use in choosing the documents to return. The output from `find()` is a document formatted as a single line of text with no line breaks. To format the output document for easier reading, use `find().pretty()`. All the examples in this topic use `.pretty()` to format the output.

The following code samples use the four documents you inserted into the `example` collection in the preceding two exercises — `insertOne()` and `insertMany()` that are located in the Adding Documents section of [Working with Documents](document-database-working-with-documents.md "document-database-working-with-documents.md").

###### Topics

- [Retrieving all documents](#querying.alldocs "#querying.alldocs")
- [Matching field values](#querying.matchfield "#querying.matchfield")
- [Embedded documents](#querying.embedded-doc "#querying.embedded-doc")
- [Field values in embedded documents](#querying.embedded-docs-field "#querying.embedded-docs-field")
- [Matching an array](#querying.array "#querying.array")
- [Matching values in an array](#querying.array-values "#querying.array-values")
- [Using operators](#querying.operators "#querying.operators")

### Retrieving all documents in a collection

To retrieve all the documents in your collection, use the `find()` operation with an empty query document.

The following query returns all documents in the `example` collection.

```
db.example.find( {} ).pretty()
```

### Retrieving documents that match a field Value

To retrieve all documents that match a field and value, use the `find()` operation with a query document that identifies the fields and values to match.

Using the preceding documents, this query returns all documents where the "Item" field equals "Pen".

```
db.example.find( { "Item": "Pen" } ).pretty()
```

### Retrieving documents that match an embedded document

To find all the documents that match an embedded document, use the `find()` operation with a query document that specifies the embedded document name and all the fields and values for that embedded document.

When matching an embedded document, the document's embedded document must have the same name as in the query. In addition, the fields and values in the embedded document must match the query.

The following query returns only the "Poster Paint" document. This is because the "Pen" has different values for "`OnHand`" and "`MinOnHand`", and "Spray Paint" has one more field (`OrderQnty`) than the query document.

```
db.example.find({"Inventory": {
    "OnHand": 47,
    "MinOnHand": 50 } } ).pretty()
```

### Retrieving documents that match a field value in an embedded document

To find all the documents that match an embedded document, use the `find()` operation with a query document that specifies the embedded document name and all the fields and values for that embedded document.

Given the preceding documents, the following query uses "dot notation" to specify the embedded document and fields of interest. Any document that matches these are returned, regardless of what other fields might be present in the embedded document. The query returns "Poster Paint" and "Spray Paint" because they both match the specified fields and values.

```
db.example.find({"Inventory.OnHand": 47, "Inventory.MinOnHand": 50 }).pretty()
```

### Retrieving documents that match an array

To find all documents that match an array, use the `find()` operation with the array name that you are interested in and all the values in that array. The query returns all documents that have an array with that name in which the array values are identical to and in the same order as in the query.

The following query returns only the "Pen" because the "Poster Paint" has an additional color (White), and "Spray Paint" has the colors in a different order.

```
db.example.find( { "Colors": ["Red","Green","Blue","Black"] } ).pretty()
```

### Retrieving documents that match a value in an array

To find all the documents that have a particular array value, use the `find()` operation with the array name and the value that you're interested in.

```
db.example.find( { "Colors": "Red" } ).pretty()
```

The preceding operation returns all three documents because each of them has an array named `Colors` and the value "`Red`" somewhere in the array. If you specify the value "`White`," the query would only return "Poster Paint."

### Retrieving documents using operators

The following query returns all documents where the "`Inventory.OnHand`" value is less than 50.

```
db.example.find(
        { "Inventory.OnHand": { $lt: 50 } } )
```

For a listing of supported query operators, see [Query and projection operators](mongo-apis.md#mongo-apis-query "mongo-apis.md#mongo-apis-query").

## Query plan

### How Can I See

the `executionStats` for a Query Plan?

When determining why a query is executing slower than expected, it can be useful to understand what the `executionStats` are
for the query plan. The `executionStats` provide the number of documents returned from a particular stage (`nReturned`), the amount of execution time spent at each stage (`executionTimeMillisEstimate`), and the amount of time it takes to generate a query plan (`planningTimeMillis`). You can determine the most time-intensive stages of your query to help focus your optimization efforts from the output of `executionStats`, as shown in the query examples below. The `executionStats` parameter does not currently support `update` and `delete` commands.

###### Note

Amazon DocumentDB emulates the MongoDB 3.6 API on a purpose-built database engine that utilizes a distributed, fault-tolerant, self-healing storage system. As a result, query plans and the output of `explain()` may differ between Amazon DocumentDB and MongoDB. Customers who want control over their query plan can use the `$hint` operator to enforce selection of a preferred index.

Run the query that you want to improve under the
`explain()` command as follows.

```
db.runCommand({explain: {query document}}).
explain("executionStats").executionStats;
```

The following is an example operation.

```
db.fish.find({}).limit(2).explain("executionStats");
```

Output from this operation looks something like the following.

```
{
    "queryPlanner" : {
        "plannerVersion" : 1,
        "namespace" : "test.fish",
        "winningPlan" : {
            "stage" : "SUBSCAN",
            "inputStage" : {
                "stage" : "LIMIT_SKIP",
                "inputStage" : {
                    "stage" : "COLLSCAN"
                }
            }
        }
    },
    "executionStats" : {
        "executionSuccess" : true,
        "executionTimeMillis" : "0.063",
        "planningTimeMillis" : "0.040",
        "executionStages" : {
            "stage" : "SUBSCAN",
            "nReturned" : "2",
            "executionTimeMillisEstimate" : "0.012",
            "inputStage" : {
                "stage" : "LIMIT_SKIP",
                "nReturned" : "2",
                "executionTimeMillisEstimate" : "0.005",
                "inputStage" : {
                    "stage" : "COLLSCAN",
                    "nReturned" : "2",
                    "executionTimeMillisEstimate" : "0.005"
                }
            }
        }
    },
    "serverInfo" : {
        "host" : "enginedemo",
        "port" : 27017,
        "version" : "3.6.0"
    },
    "ok" : 1
}

```

If you are interested in seeing only the `executionStats` from the query above, you can use the following command. For small collections, the Amazon DocumentDB query processor can choose to not use an index if the performance gains are negligible.

```
db.fish.find({}).limit(2).explain("executionStats").executionStats;
```

### Query plan cache

In order to optimize performance and reduce planning duration, Amazon DocumentDB internally caches query plans. This enables queries with the same shape to be executed directly using a cached plan.

However, this caching may sometimes cause a random delay for the same query; for example, a query that typically takes one second to run may occasionally take ten seconds. This is because over time, the reader instance cached various shapes of the query, thus consuming memory. If you experience this random slowness, there is no action needed you need to do to release the memory--the system will manage the memory usage for you and once the memory reaches certain threshold, it will be automatically released.

## Explain results

If you want to return information on query plans, Amazon DocumentDB supports verbosity mode `queryPlanner`. The `explain` results return the selected query plan chosen by the optimizer in a format similar to the following:

```
{
   "queryPlanner" : {
      "plannerVersion" : <int>,
      "namespace" : <string>,
      "winningPlan" : {
         "stage" : <STAGE1>,
         ...
         "inputStage" : {
            "stage" : <STAGE2>,
            ...
            "inputStage" : {
               ...
            }
         }
      }
   }
}

```

The following sections will define common `explain` results.

###### Topics

- [Scan and filter stage](#querying.explainresults-scan-filter "#querying.explainresults-scan-filter")
- [Index intersection](#querying.explainresults-index-intersection "#querying.explainresults-index-intersection")
- [Index union](#querying.explainresults-index-union "#querying.explainresults-index-union")
- [Multiple index intersection/union](#querying.explainresults-multiple-index-union "#querying.explainresults-multiple-index-union")
- [Compound index](#querying.explainresults-compound-index "#querying.explainresults-compound-index")
- [Sort stage](#querying.explainresults-sort "#querying.explainresults-sort")
- [Group stage](#querying.explainresults-group "#querying.explainresults-group")

### Scan and filter stage

The optimizer may choose one of the following scans:

COLLSCAN

This stage is a sequential collection scan.

```
{
    "stage" : "COLLSCAN"
}

```

IXSCAN

This stage scans the index keys. The optimizer may retrieve the document within this stage and this may result in a FETCH stage appended later.

```
db.foo.find({"a": 1})
{
    "stage" : "IXSCAN",
    "direction" : "forward",
    "indexName" : <idx_name>
}

```

FETCH

If the optimizer retrieved documents in a stage other than IXSCAN, the result will include a FETCH stage. For example, the IXSCAN query above may result a combination of FETCH and IXSCAN stages:

```
db.foo.find({"a": 1})
{
    "stage" : "FETCH",
    "inputStage" : {
        "stage" : "IXSCAN",
        "indexName" : <idx_name>
    }
}

```

IXONLYSCAN scans only the index key. Create compound indexes won't avoid FETCH.

### Index intersection

IXAND

Amazon DocumentDB may include an IXAND stage with an inputStages array of IXSCAN if it can utilize index intersection. For example, we may see output like:

```
{
    "stage" : "FETCH",
    "inputStage" : {
        "stage" : "IXAND",
        "inputStages" : [
            {
                "stage" : "IXSCAN",
                "indexName" : "a_1"
            },
            {
                "stage" : "IXSCAN",
                "indexName" : "b_1"
            }
        ]
    }
}

```

### Index union

IXOR

Similar to index intersection, Amazon DocumentDB may include `IXOR` stage with an `inputStages` array for the `$or` operator.

```
db.foo.find({"$or": [{"a": {"$gt": 2}}, {"b": {"$lt": 2}}]})
```

For the above query, the explain output may look like this:

```
{
    "stage" : "FETCH",
    "inputStage" : {
        "stage" : "IXOR",
        "inputStages" : [
            {
                "stage" : "IXSCAN",
                "indexName" : "a_1"
            },
            {
                "stage" : "IXSCAN",
                "indexName" : "b_1"
            }
        ]
    }
}

```

### Multiple index intersection/union

Amazon DocumentDB can combine multiple index intersection or union stages together then fetch the result. For example:

```
{
    "stage" : "FETCH",
    "inputStage" : {
        "stage" : "IXOR",
        "inputStages" : [
            {
                "stage" : "IXSCAN",
                ...
            },
            {
                "stage" : "IXAND",
                "inputStages" : [
                    {
                        "stage" : "IXSCAN",
                        ...
                    },
                    {
                        "stage" : "IXSCAN",
                        ...
                    }
                ]
            }
        ]
    }
}

```

The usage of index intersection or union stages are not impacted by the index type (sparse, compound, etc).

### Compound index

Amazon DocumentDB compound index usage is not limited in the beginning subsets of indexed fields; it can use index with the suffix part but it may not be very efficient.

For example, the compound index of `{ a: 1, b: -1 }` can support all three queries below:

`db.orders.find( { a: 1 } )`

`db.orders.find( { b: 1 } )`

`db.orders.find( { a: 1, b: 1 } )`

### Sort stage

If there is an index on the requested sort key(s), Amazon DocumentDB can use the index to obtain the order. In that case, the result will not include a `SORT` stage, but rather an `IXSCAN` stage. If the optimizer favors a plain sort, it will include a stage like this:

```
{
    "stage" : "SORT",
    "sortPattern" : {
        "a" : 1,
        "b" : -1
    }
}

```

### Group stage

Amazon DocumentDB supports two different group strategies:

- `SORT_AGGREGATE`: On disk sort aggregate.
- `HASH_AGGREGATE`: In memory hash aggregate.
