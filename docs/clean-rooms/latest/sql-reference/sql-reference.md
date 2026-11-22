

# Overview of SQL in AWS Clean Rooms

This reference describes the SQL that AWS Clean Rooms runs. AWS Clean Rooms SQL is based on Spark SQL. Use this reference to find the commands, functions, conditions, and data types that you can use in your queries.

The analysis rules on the configured tables that a query reads can further limit the SQL you can use. For more information, see [Analysis rules](https://docs.aws.amazon.com/clean-rooms/latest/userguide/analysis-rules.html) in the *AWS Clean Rooms User Guide*.

AWS Clean Rooms runs only `SELECT`-type queries: `SELECT` statements, including those that start with `WITH`, and `CACHE TABLE` statements. AWS Clean Rooms doesn't support other statements, such as `INSERT`, `CREATE TABLE`, `SET`, and `EXPLAIN`. Every query must include a `FROM` clause that reads from a [configured table](https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-configured-tables.html) or an [intermediate table](https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-intermediate-tables.html).

**Topics**
+ [SQL reference conventions](sql-ref-conventions.md)

The following sections describe the SQL that you can use in AWS Clean Rooms.
+ [Basic elements](sql-basic-elements.md)
+ [AWS Clean Rooms Spark SQL commands](sql-commands-topic-spark.md)
+ [AWS Clean Rooms Spark SQL functions](sql-functions-topic-spark.md)
+ [AWS Clean Rooms Spark SQL conditions](sql-conditions-topic-spark.md)

For more information about AWS Clean Rooms, see the [AWS Clean Rooms User Guide](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html) and the [AWS Clean Rooms API Reference](https://docs.aws.amazon.com/clean-rooms/latest/apireference/Welcome.html).