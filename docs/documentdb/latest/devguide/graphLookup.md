

# $graphLookup
<a name="graphLookup"></a>

New from version 8.0.2.

The `$graphLookup` aggregation stage in Amazon DocumentDB performs a recursive search on a collection. For each input document, `$graphLookup` starts from one or more values and repeatedly matches a connecting field to a target field, following the chain of matching documents until there are no more matches or an optional recursion depth is reached. This is useful for traversing graph-like or hierarchical data, such as organizational reporting structures, category trees, or network relationships.

**Parameters**
+ `from`: The target collection to search recursively. The `from` collection must be in the same database.
+ `startWith`: The expression that specifies the value or values to begin the recursive search with. This value is compared against the `connectToField` of the documents in the `from` collection. If `startWith` evaluates to an array, the search runs from all array elements at the same time.
+ `connectFromField`: The field name whose value is used to connect to the next document in the recursive search. If the value is an array, each element is followed individually through the traversal.
+ `connectToField`: The field name in the `from` collection that is matched against the value of the `connectFromField`.
+ `as`: The name of the array field added to each output document. This field contains the documents found during the recursive search. For information about the order of these documents, see the Result ordering item in the following Behavior section.
+ `maxDepth`: A non-negative integer that specifies the maximum number of recursive iterations to perform after the initial lookup. This parameter is optional. A value of `0` performs only the initial match and no recursion. If you omit `maxDepth`, the search continues recursively until there are no more matching documents.
+ `depthField`: The name of the field to add to each document in the `as` array that holds the recursion depth at which the document was found. This parameter is optional. The depth is represented as a `NumberLong` and starts at zero, so the initial lookup corresponds to a depth of `0`.
+ `restrictSearchWithMatch`: A document that specifies an additional match condition applied to the documents of the search. This parameter is optional. The condition uses the same query syntax as a `$match` stage and cannot include aggregation expressions.

**Note**  
The `$graphLookup` stage is subject to a 100 MB memory limit and doesn't support `allowDiskUse:true`. An operation that exceeds this limit returns an error. If the aggregation includes other stages, the `allowDiskUse:true` option remains in effect for those stages.

**Behavior**
+ **Cross-collection traversal**: Set `from` to the collection you want to search. This can be the same collection the pipeline runs against or a different collection in the same database.
+ **Result ordering**: The documents in the `as` array are not returned in any guaranteed order.

## Example (MongoDB Shell)
<a name="graphLookup-examples"></a>

The following example uses `$graphLookup` to traverse an employee reporting hierarchy and, for each employee, return the full chain of managers above them.

The following commands, run in the mongosh shell, insert sample employee documents that establish a reporting hierarchy:

```
db.employees.insertMany([
  { _id: 1, name: "Dev", reportsTo: "Eliot" },
  { _id: 2, name: "Eliot", reportsTo: "Ron" },
  { _id: 3, name: "Ron", reportsTo: "Andrew" },
  { _id: 4, name: "Andrew", reportsTo: "Asya" },
  { _id: 5, name: "Asya" }
]);
```

The following aggregation returns the full management chain for each employee in a new `reportingHierarchy` array:

```
db.employees.aggregate([
  {
    $graphLookup: {
      from: "employees",
      startWith: "$reportsTo",
      connectFromField: "reportsTo",
      connectToField: "name",
      as: "reportingHierarchy",
      depthField: "level"
    }
  }
]);
```

This operation returns the following output:

```
[
  {
    _id: 1,
    name: 'Dev',
    reportsTo: 'Eliot',
    reportingHierarchy: [
      { _id: 2, name: 'Eliot', reportsTo: 'Ron', level: 0 },
      { _id: 3, name: 'Ron', reportsTo: 'Andrew', level: 1 },
      { _id: 4, name: 'Andrew', reportsTo: 'Asya', level: 2 },
      { _id: 5, name: 'Asya', level: 3 }
    ]
  },
  {
    _id: 2,
    name: 'Eliot',
    reportsTo: 'Ron',
    reportingHierarchy: [
      { _id: 3, name: 'Ron', reportsTo: 'Andrew', level: 0 },
      { _id: 4, name: 'Andrew', reportsTo: 'Asya', level: 1 },
      { _id: 5, name: 'Asya', level: 2 }
    ]
  },
  {
    _id: 3,
    name: 'Ron',
    reportsTo: 'Andrew',
    reportingHierarchy: [
      { _id: 4, name: 'Andrew', reportsTo: 'Asya', level: 0 },
      { _id: 5, name: 'Asya', level: 1 }
    ]
  },
  {
    _id: 4,
    name: 'Andrew',
    reportsTo: 'Asya',
    reportingHierarchy: [
      { _id: 5, name: 'Asya', level: 0 }
    ]
  },
  {
    _id: 5,
    name: 'Asya',
    reportingHierarchy: []
  }
]
```

