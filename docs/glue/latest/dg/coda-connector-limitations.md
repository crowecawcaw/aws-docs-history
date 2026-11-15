

# Limitations and notes for the Coda connector
<a name="coda-connector-limitations"></a>

The following are limitations and notes for the Coda connector:
+ Coda is supported as a source only. Writing to Coda is not supported.
+ The `rows` entity returns the cell values of each row as one JSON string in the `values` field, keyed by column ID. To map column IDs to column names, read the `columns` entity for the same table.
+ Job bookmarks are not supported.