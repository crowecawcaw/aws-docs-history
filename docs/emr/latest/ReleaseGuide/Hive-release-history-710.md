# Amazon EMR 7.1.0 - Hive

release notes

## Amazon EMR 7.1.0 -

Hive changes

| Type    | Description                                                                                                                                                                                                               |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bug Fix | [HIVE-24381](https://issues.apache.org/jira/browse/HIVE-24381 "https://issues.apache.org/jira/browse/HIVE-24381") – Compressed text input returns 0 rows<br>if skip header/footer is included.                            |
| Bug Fix | [HIVE-24190](https://issues.apache.org/jira/browse/HIVE-24190 "https://issues.apache.org/jira/browse/HIVE-24190") –<br>LLAP: ShuffleHandler might return DISK_ERROR_EXCEPTION according to TEZ-4233.                      |
| Bug Fix | [HIVE-23073](https://issues.apache.org/jira/browse/HIVE-23073 "https://issues.apache.org/jira/browse/HIVE-23073") –<br>Shade Netty.                                                                                       |
| Bug Fix | [HIVE-23073](https://issues.apache.org/jira/browse/HIVE-23073 "https://issues.apache.org/jira/browse/HIVE-23073") –<br>Shade Netty and upgrade to netty 4.1.48.Final.                                                     |
| Bug Fix | [HIVE-23148](https://issues.apache.org/jira/browse/HIVE-23148 "https://issues.apache.org/jira/browse/HIVE-23148") –<br>Llap external client flow is broken due to netty shading.                                          |
| Bug Fix | [HIVE-25180](https://issues.apache.org/jira/browse/HIVE-25180 "https://issues.apache.org/jira/browse/HIVE-25180") –<br>Upgrades Netty.                                                                                    |
| Bug Fix | [HIVE-24524](https://issues.apache.org/jira/browse/HIVE-24524 "https://issues.apache.org/jira/browse/HIVE-24524") –<br>LLAP ShuffleHandler: upgrade to Netty4 and remove Netty3 dependency from hive where it's possible. |
| Bug Fix | [HIVE-28000](https://issues.apache.org/jira/browse/HIVE-28000 "https://issues.apache.org/jira/browse/HIVE-28000") –<br>Hive QL: the"not in" clause gives incorrect results when type coercion cannot take place.          |
| Bug Fix | [HIVE-27993](https://issues.apache.org/jira/browse/HIVE-27993 "https://issues.apache.org/jira/browse/HIVE-27993") –<br>Netty4 ShuffleHandler should use 1 boss thread.                                                    |
| Upgrade | Upgrades Netty to 4.1.100.Final                                                                                                                                                                                           |
| Upgrade | Upgrades Jetty to 9.4.53.v20231009                                                                                                                                                                                        |
| Upgrade | Upgrades Zookeeper to 3.9.1                                                                                                                                                                                               |

## Amazon EMR 7.1.0 - Hive changes

- Amazon EMR 7.1 upgrades Hive to Netty 4.1.100.Final to solve the security vulnerabilities
  in Netty3. Since hive-druid-handler has a dependency on netty3,
  Hive doesn't have the `hive-druid-handler` JAR in Hive's classpath in Amazon EMR 7.1.
  An upcoming Amazon EMR release will include it in Hive's classpath once the Druid handler supports
  4.1.100.Final or later versions of Netty. Reach out to AWS support
  if you need the `hive-druid-handler` JAR in Amazon EMR releases 7.1 or higher.
