# Storage

Neptune supports dictionary garbage collection (GC) for property graph data, which can be enabled via the
`neptune_lab_mode` [parameter](parameters.md "parameters.md") when `neptune_streams` is not active.
When activated, this background job cleans up unused dictionary entries,
potentially reducing the rate of data growth. The feature can run in two modes: soft_delete (marking entries as
deleted without explicit removal) and enabled (explicitly deleting entries). The GC process can impact system
performance by contending with query threads for resources like CPU and buffer cache, and can run with a maximum
concurrency of 16 threads.

Neptune also supports inline server-generated edge IDs, which can be enabled through a configuration
[parameter](parameters.md "parameters.md") when
neptune_streams is not active. When this feature is enabled, the server generates unique inlined IDs for edges that do
not have a user-defined ID, using a reserved prefix of "neptune_reserved". These inlined IDs are not stored in the
dictionary, which can improve storage efficiency.

###### Topics

- [Neptune dictionary garbage collection](storage-gc.md "storage-gc.md")
- [Neptune inlined server-generated edge ID](storage-edge-id.md "storage-edge-id.md")
