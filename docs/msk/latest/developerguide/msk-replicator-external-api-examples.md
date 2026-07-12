# CreateReplicator API examples for self-managed Kafka clusters

## Forward replication (Self-managed Kafka to MSK Provisioned)

Use the following AWS CLI command to create a Replicator that replicates data from your self-managed Kafka cluster to an Amazon MSK Provisioned cluster.

**Using SASL/SCRAM authentication:**

```
aws kafka create-replicator \
  --replicator-name my-selfmanaged-to-msk-replicator \
  --description "Replicating from self-managed Kafka to MSK Provisioned" \
  --service-execution-role-arn arn:aws:iam::123456789012:role/MSKReplicatorRole \
  --kafka-clusters '[
    {
      "apacheKafkaCluster": {
        "bootstrapBrokerString": "broker1:9094,broker2:9094,broker3:9094",
        "apacheKafkaClusterId": "<self-managed-cluster-id>"
      },
      "clientAuthentication": {
        "saslScram": {
          "mechanism": "SHA256",
          "secretArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-scram-creds"
        }
      },
      "encryptionInTransit": {
        "encryptionType": "TLS",
        "rootCaCertificate": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-scram-creds"
      },
      "vpcConfig": {
        "subnetIds": ["subnet-aaa","subnet-bbb","subnet-ccc"],
        "securityGroupIds": ["sg-xxxxxxxxxxxxxxxxx"]
      }
    },
    {
      "amazonMskCluster": {
        "mskClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/msk-provisioned/xxx"
      },
      "vpcConfig": {
        "subnetIds": ["subnet-ddd","subnet-eee","subnet-fff"],
        "securityGroupIds": ["sg-yyyyyyyyy"]
      }
    }]' \
  --replication-info-list '[{
    "sourceKafkaClusterId": "<self-managed-cluster-id>",
    "targetKafkaClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/msk-provisioned/xxx",
    "targetCompressionType": "NONE",
    "topicReplication": {
      "topicsToReplicate": [".*"],
      "topicNameConfiguration": {"type": "IDENTICAL"},
      "startingPosition": {"type": "EARLIEST"},
      "detectAndCopyNewTopics": true,
      "copyTopicConfigurations": true,
      "copyAccessControlListsForTopics": true
    },
    "consumerGroupReplication": {
      "consumerGroupsToReplicate": [".*"],
      "detectAndCopyNewConsumerGroups": true,
      "synchroniseConsumerGroupOffsets": true
    }}]'
```

**Using mTLS authentication:**

```
aws kafka create-replicator \
  --replicator-name my-selfmanaged-to-msk-replicator \
  --description "Replicating from self-managed Kafka to MSK Provisioned" \
  --service-execution-role-arn arn:aws:iam::123456789012:role/MSKReplicatorRole \
  --kafka-clusters '[
    {
      "apacheKafkaCluster": {
        "bootstrapBrokerString": "broker1:9095,broker2:9095,broker3:9095",
        "apacheKafkaClusterId": "<self-managed-cluster-id>"
      },
      "clientAuthentication": {
        "MTLS": {
          "secretArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-mtls-creds"
        }
      },
      "encryptionInTransit": {
        "encryptionType": "TLS",
        "rootCaCertificate": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-ca-cert"
      },
      "vpcConfig": {
        "subnetIds": ["subnet-aaa","subnet-bbb","subnet-ccc"],
        "securityGroupIds": ["sg-xxxxxxxxxxxxxxxxx"]
      }
    },
    {
      "amazonMskCluster": {
        "mskClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/msk-provisioned/xxx"
      },
      "vpcConfig": {
        "subnetIds": ["subnet-ddd","subnet-eee","subnet-fff"],
        "securityGroupIds": ["sg-yyyyyyyyy"]
      }
    }]' \
  --replication-info-list '[{
    "sourceKafkaClusterId": "<self-managed-cluster-id>",
    "targetKafkaClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/msk-provisioned/xxx",
    "targetCompressionType": "NONE",
    "topicReplication": {
      "topicsToReplicate": [".*"],
      "topicNameConfiguration": {"type": "IDENTICAL"},
      "startingPosition": {"type": "EARLIEST"},
      "detectAndCopyNewTopics": true,
      "copyTopicConfigurations": true,
      "copyAccessControlListsForTopics": true
    },
    "consumerGroupReplication": {
      "consumerGroupsToReplicate": [".*"],
      "detectAndCopyNewConsumerGroups": true,
      "synchroniseConsumerGroupOffsets": true
    }}]'
```

## Bidirectional replication example

To set up bidirectional replication for rollback capability, both the forward and reverse Replicators must be created with `consumerGroupOffsetSyncMode` set to `ENHANCED`. This ensures consumer group offsets are synchronized in a way that supports seamless cutover in either direction.

