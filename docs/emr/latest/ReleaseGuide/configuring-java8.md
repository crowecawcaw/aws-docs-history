# Configure applications to use a specific Java

Virtual Machine

Amazon EMR releases have different default Java Virtual Machine (JVM) versions. This page
explains the JVM support for different releases and applications.

## Considerations

For information about the supported Java versions for applications, see the
application pages in the [Amazon EMR Release Guide](emr-release-components.md "emr-release-components.md").

- Amazon EMR only supports running one runtime version in a cluster, and doesn't
  support running different nodes or applications on different runtime
  versions on the same cluster.
- For Amazon EMR 7.x, the default Java Virtual Machine
  (JVM) is Java 17 for applications that support Java 17, with the exception
  of Apache Livy. For more information about the supported JDK versions for
  applications, see the corresponding release page in the
  Amazon EMR Release Guide.
- Starting with Amazon EMR 7.1.0, Flink supports and is set to Java 17 by default. To use a different version Java runtime, override the settings in
  `flink-conf`. For more information about configuring Flink to use Java 8 or Java 11, see
  [Configure Flink to run with Java 11](flink-configure.md#flink-configure-java11 "flink-configure.md#flink-configure-java11").
- For Amazon EMR 5.x and 6.x, the default Java Virtual Machine
  (JVM) is Java 8.
  - For Amazon EMR releases 6.12.0 and higher, some applications also
    support Java 11 and 17.
  - For Amazon EMR releases 6.9.0 and higher, Trino supports Java 17 as
    default. For more information about Java 17 with Trino, see [Trino updates to Java 17](https://trino.io/blog/2022/07/14/trino-updates-to-java-17.html "https://trino.io/blog/2022/07/14/trino-updates-to-java-17.html") on the Trino blog.

Keep in mind the following application-specific considerations when you choose
your runtime version:

| Application-specific Java configuration notes | Application                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Java configuration notes |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| Spark                                         | To run Spark with a non-default Java version, you must<br>configure both Spark and Hadoop. For examples, see [Override the JVM](#configuring-java8-override "#configuring-java8-override").<br>• Configure `JAVA_HOME` in<br>`spark-env` to update the Java runtime of<br>primary instance processes. For example, spark-submit,<br>spark-shell, and Spark History Server.<br>• Modify the Hadoop configuration to update the Java<br>runtime of the Spark executors and the YARN<br>`ApplicationMaster` |
| Spark RAPIDS                                  | You can run RAPIDS with the configured Java version for<br>Spark.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Iceberg                                       | You can run Iceberg with the configured Java version of the<br>application that is using it.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Delta                                         | You can run Delta with the configured Java version of the<br>application that is using it.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Hudi                                          | You can run Hudi with the configured Java version of the<br>application that is using it.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Hadoop                                        | To update the JVM for Hadoop, modify<br>`hadoop-env`. For examples, see [Override the JVM](#configuring-java8-override "#configuring-java8-override").                                                                                                                                                                                                                                                                                                                                                   |
| Hive                                          | To set the Java version to 11 or 17 for Hive, configure the<br>Hadoop JVM setting to the Java version that you want to use.                                                                                                                                                                                                                                                                                                                                                                              |
| HBase                                         | To update the JVM for HBase, modify `hbase-env`.<br>By default, Amazon EMR sets the HBase JVM based on the JVM<br>configuration for Hadoop unless you override the settings in<br>`hbase-env`. For examples, see [Override the JVM](#configuring-java8-override "#configuring-java8-override").                                                                                                                                                                                                          |
| Flink                                         | To update the JVM for Flink, modify<br>`flink-conf`. By default, Amazon EMR sets the Flink JVM<br>based on the JVM configuration for Hadoop unless you override<br>the settings in `flink-conf`. For more information,<br>see [Configure Flink to run with<br>Java 11](flink-configure.md#flink-configure-java11 "flink-configure.md#flink-configure-java11").                                                                                                                                           |
| Oozie                                         | To configure Oozie to run on Java 11 or 17, configure Oozie<br>Server, the Oozie LauncherAM Launcher AM, and change your<br>client-side executable and job configurations. You can also<br>configure `EmbeddedOozieServer` to run on Java 17.<br>For more information, see [Configure Java version for Oozie](oozie-java.md "oozie-java.md").                                                                                                                                                            |
| Pig                                           | Pig only supports Java 8. You can't use Java 11 or 17 with<br>Hadoop and run Pig on the same cluster.                                                                                                                                                                                                                                                                                                                                                                                                    |

## Override the JVM

To override the JVM setting for an Amazon EMR release - for example, to use Java 17
with a cluster that uses Amazon EMR release 6.12.0 - supply the `JAVA_HOME`
setting to its environment classification, which is
``application`-env`for all applications
 except Flink. For Flink, the environment classification is`flink-conf`.
For steps to configure the Java runtime with Flink, see [Configure Flink to run with
Java 11](flink-configure.md#flink-configure-java11 "flink-configure.md#flink-configure-java11").

###### Topics

- [Override the JVM setting with
  Apache Spark](#configuring-java8-override-spark "#configuring-java8-override-spark")
- [Override the JVM setting with
  Apache HBase](#configuring-java8-override-hbase "#configuring-java8-override-hbase")
- [Override the JVM setting
  with Apache Hadoop and Hive](#configuring-java8-override-hadoop "#configuring-java8-override-hadoop")

### Override the JVM setting with

Apache Spark

When you use Spark with Amazon EMR releases 6.12 and higher, you can set the
environment so that the executors use Java 11 or 17. And when you use Spark with
Amazon EMR releases lower than 5.x, and you write a driver for submission in cluster
mode, the driver uses Java 7. However, you can set the environment to ensure
that the executors use Java 8.

To override the JVM for Spark, set the
Spark classification setting. In this sample, the Java version for Hadoop is the same, but that isn't required.

```
[
{
"Classification": "hadoop-env",
        "Configurations": [
            {
"Classification": "export",
                "Configurations": [],
                "Properties": {
"JAVA_HOME": "/usr/lib/jvm/java-1.8.0"
                }
            }
        ],
        "Properties": {}
    },
    {
"Classification": "spark-env",
        "Configurations": [
            {
"Classification": "export",
                "Configurations": [],
                "Properties": {
"JAVA_HOME": "/usr/lib/jvm/java-1.8.0"
                }
            }
        ],
        "Properties": {}
    }
]
```

Note that it's a recommended best practice for Hadoop on Amazon EMR that the JVM version should be consistent
across all Hadoop components.

The following example shows how to add required configuration parameters for EMR 7.0.0+ to ensure consistent Java version usage across all components.

```
[
  {
    "Classification": "spark-defaults",
    "Properties": {
      "spark.executorEnv.JAVA_HOME": "/usr/lib/jvm/java-1.8.0",
      "spark.yarn.appMasterEnv.JAVA_HOME": "/usr/lib/jvm/java-1.8.0"
    }
  },
  {
    "Classification": "hadoop-env",
    "Configurations": [
      {
        "Classification": "export",
        "Configurations": [],
        "Properties": {
          "JAVA_HOME": "/usr/lib/jvm/java-1.8.0"
        }
      }
    ],
    "Properties": {}
  },
  {
    "Classification": "spark-env",
    "Configurations": [
      {
        "Classification": "export",
        "Configurations": [],
        "Properties": {
          "JAVA_HOME": "/usr/lib/jvm/java-1.8.0"
        }
      }
    ],
    "Properties": {}
  }
]
```

### Override the JVM setting with

Apache HBase

To configure HBase to use Java 11, you can set the following configuration
when you launch the cluster.

```
[
    {
        "Classification": "hbase-env",
        "Properties": {},
        "Configurations": [
            {
                "Classification": "export",
                "Properties": {
                    "JAVA_HOME": "/usr/lib/jvm/jre-11",
                    "HBASE_OPTS": "-XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=70 -Dsun.net.inetaddr.ttl=5"
                },
                "Configurations": []
            }
        ]
    }
]
```

### Override the JVM setting

with Apache Hadoop and Hive

The following example shows how to set the JVM to version 17 for Hadoop and
Hive.

```
[
    {
        "Classification": "hadoop-env",
            "Configurations": [
                {
                    "Classification": "export",
                    "Configurations": [],
                    "Properties": {
                        "JAVA_HOME": "/usr/lib/jvm/jre-17"
                    }
                }
        ],
        "Properties": {}
    }
]
```

## Service ports

The following are YARN and HDFS service ports. These settings reflect Hadoop
defaults. Other application services are hosted at default ports unless otherwise
documented. For more information, see the application's project
documentation.

| Port settings for YARN and HDFS                 | Setting                                           | Hostname/Port |
| ----------------------------------------------- | ------------------------------------------------- | ------------- |
| `fs.default.name`                               | default (`hdfs://`emrDeterminedIP`:8020`)         |
| `dfs.datanode.address`                          | default (`0.0.0.0:50010`)                         |
| `dfs.datanode.http.address`                     | default (`0.0.0.0:50075`)                         |
| `dfs.datanode.https.address`                    | default (`0.0.0.0:50475`)                         |
| `dfs.datanode.ipc.address`                      | default (`0.0.0.0:50020`)                         |
| `dfs.http.address`                              | default (`0.0.0.0:50070`)                         |
| `dfs.https.address`                             | default (`0.0.0.0:50470`)                         |
| `dfs.secondary.http.address`                    | default (`0.0.0.0:50090`)                         |
| `yarn.nodemanager.address`                      | default (`${yarn.nodemanager.hostname}:0`)        |
| `yarn.nodemanager.localizer.address`            | default (`${yarn.nodemanager.hostname}:8040`)     |
| `yarn.nodemanager.webapp.address`               | default (`${yarn.nodemanager.hostname}:8042`)     |
| `yarn.resourcemanager.address`                  | default (`${yarn.resourcemanager.hostname}:8032`) |
| `yarn.resourcemanager.admin.address`            | default (`${yarn.resourcemanager.hostname}:8033`) |
| `yarn.resourcemanager.resource-tracker.address` | default (`${yarn.resourcemanager.hostname}:8031`) |
| `yarn.resourcemanager.scheduler.address`        | default (`${yarn.resourcemanager.hostname}:8030`) |
| `yarn.resourcemanager.webapp.address`           | default (`${yarn.resourcemanager.hostname}:8088`) |
| `yarn.web-proxy.address`                        | default (`no-value`)                              |
| `yarn.resourcemanager.hostname`                 | `emrDeterminedIP`                                 |

###### Note

The term `emrDeterminedIP` is an IP address that is
generated by the Amazon EMR control plane. In the newer version, this convention has
been removed, except for the `yarn.resourcemanager.hostname` and
`fs.default.name` settings.

## Application users

Applications run processes as their own user. For example, Hive JVMs run as user
`hive`, MapReduce JVMs run as `mapred`, and so on. This is
demonstrated in the following process status example.

```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
hive      6452  0.2  0.7 853684 218520 ?       Sl   16:32   0:13 /usr/lib/jvm/java-openjdk/bin/java -Xmx256m -Dhive.log.dir=/var/log/hive -Dhive.log.file=hive-metastore.log -Dhive.log.threshold=INFO -Dhadoop.log.dir=/usr/lib/hadoop
hive      6557  0.2  0.6 849508 202396 ?       Sl   16:32   0:09 /usr/lib/jvm/java-openjdk/bin/java -Xmx256m -Dhive.log.dir=/var/log/hive -Dhive.log.file=hive-server2.log -Dhive.log.threshold=INFO -Dhadoop.log.dir=/usr/lib/hadoop/l
hbase     6716  0.1  1.0 1755516 336600 ?      Sl   Jun21   2:20 /usr/lib/jvm/java-openjdk/bin/java -Dproc_master -XX:OnOutOfMemoryError=kill -9 %p -Xmx1024m -ea -XX:+UseConcMarkSweepGC -XX:+CMSIncrementalMode -Dhbase.log.dir=/var/
hbase     6871  0.0  0.7 1672196 237648 ?      Sl   Jun21   0:46 /usr/lib/jvm/java-openjdk/bin/java -Dproc_thrift -XX:OnOutOfMemoryError=kill -9 %p -Xmx1024m -ea -XX:+UseConcMarkSweepGC -XX:+CMSIncrementalMode -Dhbase.log.dir=/var/
hdfs      7491  0.4  1.0 1719476 309820 ?      Sl   16:32   0:22 /usr/lib/jvm/java-openjdk/bin/java -Dproc_namenode -Xmx1000m -Dhadoop.log.dir=/var/log/hadoop-hdfs -Dhadoop.log.file=hadoop-hdfs-namenode-ip-10-71-203-213.log -Dhadoo
yarn      8524  0.1  0.6 1626164 211300 ?      Sl   16:33   0:05 /usr/lib/jvm/java-openjdk/bin/java -Dproc_proxyserver -Xmx1000m -Dhadoop.log.dir=/var/log/hadoop-yarn -Dyarn.log.dir=/var/log/hadoop-yarn -Dhadoop.log.file=yarn-yarn-
yarn      8646  1.0  1.2 1876916 385308 ?      Sl   16:33   0:46 /usr/lib/jvm/java-openjdk/bin/java -Dproc_resourcemanager -Xmx1000m -Dhadoop.log.dir=/var/log/hadoop-yarn -Dyarn.log.dir=/var/log/hadoop-yarn -Dhadoop.log.file=yarn-y
mapred    9265  0.2  0.8 1666628 260484 ?      Sl   16:33   0:12 /usr/lib/jvm/java-openjdk/bin/java -Dproc_historyserver -Xmx1000m -Dhadoop.log.dir=/usr/lib/hadoop/logs -Dhadoop.log.file=hadoop.log -Dhadoop.home.dir=/usr/lib/hadoop
```
