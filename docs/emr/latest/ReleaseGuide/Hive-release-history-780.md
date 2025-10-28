# Amazon EMR 7.8.0 - Hive

release notes

## Amazon EMR 7.8.0 -

Hive changes

| Type    | Description                                                                 |
| ------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bug Fix | Fixes CVE-2024-23953: Apache Hive: Timing Attack Against Signature in LLAP. | **Known issues** <br>• For Hive Insert Over-write queries with Amazon S3 Express One Zone as the output location, set the core-site config: `fs.s3a.directory.operations.purge.uploads` to `false`. |
