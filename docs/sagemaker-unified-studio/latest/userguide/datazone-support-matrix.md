# Data lineage support matrix

Lineage capture is automated from the following tools in Amazon SageMaker Unified Studio:

| Tools support matrix | **Tool** | **Compute** | **AWS Service**    | **Service deployment<br>option** | **Support status**                               | **Notes** |
| -------------------- | -------- | ----------- | ------------------ | -------------------------------- | ------------------------------------------------ | --------- |
| Jupyterlab notebook  | Spark    | EMR         | EMR Serverless     | Automated                        | Spark DataFrames only; remote workflow execution |
| Jupyterlab notebook  | Spark    | AWS Glue    | N/A                | Automated                        | Spark DataFrames only; remote workflow execution |
| Visual ETL           | Spark    | AWS Glue    | compatibility mode | Automated                        | Spark DataFrames only                            |
| Visual ETL           | Spark    | AWS Glue    | fineGrained mode   | Not supported                    | Spark DataFrames only                            |

Lineage capture is automated from the following sources in SageMaker Unified
Studio:

| Services support matrix    | **Data source**      | **Support status**                        | **Configuration update**                                                                                                                                                                                                                           | **Notes** |
| -------------------------- | -------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| AWS Glue catalog           | Automated by default | Through data source run job configuration | Supported for assets crawled via AWS Glue Crawler for the<br>following data sources: Amazon S3, Amazon DynamoDB, Amazon S3 Open<br>Table Formats including: Delta Lake, Iceberg tables, Hudi tables,<br>JDBC, PostgreSql, DocumentDB, and MongoDB. |
| Amazon Redshift            | Automated by default |                                           |                                                                                                                                                                                                                                                    |
| Amazon Redshift Serverless | Automated by default |                                           |                                                                                                                                                                                                                                                    |
