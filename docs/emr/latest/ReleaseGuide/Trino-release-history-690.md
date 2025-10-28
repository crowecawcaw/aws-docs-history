# Amazon EMR 6.9.0 - Trino

release notes

## Amazon EMR 6.9.0 - Trino new features

- To support long running queries, Trino now includes a fault-tolerant execution mechanism. Fault-tolerant execution mitigates query failures by retrying failed queries or their component tasks.

## Amazon EMR 6.9.0 - Trino changes

| Amazon EMR 6.9.0 - Trino changes | Type                                                                                                        | Description                                                                                                                                                                                                                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Upgrade                          | Trino Upgrade to 398                                                                                        |
| Upgrade                          | Support for Hadoop 3.3.3                                                                                    |
| Feature                          | Tardigrade support: Add support for exchange spooling on HDFS and Amazon S3.                                |
| Bug fix                          | When Trino Iceberg is used and Glue catalog is enabled, avoid adding metastore uri in `iceberg.properties.` | ## Amazon EMR 6.9.0 - Trino known issues <br>• For Amazon EMR release 6.9.0, Trino does not work on clusters enabled for Apache Ranger. If you need to use Trino with Ranger, contact [Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). |
