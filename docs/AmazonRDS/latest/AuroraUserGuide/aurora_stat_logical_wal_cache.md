# aurora_stat_logical_wal_cache

Shows logical write-ahead log (WAL) cache usage per slot.

## Syntax

```
SELECT * FROM aurora_stat_logical_wal_cache()
```

## Arguments

None

## Return type

SETOF record with the following columns:

- `name` – The name of the replication slot.
- `active_pid` – ID of the walsender process.
- `cache_hit` – The total number of wal cache hits since
  last reset.
- `cache_miss` – The total number of wal cache misses
  since last reset.
- `blks_read` – The total number of wal cache read
  requests.
- `hit_rate` – The WAL cache hit rate (cache_hit /
  blks_read).
- `last_reset_timestamp` – Last time that the counter was
  reset.

## Usage notes

This function is available for the following Aurora PostgreSQL versions.

- 15.2 and all higher versions
- 14.7 and higher versions
- 13.8 and higher versions
- 12.12 and higher versions
- 11.17 and higher versions

## Examples

The following example shows two replication slots with only one active.
`aurora_stat_logical_wal_cache` function.

```
`=>` `SELECT *
 FROM aurora_stat_logical_wal_cache();`
 `name | active_pid | cache_hit | cache_miss | blks_read | hit_rate | last_reset_timestamp
------------+------------+-----------+------------+-----------+----------+-------------------------------
 test_slot1 | 79183 | 24 | 0 | 24 | 100.00% | 2022-08-05 17:39:56.830635+00
 test_slot2 | | 1 | 0 | 1 | 100.00% | 2022-08-05 17:34:04.036795+00
(2 rows)`
```
