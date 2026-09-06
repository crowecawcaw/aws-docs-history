

# CreateReplicator API examples for self-managed Kafka clusters
<a name="msk-replicator-external-api-examples"></a>

## Forward replication (Self-managed Kafka to MSK Provisioned)
<a name="msk-replicator-external-forward"></a>

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

**Using SASL/OAUTHBEARER (OAuth) authentication:**

The following example uses the client credentials mechanism, which reads a `client_id` and `client_secret` from the secret referenced by `tokenRequestSecretArn`. The `saslOAuthBearer` block replaces the `saslScram` or `MTLS` block in `clientAuthentication`. Specify exactly one of `clientCredentials`, `iamJwtBearer`, or `clientCredentialsAssertion`.

```
aws kafka create-replicator \
  --replicator-name my-selfmanaged-to-msk-replicator \
  --description "Replicating from self-managed Kafka to MSK Provisioned" \
  --service-execution-role-arn arn:aws:iam::123456789012:role/MSKReplicatorRole \
  --kafka-clusters '[
    {
      "apacheKafkaCluster": {
        "bootstrapBrokerString": "broker1:9096,broker2:9096,broker3:9096",
        "apacheKafkaClusterId": "<self-managed-cluster-id>"
      },
      "clientAuthentication": {
        "saslOAuthBearer": {
          "tokenEndpointUrl": "https://idp.example.com/oauth/token",
          "clientCredentials": {
            "tokenRequestSecretArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:kafka-oauth-creds"
          },
          "tokenEndpointAuthenticationMethod": "POST",
          "scope": "kafka",
          "tokenEndpointTlsCertificateArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:idp-ca-cert"
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

To use a secretless mechanism instead, replace the `clientCredentials` block with one of the following. The IAM JWT bearer mechanism uses the service execution role's AWS identity as the assertion. It requires an `audience` (the value of the `aud` claim your IDP expects) and a `signingAlgorithm` (`RS256` or `ES384`):

```
"clientAuthentication": {
  "saslOAuthBearer": {
    "tokenEndpointUrl": "https://idp.example.com/oauth/token",
    "iamJwtBearer": {
      "audience": "msk-replicator-client",
      "signingAlgorithm": "RS256"
    },
    "tokenEndpointAuthenticationMethod": "NONE",
    "scope": "kafka"
  }
}
```

The client credentials assertion mechanism uses the service execution role's signed JWT as the `client_assertion`. It also requires `audience` and `signingAlgorithm`, and requires `tokenEndpointAuthenticationMethod` to be set to `NONE`:

```
"clientAuthentication": {
  "saslOAuthBearer": {
    "tokenEndpointUrl": "https://idp.example.com/oauth/token",
    "clientCredentialsAssertion": {
      "audience": "msk-replicator-client",
      "signingAlgorithm": "RS256"
    },
    "tokenEndpointAuthenticationMethod": "NONE",
    "scope": "kafka"
  }
}
```

The example includes `tokenEndpointTlsCertificateArn`, which is optional and needed only if your IDP presents a certificate issued by a private CA; omit it if your IDP uses a publicly trusted certificate. If your Kafka provider requires SASL extensions during the handshake, add them as `extension.<name>` entries in your secret rather than in the API request. See [Store credentials in AWS Secrets Manager](msk-replicator-external-prereqs.md#msk-replicator-external-secrets).

## Bidirectional replication example
<a name="msk-replicator-external-bidirectional"></a>

To set up bidirectional replication for rollback capability, both the forward and reverse Replicators must be created with `consumerGroupOffsetSyncMode` set to `ENHANCED`. This ensures consumer group offsets are synchronized in a way that supports seamless cutover in either direction.

**Important**  
Register each cluster the same way in both Replicators. If a cluster is registered as an Amazon MSK cluster (`amazonMskCluster`, using its cluster ARN) in one Replicator, register it as an Amazon MSK cluster in the other as well. If it is registered as a self-managed Apache Kafka cluster (`apacheKafkaCluster`, using a bootstrap broker string), use that same type in both. Doing so ensures consistent tracking in MSK Replicator to prevent replication loops.

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
<a name="msk-replicator-external-verify"></a>

Check the status of your Replicator using the `describe-replicator` CLI command:

```
aws kafka describe-replicator \
  --replicator-arn arn:aws:kafka:us-east-1:123456789012:replicator/my-replicator/xxx
```

The Replicator will progress through `CREATING` → `RUNNING` states. Allow approximately 30 minutes for the Replicator to reach `RUNNING` status.