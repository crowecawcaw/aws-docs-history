

# Troubleshoot Amazon MSK Replicator
<a name="msk-replicator-troubleshooting"></a>

The following information can help you troubleshoot problems with MSK Replicator. See [Troubleshoot your Amazon MSK cluster](troubleshooting.md) for other Amazon MSK features. You can also post your issue to [AWS re:Post](https://repost.aws/).

## Replicator state goes from CREATING to FAILED
<a name="msk-replicator-ts-failed-state"></a>

Common causes for MSK Replicator creation failure:

1. Verify that the security groups you provided for the target cluster have outbound rules to allow traffic to your target cluster's security groups, and that your target cluster's security groups have inbound rules that accept traffic from the Replicator security groups.

1. For cross-region replication, verify that your source cluster has multi-VPC connectivity turned on for IAM access control and that the cluster policy is set up on the source cluster.

1. Verify that the IAM role provided during creation has the permissions required to read and write to your source and target clusters, including permissions to write to topics.

1. Verify that your network ACLs are not blocking the connection between the MSK Replicator and your clusters.

1. It is possible that source or target clusters are not fully available when the MSK Replicator tried to connect. This might be due to excessive load, disk usage, or CPU usage. Fix the issue with the brokers and retry Replicator creation.

After you have performed the validations above, create the MSK Replicator again.

## Replicator appears stuck in the CREATING state
<a name="msk-replicator-ts-stuck-creating"></a>

MSK Replicator creation can take up to 30 minutes. Wait for 30 minutes and check the state of the Replicator again.

## Replicator is not replicating data or replicating only partial data
<a name="msk-replicator-ts-not-replicating"></a>

1. Verify that your Replicator is not running into authentication errors using the `AuthError` metric in Amazon CloudWatch. If this metric is above 0, check the IAM role policy and ensure there are no deny permissions set for the cluster permissions.

1. Verify that your source and target clusters are not experiencing issues (too many connections, disk at full capacity, or high CPU usage).

1. Verify that your clusters are reachable using the `KafkaClusterPingSuccessCount` metric. If this metric is 0 or has no datapoint, check network and IAM role permissions.

1. Verify that your Replicator is not running into failures using the `ReplicatorFailure` metric. If above 0, check the IAM role for topic-level permissions.

1. Verify that the regular expression in the allow list matches the names of the topics you want to replicate, and that topics are not being excluded by the deny list.

1. It may take up to 30 seconds for the Replicator to detect and create new topics. Messages produced before the topic is created on the target cluster will not be replicated if the starting position is *latest* (default).

## Message offsets in the target cluster are different than the source cluster
<a name="msk-replicator-ts-offset-mismatch"></a>

MSK Replicator consumes messages from the source cluster and produces them to the target cluster, which can lead to different offsets. If you have turned on consumer group offset syncing, MSK Replicator will automatically translate the offsets so that after failover, your consumers can resume processing from near where they left off.

## Replicator is not syncing consumer group offsets
<a name="msk-replicator-ts-consumer-groups"></a>

1. Verify that data replication is working as expected.

1. Verify that the regular expression in the allow list matches the consumer groups you want to replicate.

1. Verify that MSK Replicator has created the topic on the target cluster. If your consumer group on the source cluster has only consumed messages that have not been replicated, the consumer group will not be replicated to the target cluster. Once your consumer group starts reading newly replicated messages, MSK Replicator will automatically replicate the consumer group.

**Note**  
MSK Replicator optimizes consumer group offset syncing for consumers reading from near the end of the topic partition. If your consumer groups are lagging on the source cluster, you may see higher lag on the target. As your consumers catch up, MSK Replicator will automatically reduce the lag.

## Replication latency is high or keeps increasing
<a name="msk-replicator-ts-high-latency"></a>

1. Verify that you have the right number of partitions. The following table shows the recommended minimum number of partitions for your desired throughput.  
**Throughput and recommended minimum number of partitions**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-troubleshooting.html)

1. Verify that you have enough read and write capacity in your clusters. MSK Replicator acts as a consumer for your source cluster (egress) and as a producer for your target cluster (ingress). Provision cluster capacity to support replication traffic in addition to other traffic.

1. Replication latency varies by Region pair distance.

