

# Manage topic migration during upgrade

This topic describes how to move topics between Standard brokers and Express brokers during the in-place upgrade. You use these operations in Controlled mode to move topics at your own pace. In either mode, you also use them to stop a reassignment or roll back topics before you complete the upgrade.

For more information, see [Initiate the in-place upgrade](msk-upgrade-initiate.md).

**Topics**
+ [Migrate topics individually or in batches](#msk-upgrade-migrate-topics)
+ [Stop a topic reassignment](#msk-upgrade-stop-reassignment)
+ [Roll back a topic to Standard brokers](#msk-upgrade-rollback-topic)
+ [Full rollback to Standard brokers](#msk-upgrade-full-rollback)

## Migrate topics individually or in batches
<a name="msk-upgrade-migrate-topics"></a>

If you initiated the upgrade in Controlled mode (`--topic-reassignment MANUAL`), Amazon MSK adds Express brokers but doesn't move any topics. Wait until the cluster returns to the `ACTIVE` state with both Standard and Express brokers, then use the `StartTopicReassignment` API to move topics individually or in batches.

To migrate a single topic:

```
aws kafka start-topic-reassignment \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --target-instance-type express.m7g.large \
    --topics-to-include "orders"
```

To migrate multiple topics using a regular expression pattern:

```
aws kafka start-topic-reassignment \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --target-instance-type express.m7g.large \
    --topics-to-include "orders.*" "payments.*"
```

To migrate all remaining topics at once:

```
aws kafka start-topic-reassignment \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --target-instance-type express.m7g.large \
    --topics-to-include ".*"
```

**Note**  
`--topics-to-include` accepts up to 100 patterns. Patterns are regular expressions, so a pattern such as `orders.*` can match many topics. To hold specific topics back, use `--topics-to-exclude`. Amazon MSK applies exclude patterns after include patterns, so a topic that matches both stays where it is.

**Note**  
To complete the upgrade, all topics must be on Express brokers, including internal topics. After you finish testing your application topics, also move your internal topics to Express brokers.

We recommend the following approach for topic-by-topic migration:

1. Start with lower-risk topics to validate the migration process and Express broker behavior.

1. Validate application performance on Express for each batch before migrating the next batch.

1. Gradually migrate higher-traffic and business-critical topics.

1. After all application topics are on Express, move your internal topics as well, then perform a final validation before you complete the upgrade.

## Stop a topic reassignment
<a name="msk-upgrade-stop-reassignment"></a>

To stop an in-flight reassignment, use the `StopTopicReassignment` API. Only the partitions in the in-flight batch return to Standard brokers. Topics and partitions that have already moved to Express brokers stay on Express, and topics that haven't moved yet stay on Standard.

```
aws kafka stop-topic-reassignment \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --topic-reassignment-operation-arn {{TopicReassignmentOperationArn}}
```

Only one reassignment can run on a cluster at a time. After you stop a reassignment, wait until `list-topic-reassignments` shows its status as `STOPPED`. Then start a new reassignment with `StartTopicReassignment`. The new reassignment gets its own operation ARN, so use that ARN if you need to stop it later.

## Roll back a topic to Standard brokers
<a name="msk-upgrade-rollback-topic"></a>

If a topic experiences issues after migrating to Express, you can roll it back to Standard brokers while other topics remain on Express. Use `StartTopicReassignment` with `--target-instance-type` set to your Standard broker instance type.

```
aws kafka start-topic-reassignment \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --target-instance-type kafka.m7g.large \
    --topics-to-include "orders\.eu"
```

The affected topic moves back to Standard brokers while the rest remain on Express. After resolving the issue, you can re-migrate the topic to Express when ready.

## Full rollback to Standard brokers
<a name="msk-upgrade-full-rollback"></a>

To move all topics back to Standard brokers:

```
aws kafka start-topic-reassignment \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --target-instance-type kafka.m7g.large \
    --topics-to-include ".*"
```

Once all topics are back on Standard, decommission the Express brokers by calling `UpdateBrokerType` specifying only the Standard broker instance type.

```
aws kafka update-broker-type \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --current-version {{Current-Cluster-Version}} \
    --target-instance-type kafka.m7g.large
```

The cluster returns to its original Standard-only state. You can restart the upgrade later when ready.