# Amazon EMR 7.7.0 - Hive

release notes

## Amazon EMR 7.7.0 -

Hive changes

| Type    | Description                                                                                   |
| ------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bug Fix | Fixes CVE-2024-29869: Apache Hive: Credentials file created with non restrictive permissions. |
| Bug Fix | Fixes SemanticException when a row-level filtering policy is enabled in Apache Ran.           |
| Bug Fix | Disable Tez Async Init RR when LLAP or ACID is enabled.                                       | **Known issues** <br>• For Hive Insert Over-write queries with Amazon S3 Express One Zone as the output location, set the core-site config: `fs.s3a.directory.operations.purge.uploads` to `false`. |
