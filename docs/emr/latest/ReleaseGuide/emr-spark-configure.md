# Configure Spark

You can configure [Spark on Amazon EMR](https://aws.amazon.com/elasticmapreduce/details/spark/ "https://aws.amazon.com/elasticmapreduce/details/spark/") with configuration classifications. For more information
about configuration classifications, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

Configuration classifications for Spark on Amazon EMR include the following:

- `spark` – Sets the
  `maximizeResourceAllocation` property to true or false. When
  true, Amazon EMR automatically configures `spark-defaults` properties
  based on cluster hardware configuration. For more information, see [Using
  maximizeResourceAllocation](#emr-spark-maximizeresourceallocation "#emr-spark-maximizeresourceallocation").
- `spark-defaults` – Sets
  values in the `spark-defaults.conf` file. For more information, see
  [Spark
  configuration](https://spark.apache.org/docs/latest/configuration.html "https://spark.apache.org/docs/latest/configuration.html") in the Spark documentation.
- `spark-env` – Sets values in
  the `spark-env.sh` file. For more information, see [Environment variables](https://spark.apache.org/docs/latest/configuration.html#environment-variables "https://spark.apache.org/docs/latest/configuration.html#environment-variables") in the Spark documentation.
- `spark-hive-site` – Sets
  values in the `hive-site.xml` for Spark.
- `spark-log4j` – (Amazon EMR
  releases 6.7.x and lower) Sets values in the `log4j.properties` file.
  For more information, see the [log4j.properties.template](https://github.com/apache/spark/blob/branch-3.2/conf/log4j.properties.template "https://github.com/apache/spark/blob/branch-3.2/conf/log4j.properties.template") file on Github.
- `spark-log4j2` – (Amazon EMR
  releases 6.8.0 and higher) Sets values in the `log4j2.properties`
  file. For more information, see the [log4j2.properties.template](https://github.com/apache/spark/blob/v3.3.0/conf/log4j2.properties.template "https://github.com/apache/spark/blob/v3.3.0/conf/log4j2.properties.template") file on Github.
- `spark-metrics` – Sets values
  in the `metrics.properties` file. For settings and more information,
  see the [metrics.properties.template](https://github.com/apache/spark/blob/master/conf/metrics.properties.template "https://github.com/apache/spark/blob/master/conf/metrics.properties.template") file on Github, and [Metrics](https://spark.apache.org/docs/latest/monitoring.html#metrics "https://spark.apache.org/docs/latest/monitoring.html#metrics") in Spark documentation.

###### Note

If you're migrating Spark workloads to Amazon EMR from another platform, we recommend
that you test your workloads with the [Spark defaults set by Amazon EMR](#spark-defaults "#spark-defaults") before you add custom configurations. Most
customers see improved performance with our default settings.

###### Topics

- [Spark defaults set by Amazon EMR](#spark-defaults "#spark-defaults")
- [Configuring Spark garbage collection on Amazon EMR
  6.1.0](#spark-gc-config "#spark-gc-config")
- [Using
  maximizeResourceAllocation](#emr-spark-maximizeresourceallocation "#emr-spark-maximizeresourceallocation")
- [Configuring node decommissioning
  behavior](#spark-decommissioning "#spark-decommissioning")
- [Spark ThriftServer environment variable](#spark-thriftserver "#spark-thriftserver")
- [Changing Spark default settings](#spark-change-defaults "#spark-change-defaults")
- [Migrating from Apache Log4j 1.x to Log4j
  2.x](#spark-migrate-logj42 "#spark-migrate-logj42")

## Spark defaults set by Amazon EMR

The following table shows how Amazon EMR sets default values in
`spark-defaults` that affect applications.

| Spark defaults set by Amazon EMR                              | Setting                                                                                                                                                                                                                                                                                                                                         | Description                                                                                                           | Default value |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------- |
| `spark.executor.memory`                                       | The amount of memory to use per executor process. For<br>example: `1g`, `2g`.                                                                                                                                                                                                                                                                   | This setting is determined by the core and task instance types<br>in the cluster.                                     |
| `spark.executor.cores`                                        | The number of cores to use on each executor.                                                                                                                                                                                                                                                                                                    | This setting is determined by the core and task instance<br>types in the cluster.                                     |
| `spark.dynamicAllocation.enabled`                             | When true, use dynamic resource allocation to scale the<br>number of executors registered with an application up and down<br>based on the workload.                                                                                                                                                                                             | `true` (with Amazon EMR 4.4.0 and higher)<br>NoteSpark shuffle service is automatically configured by Amazon EMR<br>. |
| `spark.sql.hive.advancedPartitionPredicatePushdown.enabled`   | When true, advanced partition predicate pushdown into Hive<br>metastore is enabled.                                                                                                                                                                                                                                                             | `true`                                                                                                                |
| `spark.sql.hive.stringLikePartitionPredicatePushdown.enabled` | Pushes down `startsWith`, `contains`,<br>and `endsWith` filters into Hive metastore.<br>NoteGlue doesn't support predicate push down for<br>`startsWith`, `contains`, or<br>`endsWith`. If you are using Glue metastore<br>and you encounter errors due to the predicate pushdown for<br>these functions, set this configuration to<br>`false`. | `true`                                                                                                                |

## Configuring Spark garbage collection on Amazon EMR

6.1.0

Setting custom garbage collection configurations with
`spark.driver.extraJavaOptions` and
`spark.executor.extraJavaOptions` results in driver or executor
launch failure with Amazon EMR 6.1 because of a conflicting garbage collection
configuration with Amazon EMR 6.1.0. For Amazon EMR 6.1.0, the default garbage collection
configuration is set through `spark.driver.defaultJavaOptions` and
`spark.executor.defaultJavaOptions`. This configuration applies only
to Amazon EMR 6.1.0. JVM options not related to garbage collection, such as those for
configuring logging (`-verbose:class`), can still be set through
`extraJavaOptions`. For more information, see [Spark application properties.](https://spark.apache.org/docs/latest/configuration.html#application-properties "https://spark.apache.org/docs/latest/configuration.html#application-properties")

## Using

`maximizeResourceAllocation`

To configure your executors to use the maximum resources possible on each node in
a cluster, set `maximizeResourceAllocation` to `true` in your
`spark` configuration classification. The
`maximizeResourceAllocation` is specific to Amazon EMR . When you enable
`maximizeResourceAllocation`, Amazon EMR calculates the maximum compute
and memory resources available for an executor on an instance in the core instance
group. It then sets the corresponding `spark-defaults` settings based on
the calculated maximum values.

Amazon EMR calculates the maximum compute and memory resources available for
an executor based on an instance type from the core instance fleet. Since each instance fleet
can have different instance types and sizes within a fleet, the executor configuration that
Amazon EMR uses might not be the best for your clusters, so we don't recommend using the default settings when using
maximum resource allocation. Configure custom settings for your instance fleet clusters.

###### Note

You should not use the `maximizeResourceAllocation` option on
clusters with other distributed applications like HBase. Amazon EMR uses custom YARN
configurations for distributed applications, which can conflict with
`maximizeResourceAllocation` and cause Spark applications to
fail.

The following is an example Spark configuration classification with
`maximizeResourceAllocation` set to `true`.

```
[
  {
    "Classification": "spark",
    "Properties": {
      "maximizeResourceAllocation": "true"
    }
  }
]
```

Settings configured in `spark-defaults` when
`maximizeResourceAllocation` is enabled| Setting | Description | Value |
| --- | --- | --- |
| spark.default.parallelism | Default number of partitions in RDDs returned by transformations<br>like join, reduceByKey, and parallelize when not set by<br>user. | 2X number of CPU cores available to YARN containers. |
| spark.driver.memory | Amount of memory to use for the driver process, i.e. where<br>SparkContext is initialized. (for example, 1g, 2g). | Setting is configured based on the instance types in the<br>cluster. However, because the Spark driver application may run<br>on either the primary or one of the core instances (for example,<br>in YARN client and cluster modes, respectively), this is set<br>based on the smaller of the instance types in these two instance<br>groups. |
| spark.executor.memory | Amount of memory to use per executor process. (for example, 1g,<br>2g) | Setting is configured based on the core and task instance<br>types in the cluster. |
| spark.executor.cores | The number of cores to use on each executor. | Setting is configured based on the core and task instance types<br>in the cluster. |
| spark.executor.instances | The number of executors. | Setting is configured based on the core and task instance<br>types in the cluster. Set unless<br>`spark.dynamicAllocation.enabled` explicitly set<br>to true at the same time. |

## Configuring node decommissioning

behavior

With Amazon EMR release 5.9.0 and higher, Spark on Amazon EMR includes a set of features to
help ensure that Spark gracefully handles node termination because of a manual
resize or an automatic scaling policy request. Amazon EMR implements a deny listing
mechanism in Spark that is built on top of the YARN decommissioning mechanism. This
mechanism helps ensure that no new tasks are scheduled on a node that is
decommissioning, while at the same time allowing tasks that are already running to
complete. In addition, there are features to help recover Spark jobs faster if
shuffle blocks are lost when a node terminates. The recomputation process is
triggered sooner and optimized to recompute faster with fewer stage retries, and
jobs can be prevented from failing because of fetch failures that are caused by
missing shuffle blocks.

###### Important

The `spark.decommissioning.timeout.threshold` setting was added in
Amazon EMR release 5.11.0 to improve Spark resiliency when you use Spot instances. In
earlier releases, when a node uses a Spot instance, and the instance is
terminated because of bid price, Spark may not be able to handle the termination
gracefully. Jobs may fail, and shuffle recomputations could take a significant
amount of time. For this reason, we recommend using release 5.11.0 or later if
you use Spot instances.

| Spark node decommissioning settings                    | Setting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description | Default value |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| `spark.blacklist.decommissioning.enabled`              | When set to `true`, Spark deny lists nodes that are in<br>the `decommissioning` state in YARN. Spark does not<br>schedule new tasks on executors running on that node. Tasks already<br>running are allowed to complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `true`      |
| `spark.blacklist.decommissioning.timeout`              | The amount of time that a node in the `decommissioning`<br>state is deny listed. By default, this value is set to one hour,<br>which is also the default for<br>`yarn.resourcemanager.decommissioning.timeout`. To<br>ensure that a node is deny listed for its entire decommissioning<br>period, set this value equal to or greater than<br>`yarn.resourcemanager.decommissioning.timeout`. After<br>the decommissioning timeout expires, the node transitions to a<br>`decommissioned` state, and Amazon EMR can terminate the<br>node's EC2 instance. If any tasks are still running after the<br>timeout expires, they are lost or killed and rescheduled on<br>executors running on other nodes.                                       | `1h`        |
| `spark.decommissioning.timeout.threshold`              | Available in Amazon EMR release 5.11.0 or later. Specified in seconds.<br>When a node transitions to the decommissioning state, if the host<br>will decommission within a time period equal to or less than this<br>value, Amazon EMR not only deny lists the node, but also cleans up the<br>host state (as specified by<br>`spark.resourceManager.cleanupExpiredHost`) without<br>waiting for the node to transition to a decommissioned state. This<br>allows Spark to handle Spot instance terminations better because<br>Spot instances decommission within a 20-second timeout regardless of<br>the value of<br>`yarn.resourcemager.decommissioning.timeout`, which may<br>not provide other nodes enough time to read shuffle files. | `20s`       |
| `spark.resourceManager.cleanupExpiredHost`             | When set to `true`, Spark unregisters all cached data<br>and shuffle blocks that are stored in executors on nodes that are in<br>the `decommissioned` state. This speeds up the recovery<br>process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `true`      |
| `spark.stage.attempt.ignoreOnDecommissionFetchFailure` | When set to `true`, helps prevent Spark from failing<br>stages and eventually failing the job because of too many failed<br>fetches from decommissioned nodes. Failed fetches of shuffle blocks<br>from a node in the `decommissioned` state will not count<br>toward the maximum number of consecutive fetch failures.                                                                                                                                                                                                                                                                                                                                                                                                                     | `true`      |

## Spark ThriftServer environment variable

Spark sets the Hive Thrift Server Port environment variable,
`HIVE_SERVER2_THRIFT_PORT`, to 10001.

## Changing Spark default settings

You change the defaults in `spark-defaults.conf` using the
`spark-defaults` configuration classification or the
`maximizeResourceAllocation` setting in the `spark`
configuration classification.

The following procedures show how to modify settings using the CLI or
console.

###### To create a cluster with spark.executor.memory set to 2g using the

CLI

- Create a cluster with Spark installed and
  `spark.executor.memory` set to 2g, using the following
  command, which references a file, `myConfig.json` stored in
  Amazon S3.

```
aws emr create-cluster --release-label `emr-7.12.0` --applications Name=Spark \
--instance-type m5.xlarge --instance-count 2 --service-role EMR_DefaultRole_V2 --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole --configurations https://s3.amazonaws.com/amzn-s3-demo-bucket/myfolder/myConfig.json
```

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

`myConfig.json`:

```
[
    {
      "Classification": "spark-defaults",
      "Properties": {
        "spark.executor.memory": "2G"
      }
    }
  ]

```

###### To create a cluster with spark.executor.memory set to 2g using the

console

1. Navigate to the new Amazon EMR console and select **Switch to the old console** from the side navigation. For more information on what to expect when you switch to the old console, see [Using the old console](../ManagementGuide/whats-new-in-console.md#console-opt-in "../ManagementGuide/whats-new-in-console.md#console-opt-in").
2. Choose **Create cluster**, **Go to advanced options**.
3. Choose **Spark**.
4. Under **Edit software settings**, leave **Enter
   configuration** selected and enter the following
   configuration:

```
classification=spark-defaults,properties=[spark.executor.memory=2G]
```

5. Select other options, choose and then choose **Create
   cluster**.

###### To set maximizeResourceAllocation

- Create a cluster with Spark installed and
  `maximizeResourceAllocation` set to true using the AWS CLI,
  referencing a file, `myConfig.json`, stored in Amazon S3.

```
aws emr create-cluster --release-label `emr-7.12.0` --applications Name=Spark \
--instance-type m5.xlarge --instance-count 2 --service-role EMR_DefaultRole_V2 --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole --configurations https://s3.amazonaws.com/amzn-s3-demo-bucket/myfolder/myConfig.json
```

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

`myConfig.json`:

```
[
  {
    "Classification": "spark",
    "Properties": {
      "maximizeResourceAllocation": "true"
    }
  }
]
```

###### Note

With Amazon EMR version 5.21.0 and later, you can override cluster configurations and specify additional configuration classifications for each instance group in a running cluster. You do this by using the Amazon EMR console, the AWS Command Line Interface (AWS CLI), or the AWS SDK. For more information, see [Supplying a Configuration for an Instance Group in a Running Cluster](emr-configure-apps-running-cluster.md "emr-configure-apps-running-cluster.md").

## Migrating from Apache Log4j 1.x to Log4j

2.x

[Apache Spark](https://aws.amazon.com/emr/features/spark/ "https://aws.amazon.com/emr/features/spark/") releases 3.2.x and earlier use the legacy Apache Log4j 1.x and
the `log4j.properties` file to configure Log4j in Spark processes. Apache
Spark releases 3.3.0 and later use Apache Log4j 2.x and the
`log4j2.properties` file to configure Log4j in Spark
processes.

If you have configured Apache Spark Log4j using an Amazon EMR release lower than 6.8.0,
then you must remove the legacy `spark-log4j` configuration
classification and migrate to the `spark-log4j2` configuration
classification and key format before you can upgrade to Amazon EMR 6.8.0 or later. The
legacy `spark-log4j` classification causes cluster creation to fail with
a `ValidationException` error in Amazon EMR releases 6.8.0 and
later. You will not be charged for a failure related to the Log4j incompatibility,
but you must remove the defunct `spark-log4j` configuration
classification to continue.

For more information about migrating from Apache Log4j 1.x to Log4j 2.x, see the
[Apache
Log4j Migration Guide](https://logging.apache.org/log4j/2.x/manual/migration.html "https://logging.apache.org/log4j/2.x/manual/migration.html") and the [Spark Log4j 2 Template](https://github.com/apache/spark/blob/master/conf/log4j2.properties.template "https://github.com/apache/spark/blob/master/conf/log4j2.properties.template") on Github.

###### Note

With Amazon EMR , Apache Spark uses a `log4j2.properties` file rather
than the .xml file described in the [Apache
Log4j Migration Guide](https://logging.apache.org/log4j/2.x/manual/migration.html "https://logging.apache.org/log4j/2.x/manual/migration.html"). Also, we do not recommend using the Log4j 1.x
bridge method to convert to Log4j 2.x.
