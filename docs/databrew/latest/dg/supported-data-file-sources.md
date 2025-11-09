# Supported file types for data sources

The following file requirements apply to files stored in Amazon S3 and to files that you upload
from a local drive. DataBrew supports the following file formats: comma-separated value
(CSV), Microsoft Excel, JSON, ORC, and Parquet. You can use files with a nonstandard
extension or no extension if the file is of one of the supported types.

If DataBrew is unable to infer the file type, make sure to select the correct file type
yourself (CSV, Excel, JSON, ORC, or Parquet). Compressed CSV, JSON, ORC, and Parquet files are
supported, but CSV and JSON files must include the compression codec as the file
extension. If you are importing a folder, all files in the folder must be of the same
file type.

File formats and supported compression algorithms are shown in the following table.

###### Note

CSV, Excel, and JSON files must be encoded with Unicode (UTF-8).

| **Format**                          | **File extension (optional)** | **Extensions for compressed files (required)**       |
| ----------------------------------- | ----------------------------- | ---------------------------------------------------- |
| Comma-separated values              | `.csv`                        | `.gz`<br>`.snappy`<br>`.lz4`<br>`.bz2`<br>`.deflate` |
| Microsoft Excel workbook            | `.xlsx`                       | No compression support                               |
| JSON (JSON document and JSON lines) | `.json, .jsonl`               | `.gz`<br>`.snappy`<br>`.lz4`<br>`.bz2`<br>`.deflate` |
| Apache ORC                          | `.orc`                        | `.zlib`<br>`.snappy`                                 |
| Apache Parquet                      | `.parquet`                    | `.gz`<br>`.snappy`<br>`.lz4`                         |
