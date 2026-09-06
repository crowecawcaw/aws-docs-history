

# Using shared plan cache
<a name="apg-shared-plan-cache"></a>

## Overview
<a name="apg-shared-plan-cache-overview"></a>

Aurora PostgreSQL uses a process-per-user model where each client connection creates a dedicated backend process. Each backend process maintains its own local plan cache for prepared statements. Because these caches can't be shared between processes, applications that use many prepared statements might create duplicate caches across different backend processes, which leads to increased memory usage.

Aurora PostgreSQL versions 17.6 and later and 16.10 and later introduce shared plan cache functionality. When you enable this feature, backend processes can share generic plans, which reduces memory usage and improves performance by eliminating duplicate plan generation.

**Note**  
Babelfish for Aurora PostgreSQL supports shared plan cache starting from versions 4.10 and 5.6.

The shared plan cache uses the following components as its cache key:
+ Query string (including comments)
+ Planner-related GUC parameters (including `search_path`)
+ User ID
+ Database ID

Instance restarts reset the shared cache.

## Parameters
<a name="apg-shared-plan-cache-parameters"></a>

The following table describes the parameters that control the shared plan cache feature:


| Parameter | Description | Default | Allowed | 
| --- | --- | --- | --- | 
| apg\_shared\_plan\_cache.enable | Turns shared plan cache on or off | 0 (OFF) | 0, 1 | 
| apg\_shared\_plan\_cache.max | The maximum number of cache entries | 200–1000 (instance size dependent) | 100–50000 | 
| apg\_shared\_plan\_cache.min\_size\_per\_entry | The minimum plan size to store in shared cache. Smaller plans use local cache to optimize OLTP performance. | 16 KB | 0–32768 (KB) | 
| apg\_shared\_plan\_cache.max\_size\_per\_entry | The maximum plan size for shared cache. Larger plans store only cost information. | 256 KB–4 MB (instance size dependent) | 0–32768 (KB) | 
| apg\_shared\_plan\_cache.idle\_generic\_plan\_release\_timeout | The time after which idle sessions release local generic plans. Lower values save memory; higher values might improve performance. | 10 seconds | 0–2147483647 (ms) | 

**Note**  
You can modify all parameters without restarting.

## Monitoring views and functions
<a name="apg-shared-plan-cache-monitoring"></a>
+ `apg_shared_plan_cache()` – Shows detailed cache entry information (hits, validity, timestamps)
+ `apg_shared_plan_cache_stat()` – Displays instance-level statistics (evictions, invalidations)
+ `apg_shared_plan_cache_reset()` – Removes all entries in `apg_shared_plan_cache()` and `apg_shared_plan_cache_stat()`
+ `apg_shared_plan_cache_remove(cache_key)` – Removes an entry from `apg_shared_plan_cache()` where the entry matches the `cache_key`

## Limitations
<a name="apg-shared-plan-cache-limitations"></a>
+ Only works with prepared statements and doesn't cache PL/pgSQL statements
+ Doesn't cache a query that contains temporary tables or catalog tables
+ Doesn't cache a query that depends on RLS (Row-Level Security)
+ Each replica maintains its own cache (no cross-replica sharing)