**Using SASL/SCRAM authentication:**

Create the forward Replicator (self-managed Kafka to MSK Provisioned) with `ENHANCED` offset sync mode:

```
aws kafka create-replicator \
  --replicator-name my-selfmanaged-to-msk-replicator \
  --description "Replicating from self-managed Kafka to MSK Provisioned" \
  --service-execution-role-arn arn:aws:iam::123456789012:role/MSKReplicatorRole \
  --kafka-clusters '[
    {
      "apacheKafkaCluster": {
        "bootstrapBrokerString": "broker1:9094,broker2:9094,broker3:9094",
        "apacheKafkaClusterId": "<self-managed-cluster-id>"
      },
      "clientAuthentication": {
        "saslScram": {
          "mechanism": "SHA256",
          "secretArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-scram-creds"
        }
      },
      "encryptionInTransit": {
        "encryptionType": "TLS",
        "rootCaCertificate": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-ca-cert"
      },
      "vpcConfig": {
        "subnetIds": ["subnet-aaa","subnet-bbb","subnet-ccc"],
        "securityGroupIds": ["sg-xxxxxxxxxxxxxxxxx"]
      }
    },
    {
      "amazonMskCluster": {
        "mskClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/msk-provisioned/xxx"
      },
      "vpcConfig": {
        "subnetIds": ["subnet-ddd","subnet-eee","subnet-fff"],
        "securityGroupIds": ["sg-yyyyyyyyy"]
      }
    }]' \
  --replication-info-list '[{
    "sourceKafkaClusterId": "<self-managed-cluster-id>",
    "targetKafkaClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/msk-provisioned/xxx",
    "targetCompressionType": "NONE",
    "topicReplication": {
      "topicsToReplicate": [".*"],
      "topicNameConfiguration": {"type": "IDENTICAL"},
      "startingPosition": {"type": "EARLIEST"},
      "detectAndCopyNewTopics": true,
      "copyTopicConfigurations": true,
      "copyAccessControlListsForTopics": true
    },
    "consumerGroupReplication": {
      "consumerGroupsToReplicate": [".*"],
      "detectAndCopyNewConsumerGroups": true,
      "synchroniseConsumerGroupOffsets": true,
      "consumerGroupOffsetSyncMode": "ENHANCED"
    }}]'
```

Then create the reverse Replicator (MSK Provisioned to self-managed Kafka) also with `ENHANCED` offset sync mode:

```
aws kafka create-replicator \
  --replicator-name my-msk-to-selfmanaged-replicator \
  --description "Reverse replication for rollback" \
  --service-execution-role-arn arn:aws:iam::123456789012:role/MSKReplicatorRole \
  --kafka-clusters '[
    {
      "amazonMskCluster": {
        "mskClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/msk-provisioned/xxx"
      },
      "vpcConfig": {
        "subnetIds": ["subnet-ddd","subnet-eee","subnet-fff"],
        "securityGroupIds": ["sg-yyyyyyyyy"]
      }
    },
    {
      "apacheKafkaCluster": {
        "bootstrapBrokerString": "broker1:9094,broker2:9094,broker3:9094",
        "apacheKafkaClusterId": "<self-managed-cluster-id>"
      },
      "clientAuthentication": {
        "saslScram": {
          "mechanism": "SHA256",
          "secretArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-scram-creds"
        }
      },
      "encryptionInTransit": {
        "encryptionType": "TLS",
        "rootCaCertificate": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-ca-cert"
      },
      "vpcConfig": {
        "subnetIds": ["subnet-aaa","subnet-bbb","subnet-ccc"],
        "securityGroupIds": ["sg-xxxxxxxxxxxxxxxxx"]
      }
    }]' \
  --replication-info-list '[{
    "sourceKafkaClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/msk-provisioned/xxx",
    "targetKafkaClusterId": "<self-managed-cluster-id>",
    "targetCompressionType": "NONE",
    "topicReplication": {
      "topicsToReplicate": [".*"],
      "topicNameConfiguration": {"type": "IDENTICAL"},
      "startingPosition": {"type": "LATEST"},
      "detectAndCopyNewTopics": true,
      "copyTopicConfigurations": true,
      "copyAccessControlListsForTopics": true
    },
    "consumerGroupReplication": {
      "consumerGroupsToReplicate": [".*"],
      "detectAndCopyNewConsumerGroups": true,
      "synchroniseConsumerGroupOffsets": true,
      "consumerGroupOffsetSyncMode": "ENHANCED"
    }}]'
```

**Using mTLS authentication:**

Create the forward Replicator (self-managed Kafka to MSK Provisioned) with `ENHANCED` offset sync mode:

