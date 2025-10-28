# Troubleshoot dynamic partitioning

errors

If Amazon Data Firehose is not able to parse data records in your Firehose stream or
it fails to extract the specified partitioning keys, or to evaluate the expressions
included in the S3 prefix value, these data records are delivered to the S3 error bucket
prefix that you must specify when you create the Firehose stream where you enable
dynamic partitioning. The S3 error bucket prefix contains all the records that Firehose is not able to deliver to the specified S3 destination. These records are
organized based on the error type. Along with the record, the delivered object also
includes information about the error to help understand and resolve the error.

You must specify an S3 error bucket prefix for a Firehose stream if you want to enable
dynamic partitioning for this Firehose stream. If you don't want to enable dynamic
partitioning for a Firehose stream, specifying an S3 error bucket prefix is optional.
