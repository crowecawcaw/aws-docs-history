# Use Prometheus metrics

All metrics emitted by Apache Kafka to JMX are accessible using open monitoring
with Prometheus. For information about Apache Kafka metrics, see [Monitoring](https://kafka.apache.org/documentation/#monitoring "https://kafka.apache.org/documentation/#monitoring") in
the Apache Kafka documentation. Along with Apache Kafka metrics, consumer-lag
metrics are also available at port 11001 under the JMX MBean name
`kafka.consumer.group:type=ConsumerLagMetrics`. You can also use the
Prometheus Node Exporter to get CPU and disk metrics for your brokers at port 11002.
