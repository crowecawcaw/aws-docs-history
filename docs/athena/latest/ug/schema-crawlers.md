# Use a crawler to add a table

AWS Glue crawlers help discover the schema for datasets and register them as tables in the
AWS Glue Data Catalog. The crawlers go through your data and determine the schema. In addition,
the crawler can detect and register partitions. For more information, see [Defining crawlers](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md") in the
_AWS Glue Developer Guide_. Tables from data that were successfully
crawled can be queried from Athena.

###### Note

Athena does not recognize [exclude
patterns](../../../glue/latest/dg/define-crawler.md#crawler-data-stores-exclude "../../../glue/latest/dg/define-crawler.md#crawler-data-stores-exclude") that you specify for an AWS Glue crawler. For example, if you have an
Amazon S3 bucket that contains both `.csv` and `.json`
files and you exclude the `.json` files from the crawler, Athena
queries both groups of files. To avoid this, place the files that you want to exclude in
a different location.

## Create an AWS Glue crawler

You can create a crawler by starting in the Athena console and then using the AWS Glue
console in an integrated way. When you create the crawler, you specify a data location
in Amazon S3 to crawl.

###### To create a crawler in AWS Glue starting from the Athena console

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the query editor, next to **Tables and views**, choose
   **Create**, and then choose **AWS Glue
   crawler**.
3. On the **AWS Glue** console **Add crawler**
   page, follow the steps to create a crawler. For more information, see [Using AWS Glue Crawlers](schema-crawlers.md "schema-crawlers.md") in this guide and
   [Populating the
   AWS Glue Data Catalog](../../../glue/latest/dg/populate-catalog-methods.md "../../../glue/latest/dg/populate-catalog-methods.md") in the _AWS Glue Developer Guide_.

###### Note

Athena does not recognize [exclude
patterns](../../../glue/latest/dg/define-crawler.md#crawler-data-stores-exclude "../../../glue/latest/dg/define-crawler.md#crawler-data-stores-exclude") that you specify for an AWS Glue crawler. For example, if you have
an Amazon S3 bucket that contains both `.csv` and
`.json` files and you exclude the `.json`
files from the crawler, Athena queries both groups of files. To avoid this, place
the files that you want to exclude in a different location.

After a crawl, the AWS Glue crawler automatically assigns certain table metadata to
help make it compatible with other external technologies like Apache Hive, Presto, and
Spark. Occasionally, the crawler may incorrectly assign metadata properties. Manually
correct the properties in AWS Glue before querying the table using Athena. For more
information, see [Viewing and editing table details](../../../glue/latest/dg/console-tables.md#console-tables-details "../../../glue/latest/dg/console-tables.md#console-tables-details") in the _AWS Glue Developer
Guide_.

AWS Glue may mis-assign metadata when a CSV file has quotes around each data field,
getting the `serializationLib` property wrong. For more information, see
[Handling CSV data enclosed in quotes](schema-csv.md#schema-csv-quotes "schema-csv.md#schema-csv-quotes").
