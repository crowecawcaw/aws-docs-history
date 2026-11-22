

# Get top network paths

To get the top network paths for a monitor, start a `TOP_PATHS` query, check its status, and then retrieve the results. The following `start-query-performance-monitor` example starts a query and returns a query ID.

```
aws networkflowmonitor start-query-performance-monitor \
    --monitor-name production-vpc-monitor \
    --query-type TOP_PATHS \
    --start-time 2026-07-01T00:00:00Z \
    --end-time 2026-07-01T01:00:00Z
```

The following `get-query-status-performance-monitor` example checks the status of the query.

```
aws networkflowmonitor get-query-status-performance-monitor \
    --monitor-name production-vpc-monitor \
    --query-id {{query-id}}
```

The following `get-query-results-performance-monitor` example retrieves the results of the query. Results are returned as a set of fields (columns) and rows of data.

```
aws networkflowmonitor get-query-results-performance-monitor \
    --monitor-name production-vpc-monitor \
    --query-id {{query-id}}
```