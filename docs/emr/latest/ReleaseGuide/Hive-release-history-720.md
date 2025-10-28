# Amazon EMR 7.2.0 - Hive

release notes

## Amazon EMR 7.2.0 -

Hive changes

| Type           | Description                                                                                                                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------- | --------------------------------------------------------------------------------------- |
| Upgrade        | [Parquet 1.13.1](https://github.com/apache/parquet-java/blob/apache-parquet-1.13.1/CHANGES.md "https://github.com/apache/parquet-java/blob/apache-parquet-1.13.1/CHANGES.md") – Parquet is upgraded to 113.1.                                                      |
| Improvement    | [HIVE-12930](https://issues.apache.org/jira/browse/HIVE-12930 "https://issues.apache.org/jira/browse/HIVE-12930") – Support SSL shuffle for LLAP.                                                                                                                  |
| Improvement    | [HIVE-23062](https://issues.apache.org/jira/browse/HIVE-23062 "https://issues.apache.org/jira/browse/HIVE-23062") – Hive to check Yarn RM URL in TLS and Yarn HA mode for custom Tez queue.                                                                        |
| Bug Fix        | [HIVE-27952](https://issues.apache.org/jira/browse/HIVE-27952 "https://issues.apache.org/jira/browse/HIVE-27952") – Hive fails to create SslContextFactory when KeyStore has multiple certificates.                                                                |
| Bug Fix        | [HIVE-28085](https://issues.apache.org/jira/browse/HIVE-28085 "https://issues.apache.org/jira/browse/HIVE-28085") – YarnQueueHelper fails to access HTTPS enabled YARN WebService.                                                                                 |
| Bug Fix        | [HIVE-26436](https://issues.apache.org/jira/browse/HIVE-26436 "https://issues.apache.org/jira/browse/HIVE-26436") – Hive on MR NullPointerException When initializeOp has not been called and close called. If the operator has not been initialized, skip close.. | ### Amazon EMR 7.2.0 - New configurations |
| Classification | Name                                                                                                                                                                                                                                                               | Default                                   | Description                                                                             |
| ---            | ---                                                                                                                                                                                                                                                                | ---                                       | ---                                                                                     |
| hive-site      | hive.llap.shuffle.ssl.enabled                                                                                                                                                                                                                                      | false                                     | Set to true along with _tez.runtime.shuffle.ssl.enable_ to enable SSL shuffle for LLAP. |
