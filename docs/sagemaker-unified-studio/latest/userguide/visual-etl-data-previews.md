# Data preview

Data preview help you create and test your visual flow using a sample of your data without having to repeatedly run the flow with the full dataset. By using data preview, you can:

- Make sure that you have access to your data sources or data targets.
- Check that the transform is modifying the data in the intended way. For example, if you use a Filter transform, you can make sure that the filter is selecting the right subset of data.
- Check your data. If your dataset contains columns with values of multiple types, the data preview shows a list of tuples for these columns. Each tuple contains the data type and its value.

## Authoring with Glue data preview

As you author a visual ETL flow, a new Glue interactive session is automatically started and used to preview your data. Learn more on authoring with Glue data previews in AWS Glue [documentation](../../../glue/latest/dg/job-editor-features.md "../../../glue/latest/dg/job-editor-features.md") and Glue [pricing console](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/") page. AWS Glue interactive sessions are billed per second with a 1-minute minimum.

## Authoring with SageMaker data preview

Amazon SageMaker Unified Studio offers a new built-in data preview experience, which doesn't incur Glue interactive sessions resources. You may choose "Data preview v2.0" in your preview panel to use the SageMaker data preview, and turn off "Glue data preview". This new data preview experience is optional.

### Key benefits

SageMaker data preview provides the following advantages:

- Not incurring Glue interactive sessions resources
- Faster time to start and to preview your data

### Limitations

SageMaker data preview has the following support limitations:

#### File format and compression

Not supported file formats:

- ORC and Avro files are currently not supported.

Supported file formats:

- CSV (uncompressed files, must include headers)
- JSON/JSONL (uncompressed files)
- Parquet (uncompressed files, gzip, zstandard, lz4, and Snappy compression)

#### Transforms

The following transforms are not supported:

- FlattenTransform
- PivotRowsTransform
- LookupTransform

#### Data sources

Queries with WHERE clauses are not supported for JDBC connectors (MySQL, PostgreSQL, and SQL Server) and BigQuery connectors.

#### Performance considerations

Large Parquet files are read by reading the first row group. If your parquet file has very large row groups (2GB or larger) you may see performance degradation. Our recommendation for large parquet files is to continue to use Glue data preview.

SageMaker data preview works best with simple primitive data types such as strings, integers, booleans, and binary data. Complex types in Parquet and JSON files (such as struct, map, or array) are supported, but may run into limitations for extremely nested data types. Our recommendation for complex types is to continue to use Glue data preview.
