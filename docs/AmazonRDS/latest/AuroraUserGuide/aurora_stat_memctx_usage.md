# aurora_stat_memctx_usage

Reports the memory context usage for each PostgreSQL process.

## Syntax

```
aurora_stat_memctx_usage()
```

## Arguments

None

## Return type

SETOF record with the following columns:

- `pid` – The ID of the process.
- `name` – The name of the memory context.
- `allocated` – The number of bytes obtained from the
  underlying memory subsystem by the memory context.
- `used` – The number of bytes committed to clients of the
  memory context.
- `instances` – The count of currently existing contexts
  of this type.

## Usage notes

This function displays the memory context usage for each PostgreSQL process. Some
processes are labeled `anonymous`. The processes aren't exposed because
they contain restricted keywords.

This function is available starting with the following Aurora PostgreSQL
versions:

- 15.3 and higher 15 versions
- 14.8 and higher 14 versions
- 13.11 and higher 13 versions
- 12.15 and higher 12 versions
- 11.20 and higher 11 versions

## Examples

The following example shows the results of calling the
`aurora_stat_memctx_usage` function.

```
`=>` `SELECT *
 FROM aurora_stat_memctx_usage();`
 `pid| name | allocated | used | instances
-------+---------------------------------+-----------+---------+-----------
123864 | Miscellaneous | 19520 | 15064 | 3
123864 | Aurora File Context | 8192 | 616 | 1
123864 | Aurora WAL Context | 8192 | 296 | 1
123864 | CacheMemoryContext | 524288 | 422600 | 1
123864 | Catalog tuple context | 16384 | 13736 | 1
123864 | ExecutorState | 32832 | 28304 | 1
123864 | ExprContext | 8192 | 1720 | 1
123864 | GWAL record construction | 1024 | 832 | 1
123864 | MdSmgr | 8192 | 296 | 1
123864 | MessageContext | 532480 | 353832 | 1
123864 | PortalHeapMemory | 1024 | 488 | 1
123864 | PortalMemory | 8192 | 576 | 1
123864 | printtup | 8192 | 296 | 1
123864 | RelCache hash table entries | 8192 | 8152 | 1
123864 | RowDescriptionContext | 8192 | 1344 | 1
123864 | smgr relation context | 8192 | 296 | 1
123864 | Table function arguments | 8192 | 352 | 1
123864 | TopTransactionContext | 8192 | 632 | 1
123864 | TransactionAbortContext | 32768 | 296 | 1
123864 | WAL record construction | 50216 | 43904 | 1
123864 | hash table | 65536 | 52744 | 6
123864 | Relation metadata | 191488 | 124240 | 87
104992 | Miscellaneous | 9280 | 7728 | 3
104992 | Aurora File Context | 8192 | 376 | 1
104992 | Aurora WAL Context | 8192 | 296 | 1
104992 ||Autovacuum Launcher | 8192 | 296 | 1
104992 | Autovacuum database list | 16384 | 744 | 2
104992 | CacheMemoryContext | 262144 | 140288 | 1
104992 | Catalog tuple context | 8192 | 296 | 1
104992 | GWAL record construction | 1024 | 832 | 1
104992 | MdSmgr | 8192 | 296 | 1
104992 | PortalMemory | 8192 | 296 | 1
104992 | RelCache hash table entries | 8192 | 296 | 1
104992 | smgr relation context | 8192 | 296 | 1
104992 | Autovacuum start worker (tmp) | 8192 | 296 | 1
104992 | TopTransactionContext | 16384 | 592 | 2
104992 | TransactionAbortContext | 32768 | 296 | 1
104992 | WAL record construction | 50216 | 43904 | 1
104992 | hash table | 49152 | 34024 | 4
(39 rows)`
```

Some restricted keywords will be hidden and the output will look as
follows:

```
postgres`=>``SELECT *
 FROM aurora_stat_memctx_usage();`
 `pid| name | allocated | used | instances
-------+---------------------------------+-----------+---------+-----------
 5482 | anonymous | 8192 | 456 | 1
 5482 | anonymous | 8192 | 296 | 1`
```
