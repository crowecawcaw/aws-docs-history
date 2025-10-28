# CustomSQL

This rule type has been extended to support two use cases:

- Run a custom SQL statement against a dataset and checks the return value against a given expression.
- Run a custom SQL statement where you specify a column name in your SELECT statement against which you compare with some condition to get row-level results.
  **Syntax**

```
CustomSql `<SQL_STATEMENT>` `<EXPRESSION>`
```

- **SQL_STATEMENT** – A SQL statement that returns a single
  numeric value, surrounded by double quotes.
- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Custom SQL to retrieve an overall rule outcome**

This example rule uses a SQL statement to retrieve the record count for a data set. The
rule then checks that the record count is between 10 and 20.

```
CustomSql "select count(*) from primary" between 10 and 20
```

**Example: Custom SQL to retrieve row-level results**

This example rule uses a SQL statement wherein you specify a column name in your SELECT statement against which you compare with some condition to get row level results. A threshold condition expression defines a threshold of how many records should fail for the entire rule to fail. Note that a rule may not contain both a condition and keyword together.

```
CustomSql "select Name from primary where Age  > 18"
```

or

```
CustomSql "select Name from primary where Age > 18" with threshold  > 3
```

###### Important

The `primary` alias stands in for the name of the data set that you want to
evaluate. When you work with visual ETL jobs on the console, `primary` always
represents the `DynamicFrame` being passed to the
`EvaluateDataQuality.apply()` transform. When you use the AWS Glue Data Catalog to run
data quality tasks against a table, `primary` represents the table.

If you are in AWS Glue Data Catalog, you can also use the actual table names:

```
CustomSql "select count(*) from database.table" between 10 and 20
```

You can also join multiple tables to compare different data elements:

```
CustomSql "select count(*) from database.table inner join database.table2 on id1 = id2" between 10 and 20
```

In AWS Glue ETL, CustomSQL can identify records that failed the data quality checks. For this to work, you need to return records that are
part of the primary table for which you are evaluating data quality. Records that are returned as part of the query are considered successful and records
that are not returned are considered failed. This works by joining the result of your CustomSQL query with the original dataset. There may be performance
implications based on the complexity of your SQL query.

To do this:

- You need to select at least 1 column from your primary table.
  - `select count(*) from primary` is a valid query for OVERALL CustomSQL DQ rule but not for Row Level Custom SQL.
  - This rule will throw an error during evaluation: `The output from CustomSQL must contain at least one column that matches the input dataset 
for AWS Glue Data Quality to provide row level results. The SQL query is a valid query but the columns from the SQL result are not present in the 
Input Dataset. Ensure that matching columns are returned from the SQL.`

- In your SQL query, select a `Primary Key` from your table or select a set of columns that form a composite key. Not doing so may result in
  inconsistent results due to matching of duplicate rows and degraded performance.
- Select keys ONLY from your primary table and not from your reference tables.
  The following rule will ensure that records with age < 100 are identified as successful and records that are above are marked as failed.

```
CustomSql "select id from primary where age < 100"
```

This CustomSQL rule will pass when 50% of the records have age > 10 and will also identify records that failed. The records returned by this
CustomSQL will be considered passed while the ones not returned will be considered failed.

```
CustomSQL "select ID, CustomerID from primary where age > 10" with threshold > 0.5
```

Note: CustomSQL rule will fail if you return records that are not available in the dataset.
