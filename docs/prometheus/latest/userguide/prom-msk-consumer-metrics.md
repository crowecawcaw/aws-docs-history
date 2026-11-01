

# Consumer-group metrics
<a name="prom-msk-consumer-metrics"></a>

When you collect consumer-group metrics with the example configuration in [Collect Amazon MSK consumer-group metrics](prom-msk-kafka-exporter.md), the Amazon Managed Service for Prometheus collector sends the following metrics. Each metric has the `clusterArn` label from the scrape configuration, so that you can tell clusters apart.


| Metric | Description / Purpose | 
| --- | --- | 
| kafka\_consumergroup\_lag | Difference between the newest offset in a partition and the consumer group's committed offset. This is approximately the number of messages that the group has not committed yet. Labels: `consumergroup`, `topic`, `partition`. | 
| kafka\_consumergroup\_current\_offset | Last offset that the consumer group committed for a partition. Labels: `consumergroup`, `topic`, `partition`. | 
| kafka\_consumergroup\_members | Number of members in the consumer group. Label: `consumergroup`. | 

A value of `-1` for lag or committed offset means that the consumer group has not committed an offset for that partition yet. Leave these values out when you add up lag. For example, the following query shows the total lag of each consumer group for each topic:

```
sum by (clusterArn, consumergroup, topic) (kafka_consumergroup_lag >= 0)
```

This total does not include partitions where the consumer group has not committed an offset.

The exporter calculates lag from the offsets that it reads from your cluster. Its values can differ from the [consumer-lag metrics that Amazon MSK provides](https://docs.aws.amazon.com/msk/latest/developerguide/consumer-lag.html), because each reads offsets at different times.