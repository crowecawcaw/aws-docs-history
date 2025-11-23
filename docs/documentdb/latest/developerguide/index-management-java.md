# Index management in Amazon DocumentDB with Java

Indexes allow efficient retrieval of data from an Amazon DocumentDB collection.
Without indexes, DocumentDB must scan every document in the collection to return results that satisfy a given query.
This topic provides information on how to create, drop, and list indexes using the MongoDB Java drivers.
It also discusses how to determine if a particular index is being used in the query and how to give hints to Amazon DocumentDB to use a specific index.

###### Topics

- [Creating indexes](#creating-indexes "#creating-indexes")
- [Dropping indexes](#dropping-indes "#dropping-indes")
- [Determining index selection and providing index hint](#w2aac43b9b7c17c13 "#w2aac43b9b7c17c13")
  Amazon DocumentDB support many types of indexes. For a comprehensive overview of all the supported indexes refer to this [blog post](https://aws.amazon.com/blogs/database/how-to-index-on-amazon-documentdb-with-mongodb-compatibility/ "https://aws.amazon.com/blogs/database/how-to-index-on-amazon-documentdb-with-mongodb-compatibility/").

## Creating indexes with Java

There are two mechanisms for creating indexes in Amazon DocumentDB using MongoDB Java drivers: through `runCommand()`, and by either the `createIndex()` method for a single index or the `createIndexes()` method for multiple indexes.
One reason for using the `createIndex()` and `createIndexes()` methods is that you can build better error handling by catching specific errors related to index creation.
Another reason for using these method over `runCommand()` is that the MongDB Java driver provides a rich set of supporting classes for index creation and manipulation. Note that these supporting classes can only be used when you are using the `createIndex()` or `createIndexes()` methods.
There are three supporting classes:

- **[`Indexes`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/Indexes.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/Indexes.html")** — This class serves as a utility class offering static factory methods for creating various types of indexes.
  It simplifies the process of creating complex index definitions and is commonly used in conjunction with other index-related classes.
- **[`IndexModel`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/IndexModel.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/IndexModel.html")** — This is a fundamental class that encapsulates both the index keys definition and its options.
  It represents a complete index specification, combining what to index (the keys) with how to index (the options).
  This class is particularly useful when creating multiple indexes simultaneously, as it allows you to define a collection of index specifications that can be passed to the `createIndexes()` method.
- **[`IndexOptions`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/IndexOptions.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/IndexOptions.html")** — This is a comprehensive configuration class that provides a rich set of methods for customizing index behavior.
  It includes settings for unique indexes, sparse indexes, expiration time (TTL), and partial filter expressions.
  Through method chaining, you can configure multiple options like background index building and unique constraints.

**Create single index**

This example shows how to create a single index using the `createIndex(`) method in the background.
To understand background and foreground index creation, please refer [Index build types](managing-indexes.md#index-build-types "managing-indexes.md#index-build-types").
The following code example uses [`IndexOptions`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/IndexOptions.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/IndexOptions.html") to create a unique index with a name of “unique_restaurantId_idx” in the background.
This `IndexOptions` object is then passed to the `createIndex()` method.

```
collection.createIndex(
    Indexes.ascending("restaurantId"),
    new IndexOptions()
        .unique(true)
        .name("unique_restaurantId_idx")
        .background(true));
```

**Create multiple indexes**

This example creates multiple indexes using the `createIndexes()` method.
It first builds the option for each index by using the [`IndexModel`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/IndexModel.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/IndexModel.html") object and then passes a list of `IndexModel` objects to the `createIndexes()` method.
The the following code example shows how to create a composite index by using the [`Indexes`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/Indexes.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/Indexes.html") utility class.
This class is also used to specify if you want to create an index using ascending or descending sort order.
After creating multiple indexes, it verifies index creation by calling the `listIndexes()` method.

```
// Single Field Index on cuisine
IndexModel singleIndex = new IndexModel(
    Indexes.ascending("cuisine"),
    new IndexOptions().name("cuisine_idx"));

// Compound Index
IndexModel compoundIndex = new IndexModel(
    Indexes.compoundIndex(
        Indexes.ascending("address.state"),
        Indexes.ascending("priceRange")),
    new IndexOptions().name("location_price_idx"));

// Build a list of IndexModel for the indexes
List < IndexModel > indexes = Arrays.asList(
    singleIndex,
    compoundIndex
);

collection.createIndexes(indexes);

// Verify created indexes
collection.listIndexes().forEach(index - > System.out.println("Created index: " + index.toJson()));
```

**Create sparse and partial indexes**

This example shows creates a sparse and a partial index by creating an [`IndexModel`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/IndexModel.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/IndexModel.html") for each type of index.

```
// Sparse Index Model, this will identify only those documents that have a
// michelin star rating
IndexModel sparseIndex = new IndexModel(
    Indexes.ascending("michelin.star"),
    new IndexOptions()
    .name("michelin_sparse_idx")
    .sparse(true));

// Partial Index Model where the restaurant is active and has a rating of 4 and above
IndexModel partialIndex = new IndexModel(
    Indexes.ascending("rating.average"),
    new IndexOptions()
    .name("high_rated_active_idx")
    .partialFilterExpression(
        Filters.and(
            Filters.eq("isActive", true),
            Filters.gte("rating.average", 4.0))));
```

**Create a text index**

This example shows how to create a text index.
Only one text index is allowed on a collection but that one text index can be a compound index covering multiple fields.
When using multiple fields in the text index, you can also assign weights to each of the fields in the index.
Text indexes on array fields are not supported by Amazon DocumentDB and even though you can use up to 30 fields in the compound text index, only three fields can be assigned a weight.

```
IndexModel textIndex = new IndexModel(
    new Document()
    .append("name", "text")
    .append("description", "text")
    .append("cuisine", "text"),
    new IndexOptions()
    .name("restaurant_text_idx")
    .weights(new Document()
        .append("name", 10) // Restaurant name gets highest weight
        .append("description", 5) // Description get medium weight
        .append("cuisine", 2) // Cuisine type gets low weight
    ));

collection.createIndex(textIndex.getKeys(), textIndex.getOptions());
```

**Create an index using `runCommand()`**

Amazon DocumentDB supports parallel index creation to decrease the time it takes to create indexes.
Parallel indexing uses multiple concurrent workers.
The default workers used for index creation is two.
This [blog post](https://aws.amazon.com/blogs/database/unlock-the-power-of-parallel-indexing-in-amazon-documentdb/ "https://aws.amazon.com/blogs/database/unlock-the-power-of-parallel-indexing-in-amazon-documentdb/") provides an in-depth discussion on parallel indexing.
Currently, MongDB Java drivers do not support specifying the worker option when you are using `createIndex()` or `createIndexes()` and therefore the only way to specify workers is through the `runCommand`.
The following code example demonstrates how to use `runCommand` to create an index that increase the worker to four:

```
Document command = new Document("createIndexes", "Restaurants")
    .append("indexes", Arrays.asList(
        new Document("key", new Document("name", 1))
        .append("name", "restaurant_name_idx")
        .append("workers", 4) // Specify number of workers
    ));

Document commendResult = connectedDB.runCommand(command);
```

## Dropping indexes

The MongoDB Java driver provides multiple methods to drop indexes, catering to different scenarios and your preferences.
You can drop indexes by name, by key specification, or drop all indexes at once.
The methods `dropIndex()` and `dropIndexes()` can be invoked on a collection object to drop an index.
When dropping an index by name, you should ensure they use the correct index name which may not always be intuitive, especially for compound or auto-generated indexes.
Attempting to drop a non-existent index will result in a [`MongoCommandException`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/MongoCommandException.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/MongoCommandException.html").
The `default _id` index cannot be dropped as it ensures document uniqueness within the collection.

The following code example shows demonstrates how to drop an index by providing field name where the index is created or by deleting all the indexes:

```
String indexName = "unique_restaurantId_idx";
Document keys = new Document("cuisine", 1);
// Drop index by name
collection.dropIndex(indexName);

// Drop index by keys
collection.dropIndex(keys);

// Drop all indexes
collection.dropIndexes();
```

When dropping indexes using multiple keys, make sure there is a compound index containing all the keys specified and the order of the keys is correct.
The above index creation example code shows a compound key on "cuisine" and features.
If you try to drop that compound key but the order is not what was used for creation, then a MongoCommnadException error occurs as follows:

```
Document keys = new Document("features", 1)
    .append("cuisine", 1);
try {
    // Drop index by keys
    collection.dropIndex(keys);
    System.out.println("Successfully dropped index with keys: " + keys.toJson());

} catch (MongoCommandException commErr) {
    System.out.println("Error dropping index: " + commErr.getErrorMessage());
    throw new RuntimeException("MongoCommandException was thrown while dropping index", commErr);
}
```

The following error is displayed:

```
**`Error dropping index: Cannot drop index: index not found.`**
`Tests run: 3, Failures: 1, Errors: 0, Skipped: 0, Time elapsed: 0.819 sec <<< FAILURE!
com.amazon.docdb.guide.DocDBGuideTest.testindexGuide() Time elapsed: 0.817 sec <<< FAILURE!
org.opentest4j.AssertionFailedError: Unexpected exception thrown: java.lang.RuntimeException: MongoCommandException was thrown while dropping index`
```

## Determining index selection and providing index hint

Working with the explain functionality in Amazon DocumentDB is crucial for you to understand query performance and index usage.
When executing a query, you can append the `explain()` method to obtain detailed information about the query plan, including which indexes, if any, are being used.
The `explain()` output provides insights into the query execution stages, the number of documents examined, and the time taken for each stage.
This information is invaluable for identifying whether a particular index is being used effectively or if the query could benefit from a different index structure.

The `explain()` method can be chained with the `find()` method.
The `explain()` method can take an optional [`ExplainVerbosity`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/ExplainVerbosity.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/ExplainVerbosity.html") enum that determines the level of verbosity that is returned by `explain()`.
At this time, only the `EXECUTION_STATS` and `QUERY_PLANNER` enumerators are supported by DocumentDB.
The following code example shows how to get query planner for a specific query:

```
// Query we want to analyze
Document query = new Document()
    .append("cuisine", "Thai")
    .append("rating.average", new Document("$gte", 4.0));


Document allPlansExplain = collection.find(query).explain(ExplainVerbosity.QUERY_PLANNER);
System.out.println("All Plans Explain:\n" + allPlansExplain.toJson());
```

The following JSON document is returned for the query planner verbosity level:

```
{
  "queryPlanner": {
    "plannerVersion": 1,
    "namespace": "ProgGuideData.Restaurants",
    "winningPlan": {
      "stage": "IXSCAN",
      "indexName": "cuisine_idx",
      "direction": "forward"
    }
  },
  "serverInfo": {
    "host": "guidecluster3",
    "port": 27017,
    "version": "5.0.0"
  },
  "ok": 1,
  "operationTime": {
    "$timestamp": {
      "t": 1739221668,
      "i": 1
    }
  }
}
```

You have several options to influence or force Amazon DocumentDB to use a specific index.
The `hint()` and `hintString()` methods allow you to override the query optimizer's default index selection behavior by explicitly specifying which index should be used for a query.
While DocumentDB's query optimizer generally makes good choices for index selection, there are scenarios where forcing a specific index through `hint()` or `hintString()` can be beneficial, such as when dealing with skewed data, or testing index performance.

The following code example forces the use of compound index “cuisine_features_idx” for the same query that was run in the above code:

```
// Query we want to analyze
Document query = new Document()
    .append("cuisine", "Thai")
    .append("rating.average", new Document("$gte", 4.0));

List < Document > queryDocs = new ArrayList < > ();
collection.find(query).hintString("cuisine_features_idx").forEach(doc - > queryDocs.add(doc));
```
