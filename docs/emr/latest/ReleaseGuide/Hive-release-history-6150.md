# Amazon EMR 6.15.0 - Hive

release notes

## Amazon EMR 6.15.0 -

Hive changes

| Type        | Description                                                                                                                                                                                                                                                                                                                       |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feature     | Support for [TEZ-4397](https://issues.apache.org/jira/browse/TEZ-4397 "https://issues.apache.org/jira/browse/TEZ-4397") – For Tez asynchronous<br>split opening, Hive now supports the Tez configs<br>described in [Tez asynchronous split opening](tez-configure.md#tez-configure-async "tez-configure.md#tez-configure-async"). |
| Bug fix     | [HIVE-25400](https://issues.apache.org/jira/browse/HIVE-25400 "https://issues.apache.org/jira/browse/HIVE-25400") – Move the offset<br>updating in `BytesColumnVector` to<br>`setValPreallocated`.                                                                                                                                |
| Bug fix     | [HIVE-25190](https://issues.apache.org/jira/browse/HIVE-25190 "https://issues.apache.org/jira/browse/HIVE-25190") – Fix many small<br>allocations in<br>`BytesColumnVector`.                                                                                                                                                      |
| Bug Fix     | Packaging netty modules with llap server to avoid *NoClassDefFound<br>• exception when<br>starting *LLapDaemon<br>• on worker nodes.                                                                                                                                                                                              |
| Upgrade     | Upgrade Apache Hadoop to 3.3.6.                                                                                                                                                                                                                                                                                                   |
| Upgrade     | [HIVE-26684](https://issues.apache.org/jira/browse/HIVE-26684 "https://issues.apache.org/jira/browse/HIVE-26684") – Upgrade<br>`maven-shade-plugin` to<br>3.4.1.                                                                                                                                                                  |
| Improvement | To reduce Amazon EMR cluster startup time, remove<br>15 seconds of sleep time from the<br>HCatalog startup<br>script.                                                                                                                                                                                                             |
