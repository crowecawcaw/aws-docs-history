# Major engine version behavior and compatibility differences with Redis OSS

###### Important

The following page is structured to signify all incompability differences between
versions and inform you of any considerations you should make when upgrading to
newer versions. This list is inclusive of any version incompability issues you may
encounter when upgrading.

You can upgrade directly from your current Redis OSS version to the latest Redis OSS version available, without the need for sequential upgrades. For example, you can
upgrade directly from Redis OSS version 3.0 to version 7.0.

Redis OSS versions are identified with a semantic version which comprise a major, minor,
and patch component. For example, in Redis OSS 4.0.10, the major version is 4, the minor
version 0, and the patch version is 10. These values are generally incremented based off
the following conventions:

- Major versions are for API incompatible changes
- Minor versions are for new functionality added in a backwards-compatible
  way
- Patch versions are for backwards-compatible bug fixes and non-functional
  changes
  We recommend always staying on the latest patch version within a given **major.minor**
  version in order to have the latest performance and stability improvements. Beginning with ElastiCache version 6.0 for Redis OSS, ElastiCache will offer a single version for
  each Redis OSS minor release rather than offering multiple patch versions. ElastiCache
  will automatically manage the patch version of your running clusters, ensuring
  improved performance and enhanced security.

We also recommend periodically upgrading to the latest major version, since most major
improvements are not back ported to older versions. As ElastiCache expands availability to a
new AWS region, ElastiCache for Redis OSS supports the two most recent **major.minor** versions at that time
for the new region. For example, if a new AWS region launches and the latest
major.minor ElastiCache versions for Redis OSS are **7.0** and **6.2**, ElastiCache will support Redis OSS versions **7.0** and **6.2** in
the new AWS region. As newer major.minor versions of ElastiCache for Redis OSS are released, ElastiCache will
continue to add support for the newly released versions. To learn more about
choosing regions for ElastiCache, see [Choosing regions and
availability zones](../red-ug/RegionsAndAZs.md#SupportedRegions "../red-ug/RegionsAndAZs.md#SupportedRegions").

When doing an upgrade that spans major or minor versions, please consider the
following list which includes behavior and backwards incompatible changes released with
Redis OSS over time.

## Redis OSS 7.0 behavior and backwards incompatible changes

For a full list of changes, see [Redis OSS 7.0 release notes](https://raw.githubusercontent.com/redis/redis/7.0/00-RELEASENOTES "https://raw.githubusercontent.com/redis/redis/7.0/00-RELEASENOTES").

- `SCRIPT LOAD` and `SCRIPT FLUSH` are no longer
  propagated to replicas. If you need to have some durability for scripts, we
  recommend you consider using [Redis OSS functions](https://valkey.io/topics/functions-intro/ "https://valkey.io/topics/functions-intro/").
- Pubsub channels are now blocked by default for new ACL users.
- `STRALGO` command was replaced with the `LCS`
  command.
- The format for `ACL GETUSER` has changed so that all fields
  show the standard access string pattern. If you had automation using
  `ACL GETUSER`, you should verify that it will handle either
  format.
- The ACL categories for `SELECT`, `WAIT`,
  `ROLE`, `LASTSAVE`, `READONLY`,
  `READWRITE`, and `ASKING` have changed.
- The `INFO` command now shows command stats per sub-command
  instead of in the top level container commands.
- The return values of `LPOP`, `RPOP`,
  `ZPOPMIN` and `ZPOPMAX` commands have changed
  under certain edge cases. If you use these commands, you should check the
  release notes and evaluate if you are impacted.
- The `SORT` and `SORT_RO` commands now require access
  to the entire keyspace in order to use the `GET` and
  `BY` arguments.

## Redis OSS 6.2 behavior and backwards incompatible changes

For a full list of changes, see [Redis OSS 6.2 release notes](https://raw.githubusercontent.com/redis/redis/6.2/00-RELEASENOTES "https://raw.githubusercontent.com/redis/redis/6.2/00-RELEASENOTES").

- The ACL flags of the `TIME`, `ECHO`,
  `ROLE`, and `LASTSAVE` commands were changed. This
  may cause commands that were previously allowed to be rejected and vice
  versa.

###### Note

None of these commands modify or give access to data.

- When upgrading from Redis OSS 6.0, the ordering of key/value pairs returned
  from a map response to a lua script are changed. If your scripts use
  `redis.setresp()` or return a map (new in Redis OSS 6.0),
  consider the implications that the script may break on upgrades.

## Redis OSS 6.0 behavior and backwards incompatible changes

For a full list of changes, see [Redis OSS 6.0 release notes](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES "https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES").

- The maximum number of allowed databases has been decreased from 1.2
  million to 10 thousand. The default value is 16, and we discourage using
  values much larger than this as we’ve found performance and memory
  concerns.
- Set `AutoMinorVersionUpgrade` parameter to yes, and ElastiCache will
  manage the minor version upgrade through self-service updates. This will be
  handled through standard customer-notification channels via a self-service
  update campaign. For more information, see [Self-service updates in ElastiCache](Self-Service-Updates.md "Self-Service-Updates.md").

## Redis OSS 5.0 behavior and backwards incompatible changes

For a full list of changes, see [Redis OSS 5.0 release notes](https://raw.githubusercontent.com/redis/redis/5.0/00-RELEASENOTES "https://raw.githubusercontent.com/redis/redis/5.0/00-RELEASENOTES").

- Scripts are by replicated by effects instead of re-executing the script on
  the replica. This generally improves performance but may increase the amount
  of data replicated between primaries and replicas. There is an option to
  revert back to the previous behavior that is only available in ElastiCache version
  5.0 for Redis OSS.
- If you are upgrading from Redis OSS 4.0, some commands in LUA scripts will
  return arguments in a different order than they did in earlier versions. In
  Redis OSS 4.0, Redis OSS would order some responses lexographically in order to make
  the responses deterministic, this ordering is not applied when scripts are
  replicated by effects.
- In Redis OSS 5.0.3 and above, ElastiCache for Redis OSS will offload some IO work to background
  cores on instance types with more than 4 VCPUs. This may change the
  performance characteristics Redis OSS and change the values of some metrics. For
  more information, see [Which Metrics Should I Monitor?](CacheMetrics.md "CacheMetrics.md") to understand if you
  need to change which metrics you watch.

## Redis OSS 4.0 behavior and backwards incompatible changes

For a full list of changes, see [Redis OSS 4.0 release notes](https://raw.githubusercontent.com/redis/redis/4.0/00-RELEASENOTES "https://raw.githubusercontent.com/redis/redis/4.0/00-RELEASENOTES").

- Slow log now logs an additional two arguments, the client name and
  address. This change should be backwards compatible unless you are
  explicitly relying on each slow log entry containing 3 values.
- The `CLUSTER NODES` command now returns a slight different
  format, which is not backwards compatible. We recommend that clients don’t
  use this command for learning about the nodes present in a cluster, and
  instead they should use `CLUSTER SLOTS`.

## Past EOL

### Redis OSS 3.2 behavior and backwards incompatible changes

For a full list of changes, see [Redis OSS 3.2 release notes](https://raw.githubusercontent.com/redis/redis/3.2/00-RELEASENOTES "https://raw.githubusercontent.com/redis/redis/3.2/00-RELEASENOTES").

- There are no compatibility changes to call out for this
  version.

For more information, see [ElastiCache versions for Redis OSS end of life schedule](engine-versions.md#deprecated-engine-versions "engine-versions.md#deprecated-engine-versions").

### Redis OSS 2.8 behavior and backwards incompatible changes

For a full list of changes, see [Redis OSS 2.8 release notes](https://raw.githubusercontent.com/redis/redis/2.8/00-RELEASENOTES "https://raw.githubusercontent.com/redis/redis/2.8/00-RELEASENOTES").

- Starting in Redis OSS 2.8.22, Redis OSS AOF is no longer supported in ElastiCache for Redis OSS.
  We recommend using MemoryDB when data needs to be persisted durably.
- Starting in Redis OSS 2.8.22, ElastiCache for Redis OSS no longer supports attaching replicas
  to primaries hosted within ElastiCache. While upgrading, external
  replicas will be disconnected and they will be unable to reconnect. We
  recommend using client-side caching, made available in Redis OSS 6.0 as an
  alternative to external replicas.
- The `TTL` and `PTTL` commands now return -2 if
  the key does not exist and -1 if it exists but has no associated expire.
  Redis OSS 2.6 and previous versions used to return -1 for both the
  conditions.
- `SORT` with `ALPHA` now sorts according to local
  collation locale if no `STORE` option is used.

For more information, see [ElastiCache versions for Redis OSS end of life schedule](engine-versions.md#deprecated-engine-versions "engine-versions.md#deprecated-engine-versions").
