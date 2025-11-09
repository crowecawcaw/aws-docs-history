# Data format options for inputs and outputs in

AWS Glue for Spark

These pages offer information about feature support and configuration parameters for data formats supported by
AWS Glue for Spark. See the following for a description of the usage and applicablity of this information.

## Feature support across data formats in AWS Glue

Each data format may support different AWS Glue features. The following common features may or may not be supported based on your format type.
Refer to the documentation for your data format to understand how to leverage our features to meet your requirements.

|                   |                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Read              | AWS Glue can recognize and interpret this data format without additional resources, such as connectors.                                                                                                                                                                                                                                                                                                        |
| Write             | AWS Glue can write data in this format without additional resources. You can include third-party libraries<br>in your job and use standard Apache Spark functions to write data, as you would in other Spark<br>environments. For more information about including libraries, see [Using Python libraries with AWS Glue](aws-glue-programming-python-libraries.md "aws-glue-programming-python-libraries.md"). |
| Streaming read    | AWS Glue can recognize and interpret this data format from an Apache Kafka, Amazon Managed Streaming for Apache Kafka or Amazon Kinesis message<br>stream. We expect streams to present data in a consistent format, so they are read in as<br>`DataFrames`.                                                                                                                                                   |
| Group small files | AWS Glue can group files together to batch work sent to each node when performing AWS Glue transforms. This can significantly<br>improve performance for workloads involving large amounts of small files. For more information, see<br>[Reading input files in larger groups](grouping-input-files.md "grouping-input-files.md").                                                                             |
| Job bookmarks     | AWS Glue can track the progress of transforms performing the same work on the same dataset across job<br>runs with job bookmarks. This can improve performance for workloads involving datasets where work only<br>needs to be done on new data since the last job run. For more information, see [Tracking processed data using job bookmarks](monitor-continuations.md "monitor-continuations.md").          |

## Parameters used to interact with data formats in AWS Glue

Certain AWS Glue connection types support multiple `format` types, requiring you to specify
information about your data format with a `format_options` object when using methods like
`GlueContext.write_dynamic_frame.from_options`.

- `s3` – For more information, see Connection types and options for ETL in AWS Glue: [S3 connection parameters](aws-glue-programming-etl-connect-s3-home.md#aws-glue-programming-etl-connect-s3 "aws-glue-programming-etl-connect-s3-home.md#aws-glue-programming-etl-connect-s3"). You
  can also view the documentation for the methods facilitating this connection type: [create_dynamic_frame_from_options](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_options "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_options") and [write_dynamic_frame_from_options](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-write_dynamic_frame_from_options "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-write_dynamic_frame_from_options") in Python
  and the corresponding Scala methods [def getSourceWithFormat](glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getSourceWithFormat "glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getSourceWithFormat") and [def getSinkWithFormat](glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getSinkWithFormat "glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getSinkWithFormat").
- `kinesis` – For more information, see Connection types and options for ETL in AWS Glue:
  [Kinesis connection parameters](aws-glue-programming-etl-connect-kinesis-home.md#aws-glue-programming-etl-connect-kinesis "aws-glue-programming-etl-connect-kinesis-home.md#aws-glue-programming-etl-connect-kinesis"). You can also view the documentation for the method
  facilitating this connection type: [create_data_frame_from_options](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create-dataframe-from-options "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create-dataframe-from-options")
  and the corresponding Scala method [def createDataFrameFromOptions](glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-createDataFrameFromOptions "glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-createDataFrameFromOptions").
- `kafka` – For more information, see Connection types and options for ETL in AWS Glue: [Kafka connection parameters](aws-glue-programming-etl-connect-kafka-home.md#aws-glue-programming-etl-connect-kafka "aws-glue-programming-etl-connect-kafka-home.md#aws-glue-programming-etl-connect-kafka"). You can also view the documentation for the method facilitating this connection type: [create_data_frame_from_options](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create-dataframe-from-options "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create-dataframe-from-options") and the
  corresponding Scala method [def createDataFrameFromOptions](glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-createDataFrameFromOptions "glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-createDataFrameFromOptions").

Some connection types do not require `format_options`. For example, in normal use, a JDBC
connection to a relational database retrieves data in a consistent, tabular data format. Therefore, reading from a
JDBC connection would not require `format_options`.

Some methods to read and write data in glue do not require `format_options`. For example, using
`GlueContext.create_dynamic_frame.from_catalog` with AWS Glue crawlers. Crawlers determine the shape of
your data. When using crawlers, a AWS Glue classifier will examine your data to make smart decisions about how to
represent your data format. It will then store a representation of your data in the AWS Glue Data Catalog, which can
be used within a AWS Glue ETL script to retrieve your data with the
`GlueContext.create_dynamic_frame.from_catalog` method. Crawlers remove the need to manually specify
information about your data format.

For jobs that access AWS Lake Formation governed tables, AWS Glue supports reading and
writing all formats supported by Lake Formation governed tables. For the current list of supported formats
for AWS Lake Formation governed tables, see [Notes and
Restrictions for Governed Tables](../../../lake-formation/latest/dg/governed-table-restrictions.md "../../../lake-formation/latest/dg/governed-table-restrictions.md") in the _AWS Lake Formation Developer Guide_.

###### Note

For writing Apache Parquet, AWS Glue ETL only supports writing to a governed table by specifying an option for a custom Parquet writer type optimized for Dynamic Frames. When writing to a governed table with the `parquet` format, you should add the key `useGlueParquetWriter` with a value of `true` in the table parameters.

###### Topics

- [Using the CSV format in AWS Glue](aws-glue-programming-etl-format-csv-home.md "aws-glue-programming-etl-format-csv-home.md")
- [Using the Parquet format in AWS Glue](aws-glue-programming-etl-format-parquet-home.md "aws-glue-programming-etl-format-parquet-home.md")
- [Using the XML format in AWS Glue](aws-glue-programming-etl-format-xml-home.md "aws-glue-programming-etl-format-xml-home.md")
- [Using the Avro format in AWS Glue](aws-glue-programming-etl-format-avro-home.md "aws-glue-programming-etl-format-avro-home.md")
- [Using the grokLog format in AWS Glue](aws-glue-programming-etl-format-grokLog-home.md "aws-glue-programming-etl-format-grokLog-home.md")
- [Using the Ion format in AWS Glue](aws-glue-programming-etl-format-ion-home.md "aws-glue-programming-etl-format-ion-home.md")
- [Using the JSON format in AWS Glue](aws-glue-programming-etl-format-json-home.md "aws-glue-programming-etl-format-json-home.md")
- [Using the ORC format in AWS Glue](aws-glue-programming-etl-format-orc-home.md "aws-glue-programming-etl-format-orc-home.md")
- [Using data lake
  frameworks with AWS Glue ETL jobs](aws-glue-programming-etl-datalake-native-frameworks.md "aws-glue-programming-etl-datalake-native-frameworks.md")
- [Shared configuration reference](#aws-glue-programming-etl-format-shared-reference "#aws-glue-programming-etl-format-shared-reference")

## Shared configuration reference

You can use the following `format_options` values with any format type.

- `attachFilename` — A string in the appropriate format to be used as a column name. If
  you provide this option, the name of the source file for the record will be appended to the record. The
  parameter value will be used as the column name.
- `attachTimestamp` — A string in the appropriate format to be used as a column name. If
  you provide this option, the modification time of the source file for the record will be appended to the
  record. The parameter value will be used as the column name.
