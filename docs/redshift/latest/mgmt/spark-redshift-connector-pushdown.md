Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Performance improvements with

pushdown

The Spark connector automatically applies predicate and query pushdown to optimize
for performance. This support means that if you’re using a supported function in your
query, the Spark connector will turn the function into a SQL query and run the query in
Amazon Redshift. This optimization results in less data being retrieved, so Apache Spark can
process less data and have better performance. By default, pushdown is automatically
activated. To deactivate it, set `autopushdown` to false.

```
import sqlContext.implicits._val
 sample= sqlContext.read
    .format("io.github.spark_redshift_community.spark.redshift")
    .option("url",jdbcURL )
    .option("tempdir", tempS3Dir)
    .option("dbtable", "event")
    .option("autopushdown", "false")
    .load()
```

The following functions are supported with pushdown. If you’re using a function
that’s not in this list, the Spark connector will perform the function in Spark instead
of Amazon Redshift, resulting in unoptimized performance. For a complete list of functions in
Spark, see [Built-in
Functions](https://spark.apache.org/docs/latest/api/sql/index.html "https://spark.apache.org/docs/latest/api/sql/index.html").

- Aggregation functions
  - avg
  - count
  - max
  - min
  - sum
  - stddev_samp
  - stddev_pop
  - var_samp
  - var_pop

- Boolean operators
  - in
  - isnull
  - isnotnull
  - contains
  - endswith
  - startswith

- Logical operators
  - and
  - or
  - not (or !)

- Mathematical functions
  - -
  - -
  - \*
  - /
  - - (unary)
  - abs
  - acos
  - asin
  - atan
  - ceil
  - cos
  - exp
  - floor
  - greatest
  - least
  - log10
  - pi
  - pow
  - round
  - sin
  - sqrt
  - tan

- Miscellaneous functions
  - cast
  - coalesce
  - decimal
  - if
  - in

- Relational operators
  - !=
  - =
  - >
  - > =
  - <
  - <=

- String functions
  - ascii
  - lpad
  - rpad
  - translate
  - upper
  - lower
  - length
  - trim
  - ltrim
  - rtrim
  - like
  - substring
  - concat

- Time and date functions
  - add_months
  - date
  - date_add
  - date_sub
  - date_trunc
  - timestamp
  - trunc

- Mathematical operations
  - CheckOverflow
  - PromotePrecision

- Relational operations
  - Aliases (for example, AS)
  - CaseWhen
  - Distinct
  - InSet
  - Joins and cross joins
  - Limits
  - Unions, union all
  - ScalarSubquery
  - Sorts (ascending and descending)
  - UnscaledValue
