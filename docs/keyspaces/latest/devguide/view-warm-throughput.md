# View warm throughput of an Amazon Keyspaces table

You can view your Amazon Keyspaces table's current warm throughput values using the console, CQL, or the AWS CLI.

Console

###### How to view your table's pre-warming settings using the console.

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**, and then choose
   the table that you want to review.
3. On the **Capacity** tab of the table, continue to **Pre-warming for tables**.

Cassandra Query Language (CQL)

###### View the warm-throughput settings of a table using CQL

- To view the warm-throughput settings of a table, you can use the following CQL statement.

```
SELECT custom_properties
FROM system_schema_mcs.tables
WHERE keyspace_name='catalog' and table_name='book_awards';

// Output:
...
custom_properties
----------------------------------------------------------------------------------
{
    'warm_throughput':
    {
        'read_units_per_second': '40000',
        'write_units_per_second': '20000',
        'status': 'AVAILABLE'
    }
}
...

```

CLI

###### View the warm-throughput settings of a table using the AWS CLI

- You can view the warm-throughput settings of a table using the `get-table` command as shown
  in the following example.

```
aws keyspaces get-table \
--keyspace-name 'catalog' \
--table-name 'book_awards'

```

The following is showing the example output of the `get-table` command for a single-Region table in
provisioned mode.

```
`{
 "keyspaceName": "catalog",
 "tableName": "book_awards",
 ... Existing Fields ...,
 "capacitySpecificationSummary": {
 "throughputMode": "PROVISIONED",
 "readCapacityUnits": 20000,
 "writeCapacityUnits": 10000
 },
 "warmThroughputSpecificationSummary": {
 "readUnitsPerSecond": 40000,
 "writeUnitsPerSecond": 20000,
 "status": "AVAILABLE"
 }
}`
```

The following is showing the example output for a single-Region table in on-demand mode.

```
`{
 "keyspaceName": "catalog",
 "tableName": "book_awards_ondemand",
 ... Existing Fields ...,
 "capacitySpecification": {
 "throughputMode": "PAY_PER_REQUEST"
 },
 "warmThroughputSpecificationSummary": {
 "readUnitsPerSecond": 40000,
 "writeUnitsPerSecond": 20000,
 "status": "AVAILABLE"
 }
}`
```

Java

###### Read the pre-warming settings of a table using the SDK for Java.

- Read the warm-throughput values of a table using `get-table`. The following code example is an
  example of this.

```
import software.amazon.awssdk.services.keyspaces.KeyspacesClient;
import software.amazon.awssdk.services.keyspaces.model.*;

public class GetTableWithPreWarmingExample {
    public static void main(String[] args) {
        KeyspacesClient keyspacesClient = KeyspacesClient.builder().build();

        // Get table details including PreWarming specification
        GetTableRequest request = GetTableRequest.builder()
            .keyspaceName("catalog")
            .tableName("book_awards")
            .build();

        GetTableResponse response = keyspacesClient.getTable(request);

        // Access PreWarming details
        if (response.warmThroughputSpecification() != null) {
            WarmThroughputSpecificationSummary warmThroughputSummary = response.warmThroughputSpecification();
            System.out.println("PreWarming Status: " + warmThroughputSummary.status());
            System.out.println("Read Units: " + warmThroughputSummary.readUnitsPerSecond());
            System.out.println("Write Units: " + warmThroughputSummary.writeUnitsPerSecond());

            // Check if PreWarming is active
            if (warmThroughputSummary.status().equals("AVAILABLE")) {
                System.out.println("Table is fully pre-warmed and ready for high throughput");
            } else if (warmThroughputSummary.status().equals("UPDATING")) {
                System.out.println("Table PreWarming is currently being updated");
            }
        } else {
            System.out.println("Table does not have PreWarming enabled");
        }
    }
}
```
