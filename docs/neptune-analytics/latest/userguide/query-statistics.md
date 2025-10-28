# Statistics

Neptune Analytics uses similar statistics for planning query execution as in [Neptune Database](../../../neptune/latest/userguide/neptune-dfe-statistics.md "../../../neptune/latest/userguide/neptune-dfe-statistics.md"). Computing these statistics is performed as
an integrated part of the Neptune Analytics storage system. There are a number of differences between the features and usage of
statistics between Neptune Analytics and Neptune Database:

1. Initial statistics generation is performed as part of either the initial import task or an initial data load
   occurring before any query-driven updates. Subsequently, statistics re-computation is triggered automatically
   based on the amount of update operations performed by the database.
2. Like with Neptune Database, Neptune Analytics has a size limit for statistics data, beyond which statistics will be disabled. The
   number of predicate statistics, may not exceed one million (the same as Neptune Database). There is no hard limit on
   the number of characteristic sets present in the underlying data. However, beyond 10,000 characteristic sets,
   the system will begin to merge statistics data in order to limit the overall size of data being managed.
3. Statistics generation is fully managed by the storage system. There are no APIs to disable or re-compute statistics.
4. There are no CloudWatch metrics relating to statistics generation.
