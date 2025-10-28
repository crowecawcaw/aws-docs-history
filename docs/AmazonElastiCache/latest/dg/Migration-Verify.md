# Verifying the data migration progress

After the data migration has begun, you can do the following to track its
progress:

- Verify that Valkey or Redis OSS `master_link_status` is `up` in the
  `INFO` command on ElastiCache primary node(s). You can also find this
  information in the ElastiCache console. Select the cluster and under
  **CloudWatch metrics**, observe **Primary Link
  Health Status**. After the value reaches 1, the data is in sync.
- You can check that the ElastiCache replica has an **online**
  state by running the `INFO` command on your Valkey or Redis OSS instances. Doing
  this also provides information about replication lag.
- Verify low client output buffer by using the [CLIENT LIST](https://valkey.io/commands/client-list "https://valkey.io/commands/client-list") command on your Valkey or Redis OSS instances.
  After the data migration is complete, the data is in sync with any new writes coming
  to the primary node(s) of your Valkey or Redis OSS cluster.
