

# Document history for the AWS Clean Rooms SQL Reference
<a name="doc-history-sql-ref"></a>

The following table describes the documentation releases for the AWS Clean Rooms SQL Reference. 

For notification about updates to this documentation, you can subscribe to the RSS feed. To subscribe to RSS updates, you must have an RSS plug-in enabled for the browser you are using.

| Change | Description | Date | 
| --- |--- |--- |
| [Clarified nested data type limitation for Amazon Athena data sources](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_Supported_data_types.html) | Clarified that nested data types (ARRAY, MAP, and STRUCT) are not supported for Amazon Athena data sources in AWS Clean Rooms Spark SQL. | July 23, 2026 | 
| [Spark SQL supports Hints](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-commands-hints-spark.html) | AWS Clean Rooms Spark SQL supports query hints to optimize query performance and reduce compute costs. | January 20, 2026 | 
| [Spark SQL supports CACHE TABLE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-commands-cache-table.html) | AWS Clean Rooms Spark SQL supports the CACHE TABLE command, which allows customers to cache existing tables or create and cache new tables from query results for improved query performance. | October 22, 2025 | 
| [Spark SQL supports FIRST and LAST Window functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Window_functions.html#Window_function_supported) | AWS Clean Rooms Spark SQL supports the following Window functions: FIRST and LAST. | June 12, 2025 | 
| [Spark SQL function documentation updates](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-reference-spark.html) | Documentation-only update to accurately reflect supported Spark SQL functions. Removed documentation for 25 unsupported functions, including <=> operator, SIMILAR TO, LISTAGG, and ARRAY\_INSERT. Corrected function names from DATEADD to DATE\_ADD, DATEDIFF to DATE\_DIFF, ISNULL to IS\_NULL, and ISNOTNULL to IS\_NOT\_NULL. Fixed a typo in DATE\_PART examples. | May 20, 2025 | 
| [AWS Clean Rooms Spark SQL](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-reference-spark.html) | Customers can now run queries using some SQL conditions, functions, commands, and conventions supported with the Spark SQL analytics engine.  | October 29, 2024 | 
| [SQL commands and SQL functions – update](#doc-history-sql-ref) | Examples have been added for the JOIN clause, EXCEPT set operator, CASE conditional expression, and the following functions: ANY\_VALUE, NVL and COALESCE, NULLIF, CAST, CONVERT, CONVERT\_TIMEZONE, EXTRACT, MOD, SIGN, CONCAT, FIRST\_VALUE, and LAST\_VALUE. | February 28, 2024 | 
| [SQL functions - update](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-functions-topic.html) | AWS Clean Rooms now supports the following SQL functions: Array, SUPER, and VARBYTE. The following math functions are now supported: ACOS, ASIN, ATAN, ATAN2, COT, DEXP, PI, POW, RADIANS, and SIN. The following JSON functions are now supported: CAN\_JSON\_PARSE, JSON\_PARSE, and JSON\_SERIALIZE. | October 6, 2023 | 
| [Nested data type support](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/nested-data-type.html) | AWS Clean Rooms now supports nested data types. | August 30, 2023 | 
| [SQL naming rules - update](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-ref-naming.html) | Documentation-only change to clarify reserved column names.  | August 16, 2023 | 
| [General availability](#doc-history-sql-ref) | The AWS Clean Rooms SQL Reference is now generally available. | July 31, 2023 | 