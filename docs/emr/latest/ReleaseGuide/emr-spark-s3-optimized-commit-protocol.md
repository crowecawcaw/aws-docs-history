# Use the EMRFS S3-optimized

commit protocol

The EMRFS S3-optimized commit protocol is an alternative [FileCommitProtocol](https://spark.apache.org/docs/2.2.0//api/java/org/apache/spark/internal/io/FileCommitProtocol.html "https://spark.apache.org/docs/2.2.0//api/java/org/apache/spark/internal/io/FileCommitProtocol.html") implementation that is optimized for writing files
with Spark dynamic partition overwrite to Amazon S3 when using EMRFS. The protocol
improves application performance by avoiding rename operations in Amazon S3 during the
Spark dynamic partition overwrite job commit phase.

Note that the [EMRFS
S3-optimized committer](emr-spark-s3-optimized-committer.md "emr-spark-s3-optimized-committer.md") also improves performance by avoiding rename
operations. However, it doesn't work for dynamic partition overwrite cases, while
the commit protocol’s improvements only target dynamic partition overwrite
cases.

The commit protocol is available with Amazon EMR release 5.30.0 and later and 6.2.0 and
later and is enabled by default. Amazon EMR added a parallelism improvement starting with
release 5.31.0. The protocol is used for Spark jobs that use Spark, DataFrames, or
Datasets. There are circumstances under which the commit protocol is not used. For
more information, see [Requirements for the EMRFS
S3-optimized commit protocol](emr-spark-committer-reqs.md "emr-spark-committer-reqs.md").

###### Topics

- [Requirements for the EMRFS
  S3-optimized commit protocol](emr-spark-commit-protocol-reqs.md "emr-spark-commit-protocol-reqs.md")
- [The EMRFS S3-optimized
  commit protocol and multipart uploads](emr-spark-commit-protocol-multipart.md "emr-spark-commit-protocol-multipart.md")
- [Job tuning
  considerations](emr-spark-commit-protocol-tuning.md "emr-spark-commit-protocol-tuning.md")
