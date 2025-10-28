# aurora_stat_wait_type

Lists all supported wait types for Aurora PostgreSQL.

## Syntax

```
aurora_stat_wait_type()
```

## Arguments

None

## Return type

SETOF record with the following columns:

- type_id – The ID of the type of wait event.
- type_name – Wait type name.

## Usage notes

To see wait event names with wait event types instead of IDs, use this function
together with other functions such as `aurora_stat_wait_event` and
`aurora_stat_system_waits`. Wait type names returned by this function
are the same as those returned by the `aurora_wait_report`
function.

## Examples

The following example shows results from calling the
`aurora_stat_wait_type` function.

```
`=>` `SELECT *
 FROM aurora_stat_wait_type();` `type_id | type_name
---------+-----------
 1 | LWLock
 3 | Lock
 4 | BufferPin
 5 | Activity
 6 | Client
 7 | Extension
 8 | IPC
 9 | Timeout
 10 | IO
 11 | LSN`
```
