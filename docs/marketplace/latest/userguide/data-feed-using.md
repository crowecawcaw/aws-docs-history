

# Collecting and analyzing data with data feeds
<a name="data-feed-using"></a>

AWS Marketplace provides data feeds as a mechanism to send structured, up-to-date product and customer information from AWS Marketplace systems to seller Amazon S3 buckets for ETL (extract, transform, and load) between seller-owned business intelligence tools. When data is available in your Amazon S3 bucket, you can use data feeds in the following ways:
+ Download the .CSV files from the Amazon S3 bucket you created in [Accessing data feeds](data-feed-accessing.md) so that you can view the data in a spreadsheet.
+ Use ETL (extract, transform, and load), SQL query, business analytics tools to collect and analyze the data.

  You can use AWS services to collect and analyze data, or any third-party tool that can perform analysis of .CSV-based datasets.

For more information about data feeds to collect and analyze data, see the following example.

## Example: Use AWS services to collect and analyze data
<a name="data-feed-using-example"></a>

The following procedure assumes that you've already configured your environment to receive data feeds to an Amazon S3 bucket and that the bucket contains data feeds.

**To collect and analyze data from data feeds**

1. From the [AWS Glue console](https://console.aws.amazon.com/glue), [create a crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) to connect to the Amazon S3 bucket that stores the data feeds, extract the data you want, and create metadata tables in the AWS Glue Data Catalog.

   For more information about AWS Glue, see the [*AWS Glue Developer Guide*](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html).

1. From the [Athena console](https://console.aws.amazon.com/athena), [run SQL queries on the data in the AWS Glue Data Catalog](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html).

   For more information about Athena see the [*Amazon Athena User Guide*](https://docs.aws.amazon.com/athena/latest/ug/what-is.html). 

1. From the [Quick console](http://quicksight.aws.amazon.com), [create an analysis](https://docs.aws.amazon.com/quick/latest/userguide/creating-an-analysis.html) and then [create a visual](https://docs.aws.amazon.com/quick/latest/userguide/creating-a-visual.html) of the data.

   For more information about Quick, see the [*Amazon Quick User Guide*](https://docs.aws.amazon.com/quick/latest/userguide/welcome.html).

For a detailed example of one way to use AWS services to collect and analyze data in data feeds, see [Using Seller Data Feed Delivery Service, Amazon Athena, and Quick to create seller reports](https://aws.amazon.com/blogs/awsmarketplace/using-seller-data-feed-delivery-service-amazon-athena-and-amazon-quicksight-to-create-seller-reports/) at the AWS Marketplace Blog.