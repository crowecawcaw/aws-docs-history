# Hints

Hints for SQL analyses provide optimization directives that guide query execution strategies in AWS Clean Rooms, enabling you to improve query performance and reduce compute costs. Hints suggest how the Spark analytics engine should generate its execution plan.

## Syntax

```
SELECT /*+ `hint_name`(`parameters`), `hint_name`(`parameters`) */ `column_list`
FROM `table_name`;
```

Hints are embedded in SQL queries using comment-style syntax and must be placed directly after the SELECT keyword.

## Supported hint types

AWS Clean Rooms supports two categories of hints: Join hints and Partitioning hints.

###### Topics

- [Join hints](join-hints.md "join-hints.md")
- [Partitioning hints](partitioning-hints.md "partitioning-hints.md")

## Combining multiple hints

You can specify multiple hints in a single query by separating them with commas:

```
-- Combine join and partitioning hints
SELECT /*+ BROADCAST(d), REPARTITION(8) */ e.name, d.dept_name
FROM employees e JOIN departments d ON e.dept_id = d.id;

-- Multiple join hints
SELECT /*+ BROADCAST(s), MERGE(d) */ *
FROM employees e
JOIN students s ON e.id = s.id
JOIN departments d ON e.dept_id = d.id;

-- Hints within separate hint blocks within the same query
SELECT /*+ REPARTITION(100) */ /*+ COALESCE(500) */ /*+ REPARTITION_BY_RANGE(3, c) */ * FROM t;
```

## Considerations and limitations

- Hints are optimization suggestions, not commands. The query optimizer may ignore hints based on resource constraints or execution conditions.
- Hints are embedded directly in SQL query strings for both CreateAnalysisTemplate and StartProtectedQuery APIs.
- Hints must be placed directly after the SELECT keyword.
- Named parameters are not supported with hints and will throw an exception.
- Column names in REPARTITION amd REPARTITION_BY_RANGE hints must exist in the input schema.
- Column names in REBALANCE hints must appear in the SELECT output list.
- Numeric parameters must be positive integers between 1 and 2147483647. Scientific notations like _1e1_ are not supported
- Hints are not supported in Differential Privacy SQL queries.
- Hints for SQL queries are not supported in PySpark jobs. To provide directives for execution plans in a PySpark job, use the data frame API. See [Apache Spark DataFrame API Docs](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.hint.html "https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.hint.html") for more information.
