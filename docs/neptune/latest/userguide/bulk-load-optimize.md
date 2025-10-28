# Optimizing an Amazon Neptune bulk load

Use the following strategies to keep the load time to a minimum for a Neptune
bulk load:

- **Clean your data:**
  - Be sure to convert your data into a [supported data format](bulk-load-tutorial-format.md "bulk-load-tutorial-format.md") before loading.
  - Remove any duplicates or known errors.
  - Reduce the number of unique predicates (such as properties
    of edges and vertices) as much as you can.

- **Optimize your files:**
  - If you load large files such as CSV files from an Amazon S3 bucket,
    the loader manages concurrency for you by parsing them into chunks that it
    can load in parallel. Using a very large number of tiny files can slow this
    process.
  - If you load multiple files from an Amazon S3 prefix, the loader automatically loads vertex files first,
    then edge files afterwards. However, if you know that you will only be loading edge files, `edgeOnlyLoad`
    can be set to `TRUE` to skip the first-pass where all files are scanned to determine their contents
    (vertices or edges) so that any vertex files found are loaded before any edge files. This can speed up
    the load time significantly, especially when many edge files are involved. In case some vertex files are
    also present in the same Amazon S3 prefix (`source` parameter), they will get loaded but without any ordering
    guarantees relative to other files. Also, if some `from` or `to` vertices are not present
    in the database, the edge insertion may report errors with the message
    `FROM_OR_TO_VERTEX_ARE_MISSING`. As a best practice, put nodes and edges in separate Amazon S3 prefix.

- **Check your loader settings:**
  - If you don't need to perform any other operations during the load,
    use the [OVERSUBSCRIBE
     parallelism](load-api-reference-load.md#load-api-reference-load-syntax "load-api-reference-load.md#load-api-reference-load-syntax") parameter. This parameter setting causes
    the bulk loader to use all available CPU resources when it runs. It generally
    takes 60%-70% of CPU capacity to keep the operation running as fast as
    I/O constraints permit.

  ###### Note

  When `parallelism` is set to `OVERSUBSCRIBE`
  or `HIGH` (the default setting), there is the risk when loading
  openCypher data that threads may encounter a race condition and deadlock,
  resulting in a `LOAD_DATA_DEADLOCK` error. In this case, set
  `parallelism` to a lower setting and retry the load.
  - If your load job will include multiple load requests, use the
    `queueRequest` parameter. Setting `queueRequest` to
    `TRUE` lets Neptune queue up your requests so you don't have to
    wait for one to finish before issuing another.
  - If your load requests are being queued, you can set up levels of
    dependency using the `dependencies` parameter, so that the failure
    of one job causes dependent jobs to fail. This can prevent inconsistencies in
    the loaded data.
  - If a load job is going to involve updating previously loaded
    values, be sure to set the `updateSingleCardinalityProperties` parameter
    to `TRUE`. If you don't, the loader will treat an attempt to update an
    existing single-cardinality value as an error. For Gremlin data, cardinality is
    also specified in property column headers (see [Property Column Headers](bulk-load-tutorial-format-gremlin.md#bulk-load-tutorial-format-gremlin-propheaders "bulk-load-tutorial-format-gremlin.md#bulk-load-tutorial-format-gremlin-propheaders")).

  ###### Note

  The `updateSingleCardinalityProperties` parameter is
  not available for Resource Description Framework (RDF) data.
  - You can use the `failOnError` parameter to determine
    whether bulk load operations should fail or continue when an error is encountered.
    Also, you can use the `mode` parameter to be sure that a load job
    resumes loading from the point where a previous job failed rather than reloading
    data that had already been loaded.

- **Scale up**   –  
  Set the writer instance of your DB cluster to the maximum size before
  bulk loading. Note that if you do this, you must either scale up any read-replica
  instances in the DB cluster as well, or remove them until you have finished
  loading the data.

When your bulk load is complete, be sure to scale the writer instance
down again.

###### Important

If you experience a cycle of repeated read-replica restarts because
of replication lag during a bulk load, your replicas are likely unable to keep up
with the writer in your DB cluster. Either scale the readers to be larger than the
writer, or temporarily remove them during the bulk load and then recreate them
after it completes.

See [Request Parameters](load-api-reference-load.md#load-api-reference-load-parameters "load-api-reference-load.md#load-api-reference-load-parameters") for more details about setting
loader request parameters.
