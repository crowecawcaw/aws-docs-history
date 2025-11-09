# Amazon EMR 6.10.0 - Tez

release notes

## Amazon EMR 6.10.0 -

Tez changes

| Type     | Description                                                                                                                                                                                              |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feature  | Enable<br>`tez.runtime.transfer.data-via-events.enabled`<br>by default                                                                                                                                   |
| Backport | [TEZ-4450](https://issues.apache.org/jira/browse/TEZ-4450 "https://issues.apache.org/jira/browse/TEZ-4450"): Fix shuffle data fetch failure when<br>shuffle data is transferred via data movement events |
| Backport | [TEZ-4460](https://issues.apache.org/jira/browse/TEZ-4460 "https://issues.apache.org/jira/browse/TEZ-4460"): Fix read timeout error in fetching<br>shuffle data from Tez Shuffle Handler                 |
| Backport | [TEZ-4455](https://issues.apache.org/jira/browse/TEZ-4455 "https://issues.apache.org/jira/browse/TEZ-4455"): Add LoggingHandler in ShuffleHandler<br>pipeline for better debuggability                   |
| Bug      | Fix Tez task getting stuck intermittently when preemption<br>of task is enabled                                                                                                                          |

**Amazon EMR 6.10.0 -
Tez known issues**

- **Hive jobs running on Tez** – In clusters with SSL enabled running EMR version 6.9.0, there is a known issue where Hive jobs running on Tez fail with _SSLHandshakeException_. This is related to the
  open-source issue [TEZ-4096](https://issues.apache.org/jira/browse/TEZ-4096 "https://issues.apache.org/jira/browse/TEZ-4096"), which was introduced with the Tez upgrade to version 0.10.2 in EMR 6.9.0. The issue
  requires SSL-related configurations to be passed from the client side (Hive).

**Fix version:** – EMR 6.10.0

**Workaround for version 6.9** – Add the following SSL configuration
to tez-site.xml:

```
<property>
    <name>ssl.client.truststore.location</name>
    <value>{SSL_TRUSTSTORE_LOCATION}</value>
</property>
```

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
