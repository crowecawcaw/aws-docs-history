# Migrate from ZooKeeper to KRaft mode

You can migrate an existing ZooKeeper-based MSK cluster to KRaft mode using the
`UpdateClusterKafkaVersion` API. The migration is performed in-place — your
cluster remains available throughout the process and no data is moved. Amazon MSK provisions
KRaft controllers, migrates cluster metadata from ZooKeeper to the KRaft quorum, and
decommissions ZooKeeper nodes automatically.

## Prerequisites

Before migrating your cluster from ZooKeeper to KRaft mode, ensure the following:

- For Standard brokers, the cluster must be deployed across 3 Availability Zones. Express brokers provide this by default.
- Your cluster is running Apache Kafka version `3.9.x` in ZooKeeper mode. If your cluster is on an older version, upgrade to `3.9.x` first using the standard version upgrade process.
- Your cluster is in the `ACTIVE` state with no pending operations.
- If you use tools that rely on direct ZooKeeper access (such as older versions of Cruise Control or custom admin tools), update them to use Kafka Admin APIs instead of direct ZooKeeper connections.
- For Standard (provisioned) clusters: ZooKeeper client access must be disabled. Use the `UpdateConnectivity` API to set `ZookeeperAccess.Enabled=false` before initiating migration. Express clusters do not require this step.
- All client applications use the `--bootstrap-server` connection string, not the `--zookeeper` connection string. The ZooKeeper connection string is not available after migration.
- Your cluster does not have both Public Access and Open Monitoring enabled simultaneously.
- Your cluster does not use `kafka.t3.small` broker instances.
- Your cluster does not use dynamic advertised listeners. To check whether the `advertised.listeners` property has been set dynamically on your brokers, run the following command, where `$bs` is your cluster's bootstrap server connection string, and ensure the output doesn't include `advertised.listeners`:

```
bin/kafka-configs.sh --bootstrap-server $bs --entity-type brokers --describe
```

For more information about dynamically set properties, see [Dynamic Amazon MSK configuration](msk-configuration-properties.md#msk-dynamic-confinguration "msk-configuration-properties.md#msk-dynamic-confinguration").

## What happens during migration

When you initiate a ZooKeeper-to-KRaft migration, Amazon MSK performs the following steps automatically:

1. Amazon MSK provisions KRaft controller nodes in your cluster. These controllers are included at no additional cost.
2. The data plane migration runs: brokers are reconfigured to use the KRaft quorum for metadata while continuing to serve client traffic.
3. After all brokers are registered with the KRaft quorum, Amazon MSK decommissions the ZooKeeper nodes.
4. The cluster management mode is updated to KRaft.

The migration is a long-running operation that can take several hours depending on cluster size. You can monitor the operation status using the `DescribeClusterOperation` API.

###### Important

Migration cannot be reversed. Once the cluster is migrated to KRaft mode, you cannot switch it back to ZooKeeper mode.

## Migrate using the AWS CLI

1. Verify available target versions for your cluster:

```
aws kafka get-compatible-kafka-versions --cluster-arn `ClusterArn`
```

The output includes KRaft target versions (with a `.kraft` suffix) if your cluster is eligible for migration. 2. Start the migration by specifying the KRaft target version:

```
aws kafka update-cluster-kafka-version \
    --cluster-arn `ClusterArn` \
    --current-version `Current-Cluster-Version` \
    --target-kafka-version "3.9.x.kraft"
```

###### Important

Cluster versions aren't simple integers. Use the `DescribeCluster` operation to find the current version of your cluster. 3. Monitor the migration progress:

```
aws kafka describe-cluster-operation --cluster-operation-arn `ClusterOperationArn`
```

The operation state transitions through `UPDATE_IN_PROGRESS` and completes with `UPDATE_COMPLETE`.

## After migration

After the migration completes:

- Your cluster operates in KRaft mode. All metadata is managed by KRaft controllers.
- ZooKeeper nodes are removed. The ZooKeeper connection string is no longer available.
- Client applications continue to work without any changes if they use the `--bootstrap-server` connection string.
- You can view KRaft controller endpoints using the `ListNodes` API if you need them for open monitoring.
