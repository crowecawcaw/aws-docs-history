# Configure Athena to use a deployed

Hive metastore connector

After you have deployed a Lambda data source connector like
`AthenaHiveMetastoreFunction` to your account, you can configure Athena to use
it. To do so, you create a data source name that refers to your external Hive metastore to
use in your Athena queries.

###### To connect Athena to your Hive metastore using an existing Lambda function

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. If the console navigation pane is not visible, choose the expansion menu
   on the left.

![Choose the expansion menu.](images/nav-pane-expansion.png) 3. Choose **Data sources and catalogs**. 4. On the **Data sources and catalogs** page, choose **Create data
source**. 5. On the **Choose a data source** page, for **Data
sources**, choose **S3 - Apache Hive
metastore**. 6. Choose **Next**. 7. In the **Data source details** section, for **Data source
name**, enter the name that you want to use in your SQL statements when
you query the data source from Athena (for example, `MyHiveMetastore`).
The name can be up to 127 characters and must be unique within your account. It
cannot be changed after you create it. Valid characters are a-z, A-Z, 0-9, \_
(underscore), @ (at sign) and - (hyphen). The names `awsdatacatalog`,
`hive`, `jmx`, and `system` are reserved by
Athena and cannot be used for data source names. 8. In the **Connection details** section, use the **Select
or enter a Lambda function** box to choose the name of the function that
you just created. The ARN of the Lambda function displays. 9. (Optional) For **Tags**, add key-value pairs to associate with
this data source. For more information about tags, see [Tag Athena resources](tags.md "tags.md"). 10. Choose **Next**. 11. On the **Review and create** page, review the data source
details, and then choose **Create data source**. 12. The **Data source details** section of the page for your data
source shows information about your new connector.

You can now use the **Data source name** that you specified to
reference the Hive metastore in your SQL queries in Athena.

In your SQL queries, use the following example syntax, replacing
`ehms-catalog` with the data source name that you specified
earlier.

```
SELECT * FROM ehms-catalog.CustomerData.customers
```

13. To view, edit, or delete the data sources that you create, see [Manage your data sources](data-sources-managing.md "data-sources-managing.md").
