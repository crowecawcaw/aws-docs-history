# Create a new Amazon Keyspaces table with higher

warm throughput

You can adjust the warm throughput values when you create your Amazon Keyspaces table by
using the console, CQL, or the AWS CLI.

Console

###### How to create a new table with warm-throughput settings

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**, and then choose
   **Create table**.
3. On the **Create table** page in the **Table
   details** section, select a keyspace and provide a name for the new
   table.
4. In the **Columns** section, create the schema for your
   table.
5. In the **Primary key** section, define the primary key of the table and
   select optional clustering columns.
6. In the **Table settings** section, choose **Customize
   settings**.
7. Continue to **Read/write capacity settings**.
8. For **Capacity mode**, you can choose either **On-demand** or
   **Provisioned**.
9. In the **Pre-warming for tables** section, you can increase the values
   for **Read units per second** and **Write units per second**
   as needed to prepare your table to handle planned peak events.

The warm throughput values that Amazon Keyspaces adjusts based on your on-demand usage or provisioned capacity are available by
default for all tables without additional charges.
Note that if you manually increase the default warm throughput values to
pre-warm the table for peak traffic events, additional charges apply. 10. Configure other optional table features as needed. Then choose **Create table**.

Cassandra Query Language (CQL)

- Create a table with warm throughput using one of the following methods:
  - For provisioned mode, create a table and specify the expected peak capacity for reads and
    writes using the following CQL syntax:

  ```
  CREATE TABLE catalog.book_awards (
     year int,
     award text,
     rank int,
     category text,
     book_title text,
     author text,
     publisher text,
     PRIMARY KEY ((year, award), category, rank))
  WITH CUSTOM_PROPERTIES = {
      'capacity_mode': {
         'throughput_mode': 'PROVISIONED',
         'read_capacity_units': 20000,
         'write_capacity_units': 10000
       },
      'warm_throughput': {
          'read_units_per_second': 40000,
          'write_units_per_second': 20000
       }
  };
  ```

  - For on-demand mode, create a table and specify the expected peak capacity for reads and
    writes using the following CQL syntax:

  ````
  CREATE TABLE catalog.book_awards (
     year int,
     award text,
     rank int,
     category text,
     book_title text,
     author text,
     publisher text,
     PRIMARY KEY ((year, award), category, rank))
  WITH CUSTOM_PROPERTIES = {
      'capacity_mode': {
         'throughput_mode': 'PAY_PER_REQUEST'
       },
      'warm_throughput': {
          'read_units_per_second': 40000,
          'write_units_per_second': 20000
       }
  };
  ```To confirm the capacity settings of the table, see [View warm throughput of an Amazon Keyspaces table](view-warm-throughput.md "view-warm-throughput.md").
  ````

CLI

1. Create a table with warm throughput using one of the following methods using the AWS CLI
   - Create a new table in provisioned mode and specify the expected peak capacity values for reads
     and writes for the new table. The following statement is an
     example of this.

   ```
   aws keyspaces create-table \
   --keyspace-name 'catalog' \
   --table-name 'book_awards' \
   --schema-definition 'allColumns=[{name=year,type=int},{name=award,type=text},{name=rank,type=int},{name=category,type=text},{name=book_title,type=text},{name=author,type=text},{name=publisher,type=text}],partitionKeys=[{name=year},{name=award}],clusteringKeys=[{name=category,orderBy=ASC},{name=rank,orderBy=ASC}]' \
   --capacity-specification throughputMode=PROVISIONED,readCapacityUnits=20000,writeCapacityUnits=10000 \
   --warm-throughput-specification readUnitsPerSecond=40000,writeUnitsPerSecond=20000
   ```

   - Create a new table in on-demand mode and specify the expected peak capacity values for reads
     and writes for the new table. The following statement is an
     example of this.

   ```
   aws keyspaces create-table \
   --keyspace-name 'catalog' \
   --table-name 'book_awards' \
   --schema-definition 'allColumns=[{name=year,type=int},{name=award,type=text},{name=rank,type=int},{name=category,type=text},{name=book_title,type=text},{name=author,type=text},{name=publisher,type=text}],partitionKeys=[{name=year},{name=award}],clusteringKeys=[{name=category,orderBy=ASC},{name=rank,orderBy=ASC}]' \
   --warmThroughputSpecification readUnitsPerSecond=40000,writeUnitsPerSecond=20000
   ```

2. The output of the command returns the ARN of the table as shown in the following example.

```
`{
 "resourceArn": "arn:aws::cassandra:us-east-1:111122223333:/keyspace/catalog/table/book_awards>"
}`
```

To confirm the capacity settings of the table, see [View warm throughput of an Amazon Keyspaces table](view-warm-throughput.md "view-warm-throughput.md").

Java

###### Create a new table using the SDK for Java.

- Create a new table in provisioned mode and specify the expected peak capacity values for reads
  and writes for the new table. The following code example is an
  example of this.

```
import software.amazon.awssdk.services.keyspaces.KeyspacesClient;
import software.amazon.awssdk.services.keyspaces.model.*;

public class PreWarmingExample {
    public static void main(String[] args) {
        KeyspacesClient keyspacesClient = KeyspacesClient.builder().build();

        // Define schema
        List<ColumnDefinition> columns = Arrays.asList(
            ColumnDefinition.builder().name("year").type("int").build(),
            ColumnDefinition.builder().name("award").type("text").build(),
            ColumnDefinition.builder().name("rank").type("int").build(),
            ColumnDefinition.builder().name("category").type("text").build(),
            ColumnDefinition.builder().name("book_title").type("text").build(),
            ColumnDefinition.builder().name("author").type("text").build(),
            ColumnDefinition.builder().name("publisher").type("text").build()
        );

        List<PartitionKey> partitionKeys = Arrays.asList(
            PartitionKey.builder().name("year").build(),
            PartitionKey.builder().name("award").build()
        );

        List<ClusteringKey> clusteringKeys = Arrays.asList(
            ClusteringKey.builder().name("category").orderBy("ASC").build(),
            ClusteringKey.builder().name("rank").orderBy("ASC").build()
        );

        SchemaDefinition schema = SchemaDefinition.builder()
            .allColumns(columns)
            .partitionKeys(partitionKeys)
            .clusteringKeys(clusteringKeys)
            .build();

        // Define capacity specification
        CapacitySpecification capacitySpec = CapacitySpecification.builder()
            .throughputMode(ThroughputMode.PROVISIONED)
            .readCapacityUnits(20000)
            .writeCapacityUnits(10000)
            .build();

        // Define warm throughput specification
        WarmThroughputSpecification warmThroughput = WarmThroughputSpecification.builder()
            .readUnitsPerSecond(40000L)
            .writeUnitsPerSecond(20000L)
            .build();

        // Create table with PreWarming
        CreateTableRequest request = CreateTableRequest.builder()
            .keyspaceName("catalog")
            .tableName("book_awards")
            .schemaDefinition(schema)
            .capacitySpecification(capacitySpec)
            .warmThroughputSpecification(warmThroughput)
            .build();

        CreateTableResponse response = keyspacesClient.createTable(request);
        System.out.println("Table created with ARN: " + response.resourceArn());
    }
}
```
