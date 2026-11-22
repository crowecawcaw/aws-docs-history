

# Query status and billing

After you start a query with `StartTelemetryQuery`, call `GetTelemetryQueryResults` to read its status and results. For information about query limits, including the query timeout, see [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md). The `status` field in the response has one of the following values.


| Status | Meaning | Rows returned | Billed | 
| --- | --- | --- | --- | 
| Running | The query is still running. Call GetTelemetryQueryResults again. | None yet | Not yet | 
| Complete | The query finished. | All result rows, in pages. Use nextToken to get the next page. | Yes, for the data scanned | 
| Cancelled | You stopped the query with StopTelemetryQuery, or it reached the query timeout. | None | Yes, for the data scanned before it stopped | 
| Failed | The query ended with an error or stopped unexpectedly. | None | No | 

The `statistics` object in the response includes the following fields.
+ `percentComplete` – The progress of the query while it runs, when that value is available.
+ `bytesScanned` – The amount of data the query scanned. The billed amount can be slightly higher, most often for a cancelled query.

A cancelled query does not return rows, even when its statistics show matched records.

`EXPLAIN (ANALYZE_FIELDS)` and `EXPLAIN (ESTIMATE)` queries are not billed.