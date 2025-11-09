# Amazon EMR 7.6.0 - Hadoop release notes

## Amazon EMR 7.6.0 - Hadoop changes

| Type        | Description                                                                                                                                                                                                       |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New Feature | Framework of S3A Credential Vending                                                                                                                                                                               |
| New Feature | S3A Magic Committer Support For Hive                                                                                                                                                                              |
| Backport    | [HADOOP-19309: S3A](https://issues.apache.org/jira/browse/HADOOP-19309 "https://issues.apache.org/jira/browse/HADOOP-19309"): CopyFromLocalFile operation fails when the source file does not contain file scheme |
| Backport    | [HADOOP-19050](https://issues.apache.org/jira/browse/HADOOP-19050 "https://issues.apache.org/jira/browse/HADOOP-19050") S3A:Support S3 Access Grants                                                              |
| Backport    | [HADOOP-18708](https://issues.apache.org/jira/browse/HADOOP-18708 "https://issues.apache.org/jira/browse/HADOOP-18708") S3A: Support S3 Client Side Encryption(CSE)                                               |

## Amazon EMR 7.6.0 - Hadoop features

- The default configuration settings for `yarn.scheduler.increment-allocation-mb` and `yarn.scheduler.minimum-allocation-mb` have been
  modified from 32 to 1, which effectively disables container resource normalization in YARN.
- The S3A Filesystem in Hadoop has been enhanced to support request-level credential vending. With this feature, every Amazon S3 request made will utilize
  an `AwsCredentialsProvider`. This ensures improved flexibility and security by dynamically providing credentials for each request.
- The S3A Filesystem in Hadoop supports S3 client-side encryption.
