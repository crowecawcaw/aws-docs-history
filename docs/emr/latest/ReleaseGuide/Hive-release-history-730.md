# Amazon EMR 7.3.0 - Hive

release notes

## Amazon EMR 7.3.0 -

Hive changes

| Type        | Description                                                                                                                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Feature     | [HIVE-18728](https://issues.apache.org/jira/browse/HIVE-18728 "https://issues.apache.org/jira/browse/HIVE-18728") – Secure webHCat with SSL.                                                     |
| Improvement | Support configuring SSL keystore credentials for LLAP daemon web UI.                                                                                                                             |
| Improvement | Provide option to control SSL hostname verification for Hive metastore server.                                                                                                                   |
| Bug Fix     | [HIVE-26541](https://issues.apache.org/jira/browse/HIVE-26541 "https://issues.apache.org/jira/browse/HIVE-26541") – NPE when starting WebHCat Service.                                           |
| Bug Fix     | [HIVE-23011](https://issues.apache.org/jira/browse/HIVE-23011 "https://issues.apache.org/jira/browse/HIVE-23011") – Shared work optimizer should check residual predicates when comparing joins. |
| Bug Fix     | Fix **javax.security.sasl.SaslException**: No common protection layer between client and server between HMS and Namenode when In-Transit Encryption is enabled.                                  |
| Bug Fix     | Fix \*_IOException_<br>• where end of orc split overlaps with the start of a block location.                                                                                                     |
| Bug Fix     | Use column name delimiter instead of always splitting by comma when column names contain comma character and using CSVSerde.                                                                     |

### Amazon EMR 7.3.0 -

New configurations

| Classification        | Name                                                            | Default      | Description                                                                                                             |
| --------------------- | --------------------------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| hcatalog-webhcat-site | templeton.use.ssl                                               | false        | Set this to true for using SSL encryption for WebHCat server.                                                           |
| hcatalog-webhcat-site | templeton.keystore.path                                         |              | SSL certificate keystore location for WebHCat server.                                                                   |
| hcatalog-webhcat-site | templeton.keystore.password                                     |              | SSL certificate keystore password for WebHCat server.                                                                   |
| hcatalog-webhcat-site | templeton.ssl.protocol.blacklist                                | SSLv2, SSLv3 | SSL Versions to disable for WebHCat server.                                                                             |
| hcatalog-webhcat-site | templeton.host                                                  | 0.0.0.0      | The host address the WebHCat server will listen on.                                                                     |
| hive-site             | hive.metastore.ssl.enable.hostname.verification                 | false        | Control hostname verification during SSL/TLS handshaking.                                                               |
| hive-site             | hive.llap.daemon.web.ssl.keystore.path                          |              | SSL certificate keystore location for LLAP daemon web UI.                                                               |
| hive-site             | hive.llap.daemon.web.ssl.keystore.password                      |              | SSL certificate keystore password for LLAP daemon web UI.                                                               |
| hive-site             | hive.metastore.hadoop.rpc.protection.override.to.authentication | false        | When enabled, HMS always overrides the value for hadoop.rpc.protection for authentication in its set of configurations. |
