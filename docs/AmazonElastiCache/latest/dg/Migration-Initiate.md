# Starting migration

After all prerequisites are complete, you can begin data migration using the
AWS Management Console, ElastiCache API, or AWS CLI. For cluster-mode enabled, if slot migration differs, a
resharding will be performed before live migration. The following example shows using
the CLI.

###### Note

We recommended to use `TestMigration` API to validate migration setup.
But this is strictly optional.

Start migration by calling the `start-migration` command with the following
parameters:

- `--replication-group-id` – Identifier of the target ElastiCache
  replication group
- `--customer-node-endpoint-list` – A list of endpoints with
  either DNS or IP addresses and the port where your source Valkey or Redis OSS cluster is
  running. The list can only take one element for both cluster-mode disabled and
  cluster-mode enabled. If you have enabled chained replication, the endpoint can
  point to a replica instead of the primary node in your Valkey or Redis OSS cluster.
  The following is an example using the CLI.

```
aws elasticache start-migration --replication-group-id test-cluster --customer-node-endpoint-list "Address='10.0.0.241',Port=6379"
```

As you run this command, the ElastiCache primary node (in each shard) configures itself to
become a replica of your Valkey or Redis OSS instance (in corresponding shard owning same slots in
cluster enabled redis). The status of ElastiCache cluster changes to
**migrating** and data starts migrating from your Valkey or Redis OSS instance to
the ElastiCache primary node. Depending on the size of the data and load on your Valkey or Redis OSS instance, the migration can take a while to complete. You can check the progress of the
migration by running the [valkey-cli
INFO](https://valkey.io/commands/info "https://valkey.io/commands/info") command on your Valkey instance and ElastiCache primary node.

After successful replication, all writes to your Valkey or Redis OSS instances propagate to the ElastiCache
cluster. You can use ElastiCache nodes for reads. However, you can't write to the ElastiCache
cluster. If an ElastiCache primary node has other replica nodes connected to it, these
replica nodes continue to replicate from the ElastiCache primary node. This way, all the data
from your Valkey or Redis OSS cluster gets replicated to all the nodes in ElastiCache cluster.

If an ElastiCache primary node can't become a replica of your Valkey or Redis OSS instance, it retries
several times before eventually promoting itself back to primary. The status of ElastiCache
cluster then changes to **available**, and a replication group event
about the failure to initiate the migration is sent. To troubleshoot such a failure,
check the following:

- Look at the replication group event. Use any specific information from the
  event to fix the migration failure.
- If the event doesn’t provide any specific information, make sure that you have
  followed the guidelines in [Preparing your source and target for migration](Migration-Prepare.md "Migration-Prepare.md").
- Ensure that the routing configuration for your VPC and subnets allows traffic
  between ElastiCache nodes and your Valkey or Redis OSS instances.
- Ensure the security group attached to your Valkey or Redis OSS instances allows input bound
  traffic from ElastiCache nodes.
- Check Valkey or Redis OSS logs for your instances for more information about failures
  specific to replication.