```
aws kafka create-replicator \
  --replicator-name my-selfmanaged-to-msk-replicator \
  --description "Replicating from self-managed Kafka to MSK Provisioned" \
  --service-execution-role-arn arn:aws:iam::123456789012:role/MSKReplicatorRole \
  --kafka-clusters '[
    {
      "apacheKafkaCluster": {
        "bootstrapBrokerString": "broker1:9095,broker2:9095,broker3:9095",
        "apacheKafkaClusterId": "<self-managed-cluster-id>"
      },
      "clientAuthentication": {
        "MTLS": {
          "secretArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-mtls-creds"
        }
      },
      "encryptionInTransit": {
        "encryptionType": "TLS",
        "rootCaCertificate": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-ca-cert"
      },
      "vpcConfig": {
        "subnetIds": ["subnet-aaa","subnet-bbb","subnet-ccc"],
        "securityGroupIds": ["sg-xxxxxxxxxxxxxxxxx"]
      }
    },
    {
      "amazonMskCluster": {
        "mskClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/msk-provisioned/xxx"
      },
      "vpcConfig": {
        "subnetIds": ["subnet-ddd","subnet-eee","subnet-fff"],
        "securityGroupIds": ["sg-yyyyyyyyy"]
      }
    }]' \
  --replication-info-list '[{
    "sourceKafkaClusterId": "<self-managed-cluster-id>",
    "targetKafkaClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/msk-provisioned/xxx",
    "targetCompressionType": "NONE",
    "topicReplication": {
      "topicsToReplicate": [".*"],
      "topicNameConfiguration": {"type": "IDENTICAL"},
      "startingPosition": {"type": "EARLIEST"},
      "detectAndCopyNewTopics": true,
      "copyTopicConfigurations": true,
      "copyAccessControlListsForTopics": true
    },
    "consumerGroupReplication": {
      "consumerGroupsToReplicate": [".*"],
      "detectAndCopyNewConsumerGroups": true,
      "synchroniseConsumerGroupOffsets": true,
      "consumerGroupOffsetSyncMode": "ENHANCED"
    }}]'
```

Then create the reverse Replicator (MSK Provisioned to self-managed Kafka) also with `ENHANCED` offset sync mode:

```
aws kafka create-replicator \
  --replicator-name my-msk-to-selfmanaged-replicator \
  --description "Reverse replication for rollback" \
  --service-execution-role-arn arn:aws:iam::123456789012:role/MSKReplicatorRole \
  --kafka-clusters '[
    {
      "amazonMskCluster": {
        "mskClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/msk-provisioned/xxx"
      },
      "vpcConfig": {
        "subnetIds": ["subnet-ddd","subnet-eee","subnet-fff"],
        "securityGroupIds": ["sg-yyyyyyyyy"]
      }
    },
    {
      "apacheKafkaCluster": {
        "bootstrapBrokerString": "broker1:9095,broker2:9095,broker3:9095",
        "apacheKafkaClusterId": "<self-managed-cluster-id>"
      },
      "clientAuthentication": {
        "MTLS": {
          "secretArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-mtls-creds"
        }
      },
      "encryptionInTransit": {
        "encryptionType": "TLS",
        "rootCaCertificate": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-ca-cert"
      },
      "vpcConfig": {
        "subnetIds": ["subnet-aaa","subnet-bbb","subnet-ccc"],
        "securityGroupIds": ["sg-xxxxxxxxxxxxxxxxx"]
      }
    }]' \
  --replication-info-list '[{
    "sourceKafkaClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/msk-provisioned/xxx",
    "targetKafkaClusterId": "<self-managed-cluster-id>",
    "targetCompressionType": "NONE",
    "topicReplication": {
      "topicsToReplicate": [".*"],
      "topicNameConfiguration": {"type": "IDENTICAL"},
      "startingPosition": {"type": "LATEST"},
      "detectAndCopyNewTopics": true,
      "copyTopicConfigurations": true,
      "copyAccessControlListsForTopics": true
    },
    "consumerGroupReplication": {
      "consumerGroupsToReplicate": [".*"],
      "detectAndCopyNewConsumerGroups": true,
      "synchroniseConsumerGroupOffsets": true,
      "consumerGroupOffsetSyncMode": "ENHANCED"
    }}]'
```

## Verify Replicator status

Check the status of your Replicator using the `describe-replicator` CLI command:

```
aws kafka describe-replicator \
  --replicator-arn arn:aws:kafka:us-east-1:123456789012:replicator/my-replicator/xxx
```

The Replicator will progress through `CREATING` → `RUNNING` states. Allow approximately 30 minutes for the Replicator to reach `RUNNING` status.
