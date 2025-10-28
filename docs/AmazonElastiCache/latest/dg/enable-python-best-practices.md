# Best practices when enabling in-transit encryption

## Before enabling in-transit

encryption: make sure you have proper DNS records handling

###### Note

We are changing and deleting old endpoints during this process. Incorrect
usage of the endpoints can result in the Valkey or Redis OSS client using old and deleted
endpoints that will prevent it from connecting to the cluster.

While the cluster is being migrated from no-TLS to TLS-preferred, the old cluster configuration
endpoint DNS record is kept and the new cluster configuration endpoint DNS records are being generated
in a different format. TLS-enabled clusters use a different format of DNS records than TLS-disabled
clusters. ElastiCache will keep both DNS records when a cluster is configured in `encryption mode: Preferred` so that Applications and other Valkey or Redis OSS clients can switch between them. The following changes in
the DNS records take place during the TLS-migration process:

### Description of

the changes in the DNS records that take place when enabling in-transit
encryption

**For CME clusters**

When a cluster is set to ‘transit encryption mode: preferred’:

- The original cluster configuration endpoint for no-TLS cluster will remain active. There will be no downtime when cluster is re-configured form TLS encryption mode ‘none’ to ‘preferred’.
- New TLS Valkey or Redis OSS endpoints will be generated when cluster is set to
  TLS-preferred mode. These new endpoints will resolve to the same IPs
  as the old ones (non-TLS).
- The new TLS Valkey or Redis OSS configuration endpoint will be exposed in the
  ElastiCache Console and in the response to
  `describe-replication-group` API.

When a cluster is set to ‘transit encryption mode: required’:

- Old non-TLS enabled endpoints will be deleted. There will be no
  downtime of TLS cluster endpoints.
- You can retrieve a new `cluster-configuration-endpoint`
  from ElastiCache Console or from the
  `describe-replication-group` API.

**For CMD clusters with Automatic Failover enabled or
Automatic Failover disabled**

When replication group is set to ‘transit encryption mode:
preferred’:

- The original primary endpoint and reader endpoint for non-TLS
  enabled cluster will remain active.
- New TLS primary and reader endpoints will be generated when
  cluster is set to TLS `Preferred` mode. This new
  endpoints will resolve to the same IP(s) as the old ones
  (non-TLS).
- The new primary endpoint and reader endpoint will be exposed in
  the ElastiCache Console and in the response to the
  `describe-replication-group` API.

When replication group is set to ‘transit encryption mode:
required’:

- Old non-TLS primary and reader endpoints will be deleted. There
  will be no downtime of TLS cluster endpoints.
- You can retrieve new primary and reader endpoints from ElastiCache
  Console or from the `describe-replication-group`
  API.

### The suggested

usage of the DNS records

**For CME clusters**

- Use the cluster configuration endpoint instead of per-node DNS records in your application’s code. Using per-node DNS names directly is not recommended because during migration they will change and the application code will break connection to the cluster.
- Don't hardcode a cluster configuration endpoint in your application,
  as it will change during this process.
- Having the cluster configuration endpoint hardcoded in your application
  is a bad practice, since it can be changed during this process. After the
  in-transit encryption is completed, query the cluster configuration
  endpoint with the `describe-replication-group` API
  (as demonstrated above (in bold)) and use the DNS you get in response from that
  point on.

**For CMD clusters with Automatic Failover enabled**

- Use the primary endpoint and reader endpoint instead of the
  per-node DNS names in your application’s code since the old per-node
  DNS names are deleted and new ones are generated when migrating the
  cluster from no-TLS to TLS-preferred. Using per-node DNS names
  directly is not recommended because you might add replicas to your
  cluster in the future. Also, when Automatic Failover is enabled, the
  roles of the primary cluster and replicas are changed automatically
  by the ElastiCache service, using the primary endpoint and reader
  endpoint is suggested to help you keep track of those changes.
  Lastly, using the reader endpoint will help you distribute your
  reads from the replicas equally between the replicas in the
  cluster.
- Having the primary endpoint and reader endpoint hardcoded in your
  application is a bad practice since it can be changed during the TLS
  migration process. After the migration change to TLS-preferred is
  completed, query the primary endpoint and reader endpoint endpoint
  with the describe-replication-group API and use the DNS you get in
  response from this point on. This way you will be able to keep track
  of changes in endpoints in a dynamic way.

**For CMD cluster with Automatic Failover disabled**

- Use the primary endpoint and reader endpoint instead of the
  per-node DNS names in your application’s code. When Automatic
  Failover is disabled, scaling, patching, failover, and other
  procedures that are managed automatically by the ElastiCache service
  when Automatic Failover is enabled are done by you instead. This
  makes it easier for you to manually keep track of the different
  endpoints. Since the old per-node DNS names are deleted and new ones
  are generated when migrating the cluster from no-TLS to
  TLS-preferred, do not use the per-node DNS names directly. This is
  mandatory so that clients will be able to connect to the cluster
  during the TLS-migration. Also, you’ll benefit from evenly spreading
  the reads between the replicas when using the reader endpoint and
  keep track of the DNS-records when adding or deleting replicas form
  the cluster.
- Having the cluster configuration endpoint hardcoded in your
  application is a bad practice since it can be changed during the TLS
  migration process.

## During the in-transit

encryption: pay attention to when the migration process finishes

Change of transit encryption mode is not immediate and can take some time.
This is especially true for large clusters. Only when the cluster finishes the
migration to TLS-preferred is it able to accept and serve both TCP and TLS
connections. Therefore, you should not create clients that will try to establish
TLS connections to the cluster until the in-transit encryption is
completed.

There are several ways to get notified when the in-transit encryption is
completed successfully or failed: (Not shown in the code example above):

- Using the SNS service to get a notification when the encryption is
  completed
- Using the `describe-events` API that will emit an event
  when the encryption is completed
- Seeing a message in the ElastiCache Console that the encryption is
  completed

You can also implement logic in your application to know if the encryption is
completed. In the example above, we saw several ways to ensure the cluster
finishes the migration:

- Waiting until the migration process starts (the cluster status changes
  to “modifying“), and waiting until the modification is finished (the
  cluster status changes back to “available“)
- Asserting that the cluster has `transit_encryption_enabled`
  set to True by querying the `describe-replication-group`
  API.

### After enabling

in-transit encryption: make sure the clients you use are configured
properly

While the cluster is in TLS-preferred mode, your application should open
TLS connections to the cluster and only use those connections. This way your
application will not experience downtime when enabling in-transit
encryption. You can make sure that there are no clearer TCP connections to
the Valkey or Redis OSS engine using the info command under the SSL section.

```
# SSL
ssl_enabled:yes
ssl_current_certificate_not_before_date:Mar 20 23:27:07 2017 GMT
ssl_current_certificate_not_after_date:Feb 24 23:27:07 2117 GMT
ssl_current_certificate_serial:D8C7DEA91E684163
tls_mode_connected_tcp_clients:0   (should be zero)
tls_mode_connected_tls_clients:100
```
