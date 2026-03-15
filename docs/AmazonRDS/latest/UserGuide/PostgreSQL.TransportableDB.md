# Transportable databases parameter reference

Several parameters control the behavior of the `pg_transport` extension.
Following, you can find descriptions of these parameters.

**`pg_transport.num_workers`**

The number of workers to use for the transport process. The default
is 3. Valid values are 1–32. Even the largest database transports typically
require fewer than 8 workers. The value of this setting on the destination DB instance
is used by both destination and source during transport.

**`pg_transport.timing`**

Specifies whether to report timing information during the transport.
The default is `true`, meaning that timing information
is reported. We recommend that you leave this parameter set to
`true` so you can monitor
progress. For example output, see [Transporting a PostgreSQL database to the destination from the source](PostgreSQL.TransportableDB.md "PostgreSQL.TransportableDB.md").

**`pg_transport.work_mem`**

The maximum amount of memory to allocate for each worker. The
default is 131072 kilobytes (KB) or 262144 KB (256 MB), depending on the
PostgreSQL version. The minimum value is 64 megabytes
(65536 KB). Valid values are in kilobytes (KBs) as binary base-2
units, where 1 KB = 1024 bytes.

The transport might use less memory than is specified in this
parameter. Even large database transports typically require less
than 256 MB (262144 KB) of memory per worker.
