# Query Apache Hudi datasets

[_Apache Hudi_](https://hudi.incubator.apache.org/ "https://hudi.incubator.apache.org/")
is an open-source data management framework that simplifies incremental data processing.
Record-level insert, update, upsert, and delete actions are processed much more granularly,
reducing overhead. `Upsert` refers to the ability to insert records into an
existing dataset if they do not already exist or to update them if they do.

Hudi handles data insertion and update events without creating many small files that can
cause performance issues for analytics. Apache Hudi automatically tracks changes and merges
files so that they remain optimally sized. This avoids the need to build custom solutions
that monitor and re-write many small files into fewer large files.

Hudi datasets are suitable for the following use cases:

- Complying with privacy regulations like [General
  data protection regulation](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation "https://en.wikipedia.org/wiki/General_Data_Protection_Regulation") (GDPR) and [California
  consumer privacy act](https://en.wikipedia.org/wiki/California_Consumer_Privacy_Act "https://en.wikipedia.org/wiki/California_Consumer_Privacy_Act") (CCPA) that enforce people's right to remove
  personal information or change how their data is used.
- Working with streaming data from sensors and other Internet of Things (IoT)
  devices that require specific data insertion and update events.
- Implementing a [change data capture (CDC) system](https://en.wikipedia.org/wiki/Change_data_capture "https://en.wikipedia.org/wiki/Change_data_capture").
  Data sets managed by Hudi are stored in Amazon S3 using open storage formats. Currently, Athena
  can read compacted Hudi datasets but not write Hudi data. Athena supports Hudi version 0.14.0 with Athena engine version 3. This is subject to change. Athena
  cannot guarantee read compatibility with tables that are created with later versions of
  Hudi. For information about Athena engine versioning, see [Athena engine versioning](engine-versions.md "engine-versions.md"). For more information about Hudi features and
  versioning, see the [Hudi
  documentation](https://hudi.apache.org/docs/overview "https://hudi.apache.org/docs/overview") on the Apache website.

A Hudi dataset can be one of the following types:

- **Copy on Write (CoW)** – Data is stored in a columnar
  format (Parquet), and each update creates a new version of files during a
  write.
- **Merge on Read (MoR)** – Data is stored using a
  combination of columnar (Parquet) and row-based (Avro) formats. Updates are logged
  to row-based `delta` files and are compacted as needed to create new
  versions of the columnar files.
  With CoW datasets, each time there is an update to a record, the file that contains the
  record is rewritten with the updated values. With a MoR dataset, each time there is an
  update, Hudi writes only the row for the changed record. MoR is better suited for write- or
  change-heavy workloads with fewer reads. CoW is better suited for read-heavy workloads on
  data that change less frequently.

Hudi provides three query types for accessing the data:

- Snapshot queries – Queries that see the
  latest snapshot of the table as of a given commit or compaction action. For MoR
  tables, snapshot queries expose the most recent state of the table by merging the
  base and delta files of the latest file slice at the time of the query.
- Incremental queries – Queries only see new
  data written to the table, since a given commit/compaction. This effectively
  provides change streams to enable incremental data pipelines.
- Read optimized queries – For MoR tables,
  queries see the latest data compacted. For CoW tables, queries see the latest data
  committed.
  The following table shows the possible Hudi query types for each table type.

| Table type                                  | Possible Hudi query types             |
| ------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Copy On Write                               | snapshot, incremental                 |
| Merge On Read                               | snapshot, incremental, read optimized | Currently, Athena supports snapshot queries and read optimized queries, but not incremental queries. On MoR tables, all data exposed to read optimized queries are compacted. This provides good performance but does not include the latest delta commits. Snapshot queries contain the freshest data but incur some computational overhead, which makes these queries less performant. For more information about the tradeoffs between table and query types, see [Table & Query Types](https://hudi.apache.org/docs/table_types/ "https://hudi.apache.org/docs/table_types/") in the Apache Hudi documentation. ## Hudi terminology change: Views are now queries Starting in Apache Hudi release version 0.5.1, what were formerly called views are now called queries. The following table summarizes the changes between the old and new terms. |
| Old term                                    | New term                              |
| ---                                         | ---                                   |
| CoW: read optimized view MoR: realtime view | Snapshot queries                      |
| Incremental view                            | Incremental query                     |
| MoR read optimized view                     | Read optimized query                  | ###### Topics <br>• [Considerations and limitations](querying-hudi-in-athena-considerations-and-limitations.md "querying-hudi-in-athena-considerations-and-limitations.md") <br>• [Copy on write (CoW) create table examples](querying-hudi-copy-on-write-create-table-examples.md "querying-hudi-copy-on-write-create-table-examples.md") <br>• [Merge on read (MoR) create table examples](querying-hudi-merge-on-read-create-table-examples.md "querying-hudi-merge-on-read-create-table-examples.md") <br>• [Use Hudi metadata for improved performance](querying-hudi-metadata-table.md "querying-hudi-metadata-table.md") <br>• [Additional resources](querying-hudi-additional-resources.md "querying-hudi-additional-resources.md")                                                                                                            |
