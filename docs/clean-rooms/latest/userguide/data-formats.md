# Data formats for AWS Clean Rooms

To
analyze
data, the datasets must be in a format that AWS Clean Rooms supports. ​

###### Topics

- [Supported data formats for PySpark jobs](#supported-data-formats-pyspark "#supported-data-formats-pyspark")
- [Supported data
  formats for SQL
  queries](#supported-data-formats "#supported-data-formats")
- [Supported data types](#data-types "#data-types")
- [File compression types for AWS Clean Rooms](#compression-types "#compression-types")
- [Server-side encryption for AWS Clean Rooms](#server-side-encryption "#server-side-encryption")

## Supported data formats for PySpark jobs

AWS Clean Rooms supports the following structured formats for running PySpark jobs.

- Parquet
- OpenCSV
- JSON

## Supported data

formats for SQL
queries

AWS Clean Rooms supports different structured
formats for running SQL
queries, depending on whether you choose the Spark SQL analytics engine or the
AWS Clean Rooms SQL analytics engine.

Spark SQL analytics engine

- [Apache Iceberg
  tables](iceberg-tables.md "iceberg-tables.md")
- Parquet
- OpenCSV
- JSON

AWS Clean Rooms SQL analytics engine

- [Apache Iceberg
  tables](iceberg-tables.md "iceberg-tables.md")
- Parquet
- RCFile
- TextFile
- SequenceFile
- RegexSerde
- OpenCSV
- AVRO
- JSON

###### Note

A `timestamp` value in a text file must be in the format `yyyy-MM-dd
 HH:mm:ss.SSSSSS`. For example: `2017-05-01 11:30:59.000000`. ​

We recommend using a columnar storage file format, such as Apache Parquet.
With a columnar storage file format, you can minimize data movement by selecting only the columns
that you need. ​ For optimal performance, large objects should be split into 100mb–1gb
objects.

## Supported data types

AWS Clean Rooms supports different types, depending on whether you choose the Spark SQL analytics
engine or the AWS Clean Rooms SQL analytics engine.

Spark SQL analytics engine

- ARRAY
- BIGINT
- BOOLEAN
- BYTE
- CHAR
- DATE
- DECIMAL
- FLOAT
- INTEGER
- INTERVAL
- LONG
- MAP
- REAL
- SHORT
- SMALLINT
- STRUCT
- TIME
- TIMESTAMP_LTZ
- TIMESTAMP_NTZ
- TINYINT
- VARCHAR

For more information, see [Data
types](../sql-reference/s_Supported_data_types.md "../sql-reference/s_Supported_data_types.md") in the _AWS Clean Rooms SQL Reference_.

AWS Clean Rooms SQL

- ARRAY
- BIGINT
- BOOLEAN
- CHAR
- DATE
- DECIMAL
- DOUBLE PRECISION
- INTEGER
- MAP
- REAL
- SMALLINT
- STRUCT
- SUPER
- TIME
- TIMESTAMP
- TIMESTAMPTZ
- TIMETZ
- VARBYTE
- VARCHAR

For more information, see [Data
types](../sql-reference/s_Supported_data_types.md "../sql-reference/s_Supported_data_types.md") in the _AWS Clean Rooms SQL Reference_.

## File compression types for AWS Clean Rooms

To reduce storage space, improve performance, and minimize costs, we strongly recommend that
you compress your datasets.

AWS Clean Rooms recognizes file compression types based on the file extension and supports the
compression types and extensions shown in the following table. ​

| Compression algorithm | File extension |
| --------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| GZIP                  | .gz            |
| Bzip2                 | .bz2           |
| Snappy                | .snappy        | You can apply compression at different levels. Most commonly, you compress a whole file or compress individual blocks within a file. Compressing columnar formats at the file level doesn't yield performance benefits. ​ ## Server-side encryption for AWS Clean Rooms ###### Note Server-side encryption does not replace cryptographic computing for those use cases that require it. AWS Clean Rooms transparently decrypts datasets that are encrypted using the following encryption options: ​ <br>• **SSE-S3** – Server-side encryption using an AES-256 encryption key managed by Amazon S3 <br>• **SSE-KMS** – Server-side encryption with keys managed by AWS Key Management Service To use SSE-S3, the AWS Clean Rooms service role used to associate the configured table to the collaboration must have KMS-decrypt permissions. To use SSE-KMS, the KMS key policy must also allow the AWS Clean Rooms service role to decrypt. ​ AWS Clean Rooms doesn't support Amazon S3 client-side encryption. For more information about server-side encryption, see [Protecting data using server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the _Amazon Simple Storage Service User Guide_. ​ |
