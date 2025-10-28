# aurora_stat_optimized_reads_cache

This function shows tiered cache stats.

## Syntax

```
aurora_stat_optimized_reads_cache()
```

## Arguments

None

## Return type

SETOF record with the following columns:

- `total_size` – Total optimized reads cache size.
- `used_size` – Used page size in optimized reads cache.

## Usage notes

This function is available in the following Aurora PostgreSQL versions:

- 15.4 and higher 15 versions
- 14.9 and higher 14 versions

## Examples

The following example shows the output on a r6gd.8xlarge instance :

```
`=>` `select pg_size_pretty(total_size) as total_size, pg_size_pretty(used_size)
 as used_size from aurora_stat_optimized_reads_cache();` `total_size | used_size
-----------+-----------
1054 GB | 975 GB`
```
