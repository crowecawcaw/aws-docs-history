# Authenticating with the Valkey and Redis OSS AUTH command

###### Note

The **AUTH** has been superseded by [Role-Based Access Control (RBAC)](Clusters.md "Clusters.md"). All serverless caches must use RBAC for authentication.

Valkey and Redis OSS authentication tokens or passwords enable Valkey and Redis OSS to require a password before allowing clients to run commands, thereby improving data security.
The **AUTH** is available for node-based clusters only.

###### Topics

- [Overview of AUTH in ElastiCache for Valkey and Redis OSS](#auth-overview "#auth-overview")
- [Applying authentication to an ElastiCache for Valkey and Redis OSS cluster](#auth-using "#auth-using")
- [Modifying the AUTH token on an existing cluster](#auth-modifyng-token "#auth-modifyng-token")
- [Migrating from RBAC to AUTH](#Migrate-From-RBAC-to-AUTH "#Migrate-From-RBAC-to-AUTH")

## Overview of AUTH in ElastiCache for Valkey and Redis OSS

When you use the **AUTH** with your ElastiCache for Valkey and Redis OSS cluster, there are some refinements.

In particular, be aware of these AUTH token or password constraints when using AUTH:

- Tokens, or passwords, must be 16–128 printable characters.
- Nonalphanumeric characters are restricted to (!, &, #, $, ^, <, >, -).
- AUTH can only be enabled for encryption in-transit enabled Valkey or Redis OSS clusters.

To set up a strong token, we recommend that you follow a strict password policy, such as requiring the
following:

- Tokens or passwords must include at least three of the following character types:
  - Uppercase characters
  - Lowercase characters
  - Digits
  - Nonalphanumeric characters (`!`, `&`, `#`,
    `$`, `^`, `<`,
    `>`, `-`)

- Tokens or passwords must not contain a dictionary word or a slightly modified dictionary
  word.
- Tokens or passwords must not be the same as or similar to a recently used token.

## Applying authentication to an ElastiCache for Valkey and Redis OSS cluster

You can require that users enter a token (password) on a token-protected Valkey or Redis OSS server. To do
this, include the parameter `--auth-token` (API: `AuthToken`) with
the correct token when you create your replication group or cluster. Also include it
in all subsequent commands to the replication group or cluster.

The following AWS CLI operation creates a replication group with encryption in transit (TLS)
enabled and the **AUTH** token `This-is-a-sample-token`. Replace the
subnet group `sng-test` with a subnet group that exists.

###### Key parameters

- `--engine` – Must be `valkey` or `redis`.
- `--engine-version` – If engine is Redis OSS, must be 3.2.6, 4.0.10, or later.
- `--transit-encryption-enabled` – Required for authentication and
  HIPAA eligibility.
- `--auth-token` – Required for HIPAA eligibility. This value
  must be the correct token for this token-protected Valkey or Redis OSS server.
- `--cache-subnet-group` – Required for HIPAA eligibility.

For Linux, macOS, or Unix:

```
aws elasticache create-replication-group \
    --replication-group-id `authtestgroup` \
    --replication-group-description `authtest` \
    --engine `redis` \
    --cache-node-type `cache.m4.large` \
    --num-node-groups `1` \
    --replicas-per-node-group `2` \
    --transit-encryption-enabled \
    --auth-token `This-is-a-sample-token` \
    --cache-subnet-group `sng-test`
```

For Windows:

```
aws elasticache create-replication-group ^
    --replication-group-id `authtestgroup` ^
    --replication-group-description `authtest` ^
    --engine `redis` ^
    --cache-node-type `cache.m4.large` ^
    --num-node-groups `1` ^
    --replicas-per-node-group `2` ^
    --transit-encryption-enabled ^
    --auth-token `This-is-a-sample-token` ^
    --cache-subnet-group `sng-test`
```

## Modifying the AUTH token on an existing cluster

To make it easier to update your authentication, you can modify the
**AUTH** token used on a cluster. You can make this
modification if the engine version is Valkey 7.2 or higher or Redis 5.0.6 or higher. ElastiCache must also have encryption in
transit enabled. For more information, see [ElastiCache in-transit encryption (TLS)](in-transit-encryption.md "in-transit-encryption.md").

Modifying the auth token supports two strategies: ROTATE and SET. The ROTATE strategy
adds an additional AUTH token to the server while retaining the
previous token. The SET strategy updates the server to support just a single
AUTH token. Make these modification calls with the
`--apply-immediately` parameter to apply changes immediately.

### Rotating the AUTH token

To update a Valkey or Redis OSS server with a new **AUTH token**, call the
`ModifyReplicationGroup` API with the `--auth-token`
parameter as the new **AUTH** token and the `--auth-token-update-strategy`
with the value ROTATE. After the ROTATE modification is complete, the cluster will support
the previous AUTH token in addition to the one specified in the
`auth-token` parameter.
If no AUTH token was configured on the replication group before the AUTH token rotation,
the cluster supports the AUTH token specified in the `--auth-token` parameter in addition to supporting connecting without authentication.
See [Setting the AUTH token](#auth-modifying-set "#auth-modifying-set") to update the AUTH token to be required using update strategy SET.

###### Note

If you do not configure the AUTH token before, then once the modification is
complete, the cluster will support no AUTH token in addition to the one
specified in the auth-token parameter.

If this modification is performed on a server that already supports two
AUTH tokens, the oldest AUTH token will
also be removed during this operation. This allows a server to support up to two most
recent AUTH tokens at a given time.

At this point, you can proceed by updating the client to use the latest
AUTH token. After the clients are updated, you can use the
SET strategy for **AUTH** token rotation (explained in the following
section) to exclusively start using the new token.

The following AWS CLI operation modifies a replication group to rotate the
**AUTH** token
`This-is-the-rotated-token`.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group \
--replication-group-id `authtestgroup` \
--auth-token `This-is-the-rotated-token` \
--auth-token-update-strategy ROTATE \
--apply-immediately

```

For Windows:

```
aws elasticache modify-replication-group ^
--replication-group-id `authtestgroup` ^
--auth-token `This-is-the-rotated-token` ^
--auth-token-update-strategy ROTATE ^
--apply-immediately

```

### Setting the AUTH token

To update a Valkey or Redis OSS server to support a
single required **AUTH** token, call the `ModifyReplicationGroup`
API operation with the `--auth-token` parameter with same value as the last AUTH token and the `--auth-token-update-strategy` parameter with the value `SET`. The SET strategy can only be used with a cluster that has 2 AUTH tokens or 1 optional AUTH token from using a ROTATE strategy before.
After the modification is complete, the server supports only the AUTH token specified in the auth-token parameter.

The following AWS CLI operation modifies a replication group to set the
AUTH token to
`This-is-the-set-token`.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group \
--replication-group-id `authtestgroup` \
--auth-token `This-is-the-set-token` \
--auth-token-update-strategy SET \
--apply-immediately

```

For Windows:

```
aws elasticache modify-replication-group ^
--replication-group-id `authtestgroup` ^
--auth-token `This-is-the-set-token` ^
--auth-token-update-strategy SET ^
--apply-immediately

```

### Enabling authentication on an existing cluster

To enable authentication on an existing Valkey or Redis OSS server, call the
`ModifyReplicationGroup` API operation. Call
`ModifyReplicationGroup` with the `--auth-token` parameter
as the new token and the `--auth-token-update-strategy` with the value
ROTATE.

After the ROTATE modification is complete, the cluster supports the
**AUTH** token specified in the `--auth-token` parameter
in addition to supporting connecting without authentication.
Once all client applications are updated to authenticate to Valkey or Redis OSS with the AUTH token, use the SET strategy to mark the AUTH token as required. Enabling authentication is only supported on Valkey and Redis OSS servers with encryption in transit (TLS) enabled.

## Migrating from RBAC to AUTH

If you are authenticating users with Valkey or Redis OSS Role-Based Access Control (RBAC) as described in [Role-Based Access Control (RBAC)](Clusters.md "Clusters.md"), and you want to
migrate to AUTH, use the following procedures. You can migrate using either
console or CLI.

###### To migrate from RBAC to AUTH using the console

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the list in the upper-right corner, choose the AWS Region where the
   cluster that you want to modify is located.
3. In the navigation pane, choose the engine running on the cluster that you
   want to modify.

A list of the chosen engine's clusters appears. 4. In the list of clusters, for the cluster that you want to modify, choose
its name. 5. For **Actions**, choose **Modify**.

The **Modify** window appears. 6. For **Access control**, choose **Valkey AUTH default
user access** or **Redis OSS AUTH default
user access**. 7. Under **Valkey AUTH token** or **Redis OSS AUTH token**, set a new token. 8. Choose **Preview changes** and then on the next screen, **Modify**.

**To migrate from RBAC to AUTH using the AWS CLI**

Use one of the following commands to configure a new optional **AUTH** token for your Valkey or Redis OSS replication group. Note that an optional Auth token will allow unauthenticated access to the replication group until the Auth token is marked as required, using the update strategy `SET` in the following step.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group \
    --replication-group-id test \
    --remove-user-groups \
    --auth-token This-is-a-sample-token \
    --auth-token-update-strategy ROTATE \
    --apply-immediately
```

For Windows:

```
aws elasticache modify-replication-group ^
    --replication-group-id test ^
    --remove-user-groups ^
    --auth-token This-is-a-sample-token ^
    --auth-token-update-strategy ROTATE ^
    --apply-immediately
```

After executing the above command, you can update your Valkey or Redis OSS applications to authenticate to the ElastiCache replication group using the newly configured optional AUTH token. To complete the Auth token rotation, use the the update strategy `SET` in the subsequent command below. This will mark to the optional AUTH token as required. When the Auth token update completes, the replication group status will show as `ACTIVE` and all connections to this replication group will require authentication.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group \
			--replication-group-id test \
			--auth-token This-is-a-sample-token \
			--auth-token-update-strategy SET \
			--apply-immediately
```

For Windows:

```
aws elasticache modify-replication-group ^
			--replication-group-id test ^
			--remove-user-groups ^
			--auth-token This-is-a-sample-token ^
			--auth-token-update-strategy SET ^
			--apply-immediately
```

For more information, see [Authenticating with the Valkey and Redis OSS AUTH command](auth.md "auth.md").

###### Note

If you need to disable access control on an ElastiCache Cluster, see [Disabling access control on an ElastiCache Valkey or Redis OSS cache](in-transit-encryption-disable.md "in-transit-encryption-disable.md").
