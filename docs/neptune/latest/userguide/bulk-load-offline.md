

# Fast bulk load (offline loader)
<a name="bulk-load-offline"></a>

The Amazon Neptune offline loader is a high-performance variant of the standard bulk loader. Use it for initial loads of large Gremlin CSV datasets. The loader reads files from Amazon Simple Storage Service and builds graph index structures directly on the instance. When the load completes, Neptune swaps the new indexes into place atomically. Because it bypasses the per-row transactional write path, it loads large datasets significantly faster than the standard bulk loader.

## When to use the offline loader
<a name="bulk-load-offline-when"></a>

Use the offline loader when *all* of the following are true:
+ You are loading Gremlin CSV data.
+ The target graph is empty, or you are willing to reset the graph entirely before loading.
+ The dataset is large enough that load throughput matters more than incremental write availability.
+ Your source data is clean. The offline loader fails the entire load on any referential or cardinality violation.
+ You can accept that Neptune blocks read and write queries for the duration of the load.

Use the [standard bulk loader](bulk-load.md) when any of the following apply:
+ You are loading RDF, openCypher, or geospatial data.
+ You need to append to an existing, non-empty graph.
+ You need to resume a previously failed load (`mode=RESUME`).
+ You need to queue multiple load jobs (`queueRequest=TRUE`).
+ You need to overwrite single-cardinality property values (`updateSingleCardinalityProperties=TRUE`).
+ Your source data might contain errors (for example, duplicate edge IDs or missing vertex references) and you want those rows skipped rather than treated as fatal.

## Prerequisites and limitations
<a name="bulk-load-offline-prerequisites"></a>

### Engine version
<a name="bulk-load-offline-engine-version"></a>

The offline loader requires Neptune engine version 1.5.0.0 or later.

### Instance requirements
<a name="bulk-load-offline-instance-requirements"></a>