1. Verify that your Replicator is not getting throttled using the `ThrottleTime` metric. If above 0, adjust Kafka quotas. See [Managing throughput with Kafka quotas](msk-replicator-bp-quotas.md).

1. Check the [AWS Service Health Dashboard](https://health.aws.amazon.com/health/status) for MSK service events in your Region.

## Troubleshooting using the ReplicatorFailure metric
<a name="msk-replicator-ts-replicator-failure"></a>

The `ReplicatorFailure` metric helps you monitor and detect replication issues. A non-zero value typically indicates a replication failure caused by message size limitations, timestamp range violations, or record batch size problems. If you have log delivery configured for your replicator, you can use the delivered log messages to identify the specific failure. For more details, see [MSK Replicator logs](msk-replicator-logs.md). If log delivery is not configured, follow the steps below to query the replicator's status topic for error messages.

If the `ReplicatorFailure` metric reports a non-zero value, follow these steps to troubleshoot:

1. Configure a client that can connect to the target MSK cluster and has Apache Kafka CLI tools set up. See [Connect to an Amazon MSK Provisioned cluster](client-access.md).

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

   Obtain the ARNs of the MSK Replicator and target MSK cluster, and [obtain the broker endpoints](get-bootstrap-console.md) of the target MSK cluster.

1. Export the MSK Replicator ARN and broker endpoints:

   ```
   export TARGET_CLUSTER_SERVER_STRING=<BootstrapServerString>
   export REPLICATOR_ARN=<ReplicatorARN>
   export CONSUMER_CONFIG_FILE=<ConsumerConfigFile>
   ```

1. In your `<path-to-your-kafka-installation>/bin` directory, save the following script as **query-replicator-failure-message.sh**.

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
   #   ./query-replicator-failure-message.sh --replicator-arn <replicator-arn> --bootstrap-server <bootstrap-server> --consumer.config <consumer.config>
   
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

   Run this script to query the MSK Replicator failure messages:

   ```
   <path-to-your-kafka-installation>/bin/query-replicator-failure-message.sh --replicator-arn $REPLICATOR_ARN --bootstrap-server $TARGET_CLUSTER_SERVER_STRING --consumer.config $CONSUMER_CONFIG_FILE
   ```

   This script outputs all the errors with their exception messages and affected topic-partitions. Because the topic contains all the historical failure messages, start investigation using the last message. The following is an example of a failure message:

   ```
   ReplicatorException: The request included a message larger than the max message size the server will accept. Topic: test, Partition: 1
   ```

**Common failures and solutions**  
The following describes common MSK Replicator failures and how to mitigate them.

**Message size larger than max.request.size**  
*Cause:* The individual message size exceeds 10 MB (the default maximum).  
The following is an example of this failure message type.  

```
ReplicatorException: The message is 20635370 bytes when serialized which is larger than 10485760, which is the value of the max.request.size configuration. Topic: test, Partition: 1
```
*Solution:* Reduce the individual message sizes in your topic. If you cannot, follow the instructions for [requesting a limit increase](limits.md#request-msk-quota-increase).

**Message size larger than the max message size the server will accept**  
*Cause:* The message size exceeds the target cluster's maximum message size.  
The following is an example of this failure message type.  

```
ReplicatorException: The request included a message larger than the max message size the server will accept. Topic: test, Partition: 1
```
*Solution:* Increase the `max.message.bytes` configuration on the target cluster or topic. See [max.message.bytes](https://kafka.apache.org/documentation/#topicconfigs_max.message.bytes).

**Timestamp is out of range**  
*Cause:* The message timestamp falls outside the target cluster's allowed range.  
The following is an example of this failure message type.  

```
ReplicatorException: Timestamp 1730137653724 of message with offset 0 is out of range. The timestamp should be within [1730137892239, 1731347492239] Topic: test, Partition: 1
```
*Solution:* Update the target cluster's `message.timestamp.before.max.ms` configuration. See [message.timestamp.before.max.ms](https://kafka.apache.org/documentation/#topicconfigs_message.timestamp.before.max.ms).

**Record batch too large**  
*Cause:* The record batch size exceeds the segment size set for the topic on the target cluster. MSK Replicator supports a maximum batch size of 1 MB.  
The following is an example of this failure message type.  

```
ReplicatorException: The request included message batch larger than the configured segment size on the server. Topic: test, Partition: 1
```
*Solution:* Update the target cluster's `segment.bytes` to be at least 1048576 (1 MB). See [segment.bytes](https://kafka.apache.org/documentation/#topicconfigs_segment.bytes).

**Note**  
If the `ReplicatorFailure` metric continues to emit non-zero values after applying these solutions, repeat the troubleshooting process until the metric emits a value of zero.

## Troubleshoot replication from self-managed Kafka clusters
<a name="msk-replicator-ts-external"></a>

### MSK Replicator cannot connect to self-managed Kafka cluster
<a name="msk-replicator-ts-external-connect"></a>

Perform the following checks if MSK Replicator cannot connect to your self-managed Kafka cluster:

1. Verify that your VPN or Direct Connect connection is active and the route tables are correct.

1. Verify that security groups allow inbound traffic from MSK Replicator subnets on the SASL\_SSL port (typically 9096).

1. Verify DNS resolution from the VPC to the self-managed cluster broker hostnames.

1. Check the `KafkaClusterPingSuccessCount` metric in Amazon CloudWatch — a value of 0 indicates a connectivity failure.

### SASL/SCRAM or mTLS authentication failures
<a name="msk-replicator-ts-external-sasl"></a>

If the `AuthError` metric is non-zero or the Replicator logs show SASL/SCRAM or mTLS errors:

1. Verify that the credentials stored in AWS Secrets Manager match the SCRAM user credentials on the self-managed cluster (for SASL/SCRAM) or that the client certificate and private key are correct (for mTLS).

1. Verify that the SCRAM user or certificate principal has the required ACL permissions (Read, Describe on topics; Read, Describe on consumer groups; Describe on cluster).

1. Check the `AuthError` metric to confirm authentication errors and identify whether the source or target cluster is affected using the `ClusterAlias` dimension.

### SASL/OAUTHBEARER (OAuth) authentication failures
<a name="msk-replicator-ts-external-oauth"></a>

If the `AuthError` metric is non-zero or the Replicator logs show access token retrieval or SASL/OAUTHBEARER errors:

1. Verify that the `tokenEndpointUrl` is correct, uses the HTTPS scheme, and is reachable from the VPC subnets you provided for the Replicator. A `KafkaClusterPingSuccessCount` of 0 combined with token errors often indicates the token endpoint is not reachable.

1. For the client credentials mechanism, verify that the `client_id` and `client_secret` in AWS Secrets Manager are correct and that the token acquisition mechanism matches what your IDP expects.

1. Verify that the `tokenEndpointAuthenticationMethod` is valid for your token acquisition mechanism. The client credentials mechanism requires `POST` or `BASIC`, and the client credentials assertion mechanism requires `NONE`.

1. For the IAM JWT bearer and client credentials assertion mechanisms, verify that the service execution role has the `sts:GetWebIdentityToken` permission, and that the `audience` and `signingAlgorithm` match what your IDP expects when it validates the token.

1. If your IDP uses a private CA, verify that the CA certificate referenced by `tokenEndpointTlsCertificateArn` is complete and valid.

1. Verify that the Kafka principal that your IDP maps the access token to has the ACL permissions that MSK Replicator requires on the source cluster.

1. Check the Replicator logs for the HTTP status and OAuth `error` code returned by the token endpoint. MSK Replicator logs these fields but never logs the token endpoint response body.

### SSL certificate issues
<a name="msk-replicator-ts-external-ssl"></a>

If the Replicator cannot establish a secure connection to the self-managed cluster:

1. Verify that the `certificate` value in AWS Secrets Manager includes the full CA certificate chain in PEM format.

1. Verify that the SSL listener is configured on all self-managed cluster brokers.

1. Verify that the certificate has not expired and is issued by a trusted CA.

### Consumer group offset synchronization failures for self-managed clusters
<a name="msk-replicator-ts-external-offsets"></a>

If consumer group offsets are not being synchronized correctly:

1. Verify the `ConsumerGroupOffsetSyncFailure` metric — it should be 0.

1. Verify that consumer groups are actively consuming on the source cluster (inactive consumer groups may not be synchronized).

1. For bidirectional replication, verify that `synchroniseConsumerGroupOffsets` is set to `true` on both Replicators.