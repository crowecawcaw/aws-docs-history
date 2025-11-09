# Amazon EMR 7.4.0 - Hadoop release notes

## Amazon EMR 7.4.0 - Hadoop changes

| Type        | Description                                                                                                                                                                                                                                                                                          |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Upgrade     | Hadoop version is upgraded to 3.4.0, refer to<br>[OSS release notes](https://hadoop.apache.org/docs/r3.4.0/hadoop-project-dist/hadoop-common/release/3.4.0/RELEASENOTES.3.4.0.html "https://hadoop.apache.org/docs/r3.4.0/hadoop-project-dist/hadoop-common/release/3.4.0/RELEASENOTES.3.4.0.html"). |
| Bug Fix     | Fix negative Pending and Allocated Yarn metrics for FairScheduler                                                                                                                                                                                                                                    |
| Bug Fix     | [YARN-11702](https://issues.apache.org/jira/browse/YARN-11702 "https://issues.apache.org/jira/browse/YARN-11702") : Fix Yarn over allocating containers                                                                                                                                              |
| Bug Fix     | Improve race-condition handling when downscaling nodes                                                                                                                                                                                                                                               |
| Improvement | [HADOOP-18679](https://issues.apache.org/jira/browse/HADOOP-18679 "https://issues.apache.org/jira/browse/HADOOP-18679") : Add API for bulk/paged delete of files                                                                                                                                     |
| Improvement | [HADOOP-19203](https://issues.apache.org/jira/browse/HADOOP-19203 "https://issues.apache.org/jira/browse/HADOOP-19203"): WrappedIO BulkDelete API to raise IOEs as UncheckedIOExceptions                                                                                                             |
| Improvement | [HADOOP-19205](https://issues.apache.org/jira/browse/HADOOP-19205 "https://issues.apache.org/jira/browse/HADOOP-19205"): S3A: initialization/close slower than with v1 SDK                                                                                                                           |
| Improvement | [HADOOP-19161](https://issues.apache.org/jira/browse/HADOOP-19205 "https://issues.apache.org/jira/browse/HADOOP-19205"): S3A: option \*fs.s3a.performance.flags<br>• to take list of performance flags                                                                                               |
| Improvement | [HADOOP-19072](https://issues.apache.org/jira/browse/HADOOP-19205 "https://issues.apache.org/jira/browse/HADOOP-19205"): S3A: expand optimisations on stores with \*fs.s3a.performance.flags<br>• for mkdir                                                                                          |

## Amazon EMR 7.4.0 - Hadoop features

See the following list for new Hadoop features in Amazon EMR 7.4.0.

- The default configuration values have been fine-tuned for optimal performance:
  - **mapreduce.input.fileinputformat.list-status.num-threads=10** – This is up from 1.
  - **fs.s3a.block.size=64M** – This is up from 32M.
  - **fs.s3a.multipart.size=128M** – This is up from 64M.

- Out-of-the-box performance enhancing optimizations for accelerating MapReduce jobs with the S3A filesystem.
