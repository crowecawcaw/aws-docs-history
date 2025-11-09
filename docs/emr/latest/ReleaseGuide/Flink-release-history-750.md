# Amazon EMR 7.5.0 - Flink release notes

| Type        | Description                                             |
| ----------- | ------------------------------------------------------- |
| Feature     | Added support for running Flink jobs with a remote jar. |
| Improvement | Make vertex exclusion and inclusion thread safe.        |

## Amazon EMR 7.5.0 - Flink features

- Starting with Amazon EMR 7.5.0, you can specify an Amazon S3 location as the JAR path when using the `run` and `run-application` Apache Flink CLI
  commands. When you provide an S3 path, EMR automatically downloads the JAR file from Amazon S3 to the cluster's EBS storage. Each time you specify the same JAR
  file, EMR downloads the latest version from Amazon S3 instead of reusing the existing JAR file on the cluster.
- Starting with Amazon EMR 7.5.0, customers can pass remote path (an S3 location) as the JAR path with `run` and `run-application` Flink CLI commands. The
  JAR is then automatically pulled from the S3 store to the EBS storage of the cluster. If the same JAR is provided again, it downloads the latest one from S3 and doesn't reuse the existing
  JAR on the cluster.
