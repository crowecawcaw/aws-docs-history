# Working with items: Java

You can use the AWS SDK for Java Document API to perform typical create, read, update, and delete
(CRUD) operations on Amazon DynamoDB items in a table.

###### Note

The SDK for Java also provides an object persistence model, allowing you to map your client-side
classes to DynamoDB tables. This approach can reduce the amount of code that you have to write.
For more information, see [Java 1.x: DynamoDBMapper](DynamoDBMapper.md "DynamoDBMapper.md").

This section contains Java examples to perform several Java Document API item actions and
several complete working examples.

###### Topics

- [Putting an item](#PutDocumentAPIJava "#PutDocumentAPIJava")
- [Getting an item](#JavaDocumentAPIGetItem "#JavaDocumentAPIGetItem")
- [Batch write: Putting and deleting multiple
  items](#BatchWriteDocumentAPIJava "#BatchWriteDocumentAPIJava")
- [Batch get: Getting multiple items](#JavaDocumentAPIBatchGetItem "#JavaDocumentAPIBatchGetItem")
- [Updating an item](#JavaDocumentAPIItemUpdate "#JavaDocumentAPIItemUpdate")
- [Deleting an item](#DeleteMidLevelJava "#DeleteMidLevelJava")
- [Example: CRUD operations using the AWS SDK for Java
  document API](JavaDocumentAPICRUDExample.md "JavaDocumentAPICRUDExample.md")
- [Example: Batch operations using AWS SDK for Java
  document API](batch-operation-document-api-java.md "batch-operation-document-api-java.md")
- [Example: Handling binary type attributes
  using the AWS SDK for Java document API](JavaDocumentAPIBinaryTypeExample.md "JavaDocumentAPIBinaryTypeExample.md")

## Putting an item

The `putItem` method stores an item in a table. If the item exists, it replaces
the entire item. Instead of replacing the entire item, if you want to update only specific
attributes, you can use the `updateItem` method. For more information, see [Updating an item](#JavaDocumentAPIItemUpdate "#JavaDocumentAPIItemUpdate").

Java v2

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;
import software.amazon.awssdk.services.dynamodb.model.PutItemRequest;
import software.amazon.awssdk.services.dynamodb.model.PutItemResponse;
import software.amazon.awssdk.services.dynamodb.model.ResourceNotFoundException;
import java.util.HashMap;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 *
 * To place items into an Amazon DynamoDB table using the AWS SDK for Java V2,
 * its better practice to use the
 * Enhanced Client. See the EnhancedPutItem example.
 */
public class PutItem {
    public static void main(String[] args) {
        final String usage = """

                Usage:
                    <tableName> <key> <keyVal> <albumtitle> <albumtitleval> <awards> <awardsval> <Songtitle> <songtitleval>

                Where:
                    tableName - The Amazon DynamoDB table in which an item is placed (for example, Music3).
                    key - The key used in the Amazon DynamoDB table (for example, Artist).
                    keyval - The key value that represents the item to get (for example, Famous Band).
                    albumTitle - The Album title (for example, AlbumTitle).
                    AlbumTitleValue - The name of the album (for example, Songs About Life ).
                    Awards - The awards column (for example, Awards).
                    AwardVal - The value of the awards (for example, 10).
                    SongTitle - The song title (for example, SongTitle).
                    SongTitleVal - The value of the song title (for example, Happy Day).
                **Warning** This program will  place an item that you specify into a table!
                """;

        if (args.length != 9) {
            System.out.println(usage);
            System.exit(1);
        }

        String tableName = args[0];
        String key = args[1];
        String keyVal = args[2];
        String albumTitle = args[3];
        String albumTitleValue = args[4];
        String awards = args[5];
        String awardVal = args[6];
        String songTitle = args[7];
        String songTitleVal = args[8];

        Region region = Region.US_EAST_1;
        DynamoDbClient ddb = DynamoDbClient.builder()
                .region(region)
                .build();

        putItemInTable(ddb, tableName, key, keyVal, albumTitle, albumTitleValue, awards, awardVal, songTitle,
                songTitleVal);
        System.out.println("Done!");
        ddb.close();
    }

    public static void putItemInTable(DynamoDbClient ddb,
            String tableName,
            String key,
            String keyVal,
            String albumTitle,
            String albumTitleValue,
            String awards,
            String awardVal,
            String songTitle,
            String songTitleVal) {

        HashMap<String, AttributeValue> itemValues = new HashMap<>();
        itemValues.put(key, AttributeValue.builder().s(keyVal).build());
        itemValues.put(songTitle, AttributeValue.builder().s(songTitleVal).build());
        itemValues.put(albumTitle, AttributeValue.builder().s(albumTitleValue).build());
        itemValues.put(awards, AttributeValue.builder().s(awardVal).build());

        PutItemRequest request = PutItemRequest.builder()
                .tableName(tableName)
                .item(itemValues)
                .build();

        try {
            PutItemResponse response = ddb.putItem(request);
            System.out.println(tableName + " was successfully updated. The request id is "
                    + response.responseMetadata().requestId());

        } catch (ResourceNotFoundException e) {
            System.err.format("Error: The Amazon DynamoDB table \"%s\" can't be found.\n", tableName);
            System.err.println("Be sure that it exists and that you've typed its name correctly!");
            System.exit(1);
        } catch (DynamoDbException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
}

```

Java v1
Follow these steps:

1. Create an instance of the `DynamoDB` class.
2. Create an instance of the `Table` class to represent the table you
   want to work with.
3. Create an instance of the `Item` class to represent the new item. You
   must specify the new item's primary key and its attributes.
4. Call the `putItem` method of the `Table` object, using the
   `Item` that you created in the preceding step.

The following Java code example demonstrates the preceding tasks. The code writes a
new item to the `ProductCatalog` table.

###### Example

```
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().build();
DynamoDB dynamoDB = new DynamoDB(client);

Table table = dynamoDB.getTable("ProductCatalog");

// Build a list of related items
List<Number> relatedItems = new ArrayList<Number>();
relatedItems.add(341);
relatedItems.add(472);
relatedItems.add(649);

//Build a map of product pictures
Map<String, String> pictures = new HashMap<String, String>();
pictures.put("FrontView", "http://example.com/products/123_front.jpg");
pictures.put("RearView", "http://example.com/products/123_rear.jpg");
pictures.put("SideView", "http://example.com/products/123_left_side.jpg");

//Build a map of product reviews
Map<String, List<String>> reviews = new HashMap<String, List<String>>();

List<String> fiveStarReviews = new ArrayList<String>();
fiveStarReviews.add("Excellent! Can't recommend it highly enough!  Buy it!");
fiveStarReviews.add("Do yourself a favor and buy this");
reviews.put("FiveStar", fiveStarReviews);

List<String> oneStarReviews = new ArrayList<String>();
oneStarReviews.add("Terrible product!  Do not buy this.");
reviews.put("OneStar", oneStarReviews);

// Build the item
Item item = new Item()
    .withPrimaryKey("Id", 123)
    .withString("Title", "Bicycle 123")
    .withString("Description", "123 description")
    .withString("BicycleType", "Hybrid")
    .withString("Brand", "Brand-Company C")
    .withNumber("Price", 500)
    .withStringSet("Color",  new HashSet<String>(Arrays.asList("Red", "Black")))
    .withString("ProductCategory", "Bicycle")
    .withBoolean("InStock", true)
    .withNull("QuantityOnHand")
    .withList("RelatedItems", relatedItems)
    .withMap("Pictures", pictures)
    .withMap("Reviews", reviews);

// Write the item to the table
PutItemOutcome outcome = table.putItem(item);
```

In the preceding example, the item has attributes that are scalars
(`String`, `Number`, `Boolean`, `Null`),
sets (`String Set`), and document types (`List`,
`Map`).

### Specifying optional parameters

Along with the required parameters, you can also specify optional parameters to the
`putItem` method. For example, the following Java code example uses an optional
parameter to specify a condition for uploading the item. If the condition you specify is not
met, the AWS SDK for Java throws a `ConditionalCheckFailedException`. The code example
specifies the following optional parameters in the `putItem` method:

- A `ConditionExpression` that defines the conditions for the request. The
  code defines the condition that the existing item with the same primary key is replaced
  only if it has an ISBN attribute that equals a specific value.
- A map for `ExpressionAttributeValues` that is used in the condition. In
  this case, there is only one substitution required: The placeholder `:val` in
  the condition expression is replaced at runtime with the actual ISBN value to be
  checked.

The following example adds a new book item using these optional parameters.

###### Example

```
Item item = new Item()
    .withPrimaryKey("Id", 104)
    .withString("Title", "Book 104 Title")
    .withString("ISBN", "444-4444444444")
    .withNumber("Price", 20)
    .withStringSet("Authors",
        new HashSet<String>(Arrays.asList("Author1", "Author2")));

Map<String, Object> expressionAttributeValues = new HashMap<String, Object>();
expressionAttributeValues.put(":val", "444-4444444444");

PutItemOutcome outcome = table.putItem(
    item,
    "ISBN = :val", // ConditionExpression parameter
    null,          // ExpressionAttributeNames parameter - we're not using it for this example
    expressionAttributeValues);
```

### PutItem and JSON documents

You can store a JSON document as an attribute in a DynamoDB table. To do this, use the
`withJSON` method of `Item`. This method parses the JSON document
and maps each element to a native DynamoDB data type.

Suppose that you wanted to store the following JSON document, containing vendors that
can fulfill orders for a particular product.

###### Example

```
{
    "V01": {
        "Name": "Acme Books",
        "Offices": [ "Seattle" ]
    },
    "V02": {
        "Name": "New Publishers, Inc.",
        "Offices": ["London", "New York"
        ]
    },
    "V03": {
        "Name": "Better Buy Books",
        "Offices": [ "Tokyo", "Los Angeles", "Sydney"
        ]
    }
}
```

You can use the `withJSON` method to store this in the
`ProductCatalog` table, in a `Map` attribute named
`VendorInfo`. The following Java code example demonstrates how to do
this.

```
// Convert the document into a String.  Must escape all double-quotes.
String vendorDocument = "{"
    + "    \"V01\": {"
    + "        \"Name\": \"Acme Books\","
    + "        \"Offices\": [ \"Seattle\" ]"
    + "    },"
    + "    \"V02\": {"
    + "        \"Name\": \"New Publishers, Inc.\","
    + "        \"Offices\": [ \"London\", \"New York\"" + "]" + "},"
    + "    \"V03\": {"
    + "        \"Name\": \"Better Buy Books\","
    +          "\"Offices\": [ \"Tokyo\", \"Los Angeles\", \"Sydney\""
    + "            ]"
    + "        }"
    + "    }";

Item item = new Item()
    .withPrimaryKey("Id", 210)
    .withString("Title", "Book 210 Title")
    .withString("ISBN", "210-2102102102")
    .withNumber("Price", 30)
    .withJSON("VendorInfo", vendorDocument);

PutItemOutcome outcome = table.putItem(item);
```

## Getting an item

To retrieve a single item, use the `getItem` method of a `Table`
object. Follow these steps:

1. Create an instance of the `DynamoDB` class.
2. Create an instance of the `Table` class to represent the table you want to
   work with.
3. Call the `getItem` method of the `Table` instance. You must
   specify the primary key of the item that you want to retrieve.

The following Java code example demonstrates the preceding steps. The code gets the item
that has the specified partition key.

```
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().build();
DynamoDB dynamoDB = new DynamoDB(client);

Table table = dynamoDB.getTable("ProductCatalog");

Item item = table.getItem("Id", 210);
```

### Specifying optional parameters

Along with the required parameters, you can also specify optional parameters for the
`getItem` method. For example, the following Java code example uses an optional
method to retrieve only a specific list of attributes and to specify strongly consistent
reads. (To learn more about read consistency, see [DynamoDB read consistency](HowItWorks.md "HowItWorks.md").)

You can use a `ProjectionExpression` to retrieve only specific attributes or
elements, rather than an entire item. A `ProjectionExpression` can specify
top-level or nested attributes using document paths. For more information, see [Using projection expressions in
DynamoDB](Expressions.md "Expressions.md").

The parameters of the `getItem` method don't let you specify read
consistency. However, you can create a `GetItemSpec`, which provides full access
to all of the inputs to the low-level `GetItem` operation. The following code
example creates a `GetItemSpec` and uses that spec as input to the
`getItem` method.

###### Example

```
GetItemSpec spec = new GetItemSpec()
    .withPrimaryKey("Id", 206)
    .withProjectionExpression("Id, Title, RelatedItems[0], Reviews.FiveStar")
    .withConsistentRead(true);

Item item = table.getItem(spec);

System.out.println(item.toJSONPretty());
```

To print an `Item` in a human-readable format, use the
`toJSONPretty` method. The output from the previous example looks like the
following.

```
`{
 "RelatedItems" : [ 341 ],
 "Reviews" : {
 "FiveStar" : [ "Excellent! Can't recommend it highly enough! Buy it!", "Do yourself a favor and buy this" ]
 },
 "Id" : 123,
 "Title" : "20-Bicycle 123"
}`
```

### GetItem and JSON documents

In the [PutItem and JSON documents](#PutItemJavaDocumentAPI.JSON "#PutItemJavaDocumentAPI.JSON") section, you store a JSON document in a
`Map` attribute named `VendorInfo`. You can use the
`getItem` method to retrieve the entire document in JSON format. Or you can use
document path notation to retrieve only some of the elements in the document. The following
Java code example demonstrates these techniques.

```
GetItemSpec spec = new GetItemSpec()
    .withPrimaryKey("Id", 210);

System.out.println("All vendor info:");
spec.withProjectionExpression("VendorInfo");
System.out.println(table.getItem(spec).toJSON());

System.out.println("A single vendor:");
spec.withProjectionExpression("VendorInfo.V03");
System.out.println(table.getItem(spec).toJSON());

System.out.println("First office location for this vendor:");
spec.withProjectionExpression("VendorInfo.V03.Offices[0]");
System.out.println(table.getItem(spec).toJSON());

```

The output from the previous example looks like the following.

```
All vendor info:
{"VendorInfo":{"V03":{"Name":"Better Buy Books","Offices":["Tokyo","Los Angeles","Sydney"]},"V02":{"Name":"New Publishers, Inc.","Offices":["London","New York"]},"V01":{"Name":"Acme Books","Offices":["Seattle"]}}}
A single vendor:
{"VendorInfo":{"V03":{"Name":"Better Buy Books","Offices":["Tokyo","Los Angeles","Sydney"]}}}
First office location for a single vendor:
{"VendorInfo":{"V03":{"Offices":["Tokyo"]}}}

```

###### Note

You can use the `toJSON` method to convert any item (or its attributes) to
a JSON-formatted string. The following code retrieves several top-level and nested
attributes and prints the results as JSON.

```
GetItemSpec spec = new GetItemSpec()
    .withPrimaryKey("Id", 210)
    .withProjectionExpression("VendorInfo.V01, Title, Price");

Item item = table.getItem(spec);
System.out.println(item.toJSON());
```

The output looks like the following.

```
{"VendorInfo":{"V01":{"Name":"Acme Books","Offices":["Seattle"]}},"Price":30,"Title":"Book 210 Title"}

```

## Batch write: Putting and deleting multiple

items

_Batch write_ refers to putting and deleting multiple items in a batch.
The `batchWriteItem` method enables you to put and delete multiple items from one
or more tables in a single call. The following are the steps to put or delete multiple items
using the AWS SDK for Java Document API.

1. Create an instance of the `DynamoDB` class.
2. Create an instance of the `TableWriteItems` class that describes all the
   put and delete operations for a table. If you want to write to multiple tables in a single
   batch write operation, you must create one `TableWriteItems` instance per
   table.
3. Call the `batchWriteItem` method by providing the
   `TableWriteItems` objects that you created in the preceding step.
4. Process the response. You should check if there were any unprocessed request items
   returned in the response. This could happen if you reach the provisioned throughput quota
   or some other transient error. Also, DynamoDB limits the request size and the number of
   operations you can specify in a request. If you exceed these limits, DynamoDB rejects the
   request. For more information, see [Quotas in Amazon DynamoDB](ServiceQuotas.md "ServiceQuotas.md").

The following Java code example demonstrates the preceding steps. The example performs a
`batchWriteItem` operation on two tables: `Forum` and
`Thread`. The corresponding `TableWriteItems` objects define the
following actions:

- Put an item in the `Forum` table.
- Put and delete an item in the `Thread` table.

The code then calls `batchWriteItem` to perform the operation.

```
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().build();
DynamoDB dynamoDB = new DynamoDB(client);

TableWriteItems forumTableWriteItems = new TableWriteItems("Forum")
    .withItemsToPut(
        new Item()
            .withPrimaryKey("Name", "Amazon RDS")
            .withNumber("Threads", 0));

TableWriteItems threadTableWriteItems = new TableWriteItems("Thread")
    .withItemsToPut(
        new Item()
            .withPrimaryKey("ForumName","Amazon RDS","Subject","Amazon RDS Thread 1")
    .withHashAndRangeKeysToDelete("ForumName","Some partition key value", "Amazon S3", "Some sort key value");

BatchWriteItemOutcome outcome = dynamoDB.batchWriteItem(forumTableWriteItems, threadTableWriteItems);

// Code for checking unprocessed items is omitted in this example
```

For a working example, see [Example: Batch write operation using the
AWS SDK for Java document API](batch-operation-document-api-java.md#JavaDocumentAPIBatchWrite "batch-operation-document-api-java.md#JavaDocumentAPIBatchWrite").

## Batch get: Getting multiple items

The `batchGetItem` method enables you to retrieve multiple items from one or
more tables. To retrieve a single item, you can use the `getItem` method.

Follow these steps:

1. Create an instance of the `DynamoDB` class.
2. Create an instance of the `TableKeysAndAttributes` class that describes a
   list of primary key values to retrieve from a table. If you want to read from multiple
   tables in a single batch get operation, you must create one
   `TableKeysAndAttributes` instance per table.
3. Call the `batchGetItem` method by providing the
   `TableKeysAndAttributes` objects that you created in the preceding
   step.

The following Java code example demonstrates the preceding steps. The example retrieves
two items from the `Forum` table and three items from the `Thread`
table.

```
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().build();
DynamoDB dynamoDB = new DynamoDB(client);

    TableKeysAndAttributes forumTableKeysAndAttributes = new TableKeysAndAttributes(forumTableName);
    forumTableKeysAndAttributes.addHashOnlyPrimaryKeys("Name",
    "Amazon S3",
    "Amazon DynamoDB");

TableKeysAndAttributes threadTableKeysAndAttributes = new TableKeysAndAttributes(threadTableName);
threadTableKeysAndAttributes.addHashAndRangePrimaryKeys("ForumName", "Subject",
    "Amazon DynamoDB","DynamoDB Thread 1",
    "Amazon DynamoDB","DynamoDB Thread 2",
    "Amazon S3","S3 Thread 1");

BatchGetItemOutcome outcome = dynamoDB.batchGetItem(
    forumTableKeysAndAttributes, threadTableKeysAndAttributes);

for (String tableName : outcome.getTableItems().keySet()) {
    System.out.println("Items in table " + tableName);
    List<Item> items = outcome.getTableItems().get(tableName);
    for (Item item : items) {
        System.out.println(item);
    }
}
```

### Specifying optional parameters

Along with the required parameters, you can also specify optional parameters when using
`batchGetItem`. For example, you can provide a
`ProjectionExpression` with each `TableKeysAndAttributes` you
define. This allows you to specify the attributes that you want to retrieve from the
table.

The following code example retrieves two items from the `Forum` table. The
`withProjectionExpression` parameter specifies that only the
`Threads` attribute is to be retrieved.

###### Example

```
TableKeysAndAttributes forumTableKeysAndAttributes = new TableKeysAndAttributes("Forum")
    .withProjectionExpression("Threads");

forumTableKeysAndAttributes.addHashOnlyPrimaryKeys("Name",
    "Amazon S3",
    "Amazon DynamoDB");

BatchGetItemOutcome outcome = dynamoDB.batchGetItem(forumTableKeysAndAttributes);
```

## Updating an item

The `updateItem` method of a `Table` object can update existing
attribute values, add new attributes, or delete attributes from an existing item.

The `updateItem` method behaves as follows:

- If an item does not exist (no item in the table with the specified primary key),
  `updateItem` adds a new item to the table.
- If an item exists, `updateItem` performs the update as specified by the
  `UpdateExpression` parameter.

###### Note

It is also possible to "update" an item using `putItem`. For example, if you
call `putItem` to add an item to the table, but there is already an item with the
specified primary key, `putItem` replaces the entire item. If there are
attributes in the existing item that are not specified in the input, `putItem`
removes those attributes from the item.

In general, we recommend that you use `updateItem` whenever you want to
modify any item attributes. The `updateItem` method only modifies the item
attributes that you specify in the input, and the other attributes in the item remain
unchanged.

Follow these steps:

1. Create an instance of the `Table` class to represent the table that you
   want to work with.
2. Call the `updateTable` method of the `Table` instance. You must
   specify the primary key of the item that you want to retrieve, along with an
   `UpdateExpression` that describes the attributes to modify and how to modify
   them.

The following Java code example demonstrates the preceding tasks. The code updates a book
item in the `ProductCatalog` table. It adds a new author to the set of
`Authors` and deletes the existing `ISBN` attribute. It also reduces
the price by one.

An `ExpressionAttributeValues` map is used in the
`UpdateExpression`. The placeholders `:val1` and `:val2` are
replaced at runtime with the actual values for `Authors` and
`Price`.

```
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().build();
DynamoDB dynamoDB = new DynamoDB(client);

Table table = dynamoDB.getTable("ProductCatalog");

Map<String, String> expressionAttributeNames = new HashMap<String, String>();
expressionAttributeNames.put("#A", "Authors");
expressionAttributeNames.put("#P", "Price");
expressionAttributeNames.put("#I", "ISBN");

Map<String, Object> expressionAttributeValues = new HashMap<String, Object>();
expressionAttributeValues.put(":val1",
    new HashSet<String>(Arrays.asList("Author YY","Author ZZ")));
expressionAttributeValues.put(":val2", 1);   //Price

UpdateItemOutcome outcome =  table.updateItem(
    "Id",          // key attribute name
    101,           // key attribute value
    "add #A :val1 set #P = #P - :val2 remove #I", // UpdateExpression
    expressionAttributeNames,
    expressionAttributeValues);
```

### Specifying optional parameters

Along with the required parameters, you can also specify optional parameters for the
`updateItem` method, including a condition that must be met in order for the
update is to occur. If the condition you specify is not met, the AWS SDK for Java throws a
`ConditionalCheckFailedException`. For example, the following Java code example
conditionally updates a book item price to 25. It specifies a
`ConditionExpression` stating that the price should be updated only if the
existing price is 20.

###### Example

```
Table table = dynamoDB.getTable("ProductCatalog");

Map<String, String> expressionAttributeNames = new HashMap<String, String>();
expressionAttributeNames.put("#P", "Price");

Map<String, Object> expressionAttributeValues = new HashMap<String, Object>();
expressionAttributeValues.put(":val1", 25);  // update Price to 25...
expressionAttributeValues.put(":val2", 20);  //...but only if existing Price is 20

UpdateItemOutcome outcome = table.updateItem(
    new PrimaryKey("Id",101),
    "set #P = :val1", // UpdateExpression
    "#P = :val2",     // ConditionExpression
    expressionAttributeNames,
    expressionAttributeValues);
```

### Atomic counter

You can use `updateItem` to implement an atomic counter, where you increment
or decrement the value of an existing attribute without interfering with other write
requests. To increment an atomic counter, use an `UpdateExpression` with a
`set` action to add a numeric value to an existing attribute of type
`Number`.

The following example demonstrates this, incrementing the `Quantity`
attribute by one. It also demonstrates the use of the `ExpressionAttributeNames`
parameter in an `UpdateExpression`.

```
Table table = dynamoDB.getTable("ProductCatalog");

Map<String,String> expressionAttributeNames = new HashMap<String,String>();
expressionAttributeNames.put("#p", "PageCount");

Map<String,Object> expressionAttributeValues = new HashMap<String,Object>();
expressionAttributeValues.put(":val", 1);

UpdateItemOutcome outcome = table.updateItem(
    "Id", 121,
    "set #p = #p + :val",
    expressionAttributeNames,
    expressionAttributeValues);
```

## Deleting an item

The `deleteItem` method deletes an item from a table. You must provide the
primary key of the item that you want to delete.

Follow these steps:

1. Create an instance of the `DynamoDB` client.
2. Call the `deleteItem` method by providing the key of the item you want to
   delete.

The following Java example demonstrates these tasks.

###### Example

```
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().build();
DynamoDB dynamoDB = new DynamoDB(client);

Table table = dynamoDB.getTable("ProductCatalog");

DeleteItemOutcome outcome = table.deleteItem("Id", 101);
```

### Specifying optional parameters

You can specify optional parameters for `deleteItem`. For example, the
following Java code example specifies a `ConditionExpression`, stating that a
book item in `ProductCatalog` can only be deleted if the book is no longer in
publication (the `InPublication` attribute is false).

###### Example

```
Map<String,Object> expressionAttributeValues = new HashMap<String,Object>();
expressionAttributeValues.put(":val", false);

DeleteItemOutcome outcome = table.deleteItem("Id",103,
    "InPublication = :val",
    null, // ExpressionAttributeNames - not used in this example
    expressionAttributeValues);
```
