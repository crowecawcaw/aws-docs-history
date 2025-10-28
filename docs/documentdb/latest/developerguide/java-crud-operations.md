# Performing CRUD operations in Amazon DocumentDB with Java

This section discusses performing CRUD (create, read, update, delete) operation in Amazon DocumentDB using MongoDB Java drivers.

###### Topics

- [Creating and inserting documents in a DocumentDB collection](#creating-inserting "#creating-inserting")
- [Reading and retrieving data from a DocumentDB collection](#reading-retrieving "#reading-retrieving")
- [Updating existing documents in a DocumentDB collection](#updating-documents "#updating-documents")
- [Removing documents from a DocumentDB collection](#deleting-documents "#deleting-documents")
- [Error handling with retry logic](#error-handling "#error-handling")

## Creating and inserting documents in a DocumentDB collection

Inserting documents into Amazon DocumentDB allows you to add new data to your collections.
There are several ways to perform insertions, depending on your needs and the volume of data you're working with.
The most basic method for inserting an individual document to the collection is `insertOne()`.
For inserting multiple documents at once, you can use the `insertMany()` method, which allows you to add an array of documents in a single operation.
Another method for inserting many documents in a DocumentDB collection is `bulkWrite()`.
In this guide, we discuss all of these methods for creating documents in a DocumentDB collection.

**`insertOne()`**

Let's begin by examining how to insert an individual document into an Amazon DocumentDBB collection.
Inserting a single document is accomplished by using the `insertOne()` method.
This method takes a [BsonDocument](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/bson/org/bson/BsonDocument.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/bson/org/bson/BsonDocument.html") for insertion and returns an [`InsertOneResult`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/result/InsertOneResult.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/result/InsertOneResult.html") object that can be used to get the object id of the new inserted document.
The example code below shows inserting one restaurant document into the collection:

```
Document article = new Document()
    .append("restaurantId", "REST-21G145")
    .append("name", "Future-proofed Intelligent Bronze Hat")
    .append("cuisine", "International")
    .append("rating", new Document()
        .append("average", 1.8)
        .append("totalReviews", 267))
    .append("features", Arrays.asList("Outdoor Seating", "Live Music"));

try {
    InsertOneResult result = collection.insertOne(article);
    System.out.println("Inserted document with the following id: " + result.getInsertedId());
} catch (MongoWriteException e) {
    // Handle duplicate key or other write errors
    System.err.println("Failed to insert document: " + e.getMessage());
    throw e;
} catch (MongoException e) {
    // Handle other MongoDB errors
    System.err.println("MongoDB error: " + e.getMessage());
    throw e;
}
```

When using `insertOne()`, make sure to include appropriate error handling.
For instance, in the above code, “`restaurantId`” has a unique index and therefore running this code again will raise the following `MongoWriteException`:

```
`Failed to insert document: Write operation error on server docdbCluster.docdb.amazonaws.com:27017.
Write error: WriteError{code=11000, message='E11000 duplicate key error collection: Restaurants index: restaurantId_1', details={}}.`
```

**insertMany()**

The primary methods used for inserting many document into a collection are insertMany() and `bulkWrite()`.

The `insertMany()` method is the simplest way to insert multiple documents in a single operation.
It accepts a list of documents and inserts them into the collection.
This method is ideal when you're inserting a batch of new documents that are independent of each other and don't require any special processing or mixed operations.
The following code shows reading JSON documents from a file and inserting them into the collection.
The `insertMany()` function returns an [`InsertManyResult`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/result/InsertManyResult.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/result/InsertManyResult.html")`InsertManyResult` object that can be used to get the IDs of all the inserted documents.

```
// Read JSON file content
String content = new String(Files.readAllBytes(Paths.get(jsonFileName)));
JSONArray jsonArray = new JSONArray(content);

// Convert JSON articles to Documents
List < Document > restaurants = new ArrayList < > ();
for (int i = 0; i < jsonArray.length(); i++) {
    JSONObject jsonObject = jsonArray.getJSONObject(i);
    Document doc = Document.parse(jsonObject.toString());
    restaurants.add(doc);
}
//insert documents in collection
InsertManyResult result = collection.insertMany(restaurants);

System.out.println("Count of inserted documents: " + result.getInsertedIds().size());
```

**[`bulkWrite()`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/bulk/package-summary.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/bulk/package-summary.html")**

The `bulkWrite()` method allows to perform multiple write operations (insert, update, delete) in a single batch.
You can use `bulkWrite()` when you need to perform different types of operations in a single batch, such as inserting some documents while updating others.
`bulkWrite()` support two types of batch write, ordered and unordered:

- _Ordered operations_ — (default) Amazon DocumentDB processes the write operations sequentially, and stops at the first error it encounters.
  This is useful when the order of operations matters, such as when later operations depend on earlier ones.
  However, ordered operations are generally slower then unordered operations.
  With ordered operations, you must address the case where the batch stops at the first error, potentially leaving some operations unprocessed.
- _Unordered operations_ — Allows Amazon DocumentDB to process inserts as a single execution in the database.
  If an error occurs with one document, the operation continues with the remaining documents.
  This is particularly useful when you're inserting large amounts of data and can tolerate some failures, such as during data migration or bulk imports where some documents might fail due to duplicate keys.
  With unordered operations, you must address partial success scenarios where some operations succeed while others fail.

When working with the `bulkWrite()` method, there are some essential classes that are required.
First, the [`WriteModel`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/WriteModel.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/WriteModel.html") class serves as the base class for all write operations and with specific implementations like
[`InsertOneModel`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/InsertOneModel.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/InsertOneModel.html"),
[`UpdateOneModel`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/UpdateOneModel.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/UpdateOneModel.html"),
[`UpdateManyModel`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/UpdateManyModel.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/UpdateManyModel.html"),
[`DeleteOneModel`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/DeleteOneModel.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/DeleteOneModel.html"),
and [`DeleteManyModel`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/DeleteManyModel.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/DeleteManyModel.html") handling different types of operations.

The [`BulkWriteOptions`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/BulkWriteOptions.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/BulkWriteOptions.html") class is necessary for configuring the behavior of bulk operations, such as setting ordered/unordered execution or bypassing document validation.
The [`BulkWriteResult`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/bulk/BulkWriteResult.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/bulk/BulkWriteResult.html") class provides detailed information about the execution results, including counts of inserted, updated, and deleted documents.

For error handling, the [`MongoBulkWriteException`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/MongoBulkWriteException.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/MongoBulkWriteException.html") class is crucial as it contains information about any failures during the bulk operation, while the
[`BulkWriteError`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/bulk/BulkWriteError.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/bulk/BulkWriteError.html") class provides specific details about individual operation failures.
The following code shows an example of inserting a list of documents, as well as updating and deleting a single document, all within the execution of single `bulkWrite()` method call.
The code also shows how to work with [`BulkWriteOptions`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/BulkWriteOptions.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/BulkWriteOptions.html") and
[`BulkWriteResult`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/bulk/BulkWriteResult.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/bulk/BulkWriteResult.html"), as well as proper error handling of the `bulkWrite()` operation.

```
List < WriteModel < Document >> bulkOperations = new ArrayList < > ();
// get list of 10 documents representing 10 restaurants
List < Document > restaurantsToInsert = getSampleData();

for (Document doc: restaurantsToInsert) {
    bulkOperations.add(new InsertOneModel < > (doc));
}
// Update operation
bulkOperations.add(new UpdateOneModel < > (
    new Document("restaurantId", "REST-Y2E9H5"),
    new Document("", new Document("stats.likes", 20))
    .append("", new Document("rating.average", 4.5))));
// Delete operation
bulkOperations.add(new DeleteOneModel < > (new Document("restaurantId", "REST-D2L431")));

// Perform bulkWrite operation
try {
    BulkWriteOptions options = new BulkWriteOptions()
        .ordered(false); // Allow unordered inserts

    BulkWriteResult result = collection.bulkWrite(bulkOperations, options);

    System.out.println("Inserted: " + result.getInsertedCount());
    System.out.println("Updated: " + result.getModifiedCount());
    System.out.println("Deleted: " + result.getDeletedCount());
} catch (MongoBulkWriteException e) {
    System.err.println("Bulk write error occurred: " + e.getMessage());
    // Log individual write errors
    for (BulkWriteError error: e.getWriteErrors()) {
        System.err.printf("Error at index %d: %s (Code: %d)%n", error.getIndex(), error.getMessage(),
            error.getCode());

        // Log the problematic document
        Document errorDoc = new Document(error.getDetails());
        if (errorDoc != null) {
            System.err.println("Problematic document: " + errorDoc);
        }
    }
} catch (Exception e) {
    System.err.println("Error during bulkWrite: " + e.getMessage());
}
```

**Retryable writes**

Unlike MongoDB, Amazon DocumentDB doesn't support retryable writes.
As a result, you must implement custom retry logic in their applications, particularly for handling network issues or temporary service unavailability.
A well-implemented retry strategy, typically, involves increasing the delay between retry attempts and limiting the total number of retries.
See [Error handling with retry logic](#error-handling "#error-handling") below for a code sample of building retry logic with error handling.

## Reading and retrieving data from a DocumentDB collection

Querying documents in Amazon DocumentDB revolves around several key components that allow you to precisely retrieve and manipulate data.
The [`find()`](<https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoCollection.html#find()> "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoCollection.html#find()") method is the fundamental querying APIs in MongoDB Java drivers.
It allows for complex data retrieval with numerous options for filtering, sorting, and projecting results.
Besides the `find()` method, [`Filters`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/Filters.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/Filters.html") and
[`FindIterable`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/FindIterable.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/FindIterable.html") are two other fundamental components that provide the building blocks for query operations in MongoDB Java drivers.

The `Filters` class is a utility class in the MongoDB Java driver that provides a fluent API for constructing query filters.
This class offers static factory methods that create instances of `Bson` objects representing various query conditions.
The most commonly used methods include `eq()` for equality comparisons, `gt()`, `lt()`, `gte()`, and `lte()` for numeric comparisons, `and()` and `or()` for combining multiple conditions, `in()` and `nin()` for array membership tests, and `regex()` for pattern matching.
The class is designed to be type-safe and provides better compile-time checking compared to raw document-based queries, making it the preferred approach for constructing DocumentDB queries in Java applications.
Error handling is robust, with clear exceptions thrown for invalid filter constructions.

`FindIterable` is a specialized interface designed to handle the result of the `find()` method.
It provides a rich set of methods for refining and controlling query execution, offering a fluent API for method chaining.
The interface includes essential query modification methods such as `limit()` for restricting the number of returned documents, `skip()` for pagination, `sort()` for ordering results, `projection()` for selecting specific fields, and `hint()` for index selection.
The batch, skip, and limit operations in `FindIterable` are essential pagination and data management tools that help control how documents are retrieved and processed from the database.

Batching (`batchSize`) controls how many documents DocumentDB returns to the client in a single network round trip.
When you set a batch size, DocumentDB doesn't return all matching documents at once but instead returns them in groups of the specified batch size.

Skip allows you to offset the starting point of your results, essentially telling DocumentDB to skip over a specified number of documents before beginning to return matches.
For example, `skip(20)` will bypass the first 20 matching documents.
This is commonly used in pagination scenarios where you want to retrieve subsequent pages of results.

Limit restricts the total number of documents that can be returned from a query.
When you specify `limit(n)`, DocumentDB will stop returning documents after it has returned 'n' documents, even if there are more matches in the database.

`FindIterable` supports both iterator and cursor patterns when retrieving documents from Amazon DocumentDB.
The benefit of using `FindIterable` as iterator is that it allows lazy loading of documents and only fetches documents when requested by the application.
Another benefit of using iterator is that you are not responsible for maintaining the connection to the cluster and thus no explicit closing of the connection is required.

`FindIterable` also provide support for [`MongoCursor`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoCursor.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoCursor.html") which allows cursor patterns to be used when working with Amazon DocumentDB queries.
`MongoCursor` is a MongoDB Java driver-specific implementation that provides control over database operations and resource management.
It implements the `AutoCloseable` interface, allowing for explicit resource management through try-with-resources blocks, which is crucial for properly closing database connections and freeing server resources.
By default, the cursor times out in 10 minutes and DocumentDB does not give you the option of changing this time out behavior.
When working with batched data, make sure to retrieve the next batch of data before the cursor times out.
One key consideration when using `MongoCursor` is that it requires explicit closing to prevent resource leaks.

In this section, several examples are presented for `find()`, `Filters` and `FindIterable`.

The following code example shows how to use `find()` to retrieve a single document using its “restaurantId” field:

```
Document filter = new Document("restaurantId", "REST-21G145");
Document result = collection.find(filter).first();
```

Even though using `Filters` allows for better compile time error checking, the java driver also allows you to specify a `Bson` filter directly in the `find()` method.
The following example code passes `Bson` document to `find()`:

```
result = collection.find(new Document("$and", Arrays.asList(
    new Document("rating.totalReviews", new Document("$gt", 1000)),
    new Document("priceRange", "$$"))))
```

The next example code shows several examples of using the `Filters` class with `find()`:

```
FindIterable < Document > results;

// Exact match
results = collection.find(Filters.eq("name", "Thai Curry Palace"));

// Not equal
results = collection.find(Filters.ne("cuisine", "Thai"));

// find an element in an array
results = collection.find(Filters.in("features", Arrays.asList("Private Dining")));

// Greater than
results = collection.find(Filters.gt("rating.average", 3.5));

// Between (inclusive)
results = collection.find(Filters.and(
    Filters.gte("rating.totalReviews", 100),
    Filters.lte("rating.totalReviews", 200)));
// AND
results = collection.find(Filters.and(
    Filters.eq("cuisine", "Thai"),
    Filters.gt("rating.average", 4.5)));

// OR
results = collection.find(Filters.or(
    Filters.eq("cuisine", "Thai"),
    Filters.eq("cuisine", "American")));


// All document where the Field exists
results = collection.find(Filters.exists("michelin"));

// Regex
results = collection.find(Filters.regex("name", Pattern.compile("Curry", Pattern.CASE_INSENSITIVE)));

// Find all document where the array contain the list of value regardless of its order
results = collection.find(Filters.all("features", Arrays.asList("Private Dining", "Parking")));

// Array size
results = collection.find(Filters.size("features", 4));
```

The following example shows how to chain the operations of `sort()`, `skip()`, `limit()`, and `batchSize()` on a `FindIterable` object.
The order of how these operations is provided will influence the performance of your query.
As a best practice, the order of these operations should be `sort()`, `projection()`, `skip()`, `limit()` and `batchSize()`.

```
FindIterable < Document > results = collection.find(Filters.gt("rating.totalReviews", 1000))
    // Sorting
    .sort(Sorts.orderBy(
        Sorts.descending("address.city"),
        Sorts.ascending("cuisine")))
    // Field selection
    .projection(Projections.fields(
        Projections.include("name", "cuisine", "priceRange"),
        Projections.excludeId()))

    // Pagination
    .skip(20)
    .limit(10)
    .batchSize(2);
```

The following example code shows creating an iterator on `FindIterable`.
It uses Java’s `forEach` construct to traverse through the result set.

```
collection.find(Filters.eq("cuisine", "American")).forEach(doc -> System.out.println(doc.toJson()));
```

In the last `find()` code example, it shows how to use `cursor()` for document retrieval.
It creates the cursor in the try block which ensures that the cursor will get closed when the code exits the try block.

```
try (MongoCursor < Document > cursor = collection.find(Filters.eq("cuisine", "American"))
    .batchSize(25)
    .cursor()) {
    while (cursor.hasNext()) {
        Document doc = cursor.next();
        System.out.println(doc.toJson());
    }
} // Cursor automatically closed
```

## Updating existing documents in a DocumentDB collection

Amazon DocumentDB provides flexible and powerful mechanisms for modifying existing documents and inserting new ones when they don't exist.
The MongoDB Java driver offers several methods for updates: `updateOne()` for single document updates, `updateMany()` for multiple document updates, and `replaceOne()` for complete document replacement.
Beside these three methods, [`Updates`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/Updates.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/Updates.html"),
[`UpdateOptions`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/UpdateOptions.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/UpdateOptions.html"), and
[`UpdateResult`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/result/UpdateResult.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/result/UpdateResult.html") are other fundamental components that provide the building blocks for update operations in MongoDB Java drivers.

The `Updates` class in the MongoDB Java driver is a utility class that provides static factory methods for creating update operators.
It serves as the primary builder for constructing update operations in a type-safe and readable manner.
Basic methods like `set()`, `unset()`, and `inc()` allows direct modification of the documents.
The power of this class becomes evident when combining multiple operations using the `Updates.combine()` method which allows multiple update operations to be executed atomically, ensuring data consistency.

`UpdateOptions` is a powerful configuration class in MongoDB's Java driver that provides essential customization capabilities for document update operations.
Two important aspects of this class is providing upsert and array filter support for update operations.
The upsert feature, enabled through `upsert(true)`, allows for the creation of new documents when no matching documents are found during an update operation.
Through `arrayFilters()`, the update operation can precisely update array elements that meet specific criteria.

`UpdateResult` in MongoDB's Java driver provides the feedback mechanism detailing the outcome of an update operation.
This class encapsulates three key metrics: the number of documents matched by the update criteria (`matchedCount`), the number of documents actually modified (`modifiedCount`), and information about any upserted documents (`upsertedId`).
Understanding these metrics is essential for proper error handling, verification of update operations, and maintaining data consistency in applications.

### Update and replace a single document

In DocumentDB, updating a single document can be accomplished using the updateOne() method.
This method take a filter parameter, usually provided by the `Filters` class, to identify the document to be updated, an `Updat`e parameter that determines which field(s) to be updated, and an optional `UpdateOptions` parameter to set different options for the update.
Using the `updateOne()` method will only update the first document that matches the selection criteria.
The following example code updates a single field of one document:

```
collection.updateOne(Filters.eq("restaurantId", "REST-Y2E9H5"),
    Updates.set("name", "Amazing Japanese sushi"));
```

To update multiple fields in one document, use `updateOne()` with `Update.combine()` as shown in the following example.
This example also shows how to add an item to an array in the document.

```
List<Bson> updates = new ArrayList<>();
// Basic field updates
updates.add(Updates.set("name", "Shanghai Best"));
// Array operations
updates.add(Updates.addEachToSet("features", Arrays.asList("Live Music")));
// Counter updates
updates.add(Updates.inc("rating.totalReviews", 10));
// Combine all updates
Bson combinedUpdates = Updates.combine(updates);
// Execute automic update with one call
collection.updateOne(Filters.eq("restaurantId","REST-1J83NH"), combinedUpdates);
```

The following code example demonstrates how to update a document in the database.
If the specified document doesn't exist, the operation will automatically insert it as a new document instead.
This code also shows how to use the metrics available via the `UpdateResult` object.

```
Bson filter = Filters.eq("restaurantId", "REST-0Y9GL0");
Bson update = Updates.set("cuisine", "Indian");
// Upsert operation
UpdateOptions options = new UpdateOptions().upsert(true);
UpdateResult result = collection.updateOne(filter, update, options);

if (result.getUpsertedId() != null) {
   	System.out.println("Inserted document with _id: " + result.getUpsertedId());
} else {
    	System.out.println("Updated " + result.getModifiedCount() + " document(s)");
}
```

The following code example demonstrates how to completely replace an existing document with a new document using the `replaceOne()` method, rather than updating individual fields.
The `replaceOne()` method overwrites the entire document, preserving only the `_id` field of the original.
If multiple documents match the filter criteria, only the first encountered document is replaced.

```
Document newDocument = new Document()
                .append("restaurantId", "REST-0Y9GL0")
                .append("name", "Bhiryani Adda")
                .append("cuisine", "Indian")
                .append("rating", new Document()
                        .append("average", 4.8)
                        .append("totalReviews", 267))
                .append("features", Arrays.asList("Outdoor Seating", "Live Music"));

UpdateResult result = collection.replaceOne(
                    Filters.eq("restaurantId", "REST-0Y9GL0"),
                    newDocument);
System.out.printf("Modified %d document%n", result.getModifiedCount());
```

### Update multiple documents

There are two ways to update multiple document in a collection simultaneously. You can use the `updateMany()` method or use the [`UpdateManyModel`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/UpdateManyModel.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/UpdateManyModel.html") with the `bulkWrite()` method.
The `updateMany()` method uses a filter parameter to select documents for update, the `Update` parameter to identify the fields to be updated, and an optional `UpdateOptions` parameter to specify update options.

The following example code demonstrates the usage of the `updateMany()` method:

```
Bson filter = Filters.and(
    Filters.in("features", Arrays.asList("Private Dining")),
    Filters.eq("cuisine", "Thai"));
UpdateResult result1 = collection.updateMany(filter, Updates.set("priceRange", "$$$"));
```

The following example code demonstrates the `bulkWrite()` method using the same update:

```
BulkWriteOptions options = new BulkWriteOptions().ordered(false);
List < WriteModel < Document >> updates = new ArrayList < > ();
Bson filter = Filters.and(
    Filters.in("features", Arrays.asList("Private Dining")),
    Filters.eq("cuisine", "Indian"));
Bson updateField = Updates.set("priceRange", "$$$");
updates.add(new UpdateManyModel < > (filter, updateField));
BulkWriteResult result = collection.bulkWrite(updates, options);
System.out.printf("Modified %d document%n", result.getModifiedCount());
```

## Removing documents from a DocumentDB collection

The MongoDB Java driver offers `deleteOne()` for removing a single document and `deleteMany()` for removing multiple documents that match specific criteria.
Just like update, delete operation can also be used with the `bulkWrite()` method.
Both `deleteOne()` and `deleteMany()` return a [`DeleteResult`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/result/DeleteResult.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/result/DeleteResult.html") object that provides information about the operation's outcome, including the count of documents deleted.
The following is an example of using `deleteMany()` to remove multiple documents:

```
Bson filter = Filters.and(
    Filters.eq("cuisine", "Thai"),
    Filters.lt("rating.totalReviews", 50));
DeleteResult result = collection.deleteMany(filter);
System.out.printf("Deleted %d document%n", result.getDeletedCount());
```

## Error handling with retry logic

A robust error handling strategy for Amazon DocumentDB should implement categorization of errors into retryable (like network timeouts, connection issues) and non-retryable (like authentication failures, invalid queries).
For operation failures due of errors that should be retried, it should implement a time delay between each retry as well as max retry attempts.
The CRUD operations should be in a try-catch block that catches [`MongoException`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/MongoException.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/MongoException.html") and its subclasses.
Additionally, it should include monitoring and logging of errors for operational visibility.
The following is sample code that shows how to implement retry error handling:

```
int MAX_RETRIES = 3;
int INITIAL_DELAY_MS = 1000;
int retryCount = 0;

while (true) {
    try {
        crud_operation(); //perform crud that will throw MongoException or one of its subclass
        break;
    } catch (MongoException e) {
        if (retryCount < MAX_RETRIES) {
            retryCount++;
            long delayMs = INITIAL_DELAY_MS * (long) Math.pow(2, retryCount - 1);
            try {
                TimeUnit.MILLISECONDS.sleep(delayMs);
            } catch (InterruptedException t) {
                Thread.currentThread().interrupt();
                throw new RuntimeException("Retry interrupted", t);
            }
            continue;
        } else
            throw new RuntimeException("Crud operation failed", e);
    }
}
```
