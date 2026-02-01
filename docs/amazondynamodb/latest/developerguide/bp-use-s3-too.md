# Best practices for storing large items and attributes in DynamoDB

Amazon DynamoDB limits the size of each item that you store in a table to 400 KB (see [Item size](Constraints.md#limits-items-size "Constraints.md#limits-items-size")). If your application needs to store
more data in an item than the DynamoDB size limit permits, you can try compressing one or more
large attributes or breaking the item into multiple items (efficiently indexed by sort keys).
You can also store the item as an object in Amazon Simple Storage Service (Amazon S3) and store the Amazon S3 object identifier
in your DynamoDB item.

As a best practice, you should utilize the [`ReturnConsumedCapacity`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/model/ReturnConsumedCapacity.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/model/ReturnConsumedCapacity.md") parameter when writing items to monitor and
alert on items sizes that approach the 400 KB maximum item size. Exceeding the maximum item size
will result in failed write attempts. DynamoDB will return a [ValidationException error](Programming.md "Programming.md"). Monitoring and alerting on item sizes will enable you to
mitigate the items size issues before they impact your application.

## Compressing large attribute values

Compressing large attribute values can let them fit within item limits in DynamoDB and reduce
your storage costs. Compression algorithms such as GZIP or LZO produce binary output that you
can then store in a `Binary` attribute type within the item.

As an example, consider a table that stores messages written by forum users. Such messages
often contain long strings of text, which are candidates for compression. While compression
can reduce item sizes, the downside is that the compressed attribute values are not useful for
filtering.

For sample code that demonstrates how to compress such messages in DynamoDB, see the
following:

- [Example: Handling binary type attributes
  using the AWS SDK for Java document API](JavaDocumentAPIBinaryTypeExample.md "JavaDocumentAPIBinaryTypeExample.md")
- [Example: Handling binary type attributes
  using the AWS SDK for .NET low-level API](LowLevelDotNetBinaryTypeExample.md "LowLevelDotNetBinaryTypeExample.md")

## Vertical partitioning

An alternative solution to dealing with large items is to break them down into smaller
chunks of data and associating all relevant items by the partition key value. You can then use
a sort key string to identify the associated information stored alongside it. By doing this,
and having multiple items grouped by the same partition key value, you are creating an [item collection](WorkingWithItemCollections.md "WorkingWithItemCollections.md").

For more information on this approach, see:

- [Use vertical partitioning to scale data efficiently in Amazon DynamoDB](https://aws.amazon.com/blogs/database/use-vertical-partitioning-to-scale-data-efficiently-in-amazon-dynamodb/ "https://aws.amazon.com/blogs/database/use-vertical-partitioning-to-scale-data-efficiently-in-amazon-dynamodb/")
- [Implement vertical partitioning in Amazon DynamoDB using AWS Glue](https://aws.amazon.com/blogs/database/implement-vertical-partitioning-in-amazon-dynamodb-using-aws-glue/ "https://aws.amazon.com/blogs/database/implement-vertical-partitioning-in-amazon-dynamodb-using-aws-glue/")

## Storing large attribute values in Amazon S3

As mentioned previously, you can also use Amazon S3 to store large attribute values that cannot
fit in a DynamoDB item. You can store them as an object in Amazon S3 and then store the object
identifier in your DynamoDB item.

You can also use the object metadata support in Amazon S3 to provide a link back to the parent
item in DynamoDB. Store the primary key value of the item as Amazon S3 metadata of the object in Amazon S3.
Doing this often helps with maintenance of the Amazon S3 objects.

For example, consider the `ProductCatalog` table. Items in this table store
information about item price, description, book authors, and dimensions for other products. If
you wanted to store an image of each product that was too large to fit in an item, you could
store the images in Amazon S3 instead of in DynamoDB.

When implementing this strategy, keep the following in mind:

- DynamoDB doesn't support transactions that cross Amazon S3 and DynamoDB. Therefore, your
  application must deal with any failures, which could include cleaning up orphaned Amazon S3
  objects.
- Amazon S3 limits the length of object identifiers. So you must organize your data in a way
  that doesn't generate excessively long object identifiers or violate other Amazon S3
  constraints.

For more information about how to use Amazon S3, see the [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md").
