# Use Amazon S3 bucket prefix to deliver

data

When you create a Firehose stream that uses Amazon S3 as the destination, you must specify an
Amazon S3 bucket where Firehose is to deliver your data. Amazon S3 bucket prefixes are used to
organize the data that you store in your S3 buckets. An Amazon S3 bucket prefix is similar to
a directory that enables you to group similar objects together.

With dynamic partitioning, your partitioned data is delivered into the specified Amazon S3
prefixes. If you don't enable dynamic partitioning, specifying an S3 bucket prefix for
your Firehose stream is optional. However, if you choose to enable dynamic partitioning, you
must specify the S3 bucket prefixes to which Firehose delivers partitioned data.

In every Firehose stream where you enable dynamic partitioning, the S3 bucket prefix value
consists of expressions based on the specified partitioning keys for that Firehose stream.
Using the above data record example again, you can build the following S3 prefix value
that consists of expressions based on the partitioning keys defined above:

```

"ExtendedS3DestinationConfiguration": {
"BucketARN": "arn:aws:s3:::my-logs-prod",
"Prefix": "customer_id=!{partitionKeyFromQuery:customer_id}/
    device=!{partitionKeyFromQuery:device}/
    year=!{partitionKeyFromQuery:year}/
    month=!{partitionKeyFromQuery:month}/
    day=!{partitionKeyFromQuery:day}/
    hour=!{partitionKeyFromQuery:hour}/"
}

```

Firehose evaluates the above expression at runtime. It groups records that match the same
evaluated S3 prefix expression into a single data set. Firehose then delivers each data set
to the evaluated S3 prefix. The frequency of data set delivery to S3 is determined by
the Firehose stream buffer setting. As a result, the record in this example is delivered to
the following S3 object key:

```

s3://my-logs-prod/customer_id=1234567890/device=mobile/year=2019/month=08/day=09/hour=20/my-delivery-stream-2019-08-09-23-55-09-a9fa96af-e4e4-409f-bac3-1f804714faaa

```

For dynamic partitioning, you must use the following expression format in your S3
bucket prefix: `!{namespace:value}`, where namespace can be either
`partitionKeyFromQuery` or `partitionKeyFromLambda`, or both.
If you are using inline parsing to create the partitioning keys for your source data,
you must specify an S3 bucket prefix value that consists of expressions specified in the
following format: `"partitionKeyFromQuery:keyID"`. If you are using an AWS
Lambda function to create partitioning keys for your source data, you must specify an S3
bucket prefix value that consists of expressions specified in the following format:
`"partitionKeyFromLambda:keyID"`.

###### Note

You can also specify the S3 bucket prefix value using the hive style format, for
example customer_id=!{partitionKeyFromQuery:customer_id}.

For more information, see the "Choose Amazon S3 for Your Destination" in [Creating an Amazon Firehose stream](basic-create.md "basic-create.md") and [Custom Prefixes for Amazon S3 Objects](s3-prefixes.md "s3-prefixes.md").

## Add a new line delimiter when

delivering data to Amazon S3

You can enable **New Line Delimiter** to add a new line delimiter
between records in objects that are delivered to Amazon S3. This can be helpful for parsing
objects in Amazon S3. This is also particularly useful when dynamic partitioning is applied
to aggregated data because multi-record deaggregation (which must be applied to
aggregated data before it can be dynamically partitioned) removes new lines from records
as part of the parsing process.
