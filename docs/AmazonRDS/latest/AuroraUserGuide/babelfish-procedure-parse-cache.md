

# Using ANTLR parse cache in Babelfish
<a name="babelfish-procedure-parse-cache"></a>

Starting with Babelfish versions 5.7.0 and 6.2.0, you can use a persistent ANTLR parse result cache for T-SQL stored routines (procedures and functions) to reduce first-execution latency.

**With the procedure parse cache:**
+ Large T-SQL routines (hundreds to thousands of lines) no longer incur full T-SQL parsing overhead on the first execution in every new session.
+ The parsed result is serialized once at `CREATE`/`ALTER` procedure/function time, stored in the catalog, and reused across sessions – emulating SQL Server's system-wide caching behavior.
+ The feature is controlled by the session-level GUC `babelfishpg_tsql.enable_antlr_parse_cache`, with optional per-routine overrides via `sys.enable_antlr_parse_cache()`.
+ By default the feature is **OFF**.

**Performance:** For large routines, ANTLR parsing can take up to several seconds. With the ANTLR parse cache, first-execution parse time is reduced to a few milliseconds. Subsequent executions in the same session are served from the in-session cache (sub-millisecond) and are unaffected.

## Understanding the ANTLR parse cache
<a name="babelfish-procedure-parse-cache-overview"></a>

Babelfish must validate T-SQL syntax by parsing a routine's body the first time it runs in a session. This parse result is normally cached only for the lifetime of that session, so every new connection re-parses from scratch. The parse cache persists the parse result in the catalog so that new sessions can reuse it.

How it behaves:
+ **At `CREATE`/`ALTER`:** When caching is enabled, Babelfish parses the routine and stores the serialized parse result in the persistent cache.
+ **First execution without a persistent entry:** If no cached entry exists (for example, the routine was created before caching was enabled), Babelfish performs the normal ANTLR parse and populates the persistent cache.
+ **First execution in a later session:** Babelfish loads and deserializes the cached parse result instead of re-parsing – this is where the time savings occur.
+ **Subsequent executions in the same session:** served from the in-session cache (unchanged behavior).
+ If a cached result is missing or was created by a different Babelfish version, Babelfish performs the normal ANTLR parse and repopulates the persistent cache when caching is enabled.
+ If Babelfish encounters an error while serializing or deserializing a cached result, the statement fails and returns an error. Disable caching for the affected routine and retry the statement, or retry in a new session with the cache GUC disabled. If the error persists, contact AWS Support.

## Observing the parsing-time improvement
<a name="babelfish-procedure-parse-cache-observing"></a>

You can measure the effect using `SET BABELFISH_STATISTICS PROFILE ON`, which reports the `Babelfish T-SQL Batch Parsing Time` for each batch. First, create a large procedure with caching enabled to populate the persistent cache. Then compare the procedure's first execution in two separate new sessions: one with caching disabled, which ignores the persistent entry, and one with caching enabled, which reuses it. Alternatively, if caching was not enabled when the procedure was created, execute it in two separate new sessions with caching enabled: the first execution populates the persistent cache, and the second reuses it.

In the following example, first create the procedure with caching ON to populate the persistent cache:

```
-- New session 0: caching ON (at CREATE PROCEDURE time)
SELECT set_config('babelfishpg_tsql.enable_antlr_parse_cache', 'on', false);
GO
CREATE PROCEDURE dbo.updateInformation @region VARCHAR(50)
AS
BEGIN
    ...
END;
GO
```

Next, in a new session with caching OFF (the default), execute the procedure:

```
-- New session 1: caching OFF (default)
SET BABELFISH_STATISTICS PROFILE ON;
GO
EXEC dbo.updateInformation @region = 'EMEA';   -- first call in this session
GO
```

The statistics profile reports a high parsing time:

```
Babelfish T-SQL Batch Parsing Time: 20359.465 ms
```

Finally, in another new session with caching ON, execute the procedure:

```
-- New session 2: caching ON
SELECT set_config('babelfishpg_tsql.enable_antlr_parse_cache', 'on', false);
GO
SET BABELFISH_STATISTICS PROFILE ON;
GO
EXEC dbo.updateInformation @region = 'EMEA';   -- first call in this session
GO
```

The statistics profile reports a significantly lower parsing time:

```
Babelfish T-SQL Batch Parsing Time: 150.927 ms
```

