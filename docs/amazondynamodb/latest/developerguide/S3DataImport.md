# Best practices for importing from Amazon S3 into

DynamoDB

The following are the best practices for importing data from Amazon S3 into DynamoDB.

## Stay under the limit of 50,000 S3

objects

Each import job supports a maximum of 50,000 S3 objects. If your dataset contains more
than 50,000 objects, consider consolidating them into larger objects.

## Avoid excessively large

S3 objects

S3 objects are imported in parallel. Having numerous mid-sized S3 objects allows for
parallel execution without excessive overhead. For items under 1 KB, consider placing
4,000,000 items into each S3 object. If you have a larger average item size, place
proportionally fewer items into each S3 object.

## Randomize sorted

data

If an S3 object holds data in sorted order, it can create a _rolling hot partition_. This is a situation where one partition receives
all the activity, and then the next partition after that, and so on. Data in sorted
order is defined as items in sequence in the S3 object that will be written to the same
target partition during the import. One common situation where data is in sorted order
is a CSV file where items are sorted by partition key so that repeated items share the
same partition key.

To avoid a rolling hot partition, we recommend that you randomize the order in these
cases. This can improve performance by spreading the write operations. For more
information, see [Distributing write activity efficiently during
data upload in DynamoDB](bp-partition-key-data-upload.md "bp-partition-key-data-upload.md").

## Compress data to keep the

total S3 object size below the Regional limit

In the [import from S3 process](S3DataImport.md "S3DataImport.md"), there is
a limit on the sum total size of the S3 object data to be imported. The limit is 15 TB
in the us-east-1, us-west-2, and eu-west-1 Regions, and 1 TB in all other Regions. The
limit is based on the raw S3 object sizes.

Compression allows more raw data to fit within the limit. If compression alone isn’t
sufficient to fit the import within the limit, you can also contact [AWS Premium Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") for a quota
increase.

## Be aware of how item size impacts

performance

If your average item size is very small (below 200 bytes), the import process might
take a little longer than for larger item sizes.

## Do not modify S3 objects

during active imports

Ensure that your source S3 objects remain unchanged while an import operation is in
progress. If an S3 object is modified during an import, the operation will fail with
error code `ObjectModifiedInS3DuringImport` and the message "The S3 object
could not be imported because it was overwritten."

If you encounter this error, restart the import operation with a stable version of
your S3 object. To avoid this issue, wait for the current import to complete before
making changes to the source files.

## Consider importing without any Global

Secondary Indexes

The duration of an import task may depend on the presence of one or multiple global
secondary indexes (GSIs). If you plan to establish indexes with partition keys that have
low cardinality, you may see a faster import if you defer index creation until after the
import task is finished (rather than including them in the import job).

###### Note

Creating a GSI during the import does not incur write charges (creating a GSI
after the import would).
