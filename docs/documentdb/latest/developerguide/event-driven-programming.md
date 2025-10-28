# Event-driven programming with Amazon DocumentDB and Java

Event-driven programming in the context of Amazon DocumentDB represents a powerful architectural pattern where database changes serve as the primary event generators that trigger subsequent business logic and processes.
When records are inserted, updated, or deleted in a DocumentDB collection, these changes act as events that automatically initiate various downstream processes, notifications, or data synchronization tasks.
This pattern is particularly valuable in modern distributed systems where multiple applications or services need to react to data changes in real-time.
The primary mechanism of implementing event-driven programming in DocumentDB is by change streams.

###### Note

This guide assumes you have enabled change streams on a collection that you are working with.
See [Using change streams with Amazon DocumentDB](change_streams.md "change_streams.md") to learn how to enable change streams on the collection.

**Working with change streams from the Java application**

The `watch()` method in MongoDB’s Java driver is the primary mechanism for monitoring real-time data changes in Amazon DocumentDB.
The `watch()` method can be called on by [`MongoClient`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoClient.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoClient.html"), [`MongoDatabase`](<https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoDatabase.html#watch(com.mongodb.client.ClientSession,java.lang.Class)> "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoDatabase.html#watch(com.mongodb.client.ClientSession,java.lang.Class)"), and [`MongoCollection`](<https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoCollection.html#watch()> "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoCollection.html#watch()") objects.

The `watch()` method returns an instance of [`ChangeStreamIterable`](<https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/ChangeStreamIterable.html#startAtOperationTime(org.bson.BsonTimestamp)> "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/ChangeStreamIterable.html#startAtOperationTime(org.bson.BsonTimestamp)") that supports various configuration options, including full document lookup for updates, providing resume tokens and timestamp for reliability, and pipeline aggregation stages for filtering changes.

[`ChangeStreamIterable`](<https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/ChangeStreamIterable.html#startAtOperationTime(org.bson.BsonTimestamp)> "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/ChangeStreamIterable.html#startAtOperationTime(org.bson.BsonTimestamp)") implements the core Java interface `Iterable` and can be used with `forEach()`.
To capture events using `forEach()`, pass in a callback function to `forEach()` that processes the changed event.
The following code snippet shows how to open a change streams on a collection to start change event monitoring:

```
ChangeStreamIterable < Document > iterator = collection.watch();
iterator.forEach(event - > {
    System.out.println("Received a change: " + event);
});
```

Another way of traversing through all the change events is by opening a cursor that maintains a connection to the cluster and continuously receives new change events as they occur.
To obtain a change streams cursor, use the `cursor()` method of [`ChangeStreamIterable`](<https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/ChangeStreamIterable.html#startAtOperationTime(org.bson.BsonTimestamp)> "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/ChangeStreamIterable.html#startAtOperationTime(org.bson.BsonTimestamp)") object.
The following code example shows how to monitor change events using cursor:

```
try (MongoChangeStreamCursor < ChangeStreamDocument < Document >> cursor = collection.watch().cursor()) {
    System.out.println(cursor.tryNext());
}
```

As a best practice, either create the [`MongoChangeStreamCursor`](<https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoChangeStreamCursor.html#getResumeToken()> "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoChangeStreamCursor.html#getResumeToken()") in a try-with-resource statement or manually close the cursor.
Calling the `cursor()` method on [`ChangeStreamIterable`](<https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/ChangeStreamIterable.html#startAtOperationTime(org.bson.BsonTimestamp)> "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/ChangeStreamIterable.html#startAtOperationTime(org.bson.BsonTimestamp)") returns a `MongoChangeStreamCursor` that is created over a [`ChangeStreamDocument`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/changestream/ChangeStreamDocument.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/changestream/ChangeStreamDocument.html") object.

The [`ChangeStreamDocument`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/changestream/ChangeStreamDocument.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/changestream/ChangeStreamDocument.html") class is a crucial component that represents individual change events in the stream.
It contains detailed information about each modification, including the operation type (insert, update, delete, replace), the document key, namespace information, and the full document content when available.
The class provides methods to access various aspects of the change event, such as `getOperationType()` to determine the type of change, `getFullDocument()` to access the complete document state, and `getDocumentKey()` to identify the modified document.

The [`ChangeStreamDocument`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/changestream/ChangeStreamDocument.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/changestream/ChangeStreamDocument.html") object provides two important pieces of information, a resume token and time of the change event.

Resume tokens and time-based operations in DocumentDB change streams provide crucial mechanisms for maintaining continuity and managing historical data access.
A resume token is a unique identifier generated for each change event, serving as a bookmark that allows applications to restart change stream processing from a specific point after disconnections or failures.
When a change stream cursor is created, it can use a previously stored resume token through the `resumeAfter()` option, enabling the stream to continue from where it left off rather than starting from the beginning or losing events.

Time-based operations in change streams offer different approaches to manage the starting point of change event monitoring.
The `startAtOperationTime()` option allows you to begin watching changes that occurred at or after a specific timestamp.
These time-based features are particularly valuable in scenarios requiring historical data processing, point-in-time recovery, or synchronization between systems.

The following code example retrieves the event associated with the insert document, captures it’s resume token, and then provides that token to start monitoring for events after the insert event.
The event is associated with the update event, then gets the cluster time when the update happened and uses that timestamp as a starting point for further processing.

```
BsonDocument resumeToken;
BsonTimestamp resumeTime;

try (MongoChangeStreamCursor < ChangeStreamDocument < Document >> cursor = collection.watch().cursor()) {
    System.out.println("****************** Insert Document *******************");
    ChangeStreamDocument < Document > insertChange = cursor.tryNext();
    resumeToken = insertChange.getResumeToken();
    printJson(cursor.tryNext());
}
try (MongoChangeStreamCursor < ChangeStreamDocument < Document >> cursor = collection.watch()
    .resumeAfter(resumeToken)
    .cursor()) {
    System.out.println("****************** Update Document *******************");
    ChangeStreamDocument < Document > insertChange = cursor.tryNext();
    resumeTime = insertChange.getClusterTime();
    printJson(cursor.tryNext());
}
try (MongoChangeStreamCursor < ChangeStreamDocument < Document >> cursor = collection.watch()
    .startAtOperationTime(resumeTime)
    .cursor()) {
    System.out.println("****************** Delete Document *******************");
    printJson(cursor.tryNext());
  }
```

By default, the update change event does not include the full document and it only include the changes that were made.
If you need to access the complete document that was updated, you can call the `fullDocument()` method on the [`ChangeStreamIterable`](<https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/ChangeStreamIterable.html#startAtOperationTime(org.bson.BsonTimestamp)> "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/ChangeStreamIterable.html#startAtOperationTime(org.bson.BsonTimestamp)") object.
Keep in mind that when you ask for a full document to be returned for an update event, it returns the document that exists at the time the call to change streams is made.

This method takes a [`FullDocument`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/changestream/FullDocument.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/client/model/changestream/FullDocument.html") enum as a parameter.
Currently, Amazon DocumentDB only support DEFAULT and `UPDATE_LOOKUP` values.
The following code snippet shows how to ask for full document for update events when starting to watch for changes:

```
try (MongoChangeStreamCursor < ChangeStreamDocument < Document >> cursor = collection.watch().fullDocument(FullDocument.UPDATE_LOOKUP).cursor())
```
