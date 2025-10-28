# Collecting and analyzing data with data feeds

AWS Marketplace provides data feeds as a mechanism to send structured, up-to-date product and
customer information from AWS Marketplace systems to seller Amazon S3 buckets for ETL (extract, transform, and
load) between seller-owned business intelligence tools. When data is available in your Amazon S3 bucket,
you can use data feeds in the following ways:

- Download the .CSV files from the Amazon S3 bucket you created in [Accessing data feeds](data-feed-accessing.md "data-feed-accessing.md") so that you can view
  the data in a spreadsheet.
- Use ETL (extract, transform, and load), SQL query, business analytics tools to collect
  and analyze the data.

You can use AWS services to collect and analyze data, or any third-party tool that
can perform analysis of .CSV-based datasets.
For more information about data feeds to collect and analyze data, see the following example.

## Example: Use AWS services to collect and analyze

data

The following procedure assumes that you've already configured your environment to
receive data feeds to an Amazon S3 bucket and that the bucket contains data feeds.

###### To collect and analyze data from data feeds

1. From the [AWS Glue console](https://console.aws.amazon.com/glue "https://console.aws.amazon.com/glue"), [create a crawler](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md") to connect to the Amazon S3
   bucket that stores the data feeds, extract the data you want, and create metadata tables
   in the AWS Glue Data Catalog.

For more information about AWS Glue, see the [_AWS Glue Developer Guide_](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md"). 2. From the [Athena console](https://console.aws.amazon.com/athena "https://console.aws.amazon.com/athena"), [run SQL queries on the data in the
AWS Glue Data Catalog](../../../athena/latest/ug/querying-athena-tables.md "../../../athena/latest/ug/querying-athena-tables.md").

For more information about Athena see the [_Amazon Athena User Guide_](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md"). 3. From the [Quick Suite console](http://quicksight.aws.amazon.com "http://quicksight.aws.amazon.com"), [create an analysis](../../../quicksuite/latest/user/creating-an-analysis.md "../../../quicksuite/latest/user/creating-an-analysis.md") and then [create a visual](../../../quicksuite/latest/user/creating-a-visual.md "../../../quicksuite/latest/user/creating-a-visual.md") of the data.

For more information about Quick Suite, see the [_Amazon Quick Suite User Guide_](../../../quicksuite/latest/user/welcome.md "../../../quicksuite/latest/user/welcome.md").

For a detailed example of one way to use AWS services to collect and analyze data in
data feeds, see [Using Seller Data Feed Delivery Service, Amazon Athena, and Quick Suite to create seller
reports](https://aws.amazon.com/blogs/awsmarketplace/using-seller-data-feed-delivery-service-amazon-athena-and-amazon-quicksight-to-create-seller-reports/ "https://aws.amazon.com/blogs/awsmarketplace/using-seller-data-feed-delivery-service-amazon-athena-and-amazon-quicksight-to-create-seller-reports/") at the AWS Marketplace Blog.
