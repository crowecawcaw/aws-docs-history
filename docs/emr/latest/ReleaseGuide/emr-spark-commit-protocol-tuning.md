# Job tuning

considerations

On Spark executors, the EMRFS S3-optimized commit protocol consumes a small
amount of memory for each file written by a task attempt until the task gets
committed or aborted. In most jobs, the amount of memory consumed is negligible.

On Spark drivers, the EMRFS S3-optimized commit protocol requires memory to
store metadata info of each committed file until the job gets committed or
aborted. In most jobs, default Spark driver memory setting is negligible.

For jobs that have long-running tasks that write a large number of files, the
memory that the commit protocol consumes may be noticeable and require
adjustments to the memory allocated for Spark, especially for Spark executors.
You can tune memory using the `spark.driver.memory` property for
Spark drivers, and the `spark.executor.memory` property for Spark
executors. As a guideline, a single task writing 100,000 files would typically
require an additional 100MB of memory. For more information, see [Application properties](https://spark.apache.org/docs/latest/configuration.html#application-properties "https://spark.apache.org/docs/latest/configuration.html#application-properties") in the Apache Spark Configuration
documentation.
