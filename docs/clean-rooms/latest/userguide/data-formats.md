

# Data formats for AWS Clean Rooms
<a name="data-formats"></a>

To analyze data, the datasets must be in a format that AWS Clean Rooms supports. ​

**Topics**
+ [Supported data formats for PySpark jobs](#supported-data-formats-pyspark)
+ [Supported data formats for SQL queries](#supported-data-formats)
+ [Supported data types](#data-types)
+ [File compression types for AWS Clean Rooms](#compression-types)
+ [Server-side encryption for AWS Clean Rooms](#server-side-encryption)

## Supported data formats for PySpark jobs
<a name="supported-data-formats-pyspark"></a>

AWS Clean Rooms supports the following structured formats for running PySpark jobs.
+ Parquet
+ OpenCSV
+ JSON

## Supported data formats for SQL queries
<a name="supported-data-formats"></a>

AWS Clean Rooms supports the following structured formats for running SQL queries.
+ [Apache Iceberg tables](iceberg-tables.md)
+ Parquet
+ OpenCSV
+ JSON

**Note**  
A `timestamp` value in a text file must be in the format `yyyy-MM-dd HH:mm:ss.SSSSSS`. For example: `2017-05-01 11:30:59.000000`. ​ 

We recommend using a columnar storage file format, such as Apache Parquet. With a columnar storage file format, you can minimize data movement by selecting only the columns that you need. ​ For optimal performance, large objects should be split into 100mb–1gb objects.

## Supported data types
<a name="data-types"></a>

AWS Clean Rooms supports the following data types.
+ ARRAY
+ BIGINT
+ BOOLEAN
+ BYTE
+ CHAR
+ DATE
+ DECIMAL
+ FLOAT
+ INTEGER
+ INTERVAL
+ LONG
+ MAP
+ REAL
+ SHORT
+ SMALLINT
+ STRUCT
+ TIME
+ TIMESTAMP\_LTZ
+ TIMESTAMP\_NTZ
+ TINYINT
+ VARCHAR

For more information, see [Data types](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_Supported_data_types.html) in the *AWS Clean Rooms SQL Reference*.

## File compression types for AWS Clean Rooms
<a name="compression-types"></a>

To reduce storage space, improve performance, and minimize costs, we strongly recommend that you compress your datasets. 

AWS Clean Rooms recognizes file compression types based on the file extension and supports the compression types and extensions shown in the following table. ​ 


| Compression algorithm  | File extension  | 
| --- | --- | 
| GZIP | .gz  | 
| Bzip2 | .bz2  | 
| Snappy | .snappy | 
| Zstandard (Zstd) | .zstd | 

You can apply compression at different levels. Most commonly, you compress a whole file or compress individual blocks within a file. Compressing columnar formats at the file level doesn't yield performance benefits. ​

## Server-side encryption for AWS Clean Rooms
<a name="server-side-encryption"></a>

**Note**  
Server-side encryption does not replace cryptographic computing for those use cases that require it.

AWS Clean Rooms transparently decrypts datasets that are encrypted using the following encryption options: ​ 
+ **SSE-S3** – Server-side encryption using an AES-256 encryption key managed by Amazon S3
+ **SSE-KMS** – Server-side encryption with keys managed by AWS Key Management Service 

To use SSE-S3, the AWS Clean Rooms service role used to associate the configured table to the collaboration must have KMS-decrypt permissions. To use SSE-KMS, the KMS key policy must also allow the AWS Clean Rooms service role to decrypt. ​ 

AWS Clean Rooms doesn't support Amazon S3 client-side encryption. For more information about server-side encryption, see [Protecting data using server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) in the *Amazon Simple Storage Service User Guide*. ​ 