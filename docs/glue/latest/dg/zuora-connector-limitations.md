

# Limitations and notes for the Zuora connector
<a name="zuora-connector-limitations"></a>

The following are limitations and notes for the Zuora connector:
+ Zuora is supported as a source only. Writing to Zuora is not supported.
+ Some columns contain nested Zuora objects as serialized JSON strings: `productRatePlans` in `catalog-products`, `fileIds` in `accounting-periods`, and `invoice`, `creditMemo`, and `debitMemo` in `sequence-sets`. Parse these columns in your ETL job to read their members.
+ Job bookmarks are not supported.