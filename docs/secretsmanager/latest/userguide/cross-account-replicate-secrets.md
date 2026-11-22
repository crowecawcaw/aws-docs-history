

# Replicate AWS Secrets Manager secrets across accounts

Cross-account replication lets you replicate secret values from a *primary* secret into a new *replica* secret in a different AWS account. The replica secret is an independent secret that has its own access policies, KMS key, and lifecycle. When the secret value in the primary secret changes, Secrets Manager propagates the new value to the replica secret. Cross-account replication is useful when you want to use the same secret value in multiple accounts and manage the secret separately in each account.

Cross-account replication involves two AWS accounts: the *primary account* that owns the primary secret, and the *replica account* that holds the replica secret. Both secrets must be in the same AWS Region.

For pricing information for replica secrets, see [AWS Secrets Manager Pricing](https://aws.amazon.com/secrets-manager/pricing/).

**Topics**
+ [How cross-account replication works](#cross-account-replicate-secrets_model)
+ [Replication status](#cross-account-replicate-secrets_status)
+ [Constraints](#cross-account-replicate-secrets_constraints)
+ [What Secrets Manager replicates](#cross-account-replicate-secrets_whatreplicates)
+ [Create a replica secret](cross-account-replicate-create.md)
+ [Associate the replica with a primary secret](cross-account-replicate-associate.md)
+ [How Secrets Manager authorizes cross-account replication](cross-account-replicate-permissions.md)
+ [Monitor cross-account replication](cross-account-replicate-status.md)
+ [Stop cross-account replication](cross-account-replicate-remove.md)

## How cross-account replication works
<a name="cross-account-replicate-secrets_model"></a>

Cross-account replication is a two-party process. Both account owners take part:
+ The *replica-account owner* creates the replica secret, sets up the required permissions, and configures it to reference the primary secret.
+ The *primary-account owner* associates the replica with the primary secret. This association starts replication from the primary secret to the replica secret.

Replication is asynchronous and eventually consistent. After the primary-account owner associates the replica, Secrets Manager copies the secret value in the background, so the replica might not reflect the latest value immediately. To track progress, call [`DescribeSecret`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html) and check the replication status. For more information, see [Monitor cross-account replication](cross-account-replicate-status.md).

## Replication status
<a name="cross-account-replicate-secrets_status"></a>

Each secret reports a replication status that moves through the following values as replication progresses:

Pending  
Secrets Manager has recorded the replication relationship but has not yet started copying the secret value. Only the replica secret shows this status.

InProgress  
Secrets Manager is copying the secret value from the primary to the replica.

InSync  
The replica holds the same secret value as the primary. This is the steady state for a healthy replica.

Failed  
Secrets Manager could not complete replication. The status message describes the cause. For how to recover, see [Monitor cross-account replication](cross-account-replicate-status.md).

Detached  
One of the two accounts stopped replication, so the primary and replica secrets are no longer linked.

## Constraints
<a name="cross-account-replicate-secrets_constraints"></a>

Cross-account replication has the following constraints:
+ **Same Region** – The primary and replica secrets must be in the same AWS Region.
+ **One replica per primary** – A primary secret can have at most one cross-account replica. If a replica already exists, a request to associate another replica fails.
+ **Customer managed key required** – You must encrypt the replica secret with a customer managed KMS key. The replica cannot use the AWS managed key `aws/secretsmanager`. For more information, see [Create a replica secret](cross-account-replicate-create.md).

## What Secrets Manager replicates
<a name="cross-account-replicate-secrets_whatreplicates"></a>

Secrets Manager replicates the following from the primary secret to the replica:
+ The secret value and its version data
+ The secret description
+ The secret type
+ The version and staging label mappings

Secrets Manager does not replicate the following. Each account manages its own:
+ Tags
+ Resource policy
+ KMS key