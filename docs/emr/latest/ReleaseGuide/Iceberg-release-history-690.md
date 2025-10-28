# Amazon EMR 6.9.0 - Iceberg release

notes

## Amazon EMR 6.9.0 -

Iceberg changes

| Type     | Description                                                                                                                                                                                                                                     |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feature  | Amazon EMR Flink integration with Iceberg.                                                                                                                                                                                                      |
| Feature  | Amazon EMR Hive integration with Iceberg.                                                                                                                                                                                                       |
| Feature  | Support to cache Iceberg metadata files on Amazon FSx for Lustre to improve the query planning time.                                                                                                                                            |
| Backport | [PR 5050](https://github.com/apache/iceberg/pull/5050 "https://github.com/apache/iceberg/pull/5050"): Flink 1.15: Support write options in the in-line insert SQL comments.                                                                     |
| Backport | [PR 5282](https://github.com/apache/iceberg/pull/5282 "https://github.com/apache/iceberg/pull/5282"): AWS: Fix PUT retry failures by opening new data file streams.                                                                             |
| Backport | [PR 5318](https://github.com/apache/iceberg/pull/5318 "https://github.com/apache/iceberg/pull/5318"): Flink 1.15: Bridge the gap between FlinkSource and IcebergSource (FLIP-27) and added an opt-in config to use FLIP-27 source in Flink SQL. |
| Backport | [PR 5344](https://github.com/apache/iceberg/pull/5344 "https://github.com/apache/iceberg/pull/5344"): Flink 1.14: Bridge the gap between FlinkSource and IcebergSource (FLIP-27) and added an opt-in config to use FLIP-27 source in Flink SQL. |
| Backport | [PR 5393](https://github.com/apache/iceberg/pull/5393 "https://github.com/apache/iceberg/pull/5393"): Flink 1.14, 1.15: Avoid converting Iceberg MetricContext to Flink metrics in FLIP-27 source reader.                                       |
| Backport | [PR 5401](https://github.com/apache/iceberg/pull/5401 "https://github.com/apache/iceberg/pull/5401"): Flink 1.14, 1.15: Missed IcebergSourceReader group in PR #5393 for FLIP-27 source reader metrics.                                         |
| Backport | [PR 5679](https://github.com/apache/iceberg/pull/5679 "https://github.com/apache/iceberg/pull/5679"): Spark 3.2, 3.3: Fix nullability propagation for MergeRows node.                                                                           |
| Backport | [PR 5860](https://github.com/apache/iceberg/pull/5860 "https://github.com/apache/iceberg/pull/5860"): Spark 3.3: Fix QueryFailure when running RewriteManifestProcedure on Date partitioned tables.                                             |
| Backport | [PR 5880](https://github.com/apache/iceberg/pull/5880 "https://github.com/apache/iceberg/pull/5880"): Spark 3.3: Fix nullability in merge-on-read projections.                                                                                  |
| Backport | [PR 5917](https://github.com/apache/iceberg/pull/5917 "https://github.com/apache/iceberg/pull/5917"): Spark 3.2: Fix nullability in merge-on-read projections.                                                                                  |
