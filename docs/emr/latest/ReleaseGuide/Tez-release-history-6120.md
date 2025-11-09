# Amazon EMR 6.12.0 - Tez

release notes

## Amazon EMR 6.12.0 -

Tez changes

| Type        | Description                                                                                                                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Improvement | Added Support For JDK 11 and JDK 17 Runtime                                                                                                                                                                            |
| Bug Fix     | [TEZ-4492](https://issues.apache.org/jira/browse/TEZ-4492 "https://issues.apache.org/jira/browse/TEZ-4492"): Update Bowerrc to use bower.herokuapp<br>mirror to avoid Bower Registry CERT_EXPIRE issue<br>(BOWER-2608) |
| Upgrade     | Upgraded Surefire to 3.0.0-M7                                                                                                                                                                                          |

**Amazon EMR 6.12.0 -
Tez known issues**

- **Pig jobs running on Tez** – In clusters with SSL enabled running EMR version 6.9.0 to 7.0.0, there is a known issue where Pig jobs running on Tez fail with _SSLHandshakeException_. This is related to the
  open-source issue [TEZ-4096](https://issues.apache.org/jira/browse/TEZ-4096 "https://issues.apache.org/jira/browse/TEZ-4096"), which was introduced with the Tez upgrade to version 0.10.2 in EMR 6.9.0. The issue
  requires SSL-related configurations to be passed from the client side (Pig).

**Fix version:** – EMR 7.1.0

**Workaround** – Add the following SSL configuration
to tez-site.xml:

```
<property>
    <name>ssl.client.truststore.location</name>
    <value>{SSL_TRUSTSTORE_LOCATION}</value>
</property>
```

- **Tez DAG cleanup issue (EMR 6.11.0 - EMR 7.2.0)** – In clusters with SSL enabled running EMR versions 6.11.0 to 7.2.0, there is a known issue
  where _SSLHandshakeException_ occurs in TEZ Application Master (AM) during the DAG cleanup phase. This happens when attempting to delete intermediate shuffle data from remote
  nodes over HTTPS after query completion, not during the query execution. The issue occurs because Tez AM cannot read the relevant **trustStore** configuration when calling the shuffle handler
  service endpoint. However this affects only the cleaning up of shuffle data during DAG cleanup, the application(AM) level cleanup happens anyways and cleans up any lingering shuffle data. So this doesn’t lead to shuffle
  data accumulation.

**Fix version:** – EMR 7.3.0

**Workaround** – Add the following SSL configuration
to tez-site.xml:

```
<property>
    <name>ssl.client.truststore.location</name>
    <value>{SSL_TRUSTSTORE_LOCATION}</value>
</property>
```
