# Managing performance and scaling for Amazon Aurora MySQL

## Scaling Aurora MySQL DB instances

You can scale Aurora MySQL DB instances in two ways, instance scaling and read
scaling. For more information about read scaling, see
[Read scaling](Aurora.Managing.md#Aurora.Managing.Performance.ReadScaling "Aurora.Managing.md#Aurora.Managing.Performance.ReadScaling").

You can scale your Aurora MySQL DB cluster by modifying the DB instance class for
each DB instance in the DB cluster. Aurora MySQL supports several DB instance classes
optimized for Aurora. Don't use db.t2 or db.t3 instance classes for larger Aurora
clusters of size greater than 40 TB. For the specifications of the DB
instance classes supported by Aurora MySQL,
see [Amazon AuroraDB instance classes](Concepts.md "Concepts.md").

###### Note

We recommend using the T DB instance classes only for development and test servers, or other non-production servers. For
more details on the T instance classes, see [Using T instance classes for development and testing](AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.T2Medium "AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.T2Medium").

## Maximum connections to an Aurora MySQL DB instance

The maximum number of connections allowed to an Aurora MySQL DB instance is determined by
the `max_connections` parameter in the instance-level parameter group for
the DB instance.

The following table lists the resulting default value of
`max_connections` for each DB instance class available to Aurora MySQL. You
can increase the maximum number of connections to your Aurora MySQL DB instance by scaling
the instance up to a DB instance class with more memory, or by setting a larger
value for the `max_connections` parameter in the DB parameter group for your instance, up to 16,000.

###### Tip

If your applications frequently open and close connections, or keep a large number of long-lived connections open, we recommend that you use Amazon RDS Proxy.
RDS Proxy is a fully managed, highly available database proxy that uses connection pooling to share database connections securely and efficiently. To learn more
about RDS Proxy, see [Amazon RDS Proxyfor Aurora](rds-proxy.md "rds-proxy.md").

For details about how Aurora Serverless v2 instances handle this parameter, see
[Maximum connections for Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.max-connections "aurora-serverless-v2.md#aurora-serverless-v2.max-connections").

| Instance class  | max_connections default value |
| --------------- | ----------------------------- |
| db.t2.small     | 45                            |
| db.t2.medium    | 90                            |
| db.t3.small     | 45                            |
| db.t3.medium    | 90                            |
| db.t3.large     | 135                           |
| db.t4g.medium   | 90                            |
| db.t4g.large    | 135                           |
| db.r3.large     | 1000                          |
| db.r3.xlarge    | 2000                          |
| db.r3.2xlarge   | 3000                          |
| db.r3.4xlarge   | 4000                          |
| db.r3.8xlarge   | 5000                          |
| db.r4.large     | 1000                          |
| db.r4.xlarge    | 2000                          |
| db.r4.2xlarge   | 3000                          |
| db.r4.4xlarge   | 4000                          |
| db.r4.8xlarge   | 5000                          |
| db.r4.16xlarge  | 6000                          |
| db.r5.large     | 1000                          |
| db.r5.xlarge    | 2000                          |
| db.r5.2xlarge   | 3000                          |
| db.r5.4xlarge   | 4000                          |
| db.r5.8xlarge   | 5000                          |
| db.r5.12xlarge  | 6000                          |
| db.r5.16xlarge  | 6000                          |
| db.r5.24xlarge  | 7000                          |
| db.r6g.large    | 1000                          |
| db.r6g.xlarge   | 2000                          |
| db.r6g.2xlarge  | 3000                          |
| db.r6g.4xlarge  | 4000                          |
| db.r6g.8xlarge  | 5000                          |
| db.r6g.12xlarge | 6000                          |
| db.r6g.16xlarge | 6000                          |
| db.r6i.large    | 1000                          |
| db.r6i.xlarge   | 2000                          |
| db.r6i.2xlarge  | 3000                          |
| db.r6i.4xlarge  | 4000                          |
| db.r6i.8xlarge  | 5000                          |
| db.r6i.12xlarge | 6000                          |
| db.r6i.16xlarge | 6000                          |
| db.r6i.24xlarge | 7000                          |
| db.r6i.32xlarge | 7000                          |
| db.r7g.large    | 1000                          |
| db.r7g.xlarge   | 2000                          |
| db.r7g.2xlarge  | 3000                          |
| db.r7g.4xlarge  | 4000                          |
| db.r7g.8xlarge  | 5000                          |
| db.r7g.12xlarge | 6000                          |
| db.r7g.16xlarge | 6000                          |
| db.r7i.large    | 1000                          |
| db.r7i.xlarge   | 2000                          |
| db.r7i.2xlarge  | 3000                          |
| db.r7i.4xlarge  | 4000                          |
| db.r7i.8xlarge  | 5000                          |
| db.r7i.12xlarge | 6000                          |
| db.r7i.16xlarge | 6000                          |
| db.r7i.24xlarge | 7000                          |
| db.r7i.48xlarge | 8000                          |
| db.r8g.large    | 1000                          |
| db.r8g.xlarge   | 2000                          |
| db.r8g.2xlarge  | 3000                          |
| db.r8g.4xlarge  | 4000                          |
| db.r8g.8xlarge  | 5000                          |
| db.r8g.12xlarge | 6000                          |
| db.r8g.16xlarge | 6000                          |
| db.r8g.24xlarge | 7000                          |
| db.r8g.48xlarge | 8000                          |
| db.x2g.large    | 2000                          |
| db.x2g.xlarge   | 3000                          |
| db.x2g.2xlarge  | 4000                          |
| db.x2g.4xlarge  | 5000                          |
| db.x2g.8xlarge  | 6000                          |
| db.x2g.12xlarge | 7000                          |
| db.x2g.16xlarge | 7000                          |

###### Tip

The `max_connections` parameter calculation uses log base 2 (distinct from natural logarithm) and the `DBInstanceClassMemory` value in bytes for the selected Aurora MySQL instance class. The parameter accepts only integer values, with decimal portions truncated from calculations. The formula implements connection limits as follows:

- 1000 connection increment for larger R3, R4, and R5 instances
- 45 connection increment for T2 and T3 instance memory variants
  Example: For db.r6g.large, while the formula calculates 1069.2, the system implements 1000 to maintain consistent incremental patterns.

If you create a new parameter group to customize your own default for the connection limit, you'll see that the default
connection limit is derived using a formula based on the `DBInstanceClassMemory` value. As shown in the preceding
table, the formula produces connection limits that increase by 1000 as the memory doubles between progressively larger R3, R4,
and R5 instances, and by 45 for different memory sizes of T2 and T3 instances.

See [Specifying DB parameters](USER_ParamValuesRef.md "USER_ParamValuesRef.md") for more details on how
`DBInstanceClassMemory` is calculated.

Aurora MySQL and RDS for MySQL DB instances have different amounts of memory overhead. Therefore, the
`max_connections` value can be different for Aurora MySQL and RDS for MySQL DB instances that use the same instance
class. The values in the table only apply to Aurora MySQL DB instances.

###### Note

The much lower connectivity limits for T2 and T3 instances are because with Aurora, those instance classes are intended
only for development and test scenarios, not for production workloads.

The default connection limits are tuned for systems that use the default values for other major memory consumers, such as the
buffer pool and query cache. If you change those other settings for your cluster, consider adjusting the connection limit to
account for the increase or decrease in available memory on the DB instances.

## Temporary storage limits for Aurora MySQL

Aurora MySQL stores tables and indexes in the Aurora storage subsystem. Aurora MySQL uses
separate temporary or local storage for nonpersistent temporary files and non-InnoDB
temporary tables. Local storage also includes files that are used for such purposes as
sorting large datasets during query processing or for index build operations. It doesn't
include InnoDB temporary tables.

For more information on temporary tables in Aurora MySQL version 3, see [New temporary table behavior in Aurora MySQL version 3](ams3-temptable-behavior.md "ams3-temptable-behavior.md"). For
more information on temporary tables in version 2, see [Temporary tablespace behavior in Aurora MySQL version 2](AuroraMySQL.md#AuroraMySQL.TempTables57 "AuroraMySQL.md#AuroraMySQL.TempTables57").

The data and temporary files on these volumes are lost when starting and stopping the
DB instance, and during host replacement.

These local storage volumes are backed by Amazon Elastic Block Store (EBS) and can be extended by using a larger DB instance class. For more
information about storage, see [Amazon Aurora storage](Aurora.Overview.md "Aurora.Overview.md").

Local storage is also used for importing data from Amazon S3 using `LOAD DATA FROM
 S3` or `LOAD XML FROM S3`, and for exporting data to S3 using
SELECT INTO OUTFILE S3. For more information on importing from and exporting to S3, see
the following:

- [Loading data into an Amazon Aurora MySQL DB cluster from text files in an Amazon S3 bucket](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md")
- [Saving data from an Amazon Aurora MySQL DB cluster into text files in an Amazon S3 bucket](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md")

Aurora MySQL uses separate permanent storage for error logs, general logs, slow query
logs, and audit logs for most of the Aurora MySQL DB instance classes (not including
burstable-performance instance class types such as db.t2, db.t3, and db.t4g). The data
on this volume is retained when starting and stopping the DB instance, and during host
replacement.

This permanent storage volume is also backed by Amazon EBS and has a fixed size according
to the DB instance class. It can't be extended by using a larger DB instance
class.

The following table shows the maximum amount of temporary and permanent storage
available for each Aurora MySQL DB instance class. For more information on DB instance
class support for Aurora, see [Amazon AuroraDB instance classes](Concepts.md "Concepts.md").

| DB instance class | Maximum temporary/local storage available (GiB) | Additional maximum storage available for log files (GiB) |
| ----------------- | ----------------------------------------------- | -------------------------------------------------------- |
| db.x2g.16xlarge   | 1280                                            | 500                                                      |
| db.x2g.12xlarge   | 960                                             | 500                                                      |
| db.x2g.8xlarge    | 640                                             | 500                                                      |
| db.x2g.4xlarge    | 320                                             | 500                                                      |
| db.x2g.2xlarge    | 160                                             | 60                                                       |
| db.x2g.xlarge     | 80                                              | 60                                                       |
| db.x2g.large      | 40                                              | 60                                                       |
| db.r8g.48xlarge   | 3840                                            | 500                                                      |
| db.r8g.24xlarge   | 1920                                            | 500                                                      |
| db.r8g.16xlarge   | 1280                                            | 500                                                      |
| db.r8g.12xlarge   | 960                                             | 500                                                      |
| db.r8g.8xlarge    | 640                                             | 500                                                      |
| db.r8g.4xlarge    | 320                                             | 500                                                      |
| db.r8g.2xlarge    | 160                                             | 60                                                       |
| db.r8g.xlarge     | 80                                              | 60                                                       |
| db.r8g.large      | 32                                              | 60                                                       |
| db.r7i.48xlarge   | 3840                                            | 500                                                      |
| db.r7i.24xlarge   | 1920                                            | 500                                                      |
| db.r7i.16xlarge   | 1280                                            | 500                                                      |
| db.r7i.12xlarge   | 960                                             | 500                                                      |
| db.r7i.8xlarge    | 640                                             | 500                                                      |
| db.r7i.4xlarge    | 320                                             | 500                                                      |
| db.r7i.2xlarge    | 160                                             | 60                                                       |
| db.r7i.xlarge     | 80                                              | 60                                                       |
| db.r7i.large      | 32                                              | 60                                                       |
| db.r7g.16xlarge   | 1280                                            | 500                                                      |
| db.r7g.12xlarge   | 960                                             | 500                                                      |
| db.r7g.8xlarge    | 640                                             | 500                                                      |
| db.r7g.4xlarge    | 320                                             | 500                                                      |
| db.r7g.2xlarge    | 160                                             | 60                                                       |
| db.r7g.xlarge     | 80                                              | 60                                                       |
| db.r7g.large      | 32                                              | 60                                                       |
| db.r6i.32xlarge   | 2560                                            | 500                                                      |
| db.r6i.24xlarge   | 1920                                            | 500                                                      |
| db.r6i.16xlarge   | 1280                                            | 500                                                      |
| db.r6i.12xlarge   | 960                                             | 500                                                      |
| db.r6i.8xlarge    | 640                                             | 500                                                      |
| db.r6i.4xlarge    | 320                                             | 500                                                      |
| db.r6i.2xlarge    | 160                                             | 60                                                       |
| db.r6i.xlarge     | 80                                              | 60                                                       |
| db.r6i.large      | 32                                              | 60                                                       |
| db.r6g.16xlarge   | 1280                                            | 500                                                      |
| db.r6g.12xlarge   | 960                                             | 500                                                      |
| db.r6g.8xlarge    | 640                                             | 500                                                      |
| db.r6g.4xlarge    | 320                                             | 500                                                      |
| db.r6g.2xlarge    | 160                                             | 60                                                       |
| db.r6g.xlarge     | 80                                              | 60                                                       |
| db.r6g.large      | 32                                              | 60                                                       |
| db.r5.24xlarge    | 1920                                            | 500                                                      |
| db.r5.16xlarge    | 1280                                            | 500                                                      |
| db.r5.12xlarge    | 960                                             | 500                                                      |
| db.r5.8xlarge     | 640                                             | 500                                                      |
| db.r5.4xlarge     | 320                                             | 500                                                      |
| db.r5.2xlarge     | 160                                             | 60                                                       |
| db.r5.xlarge      | 80                                              | 60                                                       |
| db.r5.large       | 32                                              | 60                                                       |
| db.r4.16xlarge    | 1280                                            | 500                                                      |
| db.r4.8xlarge     | 640                                             | 500                                                      |
| db.r4.4xlarge     | 320                                             | 500                                                      |
| db.r4.2xlarge     | 160                                             | 60                                                       |
| db.r4.xlarge      | 80                                              | 60                                                       |
| db.r4.large       | 32                                              | 60                                                       |
| db.t4g.large      | 32                                              | –                                                        |
| db.t4g.medium     | 32                                              | –                                                        |
| db.t3.large       | 32                                              | –                                                        |
| db.t3.medium      | 32                                              | –                                                        |
| db.t3.small       | 32                                              | –                                                        |
| db.t2.medium      | 32                                              | –                                                        |
| db.t2.small       | 32                                              | –                                                        |

###### Important

These values represent the theoretical maximum amount of free storage on each DB instance. The actual local storage available to you might be
lower. Aurora uses some local storage for its management processes, and the DB instance uses some local storage even before you load any data.
You can monitor the temporary storage available for a specific DB instance with the `FreeLocalStorage` CloudWatch metric, described in
[Amazon CloudWatch metrics for Amazon Aurora](Aurora.AuroraMonitoring.md "Aurora.AuroraMonitoring.md"). You can check the amount of free storage
at the present time. You can also chart the amount of free storage over time. Monitoring the free storage over time helps you to determine
whether the value is increasing or decreasing, or to find the minimum, maximum, or average values.

(This doesn't apply to Aurora Serverless v2.)
