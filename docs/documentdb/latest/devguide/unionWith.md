

# $unionWith
<a name="unionWith"></a>

New from version 8.0.3.

The `$unionWith` aggregation stage in Amazon DocumentDB combines the results of two aggregations into a single result set. The stage passes the documents from the previous stage of the pipeline together with the documents from a second collection to the next stage. The combined result set includes duplicates, and `$unionWith` does not guarantee the order of the documents.

Use `$unionWith` to combine data from multiple collections in a single query, such as merging historical and current data for reporting. This avoids writing separate queries for each collection and combining the results yourself. You can analyze data across collections without maintaining application-side merge logic.

**Syntax**

To combine the documents from a collection and optionally run an aggregation pipeline on them before they are added to the result set, use the following form:

```
{ $unionWith: { coll: "<collection>", pipeline: [ <stage1>, <stage2>, ... ] } }
```

To include all documents from the specified collection without any processing, use the simplified form:

```
{ $unionWith: "<collection>" }
```

**Parameters**

The `$unionWith` stage accepts the following parameters:
+ `coll`: The name of the collection or view whose documents you want to include in the result set.
+ `pipeline`: An optional aggregation pipeline that processes the documents in the `coll` collection before adding them to the result set. The pipeline cannot include the `$out` or `$merge` stages. If you omit `pipeline`, `$unionWith` includes all documents from the `coll` collection in the result set without any processing.

**Restrictions**

The `$unionWith` stage has the following restrictions:
+ The `$unionWith` pipeline cannot include the `$out` stage.
+ The `$unionWith` pipeline cannot include the `$merge` stage.
+ The `$unionWith` stage cannot be used inside transactions.
+ If the source collection that the aggregation runs on does not exist, `$unionWith` returns no results, even when `coll` specifies a collection that contains documents.

## Example – Combine documents from two collections (MongoDB Shell)
<a name="unionWith-examples"></a>

The following example demonstrates how to use the `$unionWith` stage to combine documents from two collections into a single result set.

**Create sample documents**

```
db.sales_2020.insertMany([
  { _id: 1, item: "abc", quantity: 2 },
  { _id: 2, item: "def", quantity: 1 }
]);

db.sales_2021.insertMany([
  { _id: 1, item: "ghi", quantity: 3 },
  { _id: 2, item: "jkl", quantity: 5 }
]);
```

**Query example**

The following MongoDB Shell command combines the documents from the `sales_2020` collection with the documents from the `sales_2021` collection:

```
db.sales_2020.aggregate([
  { $unionWith: { coll: "sales_2021" } }
]);
```

**Output**

```
[
  { _id: 1, item: 'abc', quantity: 2 },
  { _id: 2, item: 'def', quantity: 1 },
  { _id: 1, item: 'ghi', quantity: 3 },
  { _id: 2, item: 'jkl', quantity: 5 }
]
```

## Code examples
<a name="unionWith-code"></a>

The following Node.js and Python code examples show how to use the `$unionWith` command. Choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const uri = 'mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false';
  const client = new MongoClient(uri);

  try {
    await client.connect();

    const db = client.db('test');
    const sales2020 = db.collection('sales_2020');

    const result = await sales2020.aggregate([
      { $unionWith: { coll: 'sales_2021' } }
    ]).toArray();

    console.log(JSON.stringify(result, null, 2));

  } catch (error) {
    console.error('Error:', error);
  } finally {
    await client.close();
  }
}

example();
```

------
#### [ Python ]

```
from pymongo import MongoClient
from pprint import pprint

def example():
    client = None
    try:
        client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

        db = client['test']
        sales_2020 = db['sales_2020']

        pipeline = [
            { '$unionWith': { 'coll': 'sales_2021' } }
        ]

        result = list(sales_2020.aggregate(pipeline))
        pprint(result)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if client:
            client.close()

example()
```

------