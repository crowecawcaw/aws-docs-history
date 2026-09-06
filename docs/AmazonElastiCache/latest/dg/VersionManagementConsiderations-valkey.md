

# Major version behavior and compatibility differences for Valkey
<a name="VersionManagementConsiderations-valkey"></a>

When upgrading to a new major Valkey version, review the following behavior changes that may affect your applications.

## Valkey 9.1
<a name="VersionManagementConsiderations-valkey-9.1"></a>

Valkey 9.1 introduces the following potentially breaking behavior change compared to Valkey 9.0:
+ `CLUSTER SHARDS` and `CLUSTER SLOTS` responses include a new availability-zone field per node. Clients that strictly parse these responses (like older go-redis versions) might reject the unexpected field. Most clients handle unknown fields gracefully. A fix has been provided for go-redis.

For more information on the Valkey 9.1 release, see the [Valkey 9.1 release notes](https://github.com/valkey-io/valkey/releases/tag/9.1.0).

## Valkey 9.0
<a name="VersionManagementConsiderations-valkey-9.0"></a>

Valkey 9.0 introduces the following potentially breaking behavior changes compared to Valkey 8.x:
+ Authentication checks run before command validation. Unauthenticated clients now get auth errors instead of "unknown command." ([\#1475](https://github.com/valkey-io/valkey/pull/1475))
+ Error messages in transactions include full command name (e.g., `CLIENT SETNAME` instead of `client`). ([\#2286](https://github.com/valkey-io/valkey/pull/2286))
+ `GEOSEARCH` shape error message now says "BYRADIUS, BYBOX and BYPOLYGON." ([\#1809](https://github.com/valkey-io/valkey/pull/1809))

For more information on the Valkey 9.0 release, see the [Valkey 9.0 release notes](https://github.com/valkey-io/valkey/blob/9.0/00-RELEASENOTES).

## Valkey 8.1
<a name="VersionManagementConsiderations-valkey-8.1"></a>

Valkey 8.1 introduces zero potentially breaking behavior changes compared to Valkey 8.0.

For more information on the Valkey 8.1 release, see the [Valkey 8.1 release notes](https://github.com/valkey-io/valkey/releases/tag/8.1.0).

## Valkey 8.0
<a name="VersionManagementConsiderations-valkey-8.0"></a>

Valkey 8.0 introduces the following potentially breaking behavior changes compared to Valkey 7.2:
+ Nested `MULTI` or `WATCH` inside a transaction now aborts the transaction. Previously silently ignored. ([\#723](https://github.com/valkey-io/valkey/pull/723))
+ `SCAN` no longer returns lazily expired keys. ([\#501](https://github.com/valkey-io/valkey/pull/501))
+ `BITCOUNT` and `BITPOS` return errors instead of zero for invalid arguments on non-existing keys. ([Redis\#11734](https://github.com/redis/redis/pull/11734))
+ Default `repl-backlog-size` increased 1 MB → 10 MB. ([\#911](https://github.com/valkey-io/valkey/pull/911))
+ Streams use 8 extra bytes per entry. ([\#688](https://github.com/valkey-io/valkey/pull/688))
+ Error messages no longer include "Redis" branding. ([\#206](https://github.com/valkey-io/valkey/pull/206))

For more information on the Valkey 8.0 release, see the [Valkey 8.0 release notes](https://github.com/valkey-io/valkey/releases/tag/8.0.0-rc1).

## Valkey 7.2
<a name="VersionManagementConsiderations-valkey-7.2"></a>

Valkey 7.2.6 has similar compatibility differences with previous versions of Redis OSS 7.2.4. Here are the potentially breaking behavior changes between Valkey 7.2 and Redis OSS 7.1 (or 7.0):
+ Freeze time sampling occurs during command execution and in scripts.
+ A blocked stream command that's released when key no longer exists carries a different error code (-NOGROUP or -WRONGTYPE instead of -UNBLOCKED).
+ Client side tracking for scripts now tracks the keys that are read by the script, instead of the keys that are declared by the caller of EVAL / FCALL.

For more information on the Valkey 7.2 release, see [Redis OSS 7.2.4 Release Notes](https://github.com/valkey-io/valkey/blob/d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7/00-RELEASENOTES) (Valkey 7.2 includes all changes from Redis OSS up to version 7.2.4) and [Valkey 7.2 release notes](https://github.com/valkey-io/valkey/blob/7.2/00-RELEASENOTES) at Valkey on GitHub.