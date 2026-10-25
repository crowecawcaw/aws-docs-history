

# Kafka cluster ID for KRaft clusters
<a name="kraft-cluster-id"></a>

Each Apache Kafka cluster has a cluster ID that identifies it to Kafka clients and tools. Amazon MSK KRaft clusters created on or after August 4, 2026, are automatically assigned a unique cluster ID. Some KRaft clusters created before that date may share the cluster ID `3Db5QLSqSZieL3rJBUUegA`.

1. Run the following command to view the cluster ID for your cluster:

   ```
   kafka-cluster.sh cluster-id --bootstrap-server {{bootstrap-brokers}}
   ```

   In the command, replace {{bootstrap-brokers}} with the bootstrap broker connection string for your cluster.

1. If your cluster reports the ID `3Db5QLSqSZieL3rJBUUegA` and you want a unique cluster ID, open the [AWS Support Center console](https://console.aws.amazon.com/support/home#/) and create a support case. Include the cluster ARN in your case.