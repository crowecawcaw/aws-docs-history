# Use Hive table compression

The compression options for Hive tables in Athena vary by engine version and file
format.

## Hive compression support in

Athena engine version 3

The following table summarizes the compression format support in Athena engine version 3 for storage
file formats in Apache Hive. Text file format includes TSV, CSV, JSON, and custom SerDes
for text. "Yes" or "No" in a cell apply equally to read and write operations except
where noted. For the purposes of this table, CREATE TABLE, CTAS, and INSERT INTO are
considered write operations. For more information about using ZSTD compression levels in
Athena, see [Use ZSTD compression levels](compression-support-zstd-levels.md "compression-support-zstd-levels.md").

|         | Avro | Ion                            | ORC | Parquet                        | Text file                      |
| ------- | ---- | ------------------------------ | --- | ------------------------------ | ------------------------------ |
| BZIP2   | Yes  | Yes                            | No  | No                             | Yes                            |
| DEFLATE | Yes  | No                             | No  | No                             | No                             |
| GZIP    | No   | Yes                            | No  | Yes                            | Yes                            |
| LZ4     | No   | Yes                            | Yes | Write<br>• No<br>Read<br>• Yes | Yes                            |
| LZO     | No   | Write<br>• No<br>Read<br>• Yes | No  | Write<br>• No<br>Read<br>• Yes | Write<br>• No<br>Read<br>• Yes |
| SNAPPY  | Yes  | Yes                            | Yes | Yes                            | Yes                            |
| ZLIB    | No   | No                             | Yes | No                             | No                             |
| ZSTD    | Yes  | Yes                            | Yes | Yes                            | Yes                            |
| NONE    | Yes  | Yes                            | Yes | Yes                            | Yes                            |
