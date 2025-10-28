# Neptune dictionary garbage collection

Neptune supports dictionary garbage collection (GC) which can be enabled via the `neptune_lab_mode`
[parameter](parameters.md "parameters.md")
for property graph data. It can be enabled for clusters with only property graph data when `neptune_streams` is
not enabled. The feature is automatically disabled if `neptune_streams` is enabled or there is any unexpired
`neptune_streams` data. The feature requires a writer instance reboot to activate. This feature is available
from engine release [1.4.3.0](../../../releases/release-1.4.3.0.md "../../../releases/release-1.4.3.0.md").

When enabled, the unused dictionary entries are cleaned up by a background job. It does not reduce
`VolumeBytesUsed`, instead it frees up space in index for new inserts. The rate of growth in
`VolumeBytesUsed` is likely to be less when dictionary GC is enabled relative to when it is not.

Dictionary garbage collection runs in the background and scans all graph and dictionary data to find terms that are not
in use. A new run is triggered on start up once approximately 6% of the data has changed. It contends with query threads
for head node resources like CPU, buffer cache, undo log generation, and write I/O operations, which could negatively
impact the query throughput. Since GC scans data that is not actively touched by queries, it can impact the buffer cache
on the writer node. The cluster could see additional write I/O operations and have more undo logs to
purge as GC performs new deletes, which may also result in higher values for the `UndoLogListSize` metric.

GC can be ran in two modes, `soft_delete` and `enabled`. When ran in the `soft_delete` mode,
unused dictionary entries are marked deleted (soft_delete) but are not explicitly deleted. This mode could also be used to
understand performance characteristics after the background operation is turned on. When the enabled mode is used,
entries are explicitly deleted ('hard' delete). It is recommended to run GC in `soft_delete` mode for a
period of time before switching to `enabled` mode.

Dictionary GC supports a maximum concurrency of 16 (on machines with 16 or more cores). It runs by default with a single
thread, but it can be run with higher concurrency when enabled for the first time. Dictionary GC thread(s) run at equal
priority with the query threads, and they contend with resources on the writer equally.

Dictionary GC can be enabled via the `neptune_lab_mode`
[parameter](parameters.md "parameters.md") by setting the `DictionaryGCMode` key.
It accepts three possible values: `disabled` (default), `soft_delete`, or `enabled`. For
example, the following code sample would set the `DictionaryGCMode` to `soft_delete`:

```
neptune_lab_mode = 'DictionaryGCMode=soft_delete'
```

The concurrency
[parameter](parameters.md "parameters.md"), `DictionaryGCConcurrency`, is optional and can take a
value between 1 and 16. If set to a higher value than the minimum of 16 and number of cores, the concurrency is
capped at that value.

```
neptune_lab_mode = 'DictionaryGCMode=soft_delete,DictionaryGCConcurrency=2'
```

The dictionary GC job is enabled in the background after the server starts, once there is some data available. The engine
status displays the current status of dictionary GC. The example output shown below shows that dictionary GC is in
`soft_delete` mode and running with a concurrency of 2. If the background job is running, it could be actively
scanning for unused dictionary entries and deleting them, or waiting for new set of deletes to trigger a new round of GC.

```
{"status":"healthy",...,"labMode":{"ObjectIndex":"disabled","DictionaryGC":"{Mode=enabled,Concurrency=2}"},...}
```

Dictionary GC is paused when any of these conditions are met:

- Active bulk load.
- Freeable memory is less than 15Gb.
- `UndoLogListSize` is higher than 1,000,000.
