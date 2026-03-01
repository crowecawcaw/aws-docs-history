# Major engine version behavior and compatibility differences with Valkey

Valkey 7.2.6 has similar compatibility differences with previous versions of Redis OSS 7.2.4. For the most recent supported version of Valkey, see [Supported engines and versions](VersionManagement.md#supported-engine-versions "VersionManagement.md#supported-engine-versions").

For more information on the Valkey 7.2 release, see [Redis OSS 7.2.4 Release Notes](https://github.com/valkey-io/valkey/blob/d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7/00-RELEASENOTES") (Valkey 7.2 includes all changes from Redis OSS up to version 7.2.4) and [Valkey 7.2 release notes](https://github.com/valkey-io/valkey/blob/7.2/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/7.2/00-RELEASENOTES") at Valkey on GitHub.

Here are the potentially breaking behavior changes between Valkey 7.2 and Redis OSS 7.1 (or 7.0):

- Freeze time sampling occurs during command execution and in scripts.
- A blocked stream command that's released when key no longer exists carries a different error code (-NOGROUP or -WRONGTYPE instead of -UNBLOCKED).
- Client side tracking for scripts now tracks the keys that are read by the
  script, instead of the keys that are declared by the caller of EVAL / FCALL.