The offline loader has the following instance requirements:
+ Use provisioned instances only. The offline loader does not support serverless instances.
+ Use a large instance type (for example, `db.r6i.12xlarge` or larger) to avoid out-of-memory failures. The offline loader uses all available vCPUs and memory on the instance.
+ Use [Neptune I/O-Optimized storage](https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html#provisioned-iops-storage) for better cost efficiency on large loads.

### Limitations
<a name="bulk-load-offline-limitations"></a>

The offline loader has the following limitations:
+ **Gremlin CSV only** – The offline loader supports only Gremlin CSV format. It does not support openCypher, RDF, or geospatial formats.
+ **No compressed files** – The offline loader does not support compressed source files. Provide uncompressed Gremlin CSV files.
+ **Empty graph required** – The target graph must be empty. Use `fast reset` to clear the graph before loading.
+ **One load at a time** – Only one offline load can run per cluster. Neptune rejects concurrent load requests.
+ **No resume** – You cannot resume a failed load. Reset the graph and restart the load from the beginning.
+ **No parallelism control** – The offline loader always uses all available vCPUs. It does not support the `parallelism` parameter. Neptune rejects the request if you include it.
+ **Queries blocked** – Neptune blocks read and write queries while an offline load is in progress.
+ **All-or-nothing semantics** – Referential integrity violations, duplicate edge IDs, and single-cardinality conflicts cause the entire load to fail. Neptune retains no partial data.

## Starting an offline load
<a name="bulk-load-offline-start"></a>

Use the same `/loader` endpoint as the standard bulk loader. Add `"loadType": "offline"` to the request body to select the offline loader.

The following example shows a request:

```
POST https://{{your-neptune-endpoint}}:{{port}}/loader
Content-Type: application/json

{
  "source": "s3://amzn-s3-demo-bucket/{{graph-data/}}",
  "format": "csv",
  "iamRoleArn": "arn:aws:iam::{{123456789012}}:role/{{NeptuneLoadFromS3}}",
  "region": "{{us-west-2}}",
  "loadType": "offline",
  "failOnError": "TRUE"
}
```

The offline loader supports the following parameters:
+ `source` – The Amazon S3 URI of your data files.
+ `format` – Must be `csv`.
+ `iamRoleArn` – The IAM role ARN with read access to the Amazon S3 bucket.
+ `region` – The AWS Region of the Amazon S3 bucket.
+ `loadType` – Set to `offline` to use the offline loader.
+ `failOnError` – Controls behavior on parse errors. When `TRUE`, any parse error aborts the load immediately.

The following standard loader parameters are *not* supported by the offline loader: `parallelism`, `mode`, `queueRequest`, `dependencies`, `updateSingleCardinalityProperties`, and `edgeOnlyLoad`.

The following example shows the response:

```
{
  "status": "200 OK",
  "payload": {
    "loadId": "ef478d76-d9da-4d94-8ff1-08d9d4863aa5"
  }
}
```

## Monitoring an offline load
<a name="bulk-load-offline-monitor"></a>

Use the same `GET /loader/{{loadId}}` endpoint as the standard bulk loader. While the load is in progress, the response includes an additional `progress` object that reports the current phase.

```
{
  "payload": {
    "overallStatus": {
      "status": "LOAD_IN_PROGRESS",
      "fullUri": "s3://amzn-s3-demo-bucket/graph-data/",
      "totalRecords": 1234567,
      "totalDuplicates": 0,
      "parsingErrors": 0,
      "insertErrors": 0,
      "progress": {
        "phase": "BUILDING_GRAPH",
        "phaseNumber": 3,
        "totalPhases": 5
      }
    }
  }
}
```

The `progress` object is present only while the load is in progress. Neptune removes it after the load reaches a terminal state.

### Load phases
<a name="bulk-load-offline-phases"></a>

The offline loader processes data in five sequential phases.


| Phase | Name | Description | 
| --- | --- | --- | 
| 1 | PARSING | Neptune reads source files and collects unique strings. | 
| 2 | BUILDING\_DICTIONARY | Neptune builds the sorted string-to-identifier dictionary. | 
| 3 | BUILDING\_GRAPH | Neptune reads the data again and translates rows into graph statements using the dictionary. | 
| 4 | INDEXING | Neptune sorts statements and builds the graph indexes. Referential and cardinality violations are detected during this phase. | 
| 5 | FINALIZING | Neptune atomically swaps the new indexes into place and unblocks queries. | 

All other status fields (`status`, `fullUri`, `totalRecords`, `totalDuplicates`, `parsingErrors`, `insertErrors`, and the error log available with `errors=true`) have the same meaning as in the standard loader. See [Neptune Loader Get-Status API](load-api-reference-status.md).

## How the offline loader differs from the standard loader
<a name="bulk-load-offline-comparison"></a>

The following table compares key behaviors of the offline loader and the standard bulk loader.


| Capability | Standard bulk loader | Offline loader | 
| --- | --- | --- | 
| Supported data formats | Gremlin CSV, openCypher, RDF (NTriples, NQuads, RDF/XML, Turtle) | Gremlin CSV only | 
| Target graph state | Empty or non-empty (appends) | Empty only. Reset the graph first. | 
| Concurrent loads | Up to 64 queued jobs (queueRequest=TRUE) | One load at a time per cluster | 
| Resume after failure | Yes (mode=RESUME or mode=AUTO) | Not supported. Reset the graph and restart the load. | 
| Parallelism control | User-configurable via parallelism | Not configurable. Uses all available vCPUs. | 
| Progress reporting | status only | status plus a progress object with five phases | 
| Query availability during load | You can run read and write queries throughout the load | Neptune blocks queries during the load | 
| Referential integrity | Neptune skips missing vertex references per row | The entire load fails with FROM\_OR\_TO\_VERTEX\_ARE\_MISSING | 
| Duplicate edge IDs | Neptune skips duplicates per row | The entire load fails with ID\_ASSIGNED\_TO\_MULTIPLE\_EDGES | 
| Single-cardinality conflicts | Neptune skips conflicts per row | The entire load fails with SINGLE\_CARDINALITY\_VIOLATION | 
| Post-load statistics | Available immediately after load completes | Neptune triggers statistics collection after the load completes. Statistics might take a few minutes to become available. | 

## Error handling
<a name="bulk-load-offline-errors"></a>

The offline loader uses all-or-nothing semantics. If any data integrity violation is detected during the `INDEXING` phase, the entire load fails and no data is retained. The graph returns to its pre-load state (empty).

The following errors cause the entire load to fail, regardless of the `failOnError` setting.


| Error code | Phase | Description | 
| --- | --- | --- | 
| FROM\_OR\_TO\_VERTEX\_ARE\_MISSING | INDEXING | An edge references a vertex ID that does not exist in the input data. | 
| ID\_ASSIGNED\_TO\_MULTIPLE\_EDGES | INDEXING | Two or more edges share the same edge ID. | 
| SINGLE\_CARDINALITY\_VIOLATION | INDEXING | A property declared with single cardinality has more than one value on the same vertex. | 
| PARSING\_ERROR | PARSING |  + A string property value starts with an internal namespace prefix, which the offline loader does not currently support.<br />+ A data type conversion failure, such as a non-numeric value in an `Int` column.  | 

Other parse errors (for example, a malformed CSV row or a value exceeding the 55 MB size limit) are handled according to the `failOnError` parameter:
+ `failOnError=TRUE` – Any parse error aborts the load immediately.
+ `failOnError=FALSE` – Neptune logs parse errors and skips the affected row. The load continues with remaining data.

Use `GET /loader/{{loadId}}?errors=true` to retrieve detailed error information after a failed load.

## Best practices
<a name="bulk-load-offline-best-practices"></a>
+ **Validate data before loading** – Validate your data before starting a load. The offline loader fails the entire load if it detects an integrity violation. Ensure all edge `~from` and `~to` values reference vertex IDs that exist in the input, edge IDs are unique, and single-cardinality properties have only one value per vertex.
+ **Use a large instance** – The offline loader uses all available memory and vCPUs. A larger instance (for example, `db.r6i.12xlarge` or larger) loads data faster and avoids out-of-memory failures on large datasets.
+ **Use fast reset before retrying** – If a load fails, use `fast reset` to clear the graph before retrying. The offline loader requires an empty graph.
+ **Monitor phase progression** – Poll `GET /loader/{{loadId}}` to track which of the five phases the load is in. The `INDEXING` phase is where data integrity violations are detected, so a failure in this phase indicates a data quality issue.
+ **Separate vertex and edge files** – Organize your Amazon S3 data with vertex files and edge files under separate prefixes. This makes it easier to validate referential integrity before loading.

**Note**  
For boolean property columns, the offline loader treats any value other than `true` as `false`. For more information, see [Gremlin load data formats](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html#bulk-load-tutorial-format-gremlin-datatypes).