

# Product and service integrations
<a name="databrew-integrations"></a>

Use this section to know which products and services integrate with DataBrew. 

DataBrew works with the following AWS services for networking, management, and governance:
+ [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-databrew.html)

DataBrew works with the following AWS data lakes and data stores:
+ [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html)
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html)

DataBrew supports the following file formats and extensions for uploading data.


| **Format** | **File extension (optional)** |  **Extensions for compressed files (required)**  | 
| --- | --- | --- | 
| Comma-separated values | `.csv` | `.gz` <br />`.snappy`<br />`.lz4`<br />`.bz2`<br />`.deflate` | 
| Microsoft Excel workbook | `.xlsx` | No compression support | 
| JSON (JSON document and JSON lines) | `.json, .jsonl` | `.gz`<br />`.snappy`<br />`.lz4`<br />`.bz2`<br />`.deflate` | 
| Apache ORC | `.orc` | `.zlib`<br />`.snappy` | 
| Apache Parquet | `.parquet` | `.gz`<br />`.snappy`<br />`.lz4` | 

DataBrew writes output files to Amazon S3, and supports the following file formats and extensions.


| **Format** |  **File extension (uncompressed)**  |  **File extensions (compressed)**  | 
| --- | --- | --- | 
| Comma-separated values | .csv | .csv.snappy, .csv.gz, .csv.lz4, csv.bz2, .csv.deflate, csv.br | 
| Tab-separated values | .csv | .tsv.snappy, .tsv.gz, .tsv.lz4, tsv.bz2, .tsv.deflate, tsv.br | 
| Apache Parquet  | .parquet | .parquet.snappy, .parquet.gz, .parquet.lz4, .parquet.lzo, .parquet.br | 
| AWS Glue Parquet | Not supported | .glue.parquet.snappy | 
| Apache Avro | .avro | .avro.snappy, .avro.gz, .avro.lz4, .avro.bz2, .avro.deflate, .avro.br | 
| Apache ORC | .orc | .orc.snappy, .orc.lzo, .orc.zlib | 
| XML | .xml | .xml.snappy, .xml.gz, .xml.lz4, .xml.bz2, .xml.deflate, .xml.br | 
| JSON (JSON Lines format only) |  .json  | .json.snappy, .json.gz, .json.lz4, json.bz2, .json.deflate, .json.br | 
| Tableau Hyper | Not supported | Not applicable | 