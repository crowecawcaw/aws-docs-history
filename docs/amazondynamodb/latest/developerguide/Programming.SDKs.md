# Programmatic interfaces that work with

DynamoDB

Every [AWS SDK](https://aws.amazon.com/tools "https://aws.amazon.com/tools") provides one or more
programmatic interfaces for working with Amazon DynamoDB. These interfaces range from
simple low-level DynamoDB wrappers to object-oriented persistence layers. The available
interfaces vary depending on the AWS SDK and programming language that you
use.

![Programmatic interfaces available in different AWS SDKs for working with DynamoDB.](images/SDKSupport.SDKInterfaces.png)
The following section highlights some of the interfaces available, using the
AWS SDK for Java as an example. (Not all interfaces are available in all AWS
SDKs.)

###### Topics

- [Low-level interfaces that
  work with DynamoDB](#Programming.SDKs.Interfaces.LowLevel "#Programming.SDKs.Interfaces.LowLevel")
- [Document interfaces that
  work with DynamoDB](#Programming.SDKs.Interfaces.Document "#Programming.SDKs.Interfaces.Document")
- [Object persistence
  interfaces that work with DynamoDB](#Programming.SDKs.Interfaces.Mapper "#Programming.SDKs.Interfaces.Mapper")

## Low-level interfaces that

work with DynamoDB

Every language-specific AWS SDK provides a low-level interface for
Amazon DynamoDB, with methods that closely resemble low-level DynamoDB API
requests.

In some cases, you will need to identify the data types of the attributes
using [Data type
descriptors](Programming.md#Programming.LowLevelAPI.DataTypeDescriptors "Programming.md#Programming.LowLevelAPI.DataTypeDescriptors"), such as
`S` for string or `N` for number.

###### Note

A low-level interface is available in every language-specific AWS
SDK.

The following Java program uses the low-level interface of the AWS SDK for Java.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.GetItemRequest;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 *
 * To get an item from an Amazon DynamoDB table using the AWS SDK for Java V2,
 * its better practice to use the
 * Enhanced Client, see the EnhancedGetItem example.
 */
public class GetItem {
    public static void main(String[] args) {
        final String usage = """

                Usage:
                    <tableName> <key> <keyVal>

                Where:
                    tableName - The Amazon DynamoDB table from which an item is retrieved (for example, Music3).\s
                    key - The key used in the Amazon DynamoDB table (for example, Artist).\s
                    keyval - The key value that represents the item to get (for example, Famous Band).
                """;

        if (args.length != 3) {
            System.out.println(usage);
            System.exit(1);
        }

        String tableName = args[0];
        String key = args[1];
        String keyVal = args[2];
        System.out.format("Retrieving item \"%s\" from \"%s\"\n", keyVal, tableName);
        Region region = Region.US_EAST_1;
        DynamoDbClient ddb = DynamoDbClient.builder()
                .region(region)
                .build();

        getDynamoDBItem(ddb, tableName, key, keyVal);
        ddb.close();
    }

    public static void getDynamoDBItem(DynamoDbClient ddb, String tableName, String key, String keyVal) {
        HashMap<String, AttributeValue> keyToGet = new HashMap<>();
        keyToGet.put(key, AttributeValue.builder()
                .s(keyVal)
                .build());

        GetItemRequest request = GetItemRequest.builder()
                .key(keyToGet)
                .tableName(tableName)
                .build();

        try {
            // If there is no matching item, GetItem does not return any data.
            Map<String, AttributeValue> returnedItem = ddb.getItem(request).item();
            if (returnedItem.isEmpty())
                System.out.format("No item found with the key %s!\n", key);
            else {
                Set<String> keys = returnedItem.keySet();
                System.out.println("Amazon DynamoDB table attributes: \n");
                for (String key1 : keys) {
                    System.out.format("%s: %s\n", key1, returnedItem.get(key1).toString());
                }
            }

        } catch (DynamoDbException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
}

```

## Document interfaces that

work with DynamoDB

Many AWS SDKs provide a document interface, allowing you to perform data
plane operations (create, read, update, delete) on tables and indexes. With a
document interface, you do not need to specify [Data type
descriptors](Programming.md#Programming.LowLevelAPI.DataTypeDescriptors "Programming.md#Programming.LowLevelAPI.DataTypeDescriptors"). The data
types are implied by the semantics of the data itself. These AWS SDKs also
provide methods to easily convert JSON documents to and from native Amazon DynamoDB
data types.

###### Note

Document interfaces are available in the AWS SDKs for [Java](https://aws.amazon.com/sdk-for-java "https://aws.amazon.com/sdk-for-java"), [.NET](https://aws.amazon.com/sdk-for-net "https://aws.amazon.com/sdk-for-net"), [Node.js](https://aws.amazon.com/sdk-for-node-js "https://aws.amazon.com/sdk-for-node-js"), and [JavaScript
SDK](../../../AWSJavaScriptSDK/v3/latest.md "../../../AWSJavaScriptSDK/v3/latest.md").

The following Java program uses the document interface of the AWS SDK for Java. The
program creates a `Table` object that represents the
`Music` table, and then asks that object to use
`GetItem` to retrieve a song. The program then prints the year
that the song was released.

The `software.amazon.dynamodb.document.DynamoDB` class
implements the DynamoDB document interface. Note how `DynamoDB` acts as
a wrapper around the low-level client (`AmazonDynamoDB`).

```
package com.amazonaws.codesamples.gsg;

import software.amazon.dynamodb.AmazonDynamoDB;
import software.amazon.dynamodb.AmazonDynamoDBClientBuilder;
import software.amazon.dynamodb.document.DynamoDB;
import software.amazon.dynamodb.document.GetItemOutcome;
import software.amazon.dynamodb.document.Table;

public class MusicDocumentDemo {

    public static void main(String[] args) {

        AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().build();
        DynamoDB docClient = new DynamoDB(client);

        Table table = docClient.getTable("Music");
        GetItemOutcome outcome = table.getItemOutcome(
                "Artist", "No One You Know",
                "SongTitle", "Call Me Today");

        int year = outcome.getItem().getInt("Year");
        System.out.println("The song was released in " + year);

    }
}

```

## Object persistence

interfaces that work with DynamoDB

Some AWS SDKs provide an object persistence interface where you do not
directly perform data plane operations. Instead, you create objects that
represent items in Amazon DynamoDB tables and indexes, and interact only with those
objects. This allows you to write object-centric code, rather than
database-centric code.

###### Note

Object persistence interfaces are available in the AWS SDKs for Java and
.NET. For more information, see [Higher-level programming interfaces for
DynamoDB](HigherLevelInterfaces.md "HigherLevelInterfaces.md") for DynamoDB.

```
import com.example.dynamodb.Customer;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedClient;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbTable;
import software.amazon.awssdk.enhanced.dynamodb.Key;
import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.enhanced.dynamodb.model.GetItemEnhancedRequest;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;

```

```
import com.example.dynamodb.Customer;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedClient;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbTable;
import software.amazon.awssdk.enhanced.dynamodb.Key;
import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.enhanced.dynamodb.model.GetItemEnhancedRequest;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;

/*
 * Before running this code example, create an Amazon DynamoDB table named Customer with these columns:
 *   - id - the id of the record that is the key. Be sure one of the id values is `id101`
 *   - custName - the customer name
 *   - email - the email value
 *   - registrationDate - an instant value when the item was added to the table. These values
 *                        need to be in the form of `YYYY-MM-DDTHH:mm:ssZ`, such as 2022-07-11T00:00:00Z
 *
 * Also, ensure that you have set up your development environment, including your credentials.
 *
 * For information, see this documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */

public class EnhancedGetItem {
    public static void main(String[] args) {
        Region region = Region.US_EAST_1;
        DynamoDbClient ddb = DynamoDbClient.builder()
                .region(region)
                .build();

        DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()
                .dynamoDbClient(ddb)
                .build();

        getItem(enhancedClient);
        ddb.close();
    }

    public static String getItem(DynamoDbEnhancedClient enhancedClient) {
        Customer result = null;
        try {
            DynamoDbTable<Customer> table = enhancedClient.table("Customer", TableSchema.fromBean(Customer.class));
            Key key = Key.builder()
                    .partitionValue("id101").sortValue("tred@noserver.com")
                    .build();

            // Get the item by using the key.
            result = table.getItem(
                    (GetItemEnhancedRequest.Builder requestBuilder) -> requestBuilder.key(key));
            System.out.println("******* The description value is " + result.getCustName());

        } catch (DynamoDbException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
        return result.getCustName();
    }
}

```