The first execution in a new session drops from \~20 s of parsing to \~0.15 s once the cached parse tree is reused. Second and later executions within the same session are served from the in-session cache in both cases (sub-millisecond) and are unaffected by the GUC.

## Enabling the cache for a session
<a name="babelfish-procedure-parse-cache-enabling"></a>

The feature is controlled by a session-level GUC (default **OFF**):

```
-- Enable parse caching for the current session
SELECT set_config('babelfishpg_tsql.enable_antlr_parse_cache', 'on', false);
GO

-- Disable for the current session
SELECT set_config('babelfishpg_tsql.enable_antlr_parse_cache', 'off', false);
GO
```

**Note**  
The GUC is **session-scoped** and resets to the default (OFF) when the session ends.
This GUC is **not** currently configurable cluster-wide via `sp_babelfish_configure`.

## Controlling the cache per routine
<a name="babelfish-procedure-parse-cache-per-routine"></a>

You can override the session GUC for an individual routine using `sys.enable_antlr_parse_cache`, which accepts the routine's object id:

```
-- Force caching ON for a specific routine (even if the session GUC is OFF)
SELECT sys.enable_antlr_parse_cache(sys.object_id('dbo.my_proc'), true);
GO

-- Force caching OFF for a specific routine — "kill switch"
-- (clears any cached data and blocks caching even if the session GUC is ON)
SELECT sys.enable_antlr_parse_cache(sys.object_id('dbo.my_proc'), false);
GO

-- Reset to default; the routine follows the session GUC
SELECT sys.enable_antlr_parse_cache(sys.object_id('dbo.my_proc'), NULL);
GO
```

**Note**  
You must be the **owner** of the routine or a member of the **sysadmin** role to change its cache setting.
The per-routine setting persists across sessions (it is stored in the catalog) and is preserved across `ALTER`; it is removed when the routine is dropped.

## Checking cache statistics
<a name="babelfish-procedure-parse-cache-stats"></a>

`sys.antlr_parse_cache_stats()` returns parse-cache activity for the current session:

```
SELECT * FROM sys.antlr_parse_cache_stats();
GO
```

The following table describes each column in the output.


| Column | Description | 
| --- | --- | 
| cache\_hits | Count of routine executions for which a cached parse result was reused. | 
| cache\_misses | Count of routine executions for which caching was enabled but no usable cache entry was found. | 
| cache\_writes | Count of successful persistent-cache writes. | 
| cache\_evictions | Count of cached entries that were invalidated or removed (for example, kill switch or GUC toggle). | 
| cache\_errors | Count of serialization or deserialization failures. | 

Counters are per-session and reset on a new connection.

## Example scenario
<a name="babelfish-procedure-parse-cache-example"></a>

```
-- Enable caching for this session
SELECT set_config('babelfishpg_tsql.enable_antlr_parse_cache', 'on', false);
GO

CREATE PROCEDURE dbo.report_proc @region VARCHAR(50)
AS
BEGIN
    -- large multi-statement T-SQL body ...
    SELECT @region;
END;
GO

-- First execution in a brand-new session: served from the persistent cache (fast)
EXEC dbo.report_proc @region = 'APAC';
GO

-- Inspect cache activity for this session
SELECT * FROM sys.antlr_parse_cache_stats();
GO

-- Opt this routine out of caching regardless of the session setting
SELECT sys.enable_antlr_parse_cache(sys.object_id('dbo.report_proc'), false);
GO
```

## Upgrade considerations
<a name="babelfish-procedure-parse-cache-upgrade"></a>
+ The ANTLR parse cache is bound to a specific Babelfish version. When the Babelfish version changes, cached parse results are no longer reused. New executions re-parse the routine and repopulate the cache automatically when caching is enabled.
+ Existing routines created before 5.7.0 and 6.2.0 are cached on their next `CREATE`/`ALTER` or on a cold-session execution once caching is enabled.

## Important limitations
<a name="babelfish-procedure-parse-cache-limitations"></a>
+ **Default OFF:** the feature must be explicitly enabled per session (or forced per routine).
+ **Connection type:** the cache is active only for **TDS (SQL Server protocol) connections**, not for psql/libpq connections.
+ **Not cached:** **triggers, event triggers, and inline table-valued functions (ITVFs)** are not cached in this release.
+ **Cluster-wide config:** the session GUC is not currently settable via `sp_babelfish_configure`.