# Troubleshoot MSK Replicator

The following information can help you troubleshoot problems that you might have
with MSK Replicator. See [Troubleshoot your Amazon MSK cluster](troubleshooting.md "troubleshooting.md") for problem solving information about other Amazon MSK features. You can also post your
issue to [AWS re:Post](https://repost.aws/ "https://repost.aws/").

## MSK Replicator state goes from CREATING to FAILED

Here are some common causes for MSK Replicator creation failure.

1. Verify that the security groups you provided for the Replicator creation in
   the Target cluster section have outbound rules to allow traffic to your target
   cluster's security groups. Also verify that your target cluster's security
   groups have inbound rules that accept traffic from the security groups you
   provide for the Replicator creation in the Target cluster section. See [Choose your
   target cluster](msk-replicator-create-console.md#msk-replicator-create-console-choose-target "msk-replicator-create-console.md#msk-replicator-create-console-choose-target").
2. If you are creating Replicator for cross-region replication, verify that your source cluster has multi-VPC connectivity turned on for IAM Access Control authentication method. See [Amazon MSK multi-VPC private connectivity in a single Region](aws-access-mult-vpc.md "aws-access-mult-vpc.md"). Also verify that the cluster policy is setup on the source cluster so that the MSK Replicator can connect to the source cluster. See [Prepare the Amazon MSK source cluster](msk-replicator-prepare-cluster.md "msk-replicator-prepare-cluster.md").
3. Verify that the IAM role that you provided during MSK Replicator creation has the permissions required to read and write to your source and target clusters. Also, verify that the IAM role has permissions to write to topics. See [Configure replicator settings
   and permissions](msk-replicator-create-console.md#msk-replicator-create-settings "msk-replicator-create-console.md#msk-replicator-create-settings")
4. Verify that your network ACLs are not blocking the connection between the MSK Replicator and your source and target clusters.
5. It's possible that source or target clusters are not fully available when the MSK Replicator tried to connect to them. This might be due to excessive load, disk usage or CPU usage, which causes the Replicator to be unable to connect to the brokers. Fix the issue with the brokers and retry Replicator creation.

After you have performed the validations above, create the MSK Replicator again.

## MSK Replicator appears stuck in the CREATING state

Sometimes MSK Replicator creation can take up to 30 minutes. Wait for 30 minutes and check the state of the Replicator again.

## MSK Replicator is not replicating data or replicating only partial data

Follow these steps to troubleshoot data replication problems.

1. Verify that your Replicator is not running into any authentication errors
   using the AuthError metric provided by MSK Replicator in Amazon CloudWatch. If this metric is
   above 0, check if the policy of the IAM role you provided for the replicator is
   valid and there aren't deny permissions set for the cluster permissions. Based
   on clusterAlias dimension, you can identify if the source or target cluster is
   experiencing authentication errors.
2. Verify that your source and target clusters are not experiencing any issues.
   It is possible that the Replicator is not able to connect to your source or
   target cluster. This might happen due to too many connections, disk at full
   capacity or high CPU usage.
3. Verify that your source and target clusters are reachable from MSK Replicator
   using the KafkaClusterPingSuccessCount metric in Amazon CloudWatch. Based on clusterAlias
   dimension, you can identify if the source or target cluster is experiencing
   auth errors. If this metric is 0 or has no datapoint, the connection is
   unhealthy. You should check network and IAM role permissions that MSK
   Replicator is using to connect to your clusters.
4. Verify that your Replicator is not running into failures due to missing
   topic-level permissions using the ReplicatorFailure metric in Amazon CloudWatch. If this
   metric is above 0, check the IAM role you provided for topic-level
   permissions.
5. Verify that the regular expression you provided in the allow list while
   creating the Replicator matches the names of the topics you want to replicate.
   Also, verify that the topics are not being excluded from replication due to a
   regular expression in the deny list.
6. Note that it may take up to 30 seconds for the Replicator to detect and create the new topics or topic partitions on the target cluster. Any messages produced to the source topic before the topic has been created on the target cluster will not be replicated if replicator starting position is latest (default). Alternatively, you can start replication from the earliest offset in the source cluster topic partitions if you want to replicate existing messages on your topics on the target cluster. See [Configure replicator settings
   and permissions](msk-replicator-create-console.md#msk-replicator-create-settings "msk-replicator-create-console.md#msk-replicator-create-settings").

## Message offsets in the target cluster are different than the source cluster

As part of replicating data, MSK Replicator consumes messages from the source cluster and produces them to the target cluster. This can lead to messages having different offsets on your source and target clusters. However, if you have turned on consumer groups offsets syncing during Replicator creation, MSK Replicator will automatically translate the offsets while copying the metadata so that after failing over to the target cluster, your consumers can resume processing from near where they left off in the source cluster.

## MSK Replicator is not syncing consumer groups offsets or consumer group does not exist on target cluster

Follow these steps to troubleshoot metadata replication problems.

1. Verify that your data replication is working as expected. If not, see [MSK Replicator is not replicating data or replicating only partial data](#msk-replicator-troubleshooting-not-replicating "#msk-replicator-troubleshooting-not-replicating").
2. Verify that the regular expression you provided in the allow list while creating the Replicator matches the names of the consumer groups you want to replicate. Also, verify that the consumer groups are not being excluded from replication due to a regular expression in the deny list.
3. Verify that MSK Replicator has created the topic on the target cluster. It may take up to 30 seconds for the Replicator to detect and create the new topics or topic partitions on the target cluster. Any messages produced to the source topic before the topic has been created on the target cluster will not be replicated if the replicator starting position is _latest_ (default). If your consumer group on the source cluster has only consumed the mesages that have not been replicated by MSK Replicator, the consumer group will not be replicated to the target cluster. After the topic is successfuly created on the target cluster, MSK Replicator will start replicating newly written messages on the source cluster to the target. Once your consumer group starts reading these messages from the source, MSK Replicator will automatically replicate the consumer group to the target cluster. Alternatively, you can start replication from the earliest offset in the source cluster topic partitions if you want to replicate existing messages on your topics on the target cluster. See [Configure replicator settings
   and permissions](msk-replicator-create-console.md#msk-replicator-create-settings "msk-replicator-create-console.md#msk-replicator-create-settings").

###### Note

MSK Replicator optimizes consumer groups offset syncing for your consumers on the source cluster which are reading from a position closer to the end of the topic partition. If your consumer groups are lagging on the source cluster, you may see higher lag for those consumer groups on the target as compared to the source. This means after failover to the target cluster, your consumers will reprocess more duplicate messages. To reduce this lag, your consumers on the source cluster would need to catch up and start consuming from the tip of the stream (end of the topic partition). As your consumers catch up, MSK Replicator will automatically reduce the lag.

## Replication latency is high or keeps increasing

Here are some common causes for high replication latency.

1. Verify that you have the right number of partitions on your source and target MSK clusters.
   Having too few or too many partitions can impact performance. For guidance on
   choosing the number of partitions, see [Best practices for using MSK Replicator](msk-replicator-best-practices.md "msk-replicator-best-practices.md"). The following table shows
   the recommended minimum number of partitions for getting the throughput you want
   with MSK Replicator.

| Throughput and recommended minimum number of partitions | Throughput (MB/s) | Minimum number of partitions required |
| ------------------------------------------------------- | ----------------- | ------------------------------------- |
| 50                                                      | 167               |
| 100                                                     | 334               |
| 250                                                     | 833               |
| 500                                                     | 1666              |
| 1000                                                    | 3333              |

2. Verify that you have enough read and write capacity in your source and target
   MSK clusters to support the replication traffic. MSK Replicator acts as a
   consumer for your source cluster (egress) and as a producer for your target
   cluster (ingress). Therefore, you should provision cluster capacity to support
   the replication traffic in addition to other traffic on your clusters. See [Best practices for using MSK Replicator](msk-replicator-best-practices.md "msk-replicator-best-practices.md") for
   guidance on sizing your MSK clusters.
3. Replication latency might vary for MSK clusters in different source and destination AWS Region pairs, depending on how geographically far apart the clusters are from each other. For example, Replication latency is typically lower when replicating between clusters in the Europe (Ireland) and Europe (London) Regions compared to replication between clusters in the Europe (Ireland) and Asia Pacific (Sydney) Regions.
4. Verify that your Replicator is not getting throttled due to overly aggressive
   quotas set on your source or target clusters. You can use the ThrottleTime
   metric provided by MSK Replicator in Amazon CloudWatch to see the average time in
   milliseconds a request was throttled by brokers on your source/target cluster.
   If this metric is above 0, you should adjust Kafka quotas to reduce throttling
   so that Replicator can catch-up. See [Managing MSK Replicator throughput using Kafka quotas](msk-replicator-best-practices.md#msk-replicator-manage-throughput-kafka-quotas "msk-replicator-best-practices.md#msk-replicator-manage-throughput-kafka-quotas") for
   information on managing Kafka quotas for the Replicator.
5. ReplicationLatency and MessageLag might increase when an AWS Region becomes degraded. Use
   the [AWS Service
   Health Dashboard](https://health.aws.amazon.com/health/status "https://health.aws.amazon.com/health/status") to check for an MSK service event in the Region
   where your primary MSK cluster is located. If there's a service event, you can
   temporarily redirect your application reads and writes to the other
   Region.

## Troubleshooting MSK Replicator failures using ReplicatorFailure metric

The ReplicatorFailure metric helps you monitor and detect replication issues in MSK Replicator. A non-zero value of this metric typically indicates replication failure issue, which might result from the following factors:

- message size limitations
- timestamp range violations
- record batch size problems

If the ReplicatorFailure metric reports a non-zero value, follow these steps to troubleshoot the issue.

###### Note

For more information about this metric, see [MSK Replicator metrics](msk-replicator-monitor.md#msk-replicator-metrics "msk-replicator-monitor.md#msk-replicator-metrics").

1. Configure a client that is able to connect to the target MSK cluster and has Apache Kafka CLI tools setup. For information about setting up the client and Kafka CLI tool, see [Connect to an Amazon MSK Provisioned cluster](client-access.md "client-access.md").
2. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").

Then, do the following:

    1. Obtain the ARNs of MSK Replicator and target MSK cluster.
    2. [Obtain the broker endpoints](get-bootstrap-console.md "get-bootstrap-console.md") of the target MSK cluster. You'll use these endpoints in the following steps.

3. Run the following commands to export the MSK Replicator ARN and broker endpoints you obtained in the previous step.

Make sure that you replace the placeholder values for <`ReplicatorARN`>, <`BootstrapServerString`>, and <`ConsumerConfigFile`> used in the following examples with their actual values.

```
export TARGET_CLUSTER_SERVER_STRING=<`BootstrapServerString`>
```

```
export REPLICATOR_ARN=<`ReplicatorARN`>
```

```
export CONSUMER_CONFIG_FILE=<`ConsumerConfigFile`>
```

4. In your `<`path-to-your-kafka-installation`>/bin` directory, do the following:
   1. Save the following script and name it `query-replicator-failure-message.sh`.

   ```
   #!/bin/bash

   # Script: Query MSK Replicator Failure Message
   # Description: This script queries exceptions from AWS MSK Replicator status topics
   # It takes a replicator ARN and bootstrap server as input and searches for replicator exceptions
   # in the replicator's status topic, formatting and displaying them in a readable manner
   #
   # Required Arguments:
   #   --replicator-arn: The ARN of the AWS MSK Replicator
   #   --bootstrap-server: The Kafka bootstrap server to connect to
   #   --consumer.config: Consumer config properties file
   # Usage Example:
   #   ./query-replicator-failure-message.sh ./query-replicator-failure-message.sh --replicator-arn <replicator-arn> --bootstrap-server <bootstrap-server> --consumer.config <consumer.config>

   print_usage() {
     echo "USAGE: $0 ./query-replicator-failure-message.sh --replicator-arn <replicator-arn> --bootstrap-server <bootstrap-server> --consumer.config <consumer.config>"
     echo "--replicator-arn <String: MSK Replicator ARN>      REQUIRED: The ARN of AWS MSK Replicator."
     echo "--bootstrap-server <String: server to connect to>  REQUIRED: The Kafka server to connect to."
     echo "--consumer.config <String: config file>            REQUIRED: Consumer config properties file."
     exit 1
   }

   # Initialize variables
   replicator_arn=""
   bootstrap_server=""
   consumer_config=""

   # Parse arguments
   while [[ $# -gt 0 ]]; do
     case "$1" in
       --replicator-arn)
         if [ -z "$2" ]; then
           echo "Error: --replicator-arn requires an argument."
           print_usage
         fi
         replicator_arn="$2"; shift 2 ;;
       --bootstrap-server)
         if [ -z "$2" ]; then
           echo "Error: --bootstrap-server requires an argument."
           print_usage
         fi
         bootstrap_server="$2"; shift 2 ;;
       --consumer.config)
         if [ -z "$2" ]; then
           echo "Error: --consumer.config requires an argument."
           print_usage
         fi
         consumer_config="$2"; shift 2 ;;
       *) echo "Unknown option: $1"; print_usage ;;
     esac
   done

   # Check for required arguments
   if [ -z "$replicator_arn" ] || [ -z "$bootstrap_server" ] || [ -z "$consumer_config" ]; then
     echo "Error: --replicator-arn, --bootstrap-server, and --consumer.config are required."
     print_usage
   fi

   # Extract replicator name and suffix from ARN
   replicator_arn_suffix=$(echo "$replicator_arn" | awk -F'/' '{print $NF}')
   replicator_name=$(echo "$replicator_arn" | awk -F'/' '{print $(NF-1)}')
   echo "Replicator name: $replicator_name"

   # List topics and find the status topic
   topics=$(./kafka-topics.sh --command-config client.properties --list --bootstrap-server "$bootstrap_server")
   status_topic_name="__amazon_msk_replicator_status_${replicator_name}_${replicator_arn_suffix}"

   # Check if the status topic exists
   if echo "$topics" | grep -Fq "$status_topic_name"; then
     echo "Found replicator status topic: '$status_topic_name'"
     ./kafka-console-consumer.sh --bootstrap-server "$bootstrap_server" --consumer.config "$consumer_config" --topic "$status_topic_name" --from-beginning | stdbuf -oL grep "Exception" | stdbuf -oL sed -n 's/.*Exception:\(.*\) Topic: \([^,]*\), Partition: \([^\]*\).*/ReplicatorException:\1 Topic: \2, Partition: \3/p'
   else
     echo "No topic matching the pattern '$status_topic_name' found."
   fi
   ```

   2. Run this script to query the MSK Replicator failure messages.

   ```
   <`path-to-your-kafka-installation`>/bin/query-replicator-failure-message.sh --replicator-arn $REPLICATOR_ARN --bootstrap-server $TARGET_CLUSTER_SERVER_STRING --consumer.config $CONSUMER_CONFIG_FILE
   ```

   This script outputs all the errors with their exception messages and affected topic-partitions. You can use this exception information to mitigate the failures as described in [Common MSK Replicator failures and their solutions](#msk-replicator-ReplicatorFailure-error-mitigation "#msk-replicator-ReplicatorFailure-error-mitigation"). Because the topic contains all the historical failure messages, start investigation using the last message. The following is an example of a failure message.

   ```
   ReplicatorException: The request included a message larger than the max message size the server will accept. Topic: test, Partition: 1
   ```

### Common MSK Replicator failures and their solutions

The following list describes some of the MSK Replicator failures that you might experience and how to mitigate them.

**Message size larger than max.request.size**

###### Cause

This failure occurs when the MSK Replicator fails to replicate data because the individual message size exceeds 10 MB. By default, MSK Replicator replicates messages up to 10 MB in size.

The following is an example of this failure message type.

```
ReplicatorException: The message is 20635370 bytes when serialized which is larger than 10485760, which is the value of the max.request.size configuration. Topic: test, Partition: 1
```

###### Solution

Reduce the individual message sizes in your topic. If you're unable to do so, follow these instructions for [requesting a limit increase](limits.md#request-msk-quota-increase "limits.md#request-msk-quota-increase").

**Message size larger than the max message size the server will accept**

###### Cause

This failure occurs when the message size exceeds the target cluster’s maximum message size.

The following is an example of this failure message type.

```
ReplicatorException: The request included a message larger than the max message size the server will accept. Topic: test, Partition: 1
```

###### Solution

Increase the `max.message.bytes` configuration on the target cluster or corresponding target cluster topic. Set the target cluster’s `max.message.bytes` configuration to match your largest uncompressed message size. For information about doing this, see [max.message.bytes](https://kafka.apache.org/documentation/#topicconfigs_max.message.bytes "https://kafka.apache.org/documentation/#topicconfigs_max.message.bytes").

**Timestamp is out of range**

###### Cause

This failure occurs because the individual message timestamp falls outside of the target cluster’s allowed range.

The following is an example of this failure message type.

```
ReplicatorException: Timestamp 1730137653724 of message with offset 0 is out of range. The timestamp should be within [1730137892239, 1731347492239] Topic: test, Partition: 1
```

###### Solution

Update the target cluster’s `message.timestamp.before.max.ms` configuration to allow for messages with older timestamps. For information about doing this, see [message.timestamp.before.max.ms](https://kafka.apache.org/documentation/#topicconfigs_message.timestamp.before.max.ms "https://kafka.apache.org/documentation/#topicconfigs_message.timestamp.before.max.ms").

**Record batch too large**

###### Cause

This failure occurs because the record batch size exceeds the segment size set for the topic on the target cluster. MSK Replicator supports a maximum batch size of 1 MB.

The following is an example of this failure message type.

```
ReplicatorException: The request included message batch larger than the configured segment size on the server. Topic: test, Partition: 1
```

###### Solution

The target cluster’s segment.bytes configuration must be at least as large as the batch size (1 MB) for Replicator to proceed without errors. Update the target cluster’s segment.bytes to be at least 1048576 (1 MB). For information about doing this, see [segment.bytes](https://kafka.apache.org/documentation/#topicconfigs_segment.bytes "https://kafka.apache.org/documentation/#topicconfigs_segment.bytes").

###### Note

If the ReplicatorFailure metric continues to emit non-zero values after applying these solutions, repeat the troubleshooting process until the metric emits a value of zero.
