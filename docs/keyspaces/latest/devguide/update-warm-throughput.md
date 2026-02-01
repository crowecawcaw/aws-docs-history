# Increase your existing Amazon Keyspaces table's warm

throughput

You can increase your Amazon Keyspaces table's current warm throughput values using the console, CQL, or the AWS CLI.

Console

###### How to increase pre-warm settings of a table using the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**, and then choose
   the table that you want to update.
3. On the **Capacity** tab of the table, continue to **Pre-warming for tables**.
4. In the **Pre-warming for tables** section, choose **Edit**.
5. On the **Edit pre-warming for tables** page, you can updated the values for
   **Read units per second** and for **Write units per second**.
6. Choose **Save changes**. Your table is getting updated with the
   specified pre-warming settings.

Cassandra Query Language (CQL)

###### Increase the warm throughput settings of a table using CQL

- Use the `ALTER TABLE`statement to increase warm-throughput of a table. The following statement is an example of this.

```
ALTER TABLE catalog.book_awards
WITH CUSTOM_PROPERTIES = {
    'warm_throughput': {
        'read_units_per_second': 60000,
        'write_units_per_second': 30000
    }
};
```

To confirm the updated capacity settings of the table, see [View warm throughput of an Amazon Keyspaces table](view-warm-throughput.md "view-warm-throughput.md").

CLI

###### Increase the pre-warming settings of a table using the AWS CLI

- To increase the warm-throughput of table, you can use the `update-table` command. The following statement is an
  example of this.

```
aws keyspaces update-table \
--keyspace-name 'catalog' \
--table-name 'book_awards' \
--warmThroughputSpecification readUnitsPerSecond=60000,writeUnitsPerSecond=30000
```

To confirm the updated capacity settings of the table, see [View warm throughput of an Amazon Keyspaces table](view-warm-throughput.md "view-warm-throughput.md").

Java

###### Update the pre-warming settings of a table using the SDK for Java.

- Update the warm-throughput settings for a table. The following code example is an
  example of this.

```
import software.amazon.awssdk.services.keyspaces.KeyspacesClient;
import software.amazon.awssdk.services.keyspaces.model.*;

public class UpdatePreWarmingExample {
    public static void main(String[] args) {
        KeyspacesClient keyspacesClient = KeyspacesClient.builder().build();

        // Define new warm throughput specification
        WarmThroughputSpecification warmThroughput = WarmThroughputSpecification.builder()
            .readUnitsPerSecond(60000L)
            .writeUnitsPerSecond(30000L)
            .build();

        // Update table with new PreWarming settings
        UpdateTableRequest request = UpdateTableRequest.builder()
            .keyspaceName("catalog")
            .tableName("book_awards")
            .warmThroughputSpecification(warmThroughput)
            .build();

        UpdateTableResponse response = keyspacesClient.updateTable(request);
        System.out.println("Table update requested: " + response.resourceArn());
    }
}
```
