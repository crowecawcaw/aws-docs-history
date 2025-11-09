# Product and service integrations

Use this section to know which products and services integrate with DataBrew.

DataBrew works with the following AWS services for networking, management, and
governance:

- [Amazon CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md "../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md")
- [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")
- [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")
- [AWS Step Functions](../../../step-functions/latest/dg/connect-databrew.md "../../../step-functions/latest/dg/connect-databrew.md")
  DataBrew works with the following AWS data lakes and data stores:

- [AWS Lake Formation](../../../lake-formation/latest/dg/what-is-lake-formation.md "../../../lake-formation/latest/dg/what-is-lake-formation.md")
- [Amazon S3](../../../AmazonS3/latest/dev/Welcome.md "../../../AmazonS3/latest/dev/Welcome.md")
  DataBrew supports the following file formats and extensions for uploading data.

| **Format**                          | **File extension (optional)** | **Extensions for compressed files (required)**       |
| ----------------------------------- | ----------------------------- | ---------------------------------------------------- |
| Comma-separated values              | `.csv`                        | `.gz`<br>`.snappy`<br>`.lz4`<br>`.bz2`<br>`.deflate` |
| Microsoft Excel workbook            | `.xlsx`                       | No compression support                               |
| JSON (JSON document and JSON lines) | `.json, .jsonl`               | `.gz`<br>`.snappy`<br>`.lz4`<br>`.bz2`<br>`.deflate` |
| Apache ORC                          | `.orc`                        | `.zlib`<br>`.snappy`                                 |
| Apache Parquet                      | `.parquet`                    | `.gz`<br>`.snappy`<br>`.lz4`                         |

DataBrew writes output files to Amazon S3, and supports the following file formats and extensions.

| **Format**                    | **File extension (uncompressed)** | **File extensions (compressed)**                                                        |
| ----------------------------- | --------------------------------- | --------------------------------------------------------------------------------------- |
| Comma-separated values        | `.csv`                            | `.csv.snappy`, `.csv.gz`,<br>`.csv.lz4`, `csv.bz2`,<br>`.csv.deflate`, `csv.br`         |
| Tab-separated values          | `.csv`                            | `.tsv.snappy`, `.tsv.gz`,<br>`.tsv.lz4`, `tsv.bz2`,<br>`.tsv.deflate`, `tsv.br`         |
| Apache Parquet                | `.parquet`                        | `.parquet.snappy`, `.parquet.gz`,<br>`.parquet.lz4`, `.parquet.lzo`,<br>`.parquet.br`   |
| AWS Glue Parquet              | Not supported                     | `.glue.parquet.snappy`                                                                  |
| Apache Avro                   | `.avro`                           | `.avro.snappy`, `.avro.gz`,<br>`.avro.lz4`, `.avro.bz2`,<br>`.avro.deflate`, `.avro.br` |
| Apache ORC                    | `.orc`                            | `.orc.snappy`, `.orc.lzo`,<br>`.orc.zlib`                                               |
| XML                           | `.xml`                            | `.xml.snappy`, `.xml.gz`,<br>`.xml.lz4`, `.xml.bz2`,<br>`.xml.deflate`, `.xml.br`       |
| JSON (JSON Lines format only) | `.json`                           | `.json.snappy`, `.json.gz`,<br>`.json.lz4`, `json.bz2`,<br>`.json.deflate`, `.json.br`  |
| Tableau Hyper                 | Not supported                     | Not applicable                                                                          |
