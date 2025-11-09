# Amazon EMR 6.8.0 - Hive release

notes

## Amazon EMR 6.8.0 -

Hive changes

| Type        | Description                                                                                                                                                                                                           |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Improvement | Reduce file system calls in msck command. Performance<br>improvements (~15-20x on 10k+ partitions)                                                                                                                    |
| Backport    | [HIVE-20678](https://issues.apache.org/jira/browse/HIVE-20678 "https://issues.apache.org/jira/browse/HIVE-20678"): HiveHBaseTableOutputFormat should<br>implement HiveOutputFormat to ensure compatibility            |
| Backport    | [HIVE-21040](https://issues.apache.org/jira/browse/HIVE-21040 "https://issues.apache.org/jira/browse/HIVE-21040"): msck does unnecessary file listing<br>at last level of directory tree                              |
| Backport    | [HIVE-21460](https://issues.apache.org/jira/browse/HIVE-21460 "https://issues.apache.org/jira/browse/HIVE-21460"): Load data followed by a select \*<br>query results in incorrect results                            |
| Backport    | [HIVE-21660](https://issues.apache.org/jira/browse/HIVE-21660 "https://issues.apache.org/jira/browse/HIVE-21660"): Wrong result when union all and<br>later view with explode is used                                 |
| Backport    | [HIVE-22505](https://issues.apache.org/jira/browse/HIVE-22505 "https://issues.apache.org/jira/browse/HIVE-22505"): ClassCastException caused by wrong<br>Vectorized operator selection                                |
| Backport    | [HIVE-22513](https://issues.apache.org/jira/browse/HIVE-22513 "https://issues.apache.org/jira/browse/HIVE-22513"): Constant propagation of casted<br>column in filter ops can cause incorrect results                 |
| Backport    | [HIVE-23435](https://issues.apache.org/jira/browse/HIVE-23435 "https://issues.apache.org/jira/browse/HIVE-23435"): Full outer join result is missing<br>rows                                                          |
| Backport    | [HIVE-24209](https://issues.apache.org/jira/browse/HIVE-24209 "https://issues.apache.org/jira/browse/HIVE-24209"): Incorrect search argument<br>conversion for NOT BETWEEN operation when vectorization is<br>enabled |
| Backport    | [HIVE-24934](https://issues.apache.org/jira/browse/HIVE-24934 "https://issues.apache.org/jira/browse/HIVE-24934"): VectorizedExpressions annotation is<br>not needed in GenericUDFSQCountCheck                        |
| Backport    | [HIVE-25278](https://issues.apache.org/jira/browse/HIVE-25278 "https://issues.apache.org/jira/browse/HIVE-25278"): HiveProjectJoinTransposeRule may do<br>invalid transformations with windowing expressions          |
| Backport    | [HIVE-25505](https://issues.apache.org/jira/browse/HIVE-25505 "https://issues.apache.org/jira/browse/HIVE-25505"): Incorrect results with header.<br>skip.header.line.count if first line is blank                    |
| Backport    | [HIVE-26080](https://issues.apache.org/jira/browse/HIVE-26080 "https://issues.apache.org/jira/browse/HIVE-26080"): Upgrade accumulo-core to<br>1.10.1                                                                 |
| Backport    | [HIVE-26235](https://issues.apache.org/jira/browse/HIVE-26235 "https://issues.apache.org/jira/browse/HIVE-26235"): OR Condition on binary column is<br>returning empty result                                         |
| Bug         | Fix multiple SLF4J bindings warning logs in stderr during<br>launch                                                                                                                                                   |
| Bug         | Fix SHOW TABLE EXTENDED query failing with Wrong FS error<br>when partition and table are on different file<br>systems.                                                                                               |

## Amazon EMR 6.8.0 - Hive known

issues

- With Amazon EMR 6.6.0 through 6.9.x, INSERT queries with dynamic partition and an ORDER BY or SORT BY clause will always have two reducers. This issue is caused by OSS change [HIVE-20703](https://issues.apache.org/jira/browse/HIVE-20703 "https://issues.apache.org/jira/browse/HIVE-20703"), which puts dynamic sort partition optimization under cost-based decision. If your workload doesn't require sorting of dynamic partitions, we recommend that you set the `hive.optimize.sort.dynamic.partition.threshold` property to `-1` to disable the new feature and get the correctly calculated number of reducers. This issue is fixed in OSS Hive as part of [HIVE-22269](https://issues.apache.org/jira/browse/HIVE-22269 "https://issues.apache.org/jira/browse/HIVE-22269") and is fixed in Amazon EMR 6.10.0.
