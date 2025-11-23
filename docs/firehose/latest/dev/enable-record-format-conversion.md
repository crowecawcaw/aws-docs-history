# Enable record format conversion

If you enable record format conversion, you can't set your Amazon Data Firehose destination to be
Amazon OpenSearch Service, Amazon Redshift, or Splunk. With format conversion enabled, Amazon S3 is the
only destination that you can use for your Firehose stream. The following section shows how
to enable record format conversion from console and Firehose API operations. For an example
of how to set up record format conversion with CloudFormation, see [AWS::DataFirehose::DeliveryStream](../../../AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.md#aws-resource-kinesisfirehose-deliverystream--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.md#aws-resource-kinesisfirehose-deliverystream--examples").

## Enable record format conversion

from console

You can enable data format conversion on the console when you create or update a
Firehose stream. With data format conversion enabled, Amazon S3 is the only destination that
you can configure for the Firehose stream. Also, Amazon S3 compression gets disabled when you
enable format conversion. However, Snappy compression happens automatically as part of
the conversion process. The framing format for Snappy that Amazon Data Firehose uses in this case is
compatible with Hadoop. This means that you can use the results of the Snappy
compression and run queries on this data in Athena. For the Snappy framing format that
Hadoop relies on, see [BlockCompressorStream.java](https://github.com/apache/hadoop/blob/f67237cbe7bc48a1b9088e990800b37529f1db2a/hadoop-common-project/hadoop-common/src/main/java/org/apache/hadoop/io/compress/BlockCompressorStream.java "https://github.com/apache/hadoop/blob/f67237cbe7bc48a1b9088e990800b37529f1db2a/hadoop-common-project/hadoop-common/src/main/java/org/apache/hadoop/io/compress/BlockCompressorStream.java").

###### To enable data format conversion for a data Firehose stream

1. Sign in to the AWS Management Console, and open the Amazon Data Firehose console at
   [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/ "https://console.aws.amazon.com/firehose/").
2. Choose a Firehose stream to update, or create a new Firehose stream by
   following the steps in [Tutorial: Create a Firehose stream from console](basic-create.md "basic-create.md").
3. Under **Convert record format**, set **Record format
   conversion** to **Enabled**.
4. Choose the output format that you want. For more information about the two
   options, see [Apache Parquet](https://parquet.apache.org/ "https://parquet.apache.org/") and
   [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/").
5. Choose an AWS Glue table to specify a schema for your source records. Set the
   Region, database, table, and table version.

## Manage record format conversion

from Firehose API

If you want Amazon Data Firehose to convert the format of your input data from JSON to Parquet or
ORC, specify the optional [DataFormatConversionConfiguration](../APIReference/API_DataFormatConversionConfiguration.md "../APIReference/API_DataFormatConversionConfiguration.md") element in [ExtendedS3DestinationConfiguration](../APIReference/API_ExtendedS3DestinationConfiguration.md "../APIReference/API_ExtendedS3DestinationConfiguration.md") or in [ExtendedS3DestinationUpdate](../APIReference/API_ExtendedS3DestinationUpdate.md "../APIReference/API_ExtendedS3DestinationUpdate.md"). If you specify [DataFormatConversionConfiguration](../APIReference/API_DataFormatConversionConfiguration.md "../APIReference/API_DataFormatConversionConfiguration.md"), the following restrictions apply.

- In [BufferingHints](../APIReference/API_BufferingHints.md "../APIReference/API_BufferingHints.md"), you can't set `SizeInMBs` to a value
  less than 64 if you enable record format conversion. Also, when format
  conversion isn't enabled, the default value is 5. The value becomes 128 when you
  enable it.
- You must set `CompressionFormat` in [ExtendedS3DestinationConfiguration](../APIReference/API_ExtendedS3DestinationConfiguration.md "../APIReference/API_ExtendedS3DestinationConfiguration.md") or in [ExtendedS3DestinationUpdate](../APIReference/API_ExtendedS3DestinationUpdate.md "../APIReference/API_ExtendedS3DestinationUpdate.md") to `UNCOMPRESSED`. The
  default value for `CompressionFormat` is `UNCOMPRESSED`.
  Therefore, you can also leave it unspecified in [ExtendedS3DestinationConfiguration](../APIReference/API_ExtendedS3DestinationConfiguration.md "../APIReference/API_ExtendedS3DestinationConfiguration.md"). The data still gets compressed
  as part of the serialization process, using Snappy compression by default. The
  framing format for Snappy that Amazon Data Firehose uses in this case is compatible with Hadoop.
  This means that you can use the results of the Snappy compression and run
  queries on this data in Athena. For the Snappy framing format that Hadoop relies
  on, see [BlockCompressorStream.java](https://github.com/apache/hadoop/blob/f67237cbe7bc48a1b9088e990800b37529f1db2a/hadoop-common-project/hadoop-common/src/main/java/org/apache/hadoop/io/compress/BlockCompressorStream.java "https://github.com/apache/hadoop/blob/f67237cbe7bc48a1b9088e990800b37529f1db2a/hadoop-common-project/hadoop-common/src/main/java/org/apache/hadoop/io/compress/BlockCompressorStream.java"). When you configure the serializer, you
  can choose other types of compression.
