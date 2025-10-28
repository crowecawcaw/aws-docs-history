# Preventing a crawler from changing an existing schema

You can prevent AWS Glue crawlers from making any schema changes to the Data Catalog when they run.
By default, crawlers updates the schema in the Data Catalog to match the data source being crawled.
However, in some cases, you may want to prevent the Crawler from modifying the existing schema,
especially if you have transformed or cleaned the data and don't want the original schema to overwrite the changes.

Follow these steps to configure your crawler not to overwrite the existing schema in a table definition.

AWS Management Console

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. Choose **Crawlers** under the **Data Catalog**.
3. Choose a crawler from the list, and choose **Edit**.
4. Choose **step 4, Set output and scheduling**.
5. Under **Advance options**, choose **Add new columns only** or **Ignore the change and don't update the table in the Data Catalog**.
6. You can also set a configuration option to **Update all new and existing partitions with metadata from the table**. This sets partition
   schemas to inherit from the table.
7. Choose **Update**.

AWS CLI
The following example shows how to configure a crawler to not change existing schema, only add new columns:

```
aws glue update-crawler \
  --name myCrawler \
  --configuration '{"Version": 1.0, "CrawlerOutput": {"Tables": {"AddOrUpdateBehavior": "MergeNewColumns"}}}'

```

The following example shows how to configure a crawler to not change the existing schema, and not add new columns:

```
aws glue update-crawler \
  --name myCrawler \
  --schema-change-policy UpdateBehavior=LOG \
  --configuration '{"Version": 1.0, "CrawlerOutput": {"Partitions": { "AddOrUpdateBehavior": "InheritFromTable" }}}'

```

API
If you don't want a table schema to change at all when a crawler runs, set the schema change
policy to `LOG`.

When you configure the crawler using the API, set the following parameters:

- Set the `UpdateBehavior` field in `SchemaChangePolicy` structure to `LOG`.
- Set the `Configuration` field with a string representation of the following JSON object in the crawler API; for example:

```
{
   "Version": 1.0,
   "CrawlerOutput": {
      "Partitions": { "AddOrUpdateBehavior": "InheritFromTable" }
   }
}
```