Each employee document gains a `reportingHierarchy` array that contains the recursively matched manager documents. The `level` field records the recursion depth at which each manager was found. Asya has no `reportsTo` value, so her `reportingHierarchy` array is empty.

## Example with maxDepth and restrictSearchWithMatch (MongoDB Shell)
<a name="graphLookup-filter-depth-example"></a>

The following example traverses a network of connections between people and uses `maxDepth` to limit the recursion and `restrictSearchWithMatch` to include only documents that match an additional condition. The search finds the connections of a starting person, up to two levels deep, keeping only people whose `hobbies` array contains `golf`.

The following commands, run in the mongosh shell, insert sample documents in which each person's `friends` point forward through a one-directional chain of connections:

```
db.people.insertMany([
  { _id: 1, name: "Tanya", friends: [ "Carole", "Shirley" ], hobbies: [ "tennis", "golf" ] },
  { _id: 2, name: "Carole", friends: [ "Joseph" ], hobbies: [ "archery", "golf" ] },
  { _id: 3, name: "Joseph", friends: [ "Angelo" ], hobbies: [ "tennis", "golf" ] },
  { _id: 4, name: "Angelo", friends: [ "Miguel" ], hobbies: [ "travel", "golf" ] },
  { _id: 5, name: "Miguel", friends: [], hobbies: [ "golf" ] },
  { _id: 6, name: "Shirley", friends: [], hobbies: [ "frisbee" ] }
]);
```

The following aggregation starts from Tanya, traverses her network of connections up to two levels deep, and keeps only the people who list `golf` as a hobby:

```
db.people.aggregate([
  { $match: { name: "Tanya" } },
  {
    $graphLookup: {
      from: "people",
      startWith: "$friends",
      connectFromField: "friends",
      connectToField: "name",
      as: "golfConnections",
      maxDepth: 2,
      restrictSearchWithMatch: { hobbies: "golf" }
    }
  },
  { $project: { name: 1, "golfConnections.name": 1 } }
]);
```

This operation returns the following output:

```
[
  {
    _id: 1,
    name: 'Tanya',
    golfConnections: [
      { name: 'Carole' },
      { name: 'Joseph' },
      { name: 'Angelo' }
    ]
  }
]
```

Only connections whose `hobbies` array contains `golf` are included, and the traversal stops after two levels of recursion. Shirley is excluded because she does not list `golf`, and Miguel is excluded because he is three levels away from Tanya, beyond the `maxDepth` of `2`. Because the connections form a one-directional chain that never points back to Tanya, the starting document is not matched during the recursive search.

## Code examples
<a name="graphLookup-code"></a>

To view a code example that builds the employee reporting hierarchy from the first example using a MongoDB driver, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = new MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');

  try {
    await client.connect();
    const db = client.db('test');
    const employees = db.collection('employees');

    const result = await employees.aggregate([
      {
        $graphLookup: {
          from: 'employees',
          startWith: '$reportsTo',
          connectFromField: 'reportsTo',
          connectToField: 'name',
          as: 'reportingHierarchy',
          depthField: 'level'
        }
      }
    ]).toArray();

    console.log(JSON.stringify(result, null, 2));
  } catch (err) {
    console.error('Failed to run $graphLookup aggregation:', err.message);
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
from pymongo.errors import PyMongoError

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

    try:
        db = client['test']
        employees = db['employees']

        pipeline = [
            {
                "$graphLookup": {
                    "from": "employees",
                    "startWith": "$reportsTo",
                    "connectFromField": "reportsTo",
                    "connectToField": "name",
                    "as": "reportingHierarchy",
                    "depthField": "level"
                }
            }
        ]

        result = list(employees.aggregate(pipeline))

        for doc in result:
            print(doc)
    except PyMongoError as error:
        print(f"Failed to run $graphLookup aggregation: {error}")
    finally:
        client.close()

example()
```

------