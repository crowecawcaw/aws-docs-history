

# Query restored Amazon Glacier objects
<a name="querying-glacier"></a>

You can use Athena to query restored objects from the Amazon Glacier Flexible Retrieval (formerly Glacier) and Amazon Glacier Deep Archive [Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-glacier). You must enable this capability on a per-table basis. If you do not enable the feature on a table before you run a query, Athena skips all of the table's Amazon Glacier Flexible Retrieval and Amazon Glacier Deep Archive objects during query execution. 

## Considerations and Limitations
<a name="querying-glacier-considerations-and-limitations"></a>
+  Querying restored Amazon Glacier objects is supported only on Athena engine version 3. 
+  The feature is supported only for Apache Hive tables. 
+  You must restore your objects before you query your data; Athena does not restore objects for you. 

## Configure a table to use restored objects
<a name="querying-glacier-configuring-a-table-to-use-restored-objects"></a>

 To configure your Athena table to include restored objects in your queries, you must set its `read_restored_glacier_objects` table property to `true`. To do this, you can use the Athena query editor or the AWS Glue console. You can also use the [AWS Glue CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-table.html), the [AWS Glue API](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-UpdateTable), or the [AWS Glue SDK](https://docs.aws.amazon.com/glue/latest/dg/sdk-general-information-section.html). 

### Use the Athena query editor
<a name="querying-glacier-using-the-athena-query-editor"></a>

 In Athena, you can use the [ALTER TABLE SET TBLPROPERTIES](alter-table-set-tblproperties.md) command to set the table property, as in the following example. 

```
ALTER TABLE table_name SET TBLPROPERTIES ('read_restored_glacier_objects' = 'true')
```

### Use the AWS Glue console
<a name="querying-glacier-using-the-aws-glue-console"></a>

 In the AWS Glue console, perform the following steps to add the `read_restored_glacier_objects` table property. 

**To configure table properties in the AWS Glue console**

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. Do one of the following:
   + Choose **Go to the Data Catalog**.
   + In the navigation pane, choose **Data Catalog tables**.

1. On the **Tables** page, in the list of tables, choose the link for the table that you want to edit.

1. Choose **Actions**, **Edit table**.

1. On the **Edit table** page, in the **Table properties** section, add the following key-value pair.
   + For **Key**, add `read_restored_glacier_objects`.
   + For **Value**, enter `true`.

1. Choose **Save**.

### Use the AWS CLI
<a name="querying-glacier-using-the-aws-cli"></a>

 In the AWS CLI, you can use the AWS Glue [update-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-table.html) command and its `--table-input` argument to redefine the table and in so doing add the `read_restored_glacier_objects` property. In the `--table-input` argument, use the `Parameters` structure to specify the `read_restored_glacier_objects` property and the value of `true`. Note that the argument for `--table-input` must not have spaces and must use backslashes to escape the double quotes. In the following example, replace {{my\_database}} and {{my\_table}} with the name of your database and table.

```
aws glue update-table \
   --database-name {{my_database}} \
   --table-input={\"Name\":\"{{my_table}}\",\"Parameters\":{\"read_restored_glacier_objects\":\"true\"}}
```

**Important**  
The AWS Glue `update-table` command works in overwrite mode, which means that it replaces the existing table definition with the new definition specified by the `table-input` parameter. For this reason, be sure to also specify all of the fields that you want to be in your table in the `table-input` parameter when you add the `read_restored_glacier_objects` property. 