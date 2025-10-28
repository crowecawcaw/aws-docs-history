# Creating a single schema for each Amazon S3 include

path

By default, when a crawler defines tables for data stored in Amazon S3, it considers both data
compatibility and schema similarity. Data compatibility factors that it considers include
whether the data is of the same format (for example, JSON), the same compression type (for
example, GZIP), the structure of the Amazon S3 path, and other data attributes. Schema similarity
is a measure of how closely the schemas of separate Amazon S3 objects are similar.

To help illustrate this option, suppose that you define a crawler with an include path
`s3://amzn-s3-demo-bucket/table1/`. When the crawler runs, it finds two JSON files
with the following characteristics:

- **File 1** – `S3://amzn-s3-demo-bucket/table1/year=2017/data1.json`
- _File content_ – `{“A”: 1, “B”: 2}`
- _Schema_ – `A:int, B:int`

- **File 2** – `S3://amzn-s3-demo-bucket/table1/year=2018/data2.json`
- _File content_ – `{“C”: 3, “D”: 4}`
- _Schema_ – `C: int, D: int`
  By default, the crawler creates two tables, named `year_2017` and `year_2018` because the schemas are not sufficiently similar.
  However, if the option **Create a single schema for each S3 path** is selected, and if the data is compatible, the crawler creates one table.
  The table has the schema `A:int,B:int,C:int,D:int` and `partitionKey` `year:string`.

AWS Management Console

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. Choose **Crawlers** under the **Data Catalog**.
3. When you configure a new crawler, under **Output and scheduling** , select
   the option **Create a single schema for each S3 path** under
   Advance options.

AWS CLI
You can configure a crawler to `CombineCompatibleSchemas` into a common table definition when possible.
With this option, the crawler still considers data compatibility, but ignores the similarity of the specific schemas when evaluating Amazon S3 objects in the specified include path.

When you configure the crawler using the AWS CLI, set the following configuration option:

```
aws glue update-crawler \
   --name myCrawler \
   --configuration '{"Version": 1.0, "Grouping": {"TableGroupingPolicy": "CombineCompatibleSchemas" }}'

```

API
When you configure the crawler using the API, set the following configuration option:

Set the `Configuration` field with a string representation of the following JSON object in the crawler API; for example:

```
{
   "Version": 1.0,
   "Grouping": {
      "TableGroupingPolicy": "CombineCompatibleSchemas" }
}
```
