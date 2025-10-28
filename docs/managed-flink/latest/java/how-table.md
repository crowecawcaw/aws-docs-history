Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Review Table API components

Your Apache Flink application uses the [Apache
Flink Table API](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/tableapi/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/tableapi/") to interact with data in a stream using a relational model. You
use the Table API to access data using Table sources, and then use Table functions to
transform and filter table data. You can transform and filter tabular data using either API
functions or SQL commands.

This section
contains the following topics:

- [Table API connectors](how-table-connectors.md "how-table-connectors.md"): These components move
  data between your application and external data sources and destinations.
- [Table API time attributes](how-table-timeattributes.md "how-table-timeattributes.md"): This topic describes how Managed Service for Apache Flink tracks
  events when using the Table API.
