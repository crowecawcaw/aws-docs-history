# Visual job API

The Visual job API allows you to create data integration jobs by using the
AWS Glue API from a JSON object that represents a visual configuration
of a AWS Glue job.

A list of `CodeGenConfigurationNodes` are provided to a
create or update job API to register a DAG in AWS Glue Studio for the
created job and generate the associated code.

## Data types

- [CodeGenConfigurationNode structure](#aws-glue-api-visual-job-api-CodeGenConfigurationNode "#aws-glue-api-visual-job-api-CodeGenConfigurationNode")
- [JDBCConnectorOptions structure](#aws-glue-api-visual-job-api-JDBCConnectorOptions "#aws-glue-api-visual-job-api-JDBCConnectorOptions")
- [StreamingDataPreviewOptions structure](#aws-glue-api-visual-job-api-StreamingDataPreviewOptions "#aws-glue-api-visual-job-api-StreamingDataPreviewOptions")
- [AthenaConnectorSource structure](#aws-glue-api-visual-job-api-AthenaConnectorSource "#aws-glue-api-visual-job-api-AthenaConnectorSource")
- [JDBCConnectorSource structure](#aws-glue-api-visual-job-api-JDBCConnectorSource "#aws-glue-api-visual-job-api-JDBCConnectorSource")
- [SparkConnectorSource structure](#aws-glue-api-visual-job-api-SparkConnectorSource "#aws-glue-api-visual-job-api-SparkConnectorSource")
- [CatalogSource structure](#aws-glue-api-visual-job-api-CatalogSource "#aws-glue-api-visual-job-api-CatalogSource")
- [MySQLCatalogSource structure](#aws-glue-api-visual-job-api-MySQLCatalogSource "#aws-glue-api-visual-job-api-MySQLCatalogSource")
- [PostgreSQLCatalogSource structure](#aws-glue-api-visual-job-api-PostgreSQLCatalogSource "#aws-glue-api-visual-job-api-PostgreSQLCatalogSource")
- [OracleSQLCatalogSource structure](#aws-glue-api-visual-job-api-OracleSQLCatalogSource "#aws-glue-api-visual-job-api-OracleSQLCatalogSource")
- [MicrosoftSQLServerCatalogSource structure](#aws-glue-api-visual-job-api-MicrosoftSQLServerCatalogSource "#aws-glue-api-visual-job-api-MicrosoftSQLServerCatalogSource")
- [CatalogKinesisSource structure](#aws-glue-api-visual-job-api-CatalogKinesisSource "#aws-glue-api-visual-job-api-CatalogKinesisSource")
- [DirectKinesisSource structure](#aws-glue-api-visual-job-api-DirectKinesisSource "#aws-glue-api-visual-job-api-DirectKinesisSource")
- [KinesisStreamingSourceOptions structure](#aws-glue-api-visual-job-api-KinesisStreamingSourceOptions "#aws-glue-api-visual-job-api-KinesisStreamingSourceOptions")
- [CatalogKafkaSource structure](#aws-glue-api-visual-job-api-CatalogKafkaSource "#aws-glue-api-visual-job-api-CatalogKafkaSource")
- [DirectKafkaSource structure](#aws-glue-api-visual-job-api-DirectKafkaSource "#aws-glue-api-visual-job-api-DirectKafkaSource")
- [KafkaStreamingSourceOptions structure](#aws-glue-api-visual-job-api-KafkaStreamingSourceOptions "#aws-glue-api-visual-job-api-KafkaStreamingSourceOptions")
- [RedshiftSource structure](#aws-glue-api-visual-job-api-RedshiftSource "#aws-glue-api-visual-job-api-RedshiftSource")
- [AmazonRedshiftSource structure](#aws-glue-api-visual-job-api-AmazonRedshiftSource "#aws-glue-api-visual-job-api-AmazonRedshiftSource")
- [AmazonRedshiftNodeData structure](#aws-glue-api-visual-job-api-AmazonRedshiftNodeData "#aws-glue-api-visual-job-api-AmazonRedshiftNodeData")
- [AmazonRedshiftAdvancedOption structure](#aws-glue-api-visual-job-api-AmazonRedshiftAdvancedOption "#aws-glue-api-visual-job-api-AmazonRedshiftAdvancedOption")
- [Option structure](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option")
- [S3CatalogSource structure](#aws-glue-api-visual-job-api-S3CatalogSource "#aws-glue-api-visual-job-api-S3CatalogSource")
- [S3SourceAdditionalOptions structure](#aws-glue-api-visual-job-api-S3SourceAdditionalOptions "#aws-glue-api-visual-job-api-S3SourceAdditionalOptions")
- [S3CsvSource structure](#aws-glue-api-visual-job-api-S3CsvSource "#aws-glue-api-visual-job-api-S3CsvSource")
- [DirectJDBCSource structure](#aws-glue-api-visual-job-api-DirectJDBCSource "#aws-glue-api-visual-job-api-DirectJDBCSource")
- [S3DirectSourceAdditionalOptions structure](#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions "#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions")
- [S3JsonSource structure](#aws-glue-api-visual-job-api-S3JsonSource "#aws-glue-api-visual-job-api-S3JsonSource")
- [S3ParquetSource structure](#aws-glue-api-visual-job-api-S3ParquetSource "#aws-glue-api-visual-job-api-S3ParquetSource")
- [S3DeltaSource structure](#aws-glue-api-visual-job-api-S3DeltaSource "#aws-glue-api-visual-job-api-S3DeltaSource")
- [S3CatalogDeltaSource structure](#aws-glue-api-visual-job-api-S3CatalogDeltaSource "#aws-glue-api-visual-job-api-S3CatalogDeltaSource")
- [CatalogDeltaSource structure](#aws-glue-api-visual-job-api-CatalogDeltaSource "#aws-glue-api-visual-job-api-CatalogDeltaSource")
- [S3HudiSource structure](#aws-glue-api-visual-job-api-S3HudiSource "#aws-glue-api-visual-job-api-S3HudiSource")
- [S3CatalogHudiSource structure](#aws-glue-api-visual-job-api-S3CatalogHudiSource "#aws-glue-api-visual-job-api-S3CatalogHudiSource")
- [S3ExcelSource structure](#aws-glue-api-visual-job-api-S3ExcelSource "#aws-glue-api-visual-job-api-S3ExcelSource")
- [CatalogHudiSource structure](#aws-glue-api-visual-job-api-CatalogHudiSource "#aws-glue-api-visual-job-api-CatalogHudiSource")
- [DynamoDBCatalogSource structure](#aws-glue-api-visual-job-api-DynamoDBCatalogSource "#aws-glue-api-visual-job-api-DynamoDBCatalogSource")
- [RelationalCatalogSource structure](#aws-glue-api-visual-job-api-RelationalCatalogSource "#aws-glue-api-visual-job-api-RelationalCatalogSource")
- [JDBCConnectorTarget structure](#aws-glue-api-visual-job-api-JDBCConnectorTarget "#aws-glue-api-visual-job-api-JDBCConnectorTarget")
- [SparkConnectorTarget structure](#aws-glue-api-visual-job-api-SparkConnectorTarget "#aws-glue-api-visual-job-api-SparkConnectorTarget")
- [BasicCatalogTarget structure](#aws-glue-api-visual-job-api-BasicCatalogTarget "#aws-glue-api-visual-job-api-BasicCatalogTarget")
- [MySQLCatalogTarget structure](#aws-glue-api-visual-job-api-MySQLCatalogTarget "#aws-glue-api-visual-job-api-MySQLCatalogTarget")
- [PostgreSQLCatalogTarget structure](#aws-glue-api-visual-job-api-PostgreSQLCatalogTarget "#aws-glue-api-visual-job-api-PostgreSQLCatalogTarget")
- [OracleSQLCatalogTarget structure](#aws-glue-api-visual-job-api-OracleSQLCatalogTarget "#aws-glue-api-visual-job-api-OracleSQLCatalogTarget")
- [MicrosoftSQLServerCatalogTarget structure](#aws-glue-api-visual-job-api-MicrosoftSQLServerCatalogTarget "#aws-glue-api-visual-job-api-MicrosoftSQLServerCatalogTarget")
- [RedshiftTarget structure](#aws-glue-api-visual-job-api-RedshiftTarget "#aws-glue-api-visual-job-api-RedshiftTarget")
- [AmazonRedshiftTarget structure](#aws-glue-api-visual-job-api-AmazonRedshiftTarget "#aws-glue-api-visual-job-api-AmazonRedshiftTarget")
- [UpsertRedshiftTargetOptions structure](#aws-glue-api-visual-job-api-UpsertRedshiftTargetOptions "#aws-glue-api-visual-job-api-UpsertRedshiftTargetOptions")
- [S3CatalogTarget structure](#aws-glue-api-visual-job-api-S3CatalogTarget "#aws-glue-api-visual-job-api-S3CatalogTarget")
- [S3GlueParquetTarget structure](#aws-glue-api-visual-job-api-S3GlueParquetTarget "#aws-glue-api-visual-job-api-S3GlueParquetTarget")
- [CatalogSchemaChangePolicy structure](#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy "#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy")
- [S3DirectTarget structure](#aws-glue-api-visual-job-api-S3DirectTarget "#aws-glue-api-visual-job-api-S3DirectTarget")
- [S3HudiCatalogTarget structure](#aws-glue-api-visual-job-api-S3HudiCatalogTarget "#aws-glue-api-visual-job-api-S3HudiCatalogTarget")
- [S3HudiDirectTarget structure](#aws-glue-api-visual-job-api-S3HudiDirectTarget "#aws-glue-api-visual-job-api-S3HudiDirectTarget")
- [S3DeltaCatalogTarget structure](#aws-glue-api-visual-job-api-S3DeltaCatalogTarget "#aws-glue-api-visual-job-api-S3DeltaCatalogTarget")
- [S3DeltaDirectTarget structure](#aws-glue-api-visual-job-api-S3DeltaDirectTarget "#aws-glue-api-visual-job-api-S3DeltaDirectTarget")
- [S3HyperDirectTarget structure](#aws-glue-api-visual-job-api-S3HyperDirectTarget "#aws-glue-api-visual-job-api-S3HyperDirectTarget")
- [S3IcebergDirectTarget structure](#aws-glue-api-visual-job-api-S3IcebergDirectTarget "#aws-glue-api-visual-job-api-S3IcebergDirectTarget")
- [DirectSchemaChangePolicy structure](#aws-glue-api-visual-job-api-DirectSchemaChangePolicy "#aws-glue-api-visual-job-api-DirectSchemaChangePolicy")
- [ApplyMapping structure](#aws-glue-api-visual-job-api-ApplyMapping "#aws-glue-api-visual-job-api-ApplyMapping")
- [Mapping structure](#aws-glue-api-visual-job-api-Mapping "#aws-glue-api-visual-job-api-Mapping")
- [SelectFields structure](#aws-glue-api-visual-job-api-SelectFields "#aws-glue-api-visual-job-api-SelectFields")
- [DropFields structure](#aws-glue-api-visual-job-api-DropFields "#aws-glue-api-visual-job-api-DropFields")
- [RenameField structure](#aws-glue-api-visual-job-api-RenameField "#aws-glue-api-visual-job-api-RenameField")
- [Spigot structure](#aws-glue-api-visual-job-api-Spigot "#aws-glue-api-visual-job-api-Spigot")
- [Join structure](#aws-glue-api-visual-job-api-Join "#aws-glue-api-visual-job-api-Join")
- [JoinColumn structure](#aws-glue-api-visual-job-api-JoinColumn "#aws-glue-api-visual-job-api-JoinColumn")
- [SplitFields structure](#aws-glue-api-visual-job-api-SplitFields "#aws-glue-api-visual-job-api-SplitFields")
- [SelectFromCollection structure](#aws-glue-api-visual-job-api-SelectFromCollection "#aws-glue-api-visual-job-api-SelectFromCollection")
- [FillMissingValues structure](#aws-glue-api-visual-job-api-FillMissingValues "#aws-glue-api-visual-job-api-FillMissingValues")
- [Filter structure](#aws-glue-api-visual-job-api-Filter "#aws-glue-api-visual-job-api-Filter")
- [FilterExpression structure](#aws-glue-api-visual-job-api-FilterExpression "#aws-glue-api-visual-job-api-FilterExpression")
- [FilterValue structure](#aws-glue-api-visual-job-api-FilterValue "#aws-glue-api-visual-job-api-FilterValue")
- [CustomCode structure](#aws-glue-api-visual-job-api-CustomCode "#aws-glue-api-visual-job-api-CustomCode")
- [SparkSQL structure](#aws-glue-api-visual-job-api-SparkSQL "#aws-glue-api-visual-job-api-SparkSQL")
- [SqlAlias structure](#aws-glue-api-visual-job-api-SqlAlias "#aws-glue-api-visual-job-api-SqlAlias")
- [DropNullFields structure](#aws-glue-api-visual-job-api-DropNullFields "#aws-glue-api-visual-job-api-DropNullFields")
- [NullCheckBoxList structure](#aws-glue-api-visual-job-api-NullCheckBoxList "#aws-glue-api-visual-job-api-NullCheckBoxList")
- [NullValueField structure](#aws-glue-api-visual-job-api-NullValueField "#aws-glue-api-visual-job-api-NullValueField")
- [Datatype structure](#aws-glue-api-visual-job-api-Datatype "#aws-glue-api-visual-job-api-Datatype")
- [Merge structure](#aws-glue-api-visual-job-api-Merge "#aws-glue-api-visual-job-api-Merge")
- [Union structure](#aws-glue-api-visual-job-api-Union "#aws-glue-api-visual-job-api-Union")
- [PIIDetection structure](#aws-glue-api-visual-job-api-PIIDetection "#aws-glue-api-visual-job-api-PIIDetection")
- [Aggregate structure](#aws-glue-api-visual-job-api-Aggregate "#aws-glue-api-visual-job-api-Aggregate")
- [DropDuplicates structure](#aws-glue-api-visual-job-api-DropDuplicates "#aws-glue-api-visual-job-api-DropDuplicates")
- [GovernedCatalogTarget structure](#aws-glue-api-visual-job-api-GovernedCatalogTarget "#aws-glue-api-visual-job-api-GovernedCatalogTarget")
- [GovernedCatalogSource structure](#aws-glue-api-visual-job-api-GovernedCatalogSource "#aws-glue-api-visual-job-api-GovernedCatalogSource")
- [AggregateOperation structure](#aws-glue-api-visual-job-api-AggregateOperation "#aws-glue-api-visual-job-api-AggregateOperation")
- [GlueSchema structure](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema")
- [GlueStudioSchemaColumn structure](#aws-glue-api-visual-job-api-GlueStudioSchemaColumn "#aws-glue-api-visual-job-api-GlueStudioSchemaColumn")
- [GlueStudioColumn structure](#aws-glue-api-visual-job-api-GlueStudioColumn "#aws-glue-api-visual-job-api-GlueStudioColumn")
- [DynamicTransform structure](#aws-glue-api-visual-job-api-DynamicTransform "#aws-glue-api-visual-job-api-DynamicTransform")
- [TransformConfigParameter structure](#aws-glue-api-visual-job-api-TransformConfigParameter "#aws-glue-api-visual-job-api-TransformConfigParameter")
- [EvaluateDataQuality structure](#aws-glue-api-visual-job-api-EvaluateDataQuality "#aws-glue-api-visual-job-api-EvaluateDataQuality")
- [DQResultsPublishingOptions structure](#aws-glue-api-visual-job-api-DQResultsPublishingOptions "#aws-glue-api-visual-job-api-DQResultsPublishingOptions")
- [DQStopJobOnFailureOptions structure](#aws-glue-api-visual-job-api-DQStopJobOnFailureOptions "#aws-glue-api-visual-job-api-DQStopJobOnFailureOptions")
- [EvaluateDataQualityMultiFrame structure](#aws-glue-api-visual-job-api-EvaluateDataQualityMultiFrame "#aws-glue-api-visual-job-api-EvaluateDataQualityMultiFrame")
- [Recipe structure](#aws-glue-api-visual-job-api-Recipe "#aws-glue-api-visual-job-api-Recipe")
- [RecipeReference structure](#aws-glue-api-visual-job-api-RecipeReference "#aws-glue-api-visual-job-api-RecipeReference")
- [SnowflakeNodeData structure](#aws-glue-api-visual-job-api-SnowflakeNodeData "#aws-glue-api-visual-job-api-SnowflakeNodeData")
- [SnowflakeSource structure](#aws-glue-api-visual-job-api-SnowflakeSource "#aws-glue-api-visual-job-api-SnowflakeSource")
- [SnowflakeTarget structure](#aws-glue-api-visual-job-api-SnowflakeTarget "#aws-glue-api-visual-job-api-SnowflakeTarget")
- [ConnectorDataSource structure](#aws-glue-api-visual-job-api-ConnectorDataSource "#aws-glue-api-visual-job-api-ConnectorDataSource")
- [ConnectorDataTarget structure](#aws-glue-api-visual-job-api-ConnectorDataTarget "#aws-glue-api-visual-job-api-ConnectorDataTarget")
- [RecipeStep structure](#aws-glue-api-visual-job-api-RecipeStep "#aws-glue-api-visual-job-api-RecipeStep")
- [RecipeAction structure](#aws-glue-api-visual-job-api-RecipeAction "#aws-glue-api-visual-job-api-RecipeAction")
- [ConditionExpression structure](#aws-glue-api-visual-job-api-ConditionExpression "#aws-glue-api-visual-job-api-ConditionExpression")
- [S3CatalogIcebergSource structure](#aws-glue-api-visual-job-api-S3CatalogIcebergSource "#aws-glue-api-visual-job-api-S3CatalogIcebergSource")
- [CatalogIcebergSource structure](#aws-glue-api-visual-job-api-CatalogIcebergSource "#aws-glue-api-visual-job-api-CatalogIcebergSource")
- [S3IcebergCatalogTarget structure](#aws-glue-api-visual-job-api-S3IcebergCatalogTarget "#aws-glue-api-visual-job-api-S3IcebergCatalogTarget")
- [DynamoDBELTConnectorSource structure](#aws-glue-api-visual-job-api-DynamoDBELTConnectorSource "#aws-glue-api-visual-job-api-DynamoDBELTConnectorSource")
- [DDBELTConnectionOptions structure](#aws-glue-api-visual-job-api-DDBELTConnectionOptions "#aws-glue-api-visual-job-api-DDBELTConnectionOptions")
- [DDBELTCatalogAdditionalOptions structure](#aws-glue-api-visual-job-api-DDBELTCatalogAdditionalOptions "#aws-glue-api-visual-job-api-DDBELTCatalogAdditionalOptions")
- [Route structure](#aws-glue-api-visual-job-api-Route "#aws-glue-api-visual-job-api-Route")
- [GroupFilters structure](#aws-glue-api-visual-job-api-GroupFilters "#aws-glue-api-visual-job-api-GroupFilters")
- [AutoDataQuality structure](#aws-glue-api-visual-job-api-AutoDataQuality "#aws-glue-api-visual-job-api-AutoDataQuality")

## CodeGenConfigurationNode structure

`CodeGenConfigurationNode` enumerates all valid Node
types. One and only one of its member variables can be populated.

###### Fields

- `AthenaConnectorSource` – An [AthenaConnectorSource](#aws-glue-api-visual-job-api-AthenaConnectorSource "#aws-glue-api-visual-job-api-AthenaConnectorSource") object.

Specifies a connector to an Amazon Athena data source.

- `JDBCConnectorSource` – A [JDBCConnectorSource](#aws-glue-api-visual-job-api-JDBCConnectorSource "#aws-glue-api-visual-job-api-JDBCConnectorSource") object.

Specifies a connector to a JDBC data source.

- `SparkConnectorSource` – A [SparkConnectorSource](#aws-glue-api-visual-job-api-SparkConnectorSource "#aws-glue-api-visual-job-api-SparkConnectorSource") object.

Specifies a connector to an Apache Spark data source.

- `CatalogSource` – A [CatalogSource](#aws-glue-api-visual-job-api-CatalogSource "#aws-glue-api-visual-job-api-CatalogSource") object.

Specifies a data store in the AWS Glue Data Catalog.

- `RedshiftSource` – A [RedshiftSource](#aws-glue-api-visual-job-api-RedshiftSource "#aws-glue-api-visual-job-api-RedshiftSource") object.

Specifies an Amazon Redshift data store.

- `S3CatalogSource` – A [S3CatalogSource](#aws-glue-api-visual-job-api-S3CatalogSource "#aws-glue-api-visual-job-api-S3CatalogSource") object.

Specifies an Amazon S3 data store in the AWS Glue Data Catalog.

- `S3CsvSource` – A [S3CsvSource](#aws-glue-api-visual-job-api-S3CsvSource "#aws-glue-api-visual-job-api-S3CsvSource") object.

Specifies a command-separated value (CSV) data store stored in Amazon
S3.

- `S3JsonSource` – A [S3JsonSource](#aws-glue-api-visual-job-api-S3JsonSource "#aws-glue-api-visual-job-api-S3JsonSource") object.

Specifies a JSON data store stored in Amazon S3.

- `S3ParquetSource` – A [S3ParquetSource](#aws-glue-api-visual-job-api-S3ParquetSource "#aws-glue-api-visual-job-api-S3ParquetSource") object.

Specifies an Apache Parquet data store stored in Amazon S3.

- `RelationalCatalogSource` – A [RelationalCatalogSource](#aws-glue-api-visual-job-api-RelationalCatalogSource "#aws-glue-api-visual-job-api-RelationalCatalogSource") object.

Specifies a relational catalog data store in the AWS Glue Data
Catalog.

- `DynamoDBCatalogSource` – A [DynamoDBCatalogSource](#aws-glue-api-visual-job-api-DynamoDBCatalogSource "#aws-glue-api-visual-job-api-DynamoDBCatalogSource") object.

Specifies a DynamoDBC Catalog data store in the AWS Glue Data
Catalog.

- `JDBCConnectorTarget` – A [JDBCConnectorTarget](#aws-glue-api-visual-job-api-JDBCConnectorTarget "#aws-glue-api-visual-job-api-JDBCConnectorTarget") object.

Specifies a data target that writes to Amazon S3 in Apache Parquet columnar
storage.

- `SparkConnectorTarget` – A [SparkConnectorTarget](#aws-glue-api-visual-job-api-SparkConnectorTarget "#aws-glue-api-visual-job-api-SparkConnectorTarget") object.

Specifies a target that uses an Apache Spark connector.

- `CatalogTarget` – A [BasicCatalogTarget](#aws-glue-api-visual-job-api-BasicCatalogTarget "#aws-glue-api-visual-job-api-BasicCatalogTarget") object.

Specifies a target that uses a AWS Glue Data Catalog table.

- `RedshiftTarget` – A [RedshiftTarget](#aws-glue-api-visual-job-api-RedshiftTarget "#aws-glue-api-visual-job-api-RedshiftTarget") object.

Specifies a target that uses Amazon Redshift.

- `S3CatalogTarget` – A [S3CatalogTarget](#aws-glue-api-visual-job-api-S3CatalogTarget "#aws-glue-api-visual-job-api-S3CatalogTarget") object.

Specifies a data target that writes to Amazon S3 using the AWS Glue Data Catalog.

- `S3GlueParquetTarget` – A [S3GlueParquetTarget](#aws-glue-api-visual-job-api-S3GlueParquetTarget "#aws-glue-api-visual-job-api-S3GlueParquetTarget") object.

Specifies a data target that writes to Amazon S3 in Apache Parquet columnar
storage.

- `S3DirectTarget` – A [S3DirectTarget](#aws-glue-api-visual-job-api-S3DirectTarget "#aws-glue-api-visual-job-api-S3DirectTarget") object.

Specifies a data target that writes to Amazon S3.

- `ApplyMapping` – An [ApplyMapping](#aws-glue-api-visual-job-api-ApplyMapping "#aws-glue-api-visual-job-api-ApplyMapping") object.

Specifies a transform that maps data property keys in the data source to
data property keys in the data target. You can rename keys, modify the data types
for keys, and choose which keys to drop from the dataset.

- `SelectFields` – A [SelectFields](#aws-glue-api-visual-job-api-SelectFields "#aws-glue-api-visual-job-api-SelectFields") object.

Specifies a transform that chooses the data property keys that you want
to keep.

- `DropFields` – A [DropFields](#aws-glue-api-visual-job-api-DropFields "#aws-glue-api-visual-job-api-DropFields") object.

Specifies a transform that chooses the data property keys that you want
to drop.

- `RenameField` – A [RenameField](#aws-glue-api-visual-job-api-RenameField "#aws-glue-api-visual-job-api-RenameField") object.

Specifies a transform that renames a single data property key.

- `Spigot` – A [Spigot](#aws-glue-api-visual-job-api-Spigot "#aws-glue-api-visual-job-api-Spigot") object.

Specifies a transform that writes samples of the data to an Amazon S3 bucket.

- `Join` – A [Join](#aws-glue-api-visual-job-api-Join "#aws-glue-api-visual-job-api-Join") object.

Specifies a transform that joins two datasets into one dataset using a
comparison phrase on the specified data property keys. You can use inner, outer,
left, right, left semi, and left anti joins.

- `SplitFields` – A [SplitFields](#aws-glue-api-visual-job-api-SplitFields "#aws-glue-api-visual-job-api-SplitFields") object.

Specifies a transform that splits data property keys into two `DynamicFrames`.
The output is a collection of `DynamicFrames`: one with selected
data property keys, and one with the remaining data property keys.

- `SelectFromCollection` – A [SelectFromCollection](#aws-glue-api-visual-job-api-SelectFromCollection "#aws-glue-api-visual-job-api-SelectFromCollection") object.

Specifies a transform that chooses one `DynamicFrame` from
a collection of `DynamicFrames`. The output is the selected `DynamicFrame`

- `FillMissingValues` – A [FillMissingValues](#aws-glue-api-visual-job-api-FillMissingValues "#aws-glue-api-visual-job-api-FillMissingValues") object.

Specifies a transform that locates records in the dataset that have missing
values and adds a new field with a value determined by imputation. The input data
set is used to train the machine learning model that determines what the missing
value should be.

- `Filter` – A [Filter](#aws-glue-api-visual-job-api-Filter "#aws-glue-api-visual-job-api-Filter") object.

Specifies a transform that splits a dataset into two, based on a filter
condition.

- `CustomCode` – A [CustomCode](#aws-glue-api-visual-job-api-CustomCode "#aws-glue-api-visual-job-api-CustomCode") object.

Specifies a transform that uses custom code you provide to perform the
data transformation. The output is a collection of DynamicFrames.

- `SparkSQL` – A [SparkSQL](#aws-glue-api-visual-job-api-SparkSQL "#aws-glue-api-visual-job-api-SparkSQL") object.

Specifies a transform where you enter a SQL query using Spark SQL syntax
to transform the data. The output is a single `DynamicFrame`.

- `DirectKinesisSource` – A [DirectKinesisSource](#aws-glue-api-visual-job-api-DirectKinesisSource "#aws-glue-api-visual-job-api-DirectKinesisSource") object.

Specifies a direct Amazon Kinesis data source.

- `DirectKafkaSource` – A [DirectKafkaSource](#aws-glue-api-visual-job-api-DirectKafkaSource "#aws-glue-api-visual-job-api-DirectKafkaSource") object.

Specifies an Apache Kafka data store.

- `CatalogKinesisSource` – A [CatalogKinesisSource](#aws-glue-api-visual-job-api-CatalogKinesisSource "#aws-glue-api-visual-job-api-CatalogKinesisSource") object.

Specifies a Kinesis data source in the AWS Glue Data Catalog.

- `CatalogKafkaSource` – A [CatalogKafkaSource](#aws-glue-api-visual-job-api-CatalogKafkaSource "#aws-glue-api-visual-job-api-CatalogKafkaSource") object.

Specifies an Apache Kafka data store in the Data Catalog.

- `DropNullFields` – A [DropNullFields](#aws-glue-api-visual-job-api-DropNullFields "#aws-glue-api-visual-job-api-DropNullFields") object.

Specifies a transform that removes columns from the dataset if all values
in the column are 'null'. By default, AWS Glue Studio will recognize
null objects, but some values such as empty strings, strings that are "null",
-1 integers or other placeholders such as zeros, are not automatically recognized
as nulls.

- `Merge` – A [Merge](#aws-glue-api-visual-job-api-Merge "#aws-glue-api-visual-job-api-Merge") object.

Specifies a transform that merges a `DynamicFrame` with
a staging `DynamicFrame` based on the specified primary keys to
identify records. Duplicate records (records with the same primary keys) are
not de-duplicated.

- `Union` – An [Union](#aws-glue-api-visual-job-api-Union "#aws-glue-api-visual-job-api-Union") object.

Specifies a transform that combines the rows from two or more datasets
into a single result.

- `PIIDetection` – A [PIIDetection](#aws-glue-api-visual-job-api-PIIDetection "#aws-glue-api-visual-job-api-PIIDetection") object.

Specifies a transform that identifies, removes or masks PII data.

- `Aggregate` – An [Aggregate](#aws-glue-api-visual-job-api-Aggregate "#aws-glue-api-visual-job-api-Aggregate") object.

Specifies a transform that groups rows by chosen fields and computes the
aggregated value by specified function.

- `DropDuplicates` – A [DropDuplicates](#aws-glue-api-visual-job-api-DropDuplicates "#aws-glue-api-visual-job-api-DropDuplicates") object.

Specifies a transform that removes rows of repeating data from a data set.

- `GovernedCatalogTarget` – A [GovernedCatalogTarget](#aws-glue-api-visual-job-api-GovernedCatalogTarget "#aws-glue-api-visual-job-api-GovernedCatalogTarget") object.

Specifies a data target that writes to a goverened catalog.

- `GovernedCatalogSource` – A [GovernedCatalogSource](#aws-glue-api-visual-job-api-GovernedCatalogSource "#aws-glue-api-visual-job-api-GovernedCatalogSource") object.

Specifies a data source in a goverened Data Catalog.

- `MicrosoftSQLServerCatalogSource` – A [MicrosoftSQLServerCatalogSource](#aws-glue-api-visual-job-api-MicrosoftSQLServerCatalogSource "#aws-glue-api-visual-job-api-MicrosoftSQLServerCatalogSource") object.

Specifies a Microsoft SQL server data source in the AWS Glue
Data Catalog.

- `MySQLCatalogSource` – A [MySQLCatalogSource](#aws-glue-api-visual-job-api-MySQLCatalogSource "#aws-glue-api-visual-job-api-MySQLCatalogSource") object.

Specifies a MySQL data source in the AWS Glue Data Catalog.

- `OracleSQLCatalogSource` – An [OracleSQLCatalogSource](#aws-glue-api-visual-job-api-OracleSQLCatalogSource "#aws-glue-api-visual-job-api-OracleSQLCatalogSource") object.

Specifies an Oracle data source in the AWS Glue Data Catalog.

- `PostgreSQLCatalogSource` – A [PostgreSQLCatalogSource](#aws-glue-api-visual-job-api-PostgreSQLCatalogSource "#aws-glue-api-visual-job-api-PostgreSQLCatalogSource") object.

Specifies a PostgresSQL data source in the AWS Glue Data Catalog.

- `MicrosoftSQLServerCatalogTarget` – A [MicrosoftSQLServerCatalogTarget](#aws-glue-api-visual-job-api-MicrosoftSQLServerCatalogTarget "#aws-glue-api-visual-job-api-MicrosoftSQLServerCatalogTarget") object.

Specifies a target that uses Microsoft SQL.

- `MySQLCatalogTarget` – A [MySQLCatalogTarget](#aws-glue-api-visual-job-api-MySQLCatalogTarget "#aws-glue-api-visual-job-api-MySQLCatalogTarget") object.

Specifies a target that uses MySQL.

- `OracleSQLCatalogTarget` – An [OracleSQLCatalogTarget](#aws-glue-api-visual-job-api-OracleSQLCatalogTarget "#aws-glue-api-visual-job-api-OracleSQLCatalogTarget") object.

Specifies a target that uses Oracle SQL.

- `PostgreSQLCatalogTarget` – A [PostgreSQLCatalogTarget](#aws-glue-api-visual-job-api-PostgreSQLCatalogTarget "#aws-glue-api-visual-job-api-PostgreSQLCatalogTarget") object.

Specifies a target that uses Postgres SQL.

- `Route` – A [Route](#aws-glue-api-visual-job-api-Route "#aws-glue-api-visual-job-api-Route") object.

Specifies a route node that directs data to different output paths based
on defined filtering conditions.

- `DynamicTransform` – A [DynamicTransform](#aws-glue-api-visual-job-api-DynamicTransform "#aws-glue-api-visual-job-api-DynamicTransform") object.

Specifies a custom visual transform created by a user.

- `EvaluateDataQuality` – An [EvaluateDataQuality](#aws-glue-api-visual-job-api-EvaluateDataQuality "#aws-glue-api-visual-job-api-EvaluateDataQuality") object.

Specifies your data quality evaluation criteria.

- `S3CatalogHudiSource` – A [S3CatalogHudiSource](#aws-glue-api-visual-job-api-S3CatalogHudiSource "#aws-glue-api-visual-job-api-S3CatalogHudiSource") object.

Specifies a Hudi data source that is registered in the AWS Glue Data Catalog. The data source must be stored in Amazon S3.

- `CatalogHudiSource` – A [CatalogHudiSource](#aws-glue-api-visual-job-api-CatalogHudiSource "#aws-glue-api-visual-job-api-CatalogHudiSource") object.

Specifies a Hudi data source that is registered in the AWS Glue Data Catalog.

- `S3HudiSource` – A [S3HudiSource](#aws-glue-api-visual-job-api-S3HudiSource "#aws-glue-api-visual-job-api-S3HudiSource") object.

Specifies a Hudi data source stored in Amazon S3.

- `S3HudiCatalogTarget` – A [S3HudiCatalogTarget](#aws-glue-api-visual-job-api-S3HudiCatalogTarget "#aws-glue-api-visual-job-api-S3HudiCatalogTarget") object.

Specifies a target that writes to a Hudi data source in the AWS Glue Data Catalog.

- `S3HudiDirectTarget` – A [S3HudiDirectTarget](#aws-glue-api-visual-job-api-S3HudiDirectTarget "#aws-glue-api-visual-job-api-S3HudiDirectTarget") object.

Specifies a target that writes to a Hudi data source in Amazon S3.

- `S3CatalogDeltaSource` – A [S3CatalogDeltaSource](#aws-glue-api-visual-job-api-S3CatalogDeltaSource "#aws-glue-api-visual-job-api-S3CatalogDeltaSource") object.

Specifies a Delta Lake data source that is registered in the AWS Glue Data Catalog. The data source must be stored in Amazon S3.

- `CatalogDeltaSource` – A [CatalogDeltaSource](#aws-glue-api-visual-job-api-CatalogDeltaSource "#aws-glue-api-visual-job-api-CatalogDeltaSource") object.

Specifies a Delta Lake data source that is registered in the AWS Glue Data Catalog.

- `S3DeltaSource` – A [S3DeltaSource](#aws-glue-api-visual-job-api-S3DeltaSource "#aws-glue-api-visual-job-api-S3DeltaSource") object.

Specifies a Delta Lake data source stored in Amazon S3.

- `S3DeltaCatalogTarget` – A [S3DeltaCatalogTarget](#aws-glue-api-visual-job-api-S3DeltaCatalogTarget "#aws-glue-api-visual-job-api-S3DeltaCatalogTarget") object.

Specifies a target that writes to a Delta Lake data source in the AWS Glue Data Catalog.

- `S3DeltaDirectTarget` – A [S3DeltaDirectTarget](#aws-glue-api-visual-job-api-S3DeltaDirectTarget "#aws-glue-api-visual-job-api-S3DeltaDirectTarget") object.

Specifies a target that writes to a Delta Lake data source in Amazon S3.

- `AmazonRedshiftSource` – An [AmazonRedshiftSource](#aws-glue-api-visual-job-api-AmazonRedshiftSource "#aws-glue-api-visual-job-api-AmazonRedshiftSource") object.

Specifies a target that writes to a data source in Amazon Redshift.

- `AmazonRedshiftTarget` – An [AmazonRedshiftTarget](#aws-glue-api-visual-job-api-AmazonRedshiftTarget "#aws-glue-api-visual-job-api-AmazonRedshiftTarget") object.

Specifies a target that writes to a data target in Amazon Redshift.

- `EvaluateDataQualityMultiFrame` – An [EvaluateDataQualityMultiFrame](#aws-glue-api-visual-job-api-EvaluateDataQualityMultiFrame "#aws-glue-api-visual-job-api-EvaluateDataQualityMultiFrame") object.

Specifies your data quality evaluation criteria. Allows multiple input
data and returns a collection of Dynamic Frames.

- `Recipe` – A [Recipe](#aws-glue-api-visual-job-api-Recipe "#aws-glue-api-visual-job-api-Recipe") object.

Specifies a AWS Glue DataBrew recipe node.

- `SnowflakeSource` – A [SnowflakeSource](#aws-glue-api-visual-job-api-SnowflakeSource "#aws-glue-api-visual-job-api-SnowflakeSource") object.

Specifies a Snowflake data source.

- `SnowflakeTarget` – A [SnowflakeTarget](#aws-glue-api-visual-job-api-SnowflakeTarget "#aws-glue-api-visual-job-api-SnowflakeTarget") object.

Specifies a target that writes to a Snowflake data source.

- `ConnectorDataSource` – A [ConnectorDataSource](#aws-glue-api-visual-job-api-ConnectorDataSource "#aws-glue-api-visual-job-api-ConnectorDataSource") object.

Specifies a source generated with standard connection options.

- `ConnectorDataTarget` – A [ConnectorDataTarget](#aws-glue-api-visual-job-api-ConnectorDataTarget "#aws-glue-api-visual-job-api-ConnectorDataTarget") object.

Specifies a target generated with standard connection options.

- `S3CatalogIcebergSource` – A [S3CatalogIcebergSource](#aws-glue-api-visual-job-api-S3CatalogIcebergSource "#aws-glue-api-visual-job-api-S3CatalogIcebergSource") object.

Specifies an Apache Iceberg data source that is registered in the AWS Glue Data Catalog. The Iceberg data source must be stored in Amazon S3.

- `CatalogIcebergSource` – A [CatalogIcebergSource](#aws-glue-api-visual-job-api-CatalogIcebergSource "#aws-glue-api-visual-job-api-CatalogIcebergSource") object.

Specifies an Apache Iceberg data source that is registered in the AWS Glue Data Catalog.

- `S3IcebergCatalogTarget` – A [S3IcebergCatalogTarget](#aws-glue-api-visual-job-api-S3IcebergCatalogTarget "#aws-glue-api-visual-job-api-S3IcebergCatalogTarget") object.

Specifies an Apache Iceberg catalog target that writes data to Amazon S3 and registers the table in the AWS Glue Data Catalog.

- `S3IcebergDirectTarget` – A [S3IcebergDirectTarget](#aws-glue-api-visual-job-api-S3IcebergDirectTarget "#aws-glue-api-visual-job-api-S3IcebergDirectTarget") object.

Defines configuration parameters for writing data to Amazon S3 as an Apache
Iceberg table.

- `S3ExcelSource` – A [S3ExcelSource](#aws-glue-api-visual-job-api-S3ExcelSource "#aws-glue-api-visual-job-api-S3ExcelSource") object.

Defines configuration parameters for reading Excel files from Amazon
S3.

- `S3HyperDirectTarget` – A [S3HyperDirectTarget](#aws-glue-api-visual-job-api-S3HyperDirectTarget "#aws-glue-api-visual-job-api-S3HyperDirectTarget") object.

Defines configuration parameters for writing data to Amazon S3 using
HyperDirect optimization.

- `DynamoDBELTConnectorSource` – A [DynamoDBELTConnectorSource](#aws-glue-api-visual-job-api-DynamoDBELTConnectorSource "#aws-glue-api-visual-job-api-DynamoDBELTConnectorSource") object.

Specifies a DynamoDB ELT connector source for extracting data from DynamoDB
tables.

## JDBCConnectorOptions structure

Additional connection options for the connector.

###### Fields

- `FilterPredicate` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Extra condition clause to filter data from source. For example:

`BillingCity='Mountain View'`

When using a query instead of a table name, you should validate that the
query works with the specified `filterPredicate`.

- `PartitionColumn` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of an integer column that is used for partitioning. This option
works only when it's included with `lowerBound`, `upperBound`,
and `numPartitions`. This option works the same way as in the Spark
SQL JDBC reader.

- `LowerBound` – Number (long), not more than None.

The minimum value of `partitionColumn` that is used to decide
partition stride.

- `UpperBound` – Number (long), not more than None.

The maximum value of `partitionColumn` that is used to decide
partition stride.

- `NumPartitions` – Number (long), not more than None.

The number of partitions. This value, along with `lowerBound`
(inclusive) and `upperBound` (exclusive), form partition strides
for generated `WHERE` clause expressions that are used to split
the `partitionColumn`.

- `JobBookmarkKeys` – An array of UTF-8 strings.

The name of the job bookmark keys on which to sort.

- `JobBookmarkKeysSortOrder` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies an ascending or descending sort order.

- `DataTypeMapping` – A map array of key-value pairs.

Each key is a UTF-8 string (valid values: `ARRAY` | `BIGINT` | `BINARY` | `BIT` | `BLOB` | `BOOLEAN` | `CHAR` | `CLOB` | `DATALINK` | `DATE` | `DECIMAL` | `DISTINCT` | `DOUBLE` | `FLOAT` | `INTEGER` | `JAVA_OBJECT` | `LONGNVARCHAR` | `LONGVARBINARY` | `LONGVARCHAR` | `NCHAR` | `NCLOB` | `NULL` | `NUMERIC` | `NVARCHAR` | `OTHER` | `REAL` | `REF` | `REF_CURSOR` | `ROWID` | `SMALLINT` | `SQLXML` | `STRUCT` | `TIME` | `TIME_WITH_TIMEZONE` | `TIMESTAMP` | `TIMESTAMP_WITH_TIMEZONE` | `TINYINT` | `VARBINARY` | `VARCHAR`).

Each value is a UTF-8 string (valid values: `DATE` | `STRING` | `TIMESTAMP` | `INT` | `FLOAT` | `LONG` | `BIGDECIMAL` | `BYTE` | `SHORT` | `DOUBLE`).

Custom data type mapping that builds a mapping from a JDBC data type to an
AWS Glue data type. For example, the option `"dataTypeMapping":{"FLOAT":"STRING"}`
maps data fields of JDBC type `FLOAT` into the Java `String`
type by calling the `ResultSet.getString()` method of the driver,
and uses it to build the AWS Glue record. The `ResultSet`
object is implemented by each driver, so the behavior is specific to the driver
you use. Refer to the documentation for your JDBC driver to understand how the
driver performs the conversions.

## StreamingDataPreviewOptions structure

Specifies options related to data preview for viewing a sample of your
data.

###### Fields

- `PollingTime` – Number (long), at least 10.

The polling time in milliseconds.

- `RecordPollingLimit` – Number (long), at least 1.

The limit to the number of records polled.

## AthenaConnectorSource structure

Specifies a connector to an Amazon Athena data source.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data source.

- `ConnectionName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the connection that is associated with the connector.

- `ConnectorName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of a connector that assists with accessing the data store in AWS Glue Studio.

- `ConnectionType` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The type of connection, such as marketplace.athena or custom.athena,
designating a connection to an Amazon Athena data store.

- `ConnectionTable` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the data source.

- `SchemaName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the Cloudwatch log group to read from. For example, `/aws-glue/jobs/output`.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the custom Athena source.

## JDBCConnectorSource structure

Specifies a connector to a JDBC data source.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data source.

- `ConnectionName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the connection that is associated with the connector.

- `ConnectorName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of a connector that assists with accessing the data store in AWS Glue Studio.

- `ConnectionType` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The type of connection, such as marketplace.jdbc or custom.jdbc, designating
a connection to a JDBC data store.

- `AdditionalOptions` – A [JDBCConnectorOptions](#aws-glue-api-visual-job-api-JDBCConnectorOptions "#aws-glue-api-visual-job-api-JDBCConnectorOptions") object.

Additional connection options for the connector.

- `ConnectionTable` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the data source.

- `Query` – UTF-8 string, matching the [Custom string pattern #62](aws-glue-api-common.md#regex_62 "aws-glue-api-common.md#regex_62").

The table or SQL query to get the data from. You can specify either `ConnectionTable`
or `query`, but not both.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the custom JDBC source.

## SparkConnectorSource structure

Specifies a connector to an Apache Spark data source.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data source.

- `ConnectionName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the connection that is associated with the connector.

- `ConnectorName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of a connector that assists with accessing the data store in AWS Glue Studio.

- `ConnectionType` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The type of connection, such as marketplace.spark or custom.spark, designating
a connection to an Apache Spark data store.

- `AdditionalOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Additional connection options for the connector.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies data schema for the custom spark source.

## CatalogSource structure

Specifies a data store in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data store.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

- `PartitionPredicate` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Partitions satisfying this predicate are deleted. Files within the retention
period in these partitions are not deleted.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the catalog source.

## MySQLCatalogSource structure

Specifies a MySQL data source in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data source.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

## PostgreSQLCatalogSource structure

Specifies a PostgresSQL data source in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data source.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

## OracleSQLCatalogSource structure

Specifies an Oracle data source in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data source.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

## MicrosoftSQLServerCatalogSource structure

Specifies a Microsoft SQL server data source in the AWS Glue
Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data source.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

## CatalogKinesisSource structure

Specifies a Kinesis data source in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data source.

- `WindowSize` – Number (integer), not more than None.

The amount of time to spend processing each micro batch.

- `DetectSchema` – Boolean.

Whether to automatically determine the schema from the incoming data.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `StreamingOptions` – A [KinesisStreamingSourceOptions](#aws-glue-api-visual-job-api-KinesisStreamingSourceOptions "#aws-glue-api-visual-job-api-KinesisStreamingSourceOptions") object.

Additional options for the Kinesis streaming data source.

- `DataPreviewOptions` – A [StreamingDataPreviewOptions](#aws-glue-api-visual-job-api-StreamingDataPreviewOptions "#aws-glue-api-visual-job-api-StreamingDataPreviewOptions") object.

Additional options for data preview.

## DirectKinesisSource structure

Specifies a direct Amazon Kinesis data source.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data source.

- `WindowSize` – Number (integer), not more than None.

The amount of time to spend processing each micro batch.

- `DetectSchema` – Boolean.

Whether to automatically determine the schema from the incoming data.

- `StreamingOptions` – A [KinesisStreamingSourceOptions](#aws-glue-api-visual-job-api-KinesisStreamingSourceOptions "#aws-glue-api-visual-job-api-KinesisStreamingSourceOptions") object.

Additional options for the Kinesis streaming data source.

- `DataPreviewOptions` – A [StreamingDataPreviewOptions](#aws-glue-api-visual-job-api-StreamingDataPreviewOptions "#aws-glue-api-visual-job-api-StreamingDataPreviewOptions") object.

Additional options for data preview.

## KinesisStreamingSourceOptions structure

Additional options for the Amazon Kinesis streaming data source.

###### Fields

- `EndpointUrl` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The URL of the Kinesis endpoint.

- `StreamName` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the Kinesis data stream.

- `Classification` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

An optional classification.

- `Delimiter` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the delimiter character.

- `StartingPosition` – UTF-8 string (valid values: `latest="LATEST"` | `trim_horizon="TRIM_HORIZON"` | `earliest="EARLIEST"` | `timestamp="TIMESTAMP"`).

The starting position in the Kinesis data stream to read data from. The
possible values are `"latest"`, `"trim_horizon"`,
`"earliest"`, or a timestamp string in UTC format in the pattern
`yyyy-mm-ddTHH:MM:SSZ` (where `Z` represents a UTC
timezone offset with a +/-. For example: "2023-04-04T08:00:00-04:00"). The
default value is `"latest"`.

Note: Using a value that is a timestamp string in UTC format for "startingPosition"
is supported only for AWS Glue version 4.0 or later.

- `MaxFetchTimeInMs` – Number (long), not more than None.

The maximum time spent for the job executor to read records for the current
batch from the Kinesis data stream, specified in milliseconds (ms). Multiple
`GetRecords` API calls may be made within this time. The default
value is `1000`.

- `MaxFetchRecordsPerShard` – Number (long), not more than None.

The maximum number of records to fetch per shard in the Kinesis data stream
per microbatch. Note: The client can exceed this limit if the streaming job has
already read extra records from Kinesis (in the same get-records call). If `MaxFetchRecordsPerShard`
needs to be strict then it needs to be a multiple of `MaxRecordPerRead`.
The default value is `100000`.

- `MaxRecordPerRead` – Number (long), not more than None.

The maximum number of records to fetch from the Kinesis data stream in each
getRecords operation. The default value is `10000`.

- `AddIdleTimeBetweenReads` – Boolean.

Adds a time delay between two consecutive getRecords operations. The
default value is `"False"`. This option is only configurable for
AWS Glue version 2.0 and above.

- `IdleTimeBetweenReadsInMs` – Number (long), not more than None.

The minimum time delay between two consecutive getRecords operations,
specified in ms. The default value is `1000`. This option is only
configurable for AWS Glue version 2.0 and above.

- `DescribeShardInterval` – Number (long), not more than None.

The minimum time interval between two ListShards API calls for your script
to consider resharding. The default value is `1s`.

- `NumRetries` – Number (integer), not more than None.

The maximum number of retries for Kinesis Data Streams API requests. The
default value is `3`.

- `RetryIntervalMs` – Number (long), not more than None.

The cool-off time period (specified in ms) before retrying the Kinesis
Data Streams API call. The default value is `1000`.

- `MaxRetryIntervalMs` – Number (long), not more than None.

The maximum cool-off time period (specified in ms) between two retries
of a Kinesis Data Streams API call. The default value is `10000`.

- `AvoidEmptyBatches` – Boolean.

Avoids creating an empty microbatch job by checking for unread data in
the Kinesis data stream before the batch is started. The default value is `"False"`.

- `StreamArn` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The Amazon Resource Name (ARN) of the Kinesis data stream.

- `RoleArn` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The Amazon Resource Name (ARN) of the role to assume using AWS Security
Token Service (AWS STS). This role must have permissions for describe or read
record operations for the Kinesis data stream. You must use this parameter when
accessing a data stream in a different account. Used in conjunction with `"awsSTSSessionName"`.

- `RoleSessionName` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

An identifier for the session assuming the role using AWS STS. You must
use this parameter when accessing a data stream in a different account. Used in
conjunction with `"awsSTSRoleARN"`.

- `AddRecordTimestamp` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

When this option is set to 'true', the data output will contain an additional
column named "\_\_src_timestamp" that indicates the time when the corresponding
record received by the stream. The default value is 'false'. This option is supported
in AWS Glue version 4.0 or later.

- `EmitConsumerLagMetrics` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

When this option is set to 'true', for each batch, it will emit the metrics
for the duration between the oldest record received by the stream and the time
it arrives in AWS Glue to CloudWatch. The metric's name is "glue.driver.streaming.maxConsumerLagInMs".
The default value is 'false'. This option is supported in AWS Glue
version 4.0 or later.

- `StartingTimestamp` – UTF-8 string.

The timestamp of the record in the Kinesis data stream to start reading
data from. The possible values are a timestamp string in UTC format of the pattern
`yyyy-mm-ddTHH:MM:SSZ` (where Z represents a UTC timezone offset
with a +/-. For example: "2023-04-04T08:00:00+08:00").

- `FanoutConsumerARN` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The Amazon Resource Name (ARN) of the Kinesis Data Streams enhanced fan-out
consumer. When specified, enables enhanced fan-out for dedicated throughput
and lower latency data consumption.

## CatalogKafkaSource structure

Specifies an Apache Kafka data store in the Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data store.

- `WindowSize` – Number (integer), not more than None.

The amount of time to spend processing each micro batch.

- `DetectSchema` – Boolean.

Whether to automatically determine the schema from the incoming data.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `StreamingOptions` – A [KafkaStreamingSourceOptions](#aws-glue-api-visual-job-api-KafkaStreamingSourceOptions "#aws-glue-api-visual-job-api-KafkaStreamingSourceOptions") object.

Specifies the streaming options.

- `DataPreviewOptions` – A [StreamingDataPreviewOptions](#aws-glue-api-visual-job-api-StreamingDataPreviewOptions "#aws-glue-api-visual-job-api-StreamingDataPreviewOptions") object.

Specifies options related to data preview for viewing a sample of your
data.

## DirectKafkaSource structure

Specifies an Apache Kafka data store.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data store.

- `StreamingOptions` – A [KafkaStreamingSourceOptions](#aws-glue-api-visual-job-api-KafkaStreamingSourceOptions "#aws-glue-api-visual-job-api-KafkaStreamingSourceOptions") object.

Specifies the streaming options.

- `WindowSize` – Number (integer), not more than None.

The amount of time to spend processing each micro batch.

- `DetectSchema` – Boolean.

Whether to automatically determine the schema from the incoming data.

- `DataPreviewOptions` – A [StreamingDataPreviewOptions](#aws-glue-api-visual-job-api-StreamingDataPreviewOptions "#aws-glue-api-visual-job-api-StreamingDataPreviewOptions") object.

Specifies options related to data preview for viewing a sample of your
data.

## KafkaStreamingSourceOptions structure

Additional options for streaming.

###### Fields

- `BootstrapServers` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

A list of bootstrap server URLs, for example, as `b-1.vpc-test-2.o4q88o.c6.kafka.us-east-1.amazonaws.com:9094`.
This option must be specified in the API call or defined in the table metadata in
the Data Catalog.

- `SecurityProtocol` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The protocol used to communicate with brokers. The possible values are
`"SSL"` or `"PLAINTEXT"`.

- `ConnectionName` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the connection.

- `TopicName` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The topic name as specified in Apache Kafka. You must specify at least one
of `"topicName"`, `"assign"` or `"subscribePattern"`.

- `Assign` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The specific `TopicPartitions` to consume. You must specify
at least one of `"topicName"`, `"assign"` or `"subscribePattern"`.

- `SubscribePattern` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

A Java regex string that identifies the topic list to subscribe to. You
must specify at least one of `"topicName"`, `"assign"`
or `"subscribePattern"`.

- `Classification` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

An optional classification.

- `Delimiter` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the delimiter character.

- `StartingOffsets` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The starting position in the Kafka topic to read data from. The possible
values are `"earliest"` or `"latest"`. The default
value is `"latest"`.

- `EndingOffsets` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The end point when a batch query is ended. Possible values are either `"latest"`
or a JSON string that specifies an ending offset for each `TopicPartition`.

- `PollTimeoutMs` – Number (long), not more than None.

The timeout in milliseconds to poll data from Kafka in Spark job executors.
The default value is `512`.

- `NumRetries` – Number (integer), not more than None.

The number of times to retry before failing to fetch Kafka offsets. The
default value is `3`.

- `RetryIntervalMs` – Number (long), not more than None.

The time in milliseconds to wait before retrying to fetch Kafka offsets.
The default value is `10`.

- `MaxOffsetsPerTrigger` – Number (long), not more than None.

The rate limit on the maximum number of offsets that are processed per trigger
interval. The specified total number of offsets is proportionally split across
`topicPartitions` of different volumes. The default value is null,
which means that the consumer reads all offsets until the known latest offset.

- `MinPartitions` – Number (integer), not more than None.

The desired minimum number of partitions to read from Kafka. The default
value is null, which means that the number of spark partitions is equal to the number
of Kafka partitions.

- `IncludeHeaders` – Boolean.

Whether to include the Kafka headers. When the option is set to "true",
the data output will contain an additional column named "glue_streaming_kafka_headers"
with type `Array[Struct(key: String, value: String)]`. The default
value is "false". This option is available in AWS Glue version 3.0
or later only.

- `AddRecordTimestamp` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

When this option is set to 'true', the data output will contain an additional
column named "\_\_src_timestamp" that indicates the time when the corresponding
record received by the topic. The default value is 'false'. This option is supported
in AWS Glue version 4.0 or later.

- `EmitConsumerLagMetrics` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

When this option is set to 'true', for each batch, it will emit the metrics
for the duration between the oldest record received by the topic and the time it
arrives in AWS Glue to CloudWatch. The metric's name is "glue.driver.streaming.maxConsumerLagInMs".
The default value is 'false'. This option is supported in AWS Glue
version 4.0 or later.

- `StartingTimestamp` – UTF-8 string.

The timestamp of the record in the Kafka topic to start reading data from.
The possible values are a timestamp string in UTC format of the pattern `yyyy-mm-ddTHH:MM:SSZ`
(where Z represents a UTC timezone offset with a +/-. For example: "2023-04-04T08:00:00+08:00").

Only one of `StartingTimestamp` or `StartingOffsets`
must be set.

## RedshiftSource structure

Specifies an Amazon Redshift data store.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Amazon Redshift data store.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The database table to read from.

- `RedshiftTmpDir` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The Amazon S3 path where temporary data can be staged when copying out of
the database.

- `TmpDirIAMRole` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The IAM role with permissions.

## AmazonRedshiftSource structure

Specifies an Amazon Redshift source.

###### Fields

- `Name` – UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Amazon Redshift source.

- `Data` – An [AmazonRedshiftNodeData](#aws-glue-api-visual-job-api-AmazonRedshiftNodeData "#aws-glue-api-visual-job-api-AmazonRedshiftNodeData") object.

Specifies the data of the Amazon Reshift source node.

## AmazonRedshiftNodeData structure

Specifies an Amazon Redshift node.

###### Fields

- `AccessType` – UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

The access type for the Redshift connection. Can be a direct connection
or catalog connections.

- `SourceType` – UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

The source type to specify whether a specific table is the source or a custom
query.

- `Connection` – An [Option](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option") object.

The AWS Glue connection to the Redshift cluster.

- `Schema` – An [Option](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option") object.

The Redshift schema name when working with a direct connection.

- `Table` – An [Option](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option") object.

The Redshift table name when working with a direct connection.

- `CatalogDatabase` – An [Option](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option") object.

The name of the AWS Glue Data Catalog database when working
with a data catalog.

- `CatalogTable` – An [Option](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option") object.

The AWS Glue Data Catalog table name when working with a data
catalog.

- `CatalogRedshiftSchema` – UTF-8 string.

The Redshift schema name when working with a data catalog.

- `CatalogRedshiftTable` – UTF-8 string.

The database table to read from.

- `TempDir` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The Amazon S3 path where temporary data can be staged when copying out of
the database.

- `IamRole` – An [Option](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option") object.

Optional. The role name use when connection to S3. The IAM role ill default
to the role on the job when left blank.

- `AdvancedOptions` – An array of [AmazonRedshiftAdvancedOption](#aws-glue-api-visual-job-api-AmazonRedshiftAdvancedOption "#aws-glue-api-visual-job-api-AmazonRedshiftAdvancedOption") objects.

Optional values when connecting to the Redshift cluster.

- `SampleQuery` – UTF-8 string.

The SQL used to fetch the data from a Redshift sources when the SourceType
is 'query'.

- `PreAction` – UTF-8 string.

The SQL used before a MERGE or APPEND with upsert is run.

- `PostAction` – UTF-8 string.

The SQL used before a MERGE or APPEND with upsert is run.

- `Action` – UTF-8 string.

Specifies how writing to a Redshift cluser will occur.

- `TablePrefix` – UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

Specifies the prefix to a table.

- `Upsert` – Boolean.

The action used on Redshift sinks when doing an APPEND.

- `MergeAction` – UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

The action used when to detemine how a MERGE in a Redshift sink will be handled.

- `MergeWhenMatched` – UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

The action used when to detemine how a MERGE in a Redshift sink will be handled
when an existing record matches a new record.

- `MergeWhenNotMatched` – UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

The action used when to detemine how a MERGE in a Redshift sink will be handled
when an existing record doesn't match a new record.

- `MergeClause` – UTF-8 string.

The SQL used in a custom merge to deal with matching records.

- `CrawlerConnection` – UTF-8 string.

Specifies the name of the connection that is associated with the catalog
table used.

- `TableSchema` – An array of [Option](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option") objects.

The array of schema output for a given node.

- `StagingTable` – UTF-8 string.

The name of the temporary staging table that is used when doing a MERGE or
APPEND with upsert.

- `SelectedColumns` – An array of [Option](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option") objects.

The list of column names used to determine a matching record when doing
a MERGE or APPEND with upsert.

## AmazonRedshiftAdvancedOption structure

Specifies an optional value when connecting to the Redshift cluster.

###### Fields

- `Key` – UTF-8 string.

The key for the additional connection option.

- `Value` – UTF-8 string.

The value for the additional connection option.

## Option structure

Specifies an option value.

###### Fields

- `Value` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the value of the option.

- `Label` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the label of the option.

- `Description` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the description of the option.

## S3CatalogSource structure

Specifies an Amazon S3 data store in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data store.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The database table to read from.

- `PartitionPredicate` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Partitions satisfying this predicate are deleted. Files within the retention
period in these partitions are not deleted. Set to `""` –
empty by default.

- `AdditionalOptions` – A [S3SourceAdditionalOptions](#aws-glue-api-visual-job-api-S3SourceAdditionalOptions "#aws-glue-api-visual-job-api-S3SourceAdditionalOptions") object.

Specifies additional connection options.

## S3SourceAdditionalOptions structure

Specifies additional connection options for the Amazon S3 data store.

###### Fields

- `BoundedSize` – Number (long).

Sets the upper limit for the target size of the dataset in bytes that will
be processed.

- `BoundedFiles` – Number (long).

Sets the upper limit for the target number of files that will be processed.

## S3CsvSource structure

Specifies a command-separated value (CSV) data store stored in Amazon
S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data store.

- `Paths` – _Required:_ An array of UTF-8 strings.

A list of the Amazon S3 paths to read from.

- `CompressionType` – UTF-8 string (valid values: `gzip="GZIP"` | `bzip2="BZIP2"`).

Specifies how the data is compressed. This is generally not necessary
if the data has a standard file extension. Possible values are `"gzip"`
and `"bzip"`).

- `Exclusions` – An array of UTF-8 strings.

A string containing a JSON list of Unix-style glob patterns to exclude.
For example, "[\"\*\*.pdf\"]" excludes all PDF files.

- `GroupSize` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The target group size in bytes. The default is computed based on the input
data size and the size of your cluster. When there are fewer than 50,000 input files,
`"groupFiles"` must be set to `"inPartition"` for
this to take effect.

- `GroupFiles` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Grouping files is turned on by default when the input contains more than
50,000 files. To turn on grouping with fewer than 50,000 files, set this parameter
to "inPartition". To disable grouping when there are more than 50,000 files,
set this parameter to `"none"`.

- `Recurse` – Boolean.

If set to true, recursively reads files in all subdirectories under the
specified paths.

- `MaxBand` – Number (integer), not more than None.

This option controls the duration in milliseconds after which the s3 listing
is likely to be consistent. Files with modification timestamps falling within
the last maxBand milliseconds are tracked specially when using JobBookmarks
to account for Amazon S3 eventual consistency. Most users don't need to set this
option. The default is 900000 milliseconds, or 15 minutes.

- `MaxFilesInBand` – Number (integer), not more than None.

This option specifies the maximum number of files to save from the last
maxBand seconds. If this number is exceeded, extra files are skipped and only
processed in the next job run.

- `AdditionalOptions` – A [S3DirectSourceAdditionalOptions](#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions "#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions") object.

Specifies additional connection options.

- `Separator` – _Required:_ UTF-8 string (valid values: `comma="COMMA"` | `ctrla="CTRLA"` | `pipe="PIPE"` | `semicolon="SEMICOLON"` | `tab="TAB"`).

Specifies the delimiter character. The default is a comma: ",", but any
other character can be specified.

- `Escaper` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies a character to use for escaping. This option is used only when
reading CSV files. The default value is `none`. If enabled, the character
which immediately follows is used as-is, except for a small set of well-known
escapes (`\n`, `\r`, `\t`, and `\0`).

- `QuoteChar` – _Required:_ UTF-8 string (valid values: `quote="QUOTE"` | `quillemet="QUILLEMET"` | `single_quote="SINGLE_QUOTE"` | `disabled="DISABLED"`).

Specifies the character to use for quoting. The default is a double quote:
`'"'`. Set this to `-1` to turn off quoting entirely.

- `Multiline` – Boolean.

A Boolean value that specifies whether a single record can span multiple
lines. This can occur when a field contains a quoted new-line character. You must
set this option to True if any record spans multiple lines. The default value is
`False`, which allows for more aggressive file-splitting during
parsing.

- `WithHeader` – Boolean.

A Boolean value that specifies whether to treat the first line as a header.
The default value is `False`.

- `WriteHeader` – Boolean.

A Boolean value that specifies whether to write the header to output. The
default value is `True`.

- `SkipFirst` – Boolean.

A Boolean value that specifies whether to skip the first data line. The
default value is `False`.

- `OptimizePerformance` – Boolean.

A Boolean value that specifies whether to use the advanced SIMD CSV reader
along with Apache Arrow based columnar memory formats. Only available in AWS Glue version 3.0.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the S3 CSV source.

## DirectJDBCSource structure

Specifies the direct JDBC source connection.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the JDBC source connection.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The database of the JDBC source connection.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The table of the JDBC source connection.

- `ConnectionName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The connection name of the JDBC source.

- `ConnectionType` – _Required:_ UTF-8 string (valid values: `sqlserver` | `mysql` | `oracle` | `postgresql` | `redshift`).

The connection type of the JDBC source.

- `RedshiftTmpDir` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The temp directory of the JDBC Redshift source.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the direct JDBC source.

## S3DirectSourceAdditionalOptions structure

Specifies additional connection options for the Amazon S3 data store.

###### Fields

- `BoundedSize` – Number (long).

Sets the upper limit for the target size of the dataset in bytes that will
be processed.

- `BoundedFiles` – Number (long).

Sets the upper limit for the target number of files that will be processed.

- `EnableSamplePath` – Boolean.

Sets option to enable a sample path.

- `SamplePath` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

If enabled, specifies the sample path.

## S3JsonSource structure

Specifies a JSON data store stored in Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data store.

- `Paths` – _Required:_ An array of UTF-8 strings.

A list of the Amazon S3 paths to read from.

- `CompressionType` – UTF-8 string (valid values: `gzip="GZIP"` | `bzip2="BZIP2"`).

Specifies how the data is compressed. This is generally not necessary
if the data has a standard file extension. Possible values are `"gzip"`
and `"bzip"`).

- `Exclusions` – An array of UTF-8 strings.

A string containing a JSON list of Unix-style glob patterns to exclude.
For example, "[\"\*\*.pdf\"]" excludes all PDF files.

- `GroupSize` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The target group size in bytes. The default is computed based on the input
data size and the size of your cluster. When there are fewer than 50,000 input files,
`"groupFiles"` must be set to `"inPartition"` for
this to take effect.

- `GroupFiles` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Grouping files is turned on by default when the input contains more than
50,000 files. To turn on grouping with fewer than 50,000 files, set this parameter
to "inPartition". To disable grouping when there are more than 50,000 files,
set this parameter to `"none"`.

- `Recurse` – Boolean.

If set to true, recursively reads files in all subdirectories under the
specified paths.

- `MaxBand` – Number (integer), not more than None.

This option controls the duration in milliseconds after which the s3 listing
is likely to be consistent. Files with modification timestamps falling within
the last maxBand milliseconds are tracked specially when using JobBookmarks
to account for Amazon S3 eventual consistency. Most users don't need to set this
option. The default is 900000 milliseconds, or 15 minutes.

- `MaxFilesInBand` – Number (integer), not more than None.

This option specifies the maximum number of files to save from the last
maxBand seconds. If this number is exceeded, extra files are skipped and only
processed in the next job run.

- `AdditionalOptions` – A [S3DirectSourceAdditionalOptions](#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions "#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions") object.

Specifies additional connection options.

- `JsonPath` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

A JsonPath string defining the JSON data.

- `Multiline` – Boolean.

A Boolean value that specifies whether a single record can span multiple
lines. This can occur when a field contains a quoted new-line character. You must
set this option to True if any record spans multiple lines. The default value is
`False`, which allows for more aggressive file-splitting during
parsing.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the S3 JSON source.

## S3ParquetSource structure

Specifies an Apache Parquet data store stored in Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data store.

- `Paths` – _Required:_ An array of UTF-8 strings.

A list of the Amazon S3 paths to read from.

- `CompressionType` – UTF-8 string (valid values: `snappy="SNAPPY"` | `lzo="LZO"` | `gzip="GZIP"` | `brotli="BROTLI"` | `lz4="LZ4"` | `uncompressed="UNCOMPRESSED"` | `none="NONE"`).

Specifies how the data is compressed. This is generally not necessary
if the data has a standard file extension. Possible values are `"gzip"`
and `"bzip"`).

- `Exclusions` – An array of UTF-8 strings.

A string containing a JSON list of Unix-style glob patterns to exclude.
For example, "[\"\*\*.pdf\"]" excludes all PDF files.

- `GroupSize` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The target group size in bytes. The default is computed based on the input
data size and the size of your cluster. When there are fewer than 50,000 input files,
`"groupFiles"` must be set to `"inPartition"` for
this to take effect.

- `GroupFiles` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Grouping files is turned on by default when the input contains more than
50,000 files. To turn on grouping with fewer than 50,000 files, set this parameter
to "inPartition". To disable grouping when there are more than 50,000 files,
set this parameter to `"none"`.

- `Recurse` – Boolean.

If set to true, recursively reads files in all subdirectories under the
specified paths.

- `MaxBand` – Number (integer), not more than None.

This option controls the duration in milliseconds after which the s3 listing
is likely to be consistent. Files with modification timestamps falling within
the last maxBand milliseconds are tracked specially when using JobBookmarks
to account for Amazon S3 eventual consistency. Most users don't need to set this
option. The default is 900000 milliseconds, or 15 minutes.

- `MaxFilesInBand` – Number (integer), not more than None.

This option specifies the maximum number of files to save from the last
maxBand seconds. If this number is exceeded, extra files are skipped and only
processed in the next job run.

- `AdditionalOptions` – A [S3DirectSourceAdditionalOptions](#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions "#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions") object.

Specifies additional connection options.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the S3 Parquet source.

## S3DeltaSource structure

Specifies a Delta Lake data source stored in Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Delta Lake source.

- `Paths` – _Required:_ An array of UTF-8 strings.

A list of the Amazon S3 paths to read from.

- `AdditionalDeltaOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options.

- `AdditionalOptions` – A [S3DirectSourceAdditionalOptions](#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions "#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions") object.

Specifies additional options for the connector.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the Delta Lake source.

## S3CatalogDeltaSource structure

Specifies a Delta Lake data source that is registered in the AWS Glue Data Catalog. The data source must be stored in Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Delta Lake data source.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

- `AdditionalDeltaOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the Delta Lake source.

## CatalogDeltaSource structure

Specifies a Delta Lake data source that is registered in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Delta Lake data source.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

- `AdditionalDeltaOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the Delta Lake source.

## S3HudiSource structure

Specifies a Hudi data source stored in Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Hudi source.

- `Paths` – _Required:_ An array of UTF-8 strings.

A list of the Amazon S3 paths to read from.

- `AdditionalHudiOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options.

- `AdditionalOptions` – A [S3DirectSourceAdditionalOptions](#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions "#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions") object.

Specifies additional options for the connector.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the Hudi source.

## S3CatalogHudiSource structure

Specifies a Hudi data source that is registered in the AWS Glue Data Catalog. The Hudi data source must be stored in Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Hudi data source.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

- `AdditionalHudiOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the Hudi source.

## S3ExcelSource structure

Specifies an S3 Excel data source.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the S3 Excel data source.

- `Paths` – _Required:_ An array of UTF-8 strings.

The S3 paths where the Excel files are located.

- `CompressionType` – UTF-8 string (valid values: `snappy="SNAPPY"` | `lzo="LZO"` | `gzip="GZIP"` | `brotli="BROTLI"` | `lz4="LZ4"` | `uncompressed="UNCOMPRESSED"` | `none="NONE"`).

The compression format used for the Excel files.

- `Exclusions` – An array of UTF-8 strings.

Patterns to exclude specific files or paths from processing.

- `GroupSize` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Defines the size of file groups for batch processing.

- `GroupFiles` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies how files should be grouped for processing.

- `Recurse` – Boolean.

Indicates whether to recursively process subdirectories.

- `MaxBand` – Number (integer), not more than None.

The maximum number of processing bands to use.

- `MaxFilesInBand` – Number (integer), not more than None.

The maximum number of files to process in each band.

- `AdditionalOptions` – A [S3DirectSourceAdditionalOptions](#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions "#aws-glue-api-visual-job-api-S3DirectSourceAdditionalOptions") object.

Additional configuration options for S3 direct source processing.

- `NumberRows` – Number (long).

The number of rows to process from each Excel file.

- `SkipFooter` – Number (integer), not more than None.

The number of rows to skip at the end of each Excel file.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

The AWS Glue schemas to apply to the processed data.

## CatalogHudiSource structure

Specifies a Hudi data source that is registered in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Hudi data source.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

- `AdditionalHudiOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the Hudi source.

## DynamoDBCatalogSource structure

Specifies a DynamoDB data source in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data source.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

- `PitrEnabled` – Boolean.

Specifies whether Point-in-Time Recovery (PITR) is enabled for the DynamoDB
table. When set to `true`, allows reading from a specific point in
time. The default value is `false`.

- `AdditionalOptions` – A [DDBELTCatalogAdditionalOptions](#aws-glue-api-visual-job-api-DDBELTCatalogAdditionalOptions "#aws-glue-api-visual-job-api-DDBELTCatalogAdditionalOptions") object.

Specifies additional connection options for the DynamoDB data source.

## RelationalCatalogSource structure

Specifies a Relational database data source in the AWS Glue
Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data source.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

## JDBCConnectorTarget structure

Specifies a data target that writes to Amazon S3 in Apache Parquet columnar
storage.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `ConnectionName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the connection that is associated with the connector.

- `ConnectionTable` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the data target.

- `ConnectorName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of a connector that will be used.

- `ConnectionType` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The type of connection, such as marketplace.jdbc or custom.jdbc, designating
a connection to a JDBC data target.

- `AdditionalOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Additional connection options for the connector.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the JDBC target.

## SparkConnectorTarget structure

Specifies a target that uses an Apache Spark connector.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `ConnectionName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of a connection for an Apache Spark connector.

- `ConnectorName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of an Apache Spark connector.

- `ConnectionType` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The type of connection, such as marketplace.spark or custom.spark, designating
a connection to an Apache Spark data store.

- `AdditionalOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Additional connection options for the connector.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the custom spark target.

## BasicCatalogTarget structure

Specifies a target that uses a AWS Glue Data Catalog table.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of your data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `PartitionKeys` – An array of UTF-8 strings.

The partition keys used to distribute data across multiple partitions
or shards based on a specific key or set of key.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The database that contains the table you want to use as the target. This
database must already exist in the Data Catalog.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The table that defines the schema of your output data. This table must already
exist in the Data Catalog.

## MySQLCatalogTarget structure

Specifies a target that uses MySQL.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to write to.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to write to.

## PostgreSQLCatalogTarget structure

Specifies a target that uses Postgres SQL.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to write to.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to write to.

## OracleSQLCatalogTarget structure

Specifies a target that uses Oracle SQL.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to write to.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to write to.

## MicrosoftSQLServerCatalogTarget structure

Specifies a target that uses Microsoft SQL.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to write to.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to write to.

## RedshiftTarget structure

Specifies a target that uses Amazon Redshift.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to write to.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to write to.

- `RedshiftTmpDir` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The Amazon S3 path where temporary data can be staged when copying out of
the database.

- `TmpDirIAMRole` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The IAM role with permissions.

- `UpsertRedshiftOptions` – An [UpsertRedshiftTargetOptions](#aws-glue-api-visual-job-api-UpsertRedshiftTargetOptions "#aws-glue-api-visual-job-api-UpsertRedshiftTargetOptions") object.

The set of options to configure an upsert operation when writing to a Redshift
target.

## AmazonRedshiftTarget structure

Specifies an Amazon Redshift target.

###### Fields

- `Name` – UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Amazon Redshift target.

- `Data` – An [AmazonRedshiftNodeData](#aws-glue-api-visual-job-api-AmazonRedshiftNodeData "#aws-glue-api-visual-job-api-AmazonRedshiftNodeData") object.

Specifies the data of the Amazon Redshift target node.

- `Inputs` – An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

## UpsertRedshiftTargetOptions structure

The options to configure an upsert operation when writing to a Redshift
target .

###### Fields

- `TableLocation` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The physical location of the Redshift table.

- `ConnectionName` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the connection to use to write to Redshift.

- `UpsertKeys` – An array of UTF-8 strings.

The keys used to determine whether to perform an update or insert.

## S3CatalogTarget structure

Specifies a data target that writes to Amazon S3 using the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `PartitionKeys` – An array of UTF-8 strings.

Specifies native partitioning using a sequence of keys.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to write to.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to write to.

- `SchemaChangePolicy` – A [CatalogSchemaChangePolicy](#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy "#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy") object.

A policy that specifies update behavior for the crawler.

- `AutoDataQuality` – An [AutoDataQuality](#aws-glue-api-visual-job-api-AutoDataQuality "#aws-glue-api-visual-job-api-AutoDataQuality") object.

Specifies whether to automatically enable data quality evaluation for
the S3 catalog target. When set to `true`, data quality checks are
performed automatically during the write operation.

## S3GlueParquetTarget structure

Specifies a data target that writes to Amazon S3 in Apache Parquet columnar
storage.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `PartitionKeys` – An array of UTF-8 strings.

Specifies native partitioning using a sequence of keys.

- `Path` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

A single Amazon S3 path to write to.

- `Compression` – UTF-8 string (valid values: `snappy="SNAPPY"` | `lzo="LZO"` | `gzip="GZIP"` | `brotli="BROTLI"` | `lz4="LZ4"` | `uncompressed="UNCOMPRESSED"` | `none="NONE"`).

Specifies how the data is compressed. This is generally not necessary
if the data has a standard file extension. Possible values are `"gzip"`
and `"bzip"`).

- `NumberTargetPartitions` – UTF-8 string.

Specifies the number of target partitions for Parquet files when writing
to Amazon S3 using AWS Glue.

- `SchemaChangePolicy` – A [DirectSchemaChangePolicy](#aws-glue-api-visual-job-api-DirectSchemaChangePolicy "#aws-glue-api-visual-job-api-DirectSchemaChangePolicy") object.

A policy that specifies update behavior for the crawler.

- `AutoDataQuality` – An [AutoDataQuality](#aws-glue-api-visual-job-api-AutoDataQuality "#aws-glue-api-visual-job-api-AutoDataQuality") object.

Specifies whether to automatically enable data quality evaluation for
the S3 AWS Glue Parquet target. When set to `true`, data
quality checks are performed automatically during the write operation.

## CatalogSchemaChangePolicy structure

A policy that specifies update behavior for the crawler.

###### Fields

- `EnableUpdateCatalog` – Boolean.

Whether to use the specified update behavior when the crawler finds a changed
schema.

- `UpdateBehavior` – UTF-8 string (valid values: `UPDATE_IN_DATABASE` | `LOG`).

The update behavior when the crawler finds a changed schema.

## S3DirectTarget structure

Specifies a data target that writes to Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `PartitionKeys` – An array of UTF-8 strings.

Specifies native partitioning using a sequence of keys.

- `Path` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

A single Amazon S3 path to write to.

- `Compression` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies how the data is compressed. This is generally not necessary
if the data has a standard file extension. Possible values are `"gzip"`
and `"bzip"`).

- `NumberTargetPartitions` – UTF-8 string.

Specifies the number of target partitions when writing data directly
to Amazon S3.

- `Format` – _Required:_ UTF-8 string (valid values: `json="JSON"` | `csv="CSV"` | `avro="AVRO"` | `orc="ORC"` | `parquet="PARQUET"` | `hudi="HUDI"` | `delta="DELTA"` | `iceberg="ICEBERG"` | `hyper="HYPER"` | `xml="XML"`).

Specifies the data output format for the target.

- `SchemaChangePolicy` – A [DirectSchemaChangePolicy](#aws-glue-api-visual-job-api-DirectSchemaChangePolicy "#aws-glue-api-visual-job-api-DirectSchemaChangePolicy") object.

A policy that specifies update behavior for the crawler.

- `AutoDataQuality` – An [AutoDataQuality](#aws-glue-api-visual-job-api-AutoDataQuality "#aws-glue-api-visual-job-api-AutoDataQuality") object.

Specifies whether to automatically enable data quality evaluation for
the S3 direct target. When set to `true`, data quality checks are
performed automatically during the write operation.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the S3 direct target.

## S3HudiCatalogTarget structure

Specifies a target that writes to a Hudi data source in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `PartitionKeys` – An array of UTF-8 strings.

Specifies native partitioning using a sequence of keys.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to write to.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to write to.

- `AdditionalOptions` – _Required:_ A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options for the connector.

- `SchemaChangePolicy` – A [CatalogSchemaChangePolicy](#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy "#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy") object.

A policy that specifies update behavior for the crawler.

- `AutoDataQuality` – An [AutoDataQuality](#aws-glue-api-visual-job-api-AutoDataQuality "#aws-glue-api-visual-job-api-AutoDataQuality") object.

Specifies whether to automatically enable data quality evaluation for
the S3 Hudi catalog target. When set to `true`, data quality checks
are performed automatically during the write operation.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the S3 Hudi catalog target.

## S3HudiDirectTarget structure

Specifies a target that writes to a Hudi data source in Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `Path` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The Amazon S3 path of your Hudi data source to write to.

- `Compression` – _Required:_ UTF-8 string (valid values: `gzip="GZIP"` | `lzo="LZO"` | `uncompressed="UNCOMPRESSED"` | `snappy="SNAPPY"`).

Specifies how the data is compressed. This is generally not necessary
if the data has a standard file extension. Possible values are `"gzip"`
and `"bzip"`).

- `NumberTargetPartitions` – UTF-8 string.

Specifies the number of target partitions for distributing Hudi dataset
files across Amazon S3.

- `PartitionKeys` – An array of UTF-8 strings.

Specifies native partitioning using a sequence of keys.

- `Format` – _Required:_ UTF-8 string (valid values: `json="JSON"` | `csv="CSV"` | `avro="AVRO"` | `orc="ORC"` | `parquet="PARQUET"` | `hudi="HUDI"` | `delta="DELTA"` | `iceberg="ICEBERG"` | `hyper="HYPER"` | `xml="XML"`).

Specifies the data output format for the target.

- `AdditionalOptions` – _Required:_ A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options for the connector.

- `SchemaChangePolicy` – A [DirectSchemaChangePolicy](#aws-glue-api-visual-job-api-DirectSchemaChangePolicy "#aws-glue-api-visual-job-api-DirectSchemaChangePolicy") object.

A policy that specifies update behavior for the crawler.

- `AutoDataQuality` – An [AutoDataQuality](#aws-glue-api-visual-job-api-AutoDataQuality "#aws-glue-api-visual-job-api-AutoDataQuality") object.

Specifies whether to automatically enable data quality evaluation for
the S3 Hudi direct target. When set to `true`, data quality checks
are performed automatically during the write operation.

## S3DeltaCatalogTarget structure

Specifies a target that writes to a Delta Lake data source in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `PartitionKeys` – An array of UTF-8 strings.

Specifies native partitioning using a sequence of keys.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to write to.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to write to.

- `AdditionalOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options for the connector.

- `SchemaChangePolicy` – A [CatalogSchemaChangePolicy](#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy "#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy") object.

A policy that specifies update behavior for the crawler.

- `AutoDataQuality` – An [AutoDataQuality](#aws-glue-api-visual-job-api-AutoDataQuality "#aws-glue-api-visual-job-api-AutoDataQuality") object.

Specifies whether to automatically enable data quality evaluation for
the S3 Delta catalog target. When set to `true`, data quality checks
are performed automatically during the write operation.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the S3 Delta catalog target.

## S3DeltaDirectTarget structure

Specifies a target that writes to a Delta Lake data source in Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `PartitionKeys` – An array of UTF-8 strings.

Specifies native partitioning using a sequence of keys.

- `Path` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The Amazon S3 path of your Delta Lake data source to write to.

- `Compression` – _Required:_ UTF-8 string (valid values: `uncompressed="UNCOMPRESSED"` | `snappy="SNAPPY"`).

Specifies how the data is compressed. This is generally not necessary
if the data has a standard file extension. Possible values are `"gzip"`
and `"bzip"`).

- `NumberTargetPartitions` – UTF-8 string.

Specifies the number of target partitions for distributing Delta Lake
dataset files across Amazon S3.

- `Format` – _Required:_ UTF-8 string (valid values: `json="JSON"` | `csv="CSV"` | `avro="AVRO"` | `orc="ORC"` | `parquet="PARQUET"` | `hudi="HUDI"` | `delta="DELTA"` | `iceberg="ICEBERG"` | `hyper="HYPER"` | `xml="XML"`).

Specifies the data output format for the target.

- `AdditionalOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options for the connector.

- `SchemaChangePolicy` – A [DirectSchemaChangePolicy](#aws-glue-api-visual-job-api-DirectSchemaChangePolicy "#aws-glue-api-visual-job-api-DirectSchemaChangePolicy") object.

A policy that specifies update behavior for the crawler.

- `AutoDataQuality` – An [AutoDataQuality](#aws-glue-api-visual-job-api-AutoDataQuality "#aws-glue-api-visual-job-api-AutoDataQuality") object.

Specifies whether to automatically enable data quality evaluation for
the S3 Delta direct target. When set to `true`, data quality checks
are performed automatically during the write operation.

## S3HyperDirectTarget structure

Specifies a HyperDirect data target that writes to Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The unique identifier for the HyperDirect target node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

Specifies the input source for the HyperDirect target.

- `Format` – UTF-8 string (valid values: `json="JSON"` | `csv="CSV"` | `avro="AVRO"` | `orc="ORC"` | `parquet="PARQUET"` | `hudi="HUDI"` | `delta="DELTA"` | `iceberg="ICEBERG"` | `hyper="HYPER"` | `xml="XML"`).

Specifies the data output format for the HyperDirect target.

- `PartitionKeys` – An array of UTF-8 strings.

Defines the partitioning strategy for the output data.

- `Path` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The S3 location where the output data will be written.

- `Compression` – UTF-8 string (valid values: `uncompressed="UNCOMPRESSED"`).

The compression type to apply to the output data.

- `SchemaChangePolicy` – A [DirectSchemaChangePolicy](#aws-glue-api-visual-job-api-DirectSchemaChangePolicy "#aws-glue-api-visual-job-api-DirectSchemaChangePolicy") object.

Defines how schema changes are handled during write operations.

- `AutoDataQuality` – An [AutoDataQuality](#aws-glue-api-visual-job-api-AutoDataQuality "#aws-glue-api-visual-job-api-AutoDataQuality") object.

Specifies whether to automatically enable data quality evaluation for
the S3 Hyper direct target. When set to `true`, data quality checks
are performed automatically during the write operation.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the S3 Hyper direct target.

## S3IcebergDirectTarget structure

Specifies a target that writes to an Iceberg data source in Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

Specifies the unique identifier for the Iceberg target node in your data
pipeline.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

Defines the single input source that provides data to this Iceberg target.

- `PartitionKeys` – An array of UTF-8 strings.

Specifies the columns used to partition the Iceberg table data in S3.

- `Path` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Defines the S3 location where the Iceberg table data will be stored.

- `Format` – _Required:_ UTF-8 string (valid values: `json="JSON"` | `csv="CSV"` | `avro="AVRO"` | `orc="ORC"` | `parquet="PARQUET"` | `hudi="HUDI"` | `delta="DELTA"` | `iceberg="ICEBERG"` | `hyper="HYPER"` | `xml="XML"`).

Specifies the file format used for storing Iceberg table data (e.g., Parquet,
ORC).

- `AdditionalOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Provides additional configuration options for customizing the Iceberg
table behavior.

- `SchemaChangePolicy` – A [DirectSchemaChangePolicy](#aws-glue-api-visual-job-api-DirectSchemaChangePolicy "#aws-glue-api-visual-job-api-DirectSchemaChangePolicy") object.

Defines how schema changes are handled when writing data to the Iceberg
table.

- `Compression` – _Required:_ UTF-8 string (valid values: `gzip="GZIP"` | `lzo="LZO"` | `uncompressed="UNCOMPRESSED"` | `snappy="SNAPPY"`).

Specifies the compression codec used for Iceberg table files in S3.

- `NumberTargetPartitions` – UTF-8 string.

Sets the number of target partitions for distributing Iceberg table files
across S3.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the S3 Iceberg direct target.

## DirectSchemaChangePolicy structure

A policy that specifies update behavior for the crawler.

###### Fields

- `EnableUpdateCatalog` – Boolean.

Whether to use the specified update behavior when the crawler finds a changed
schema.

- `UpdateBehavior` – UTF-8 string (valid values: `UPDATE_IN_DATABASE` | `LOG`).

The update behavior when the crawler finds a changed schema.

- `Table` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the table in the database that the schema change policy applies
to.

- `Database` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the database that the schema change policy applies to.

## ApplyMapping structure

Specifies a transform that maps data property keys in the data source to
data property keys in the data target. You can rename keys, modify the data types
for keys, and choose which keys to drop from the dataset.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The data inputs identified by their node names.

- `Mapping` – _Required:_ An array of [Mapping](#aws-glue-api-visual-job-api-Mapping "#aws-glue-api-visual-job-api-Mapping") objects.

Specifies the mapping of data property keys in the data source to data property
keys in the data target.

## Mapping structure

Specifies the mapping of data property keys.

###### Fields

- `ToKey` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

After the apply mapping, what the name of the column should be. Can be the
same as `FromPath`.

- `FromPath` – An array of UTF-8 strings.

The table or column to be modified.

- `FromType` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The type of the data to be modified.

- `ToType` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The data type that the data is to be modified to.

- `Dropped` – Boolean.

If true, then the column is removed.

- `Children` – An array of Mapping objects.

Only applicable to nested data structures. If you want to change the parent
structure, but also one of its children, you can fill out this data strucutre.
It is also `Mapping`, but its `FromPath` will be the
parent's `FromPath` plus the `FromPath` from this
structure.

For the children part, suppose you have the structure:

`{ "FromPath": "OuterStructure", "ToKey": "OuterStructure",
 "ToType": "Struct", "Dropped": false, "Chidlren": [{ "FromPath": "inner",
 "ToKey": "inner", "ToType": "Double", "Dropped": false, }] }`

You can specify a `Mapping` that looks like:

`{ "FromPath": "OuterStructure", "ToKey": "OuterStructure",
 "ToType": "Struct", "Dropped": false, "Chidlren": [{ "FromPath": "inner",
 "ToKey": "inner", "ToType": "Double", "Dropped": false, }] }`

## SelectFields structure

Specifies a transform that chooses the data property keys that you want
to keep.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The data inputs identified by their node names.

- `Paths` – _Required:_ An array of UTF-8 strings.

A JSON path to a variable in the data structure.

## DropFields structure

Specifies a transform that chooses the data property keys that you want
to drop.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The data inputs identified by their node names.

- `Paths` – _Required:_ An array of UTF-8 strings.

A JSON path to a variable in the data structure.

## RenameField structure

Specifies a transform that renames a single data property key.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The data inputs identified by their node names.

- `SourcePath` – _Required:_ An array of UTF-8 strings.

A JSON path to a variable in the data structure for the source data.

- `TargetPath` – _Required:_ An array of UTF-8 strings.

A JSON path to a variable in the data structure for the target data.

## Spigot structure

Specifies a transform that writes samples of the data to an Amazon S3 bucket.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The data inputs identified by their node names.

- `Path` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

A path in Amazon S3 where the transform will write a subset of records from
the dataset to a JSON file in an Amazon S3 bucket.

- `Topk` – Number (integer), not more than 100.

Specifies a number of records to write starting from the beginning of the
dataset.

- `Prob` – Number (double), not more than 1.

The probability (a decimal value with a maximum value of 1) of picking any
given record. A value of 1 indicates that each row read from the dataset should
be included in the sample output.

## Join structure

Specifies a transform that joins two datasets into one dataset using a
comparison phrase on the specified data property keys. You can use inner, outer,
left, right, left semi, and left anti joins.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 2 or more than 2 strings.

The data inputs identified by their node names.

- `JoinType` – _Required:_ UTF-8 string (valid values: `equijoin="EQUIJOIN"` | `left="LEFT"` | `right="RIGHT"` | `outer="OUTER"` | `leftsemi="LEFT_SEMI"` | `leftanti="LEFT_ANTI"`).

Specifies the type of join to be performed on the datasets.

- `Columns` – _Required:_ An array of [JoinColumn](#aws-glue-api-visual-job-api-JoinColumn "#aws-glue-api-visual-job-api-JoinColumn") objects, not less than 2 or more than 2 structures.

A list of the two columns to be joined.

## JoinColumn structure

Specifies a column to be joined.

###### Fields

- `From` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The column to be joined.

- `Keys` – _Required:_ An array of UTF-8 strings.

The key of the column to be joined.

## SplitFields structure

Specifies a transform that splits data property keys into two `DynamicFrames`.
The output is a collection of `DynamicFrames`: one with selected
data property keys, and one with the remaining data property keys.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The data inputs identified by their node names.

- `Paths` – _Required:_ An array of UTF-8 strings.

A JSON path to a variable in the data structure.

## SelectFromCollection structure

Specifies a transform that chooses one `DynamicFrame` from
a collection of `DynamicFrames`. The output is the selected `DynamicFrame`

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The data inputs identified by their node names.

- `Index` – _Required:_ Number (integer), not more than None.

The index for the DynamicFrame to be selected.

## FillMissingValues structure

Specifies a transform that locates records in the dataset that have missing
values and adds a new field with a value determined by imputation. The input data
set is used to train the machine learning model that determines what the missing
value should be.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The data inputs identified by their node names.

- `ImputedPath` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

A JSON path to a variable in the data structure for the dataset that is imputed.

- `FilledPath` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

A JSON path to a variable in the data structure for the dataset that is filled.

## Filter structure

Specifies a transform that splits a dataset into two, based on a filter
condition.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The data inputs identified by their node names.

- `LogicalOperator` – _Required:_ UTF-8 string (valid values: `AND` | `OR`).

The operator used to filter rows by comparing the key value to a specified
value.

- `Filters` – _Required:_ An array of [FilterExpression](#aws-glue-api-visual-job-api-FilterExpression "#aws-glue-api-visual-job-api-FilterExpression") objects.

Specifies a filter expression.

## FilterExpression structure

Specifies a filter expression.

###### Fields

- `Operation` – _Required:_ UTF-8 string (valid values: `EQ` | `LT` | `GT` | `LTE` | `GTE` | `REGEX` | `ISNULL`).

The type of operation to perform in the expression.

- `Negated` – Boolean.

Whether the expression is to be negated.

- `Values` – _Required:_ An array of [FilterValue](#aws-glue-api-visual-job-api-FilterValue "#aws-glue-api-visual-job-api-FilterValue") objects.

A list of filter values.

## FilterValue structure

Represents a single entry in the list of values for a `FilterExpression`.

###### Fields

- `Type` – _Required:_ UTF-8 string (valid values: `COLUMNEXTRACTED` | `CONSTANT`).

The type of filter value.

- `Value` – _Required:_ An array of UTF-8 strings.

The value to be associated.

## CustomCode structure

Specifies a transform that uses custom code you provide to perform the
data transformation. The output is a collection of DynamicFrames.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, at least 1 string.

The data inputs identified by their node names.

- `Code` – _Required:_ UTF-8 string, matching the [Custom string pattern #54](aws-glue-api-common.md#regex_54 "aws-glue-api-common.md#regex_54").

The custom code that is used to perform the data transformation.

- `ClassName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name defined for the custom code node class.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the custom code transform.

## SparkSQL structure

Specifies a transform where you enter a SQL query using Spark SQL syntax
to transform the data. The output is a single `DynamicFrame`.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, at least 1 string.

The data inputs identified by their node names. You can associate a table
name with each input node to use in the SQL query. The name you choose must meet the
Spark SQL naming restrictions.

- `SqlQuery` – _Required:_ UTF-8 string, matching the [Custom string pattern #62](aws-glue-api-common.md#regex_62 "aws-glue-api-common.md#regex_62").

A SQL query that must use Spark SQL syntax and return a single data set.

- `SqlAliases` – _Required:_ An array of [SqlAlias](#aws-glue-api-visual-job-api-SqlAlias "#aws-glue-api-visual-job-api-SqlAlias") objects.

A list of aliases. An alias allows you to specify what name to use in the SQL
for a given input. For example, you have a datasource named "MyDataSource". If
you specify `From` as MyDataSource, and `Alias` as
SqlName, then in your SQL you can do:

`select * from SqlName`

and that gets data from MyDataSource.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the SparkSQL transform.

## SqlAlias structure

Represents a single entry in the list of values for `SqlAliases`.

###### Fields

- `From` – _Required:_ UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

A table, or a column in a table.

- `Alias` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

A temporary name given to a table, or a column in a table.

## DropNullFields structure

Specifies a transform that removes columns from the dataset if all values
in the column are 'null'. By default, AWS Glue Studio will recognize
null objects, but some values such as empty strings, strings that are "null",
-1 integers or other placeholders such as zeros, are not automatically recognized
as nulls.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The data inputs identified by their node names.

- `NullCheckBoxList` – A [NullCheckBoxList](#aws-glue-api-visual-job-api-NullCheckBoxList "#aws-glue-api-visual-job-api-NullCheckBoxList") object.

A structure that represents whether certain values are recognized as
null values for removal.

- `NullTextList` – An array of [NullValueField](#aws-glue-api-visual-job-api-NullValueField "#aws-glue-api-visual-job-api-NullValueField") objects, not more than 50 structures.

A structure that specifies a list of NullValueField structures that represent
a custom null value such as zero or other value being used as a null placeholder
unique to the dataset.

The `DropNullFields` transform removes custom null values
only if both the value of the null placeholder and the datatype match the data.

## NullCheckBoxList structure

Represents whether certain values are recognized as null values for removal.

###### Fields

- `IsEmpty` – Boolean.

Specifies that an empty string is considered as a null value.

- `IsNullString` – Boolean.

Specifies that a value spelling out the word 'null' is considered as a null
value.

- `IsNegOne` – Boolean.

Specifies that an integer value of -1 is considered as a null value.

## NullValueField structure

Represents a custom null value such as a zeros or other value being used
as a null placeholder unique to the dataset.

###### Fields

- `Value` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The value of the null placeholder.

- `Datatype` – _Required:_ A [Datatype](#aws-glue-api-visual-job-api-Datatype "#aws-glue-api-visual-job-api-Datatype") object.

The datatype of the value.

## Datatype structure

A structure representing the datatype of the value.

###### Fields

- `Id` – _Required:_ UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

The datatype of the value.

- `Label` – _Required:_ UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

A label assigned to the datatype.

## Merge structure

Specifies a transform that merges a `DynamicFrame` with
a staging `DynamicFrame` based on the specified primary keys to
identify records. Duplicate records (records with the same primary keys) are
not de-duplicated.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 2 or more than 2 strings.

The data inputs identified by their node names.

- `Source` – _Required:_ UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

The source `DynamicFrame` that will be merged with a staging
`DynamicFrame`.

- `PrimaryKeys` – _Required:_ An array of UTF-8 strings.

The list of primary key fields to match records from the source and staging
dynamic frames.

## Union structure

Specifies a transform that combines the rows from two or more datasets
into a single result.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 2 or more than 2 strings.

The node ID inputs to the transform.

- `UnionType` – _Required:_ UTF-8 string (valid values: `ALL` | `DISTINCT`).

Indicates the type of Union transform.

Specify `ALL` to join all rows from data sources to the resulting
DynamicFrame. The resulting union does not remove duplicate rows.

Specify `DISTINCT` to remove duplicate rows in the resulting
DynamicFrame.

## PIIDetection structure

Specifies a transform that identifies, removes or masks PII data.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The node ID inputs to the transform.

- `PiiType` – _Required:_ UTF-8 string (valid values: `RowAudit` | `RowHashing` | `RowMasking` | `RowPartialMasking` | `ColumnAudit` | `ColumnHashing` | `ColumnMasking`).

Indicates the type of PIIDetection transform.

- `EntityTypesToDetect` – _Required:_ An array of UTF-8 strings.

Indicates the types of entities the PIIDetection transform will identify
as PII data.

PII type entities include: PERSON_NAME, DATE, USA_SNN, EMAIL, USA_ITIN,
USA_PASSPORT_NUMBER, PHONE_NUMBER, BANK_ACCOUNT, IP_ADDRESS, MAC_ADDRESS,
USA_CPT_CODE, USA_HCPCS_CODE, USA_NATIONAL_DRUG_CODE, USA_MEDICARE_BENEFICIARY_IDENTIFIER,
USA_HEALTH_INSURANCE_CLAIM_NUMBER,CREDIT_CARD,USA_NATIONAL_PROVIDER_IDENTIFIER,USA_DEA_NUMBER,USA_DRIVING_LICENSE

- `OutputColumnName` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Indicates the output column name that will contain any entity type detected
in that row.

- `SampleFraction` – Number (double), not more than 1.

Indicates the fraction of the data to sample when scanning for PII entities.

- `ThresholdFraction` – Number (double), not more than 1.

Indicates the fraction of the data that must be met in order for a column
to be identified as PII data.

- `MaskValue` – UTF-8 string, not more than 256 bytes long, matching the [Custom string pattern #58](aws-glue-api-common.md#regex_58 "aws-glue-api-common.md#regex_58").

Indicates the value that will replace the detected entity.

- `RedactText` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies whether to redact the detected PII text. When set to `true`,
PII content is replaced with redaction characters.

- `RedactChar` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The character used to replace detected PII content when redaction is enabled.
The default redaction character is `*`.

- `MatchPattern` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

A regular expression pattern used to identify additional PII content
beyond the standard detection algorithms.

- `NumLeftCharsToExclude` – Number (integer), not more than None.

The number of characters to exclude from redaction on the left side of detected
PII content. This allows preserving context around the sensitive data.

- `NumRightCharsToExclude` – Number (integer), not more than None.

The number of characters to exclude from redaction on the right side of
detected PII content. This allows preserving context around the sensitive data.

- `DetectionParameters` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Additional parameters for configuring PII detection behavior and sensitivity
settings.

- `DetectionSensitivity` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The sensitivity level for PII detection. Higher sensitivity levels detect
more potential PII but may result in more false positives.

## Aggregate structure

Specifies a transform that groups rows by chosen fields and computes the
aggregated value by specified function.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

Specifies the fields and rows to use as inputs for the aggregate transform.

- `Groups` – _Required:_ An array of UTF-8 strings.

Specifies the fields to group by.

- `Aggs` – _Required:_ An array of [AggregateOperation](#aws-glue-api-visual-job-api-AggregateOperation "#aws-glue-api-visual-job-api-AggregateOperation") objects, not less than 1 or more than 30 structures.

Specifies the aggregate functions to be performed on specified fields.

## DropDuplicates structure

Specifies a transform that removes rows of repeating data from a data set.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the transform node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The data inputs identified by their node names.

- `Columns` – An array of UTF-8 strings.

The name of the columns to be merged or removed if repeating.

## GovernedCatalogTarget structure

Specifies a data target that writes to Amazon S3 using the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `PartitionKeys` – An array of UTF-8 strings.

Specifies native partitioning using a sequence of keys.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to write to.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to write to.

- `SchemaChangePolicy` – A [CatalogSchemaChangePolicy](#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy "#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy") object.

A policy that specifies update behavior for the governed catalog.

## GovernedCatalogSource structure

Specifies the data store in the governed AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data store.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The database table to read from.

- `PartitionPredicate` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Partitions satisfying this predicate are deleted. Files within the retention
period in these partitions are not deleted. Set to `""` –
empty by default.

- `AdditionalOptions` – A [S3SourceAdditionalOptions](#aws-glue-api-visual-job-api-S3SourceAdditionalOptions "#aws-glue-api-visual-job-api-S3SourceAdditionalOptions") object.

Specifies additional connection options.

## AggregateOperation structure

Specifies the set of parameters needed to perform aggregation in the aggregate
transform.

###### Fields

- `Column` – _Required:_ An array of UTF-8 strings.

Specifies the column on the data set on which the aggregation function
will be applied.

- `AggFunc` – _Required:_ UTF-8 string (valid values: `avg` | `countDistinct` | `count` | `first` | `last` | `kurtosis` | `max` | `min` | `skewness` | `stddev_samp` | `stddev_pop` | `sum` | `sumDistinct` | `var_samp` | `var_pop`).

Specifies the aggregation function to apply.

Possible aggregation functions include: avg countDistinct, count,
first, last, kurtosis, max, min, skewness, stddev_samp, stddev_pop, sum, sumDistinct,
var_samp, var_pop

## GlueSchema structure

Specifies a user-defined schema when a schema cannot be determined by
AWS Glue.

###### Fields

- `Columns` – An array of [GlueStudioSchemaColumn](#aws-glue-api-visual-job-api-GlueStudioSchemaColumn "#aws-glue-api-visual-job-api-GlueStudioSchemaColumn") objects.

Specifies the column definitions that make up a AWS Glue schema.

## GlueStudioSchemaColumn structure

Specifies a single column in a AWS Glue schema definition.

###### Fields

- `Name` – _Required:_ UTF-8 string, not more than 1024 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the column in the AWS Glue Studio schema.

- `Type` – UTF-8 string, not more than 131072 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The hive type for this column in the AWS Glue Studio schema.

- `GlueStudioType` – UTF-8 string, not more than 131072 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The data type of the column as defined in AWS Glue Studio.

## GlueStudioColumn structure

Specifies a single column in AWS GlueStudio.

###### Fields

- `Key` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The key of the column in AWS Glue Studio.

- `FullPath` – _Required:_ An array of UTF-8 strings.

TThe full URL of the column in AWS Glue Studio.

- `Type` – _Required:_ UTF-8 string (valid values: `array="ARRAY"` | `bigint="BIGINT"` | `bigint array="BIGINT_ARRAY"` | `binary="BINARY"` | `binary array="BINARY_ARRAY"` | `boolean="BOOLEAN"` | `boolean array="BOOLEAN_ARRAY"` | `byte="BYTE"` | `byte array="BYTE_ARRAY"` | `char="CHAR"` | `char array="CHAR_ARRAY"` | `choice="CHOICE"` | `choice array="CHOICE_ARRAY"` | `date="DATE"` | `date array="DATE_ARRAY"` | `decimal="DECIMAL"` | `decimal array="DECIMAL_ARRAY"` | `double="DOUBLE"` | `double array="DOUBLE_ARRAY"` | `enum="ENUM"` | `enum array="ENUM_ARRAY"` | `float="FLOAT"` | `float array="FLOAT_ARRAY"` | `int="INT"` | `int array="INT_ARRAY"` | `interval="INTERVAL"` | `interval array="INTERVAL_ARRAY"` | `long="LONG"` | `long array="LONG_ARRAY"` | `object="OBJECT"` | `short="SHORT"` | `short array="SHORT_ARRAY"` | `smallint="SMALLINT"` | `smallint array="SMALLINT_ARRAY"` | `string="STRING"` | `string array="STRING_ARRAY"` | `timestamp="TIMESTAMP"` | `timestamp array="TIMESTAMP_ARRAY"` | `tinyint="TINYINT"` | `tinyint array="TINYINT_ARRAY"` | `varchar="VARCHAR"` | `varchar array="VARCHAR_ARRAY"` | `null="NULL"` | `unknown="UNKNOWN"` | `unknown array="UNKNOWN_ARRAY"`).

TThe type of the column in AWS Glue Studio.

- `Children` – An array of a structures.

TThe children of the parent column in AWS Glue Studio.

- `GlueStudioType` – UTF-8 string (valid values: `array="ARRAY"` | `bigint="BIGINT"` | `bigint array="BIGINT_ARRAY"` | `binary="BINARY"` | `binary array="BINARY_ARRAY"` | `boolean="BOOLEAN"` | `boolean array="BOOLEAN_ARRAY"` | `byte="BYTE"` | `byte array="BYTE_ARRAY"` | `char="CHAR"` | `char array="CHAR_ARRAY"` | `choice="CHOICE"` | `choice array="CHOICE_ARRAY"` | `date="DATE"` | `date array="DATE_ARRAY"` | `decimal="DECIMAL"` | `decimal array="DECIMAL_ARRAY"` | `double="DOUBLE"` | `double array="DOUBLE_ARRAY"` | `enum="ENUM"` | `enum array="ENUM_ARRAY"` | `float="FLOAT"` | `float array="FLOAT_ARRAY"` | `int="INT"` | `int array="INT_ARRAY"` | `interval="INTERVAL"` | `interval array="INTERVAL_ARRAY"` | `long="LONG"` | `long array="LONG_ARRAY"` | `object="OBJECT"` | `short="SHORT"` | `short array="SHORT_ARRAY"` | `smallint="SMALLINT"` | `smallint array="SMALLINT_ARRAY"` | `string="STRING"` | `string array="STRING_ARRAY"` | `timestamp="TIMESTAMP"` | `timestamp array="TIMESTAMP_ARRAY"` | `tinyint="TINYINT"` | `tinyint array="TINYINT_ARRAY"` | `varchar="VARCHAR"` | `varchar array="VARCHAR_ARRAY"` | `null="NULL"` | `unknown="UNKNOWN"` | `unknown array="UNKNOWN_ARRAY"`).

The data type of the column as defined in AWS Glue Studio.

## DynamicTransform structure

Specifies the set of parameters needed to perform the dynamic transform.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the name of the dynamic transform.

- `TransformName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the name of the dynamic transform as it appears in the AWS Glue Studio visual editor.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

Specifies the inputs for the dynamic transform that are required.

- `Parameters` – An array of [TransformConfigParameter](#aws-glue-api-visual-job-api-TransformConfigParameter "#aws-glue-api-visual-job-api-TransformConfigParameter") objects.

Specifies the parameters of the dynamic transform.

- `FunctionName` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the name of the function of the dynamic transform.

- `Path` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the path of the dynamic transform source and config files.

- `Version` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

This field is not used and will be deprecated in future release.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the dynamic transform.

## TransformConfigParameter structure

Specifies the parameters in the config file of the dynamic transform.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the name of the parameter in the config file of the dynamic transform.

- `Type` – _Required:_ UTF-8 string (valid values: `str="STR"` | `int="INT"` | `float="FLOAT"` | `complex="COMPLEX"` | `bool="BOOL"` | `list="LIST"` | `null="NULL"`).

Specifies the parameter type in the config file of the dynamic transform.

- `ValidationRule` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the validation rule in the config file of the dynamic transform.

- `ValidationMessage` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the validation message in the config file of the dynamic transform.

- `Value` – An array of UTF-8 strings.

Specifies the value of the parameter in the config file of the dynamic transform.

- `ListType` – UTF-8 string (valid values: `str="STR"` | `int="INT"` | `float="FLOAT"` | `complex="COMPLEX"` | `bool="BOOL"` | `list="LIST"` | `null="NULL"`).

Specifies the list type of the parameter in the config file of the dynamic
transform.

- `IsOptional` – Boolean.

Specifies whether the parameter is optional or not in the config file of
the dynamic transform.

## EvaluateDataQuality structure

Specifies your data quality evaluation criteria.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data quality evaluation.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The inputs of your data quality evaluation.

- `Ruleset` – _Required:_ UTF-8 string, not less than 1 or more than 65536 bytes long, matching the [Custom string pattern #59](aws-glue-api-common.md#regex_59 "aws-glue-api-common.md#regex_59").

The ruleset for your data quality evaluation.

- `Output` – UTF-8 string (valid values: `PrimaryInput` | `EvaluationResults`).

The output of your data quality evaluation.

- `PublishingOptions` – A [DQResultsPublishingOptions](#aws-glue-api-visual-job-api-DQResultsPublishingOptions "#aws-glue-api-visual-job-api-DQResultsPublishingOptions") object.

Options to configure how your results are published.

- `StopJobOnFailureOptions` – A [DQStopJobOnFailureOptions](#aws-glue-api-visual-job-api-DQStopJobOnFailureOptions "#aws-glue-api-visual-job-api-DQStopJobOnFailureOptions") object.

Options to configure how your job will stop if your data quality evaluation
fails.

## DQResultsPublishingOptions structure

Options to configure how your data quality evaluation results are published.

###### Fields

- `EvaluationContext` – UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

The context of the evaluation.

- `ResultsS3Prefix` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The Amazon S3 prefix prepended to the results.

- `CloudWatchMetricsEnabled` – Boolean.

Enable metrics for your data quality results.

- `ResultsPublishingEnabled` – Boolean.

Enable publishing for your data quality results.

## DQStopJobOnFailureOptions structure

Options to configure how your job will stop if your data quality evaluation
fails.

###### Fields

- `StopJobOnFailureTiming` – UTF-8 string (valid values: `Immediate` | `AfterDataLoad`).

When to stop job if your data quality evaluation fails. Options are Immediate
or AfterDataLoad.

## EvaluateDataQualityMultiFrame structure

Specifies your data quality evaluation criteria.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data quality evaluation.

- `Inputs` – _Required:_ An array of UTF-8 strings, at least 1 string.

The inputs of your data quality evaluation. The first input in this list
is the primary data source.

- `AdditionalDataSources` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The aliases of all data sources except primary.

- `Ruleset` – _Required:_ UTF-8 string, not less than 1 or more than 65536 bytes long, matching the [Custom string pattern #59](aws-glue-api-common.md#regex_59 "aws-glue-api-common.md#regex_59").

The ruleset for your data quality evaluation.

- `PublishingOptions` – A [DQResultsPublishingOptions](#aws-glue-api-visual-job-api-DQResultsPublishingOptions "#aws-glue-api-visual-job-api-DQResultsPublishingOptions") object.

Options to configure how your results are published.

- `AdditionalOptions` – A map array of key-value pairs.

Each key is a UTF-8 string (valid values: `performanceTuning.caching="CacheOption"` | `observations.scope="ObservationsOption"` | `compositeRuleEvaluation.method="CompositeOption"`).

Each value is a UTF-8 string.

Options to configure runtime behavior of the transform.

- `StopJobOnFailureOptions` – A [DQStopJobOnFailureOptions](#aws-glue-api-visual-job-api-DQStopJobOnFailureOptions "#aws-glue-api-visual-job-api-DQStopJobOnFailureOptions") object.

Options to configure how your job will stop if your data quality evaluation
fails.

## Recipe structure

A AWS Glue Studio node that uses a AWS Glue DataBrew recipe
in AWS Glue jobs.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the AWS Glue Studio node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the recipe node, identified by id.

- `RecipeReference` – A [RecipeReference](#aws-glue-api-visual-job-api-RecipeReference "#aws-glue-api-visual-job-api-RecipeReference") object.

A reference to the DataBrew recipe used by the node.

- `RecipeSteps` – An array of [RecipeStep](#aws-glue-api-visual-job-api-RecipeStep "#aws-glue-api-visual-job-api-RecipeStep") objects.

Transform steps used in the recipe node.

## RecipeReference structure

A reference to a AWS Glue DataBrew recipe.

###### Fields

- `RecipeArn` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The ARN of the DataBrew recipe.

- `RecipeVersion` – _Required:_ UTF-8 string, not less than 1 or more than 16 bytes long.

The RecipeVersion of the DataBrew recipe.

## SnowflakeNodeData structure

Specifies configuration for Snowflake nodes in AWS Glue Studio.

###### Fields

- `SourceType` – UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

Specifies how retrieved data is specified. Valid values: `"table"`,
`"query"`.

- `Connection` – An [Option](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option") object.

Specifies a AWS Glue Data Catalog Connection to a Snowflake
endpoint.

- `Schema` – UTF-8 string.

Specifies a Snowflake database schema for your node to use.

- `Table` – UTF-8 string.

Specifies a Snowflake table for your node to use.

- `Database` – UTF-8 string.

Specifies a Snowflake database for your node to use.

- `TempDir` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Not currently used.

- `IamRole` – An [Option](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option") object.

Not currently used.

- `AdditionalOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional options passed to the Snowflake connector. If options
are specified elsewhere in this node, this will take precedence.

- `SampleQuery` – UTF-8 string.

A SQL string used to retrieve data with the `query` sourcetype.

- `PreAction` – UTF-8 string.

A SQL string run before the Snowflake connector performs its standard
actions.

- `PostAction` – UTF-8 string.

A SQL string run after the Snowflake connector performs its standard actions.

- `Action` – UTF-8 string.

Specifies what action to take when writing to a table with preexisting
data. Valid values: `append`, `merge`, `truncate`,
`drop`.

- `Upsert` – Boolean.

Used when Action is `append`. Specifies the resolution behavior
when a row already exists. If true, preexisting rows will be updated. If false,
those rows will be inserted.

- `MergeAction` – UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

Specifies a merge action. Valid values: `simple`, `custom`.
If simple, merge behavior is defined by `MergeWhenMatched` and
`MergeWhenNotMatched`. If custom, defined by `MergeClause`.

- `MergeWhenMatched` – UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

Specifies how to resolve records that match preexisting data when merging.
Valid values: `update`, `delete`.

- `MergeWhenNotMatched` – UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

Specifies how to process records that do not match preexisting data when
merging. Valid values: `insert`, `none`.

- `MergeClause` – UTF-8 string.

A SQL statement that specifies a custom merge behavior.

- `StagingTable` – UTF-8 string.

The name of a staging table used when performing `merge` or
upsert `append` actions. Data is written to this table, then moved
to `table` by a generated postaction.

- `SelectedColumns` – An array of [Option](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option") objects.

Specifies the columns combined to identify a record when detecting matches
for merges and upserts. A list of structures with `value`, `label`
and `description` keys. Each structure describes a column.

- `AutoPushdown` – Boolean.

Specifies whether automatic query pushdown is enabled. If pushdown is
enabled, then when a query is run on Spark, if part of the query can be "pushed down"
to the Snowflake server, it is pushed down. This improves performance of some
queries.

- `TableSchema` – An array of [Option](#aws-glue-api-visual-job-api-Option "#aws-glue-api-visual-job-api-Option") objects.

Manually defines the target schema for the node. A list of structures with
`value` , `label` and `description` keys.
Each structure defines a column.

## SnowflakeSource structure

Specifies a Snowflake data source.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Snowflake data source.

- `Data` – _Required:_ A [SnowflakeNodeData](#aws-glue-api-visual-job-api-SnowflakeNodeData "#aws-glue-api-visual-job-api-SnowflakeNodeData") object.

Configuration for the Snowflake data source.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies user-defined schemas for your output data.

## SnowflakeTarget structure

Specifies a Snowflake target.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Snowflake target.

- `Data` – _Required:_ A [SnowflakeNodeData](#aws-glue-api-visual-job-api-SnowflakeNodeData "#aws-glue-api-visual-job-api-SnowflakeNodeData") object.

Specifies the data of the Snowflake target node.

- `Inputs` – An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

## ConnectorDataSource structure

Specifies a source generated with standard connection options.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of this source node.

- `ConnectionType` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The `connectionType`, as provided to the underlying AWS Glue library. This node type supports the following connection types:

    + `opensearch`
    + `azuresql`
    + `azurecosmos`
    + `bigquery`
    + `saphana`
    + `teradata`
    + `vertica`

- `Data` – _Required:_ A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

A map specifying connection options for the node. You can find standard
connection options for the corresponding connection type in the [Connection
parameters](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md") section of the AWS Glue documentation.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for this source.

## ConnectorDataTarget structure

Specifies a target generated with standard connection options.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of this target node.

- `ConnectionType` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The `connectionType`, as provided to the underlying AWS Glue library. This node type supports the following connection types:

    + `opensearch`
    + `azuresql`
    + `azurecosmos`
    + `bigquery`
    + `saphana`
    + `teradata`
    + `vertica`

- `Data` – _Required:_ A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

A map specifying connection options for the node. You can find standard
connection options for the corresponding connection type in the [Connection
parameters](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md") section of the AWS Glue documentation.

- `Inputs` – An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

## RecipeStep structure

A recipe step used in a AWS Glue Studio data preparation recipe
node.

###### Fields

- `Action` – _Required:_ A [RecipeAction](#aws-glue-api-visual-job-api-RecipeAction "#aws-glue-api-visual-job-api-RecipeAction") object.

The transformation action of the recipe step.

- `ConditionExpressions` – An array of [ConditionExpression](#aws-glue-api-visual-job-api-ConditionExpression "#aws-glue-api-visual-job-api-ConditionExpression") objects.

The condition expressions for the recipe step.

## RecipeAction structure

Actions defined in the AWS Glue Studio data preparation recipe
node.

###### Fields

- `Operation` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #56](aws-glue-api-common.md#regex_56 "aws-glue-api-common.md#regex_56").

The operation of the recipe action.

- `Parameters` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #57](aws-glue-api-common.md#regex_57 "aws-glue-api-common.md#regex_57").

Each value is a UTF-8 string, not less than 1 or more than 32768 bytes long.

The parameters of the recipe action.

## ConditionExpression structure

Condition expression defined in the AWS Glue Studio data preparation
recipe node.

###### Fields

- `Condition` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #56](aws-glue-api-common.md#regex_56 "aws-glue-api-common.md#regex_56").

The condition of the condition expression.

- `Value` – UTF-8 string, not more than 1024 bytes long.

The value of the condition expression.

- `TargetColumn` – _Required:_ UTF-8 string, not less than 1 or more than 1024 bytes long.

The target column of the condition expressions.

## S3CatalogIcebergSource structure

Specifies an Apache Iceberg data source that is registered in the AWS Glue Data Catalog. The Iceberg data source must be stored in Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Iceberg data source.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

- `AdditionalIcebergOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options for the Iceberg data source.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the Iceberg source.

## CatalogIcebergSource structure

Specifies an Apache Iceberg data source that is registered in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Iceberg data source.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to read from.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to read from.

- `AdditionalIcebergOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options for the Iceberg data source.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the Iceberg source.

## S3IcebergCatalogTarget structure

Specifies an Apache Iceberg catalog target that writes data to Amazon S3 and registers the table in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the Iceberg catalog target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The input connection for the Iceberg catalog target.

- `PartitionKeys` – An array of UTF-8 strings.

A list of partition keys for the Iceberg table.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table to write to in the catalog.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to write to.

- `AdditionalOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options for the Iceberg catalog target.

- `SchemaChangePolicy` – A [CatalogSchemaChangePolicy](#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy "#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy") object.

The policy for handling schema changes in the catalog target.

- `AutoDataQuality` – An [AutoDataQuality](#aws-glue-api-visual-job-api-AutoDataQuality "#aws-glue-api-visual-job-api-AutoDataQuality") object.

Specifies whether to automatically enable data quality evaluation for
the S3 Iceberg catalog target. When set to `true`, data quality checks
are performed automatically during the write operation.

## DynamoDBELTConnectorSource structure

Specifies a DynamoDB ELT connector source for extracting data from DynamoDB
tables.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the DynamoDB ELT connector source.

- `ConnectionOptions` – A [DDBELTConnectionOptions](#aws-glue-api-visual-job-api-DDBELTConnectionOptions "#aws-glue-api-visual-job-api-DDBELTConnectionOptions") object.

The connection options for the DynamoDB ELT connector source.

- `OutputSchemas` – An array of [GlueSchema](#aws-glue-api-visual-job-api-GlueSchema "#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the DynamoDB ELT connector source.

## DDBELTConnectionOptions structure

Specifies connection options for DynamoDB ELT (Extract, Load, Transform)
operations. This structure contains configuration parameters for connecting
to and extracting data from DynamoDB tables using the ELT connector.

###### Fields

- `DynamodbExport` – UTF-8 string (valid values: `ddb` | `s3`).

Specifies the export type for DynamoDB data extraction. This parameter
determines how data is exported from the DynamoDB table during the ELT process.

- `DynamodbUnnestDDBJson` – Boolean.

A boolean value that specifies whether to unnest DynamoDB JSON format
during data extraction. When set to `true`, the connector will flatten
nested JSON structures from DynamoDB items. When set to `false`,
the original DynamoDB JSON structure is preserved.

- `DynamodbTableArn` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The Amazon Resource Name (ARN) of the DynamoDB table to extract data from.
This parameter specifies the source table for the ELT operation.

- `DynamodbS3Bucket` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the Amazon S3 bucket used for intermediate storage during the
DynamoDB ELT process. This bucket is used to temporarily store exported DynamoDB
data before it is processed by the ELT job.

- `DynamodbS3Prefix` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The S3 object key prefix for files stored in the intermediate S3 bucket
during the DynamoDB ELT process. This prefix helps organize and identify the
temporary files created during data extraction.

- `DynamodbS3BucketOwner` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The AWS account ID of the owner of the S3 bucket specified
in `DynamodbS3Bucket`. This parameter is required when the S3 bucket
is owned by a different AWS account than the one running the ELT
job, enabling cross-account access to the intermediate storage bucket.

- `DynamodbStsRoleArn` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The Amazon Resource Name (ARN) of the AWS Security Token
Service (STS) role to assume for accessing DynamoDB and S3 resources during the
ELT operation. This role must have the necessary permissions to read from the
DynamoDB table and write to the intermediate S3 bucket.

## DDBELTCatalogAdditionalOptions structure

Specifies additional options for DynamoDB ELT catalog operations.

###### Fields

- `DynamodbExport` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies the DynamoDB export configuration for the ELT operation.

- `DynamodbUnnestDDBJson` – Boolean.

Specifies whether to unnest DynamoDB JSON format. When set to `true`,
nested JSON structures in DynamoDB items are flattened.

## Route structure

Specifies a route node that directs data to different output paths based
on defined filtering conditions.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the route node.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The input connection for the route node.

- `GroupFiltersList` – _Required:_ An array of [GroupFilters](#aws-glue-api-visual-job-api-GroupFilters "#aws-glue-api-visual-job-api-GroupFilters") objects.

A list of group filters that define the routing conditions and criteria
for directing data to different output paths.

## GroupFilters structure

Specifies a group of filters with a logical operator that determines how
the filters are combined to evaluate routing conditions.

###### Fields

- `GroupName` – _Required:_ UTF-8 string, matching the [Custom string pattern #60](aws-glue-api-common.md#regex_60 "aws-glue-api-common.md#regex_60").

The name of the filter group.

- `Filters` – _Required:_ An array of [FilterExpression](#aws-glue-api-visual-job-api-FilterExpression "#aws-glue-api-visual-job-api-FilterExpression") objects.

A list of filter expressions that define the conditions for this group.

- `LogicalOperator` – _Required:_ UTF-8 string (valid values: `AND` | `OR`).

The logical operator used to combine the filters in this group. Determines
whether all filters must match (AND) or any filter can match (OR).

## AutoDataQuality structure

Specifies configuration options for automatic data quality evaluation
in AWS Glue jobs. This structure enables automated data quality checks
and monitoring during ETL operations, helping to ensure data integrity and reliability
without manual intervention.

###### Fields

- `IsEnabled` – Boolean.

Specifies whether automatic data quality evaluation is enabled. When
set to `true`, data quality checks are performed automatically.

- `EvaluationContext` – UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The evaluation context for the automatic data quality checks. This defines
the scope and parameters for the data quality evaluation.
