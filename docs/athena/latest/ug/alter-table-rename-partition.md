

# ALTER TABLE RENAME PARTITION
<a name="alter-table-rename-partition"></a>

Renames a partition value.

**Note**  
ALTER TABLE RENAME PARTITION does not rename partition columns. To change a partition column name, you can use the AWS Glue console. For more information, see [Renaming a partition column in AWS Glue](#alter-table-rename-partition-column-name) later in this document. 

## Synopsis
<a name="synopsis"></a>

For the table named `table_name`, renames the partition value specified by `partition_spec` to the value specified by `new_partition_spec`.

```
ALTER TABLE table_name PARTITION (partition_spec) RENAME TO PARTITION (new_partition_spec)
```

## Parameters
<a name="parameters"></a>

**PARTITION (partition\_spec)**  
Each `partition_spec` specifies a column name/value combination in the form `partition_col_name = partition_col_value [,...]`.

## Examples
<a name="examples"></a>

```
ALTER TABLE orders 
PARTITION (dt = '2014-05-14', country = 'IN') RENAME TO PARTITION (dt = '2014-05-15', country = 'IN');
```

## Renaming a partition column in AWS Glue
<a name="alter-table-rename-partition-column-name"></a>

Use the following procedure to rename partition column names in the AWS Glue console.

**To rename a table partition column in the AWS Glue console**

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. In the navigation pane, choose **Tables**.

1. On the **Tables** page, use the **Filter tables** search box to find the table that you want to change.

1. In the **Name** column, choose the link of the table that you want to change.

1. On the details page for the table, in the **Schema** section, do one of the following:
   + To make the name change in JSON format, choose **Edit schema as JSON**.
   + To change the name directly, choose **Edit schema**. This procedure chooses **Edit schema**.

1. Select the check box for the partitioned column that you want to rename, and then choose **Edit**.

1. In the **Edit schema entry** dialog box, for **Name**, enter the new name for the partition column.

1. Choose **Save as new table version**. This action updates the partition column name and preserves the schema evolution history without creating a separate physical copy of your data.

1. To compare table versions, on the details page for the table, choose **Actions**, and then choose **Compare versions**.

## Additional resources
<a name="alter-table-rename-partition-additional-resources"></a>

 For more information about partitioning, see [Partition your data](partitions.md).