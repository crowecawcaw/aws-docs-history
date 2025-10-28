# Set up SASL/SCRAM authentication for an Amazon MSK

cluster

To set up a secret in AWS Secrets Manager, follow the [Creating and Retrieving a Secret](../../../secretsmanager/latest/userguide/tutorials_basic.md "../../../secretsmanager/latest/userguide/tutorials_basic.md")
tutorial in the [AWS Secrets Manager User Guide](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

Note the following requirements when creating a secret for an Amazon MSK cluster:

- Choose **Other type of secrets
  (e.g. API key)** for the secret type.
- Your secret name must begin with the prefix **AmazonMSK\_**.
- You must either use an existing custom AWS KMS key or create a new custom AWS KMS key
  for your secret. Secrets Manager uses the default AWS KMS key for a secret by default.

###### Important

A secret created with
the default AWS KMS key cannot be used with an Amazon MSK cluster.

- Your sign-in credential data must be in the following format to enter key-value pairs using the
  **Plaintext** option.

```
{
  "username": "alice",
  "password": "alice-secret"
}
```

- Record the ARN (Amazon Resource Name) value for your secret.
- ###### Important

You can't associate a Secrets Manager secret with a cluster that exceeds the limits
described in [Right-size your cluster: Number of
partitions per Standard broker](bestpractices.md#partitions-per-broker "bestpractices.md#partitions-per-broker").

- If you use the AWS CLI to create the secret, specify a key ID or ARN for the
  `kms-key-id` parameter. Don't specify an alias.
- To associate the secret with your cluster, use either the Amazon MSK console, or the
  [BatchAssociateScramSecret](../../1.0/apireference/clusters-clusterarn-scram-secrets.md#BatchAssociateScramSecret "../../1.0/apireference/clusters-clusterarn-scram-secrets.md#BatchAssociateScramSecret") operation.

###### Important

When you associate a secret with a cluster, Amazon MSK attaches a resource policy to the secret that allows your cluster to access and read the secret values that you defined. You should not modify this resource policy. Doing so can prevent your cluster from accessing your secret. If you make any changes to the Secrets resource policy and/ or the KMS key used for secret encryption, make sure you re-associate the secrets to your MSK cluster. This will make sure that your cluster can continue accessing your secret.

The following example JSON input for the `BatchAssociateScramSecret`
operation associates a secret with a cluster:

```
{
  "clusterArn" : "arn:aws:kafka:us-west-2:0123456789019:cluster/SalesCluster/abcd1234-abcd-cafe-abab-9876543210ab-4",
  "secretArnList": [
    "arn:aws:secretsmanager:us-west-2:0123456789019:secret:AmazonMSK_MyClusterSecret"
  ]
}
```
