# Examples of using Amazon S3 Select on an object

###### Important

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/ "https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/")

You can use S3 Select to
select content from one object by using the Amazon S3 console, the REST API, and the AWS SDKs.

For more information about supported SQL functions for S3 Select, see [SQL functions](s3-select-sql-reference-sql-functions.md "s3-select-sql-reference-sql-functions.md").

###### To select content from an object in the Amazon S3 console

1. Sign in to the AWS Management Console and open the Amazon S3 console
   at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. Choose the bucket that contains the object that you want to select content from, and then choose the name of the object.
4. Choose
   **Object actions**, and choose **Query with S3 Select**.
5. Configure **Input settings**, based on the format of your input data.
6. Configure **Output settings**, based on the format of the output that you want to receive.
7. To extract records from the chosen object, under **SQL
   query**, enter the SELECT
   SQL commands. For more information on how to write SQL
   commands, see [SQL reference for Amazon S3 Select](s3-select-sql-reference.md "s3-select-sql-reference.md").
8. After you enter SQL queries, choose **Run SQL query**. Then, under **Query results**, you
   can see the results of your SQL queries.
   You can use the AWS SDKs to select content from an object. However, if your
   application requires it, you can send REST requests directly. For more
   information about the request and response format, see [SelectObjectContent](../API/RESTObjectSELECTContent.md "../API/RESTObjectSELECTContent.md").

You can use Amazon S3 Select to select some of the content of an object by using the
`selectObjectContent` method. If this method is successful, it
returns the results of the SQL expression.

Java
To use Amazon S3 Select with the AWS SDK for Java, you can return the value of the first column for each record that is stored in an object that contains data stored in CSV format. You can also request `Progress` and `Stats` messages to be returned. You must provide a valid bucket name and an object that contains data in CSV format.

To use Amazon S3 Select with the AWS SDK for Java, you can return the value of the first column for each record that is stored in an object that contains data stored in CSV format. You can also request `Progress` and `Stats` messages to be returned. You must provide a valid bucket name and an object that contains data in CSV format.

For examples of how to use Amazon S3 Select with the AWS SDK for Java, see [Select content from an object](../API/s3_example_s3_SelectObjectContent_section.md "../API/s3_example_s3_SelectObjectContent_section.md") in the _Amazon S3 API Reference_.

JavaScript
For a JavaScript example that uses the AWS SDK for JavaScript with the S3
`SelectObjectContent` API operation to select records
from JSON and CSV files that are stored in Amazon S3, see the blog post
[Introducing support for Amazon S3 Select in the AWS SDK for JavaScript](https://aws.amazon.com/blogs/developer/introducing-support-for-amazon-s3-select-in-the-aws-sdk-for-javascript/ "https://aws.amazon.com/blogs/developer/introducing-support-for-amazon-s3-select-in-the-aws-sdk-for-javascript/").

Python
For a Python example of using SQL queries to search through data
that was loaded to Amazon S3 as a comma-separated value (CSV) file by
using S3 Select, see the blog post [Querying data without servers or databases using Amazon S3
Select](https://aws.amazon.com/blogs/storage/querying-data-without-servers-or-databases-using-amazon-s3-select/ "https://aws.amazon.com/blogs/storage/querying-data-without-servers-or-databases-using-amazon-s3-select/").
