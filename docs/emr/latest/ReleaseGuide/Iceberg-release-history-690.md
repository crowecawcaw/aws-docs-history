# Amazon EMR 6.9.0 - Iceberg release

notes

## Amazon EMR 6.9.0 -

Iceberg changes

| Type     | Description                                                                                                                                                                                                                                              |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feature  | Amazon EMR Flink integration with Iceberg.                                                                                                                                                                                                               |
| Feature  | Amazon EMR Hive integration with Iceberg.                                                                                                                                                                                                                |
| Feature  | Support to cache Iceberg metadata files on<br>Amazon FSx for Lustre to improve the query planning<br>time.                                                                                                                                               |
| Backport | [PR<br>5050](https://github.com/apache/iceberg/pull/5050 "https://github.com/apache/iceberg/pull/5050"): Flink 1.15: Support write options in<br>the in-line insert SQL comments.                                                                        |
| Backport | [PR<br>5282](https://github.com/apache/iceberg/pull/5282 "https://github.com/apache/iceberg/pull/5282"): AWS: Fix PUT retry failures by<br>opening new data file streams.                                                                                |
| Backport | [PR<br>5318](https://github.com/apache/iceberg/pull/5318 "https://github.com/apache/iceberg/pull/5318"): Flink 1.15: Bridge the gap between<br>FlinkSource and IcebergSource (FLIP-27) and added an<br>opt-in config to use FLIP-27 source in Flink SQL. |
| Backport | [PR<br>5344](https://github.com/apache/iceberg/pull/5344 "https://github.com/apache/iceberg/pull/5344"): Flink 1.14: Bridge the gap between<br>FlinkSource and IcebergSource (FLIP-27) and added an<br>opt-in config to use FLIP-27 source in Flink SQL. |
| Backport | [PR<br>5393](https://github.com/apache/iceberg/pull/5393 "https://github.com/apache/iceberg/pull/5393"): Flink 1.14, 1.15: Avoid converting<br>Iceberg MetricContext to Flink metrics in FLIP-27 source<br>reader.                                       |
| Backport | [PR<br>5401](https://github.com/apache/iceberg/pull/5401 "https://github.com/apache/iceberg/pull/5401"): Flink 1.14, 1.15: Missed<br>IcebergSourceReader group in PR #5393 for FLIP-27 source<br>reader metrics.                                         |
| Backport | [PR<br>5679](https://github.com/apache/iceberg/pull/5679 "https://github.com/apache/iceberg/pull/5679"): Spark 3.2, 3.3: Fix nullability<br>propagation for MergeRows node.                                                                              |
| Backport | [PR<br>5860](https://github.com/apache/iceberg/pull/5860 "https://github.com/apache/iceberg/pull/5860"): Spark 3.3: Fix QueryFailure when<br>running RewriteManifestProcedure on Date partitioned<br>tables.                                             |
| Backport | [PR<br>5880](https://github.com/apache/iceberg/pull/5880 "https://github.com/apache/iceberg/pull/5880"): Spark 3.3: Fix nullability in<br>merge-on-read projections.                                                                                     |
| Backport | [PR<br>5917](https://github.com/apache/iceberg/pull/5917 "https://github.com/apache/iceberg/pull/5917"): Spark 3.2: Fix nullability in<br>merge-on-read projections.                                                                                     |
