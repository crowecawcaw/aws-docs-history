Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Table API connectors

In the Apache Flink programming model, connectors are components that your application
uses to read or write data from external sources, such as other AWS services.

With the Apache Flink Table API, you can use the following types of connectors:

- [Table API sources](#how-table-connectors-source "#how-table-connectors-source"):
  You use Table API source connectors to create tables within your `TableEnvironment` using either API calls or SQL queries.
- [Table API sinks](#how-table-connectors-sink "#how-table-connectors-sink"): You use SQL commands to write table
  data to external sources such as an Amazon MSK topic or an Amazon S3 bucket.

## Table API sources

You create a table source from a data stream. The following code creates a table from an Amazon MSK topic:

```
//create the table
    final FlinkKafkaConsumer<StockRecord> consumer = new FlinkKafkaConsumer<StockRecord>(kafkaTopic, new KafkaEventDeserializationSchema(), kafkaProperties);
    consumer.setStartFromEarliest();
    //Obtain stream
    DataStream<StockRecord> events = env.addSource(consumer);

    Table table = streamTableEnvironment.fromDataStream(events);
```

For more information about table sources, see [Table & SQL Connectors](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/overview/") in the Apache Flink Documentation.

## Table API sinks

To write table data to a sink, you create the sink in SQL, and then run the
SQL-based sink on the `StreamTableEnvironment` object.

The following code example demonstrates how to write table data to an Amazon S3 sink:

```
final String s3Sink = "CREATE TABLE sink_table (" +
    "event_time TIMESTAMP," +
    "ticker STRING," +
    "price DOUBLE," +
    "dt STRING," +
    "hr STRING" +
    ")" +
    " PARTITIONED BY (ticker,dt,hr)" +
    " WITH" +
    "(" +
    " 'connector' = 'filesystem'," +
    " 'path' = '" + s3Path + "'," +
    " 'format' = 'json'" +
    ") ";

    //send to s3
    streamTableEnvironment.executeSql(s3Sink);
    filteredTable.executeInsert("sink_table");
```

You can use the `format` parameter to control what format Managed Service for Apache Flink uses to write
the output to the sink. For information about formats, see [Supported Connectors](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/overview/") in the Apache Flink Documentation.

## User-defined sources and sinks

You can use existing Apache Kafka connectors for sending data to and from other
AWS services, such as Amazon MSK and Amazon S3. For interacting with other data sources and
destinations, you can define your own sources and sinks. For more information, see
[User-defined Sources and Sinks](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/sourcessinks/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/sourcessinks/") in the Apache Flink Documentation.
