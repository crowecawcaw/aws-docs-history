# Using data

compression

When you use Hive to copy data among different data sources, you can request
on-the-fly data compression. Hive provides several compression codecs. You can
choose one during your Hive session. When you do this, the data is compressed in the
specified format.

The following example compresses data using the Lempel-Ziv-Oberhumer (LZO)
algorithm.

```
SET hive.exec.compress.output=true;
SET io.seqfile.compression.type=BLOCK;
SET mapred.output.compression.codec = com.hadoop.compression.lzo.LzopCodec;

CREATE EXTERNAL TABLE `lzo_compression_table` (line STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n'
LOCATION '`s3://bucketname/path/subpath/`';

INSERT OVERWRITE TABLE `lzo_compression_table` SELECT *
FROM `hiveTableName`;
```

The resulting file in Amazon S3 will have a system-generated name with
`.lzo` at the end (for example,
`8d436957-57ba-4af7-840c-96c2fc7bb6f5-000000.lzo`).

The available compression codecs are:

- `org.apache.hadoop.io.compress.GzipCodec`
- `org.apache.hadoop.io.compress.DefaultCodec`
- `com.hadoop.compression.lzo.LzoCodec`
- `com.hadoop.compression.lzo.LzopCodec`
- `org.apache.hadoop.io.compress.BZip2Codec`
- `org.apache.hadoop.io.compress.SnappyCodec`
