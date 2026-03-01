# Collect Java Management Extensions (JMX) metrics

You can use the CloudWatch agent to collect Java Management Extensions (JMX) metrics from
your Java applications.

The CloudWatch agent supports collecting these metrics from the following versions:

- JVM 8 and later
- Kafka 0.8.2.x and later
- Tomcat 9, 10.1, and 11 (beta)

Amazon EC2

###### To enable JMX in your JVM instance

For the CloudWatch agent to be able to collect JMX metrics, your application’s JVM
must bind to a port using the `com.sun.management.jmxremote.port`
system property.

```
java -Dcom.sun.management.jmxremote.port=`port-number` -jar `example.jar`
```

For more information and other configurations, see the [JMX documentation](https://docs.oracle.com/en/java/javase/17/management/monitoring-and-management-using-jmx-technology.html "https://docs.oracle.com/en/java/javase/17/management/monitoring-and-management-using-jmx-technology.html").

Amazon EKS

###### To enable JMX on your Java application pods

When using the CloudWatch Observability EKS add-on, you can manage how JMX metrics
are enabled with annotations. For more information, see [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm chart](install-CloudWatch-Observability-EKS-addon.md "install-CloudWatch-Observability-EKS-addon.md"). To enable JMX
metrics collection from a workload, add the following annotations to the workload
manifest file under the `PodTemplate` section:

- `instrumentation.opentelemetry.io/inject-java: "true"`
- One or more of the following:
  - For JVM metrics: `cloudwatch.aws.amazon.com/inject-jmx-jvm:
"true"`
  - For Kafka broker metrics:
    `cloudwatch.aws.amazon.com/inject-jmx-kafka: "true"`
  - For Kafka consumer metrics:
    `cloudwatch.aws.amazon.com/inject-jmx-kafka-consumer:
"true"`
  - For Kafka producer metrics:
    `cloudwatch.aws.amazon.com/inject-jmx-kafka-producer:
"true"`
  - For Tomcat metrics: `cloudwatch.aws.amazon.com/inject-jmx-tomcat:
"true"`

To start collecting JMX metrics, add a `jmx` section inside the
`metrics_collected` section of the CloudWatch agent configuration file. The
`jmx` section can contain the following fields.

- `jvm` – Optional. Specifies that you want to retrieve Java
  Virtual Machine (JVM) metrics from the instance. For more information, see [Collect JVM metrics](#CloudWatch-Agent-JVM-metrics "#CloudWatch-Agent-JVM-metrics").

This section can include the following fields:

    + `measurement` – Specifies the array of JVM metrics to be
     collected. For a list of the possible values to use here, see the
     **Metric** column in the table in [Collect JVM metrics](#CloudWatch-Agent-JVM-metrics "#CloudWatch-Agent-JVM-metrics").


    Within the entry for each individual metric, you can optionally specify one or
     both of the following:




    	- `rename` – Specifies a different name for this
    	 metric.
    	- `unit` – Specifies the unit to use for this metric,
    	 overriding the default unit for the metric. The unit that you specify must be
    	 a valid CloudWatch metric unit, as listed in the `Unit` description in
    	 [MetricDatum](../APIReference/API_MetricDatum.md "../APIReference/API_MetricDatum.md").

- `kafka` – Optional. Specifies that you want to retrieve Apache
  Kafka broker metrics from the instance. For more information, see [Collect Kafka metrics](#CloudWatch-Agent-Kafka-metrics "#CloudWatch-Agent-Kafka-metrics").

This section can include the following fields:

    + `measurement` – Specifies the array of Kafka broker metrics
     to be collected. For a list of the possible values to use here, see the
     **Metric** column in the first table in [Collect Kafka metrics](#CloudWatch-Agent-Kafka-metrics "#CloudWatch-Agent-Kafka-metrics").


    Within the entry for each individual metric, you can optionally specify one or
     both of the following:




    	- `rename` – Specifies a different name for this
    	 metric.
    	- `unit` – Specifies the unit to use for this metric,
    	 overriding the default unit for the metric. The unit that you specify must be
    	 a valid CloudWatch metric unit, as listed in the `Unit` description in
    	 [MetricDatum](../APIReference/API_MetricDatum.md "../APIReference/API_MetricDatum.md").

- `kafka-consumer` – Optional. Specifies that you want to retrieve
  Apache Kafka consumer metrics from the instance. For more information, see [Collect Kafka metrics](#CloudWatch-Agent-Kafka-metrics "#CloudWatch-Agent-Kafka-metrics").

This section can include the following fields:

    + `measurement` – Specifies the array of Kafka broker metrics
     to be collected. For a list of the possible values to use here, see the
     **Metric** column in the second metrics table in [Collect Kafka metrics](#CloudWatch-Agent-Kafka-metrics "#CloudWatch-Agent-Kafka-metrics").


    Within the entry for each individual metric, you can optionally specify one or
     both of the following:




    	- `rename` – Specifies a different name for this
    	 metric.
    	- `unit` – Specifies the unit to use for this metric,
    	 overriding the default unit for the metric. The unit that you specify must be
    	 a valid CloudWatch metric unit, as listed in the `Unit` description in
    	 [MetricDatum](../APIReference/API_MetricDatum.md "../APIReference/API_MetricDatum.md").

- `kafka-producer` – Optional. Specifies that you want to retrieve
  Apache Kafka producer metrics from the instance. For more information, see [Collect Kafka metrics](#CloudWatch-Agent-Kafka-metrics "#CloudWatch-Agent-Kafka-metrics").

This section can include the following fields:

    + `measurement` – Specifies the array of Kafka broker metrics
     to be collected. For a list of the possible values to use here, see the
     **Metric** column in the third metrics table in [Collect Kafka metrics](#CloudWatch-Agent-Kafka-metrics "#CloudWatch-Agent-Kafka-metrics").


    Within the entry for each individual metric, you can optionally specify one or
     both of the following:




    	- `rename` – Specifies a different name for this
    	 metric.
    	- `unit` – Specifies the unit to use for this metric,
    	 overriding the default unit for the metric. The unit that you specify must be
    	 a valid CloudWatch metric unit, as listed in the `Unit` description in
    	 [MetricDatum](../APIReference/API_MetricDatum.md "../APIReference/API_MetricDatum.md").

- `tomcat` – Optional. Specifies that you want to retrieve Tomcat
  metrics from the instance. For more information, see [Collect Tomcat metrics](#CloudWatch-Agent-Tomcat-metrics "#CloudWatch-Agent-Tomcat-metrics").

This section can include the following fields:

    + `measurement` – Specifies the array of Tomcat metrics to be
     collected. For a list of the possible values to use here, see the
     **Metric** column in the table in [Collect Tomcat metrics](#CloudWatch-Agent-Tomcat-metrics "#CloudWatch-Agent-Tomcat-metrics").


    Within the entry for each individual metric, you can optionally specify one or
     both of the following:




    	- `rename` – Specifies a different name for this
    	 metric.
    	- `unit` – Specifies the unit to use for this metric,
    	 overriding the default unit for the metric. The unit that you specify must be
    	 a valid CloudWatch metric unit, as listed in the `Unit` description in
    	 [MetricDatum](../APIReference/API_MetricDatum.md "../APIReference/API_MetricDatum.md").

The `jmx` section can also include the optional
`append_dimensions` field:

- `append_dimensions` – Optional. Additional dimensions to use for
  only the process metrics. If you specify this field, it's used in addition to
  dimensions specified in the `append_dimensions` field that is used for all
  types of metrics collected by the agent.

###### The following fields are for Amazon EC2 only.

- `endpoint` – The address for the JMX client to connect to. The
  format is `ip:port`. If the endpoint is not the localhost, and password
  authentication and SSL must be enabled.
- `metrics_collection_interval` – Optional. Specifies how often to
  collect the processes metrics, overriding the global
  `metrics_collection_interval` specified in the `agent` section
  of the configuration file.

This value is specified in seconds. For example, specifying 10 causes metrics to
be collected every 10 seconds, and setting it to 300 specifies metrics to be collected
every 5 minutes.

If you set this value below 60 seconds, each metric is collected as a
high-resolution metric. For more information, see [High-resolution metrics](publishingMetrics.md#high-resolution-metrics "publishingMetrics.md#high-resolution-metrics").
If JMX was enabled with password authentication or SSL for remote access, you can use
the following fields.

- `password_file` – Optional. Specifies a Java properties file of
  keys to passwords. The file must be read-only and restricted to the user running the
  CloudWatch agent. If password authentication is enabled, this requires the same username and
  password pair as the entry in the JMX password file provided in the
  `com.sun.management.jmxremote.password.file` property. If SSL is enabled,
  it requires entries for `keystore` and `truststore` and
  corresponds to the `javax.net.ssl.keyStorePassword` and
  `javax.net.ssl.trustStorePassword` respectively.
- `username` – If password authentication is enabled, specify the
  username that matches the username in the provided password file.
- `keystore_path` – If SSL is enabled, specify the full path to
  the Java keystore, which consists of a private key and a certificate to the public
  key. Corresponds to the `javax.net.ssl.keyStore` property.
- `keystore_type` – If SSL is enabled, specify the type of
  keystore being used. Corresponds to the `javax.net.ssl.keyStoreType`
  property.
- `truststore_path` – If SSL is enabled, specify the full path to
  the Java truststore, which must contain the remote JMX server's public certificate.
  Corresponds to the `javax.net.ssl.trustStore` property.
- `truststore_type` – If SSL is enabled, specify the type of
  truststore being used. Corresponds to the `javax.net.ssl.trustStoreType`
  property.
- `remote_profile` – Optional. Supported JMX remote profiles are
  TLS in combination with SASL profiles: `SASL/PLAIN`,
  `SASL/DIGEST-MD5`, and `SASL/CRAM-MD5`. Should be one
  of:`SASL/PLAIN`, `SASL/DIGEST-MD5`,
  `SASL/CRAM-MD5`, `TLS SASL/PLAIN`, `TLS
SASL/DIGEST-MD5`, or `TLS SASL/CRAM-MD5`
- `realm` – Optional. The realm as required by the remote profile
  `SASL/DIGEST-MD5`.
- `registry_ssl_enabled` – If RMI registry authentication is
  enabled. Set to true if the JVM was configured with
  `com.sun.management.jmxremote.registry.ssl=true`.
- `insecure` Set to `true` to opt out of the validation
  required if the agent is configured for a non-localhost endpoint.
  The following is an example of the `jmx` section of the CloudWatch agent
  configuration file.

```
{
  "metrics": {
    "metrics_collected": {
      "jmx": [
        {
          "endpoint": "remotehost:1314",
          "jvm": {
            "measurement": [
              "jvm.memory.heap.init",
              "jvm.memory.nonheap.used"
            ]
          },
          "kafka": {
            "measurement": [
              "kafka.request.count",
              {
                "name": "kafka.message.count",
                "rename": "KAFKA_MESSAGE_COUNT",
                "unit": "Count"
              }
            ]
          },
          "username": "cwagent",
          "keystore_path": "/path/to/keystore",
          "keystore_type": "PKCS12",
          "truststore_path": "/path/to/truststore",
          "truststore_type": "PKCS12"
        },
        {
          "endpoint": "localhost:1315",
          "kafka-producer": {
            "measurement": [
              "kafka.producer.request-rate"
            ]
          },
          "append_dimensions": {
            "service.name": "kafka/1"
          }
        }
      ]
    }
  }
}
```

## Collect JVM metrics

You can use the CloudWatch agent to collect Java Virtual Machine (JVM) metrics. To set
this up, add a `jvm` section inside the `jmx`section of the CloudWatch
agent configuration file.

The following metrics can be collected.

| Metric                         | Dimensions        | Description                                                                                                                                                                                    |
| ------------------------------ | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `jvm.classes.loaded`           | [DEFAULT]         | The total number of loaded classes.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                                                     |
| `jvm.gc.collections.count`     | [DEFAULT], `name` | The total number of garbage collections that have occurred.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                             |
| `jvm.gc.collections.elapsed`   | [DEFAULT], `name` | The approximate accumulated garbage collection elapsed time.<br>**Unit:\*<br>• Milliseconds<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                    |
| `jvm.memory.heap.init`         | [DEFAULT]         | The initial amount of memory that the JVM requests from the operating<br>system for the heap.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average          |
| `jvm.memory.heap.max`          | [DEFAULT]         | The maximum amount of memory that can be used for the heap.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Maximum                                                                 |
| `jvm.memory.heap.used`         | [DEFAULT]         | The current heap memory usage.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                                                         |
| `jvm.memory.heap.committed`    | [DEFAULT]         | The amount of memory that is guaranteed to be available for the<br>heap.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                               |
| `jvm.memory.nonheap.init`      | [DEFAULT]         | The initial amount of memory that the JVM requests from the operating<br>system for non-heap purposes.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average |
| `jvm.memory.nonheap.max`       | [DEFAULT]         | The maximum amount of memory that can be used for non-heap<br>purposes.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Maximum                                                     |
| `jvm.memory.nonheap.used`      | [DEFAULT]         | The current non-heap memory usage.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                                                     |
| `jvm.memory.nonheap.committed` | [DEFAULT]         | The amount of memory that is guaranteed to be available for non-heap<br>purposes.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                      |
| `jvm.memory.pool.init`         | [DEFAULT], `name` | The initial amount of memory that the JVM requests from the operating<br>system for the memory pool.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average   |
| `jvm.memory.pool.max`          | [DEFAULT], `name` | The maximum amount of memory that can be used for the memory pool.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Maximum                                                          |
| `jvm.memory.pool.used`         | [DEFAULT], `name` | The current memory pool memory usage.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                                                  |
| `jvm.memory.pool.committed`    | [DEFAULT], `name` | The amount of memory that is guaranteed to be available for the memory<br>pool.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                        |
| `jvm.threads.count`            | [DEFAULT]         | The current number of threads.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                                                          |

The JVM metrics are collected with the following dimensions:

| Dimension | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [DEFAULT] | On Amazon EC2 by default, the host is also published as a dimension of<br>metrics that are collected by the CloudWatch agent, unless you are using the<br>`append_dimensions` field in the `metrics` section.<br>See `omit_hostname` in the agent section of [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md") for more<br>information.<br>On Amazon EKS by default, k8s related context is also published as dimensions<br>of metrics (`k8s.container.name`, `k8s.deployment.name`,<br>`k8s.namespace.name`, `k8s.node.name`,<br>`k8s.pod.name`, and `k8s.replicaset.name`). These can<br>be filtered down using the `aggregation_dimensions` field. |
| `name`    | For `jvm.gc.collections` metrics, the value is the garbage<br>collector name.<br>For `jvm.memory.pool` metrics, the value is the memory pool<br>name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Collect Kafka metrics

You can use the CloudWatch agent to collect Apache Kafka metrics. To set this up, add one
or more of the following subsections inside the `jmx` section of the CloudWatch
agent configuration file.

- Use a `kafka` section to collect Kafka broker metrics.
- Use a `kafka-consumer` section to collect Kafka consumer
  metrics.
- Use a `kafka-producer` section to collect Kafka producer
  metrics.

**Kafka broker metrics**

The following metrics can be collected for Kafka brokers.

| Metric                             | Dimensions             | Description                                                                                                                                                                     |
| ---------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `kafka.message.count`              | [DEFAULT]              | The number of messages received by the Kafka broker.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                     |
| `kafka.request.count`              | [DEFAULT], `type`      | The number of requests received by the Kafka broker.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                     |
| `kafka.request.failed`             | [DEFAULT], `type`      | The number of requests to the Kafka broker that resulted in a<br>failure.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                |
| `kafka.request.time.total`         | [DEFAULT], `type`      | The total time that the Kafka broker has taken to service requests.<br>**Unit:\*<br>• Milliseconds<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average              |
| `kafka.request.time.50p`           | [DEFAULT], `type`      | The 50th percentile time that the Kafka broker has taken to service<br>requests.<br>**Unit:\*<br>• Milliseconds<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average |
| `kafka.request.time.99p`           | [DEFAULT], `type`      | The 99th percentile time that the Kafka broker has taken to service<br>requests.<br>**Unit:\*<br>• Milliseconds<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average |
| `kafka.request.time.avg`           | [DEFAULT], `type`      | The average time that the Kafka broker has taken to service<br>requests.<br>**Unit:\*<br>• Milliseconds<br>**Meaningful statistics:\*<br>• Average                              |
| `kafka.network.io`                 | [DEFAULT], `state`     | The number of bytes received by or sent by the Kafka broker.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                            |
| `kafka.purgatory.size`             | [DEFAULT], `type`      | The number of requests waiting in purgatory.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                             |
| `kafka.partition.count`            | [DEFAULT]              | The number of partitions on the Kafka broker.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                            |
| `kafka.partition.offline`          | [DEFAULT]              | The number of partitions that are offline.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                               |
| `kafka.partition.under_replicated` | [DEFAULT]              | The number of under-replicated partitions.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                               |
| `kafka.isr.operation.count`        | [DEFAULT], `operation` | The number of in-sync replica shrink and expand operations.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                              |
| `kafka.max.lag`                    | [DEFAULT]              | The maximum lag in messages between follower and leader replicas.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Maximum                                             |
| `kafka.controller.active.count`    | [DEFAULT]              | The number of active controllers on the broker.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                          |
| `kafka.leader.election.rate`       | [DEFAULT]              | Leader election rate. If this increases, it indicates broker<br>failures.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                |
| `kafka.unclean.election.rate`      | [DEFAULT]              | Unclean leader election rate. If this increases, it indicates broker<br>failures.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average        |
| `kafka.request.queue`              | [DEFAULT]              | The size of the request queue.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                                           |
| `kafka.logs.flush.time.count`      | [DEFAULT]              | The logs flush count.<br>**Unit:\*<br>• Milliseconds<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                                            |
| `kafka.logs.flush.time.median`     | [DEFAULT]              | The 50th percentile value of the logs flush count.<br>**Unit:\*<br>• Milliseconds<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                               |
| `kafka.logs.flush.time.99p`        | [DEFAULT]              | The 99th percentile value of the logs flush count.<br>**Unit:\*<br>• Milliseconds<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                               |

The Kafka broker metrics are collected with the following dimensions:

| Dimension   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [DEFAULT]   | On Amazon EC2 by default, the host is also published as a dimension of<br>metrics that are collected by the CloudWatch agent, unless you are using the<br>`append_dimensions` field in the `metrics` section.<br>See `omit_hostname` in the agent section of [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md") for more<br>information.<br>On Amazon EKS by default, k8s related context is also published as dimensions<br>of metrics (`k8s.container.name`, `k8s.deployment.name`,<br>`k8s.namespace.name`, `k8s.node.name`,<br>`k8s.pod.name`, and `k8s.replicaset.name`). These can<br>be filtered down using the `aggregation_dimensions` field. |
| `type`      | The request type. Possible values are `produce`,<br>`fetch`, `fetchconsumer`, and<br>`fetchfollower`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `state`     | The direction of network traffic. Possible values are `in`<br>and `out`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `operation` | The operation type for the in-sync replica. Possible values are<br>`shrink` and `expand`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

**Kafka consumer metrics**

The following metrics can be collected for Kafka consumers.

| Metric                                       | Dimensions                      | Description                                                                                                                                               |
| -------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `kafka.consumer.fetch-rate`                  | [DEFAULT], `client-id`          | The number of fetch requests for all topics per second.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average            |
| `kafka.consumer.records-lag-max`             | [DEFAULT], `client-id`          | The number of messages that the consumer lags behind the producer.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average |
| `kafka.consumer.total.bytes-consumed-rate`   | [DEFAULT], `client-id`          | The average number of bytes consumed for all topics per second.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Average                        |
| `kafka.consumer.total.fetch-size-avg`        | [DEFAULT], `client-id`          | The number of bytes fetched per request for all topics.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average           |
| `kafka.consumer.total.records-consumed-rate` | [DEFAULT], `client-id`          | The average number of records consumed for all topics per second.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Average                       |
| `kafka.consumer.bytes-consumed-rate`         | [DEFAULT], `client-id`, `topic` | The average number of bytes consumed per second.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Average                                       |
| `kafka.consumer.fetch-size-avg`              | [DEFAULT], `client-id`, `topic` | The number of bytes fetched per request.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                          |
| `kafka.consumer.records-consumed-rate`       | [DEFAULT], `client-id`, `topic` | The average number of records consumed per second.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Average                                      |

The Kafka consumer metrics are collected with the following dimensions:

| Dimension   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [DEFAULT]   | On Amazon EC2 by default, the host is also published as a dimension of<br>metrics that are collected by the CloudWatch agent, unless you are using the<br>`append_dimensions` field in the `metrics` section.<br>See `omit_hostname` in the agent section of [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md") for more<br>information.<br>On Amazon EKS by default, k8s related context is also published as dimensions<br>of metrics (`k8s.container.name`, `k8s.deployment.name`,<br>`k8s.namespace.name`, `k8s.node.name`,<br>`k8s.pod.name`, and `k8s.replicaset.name`). These can<br>be filtered down using the `aggregation_dimensions` field. |
| `client-id` | The ID of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `topic`     | The Kafka topic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

**Kafka producer metrics**

The following metrics can be collected for Kafka producers.

| Metric                               | Dimensions                      | Description                                                                                                                                                          |
| ------------------------------------ | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `kafka.producer.io-wait-time-ns-avg` | [DEFAULT], `client-id`          | The average length of time the I/O thread spent waiting for a socket ready<br>for reads or writes.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Average |
| `kafka.producer.outgoing-byte-rate`  | [DEFAULT], `client-id`          | The average number of outgoing bytes sent per second to all<br>servers.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Average                           |
| `kafka.producer.request-latency-avg` | [DEFAULT], `client-id`          | The average request latency.<br>**Unit:\*<br>• Milliseconds<br>**Meaningful statistics:\*<br>• Average                                                               |
| `kafka.producer.request-rate`        | [DEFAULT], `client-id`          | The average number of requests sent per second.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Average                                                    |
| `kafka.producer.response-rate`       | [DEFAULT], `client-id`          | The number of responses received per second.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                                  |
| `kafka.producer.byte-rate`           | [DEFAULT], `client-id`, `topic` | The average number of bytes sent per second for a topic.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Average                                          |
| `kafka.producer.compression-rate`    | [DEFAULT], `client-id`, `topic` | The average compression rate of record batches for a topic.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Average                                        |
| `kafka.producer.record-error-rate`   | [DEFAULT], `client-id`, `topic` | The average per-second number of record sends that resulted in errors for<br>a topic.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Average              |
| `kafka.producer.record-retry-rate`   | [DEFAULT], `client-id`, `topic` | The average per-second number of retried record sends for a topic.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Average                                 |
| `kafka.producer.record-send-rate`    | [DEFAULT], `client-id`, `topic` | The average number of records sent per second for a topic.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Average                                         |

Kafka producer metrics are collected with the following dimensions:

| Dimension   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [DEFAULT]   | On Amazon EC2 by default, the host is also published as a dimension of<br>metrics that are collected by the CloudWatch agent, unless you are using the<br>`append_dimensions` field in the `metrics` section.<br>See `omit_hostname` in the agent section of [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md") for more<br>information.<br>On Amazon EKS by default, k8s related context is also published as dimensions<br>of metrics (`k8s.container.name`, `k8s.deployment.name`,<br>`k8s.namespace.name`, `k8s.node.name`,<br>`k8s.pod.name`, and `k8s.replicaset.name`). These can<br>be filtered down using the `aggregation_dimensions` field. |
| `client-id` | The ID of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `topic`     | The Kafka topic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Collect Tomcat metrics

You can use the CloudWatch agent to collect Apache Tomcat metrics. To set this up, add a
`tomcat` section inside the `metrics_collected` section of the
CloudWatch agent configuration file.

The following metrics can be collected.

| Metric                   | Dimensions                                 | Description                                                                                                                    |
| ------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `tomcat.sessions`        | [DEFAULT]                                  | The number of active sessions.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average          |
| `tomcat.errors`          | [DEFAULT], `proto_handler`                 | The number of errors encountered.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average       |
| `tomcat.processing_time` | [DEFAULT], `proto_handler`                 | The total processing time.<br>**Unit:\*<br>• Milliseconds<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average      |
| `tomcat.traffic`         | [DEFAULT], `proto_handler`                 | The number of bytes received and sent.<br>**Unit:\*<br>• Bytes<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average |
| `tomcat.threads`         | [DEFAULT], `proto_handler`                 | The number of threads.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                  |
| `tomcat.max_time`        | [DEFAULT], `proto_handler`,<br>`direction` | Maximum time to process a request.<br>**Unit:\*<br>• Milliseconds<br>**Meaningful statistics:\*<br>• Maximum                   |
| `tomcat.request_count`   | [DEFAULT], `proto_handler`                 | The total requests.<br>**Unit:\*<br>• None<br>**Meaningful statistics:\*<br>• Minimum, Maximum,<br>Average                     |

Tomcat metrics are collected with the following dimensions:

| Dimension       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [DEFAULT]       | On Amazon EC2 by default, the host is also published as a dimension of<br>metrics that are collected by the CloudWatch agent, unless you are using the<br>`append_dimensions` field in the `metrics` section.<br>See `omit_hostname` in the agent section of [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md") for more<br>information.<br>On Amazon EKS by default, k8s related context is also published as dimensions<br>of metrics (`k8s.container.name`, `k8s.deployment.name`,<br>`k8s.namespace.name`, `k8s.node.name`,<br>`k8s.pod.name`, and `k8s.replicaset.name`). These can<br>be filtered down using the `aggregation_dimensions` field. |
| `proto_handler` | The `proto_handler` is an identifier for a connector,<br>which is provided in the `<protocol>-<type>-<port>` format<br>(for example, `http-nio-8080`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `direction`     | The traffic direction. Possible values are `received` and<br>`sent`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
