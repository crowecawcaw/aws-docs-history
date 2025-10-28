# Amazon S3 connections

You can use AWS Glue for Spark to read and write files in Amazon S3. AWS Glue for Spark supports many common data formats
stored in Amazon S3 out of the box, including CSV, Avro, JSON, Orc and Parquet. For more information about supported
data formats, see [Data format options for inputs and outputs in
AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md"). Each data format may support a different
set of AWS Glue features. Consult the page for your data format for the specifics of feature support. Additionally,
you can read and write versioned files stored in the Hudi, Iceberg and Delta Lake data lake frameworks. For more
information about data lake frameworks, see [Using data lake
frameworks with AWS Glue ETL jobs](aws-glue-programming-etl-datalake-native-frameworks.md "aws-glue-programming-etl-datalake-native-frameworks.md").

With AWS Glue you can partition your Amazon S3 objects into a folder structure while writing, then retrieve it by
partition to improve performance using simple configuration. You can also set configuration to group small files
together when transforming your data to improve performance. You can read and write `bzip2` and
`gzip` archives in Amazon S3.

###### Topics

- [Configuring S3 connections](#aws-glue-programming-etl-connect-s3-configure "#aws-glue-programming-etl-connect-s3-configure")
- [Amazon S3 connection option reference](#aws-glue-programming-etl-connect-s3 "#aws-glue-programming-etl-connect-s3")
- [Deprecated connection syntaxes for data formats](#aws-glue-programming-etl-connect-legacy-format "#aws-glue-programming-etl-connect-legacy-format")
- [Excluding Amazon S3 storage classes](aws-glue-programming-etl-storage-classes.md "aws-glue-programming-etl-storage-classes.md")
- [Managing partitions for ETL output in AWS Glue](aws-glue-programming-etl-partitions.md "aws-glue-programming-etl-partitions.md")
- [Reading input files in larger groups](grouping-input-files.md "grouping-input-files.md")
- [Amazon VPC endpoints for Amazon S3](vpc-endpoints-s3.md "vpc-endpoints-s3.md")

## Configuring S3 connections

To connect to Amazon S3 in a AWS Glue with Spark job, you will need some prerequisites:

- The AWS Glue job must have IAM permissions for relevant Amazon S3 buckets.

In certain cases, you will need to configure additional prerequisites:

- When configuring cross-account access, appropriate access controls on the Amazon S3 bucket.
- For security reasons, you may choose to route your Amazon S3 requests through an Amazon VPC.
  This approach can introduce bandwidth and availability challenges. For more information, see
  [Amazon VPC endpoints for Amazon S3](vpc-endpoints-s3.md "vpc-endpoints-s3.md").

## Amazon S3 connection option reference

Designates a connection to Amazon S3.

Since Amazon S3 manages files rather than tables, in addition to specifying the connection properties provided
in this document, you will need to specify additional configuration about your file type. You specify this
information through data format options. For more information about format options, see [Data format options for inputs and outputs in
AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md"). You can also specify this information by integrating with the
AWS Glue Data Catalog.

For an example of the distinction between connection options and format options, consider how
the [create_dynamic_frame_from_options](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_options "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_options") method
takes `connection_type`, `connection_options`, `format` and
`format_options`. This section specifically discusses parameters provided to
`connection_options`.

Use the following connection options with `"connectionType": "s3"`:

- `"paths"`: (Required) A list of the Amazon S3 paths to read from.
- `"exclusions"`: (Optional) A string containing a JSON list of Unix-style
  glob patterns to exclude. For example, `"[\"**.pdf\"]"` excludes all PDF files.
  For more information about the glob syntax that AWS Glue supports, see [Include and Exclude Patterns](define-crawler.md#crawler-data-stores-exclude "define-crawler.md#crawler-data-stores-exclude").
- `"compressionType"`: or "`compression`": (Optional) Specifies
  how the data is compressed. Use `"compressionType"` for Amazon S3 sources and
  `"compression"` for Amazon S3 targets. This is generally not necessary if the data
  has a standard file extension. Possible values are `"gzip"` and
  `"bzip2"`). Additional compression formats may be supported for specific formats.
  For the specifics of feature support, consult the data format page.
- `"groupFiles"`: (Optional) Grouping files is turned on by default when the
  input contains more than 50,000 files. To turn on grouping with fewer than 50,000 files,
  set this parameter to `"inPartition"`. To disable grouping when there are more
  than 50,000 files, set this parameter to `"none"`.
- `"groupSize"`: (Optional) The target group size in bytes. The default is
  computed based on the input data size and the size of your cluster. When there are fewer
  than 50,000 input files, `"groupFiles"` must be set to
  `"inPartition"` for this to take effect.
- `"recurse"`: (Optional) If set to true, recursively reads files in all
  subdirectories under the specified paths.
- `"maxBand"`: (Optional, advanced) This option controls the duration in
  milliseconds after which the `s3` listing is likely to be consistent. Files
  with modification timestamps falling within the last `maxBand` milliseconds are
  tracked specially when using `JobBookmarks` to account for Amazon S3 eventual
  consistency. Most users don't need to set this option. The default is 900000 milliseconds,
  or 15 minutes.
- `"maxFilesInBand"`: (Optional, advanced) This option specifies the maximum
  number of files to save from the last `maxBand` seconds. If this number is
  exceeded, extra files are skipped and only processed in the next job run. Most users don't
  need to set this option.
- `"isFailFast"`: (Optional) This option determines if an AWS Glue ETL job
  throws reader parsing exceptions. If set to `true`, jobs fail fast if four
  retries of the Spark task fail to parse the data correctly.
- `"catalogPartitionPredicate"`: (Optional) Used for Read. The contents of a SQL `WHERE`
  clause. Used when reading from Data Catalog tables with a very large quantity of partitions.
  Retrieves matching partitions from Data Catalog indices. Used with `push_down_predicate`, an option on the
  [create_dynamic_frame_from_catalog](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_catalog "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_catalog")
  method (and other similar methods). For more information, see [Server-side filtering using catalog partition predicates](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-cat-predicates "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-cat-predicates").
- `"partitionKeys"`: (Optional) Used for Write. An array of column label strings.
  AWS Glue will partition your data as specified by this configuration. For more information, see [Writing partitions](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-writing "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-writing").
- `"excludeStorageClasses"`: (Optional) Used for Read. An array of strings specifying Amazon S3
  storage classes. AWS Glue will exclude Amazon S3 objects based on this configuration. For more information,
  see [Excluding Amazon S3 storage classes](aws-glue-programming-etl-storage-classes.md "aws-glue-programming-etl-storage-classes.md").

## Deprecated connection syntaxes for data formats

Certain data formats can be accessed using a specific connection type syntax. This syntax is deprecated. We
recommend you specify your formats using the `s3` connection type and the format options provided
in [Data format options for inputs and outputs in
AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md") instead.

### "connectionType": "Orc"

Designates a connection to files stored in Amazon S3 in the [Apache Hive
Optimized Row Columnar (ORC)](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC") file format.

Use the following connection options with `"connectionType": "orc"`:

- `paths`: (Required) A list of the Amazon S3 paths to read from.
- _(Other option name/value pairs)_: Any additional options,
  including formatting options, are passed directly to the SparkSQL `DataSource`.

### "connectionType": "parquet"

Designates a connection to files stored in Amazon S3 in the [Apache Parquet](https://parquet.apache.org/docs/ "https://parquet.apache.org/docs/") file
format.

Use the following connection options with `"connectionType": "parquet"`:

- `paths`: (Required) A list of the Amazon S3 paths to read from.
- _(Other option name/value pairs)_: Any additional options,
  including formatting options, are passed directly to the SparkSQL `DataSource`.
