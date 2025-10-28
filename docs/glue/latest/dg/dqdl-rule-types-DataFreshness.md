# DataFreshness

Checks the freshness of data in a column by evaluating the difference between the current
time and the values of a date column. You can specify a time-based expression for this rule
type to make sure that column values are up to date.

**Syntax**

```
DataFreshness `<COL_NAME>` `<EXPRESSION>`
```

- **COL_NAME** – The name of the column that you want to evaluate the data quality rule against.

**Supported column types**: Date

- **EXPRESSION** – A numeric expression in hours or days.
  You must specify the time unit in your expression.
  **Example: Data freshness**

The following example rules check for data freshness.

```
DataFreshness "Order_Date" <= 24 hours
DataFreshness "Order_Date" between 2 days and 5 days
```

**Null behavior**

The `DataFreshness` rules will fail for rows with `NULL` values. If the rule fails due to a null value,
the failure reason will display the following:

```
80.00 % of rows passed the threshold
```

where 20% of the rows that failed include the rows with `NULL`.

The following example compound rule provides a way to explicitly allow for `NULL` values:

```
(DataFreshness "Order_Date" <= 24 hours) OR (ColumnValues "Order_Date" = NULL)
```

**Data Freshness for Amazon S3 objects**

Sometimes you will need to validate the freshness of data based on the Amazon S3 file creating time. To do this, you can use
the following code to get the timestamp and add it to your dataframe, and then apply Data Freshness checks.

```
df = glueContext.create_data_frame.from_catalog(database = "default", table_name = "mytable")
df = df.withColumn("file_ts", df["_metadata.file_modification_time"])

Rules = [
 DataFreshness "file_ts" < 24 hours
]

```
