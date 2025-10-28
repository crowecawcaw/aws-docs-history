# PERF 3. How do you store, manage, and access data in your workload?

The optimal data management solution for a particular system varies
based on the kind of data type (block, file, or object), access
patterns (random or sequential), required throughput, frequency of
access (online, offline, archival), frequency of update (WORM,
dynamic), and availability and durability constraints.
Well-Architected workloads use purpose-built data stores which allow
different features to improve performance.

###### Best practices

- [PERF03-BP01 Use a purpose-built data
  store that best supports your data access and storage requirements](perf_data_use_purpose_built_data_store.md "perf_data_use_purpose_built_data_store.md")
- [PERF03-BP02 Evaluate
  available configuration options for data store](perf_data_evaluate_configuration_options_data_store.md "perf_data_evaluate_configuration_options_data_store.md")
- [PERF03-BP03 Collect and record data store performance
  metrics](perf_data_collect_record_data_store_performance_metrics.md "perf_data_collect_record_data_store_performance_metrics.md")
- [PERF03-BP04 Implement strategies to improve query performance
  in data store](perf_data_implement_strategies_to_improve_query_performance.md "perf_data_implement_strategies_to_improve_query_performance.md")
- [PERF03-BP05 Implement data access patterns that utilize
  caching](perf_data_access_patterns_caching.md "perf_data_access_patterns_caching.md")
