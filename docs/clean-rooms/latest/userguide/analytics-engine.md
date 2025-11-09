# Analytics engine in AWS Clean Rooms

###### Important

AWS Clean Rooms will end support for the legacy Clean Rooms SQL analytics engine on December 17th, 2025. Before July 16, 2025, you must request a limit increase via AWS Customer Support to
create any new Clean Rooms SQL engine-based collaborations. Starting July 17, 2025, the creation
of new Clean Rooms SQL engine-based collaborations will no longer be available.

## About the analytics engine

An _analytics engine_ is a software component that
processes data queries and performs analytical computations within AWS Clean Rooms. The analytics engine
interprets SQL commands, executes data processing operations, and returns analysis
results.

The following table compares the Spark analytics engine (recommended) with the legacy Clean
Rooms SQL analytics engine.

| Analytics engine                         | When would you use it?                                                        | Aggregation analysis rule supported? | List analysis rule supported? | Custom analysis rule without differential privacy supported? | Custom analysis rule with differential privacy supported? | Amazon S3 data source supported? | Amazon Athena and Snowflake data sources supported? |
| ---------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------ | ----------------------------- | ------------------------------------------------------------ | --------------------------------------------------------- | -------------------------------- | --------------------------------------------------- |
| **Spark analytics engine**               | • Running Spark SQL queries<br>• Running PySpark jobs<br>• Custom ML modeling | Yes                                  | Yes                           | Yes                                                          | Yes                                                       | Yes                              | Yes                                                 |
| **AWS Clean Rooms SQL analytics engine** | Running AWS Clean Rooms SQL queries                                           | Yes                                  | Yes                           | Yes                                                          | Yes                                                       | Yes                              | No                                                  |

## Additional resources

For information about Spark SQL queries, see the _[AWS Clean Rooms
Spark SQL Reference](../sql-reference/sql-reference-spark.md "../sql-reference/sql-reference-spark.md")_.

For information about AWS Clean Rooms SQL queries, see the _[AWS Clean Rooms SQL
Reference](../sql-reference/sql-reference-acr.md "../sql-reference/sql-reference-acr.md")_.

For pricing information for Spark SQL and AWS Clean Rooms SQL, see [AWS Clean Rooms Pricing](https://aws.amazon.com/clean-rooms/pricing/ "https://aws.amazon.com/clean-rooms/pricing/").
