# Amazon DocumentDB serverless instance limits

For DocumentDB serverless instances, the following limits per instance are dependent upon the instance’s current scaling capacity:

- Instance Memory (GiB)
- Connections (all)
- Cursor Limit
- Open Transactions
- Connections (active)
  The following tables describe how the per-instance limits of serverless instances scale in relation to the instance’s current scaling capacity.

Note that the limit values are different depending on whether the cluster’s `MinCapacity` scaling configuration has been set to greater than two (2).
If `MinCapacity` is set to less than or equal to 2, then the limit values for cursor limit, open transactions, and connections (active) are capped to a lower maximum value.
(The technical reason for the cap is to support scaling down to an “idle” state.
For more information, see [Idle state (0.5 DCUs)](docdb-serverless-how-it-works.md#docdb-serverlerss-idle-state "docdb-serverless-how-it-works.md#docdb-serverlerss-idle-state").

**db.serverless instance limits if MinCapacity ≤1**

| Current Capacity (DCU) | Instance Memory (GiB)   | Connections (all)                    | Cursor Limit            | Open Transactions | Connections (active) |
| ---------------------- | ----------------------- | ------------------------------------ | ----------------------- | ----------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------- |
| 0.5                    | 1                       | 250                                  | 6                       | 12                | 39                   |
| 1                      | 2                       | 500                                  | 12                      | 24                | 79                   |
| 2                      | 4                       | 1000                                 | 24                      | 48                | 173                  |
| 4                      | 8                       | 2000                                 | 48                      | 96                | 416                  |
| 8                      | 16                      | 4000                                 | 96                      | 192               | 1071                 |
| 16                     | 32                      | 8000                                 | 132                     | 264               | 1550                 |
| 32                     | 64                      | 16000                                | 132                     | 264               | 1550                 |
| 64                     | 128                     | 32000                                | 132                     | 264               | 1550                 |
| 128                    | 256                     | 60000                                | 132                     | 264               | 1550                 |
| 256                    | 512                     | 60000                                | 132                     | 264               | 1550                 | **db.serverless instance limits if MinCapacity >1**                                                                                                                                                                                 |
| Current Capacity (DCU) | Instance Memory (GiB)   | Connections (all)                    | Cursor Limit            | Open Transactions | Connections (active) |
| ---                    | ---                     | ---                                  | ---                     | ---               | ---                  |
| 1.5                    | 3                       | 7250                                 | 18                      | 36                | 124                  |
| 2                      | 4                       | 1000                                 | 24                      | 48                | 173                  |
| 4                      | 8                       | 2000                                 | 48                      | 96                | 416                  |
| 8                      | 16                      | 4000                                 | 96                      | 192               | 1071                 |
| 16                     | 32                      | 8000                                 | 192                     | 384               | 2709                 |
| 32                     | 64                      | 16000                                | 384                     | 768               | 4500                 |
| 64                     | 128                     | 32000                                | 768                     | 1536              | 4500                 |
| 128                    | 256                     | 60000                                | 1536                    | 3072              | 4500                 |
| 256                    | 512                     | 60000                                | 3072                    | 6144              | 4500                 | You can monitor and alarm on the per instance limits using the following CloudWatch metrics. For more on Amazon DocumentDB CloudWatch metrics, see [Monitoring Amazon DocumentDB with CloudWatch](cloud_watch.md "cloud_watch.md"). |
| Resource               | CloudWatch limit metric | CloudWatch usage metric (1-min. max) | CloudWatch usage metric |                   | ---                  | ---                                                                                                                                                                                                                                 | ---                    | ---                 |
| Instance Memory        | -                       | -                                    | FreeableMemory          |                   | Connections (all)    | DatabaseConnectionsLimit                                                                                                                                                                                                            | DatabaseConnectionsMax | DatabaseConnections |
| Cursors                | DatabaseCursorsLimit    | DatabaseCursorsMax                   | DatabaseCursors         |                   | Transactions         | TransactionsOpenLimit                                                                                                                                                                                                               | TransactionsOpenMax    | TransactionsOpen    |
