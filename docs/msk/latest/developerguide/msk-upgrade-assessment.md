

# Upgrade readiness assessment

Before upgrading your Amazon MSK Provisioned cluster from Standard brokers to Express brokers, we recommend running an upgrade readiness assessment. The assessment validates your cluster and topic configurations against Express broker requirements and identifies any issues that must be resolved before the upgrade can proceed. For more information, see [Express broker configurations](msk-configuration-express.md).

**Note**  
Running the assessment beforehand is recommended but not required. When you initiate the upgrade, Amazon MSK automatically re-validates configurations and proceeds only after all checks pass.

**Topics**
+ [Run an upgrade readiness assessment using the AWS Management Console](#msk-upgrade-assessment-console)
+ [Run an upgrade readiness assessment using the AWS CLI](#msk-upgrade-assessment-cli)
+ [Assessment findings](#msk-upgrade-assessment-findings)
+ [Resolve common findings](#msk-upgrade-assessment-resolve-findings)

## Run an upgrade readiness assessment using the AWS Management Console
<a name="msk-upgrade-assessment-console"></a>

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. Choose the MSK cluster you want to assess.

1. On the cluster details page, choose **Assess cluster configuration for Express Upgrade**.

1. The assessment runs in the background and typically completes in about two minutes. The results appear on the cluster details page under the **Assessments** tab.

## Run an upgrade readiness assessment using the AWS CLI
<a name="msk-upgrade-assessment-cli"></a>

Run the following command, replacing the placeholder values with your cluster information.

```
aws kafka create-assessment \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --assessment-type UPDATE_BROKER_TYPE \
    --assessment-parameters TargetInstanceType=express.m7g.large
```

Specify the Express instance type that you plan to upgrade to, for example `express.m7g.large` or `express.m8g.large`.

The command returns an assessment ARN. To check the status of the assessment, run the following command. Wait until `Status` shows `COMPLETE`.

```
aws kafka describe-assessment \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --assessment-arn {{AssessmentArn}}
```

To list detailed findings for a completed assessment, run the following command.

```
aws kafka list-assessment-findings \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --assessment-arn {{AssessmentArn}}
```

## Assessment findings
<a name="msk-upgrade-assessment-findings"></a>

The assessment returns findings at three severity levels. `ERROR` findings are blocking findings. `WARNING` and `INFO` findings are informational.

### Blocking findings
<a name="msk-upgrade-assessment-blocking-findings"></a>

Blocking (`ERROR`) findings must be resolved before you can start the upgrade. The upgrade doesn't start until all blocking findings are resolved.



| Finding | Condition | Required action | 
| --- | --- | --- | 
| Replication factor | Any topic has a replication factor other than 3 | Update the topic to a replication factor of 3 | 
| min.insync.replicas | Any topic has min.insync.replicas other than 2 | Update the topic to min.insync.replicas=2 | 
| segment.ms | Any topic has segment.ms less than 60,000 | Increase the value to at least 60,000 ms | 
| max.compaction.lag.ms | Any topic has max.compaction.lag.ms less than 1 day | Increase the value to at least 1 day | 
| Instance type | The cluster uses kafka.t3.small | Upgrade to a supported broker size (M5, M7g, or M8g) | 
| Availability Zones | The cluster is deployed across two Availability Zones | Create a new cluster with Express brokers across three Availability Zones, and migrate to it using MSK Replicator. | 

### Informational findings
<a name="msk-upgrade-assessment-informational-findings"></a>

Informational (`WARNING` and `INFO`) findings don't block the upgrade. They describe behavior changes on Express brokers to review before you upgrade. For more information, see [Express broker configurations](msk-configuration-express.md).



| Finding | What changes on Express | Guidance | 
| --- | --- | --- | 
| log.segment.bytes | Express manages segment lifecycle internally | Custom values are ignored | 
| segment.bytes (topic-level) | Express manages this internally | Topic-level overrides have no effect | 
| Threading configurations | Express auto-tunes thread pools based on instance type | Custom values are replaced with Express-optimized settings | 
| Service-managed broker configurations | Express manages some broker configurations for you, such as log cleaner (log.cleaner.\*), replica fetcher (replica.fetch.\*), and log roll (log.roll.ms) settings | Custom values for these settings no longer take effect. For the full list, see [Express broker configurations](msk-configuration-express.md). | 
| Per-user and per-client quotas | Express adds broker-level limits on top of customer quotas | Review your quota strategy against Express broker-level limits | 

## Resolve common findings
<a name="msk-upgrade-assessment-resolve-findings"></a>

### Replication factor and min.insync.replicas
<a name="msk-upgrade-assessment-resolve-rf"></a>

Express brokers require all topics to have a replication factor of 3 and `min.insync.replicas` of 2. For any topic whose replication factor isn't 3, first add a third replica by reassigning the topic's partitions. Set `min.insync.replicas` to 2 only after the reassignment is complete. Run the following steps in order.

```
# 1. Write increase-rf.json. For each partition, list its 2 current replicas plus 1 new broker:
{"version":1,"partitions":[{"topic":"{{TopicName}}","partition":0,"replicas":[1,2,3]}]}

# 2. Add the third replica:
bin/kafka-reassign-partitions.sh --bootstrap-server $BS --command-config client.properties \
    --reassignment-json-file increase-rf.json --execute

# 3. Re-run this until every partition shows completed:
bin/kafka-reassign-partitions.sh --bootstrap-server $BS --command-config client.properties \
    --reassignment-json-file increase-rf.json --verify

# 4. Only after step 3 is complete, set min.insync.replicas:
bin/kafka-configs.sh --bootstrap-server $BS --command-config client.properties \
    --entity-type topics --entity-name {{TopicName}} --alter --add-config min.insync.replicas=2
```

For more information, see [Build highly available clusters](bestpractices.md#ensure-high-availability).

### Instance type
<a name="msk-upgrade-assessment-resolve-instance-type"></a>

If your cluster uses `kafka.t3.small` brokers, upgrade to a supported broker size (M5, M7g, or M8g) before you initiate the in-place upgrade. For more information, see [Update the Amazon MSK cluster broker size](msk-update-broker-type.md).

### Apache Kafka version and KRaft
<a name="msk-upgrade-assessment-resolve-kafka-version"></a>

In-place upgrade supports only Standard broker clusters on Apache Kafka version 3.9 with KRaft. If your cluster runs a different version or uses ZooKeeper, first move to version 3.9 with KRaft. For more information, see [Upgrade the Apache Kafka version](version-upgrades.md).