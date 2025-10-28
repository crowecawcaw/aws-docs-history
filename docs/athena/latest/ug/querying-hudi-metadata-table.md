# Use Hudi metadata for improved

performance

The Apache Hudi has a [metadata table](https://hudi.apache.org/docs/next/metadata/ "https://hudi.apache.org/docs/next/metadata/") that contains indexing features for improved performance
like file listing, data skipping using column statistics, and a bloom filter based
index.

Of these features, Athena currently supports only the file listing index. The file
listing index eliminates file system calls like "list files" by fetching the information
from an index which maintains a partition to files mapping. This removes the need to
recursively list each and every partition under the table path to get a view of the file
system. When you work with large datasets, this indexing drastically reduces the latency
that would otherwise occur when getting the list of files during writes and queries. It
also avoids bottlenecks like request limits throttling on Amazon S3 `LIST`
calls.

###### Note

Athena does not support data skipping or bloom filter indexing at this time.

## Enabling the Hudi metadata table

Metadata table based file listing is disabled by default. To enable the Hudi
metadata table and the related file listing functionality, set the
`hudi.metadata-listing-enabled` table property to
`TRUE`.

###### Example

The following `ALTER TABLE SET TBLPROPERTIES` example enables the
metadata table on the example `partition_cow` table.

```
ALTER TABLE partition_cow SET TBLPROPERTIES('hudi.metadata-listing-enabled'='TRUE')
```

## Use bootstrap

generated metadata

Starting in Apache Hudi version 0.6.0, the bootstrap operation feature provides
better performance with existing Parquet datasets. Instead of rewriting the dataset,
a bootstrap operation can generate metadata only, leaving the dataset in place.

You can use Athena to query tables from a bootstrap operation just like other
tables based on data in Amazon S3. In your `CREATE TABLE` statement, specify
the Hudi table path in your `LOCATION` clause.

For more information about creating Hudi tables using the bootstrap operation in
Amazon EMR, see the article [New
features from Apache Hudi available in Amazon EMR](https://aws.amazon.com/blogs/big-data/new-features-from-apache-hudi-available-in-amazon-emr/ "https://aws.amazon.com/blogs/big-data/new-features-from-apache-hudi-available-in-amazon-emr/") in the AWS Big Data
Blog.
