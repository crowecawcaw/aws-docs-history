Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Performing a merge operation by

replacing existing rows

When you run the merge operation detailed in the procedure, put all of the steps
except for creating and dropping the temporary staging table in a single
transaction. The transaction rolls back if any step fails. Using a single transaction
also reduces the number of commits, which saves time and resources.

###### To perform a merge operation by replacing existing rows

1. Create a staging table, and then populate it with data to be merged, as shown
   in the following pseudocode.

```
CREATE temp table stage (like target);

INSERT INTO stage
SELECT * FROM source
WHERE source.filter = 'filter_expression';
```

2. Use MERGE to perform an inner join with the staging table to update the rows from
   the target table that match the staging table, then insert all the remaining rows
   into the target table that don't match the staging table.

We recommend you
run the update and insert operations in a single MERGE command.

```
MERGE INTO target
USING stage [optional alias] on (target.primary_key = stage.primary_key)
WHEN MATCHED THEN
UPDATE SET col_name1 = stage.col_name1 , col_name2= stage.col_name2, col_name3 = {expr}
WHEN NOT MATCHED THEN
INSERT (col_name1 , col_name2, col_name3) VALUES (stage.col_name1, stage.col_name2, {expr});
```

3. Drop the staging table.

```
DROP TABLE stage;
```
