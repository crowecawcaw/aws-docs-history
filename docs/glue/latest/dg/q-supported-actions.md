# Supported code generation abilities

The following are the combinations of the code generation abilities of Amazon Q data integration.

| Sources and Targets                                                    | Transformation |
| ---------------------------------------------------------------------- | -------------- |
| S3 with the following format types: json, csv, parquet,<br>hudi, delta | Drop           |
| AWS Glue Data Catalog                                                  | Aggregate      |
| Redlake                                                                | DropDuplicates |
| Amazon DynamoDB                                                        | Join           |
| MySQL                                                                  | Filter         |
| Oracle                                                                 | RenameColumns  |
| PostgresSQL                                                            | FillNull       |
| Microsoft SQL Server                                                   | DropNull       |
| Amazon DocumentDB / MongoDB                                            | WithColumns    |
| Snowflake                                                              | SQL Query      |
| Google BigQuery                                                        | Union          |
| Teradata                                                               | Select         |
| Amazon OpenSearch Service                                              |                |
| Vertica                                                                |                |
| SAP HANA                                                               |                |
| Amazon Redshift                                                        |                |
