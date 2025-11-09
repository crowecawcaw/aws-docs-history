# Amazon EMR 7.7.0 - Hadoop release notes

## Amazon EMR 7.7.0 - Hadoop changes

| Type        | Description                                                                                                                                                                                             |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New Feature | Optimize S3A GlobStatus Call With S3 Prefix Listing                                                                                                                                                     |
| Backport    | [YARN-7327](https://issues.apache.org/jira/browse/YARN-7327 "https://issues.apache.org/jira/browse/YARN-7327"): Enable asynchronous scheduling by default for capacity scheduler                        |
| Backport    | [YARN-10058](https://issues.apache.org/jira/browse/YARN-10058 "https://issues.apache.org/jira/browse/YARN-10058"): Handle uncaught exception for async-scheduling threads to prevent scheduler hangs    |
| Backport    | [YARN-11732](https://issues.apache.org/jira/browse/YARN-11732 "https://issues.apache.org/jira/browse/YARN-11732"): Fix potential NPE when calling SchedulerNode#reservedContainer for CapacityScheduler |
| Backport    | [YARN-11560](https://issues.apache.org/jira/browse/YARN-11560 "https://issues.apache.org/jira/browse/YARN-11560"): Fix NPE bug when multi-node enabled with schedule asynchronously                     |
| Backport    | [YARN-11191](https://issues.apache.org/jira/browse/YARN-11191 "https://issues.apache.org/jira/browse/YARN-11191"): Fix potentional deadlock in GlobalScheduler refreshQueues                            |
| Backport    | [YARN-11041](https://issues.apache.org/jira/browse/YARN-11041 "https://issues.apache.org/jira/browse/YARN-11041"): Replace all occurences of queuePath with the new QueuePath class                     |
| Backport    | [YARN-11660](https://issues.apache.org/jira/browse/YARN-11660 "https://issues.apache.org/jira/browse/YARN-11660"): Fix performance regression for SingleConstraintAppPlacementAllocator                 |
| Backport    | [HADOOP-19116](https://issues.apache.org/jira/browse/HADOOP-19116 "https://issues.apache.org/jira/browse/HADOOP-19116"): Update to zookeeper client 3.8.4 due to CVE-2024-23944.                        |
| Backport    | [HADOOP-19115](https://issues.apache.org/jira/browse/HADOOP-19115 "https://issues.apache.org/jira/browse/HADOOP-19115"): Upgrade to nimbus-jose-jwt 9.37.2 due to CVE-2023-52428.                       |
| Backport    | [HADOOP-19024](https://issues.apache.org/jira/browse/HADOOP-19116 "https://issues.apache.org/jira/browse/HADOOP-19116"): Use bouncycastle jdk18 1.77                                                    |
| Backport    | [HADOOP-19123](https://issues.apache.org/jira/browse/HADOOP-19123 "https://issues.apache.org/jira/browse/HADOOP-19123"): Update to commons-configuration2 2.10.1 due to CVE                             |
| Backport    | [HADOOP-19114](https://issues.apache.org/jira/browse/HADOOP-19114 "https://issues.apache.org/jira/browse/HADOOP-19114"): Upgrade to commons-compress 1.26.1 due to CVEs                                 |
| Backport    | [HADOOP-19237](https://issues.apache.org/jira/browse/HADOOP-19237 "https://issues.apache.org/jira/browse/HADOOP-19237"): Upgrade to dnsjava 3.6.1 due to CVEs                                           |
| New Feature | Add S3 request auditing to S3A                                                                                                                                                                          |
| Backport    | [HADOOP-17609](https://issues.apache.org/jira/browse/HADOOP-17609 "https://issues.apache.org/jira/browse/HADOOP-17609"): Make SM4 support optional for OpenSSL native code                              |
| Backport    | [HADOOP-18583](https://issues.apache.org/jira/browse/HADOOP-18583 "https://issues.apache.org/jira/browse/HADOOP-18583"): hadoop checknative fails to load openssl 3.x                                   |
| New Feature | Add support for S3A Role Mappings                                                                                                                                                                       |

## Amazon EMR 7.7.0 - Hadoop features

- Asynchronous container scheduling is made the default scheduling strategy for the capacity scheduler, designed to optimize container allocation speed.
- S3A filesystem introduces an optimization for glob status calls using [S3 prefix listing](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") to accelerate
  list operations. By default, this feature is disabled and can be enabled by configuring `fs.s3a.prefix.listing.in.glob.status.enabled=true` in the
  core-site.xml file. When enabled, the optimization allows server-side filtering for globstatus calls like `fs.globstatus("s3://`bucket`/a*")`,
  improving list performance by by listing only the objects starting with `"a"`.
- Add S3 request auditing to S3A, when enabled the information from fileSystemOwner object is used to populate the userAgent
  string with the user and user group fields making the S3 requests.
- S3A adds support for Role mappings which helps determine which IAM role to use based on users, groups, or S3 prefixes.
