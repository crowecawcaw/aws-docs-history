# Enable and disable

tiered storage on an existing Amazon MSK topic

These sections cover how to enable and disable tiered storage on a topic that
you've already created. To create a new cluster and topic with tiered storage
enabled, see [Creating a cluster with tiered storage using the AWS Management Console](msk-create-cluster-tiered-storage-console.md "msk-create-cluster-tiered-storage-console.md").

## Enabling tiered storage on

an existing Amazon MSK topic

To enable tiered storage on an existing topic, use the `alter`
command syntax in the following example. When you enable tiered storage on an
already existing topic, you aren't restricted to a certain Apache Kafka client
version.

```
bin/kafka-configs.sh --bootstrap-server $bsrv --alter --entity-type topics --entity-name msk-ts-topic --add-config 'remote.storage.enable=true, local.retention.ms=604800000, retention.ms=15550000000'
```

## Disable tiered storage

on an existing Amazon MSK topic

To disable tiered storage on an existing topic, use the `alter`
command syntax in the same order as when you enable tiered storage.

```
bin/kafka-configs.sh --bootstrap-server $bs --alter --entity-type topics --entity-name MSKTutorialTopic --add-config 'remote.log.msk.disable.policy=Delete, remote.storage.enable=false'
```

###### Note

When you disable tiered storage, you completely delete the topic data in
tiered storage. Apache Kafka retains primary storage data , but it still
applies the primary retention rules based on
`local.retention.ms`. After you disable tiered storage on a
topic, you can't re-enable it. If you want to disable tiered storage on an
existing topic, you aren't restricted to a certain Apache Kafka client
version.
