# Working with sequences and identity columns

This section helps you understand how best to use sequences and identity
columns based on workload patterns.

###### Important

See the Important callout on the [CREATE SEQUENCE](create-sequence-syntax-support.md "create-sequence-syntax-support.md") page for more details on allocation and
caching behavior.

## Choosing identifier types

Amazon Aurora DSQL supports both UUID-based identifiers and integer values generated using
sequences or identity columns. These options differ in how values are allocated
and how they scale under load.

UUID values can be generated without coordination and are well suited to workloads where
identifiers are created frequently or across many sessions. Because Amazon Aurora DSQL is designed for
distributed operation, avoiding coordination is often beneficial. For this reason, UUIDs are
recommended as the default identifier type, especially for primary keys in workloads where
scalability is important and strict ordering of identifiers isn't required.

Sequences and identity columns generate compact integer values that are
convenient for human-readable identifiers, reporting, and external interfaces. When numeric
identifiers are preferred for usability or integration reasons, consider using a sequence
or identity column in combination with UUID-based identifiers. When integer
sequence or identity values are required, choosing an appropriate cache size becomes an
important part of workload design. See the following section for guidance on choosing a cache
size.

## Choosing a cache size

Selecting an appropriate cache value is an important part of using sequences
and identity columns effectively. The cache setting determines how
identifier allocation behaves under load, influencing both system throughput and how closely
values reflect allocation order.

**A larger cache size of `CACHE >= 65536` is well
suited when:**

- Identifiers are generated at high frequency
- Many sessions insert concurrently
- The workload can tolerate gaps and visible ordering effects

For example, high-volume event ingestion workloads (such as IoT or telemetry), as well as
operational identifiers like job run IDs, support case references, or internal order numbers
typically benefit from larger cache sizes, where identifiers are generated frequently and
strict ordering isn't required.

**A cache size of 1 is better aligned when:**

- Allocation rates are relatively low
- Identifiers are expected to follow allocation order more closely over time
- Minimizing gaps is more important than maximum throughput

Workloads such as assigning account or reference numbers, where identifiers are generated
less often and closer ordering is desirable, are better aligned with a cache size of 1.
