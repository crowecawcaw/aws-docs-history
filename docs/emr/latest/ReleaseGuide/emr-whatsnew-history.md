# Amazon EMR archive of release notes

Release notes for all Amazon EMR releases are available below. For comprehensive release
information for each release, see [Amazon EMR 6.x release versions](emr-release-6x.md "emr-release-6x.md"), [Amazon EMR 5.x release versions](emr-release-5x.md "emr-release-5x.md") and [Amazon EMR 4.x release versions](emr-release-4x.md "emr-release-4x.md").

To get updates when a new Amazon EMR release is available, subscribe to the [RSS feed for Amazon EMR release notes](amazon-emr-release-notes.md "amazon-emr-release-notes.md").

## Release 6.14.0

The following release notes include information for Amazon EMR release
6.14.0. Changes are relative to 6.13.0. For information on the
release timeline, see the [6.14.0 change log](emr-6140-release.md#6140-changelog "emr-6140-release.md#6140-changelog").

###### New features

- Amazon EMR 6.14.0 supports Apache Spark 3.4.1,
  Apache Spark RAPIDS 23.06.0-amzn-2,
  Flink 1.17.1, Iceberg 1.3.1, and Trino 422.
- [Amazon EMR managed scaling](../ManagementGuide/emr-managed-scaling.md "../ManagementGuide/emr-managed-scaling.md")
  is now available in the `ap-southeast-3` Asia Pacific (Jakarta)
  Region for clusters that you create with Amazon EMR 6.14.0 and higher.

###### Known issues

- An on-cluster instance-state script that monitors health of the instance can consume excessive CPU and memory resources when there are a large number
  of threads and/or open file handles on the node.

###### Changes, enhancements, and

resolved issues

- Starting with Spark 3.3.1 (supported in EMR versions 6.10 and above), all executors in a decommissioning host are set to a new `ExecutorState`, called _DECOMMISSIONING_ state. The executors
  being decommissioned cannot be used by Yarn to allocate tasks and thus it will request for new executors, if needed, for the tasks being executed. Thus, if you disable Spark DRA while using
  EMR Managed Scaling, EMR Auto Scaling, or any custom scaling mechanism on EMR-EC2 clusters, then Yarn may request maximum permissible executors for each job. In order to avoid this issue,
  leave the `spark.dynamicAllocation.enabled` property set to `TRUE` (which is the default) when you are using the above combination of features. In addition, you can also
  set minimum and maximum executor constraints by setting values for `spark.dynamicAllocation.maxExecutors` and `spark.dynamicAllocation.minExecutors` properties for your Spark jobs, to restrict the number of executors allocated during the job’s execution.
- The 6.14.0 release optimizes log management with Amazon EMR
  running on Amazon EC2. As a result, you might see a
  slight reduction in storage costs for your cluster
  logs.
- The 6.14.0 release improves the scaling workflow to
  account for different core instances that have a
  substantial variation in size for their Amazon EBS
  volumes. This improvement applies to core nodes
  only; scale-down operations for task nodes aren’t
  affected.
- The 6.14.0 release improves the way that Amazon EMR interacts
  with open-source applications such as Apache
  Hadoop YARN ResourceManager and HDFS
  NameNode. This improvement reduces the
  risk of operational delays with cluster scaling, and
  mitigates startup failures that occur due to
  connectivity issues with the open-source
  applications.
- The 6.14.0 release optimizes application installation
  at cluster launch. This improves the cluster startup
  times for certain combinations of Amazon EMR
  applications.
- The 6.14.0 release fixes an issue where cluster
  scale-down operations might stall when a cluster that's
  running in a VPC with a custom domain encounters a core or task node
  restart.
- When you launch a cluster with _the latest patch release_ of Amazon EMR 5.36 or higher, 6.6 or higher, or 7.0 or higher, Amazon EMR uses the latest Amazon Linux 2023 or Amazon Linux 2 release for the
  default Amazon EMR AMI. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](../ManagementGuide/emr-default-ami.md "../ManagementGuide/emr-default-ami.md").

| OsReleaseLabel (Amazon Linux version) | Amazon Linux kernel version | Available date     | Supported Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------- | --------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0.20250721.2                        | 4.14.355-280.652.amzn2      | August 14, 2025    | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Taipei), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Malaysia), Asia Pacific (Thailand), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), Mexico (Central), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon) |
| 2.0.20250623.0                        | 4.14.355-277.647.amzn2      | July 21, 2025      | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Taipei), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Malaysia), Asia Pacific (Thailand), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), Mexico (Central), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon) |
| 2.0.20250610.0                        | 4.14.355-277.647.amzn2      | July 14, 2025      | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Europe (Spain), China (Ningxia), Europe (Zurich)                                                                                                                                             |
| 2.0.20250527.1                        | 4.14.355-277.647.amzn2      | Jun 19, 2025       | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Malaysia), Europe (London), Asia Pacific (Melbourne), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), Mexico (Central), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Asia Pacific (Taipei), Canada (Central), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) |
| 2.0.20250512.0                        | 4.14.355-277.643.amzn2      | Jun 04, 2025       | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Stockholm), Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250428.0                        | 4.14.355-276.639.amzn2      | May 23, 2025       | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Thailand), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Canada West (Calgary), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia), Israel (Tel Aviv), Mexico (Central)                        |
| 2.0.20250414.0                        | 4.14.355-276.618.amzn2      | May 12, 2025       | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250321.0                        | 4.14.355                    | April 09, 2025     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250305.0                        | 4.14.355                    | March 18, 2025     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250220.0                        | 4.14.355                    | March 08, 2025     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250201.0                        | 4.14.355                    | February 28, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250123.4                        | 4.14.355                    | January 27, 2025   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250116.0                        | 4.14.355                    | January 23, 2025   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20241217.0                        | 4.14.355                    | January 8, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Middle East (UAE), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Zurich), Asia Pacific (Malaysia)                                                                                                             |
| 2.0.20240709.1                        | 4.14.348                    | July 23, 2024      | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Europe (Stockholm), Europe (Milan),<br>Europe (Frankfurt),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Jakarta),<br>Africa (Cape Town), South America (São Paulo), Middle East (Bahrain),<br>Canada (Central),<br>AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia),<br>Asia Pacific (Hyderabad), Middle East (UAE), Europe (Spain), Europe (Zurich),<br>Asia Pacific (Melbourne), Israel (Tel Aviv),<br>Canada West (Calgary)                                                  |
| 2.0.20240223.0                        | 4.14.336                    | March 8, 2024      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                                                                            |
| 2.0.20240131.0                        | 4.14.336                    | February 14, 2024  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                                                                            |
| 2.0.20240124.0                        | 4.14.336                    | February 7, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                                                                            |
| 2.0.20240109.0                        | 4.14.334                    | January 24, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central),Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                                                                             |
| 2.0.20231218.0                        | 4.14.330                    | January 2, 2024    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231206.0                        | 4.14.330                    | December 22, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231116.0                        | 4.14.328                    | December 11, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231101.0                        | 4.14.327                    | November 17, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20230906.0                        | 4.14.322                    | September 11, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                                                                     |

## Release 6.13.0

The following release notes include information for Amazon EMR release
6.13.0. Changes are relative to 6.12.0. For information on the
release timeline, see the [6.13.0 change log](emr-6130-release.md#6130-changelog "emr-6130-release.md#6130-changelog").

###### New features

- Amazon EMR 6.13.0 supports Apache Spark 3.4.1, Apache Spark RAPIDS 23.06.0-amzn-1, CUDA Toolkit 11.8.0, and JupyterHub 1.5.0.

###### Known issues

- An on-cluster instance-state script that monitors health of the instance can consume excessive CPU and memory resources when there are a large number
  of threads and/or open file handles on the node.

###### Changes, enhancements, and

resolved issues

- Starting with Spark 3.3.1 (supported in EMR versions 6.10 and above), all executors in a decommissioning host are set to a new `ExecutorState`, called _DECOMMISSIONING_ state. The executors
  being decommissioned cannot be used by Yarn to allocate tasks and thus it will request for new executors, if needed, for the tasks being executed. Thus, if you disable Spark DRA while using
  EMR Managed Scaling, EMR Auto Scaling, or any custom scaling mechanism on EMR-EC2 clusters, then Yarn may request maximum permissible executors for each job. In order to avoid this issue,
  leave the `spark.dynamicAllocation.enabled` property set to `TRUE` (which is the default) when you are using the above combination of features. In addition, you can also
  set minimum and maximum executor constraints by setting values for `spark.dynamicAllocation.maxExecutors` and `spark.dynamicAllocation.minExecutors` properties for your Spark jobs, to restrict the number of executors allocated during the job’s execution.
- The 6.13.0 release improves the Amazon EMR log management daemon to ensure that all logs are uploaded at a regular cadence to Amazon S3 when a cluster termination command is issued. This facilitates faster cluster terminations.
- The 6.13.0 release enhances Amazon EMR log management capabilities to ensure consistent and timely upload of all log files to Amazon S3. This especially benefits long-running EMR clusters.
- When you launch a cluster with _the latest patch release_ of Amazon EMR 5.36 or higher, 6.6 or higher, or 7.0 or higher, Amazon EMR uses the latest Amazon Linux 2023 or Amazon Linux 2 release for the
  default Amazon EMR AMI. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](../ManagementGuide/emr-default-ami.md "../ManagementGuide/emr-default-ami.md").

| OsReleaseLabel (Amazon Linux version) | Amazon Linux kernel version | Available date    | Supported Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------- | --------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0.20250721.2                        | 4.14.355-280.652.amzn2      | August 14, 2025   | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                           |
| 2.0.20250623.0                        | 4.14.355-277.647.amzn2      | July 21, 2025     | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                           |
| 2.0.20250610.0                        | 4.14.355-277.647.amzn2      | July 14, 2025     | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Europe (Spain), China (Ningxia), Europe (Zurich)                                                                                            |
| 2.0.20250527.1                        | 4.14.355-277.647.amzn2      | Jun 19, 2025      | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Melbourne), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich)                                           |
| 2.0.20250512.0                        | 4.14.355-277.643.amzn2      | Jun 04, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Stockholm), Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250428.0                        | 4.14.355-276.639.amzn2      | May 23, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Canada West (Calgary), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia), Israel (Tel Aviv)                                           |
| 2.0.20250414.0                        | 4.14.355-276.618.amzn2      | May 12, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250321.0                        | 4.14.355                    | April 09, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250305.0                        | 4.14.355                    | March 18, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250220.0                        | 4.14.355                    | March 08, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250201.0                        | 4.14.355                    | February 28, 2025 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250123.4                        | 4.14.355                    | January 27, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250116.0                        | 4.14.355                    | January 23, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20241217.0                        | 4.14.355                    | January 8, 2025   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Middle East (UAE), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Zurich)                                                                                     |
| 2.0.20241001.0                        | 4.14.352                    | October 4, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240816.0                        | 4.14.350                    | August 21, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240809.0                        | 4.14.349                    | August 20, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240719.0                        | 4.14.348                    | July 25, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240709.1                        | 4.14.348                    | July 23, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Europe (Stockholm), Europe (Milan),<br>Europe (Frankfurt),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Jakarta),<br>Africa (Cape Town), South America (São Paulo), Middle East (Bahrain),<br>Canada (Central),<br>AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia),<br>Asia Pacific (Hyderabad), Middle East (UAE), Europe (Spain), Europe (Zurich),<br>Asia Pacific (Melbourne), Israel (Tel Aviv),<br>Canada West (Calgary) |
| 2.0.20240223.0                        | 4.14.336                    | March 8, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                           |
| 2.0.20240131.0                        | 4.14.336                    | February 14, 2024 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                           |
| 2.0.20240124.0                        | 4.14.336                    | February 7, 2024  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                           |
| 2.0.20240109.0                        | 4.14.334                    | January 24, 2024  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                           |
| 2.0.20231218.0                        | 4.14.330                    | January 2, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20231206.0                        | 4.14.330                    | December 22, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20231116.0                        | 4.14.328                    | December 11, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20231101.0                        | 4.14.327                    | November 16, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20231020.1                        | 4.14.326                    | November 7, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20231012.1                        | 4.14.326                    | October 26, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20230926.0                        | 4.14.322                    | October 19, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20230906.0                        | 4.14.322                    | October 4, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |
| 2.0.20230808.0                        | 4.14.320                    | August 24, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |

## Release 6.12.0

The following release notes include information for Amazon EMR release
6.12.0. Changes are relative to 6.11.0. For information on the
release timeline, see the [6.12.0 change log](emr-6120-release.md#6120-changelog "emr-6120-release.md#6120-changelog").

###### New features

- Amazon EMR 6.12.0 supports Apache Spark 3.4.0,
  Apache Spark RAPIDS 23.06.0-amzn-0, CUDA 11.8.0,
  Apache Hudi 0.13.1-amzn-0, Apache Iceberg
  1.3.0-amzn-0, Trino 414, and PrestoDB
  0.281.
- Amazon EMR releases 6.12.0 and higher support LDAP
  integration with Apache Livy, Apache Hive through
  HiveServer2 (HS2), Trino, Presto, and Hue. You can
  also install Apache Spark and Apache Hadoop on an
  EMR cluster that uses 6.12.0 or higher and
  configure them to use LDAP. For more information,
  see [Use
  Active Directory or LDAP servers for
  authentication with Amazon EMR](../ManagementGuide/ldap.md "../ManagementGuide/ldap.md").

###### Known issues

- An on-cluster instance-state script that monitors health of the instance can consume excessive CPU and memory resources when there are a large number
  of threads and/or open file handles on the node.

###### Changes, enhancements, and

resolved issues

- Starting with Spark 3.3.1 (supported in EMR versions 6.10 and above), all executors in a decommissioning host are set to a new `ExecutorState`, called _DECOMMISSIONING_ state. The executors
  being decommissioned cannot be used by Yarn to allocate tasks and thus it will request for new executors, if needed, for the tasks being executed. Thus, if you disable Spark DRA while using
  EMR Managed Scaling, EMR Auto Scaling, or any custom scaling mechanism on EMR-EC2 clusters, then Yarn may request maximum permissible executors for each job. In order to avoid this issue,
  leave the `spark.dynamicAllocation.enabled` property set to `TRUE` (which is the default) when you are using the above combination of features. In addition, you can also
  set minimum and maximum executor constraints by setting values for `spark.dynamicAllocation.maxExecutors` and `spark.dynamicAllocation.minExecutors` properties for your Spark jobs, to restrict the number of executors allocated during the job’s execution.
- Amazon EMR releases 6.12.0 and higher provide Java 11
  runtime support for Flink. For more information, see
  [Configure Flink to run with
  Java 11](flink-configure.md#flink-configure-java11 "flink-configure.md#flink-configure-java11").
- The 6.12.0 release adds a new retry
  mechanism to the cluster scaling workflow for
  EMR clusters that run Presto or Trino.
  This improvement reduces the risk that cluster resizing
  will indefinitely stall due to a single failed resize
  operation. It also improves cluster utilization,
  because your cluster scales up and down faster.
- The 6.12.0 release fixes an issue where cluster
  scale-down operations might stall when a core node
  that is undergoing graceful decommissioning turns
  unhealthy for any reason before it fully
  decommissions.
- The 6.12.0 release improves cluster scale-down logic
  so that your cluster doesn't attempt a
  scale-down of core nodes below the HDFS replication
  factor setting for the cluster. This aligns with
  your data redundancy requirements, and reduces the
  chance that a scaling operation might stall.
- The 6.12.0 release enhances the performance and
  efficiency of the health monitoring service for
  Amazon EMR by increasing the speed at which it logs state
  changes for instances. This improvement reduces the
  chance of degraded performance for cluster nodes
  that are running multiple custom client tools or
  third-party applications.
- The 6.12.0 release improves the performance of the
  on-cluster log management daemon for Amazon EMR. As a
  result, there is less chance for degraded
  performance with EMR clusters that run steps with
  high concurrency.
- With Amazon EMR release 6.12.0, the log management daemon
  has been upgraded to identify all logs that are in
  active use with open file handles on the local
  instance storage, and the associated processes. This
  upgrade ensures that Amazon EMR properly deletes the
  files and reclaims storage space after the logs are
  archived to Amazon S3.
- The 6.12.0 release includes a log-management daemon
  enhancement that deletes empty, unused steps
  directories in the local cluster file system. An
  excessively large number of empty directories can
  degrade the performance of Amazon EMR daemons and result
  in disk over-utilization.
- The 6.12.0 release enables log rotation for YARN
  Timeline Server logs. This minimizes disk
  over-utilization scenarios, especially for
  long-running clusters.
- The default root volume size has increased to 15 GB in Amazon EMR 6.10.0 and higher. Earlier releases have default root volume size of 10 GB.
- When you launch a cluster with _the latest patch release_ of Amazon EMR 5.36 or higher, 6.6 or higher, or 7.0 or higher, Amazon EMR uses the latest Amazon Linux 2023 or Amazon Linux 2 release for the
  default Amazon EMR AMI. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](../ManagementGuide/emr-default-ami.md "../ManagementGuide/emr-default-ami.md").

| OsReleaseLabel (Amazon Linux version) | Amazon Linux kernel version | Available date    | Supported Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------- | --------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0.20250721.2                        | 4.14.355-280.652.amzn2      | August 14, 2025   | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                           |
| 2.0.20250623.0                        | 4.14.355-277.647.amzn2      | July 21, 2025     | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                           |
| 2.0.20250610.0                        | 4.14.355-277.647.amzn2      | July 14, 2025     | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Europe (Spain), China (Ningxia), Europe (Zurich)                                                                                            |
| 2.0.20250527.1                        | 4.14.355-277.647.amzn2      | Jun 19, 2025      | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Melbourne), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich)                                           |
| 2.0.20250512.0                        | 4.14.355-277.643.amzn2      | Jun 04, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Stockholm), Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250428.0                        | 4.14.355-276.639.amzn2      | May 23, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Canada West (Calgary), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia), Israel (Tel Aviv)                                           |
| 2.0.20250414.0                        | 4.14.355-276.618.amzn2      | May 12, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250321.0                        | 4.14.355                    | April 09, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250305.0                        | 4.14.355                    | March 18, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250220.0                        | 4.14.355                    | March 08, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250201.0                        | 4.14.355                    | February 28, 2025 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250123.4                        | 4.14.355                    | January 27, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250116.0                        | 4.14.355                    | January 23, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20241217.0                        | 4.14.355                    | January 8, 2025   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Middle East (UAE), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Zurich)                                                                                     |
| 2.0.20241001.0                        | 4.14.352                    | October 4, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240816.0                        | 4.14.350                    | August 21, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240809.0                        | 4.14.349                    | August 20, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240719.0                        | 4.14.348                    | July 25, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240709.1                        | 4.14.348                    | July 23, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Europe (Stockholm), Europe (Milan),<br>Europe (Frankfurt),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Jakarta),<br>Africa (Cape Town), South America (São Paulo), Middle East (Bahrain),<br>Canada (Central),<br>AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia),<br>Asia Pacific (Hyderabad), Middle East (UAE), Europe (Spain), Europe (Zurich),<br>Asia Pacific (Melbourne), Israel (Tel Aviv),<br>Canada West (Calgary) |
| 2.0.20240223.0                        | 4.14.336                    | March 8, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                           |
| 2.0.20240131.0                        | 4.14.336                    | February 14, 2024 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                           |
| 2.0.20240124.0                        | 4.14.336                    | February 7, 2024  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                           |
| 2.0.20240109.0                        | 4.14.334                    | January 24, 2024  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                           |
| 2.0.20231218.0                        | 4.14.330                    | January 2, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20231206.0                        | 4.14.330                    | December 22, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20231116.0                        | 4.14.328                    | December 11, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20231101.0                        | 4.14.327                    | November 16, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20231020.1                        | 4.14.326                    | November 7, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20231012.1                        | 4.14.326                    | October 26, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20230926.0                        | 4.14.322                    | October 19, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                  |
| 2.0.20230906.0                        | 4.14.322                    | October 4, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |
| 2.0.20230822.0                        | 4.14.322                    | Augest 30, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |
| 2.0.20230808.0                        | 4.14.320                    | August 24, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |
| 2.0.20230727.0                        | 4.14.320                    | August 14, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |
| 2.0.20230719.0                        | 4.14.320                    | August 2, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |
| 2.0.20230628.0                        | 4.14.318                    | July 12, 2023     | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Europe (Stockholm), Europe (Milan),<br>Europe (Spain), Europe (Frankfurt),<br>Europe (Zurich), Europe (Ireland),<br>Europe (London), Europe (Paris),<br>Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Hyderabad), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Jakarta), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain),<br>Middle East (UAE),<br>Canada (Central)                                                                                                                                                          |

## Release 6.11.1

The following release notes include information for Amazon EMR release
6.11.1. Changes are relative to 6.11.0. For information on the
release timeline, see the [6.11.1 change log](emr-6111-release.md#6111-changelog "emr-6111-release.md#6111-changelog").

###### Changes, enhancements, and

resolved issues

- Starting with Spark 3.3.1 (supported in EMR versions 6.10 and above), all executors in a decommissioning host are set to a new `ExecutorState`, called _DECOMMISSIONING_ state. The executors
  being decommissioned cannot be used by Yarn to allocate tasks and thus it will request for new executors, if needed, for the tasks being executed. Thus, if you disable Spark DRA while using
  EMR Managed Scaling, EMR Auto Scaling, or any custom scaling mechanism on EMR-EC2 clusters, then Yarn may request maximum permissible executors for each job. In order to avoid this issue,
  leave the `spark.dynamicAllocation.enabled` property set to `TRUE` (which is the default) when you are using the above combination of features. In addition, you can also
  set minimum and maximum executor constraints by setting values for `spark.dynamicAllocation.maxExecutors` and `spark.dynamicAllocation.minExecutors` properties for your Spark jobs, to restrict the number of executors allocated during the job’s execution.
- Due to lock contention, a node can enter into a
  deadlock if it's added or removed at the same time
  that it attempts to decommission. As a result, the
  Hadoop Resource Manager (YARN) becomes unresponsive,
  and affects all the incoming and currently-running
  containers.
- This release includes a change that allows
  high-availability clusters to recover from failed
  state after restart.
- This release includes security fixes for Hue and
  HBase.
- This release fixes an issue where clusters that are
  running workloads on Spark with Amazon EMR might silently
  receive incorrect results with
  `contains`, `startsWith`,
  `endsWith`, and `like`. This
  issue occurs when you use the expressions on
  partitioned fields that have metadata in the Amazon EMR
  Hive3 Metastore Server (HMS).
- This release fixes an issue with throttling on the
  Glue side when there are no user-defined functions
  (UDF).
- This release fixes an issue that deletes container
  logs by the node log aggregation service before log
  pusher can push them to S3 in case of YARN
  decommissioning.
- This release fixes an issue with FairShare Scheduler
  metrics when Node Label is enabled for
  Hadoop.
- This release fixes an issue that impacted Spark
  performance when you set a default `true`
  value for the
  `spark.yarn.heterogeneousExecutors.enabled`
  config in
  `spark-defaults.conf`.
- This release fixes an issue with Reduce Task failing
  to read shuffle data. The issue caused Hive query
  failures with a corrupted memory error.
- This release adds a new retry
  mechanism to the cluster scaling workflow for
  EMR clusters that run Presto or Trino.
  This improvement reduces the risk that cluster resizing
  will indefinitely stall due to a single failed resize
  operation. It also improves cluster utilization,
  because your cluster scales up and down faster.
- This release improves cluster scale-down logic
  so that your cluster doesn't attempt a
  scale-down of core nodes below the HDFS replication
  factor setting for the cluster. This aligns with
  your data redundancy requirements, and reduces the
  chance that a scaling operation might stall.
- The log management daemon
  has been upgraded to identify all logs that are in
  active use with open file handles on the local
  instance storage, and the associated processes. This
  upgrade ensures that Amazon EMR properly deletes the
  files and reclaims storage space after the logs are
  archived to Amazon S3.
- This release includes a log-management daemon
  enhancement that deletes empty, unused steps
  directories in the local cluster file system. An
  excessively large number of empty directories can
  degrade the performance of Amazon EMR daemons and result
  in disk over-utilization.
- When you launch a cluster with _the latest patch release_ of Amazon EMR 5.36 or higher, 6.6 or higher, or 7.0 or higher, Amazon EMR uses the latest Amazon Linux 2023 or Amazon Linux 2 release for the
  default Amazon EMR AMI. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](../ManagementGuide/emr-default-ami.md "../ManagementGuide/emr-default-ami.md").

| OsReleaseLabel (Amazon Linux Version) | Amazon Linux Kernel Version | Available Date    | Supported Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------- | --------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0.20250721.2                        | 4.14.355-280.652.amzn2      | August 14, 2025   | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Taipei), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Malaysia), Asia Pacific (Thailand), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), Mexico (Central), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon) |
| 2.0.20250623.0                        | 4.14.355-277.647.amzn2      | July 21, 2025     | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Taipei), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Malaysia), Asia Pacific (Thailand), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), Mexico (Central), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon) |
| 2.0.20250610.0                        | 4.14.355-277.647.amzn2      | July 14, 2025     | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Europe (Spain), China (Ningxia), Europe (Zurich)                                                                                                                                             |
| 2.0.20250527.1                        | 4.14.355-277.647.amzn2      | Jun 19, 2025      | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Malaysia), Europe (London), Asia Pacific (Melbourne), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), Mexico (Central), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Asia Pacific (Taipei), Canada (Central), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) |
| 2.0.20250512.0                        | 4.14.355-277.643.amzn2      | Jun 04, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Stockholm), Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250428.0                        | 4.14.355-276.639.amzn2      | May 23, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Thailand), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Canada West (Calgary), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia), Israel (Tel Aviv), Mexico (Central)                        |
| 2.0.20250414.0                        | 4.14.355-276.618.amzn2      | May 12, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250321.0                        | 4.14.355                    | April 09, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250305.0                        | 4.14.355                    | March 18, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250220.0                        | 4.14.355                    | March 08, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250201.0                        | 4.14.355                    | February 28, 2025 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250123.4                        | 4.14.355                    | January 27, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20250116.0                        | 4.14.355                    | January 23, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20241217.0                        | 4.14.355                    | January 8, 2025   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Middle East (UAE), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Zurich), Asia Pacific (Malaysia)                                                                                                             |
| 2.0.20241001.0                        | 4.14.352                    | October 4, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20240816.0                        | 4.14.350                    | August 21, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20240809.0                        | 4.14.349                    | August 20, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20240719.0                        | 4.14.348                    | July 25, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                                                                              |
| 2.0.20240709.1                        | 4.14.348                    | July 23, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Europe (Stockholm), Europe (Milan),<br>Europe (Frankfurt),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Jakarta),<br>Africa (Cape Town), South America (São Paulo), Middle East (Bahrain),<br>Canada (Central),<br>AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia),<br>Asia Pacific (Hyderabad), Middle East (UAE), Europe (Spain), Europe (Zurich),<br>Asia Pacific (Melbourne), Israel (Tel Aviv),<br>Canada West (Calgary)                                                  |
| 2.0.20240223.0                        | 4.14.336                    | March 8, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                                                                            |
| 2.0.20240131.0                        | 4.14.336                    | February 14, 2024 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                                                                            |
| 2.0.20240124.0                        | 4.14.336                    | February 7, 2024  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                                                                            |
| 2.0.20240109.0                        | 4.14.334                    | January 24, 2024  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Canada West (Calgary)                                                                                            |
| 2.0.20231218.0                        | 4.14.330                    | January 2, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231206.0                        | 4.14.330                    | December 22, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231116.0                        | 4.14.328                    | December 11, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231101.0                        | 4.14.327                    | November 16, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231020.1                        | 4.14.326                    | November 7, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231012.1                        | 4.14.326                    | October 26, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20230926.0                        | 4.14.322                    | October 19, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20230906.0                        | 4.14.322                    | October 4, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                                                                     |
| 2.0.20230822.0                        | 4.14.322                    | Augest 30, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                                                                     |
| 2.0.20230808.0                        | 4.14.320                    | August 24, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                                                                     |
| 2.0.20230727.0                        | 4.14.320                    | August 14, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central)                                                                                                                                                                                                                                                                                                                                |

## Release 6.11.0

The following release notes include information for Amazon EMR release
6.11.0. Changes are relative to 6.10.0. For information on the
release timeline, see the [change log](emr-6110-release.md#6110-changelog "emr-6110-release.md#6110-changelog").

###### New features

- Amazon EMR 6.11.0 supports
  Apache Spark 3.3.2-amzn-0,
  Apache Spark RAPIDS 23.02.0-amzn-0,
  CUDA 11.8.0,
  Apache Hudi 0.13.0-amzn-0,
  Apache Iceberg 1.2.0-amzn-0,
  Trino 410-amzn-0, and
  PrestoDB 0.279-amzn-0.

###### Changes, enhancements, and

resolved issues

- Starting with Spark 3.3.1 (supported in EMR versions 6.10 and above), all executors in a decommissioning host are set to a new `ExecutorState`, called _DECOMMISSIONING_ state. The executors
  being decommissioned cannot be used by Yarn to allocate tasks and thus it will request for new executors, if needed, for the tasks being executed. Thus, if you disable Spark DRA while using
  EMR Managed Scaling, EMR Auto Scaling, or any custom scaling mechanism on EMR-EC2 clusters, then Yarn may request maximum permissible executors for each job. In order to avoid this issue,
  leave the `spark.dynamicAllocation.enabled` property set to `TRUE` (which is the default) when you are using the above combination of features. In addition, you can also
  set minimum and maximum executor constraints by setting values for `spark.dynamicAllocation.maxExecutors` and `spark.dynamicAllocation.minExecutors` properties for your Spark jobs, to restrict the number of executors allocated during the job’s execution.
- With Amazon EMR 6.11.0, the DynamoDB connector has been upgraded to version 5.0.0. Version 5.0.0 uses AWS SDK for Java 2.x. Previous releases used AWS SDK for Java 1.x. As a result of this upgrade, we strongly advise you to test your code before you use the DynamoDB connector with Amazon EMR 6.11.
- When the DynamoDB connector for Amazon EMR 6.11.0 calls the DynamoDB service, it uses the Region value that you provide for the `dynamodb.endpoint` property. We recommend that you also configure `dynamodb.region` when you use `dynamodb.endpoint`, and that both properties target the same AWS Region. If you use `dynamodb.endpoint` and you don't configure `dynamodb.region`, the DynamoDB connector for Amazon EMR 6.11.0 will return an invalid Region exception and attempt to reconcile your AWS Region information from the Amazon EC2 instance metadata service (IMDS). If the connector can't retrieve the Region from IMDS, it defaults to US East (N. Virginia) (`us-east-1`). The following error is an example of the invalid Region exception that you might get if you don't properly configure the `dynamodb.region` property: `error software.amazon.awssdk.services.dynamodb.model.DynamoDbException: Credential should be scoped to a valid region.` For more information on the classes that are affected by the AWS SDK for Java upgrade to 2.x, see the [Upgrade AWS SDK for Java from 1.x to 2.x (#175)](https://github.com/awslabs/emr-dynamodb-connector/commit/1dec9d1972d3673c3fae6c6ea51f19f295147ccf "https://github.com/awslabs/emr-dynamodb-connector/commit/1dec9d1972d3673c3fae6c6ea51f19f295147ccf") commit in the GitHub repo for the Amazon EMR - DynamoDB connector.
- This release fixes an issue where column data becomes `NULL` when you use Delta Lake to store Delta table data in Amazon S3 after column rename operation. For more
  information about this experimental feature in Delta Lake, see [Column
  rename operation](https://docs.delta.io/latest/delta-batch.html#rename-columns "https://docs.delta.io/latest/delta-batch.html#rename-columns") in the Delta Lake User Guide.
- The 6.11.0 release fixes an issue that might occur
  when you create an edge node by replicating one of
  the primary nodes from a cluster with multiple
  primary nodes. The replicated edge node could cause
  delays with scale-down operations, or result in high
  memory-utilization on the primary nodes. For more
  information on how to create an edge node to
  communicate with your EMR cluster, see [Edge Node Creator](https://github.com/aws-samples/aws-emr-utilities/tree/main/utilities/emr-edge-node-creator "https://github.com/aws-samples/aws-emr-utilities/tree/main/utilities/emr-edge-node-creator") in the
  `aws-samples` repo on GitHub.
- The 6.11.0 release improves the automation process
  that Amazon EMR uses to re-mount Amazon EBS volumes to an
  instance after a reboot.
- The 6.11.0 release fixes an issue that resulted in
  intermittent gaps in the Hadoop metrics that Amazon EMR
  publishes to Amazon CloudWatch.
- The 6.11.0 release fixes an issue with EMR clusters
  where an update to the YARN configuration file that contains
  the exclusion list of nodes for the cluster is interrupted
  due to disk over-utilization. The incomplete
  update hinders future cluster scale-down operations. This
  release ensures that your cluster remains healthy, and that
  scaling operations work as expected.
- The default root volume size has increased to 15 GB in Amazon EMR 6.10.0 and higher. Earlier releases have default root volume size of 10 GB.
- Hadoop 3.3.3 introduced a change in YARN ([YARN-9608](https://issues.apache.org/jira/browse/YARN-9608 "https://issues.apache.org/jira/browse/YARN-9608"))
  that keeps nodes where containers ran in a
  decommissioning state until the application
  completes. This change ensures that local data such
  as shuffle data doesn't get lost, and you don' need to re-run the job.
  This approach might also lead to
  underutilization of resources on clusters with or
  without managed scaling enabled.

With Amazon EMR releases 6.11.0 and higher as well as 6.8.1, 6.9.1,
and 6.10.1, the value of
`yarn.resourcemanager.decommissioning-nodes-watcher.wait-for-applications`
is set to `false` in `yarn-site.xml`
to resolve this issue.

While the fix
addresses the issues that were introduced by
YARN-9608, it might cause Hive jobs to fail due to
shuffle data loss on clusters that have managed
scaling enabled. We've mitigated that risk in this release by also setting
`yarn.resourcemanager.decommissioning-nodes-watcher.wait-for-shuffle-data`
for Hive workloads. This config is only available
with Amazon EMR releases 6.11.0 and higher.

- When you launch a cluster with _the latest patch release_ of Amazon EMR 5.36 or higher, 6.6 or higher, or 7.0 or higher, Amazon EMR uses the latest Amazon Linux 2023 or Amazon Linux 2 release for the
  default Amazon EMR AMI. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](../ManagementGuide/emr-default-ami.md "../ManagementGuide/emr-default-ami.md").

###### Note

This release no longer gets automatic AMI updates since it has been succeeded by 1 more more patch releases. The patch release is denoted by the number after the
second decimal point (`6.8.`1``). To see if you're using the latest patch release, check the available releases in the [*Release Guide*](../ReleaseGuide.md "../ReleaseGuide.md"), or check the **Amazon EMR release** dropdown when you create a cluster in the console, or use the [`ListReleaseLabels`](../APIReference/API_ListReleaseLabels.md "../APIReference/API_ListReleaseLabels.md") API or [`list-release-labels`](../../../cli/latest/reference/emr/list-release-labels.md "../../../cli/latest/reference/emr/list-release-labels.md") CLI action. To get updates about new releases, subscribe to the RSS feed on the [What's new?](emr-whatsnew.md "emr-whatsnew.md") page.

| OsReleaseLabel (Amazon Linux version) | Amazon Linux kernel version | Available date    | Supported Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------- | --------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0.20250721.2                        | 4.14.355-280.652.amzn2      | August 14, 2025   | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                           |
| 2.0.20250623.0                        | 4.14.355-277.647.amzn2      | July 21, 2025     | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                           |
| 2.0.20250610.0                        | 4.14.355-277.647.amzn2      | July 14, 2025     | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Europe (Spain), China (Ningxia), Europe (Zurich)                                                                                            |
| 2.0.20250527.1                        | 4.14.355-277.647.amzn2      | Jun 19, 2025      | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Melbourne), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich)                                           |
| 2.0.20250512.0                        | 4.14.355-277.643.amzn2      | Jun 04, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Stockholm), Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250428.0                        | 4.14.355-276.639.amzn2      | May 23, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Canada West (Calgary), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia), Israel (Tel Aviv)                                           |
| 2.0.20250414.0                        | 4.14.355-276.618.amzn2      | May 12, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250321.0                        | 4.14.355                    | April 09, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250305.0                        | 4.14.355                    | March 18, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250220.0                        | 4.14.355                    | March 08, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250201.0                        | 4.14.355                    | February 28, 2025 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250123.4                        | 4.14.355                    | January 27, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250116.0                        | 4.14.355                    | January 23, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20241217.0                        | 4.14.355                    | January 8, 2025   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Middle East (UAE), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Zurich)                                                                                     |
| 2.0.20241001.0                        | 4.14.352                    | October 4, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240816.0                        | 4.14.350                    | August 21, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240809.0                        | 4.14.349                    | August 20, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240719.0                        | 4.14.348                    | July 25, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240709.1                        | 4.14.348                    | July 23, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Europe (Stockholm), Europe (Milan),<br>Europe (Frankfurt),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Jakarta),<br>Africa (Cape Town), South America (São Paulo), Middle East (Bahrain),<br>Canada (Central),<br>AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia),<br>Asia Pacific (Hyderabad), Middle East (UAE), Europe (Spain), Europe (Zurich),<br>Asia Pacific (Melbourne), Israel (Tel Aviv),<br>Canada West (Calgary) |
| 2.0.20230808.0                        | 4.14.320                    | August 24, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), Israel (Tel Aviv)                                                                                                                                                                                                                                  |
| 2.0.20230727.0                        | 4.14.320                    | August 14, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |
| 2.0.20230719.0                        | 4.14.320                    | August 2, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |
| 2.0.20230628.0                        | 4.14.318                    | July 12, 2023     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Zurich), Europe (Milan),<br>Europe (Spain), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain), Middle East (UAE)                                                                                                                                                                         |
| 2.0.20230612.0                        | 4.14.314                    | June 23, 2023     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Zurich), Europe (Milan),<br>Europe (Spain), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain), Middle East (UAE)                                                                                                                                                                         |
| 2.0.20230504.1                        | 4.14.313                    | May 16, 2023      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central)                                                                                                                                                                                                 |

## Release 6.10.0

The following release notes include information for Amazon EMR release
6.10.0. Changes are relative to 6.9.0. For information on the
release timeline, see the [change log](emr-6100-release.md#6100-changelog "emr-6100-release.md#6100-changelog").

###### New features

- Amazon EMR 6.10.0 supports Apache Spark 3.3.1, Apache Spark
  RAPIDS 22.12.0, CUDA 11.8.0, Apache Hudi 0.12.2-amzn-0,
  Apache Iceberg 1.1.0-amzn-0, Trino 403, and PrestoDB
  0.278.1.
- Amazon EMR 6.10.0 includes a native Trino-Hudi connector that provides read access to data in Hudi tables. You can activate the connector with `trino-cli --catalog hudi`, and configure the connector for your requirements with `trino-connector-hudi`. The native integration with Amazon EMR means that you no longer need to use `trino-connector-hive` to query Hudi tables. For a list of supported configurations with the new connector, see the [Hudi connector](https://trino.io/docs/current/connector/hudi.html "https://trino.io/docs/current/connector/hudi.html") page of the Trino documentation.
- Amazon EMR releases 6.10.0 and higher support Apache Zeppelin integration with Apache
  Flink. See [Working with Flink jobs from Zeppelin in Amazon EMR](flink-zeppelin.md "flink-zeppelin.md") for more
  information.

###### Known Issues

- Hadoop 3.3.3 introduced a change in YARN ([YARN-9608](https://issues.apache.org/jira/browse/YARN-9608 "https://issues.apache.org/jira/browse/YARN-9608"))
  that keeps nodes where containers ran in a
  decommissioning state until the application
  completes. This change ensures that local data such
  as shuffle data doesn't get lost, and you don' need to re-run the job.
  This approach might also lead to
  underutilization of resources on clusters with or
  without managed scaling enabled.

To work around this issue in Amazon EMR 6.10.0, you can set the value of
`yarn.resourcemanager.decommissioning-nodes-watcher.wait-for-applications`
to `false` in `yarn-site.xml`.
In Amazon EMR releases 6.11.0 and higher as well as 6.8.1, 6.9.1,
and 6.10.1, the config is set to `false` by default to resolve this issue.

- Starting with Spark 3.3.1 (supported in EMR versions 6.10 and above), all executors in a decommissioning host are set to a new `ExecutorState`, called _DECOMMISSIONING_ state. The executors
  being decommissioned cannot be used by Yarn to allocate tasks and thus it will request for new executors, if needed, for the tasks being executed. Thus, if you disable Spark DRA while using
  EMR Managed Scaling, EMR Auto Scaling, or any custom scaling mechanism on EMR-EC2 clusters, then Yarn may request maximum permissible executors for each job. In order to avoid this issue,
  leave the `spark.dynamicAllocation.enabled` property set to `TRUE` (which is the default) when you are using the above combination of features. In addition, you can also
  set minimum and maximum executor constraints by setting values for `spark.dynamicAllocation.maxExecutors` and `spark.dynamicAllocation.minExecutors` properties for your Spark jobs, to restrict the number of executors allocated during the job’s execution.

###### Changes, enhancements, and

resolved issues

- Amazon EMR 6.10.0 removes the dependency on `minimal-json.jar` for the [Amazon Redshift integration for Apache Spark](emr-spark-redshift-launch.md "emr-spark-redshift-launch.md"), and automatically adds the required Spark-Redshift related jars to the executor class path for Spark: `spark-redshift.jar`, `spark-avro.jar`, and `RedshiftJDBC.jar`.
- The 6.10.0 release improves the on-cluster log management
  daemon to monitor additional log folders in your
  EMR cluster. This improvement minimizes disk
  over-utilization scenarios.
- The 6.10.0 release automatically restarts the on-cluster log
  management daemon when it stops. This improvement
  reduces the risk for nodes to appear unhealthy due
  to disk over-utilization.
- Amazon EMR 6.10.0 supports regional endpoints for EMRFS
  user mapping.
- The default root volume size has increased to 15 GB in Amazon EMR 6.10.0 and higher. Earlier releases have default root volume size of 10 GB.
- The 6.10.0 release fixes an issue that caused Spark jobs to
  stall when all remaining Spark executors are on a
  decommissioning host with the YARN resource manager.
- With Amazon EMR 6.6.0 through 6.9.x, INSERT queries with dynamic partition and an ORDER BY or SORT BY clause will always have two reducers. This issue is caused by OSS change [HIVE-20703](https://issues.apache.org/jira/browse/HIVE-20703 "https://issues.apache.org/jira/browse/HIVE-20703"), which puts dynamic sort partition optimization under cost-based decision. If your workload doesn't require sorting of dynamic partitions, we recommend that you set the `hive.optimize.sort.dynamic.partition.threshold` property to `-1` to disable the new feature and get the correctly calculated number of reducers. This issue is fixed in OSS Hive as part of [HIVE-22269](https://issues.apache.org/jira/browse/HIVE-22269 "https://issues.apache.org/jira/browse/HIVE-22269") and is fixed in Amazon EMR 6.10.0.
- When you launch a cluster with _the latest patch release_ of Amazon EMR 5.36 or higher, 6.6 or higher, or 7.0 or higher, Amazon EMR uses the latest Amazon Linux 2023 or Amazon Linux 2 release for the
  default Amazon EMR AMI. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](../ManagementGuide/emr-default-ami.md "../ManagementGuide/emr-default-ami.md").

###### Note

This release no longer gets automatic AMI updates since it has been succeeded by 1 more more patch releases. The patch release is denoted by the number after the
second decimal point (`6.8.`1``). To see if you're using the latest patch release, check the available releases in the [*Release Guide*](../ReleaseGuide.md "../ReleaseGuide.md"), or check the **Amazon EMR release** dropdown when you create a cluster in the console, or use the [`ListReleaseLabels`](../APIReference/API_ListReleaseLabels.md "../APIReference/API_ListReleaseLabels.md") API or [`list-release-labels`](../../../cli/latest/reference/emr/list-release-labels.md "../../../cli/latest/reference/emr/list-release-labels.md") CLI action. To get updates about new releases, subscribe to the RSS feed on the [What's new?](emr-whatsnew.md "emr-whatsnew.md") page.

| OsReleaseLabel (Amazon Linux version) | Amazon Linux kernel version | Available date    | Supported Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------- | --------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0.20250721.2                        | 4.14.355-280.652.amzn2      | August 14, 2025   | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                           |
| 2.0.20250623.0                        | 4.14.355-277.647.amzn2      | July 21, 2025     | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                           |
| 2.0.20250610.0                        | 4.14.355-277.647.amzn2      | July 14, 2025     | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Europe (Spain), China (Ningxia), Europe (Zurich)                                                                                            |
| 2.0.20250527.1                        | 4.14.355-277.647.amzn2      | Jun 19, 2025      | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Melbourne), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich)                                           |
| 2.0.20250512.0                        | 4.14.355-277.643.amzn2      | Jun 04, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Stockholm), Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250428.0                        | 4.14.355-276.639.amzn2      | May 23, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Canada West (Calgary), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia), Israel (Tel Aviv)                                           |
| 2.0.20250414.0                        | 4.14.355-276.618.amzn2      | May 12, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250321.0                        | 4.14.355                    | April 09, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250305.0                        | 4.14.355                    | March 18, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250220.0                        | 4.14.355                    | March 08, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250201.0                        | 4.14.355                    | February 28, 2025 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250123.4                        | 4.14.355                    | January 27, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250116.0                        | 4.14.355                    | January 23, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20241217.0                        | 4.14.355                    | January 8, 2025   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Middle East (UAE), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Zurich)                                                                                     |
| 2.0.20241001.0                        | 4.14.352                    | October 4, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240816.0                        | 4.14.350                    | August 21, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240809.0                        | 4.14.349                    | August 20, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240719.0                        | 4.14.348                    | July 25, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240709.1                        | 4.14.348                    | July 23, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Europe (Stockholm), Europe (Milan),<br>Europe (Frankfurt),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Jakarta),<br>Africa (Cape Town), South America (São Paulo), Middle East (Bahrain),<br>Canada (Central),<br>AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia),<br>Asia Pacific (Hyderabad), Middle East (UAE), Europe (Spain), Europe (Zurich),<br>Asia Pacific (Melbourne), Israel (Tel Aviv),<br>Canada West (Calgary) |
| 2.0.20230808.0                        | 4.14.320                    | August 24, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), Israel (Tel Aviv)                                                                                                                                                                                                                                  |
| 2.0.20230727.0                        | 4.14.320                    | August 14, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |
| 2.0.20230719.0                        | 4.14.320                    | August 2, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |
| 2.0.20230628.0                        | 4.14.318                    | July 12, 2023     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Zurich), Europe (Milan),<br>Europe (Spain), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain), Middle East (UAE)                                                                                                                                                                         |
| 2.0.20230612.0                        | 4.14.314                    | June 23, 2023     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Zurich), Europe (Milan),<br>Europe (Spain), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain), Middle East (UAE)                                                                                                                                                                         |
| 2.0.20230504.1                        | 4.14.313                    | May 16, 2023      | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Zurich), Europe (Milan),<br>Europe (Spain), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain), Middle East (UAE)                                                                                                                                                                         |
| 2.0.20230418.0                        | 4.14.311                    | May 3, 2023       | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Zurich), Europe (Milan),<br>Europe (Spain), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain), Middle East (UAE)                                                                                                                                                                         |
| 2.0.20230404.1                        | 4.14.311                    | April 18, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain), Middle East (UAE)                                                                                                                                                                                                                                       |
| 2.0.20230404.0                        | 4.14.311                    | April 10, 2023    | US East (N. Virginia), Europe (Paris)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 2.0.20230320.0                        | 4.14.309                    | March 30, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain), Middle East (UAE)                                                                                                                                                                                                                                       |
| 2.0.20230207.0                        | 4.14.304                    | February 22, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain), Middle East (UAE)                                                                                                                                                                                                                                       |

## Release 6.9.0

The following release notes include information for Amazon EMR release 6.9.0. Changes are relative to Amazon EMR release 6.8.0. For information on the release timeline, see the [change log](emr-690-release.md#690-changelog "emr-690-release.md#690-changelog").

###### New Features

- Amazon EMR release 6.9.0 supports Apache Spark RAPIDS 22.08.0, Apache Hudi 0.12.1, Apache Iceberg 0.14.1, Trino 398, and Tez 0.10.2.
- Amazon EMR release 6.9.0 includes a new open-source application, [Delta Lake](emr-delta.md "emr-delta.md") 2.1.0.
- The Amazon Redshift integration for Apache Spark is included in Amazon EMR releases 6.9.0 and later. Previously an open-source tool, the native integration is a Spark connector that you can use to build Apache Spark applications that read from and write to data in Amazon Redshift and Amazon Redshift Serverless. For more information, see [Using Amazon Redshift integration for Apache Spark with Amazon EMR](emr-spark-redshift.md "emr-spark-redshift.md") .
- Amazon EMR release 6.9.0 adds support for archiving logs to Amazon S3 during cluster scale-down. Previously, you could only archive log files to Amazon S3 during cluster termination. The new capability ensures that log files generated on the cluster persist on Amazon S3 even after the node is terminated. For more information, see [Configure cluster logging and debugging](../ManagementGuide/emr-plan-debugging.md "../ManagementGuide/emr-plan-debugging.md").
- To support long running queries, Trino now includes a fault-tolerant execution mechanism. Fault-tolerant execution mitigates query failures by retrying failed queries or their component tasks.
- You can use Apache Flink on Amazon EMR for unified `BATCH` and `STREAM` processing of Apache Hive Tables or metadata of any Flink tablesource such as Iceberg, Kinesis or Kafka. You can specify the AWS Glue Data Catalog as the metastore for Flink using the AWS Management Console, AWS CLI, or Amazon EMR API. For more information, see [Configuring Flink in Amazon EMR](flink-configure.md "flink-configure.md").
- You can now specify AWS Identity and Access Management (IAM) runtime roles and AWS Lake Formation-based access control for Apache Spark, Apache Hive, and Presto queries on Amazon EMR on EC2 clusters with Amazon SageMaker AI Studio. For more information, see [Configure runtime roles for Amazon EMR steps](../ManagementGuide/emr-steps-runtime-roles.md "../ManagementGuide/emr-steps-runtime-roles.md").

###### Known Issues

- For Amazon EMR release 6.9.0, Trino does not work on clusters enabled for Apache Ranger. If you need to use Trino with Ranger, contact [Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
- If you use the Amazon Redshift integration for Apache Spark and have a time, timetz, timestamp, or timestamptz with microsecond precision in Parquet format, the connector rounds the time values to the nearest millisecond value. As a workaround, use the text unload format `unload_s3_format` parameter.
- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

- Connections to Amazon EMR clusters from Amazon SageMaker AI Studio may intermittently fail
  with a **403 Forbidden** response code. This error happens when
  setup of the IAM role on the cluster takes longer than 60 seconds. As a
  workaround, you can install an Amazon EMR patch to enable retries and increase
  the timeout to a minimum of 300 seconds. Use the following steps to apply
  the bootstrap action when you launch your cluster.
  1.  Download the bootstrap script and RPM files from
      the following Amazon S3 URIs.

  ```
  s3://emr-data-access-control-us-east-1/customer-bootstrap-actions/gcsc/replace-rpms.sh
  s3://emr-data-access-control-us-east-1/customer-bootstrap-actions/gcsc/emr-secret-agent-1.18.0-SNAPSHOT20221121212949.noarch.rpm
  ```

  2.  Upload the files from the previous step to an Amazon S3 bucket that
      you own. The bucket must be in the same AWS Region where
      you plan to launch the cluster.
  3.  Include the following bootstrap action when you launch your
      EMR cluster. Replace `bootstrap_URI` and
      `RPM_URI` with the corresponding URIs
      from Amazon S3.

  ```
  --bootstrap-actions "Path=`bootstrap_URI`,Args=[`RPM_URI`]"
  ```

- With Amazon EMR releases 5.36.0 and 6.6.0 through 6.9.0, `SecretAgent`
  and `RecordServer` service components may experience log
  data loss due to an incorrect file name pattern configuration in
  Log4j2 properties. The incorrect configuration causes the components
  to generate only one log file per day. When the rotation strategy
  occurs, it overwrites the existing file instead of generating a new
  log file as expected. As a workaround, use a bootstrap action to generate log files each
  hour and append an auto-increment integer in the file name to handle
  the rotation.

For Amazon EMR 6.6.0 through 6.9.0 releases, use the following bootstrap
action when you launch a cluster.

```
‑‑bootstrap‑actions "Path=s3://emr-data-access-control-us-east-1/customer-bootstrap-actions/log-rotation-emr-6x/replace-puppet.sh,Args=[]"
```

For Amazon EMR 5.36.0, use the following bootstrap action when you
launch a cluster.

```
‑‑bootstrap‑actions "Path=s3://emr-data-access-control-us-east-1/customer-bootstrap-actions/log-rotation-emr-5x/replace-puppet.sh,Args=[]"
```

- Apache Flink provides Native S3 FileSystem and Hadoop FileSystem Connectors, which let applications create a FileSink and write the data into Amazon S3. This FileSink fails with one of the following two exceptions.

```
java.lang.UnsupportedOperationException: Recoverable writers on Hadoop are only supported for HDFS
```

```
Caused by: java.lang.NoSuchMethodError: org.apache.hadoop.io.retry.RetryPolicies.retryOtherThanRemoteAndSaslException(Lorg/apache/hadoop/io/retry/RetryPolicy;Ljava/util/Map;)Lorg/apache/hadoop/io/retry/RetryPolicy;
                                        at org.apache.hadoop.yarn.client.RMProxy.createRetryPolicy(RMProxy.java:302) ~[hadoop-yarn-common-3.3.3-amzn-0.jar:?]
```

As a workaround, you can install an Amazon EMR patch, which fixes the above issue in Flink. To apply the bootstrap action when you launch your cluster, complete the following steps.

    1. Download the flink-rpm to your Amazon S3 bucket. Your RPM path is
     `s3://`DOC-EXAMPLE-BUCKET`/rpms/flink/`.
    2. Download the bootstrap script and RPM files from Amazon S3 using the following
     URI. Replace ``regionName`` with the AWS Region where
     you plan to launch the cluster.



    ```
    s3://emr-data-access-control-`regionName`/customer-bootstrap-actions/gcsc/replace-rpms.sh
    ```
    3. Hadoop 3.3.3 introduced a change in YARN ([YARN-9608](https://issues.apache.org/jira/browse/YARN-9608 "https://issues.apache.org/jira/browse/YARN-9608"))
    that keeps nodes where containers ran in a
    decommissioning state until the application
    completes. This change ensures that local data such
    as shuffle data doesn't get lost, and you don' need to re-run the job.
    In Amazon EMR 6.8.0 and 6.9.0, this approach might also lead to
    underutilization of resources on clusters with or
    without managed scaling enabled.


    With [Amazon EMR 6.10.0](emr-6100-release.md#emr-6100-relnotes "emr-6100-release.md#emr-6100-relnotes"),
    there's a workaround for this issue to set the value of
    `yarn.resourcemanager.decommissioning-nodes-watcher.wait-for-applications`
    to `false` in `yarn-site.xml`.
    In Amazon EMR releases 6.11.0 and higher as well as 6.8.1, 6.9.1,
    and 6.10.1, the config is set to `false` by default to resolve this issue.

###### Changes, Enhancements, and Resolved Issues

- For Amazon EMR release 6.9.0 and later, all components installed by Amazon EMR that use Log4j libraries use Log4j version 2.17.1 or later.
- When you use the DynamoDB connector with Spark on Amazon EMR versions 6.6.0, 6.7.0, and 6.8.0, all reads from your table
  return an empty result, even though the input split references non-empty data. Amazon EMR release 6.9.0 fixes this issue.
- Amazon EMR 6.9.0 adds limited support for Lake Formation-based access control with Apache Hudi
  when reading data using Spark SQL. The support is for SELECT queries using Spark SQL and
  is limited to column-level access control. For more information, see [Hudi and Lake Formation](../ManagementGuide/hudi-with-lake-formation.md "../ManagementGuide/hudi-with-lake-formation.md").
- When you use Amazon EMR 6.9.0 to create a Hadoop cluster with [Node Labels](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/NodeLabel.html "https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/NodeLabel.html") enabled, the [YARN metrics API](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/ResourceManagerRest.html#Cluster_Metrics_API "https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/ResourceManagerRest.html#Cluster_Metrics_API") returns aggregated information across all partitions, instead of the default partition. For more information, see [YARN-11414](https://issues.apache.org/jira/browse/YARN-11414 "https://issues.apache.org/jira/browse/YARN-11414").
- With Amazon EMR release 6.9.0, we've updated Trino to version 398, which uses Java 17. The previous supported version of Trino for Amazon EMR 6.8.0 was Trino 388 running on Java 11. For more information about this change, see [Trino updates to Java 17](https://trino.io/blog/2022/07/14/trino-updates-to-java-17.html "https://trino.io/blog/2022/07/14/trino-updates-to-java-17.html") on the Trino blog.
- This releases fixes a timing sequence mismatch issue between Apache BigTop and the Amazon EMR on EC2 cluster startup sequence. This timing sequence mismatch occurs when a system attempts to perform two or more operations at the same time instead of doing them in the proper sequence. As a result, certain cluster configurations experienced instance startup timeouts and slower cluster startup times.
- When you launch a cluster with _the latest patch release_ of Amazon EMR 5.36 or higher, 6.6 or higher, or 7.0 or higher, Amazon EMR uses the latest Amazon Linux 2023 or Amazon Linux 2 release for the
  default Amazon EMR AMI. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](../ManagementGuide/emr-default-ami.md "../ManagementGuide/emr-default-ami.md").

###### Note

This release no longer gets automatic AMI updates since it has been succeeded by 1 more more patch releases. The patch release is denoted by the number after the
second decimal point (`6.8.`1``). To see if you're using the latest patch release, check the available releases in the [*Release Guide*](../ReleaseGuide.md "../ReleaseGuide.md"), or check the **Amazon EMR release** dropdown when you create a cluster in the console, or use the [`ListReleaseLabels`](../APIReference/API_ListReleaseLabels.md "../APIReference/API_ListReleaseLabels.md") API or [`list-release-labels`](../../../cli/latest/reference/emr/list-release-labels.md "../../../cli/latest/reference/emr/list-release-labels.md") CLI action. To get updates about new releases, subscribe to the RSS feed on the [What's new?](emr-whatsnew.md "emr-whatsnew.md") page.

| OsReleaseLabel (Amazon Linux version) | Amazon Linux kernel version | Available date    | Supported Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------- | --------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0.20250721.2                        | 4.14.355-280.652.amzn2      | August 14, 2025   | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                           |
| 2.0.20250623.0                        | 4.14.355-277.647.amzn2      | July 21, 2025     | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Canada (Central), Canada West (Calgary), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                           |
| 2.0.20250610.0                        | 4.14.355-277.647.amzn2      | July 14, 2025     | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Europe (Spain), China (Ningxia), Europe (Zurich)                                                                                            |
| 2.0.20250527.1                        | 4.14.355-277.647.amzn2      | Jun 19, 2025      | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Melbourne), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich)                                           |
| 2.0.20250512.0                        | 4.14.355-277.643.amzn2      | Jun 04, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Stockholm), Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250428.0                        | 4.14.355-276.639.amzn2      | May 23, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Canada West (Calgary), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia), Israel (Tel Aviv)                                           |
| 2.0.20250414.0                        | 4.14.355-276.618.amzn2      | May 12, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250321.0                        | 4.14.355                    | April 09, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250305.0                        | 4.14.355                    | March 18, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250220.0                        | 4.14.355                    | March 08, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250201.0                        | 4.14.355                    | February 28, 2025 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250123.4                        | 4.14.355                    | January 27, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20250116.0                        | 4.14.355                    | January 23, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20241217.0                        | 4.14.355                    | January 8, 2025   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Middle East (UAE), Asia Pacific (Melbourne), Israel (Tel Aviv), Europe (Zurich)                                                                                                            |
| 2.0.20241001.0                        | 4.14.352                    | October 4, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240816.0                        | 4.14.350                    | August 21, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240809.0                        | 4.14.349                    | August 20, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240719.0                        | 4.14.348                    | July 25, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                                             |
| 2.0.20240709.1                        | 4.14.348                    | July 23, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Europe (Stockholm), Europe (Milan),<br>Europe (Frankfurt),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Jakarta),<br>Africa (Cape Town), South America (São Paulo), Middle East (Bahrain),<br>Canada (Central),<br>AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia),<br>Asia Pacific (Hyderabad), Middle East (UAE), Europe (Spain), Europe (Zurich),<br>Asia Pacific (Melbourne), Israel (Tel Aviv),<br>Canada West (Calgary) |
| 2.0.20230808.0                        | 4.14.320                    | August 24, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), Israel (Tel Aviv)                                                                                                                                                                                                                                  |
| 2.0.20230727.0                        | 4.14.320                    | August 14, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |
| 2.0.20230719.0                        | 4.14.320                    | August 2, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), Israel (Tel Aviv)                                                                                                                                                    |
| 2.0.20230628.0                        | 4.14.318                    | July 12, 2023     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan),<br>Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain)                                                                                                                                                                                                                                                       |
| 2.0.20230612.0                        | 4.14.314                    | June 23, 2023     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan),<br>Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain)                                                                                                                                                                                                                                                       |
| 2.0.20230504.1                        | 4.14.313                    | May 16, 2023      | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                          |
| 2.0.20230418.0                        | 4.14.311                    | May 3, 2023       | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                 |
| 2.0.20230404.1                        | 4.14.311                    | April 18, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                                               |
| 2.0.20230404.0                        | 4.14.311                    | April 10, 2023    | US East (N. Virginia),<br>Europe (Paris)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 2.0.20230320.0                        | 4.14.309                    | March 30, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                                               |
| 2.0.20230307.0                        | 4.14.305                    | March 15, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                                               |
| 2.0.20230207.0                        | 4.14.304                    | February 22, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                                               |
| 2.0.20221210.1                        | 4.14.301                    | January 12, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                                               |
| 2.0.20221103.3                        | 4.14.296                    | December 5, 2022  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                                               |

## Release 6.8.0

The following release notes include information for Amazon EMR release 6.8.0. Changes are relative to 6.7.0.

###### New Features

- Amazon EMR steps feature now supports Apache Livy endpoint and JDBC/ODBC clients. For more information, see [Configure runtime roles for Amazon EMR steps](../ManagementGuide/emr-steps-runtime-roles.md "../ManagementGuide/emr-steps-runtime-roles.md").
- Amazon EMR release 6.8.0 comes with Apache HBase release 2.4.12. With this HBase release, you can both archive and delete your HBase tables. The Amazon S3 archive process renames all table files to the archive directory. This can be a costly and lengthy process. Now, you can skip the archive process and quickly drop and delete large tables. For more information, see [Using the HBase shell](emr-hbase-connect.md "emr-hbase-connect.md").

###### Known Issues

- Hadoop 3.3.3 introduced a change in YARN ([YARN-9608](https://issues.apache.org/jira/browse/YARN-9608 "https://issues.apache.org/jira/browse/YARN-9608"))
  that keeps nodes where containers ran in a
  decommissioning state until the application
  completes. This change ensures that local data such
  as shuffle data doesn't get lost, and you don' need to re-run the job.
  In Amazon EMR 6.8.0 and 6.9.0, this approach might also lead to
  underutilization of resources on clusters with or
  without managed scaling enabled.

With [Amazon EMR 6.10.0](emr-6100-release.md#emr-6100-relnotes "emr-6100-release.md#emr-6100-relnotes"),
there's a workaround for this issue to set the value of
`yarn.resourcemanager.decommissioning-nodes-watcher.wait-for-applications`
to `false` in `yarn-site.xml`.
In Amazon EMR releases 6.11.0 and higher as well as 6.8.1, 6.9.1,
and 6.10.1, the config is set to `false` by default to resolve this issue.

###### Changes, Enhancements, and Resolved Issues

- When Amazon EMR release 6.5.0, 6.6.0, or 6.7.0 read Apache Phoenix tables through the Apache Spark shell, Amazon EMR produced a `NoSuchMethodError`. Amazon EMR release 6.8.0 fixes this issue.
- Amazon EMR release 6.8.0 comes with [Apache Hudi](https://hudi.apache.org/ "https://hudi.apache.org/") 0.11.1; however, Amazon EMR 6.8.0 clusters are also compatible with the open-source `hudi-spark3.3-bundle_2.12` from Hudi 0.12.0.
- Amazon EMR release 6.8.0 comes with Apache Spark 3.3.0. This Spark release uses Apache Log4j 2 and the `log4j2.properties` file to configure Log4j in Spark processes. If you use Spark in the cluster or create EMR clusters with custom configuration parameters, and you want to upgrade to Amazon EMR release 6.8.0, you must migrate to the new `spark-log4j2` configuration classification and key format for Apache Log4j 2. For more information, see [Migrating from Apache Log4j 1.x to Log4j
  2.x](emr-spark-configure.md#spark-migrate-logj42 "emr-spark-configure.md#spark-migrate-logj42").
- When you launch a cluster with _the latest patch release_ of Amazon EMR 5.36 or higher, 6.6 or higher, or 7.0 or higher, Amazon EMR uses the latest Amazon Linux 2023 or Amazon Linux 2 release for the
  default Amazon EMR AMI. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](../ManagementGuide/emr-default-ami.md "../ManagementGuide/emr-default-ami.md").

###### Note

This release no longer gets automatic AMI updates since it has been succeeded by 1 more more patch releases. The patch release is denoted by the number after the
second decimal point (`6.8.`1``). To see if you're using the latest patch release, check the available releases in the [*Release Guide*](../ReleaseGuide.md "../ReleaseGuide.md"), or check the **Amazon EMR release** dropdown when you create a cluster in the console, or use the [`ListReleaseLabels`](../APIReference/API_ListReleaseLabels.md "../APIReference/API_ListReleaseLabels.md") API or [`list-release-labels`](../../../cli/latest/reference/emr/list-release-labels.md "../../../cli/latest/reference/emr/list-release-labels.md") CLI action. To get updates about new releases, subscribe to the RSS feed on the [What's new?](emr-whatsnew.md "emr-whatsnew.md") page.

| OsReleaseLabel (Amazon Linux Version) | Amazon Linux Kernel Version | Available Date    | Supported Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------- | --------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0.20250721.2                        | 4.14.355-280.652.amzn2      | August 14, 2025   | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Canada (Central), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                        |
| 2.0.20250623.0                        | 4.14.355-277.647.amzn2      | July 21, 2025     | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Canada (Central), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                        |
| 2.0.20250610.0                        | 4.14.355-277.647.amzn2      | July 14, 2025     | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Europe (Spain), China (Ningxia), Europe (Zurich)                                                                  |
| 2.0.20250527.1                        | 4.14.355-277.647.amzn2      | Jun 19, 2025      | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Melbourne), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Europe (Spain), China (Ningxia), Europe (Zurich)                                        |
| 2.0.20250512.0                        | 4.14.355-277.643.amzn2      | Jun 04, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Stockholm), Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia)                                                                                                                                                                   |
| 2.0.20250428.0                        | 4.14.355-276.639.amzn2      | May 23, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia), Israel (Tel Aviv)                                        |
| 2.0.20250414.0                        | 4.14.355-276.618.amzn2      | May 12, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                   |
| 2.0.20250321.0                        | 4.14.355                    | April 09, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                   |
| 2.0.20250305.0                        | 4.14.355                    | March 18, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                   |
| 2.0.20250220.0                        | 4.14.355                    | March 08, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                   |
| 2.0.20250201.0                        | 4.14.355                    | February 28, 2025 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                   |
| 2.0.20250123.4                        | 4.14.355                    | January 27, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                   |
| 2.0.20250116.0                        | 4.14.355                    | January 23, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                   |
| 2.0.20241217.0                        | 4.14.355                    | January 8, 2025   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Middle East (UAE), Asia Pacific (Melbourne), Israel (Tel Aviv), Europe (Zurich)                                                                                  |
| 2.0.20241001.0                        | 4.14.352                    | October 4, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                   |
| 2.0.20240816.0                        | 4.14.350                    | August 21, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                   |
| 2.0.20240809.0                        | 4.14.349                    | August 20, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                   |
| 2.0.20240719.0                        | 4.14.348                    | July 25, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                                                                   |
| 2.0.20240709.1                        | 4.14.348                    | July 23, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Europe (Stockholm), Europe (Milan),<br>Europe (Frankfurt),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Jakarta),<br>Africa (Cape Town), South America (São Paulo), Middle East (Bahrain),<br>Canada (Central),<br>AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia),<br>Asia Pacific (Hyderabad), Middle East (UAE), Europe (Spain), Europe (Zurich),<br>Asia Pacific (Melbourne), Israel (Tel Aviv) |
| 2.0.20230808.0                        | 4.14.320                    | August 24, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central)                                                                                                                                                                                                                                                                                                                                      |
| 2.0.20230727.0                        | 4.14.320                    | August 14, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central),                                                                                                                                                                                                                          |
| 2.0.20230719.0                        | 4.14.320                    | August 2, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central)                                                                                                                                             |
| 2.0.20230628.0                        | 4.14.318                    | July 12, 2023     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan),<br>Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain)                                                                                                                                                                                                                             |
| 2.0.20230612.0                        | 4.14.314                    | June 23, 2023     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan),<br>Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain)                                                                                                                                                                                                                             |
| 2.0.20230504.1                        | 4.14.313                    | May 16, 2023      | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                |
| 2.0.20230418.0                        | 4.14.311                    | May 3, 2023       | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                       |
| 2.0.20230404.1                        | 4.14.311                    | April 18, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                     |
| 2.0.20230404.0                        | 4.14.311                    | April 10, 2023    | US East (N. Virginia), Europe (Paris)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 2.0.20230320.0                        | 4.14.309                    | March 30, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                     |
| 2.0.20230307.0                        | 4.14.305                    | March 15, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                     |
| 2.0.20230207.0                        | 4.14.304                    | February 22, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                     |
| 2.0.20230119.1                        | 4.14.301                    | February 3, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                     |
| 2.0.20221210.1                        | 4.14.301                    | December 22, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                     |
| 2.0.20221103.3                        | 4.14.296                    | December 5, 2022  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                     |
| 2.0.20221004.0                        | 4.14.294                    | November 2, 2022  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                     |
| 2.0.20220912.1                        | 4.14.291                    | September 6, 2022 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                                                                     |

###### Known Issues

- When you use the DynamoDB connector with Spark on Amazon EMR versions 6.6.0, 6.7.0, and 6.8.0, all reads from your table
  return an empty result, even though the input split references non-empty data. This is because Spark 3.2.0 sets
  `spark.hadoopRDD.ignoreEmptySplits` to `true` by default. As a workaround, explicitly set
  `spark.hadoopRDD.ignoreEmptySplits` to `false`. Amazon EMR release 6.9.0 fixes this issue.
- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

- With Amazon EMR releases 5.36.0 and 6.6.0 through 6.9.0, `SecretAgent`
  and `RecordServer` service components may experience log
  data loss due to an incorrect file name pattern configuration in
  Log4j2 properties. The incorrect configuration causes the components
  to generate only one log file per day. When the rotation strategy
  occurs, it overwrites the existing file instead of generating a new
  log file as expected. As a workaround, use a bootstrap action to generate log files each
  hour and append an auto-increment integer in the file name to handle
  the rotation.

For Amazon EMR 6.6.0 through 6.9.0 releases, use the following bootstrap
action when you launch a cluster.

```
‑‑bootstrap‑actions "Path=s3://emr-data-access-control-us-east-1/customer-bootstrap-actions/log-rotation-emr-6x/replace-puppet.sh,Args=[]"
```

For Amazon EMR 5.36.0, use the following bootstrap action when you
launch a cluster.

```
‑‑bootstrap‑actions "Path=s3://emr-data-access-control-us-east-1/customer-bootstrap-actions/log-rotation-emr-5x/replace-puppet.sh,Args=[]"
```

For more information on the release timeline, see the [change log](emr-680-release.md#680-changelog "emr-680-release.md#680-changelog").

## Release 6.7.0

The following release notes include information for Amazon EMR release 6.7.0. Changes are relative to 6.6.0.

Initial release date: July 15, 2022

###### New Features

- Amazon EMR now supports Apache Spark 3.2.1, Apache Hive 3.1.3, HUDI 0.11, PrestoDB 0.272, and Trino 0.378.
- Supports IAM Role and Lake Formation-based access controls with EMR steps (Spark, Hive) for Amazon EMR on EC2 clusters.
- Supports Apache Spark data definition statements on Apache Ranger enabled clusters. This now includes support for Trino applications reading and writing Apache Hive metadata on Apache Ranger enabled clusters. For more information, see [Enable federated governance using Trino and Apache Ranger on Amazon EMR](https://aws.amazon.com/blogs/big-data/enable-federated-governance-using-trino-and-apache-ranger-on-amazon-emr/ "https://aws.amazon.com/blogs/big-data/enable-federated-governance-using-trino-and-apache-ranger-on-amazon-emr/").
- When you launch a cluster with _the latest patch release_ of Amazon EMR 5.36 or higher, 6.6 or higher, or 7.0 or higher, Amazon EMR uses the latest Amazon Linux 2023 or Amazon Linux 2 release for the
  default Amazon EMR AMI. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](../ManagementGuide/emr-default-ami.md "../ManagementGuide/emr-default-ami.md").

| OsReleaseLabel (Amazon Linux Version) | Amazon Linux Kernel Version | Available Date    | Supported Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------- | --------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0.20250721.2                        | 4.14.355-280.652.amzn2      | August 14, 2025   | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Canada (Central), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                  |
| 2.0.20250623.0                        | 4.14.355-277.647.amzn2      | July 21, 2025     | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Canada (Central), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                  |
| 2.0.20250610.0                        | 4.14.355-277.647.amzn2      | July 14, 2025     | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Europe (Spain), China (Ningxia), Europe (Zurich)                  |
| 2.0.20250527.1                        | 4.14.355-277.647.amzn2      | Jun 19, 2025      | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Europe (Spain), China (Ningxia), Europe (Zurich)                  |
| 2.0.20250512.0                        | 4.14.355-277.643.amzn2      | Jun 04, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Stockholm), Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20250428.0                        | 4.14.355-276.639.amzn2      | May 23, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia), Israel (Tel Aviv)                  |
| 2.0.20250414.0                        | 4.14.355-276.618.amzn2      | May 12, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20250321.0                        | 4.14.355                    | April 09, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20250305.0                        | 4.14.355                    | March 18, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20250220.0                        | 4.14.355                    | March 08, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20250201.0                        | 4.14.355                    | February 28, 2025 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20250123.4                        | 4.14.355                    | January 27, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20250116.0                        | 4.14.355                    | January 23, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20241217.0                        | 4.14.355                    | January 8, 2025   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia), Middle East (UAE), Israel (Tel Aviv), Europe (Zurich)                                                            |
| 2.0.20241001.0                        | 4.14.352                    | October 4, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20240816.0                        | 4.14.350                    | August 21, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20240809.0                        | 4.14.349                    | August 20, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20240719.0                        | 4.14.348                    | July 25, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20240709.1                        | 4.14.348                    | July 23, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Europe (Stockholm), Europe (Milan),<br>Europe (Frankfurt),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Jakarta),<br>Africa (Cape Town), South America (São Paulo), Middle East (Bahrain),<br>Canada (Central),<br>AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia),<br>Asia Pacific (Hyderabad), Middle East (UAE), Europe (Spain), Europe (Zurich) |
| 2.0.20240223.0                        | 4.14.336                    | March 8, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20240131.0                        | 4.14.336                    | February 14, 2024 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20240124.0                        | 4.14.336                    | February 7, 2024  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20240109.0                        | 4.14.334                    | January 24, 2024  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231218.0                        | 4.14.330                    | January 2, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231206.0                        | 4.14.330                    | December 22, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231116.0                        | 4.14.328                    | December 11, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231101.0                        | 4.14.327                    | November 16, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231020.1                        | 4.14.326                    | November 7, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20231012.1                        | 4.14.326                    | October 26, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20230926.0                        | 4.14.322                    | October 19, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                                   |
| 2.0.20230906.0                        | 4.14.322                    | October 4, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central)                                                                                                                                                                                                     |
| 2.0.20230822.0                        | 4.14.322                    | August 30, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central)                                                                                                                                                                                                     |
| 2.0.20230808.0                        | 4.14.320                    | August 24, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central)                                                                                                                                                                                                     |
| 2.0.20230727.0                        | 4.14.320                    | August 14, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central)                                                                                                                                                                                                     |
| 2.0.20230719.0                        | 4.14.320                    | August 2, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central)                                                                                                                       |
| 2.0.20230628.0                        | 4.14.318                    | July 12, 2023     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan),<br>Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain)                                                                                                                                                                             |
| 2.0.20230612.0                        | 4.14.314                    | June 23, 2023     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan),<br>Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain)                                                                                                                                                                             |
| 2.0.20230504.1                        | 4.14.313                    | May 16, 2023      | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                |
| 2.0.20230418.0                        | 4.14.311                    | May 3, 2023       | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                       |
| 2.0.20230404.1                        | 4.14.311                    | April 18, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                     |
| 2.0.20230404.0                        | 4.14.311                    | April 10, 2023    | US East (N. Virginia), Europe (Paris)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 2.0.20230320.0                        | 4.14.309                    | March 30, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                     |
| 2.0.20230307.0                        | 4.14.305                    | March 15, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                     |
| 2.0.20230207.0                        | 4.14.304                    | February 22, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                     |
| 2.0.20230119.1                        | 4.14.301                    | February 3, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                     |
| 2.0.20221210.1                        | 4.14.301                    | December 22, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                     |
| 2.0.20221103.3                        | 4.14.296                    | December 5, 2022  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                     |
| 2.0.20221004.0                        | 4.14.294                    | November 2, 2022  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                     |
| 2.0.20220912.1                        | 4.14.291                    | October 7, 2022   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                     |
| 2.0.20220719.0                        | 4.14.287                    | August 10, 2022   | `us‑west‑1`, `eu‑west‑3`, `eu‑north‑1`, `ap‑south‑1`, `me‑south‑1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 2.0.20220606.1                        | 4.14.281                    | July 15, 2022     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Europe (Stockholm), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Milan), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Jakarta), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain)                                                                                                                                                                                                     |

###### Known Issues

- When Amazon EMR release 6.5.0, 6.6.0, or 6.7.0 read Apache Phoenix tables through the Apache Spark shell, a `NoSuchMethodError` occurs because Amazon EMR uses an incorrect `Hbase.compat.version`. Amazon EMR release 6.8.0 fixes this issue.
- When you use the DynamoDB connector with Spark on Amazon EMR versions 6.6.0, 6.7.0, and 6.8.0, all reads from your table
  return an empty result, even though the input split references non-empty data. This is because Spark 3.2.0 sets
  `spark.hadoopRDD.ignoreEmptySplits` to `true` by default. As a workaround, explicitly set
  `spark.hadoopRDD.ignoreEmptySplits` to `false`. Amazon EMR release 6.9.0 fixes this issue.
- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

- With Amazon EMR releases 5.36.0 and 6.6.0 through 6.9.0, `SecretAgent`
  and `RecordServer` service components may experience log
  data loss due to an incorrect file name pattern configuration in
  Log4j2 properties. The incorrect configuration causes the components
  to generate only one log file per day. When the rotation strategy
  occurs, it overwrites the existing file instead of generating a new
  log file as expected. As a workaround, use a bootstrap action to generate log files each
  hour and append an auto-increment integer in the file name to handle
  the rotation.

For Amazon EMR 6.6.0 through 6.9.0 releases, use the following bootstrap
action when you launch a cluster.

```
‑‑bootstrap‑actions "Path=s3://emr-data-access-control-us-east-1/customer-bootstrap-actions/log-rotation-emr-6x/replace-puppet.sh,Args=[]"
```

For Amazon EMR 5.36.0, use the following bootstrap action when you
launch a cluster.

```
‑‑bootstrap‑actions "Path=s3://emr-data-access-control-us-east-1/customer-bootstrap-actions/log-rotation-emr-5x/replace-puppet.sh,Args=[]"
```

- The `GetClusterSessionCredentials` API
  isn't supported with clusters that run on Amazon EMR 6.7 or lower.
- The following Hadoop commits were backported.

* [[HADOOP-16080]](https://issues.apache.org/jira/browse/HADOOP-16080 "https://issues.apache.org/jira/browse/HADOOP-16080") Fix issue where `hadoop-aws` not working with `hadoop-client-api`.

* [[HADOOP-18237]](https://issues.apache.org/jira/browse/HADOOP-18237 "https://issues.apache.org/jira/browse/HADOOP-18237") Upgrade Apache Xerces Java to 2.12.2.

* [[YARN-11092]](https://issues.apache.org/jira/browse/YARN-11092 "https://issues.apache.org/jira/browse/YARN-11092") Upgrade jquery to ui to 1.13.1.

* [[YARN-10720]](https://issues.apache.org/jira/browse/YARN-10720 "https://issues.apache.org/jira/browse/YARN-10720") YARN WebAppProxyServlet should support connection timeout to prevent proxy server from hanging.

## Release 6.6.0

The following release notes include information for Amazon EMR release 6.6.0. Changes
are relative to 6.5.0.

Initial release date: May 9, 2022

Updated documentation date: June 15, 2022

###### New Features

- Amazon EMR 6.6 now supports Apache Spark 3.2, Apache Spark RAPIDS 22.02, CUDA 11, Apache Hudi 0.10.1, Apache Iceberg 0.13, Trino 0.367 and PrestoDB 0.267.
- When you launch a cluster with _the latest patch release_ of Amazon EMR 5.36 or higher, 6.6 or higher, or 7.0 or higher, Amazon EMR uses the latest Amazon Linux 2023 or Amazon Linux 2 release for the
  default Amazon EMR AMI. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](../ManagementGuide/emr-default-ami.md "../ManagementGuide/emr-default-ami.md").

| OsReleaseLabel (Amazon Linux Version) | Amazon Linux Kernel Version | Available Date    | Supported Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------- | --------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2.0.20250721.2                        | 4.14.355-280.652.amzn2      | August 14, 2025   | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Canada (Central), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Stockholm), Europe (Milan), Europe (Ireland), Europe (London), Europe (Paris), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                                                                                  |
| 2.0.20250623.0                        | 4.14.355-277.647.amzn2      | July 21, 2025     | Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Canada (Central), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Stockholm), Europe (Milan), Europe (Ireland), Europe (London), Europe (Paris), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), US West (Oregon)                                                                                                  |
| 2.0.20250610.0                        | 4.14.355-277.647.amzn2      | July 14, 2025     | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Israel (Tel Aviv), Canada (Central), Europe (Spain), China (Ningxia), Europe (Zurich) |
| 2.0.20250527.1                        | 4.14.355-277.647.amzn2      | Jun 19, 2025      | Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), Asia Pacific (Jakarta), US East (Ohio), Africa (Cape Town), Europe (Ireland), Europe (Frankfurt), South America (São Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Europe (Milan), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central), China (Ningxia)                                                                                                  |
| 2.0.20250512.0                        | 4.14.355-277.643.amzn2      | Jun 04, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Stockholm), Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20250428.0                        | 4.14.355-276.639.amzn2      | May 23, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Stockholm), Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20250414.0                        | 4.14.355-276.618.amzn2      | May 12, 2025      | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20250321.0                        | 4.14.355                    | April 09, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20250305.0                        | 4.14.355                    | March 18, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20250220.0                        | 4.14.355                    | March 08, 2025    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20250201.0                        | 4.14.355                    | February 28, 2025 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20250123.4                        | 4.14.355                    | January 27, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20250116.0                        | 4.14.355                    | January 23, 2025  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20241217.0                        | 4.14.355                    | January 8, 2025   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20241001.0                        | 4.14.352                    | October 4, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20240816.0                        | 4.14.350                    | August 21, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20240809.0                        | 4.14.349                    | August 20, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20240719.0                        | 4.14.348                    | July 25, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20240709.1                        | 4.14.348                    | July 23, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Europe (Stockholm), Europe (Milan),<br>Europe (Frankfurt),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka),<br>Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Jakarta),<br>Africa (Cape Town), South America (São Paulo), Middle East (Bahrain),<br>Canada (Central),<br>AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                 |
| 2.0.20240223.0                        | 4.14.336                    | March 8, 2024     | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20240131.0                        | 4.14.336                    | February 14, 2024 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20240124.0                        | 4.14.336                    | February 7, 2024  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20240109.0                        | 4.14.334                    | January 24, 2024  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20231218.0                        | 4.14.330                    | January 2, 2024   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20231206.0                        | 4.14.330                    | December 22, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20231116.0                        | 4.14.328                    | December 11, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20231101.0                        | 4.14.327                    | November 16, 2023 | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20231020.1                        | 4.14.326                    | November 7, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20231012.1                        | 4.14.326                    | October 26, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20230926.0                        | 4.14.322                    | October 19, 2023  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), China (Beijing), China (Ningxia)                                                                                                  |
| 2.0.20230906.0                        | 4.14.322                    | October 4, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central)                                                                                                                                                                                    |
| 2.0.20230822.0                        | 4.14.322                    | August 30, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central)                                                                                                                                                                                    |
| 2.0.20230808.0                        | 4.14.320                    | August 24, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central)                                                                                                                                                                                    |
| 2.0.20230727.0                        | 4.14.320                    | August 14, 2023   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Canada (Central)                                                                                                                                                                                    |
| 2.0.20230719.0                        | 4.14.320                    | August 2, 2023    | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Frankfurt), Europe (Zurich), Europe (Ireland), Europe (London), Europe (Paris), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Africa (Cape Town), South America (São Paulo), Middle East (Bahrain), Middle East (UAE), Canada (Central)                                                                                                      |
| 2.0.20230628.0                        | 4.14.318                    | July 12, 2023     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan),<br>Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain)                                                                                                                                                            |
| 2.0.20230612.0                        | 4.14.314                    | June 23, 2023     | US East (N. Virginia), US East (Ohio), US West (N. California),<br>US West (Oregon), Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Frankfurt), Europe (Milan),<br>Asia Pacific (Hong Kong), Asia Pacific (Mumbai),<br>Asia Pacific (Jakarta), Asia Pacific (Tokyo),<br>Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town), South America (São Paulo),<br>Middle East (Bahrain)                                                                                                                                                            |
| 2.0.20230504.1                        | 4.14.313                    | May 16, 2023      | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20230418.0                        | 4.14.311                    | May 3, 2023       | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20230404.1                        | 4.14.311                    | April 18, 2023    | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20230404.0                        | 4.14.311                    | April 10, 2023    | US East (N. Virginia),<br>Europe (Paris)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 2.0.20230320.0                        | 4.14.309                    | March 30, 2023    | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20230307.0                        | 4.14.305                    | March 15, 2023    | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20230207.0                        | 4.14.304                    | February 22, 2023 | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20230119.1                        | 4.14.301                    | February 3, 2023  | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20221210.1                        | 4.14.301                    | December 22, 2023 | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20221103.3                        | 4.14.296                    | December 5, 2022  | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20221004.0                        | 4.14.294                    | November 2, 2022  | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20220912.1                        | 4.14.291                    | October 7, 2022   | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20220805.0                        | 4.14.287                    | August 30, 2022   | `us‑west‑1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 2.0.20220719.0                        | 4.14.287                    | August 10, 2022   | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20220426.0                        | 4.14.281                    | June 10, 2022     | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |
| 2.0.20220406.1                        | 4.14.275                    | May 2, 2022       | US East (N. Virginia), US East (Ohio),<br>US West (N. California), US West (Oregon),<br>Canada (Central), Europe (Stockholm),<br>Europe (Ireland), Europe (London),<br>Europe (Paris), Europe (Frankfurt),<br>Europe (Milan), Asia Pacific (Hong Kong),<br>Asia Pacific (Mumbai), Asia Pacific (Jakarta),<br>Asia Pacific (Tokyo), Asia Pacific (Seoul),<br>Asia Pacific (Osaka), Asia Pacific (Singapore),<br>Asia Pacific (Sydney), Africa (Cape Town),<br>South America (São Paulo), Middle East (Bahrain)                                                                                                                                                      |

- With Amazon EMR 6.6 and later, applications that use Log4j 1.x and Log4j 2.x are upgraded to use Log4j 1.2.17 (or higher) and Log4j 2.17.1 (or higher) respectively, and do not require using the [bootstrap actions](emr-log4j-vulnerability.md "emr-log4j-vulnerability.md") provided to mitigate the CVE issues.
- **[Managed scaling] Spark shuffle data managed scaling optimization** - For Amazon EMR versions 5.34.0 and
  later, and EMR versions 6.4.0 and later, managed scaling is now Spark shuffle data aware
  (data that Spark redistributes across partitions to perform specific operations). For more information
  on shuffle operations, see [Using EMR managed scaling in Amazon EMR](../ManagementGuide/emr-managed-scaling.md "../ManagementGuide/emr-managed-scaling.md") in the _Amazon EMR Management Guide_ and [Spark Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations "https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations").
- Starting with Amazon EMR 5.32.0 and 6.5.0, dynamic executor sizing for Apache Spark is enabled by default. To turn this feature on or off, you can use the `spark.yarn.heterogeneousExecutors.enabled` configuration parameter.

###### Changes, Enhancements, and Resolved Issues

- Amazon EMR reduces cluster startup time by up to 80 seconds on average for clusters that use the EMR default AMI option and only install common applications, such as Apache Hadoop, Apache Spark and Apache Hive.

###### Known Issues

- When Amazon EMR release 6.5.0, 6.6.0, or 6.7.0 read Apache Phoenix tables through the Apache Spark shell, a `NoSuchMethodError` occurs because Amazon EMR uses an incorrect `Hbase.compat.version`. Amazon EMR release 6.8.0 fixes this issue.
- When you use the DynamoDB connector with Spark on Amazon EMR versions 6.6.0, 6.7.0, and 6.8.0, all reads from your table
  return an empty result, even though the input split references non-empty data. This is because Spark 3.2.0 sets
  `spark.hadoopRDD.ignoreEmptySplits` to `true` by default. As a workaround, explicitly set
  `spark.hadoopRDD.ignoreEmptySplits` to `false`. Amazon EMR release 6.9.0 fixes this issue.
- On Trino long-running clusters, Amazon EMR 6.6.0 enables Garbage Collection logging parameters in the Trino jvm.config to get better insights from the Garbage Collection logs. This change appends many Garbage Collection logs to the launcher.log (/var/log/trino/launcher.log) file.
  If you are running Trino clusters in Amazon EMR 6.6.0, you may encounter nodes running out of disk space after the cluster has been running for a couple of days due to the appended logs.

The workaround for this issue is to run the script below as a Bootstrap Action to disable the Garbage Collection logging parameters in jvm.config while creating or cloning the cluster for Amazon EMR 6.6.0.

```
#!/bin/bash
  set -ex
  PRESTO_PUPPET_DIR='/var/aws/emr/bigtop-deploy/puppet/modules/trino'
  sudo bash -c "sed -i '/-Xlog/d' ${PRESTO_PUPPET_DIR}/templates/jvm.config"
```

- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

- With Amazon EMR releases 5.36.0 and 6.6.0 through 6.9.0, `SecretAgent`
  and `RecordServer` service components may experience log
  data loss due to an incorrect file name pattern configuration in
  Log4j2 properties. The incorrect configuration causes the components
  to generate only one log file per day. When the rotation strategy
  occurs, it overwrites the existing file instead of generating a new
  log file as expected. As a workaround, use a bootstrap action to generate log files each
  hour and append an auto-increment integer in the file name to handle
  the rotation.

For Amazon EMR 6.6.0 through 6.9.0 releases, use the following bootstrap
action when you launch a cluster.

```
‑‑bootstrap‑actions "Path=s3://emr-data-access-control-us-east-1/customer-bootstrap-actions/log-rotation-emr-6x/replace-puppet.sh,Args=[]"
```

For Amazon EMR 5.36.0, use the following bootstrap action when you
launch a cluster.

```
‑‑bootstrap‑actions "Path=s3://emr-data-access-control-us-east-1/customer-bootstrap-actions/log-rotation-emr-5x/replace-puppet.sh,Args=[]"
```

## Release 5.35.0

This is the Amazon EMR release 5.35.0 release note.

The following release notes include information for Amazon EMR release 5.35.0. Changes
are relative to 5.34.0.

Initial release date: March 30, 2022

###### New Features

- Amazon EMR release 5.35 applications that use Log4j 1.x and Log4j 2.x are upgraded to use Log4j 1.2.17 (or higher)
  and Log4j 2.17.1 (or higher) respectively, and do not require using bootstrap actions to mitigate the CVE issues in previous releases. See [Approach to mitigate CVE-2021-44228](emr-log4j-vulnerability.md "emr-log4j-vulnerability.md").

**Changes, Enhancements, and Resolved Issues**

| Flink changes | Change type                                                      | Description |
| ------------- | ---------------------------------------------------------------- | ----------- |
| Upgrades      | • Update flink version to 1.14.2.<br>• log4j upgraded to 2.17.1. |

| Hadoop changes                                | Change type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| Hadoop open source backports since EMR 5.34.0 | • [YARN-10438](https://issues.apache.org/jira/browse/YARN-10438 "https://issues.apache.org/jira/browse/YARN-10438"): Handle null containerId in ClientRMService#getContainerReport()<br>• [YARN-7266](https://issues.apache.org/jira/browse/YARN-7266 "https://issues.apache.org/jira/browse/YARN-7266"): Timeline Server event handler threads locked<br>• [YARN-10438](https://issues.apache.org/jira/browse/YARN-9063 "https://issues.apache.org/jira/browse/YARN-9063"): ATS 1.5 fails to start if RollingLevelDb files are corrupt or missing<br>• [HADOOP-13500](https://issues.apache.org/jira/browse/HADOOP-13500 "https://issues.apache.org/jira/browse/HADOOP-13500"): Synchronizing iteration of Configuration properties object<br>• [YARN-10651](https://issues.apache.org/jira/browse/YARN-10651 "https://issues.apache.org/jira/browse/YARN-10651"): CapacityScheduler crashed with NPE in AbstractYarnScheduler.updateNodeResource()<br>• [HDFS-12221](https://issues.apache.org/jira/browse/HDFS-12221 "https://issues.apache.org/jira/browse/HDFS-12221"): Replace xerces in XmlEditsVisitor<br>• [HDFS-16410](https://issues.apache.org/jira/browse/HDFS-16410 "https://issues.apache.org/jira/browse/HDFS-16410"): Insecure Xml parsing in OfflineEditsXmlLoader |
| Hadoop changes and fixes                      | • Tomcat used in KMS and HttpFS is upgraded to 8.5.75<br>• In FileSystemOptimizedCommitterV2, the success marker was written in the commitJob output path defined while creating the committer.<br>Since commitJob and task level output paths can differ, the path has been corrected to use the one defined in manifest files.<br>For Hive jobs, this results in the success marker being written correctly in when performing operations such as dynamic partition or UNION ALL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

| Hive changes                                                                                                                                                                                                | Change type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Hive upgraded to open source [release 2.3.9](https://www.mail-archive.com/user@hive.apache.org/msg22311.html "https://www.mail-archive.com/user@hive.apache.org/msg22311.html"), including these JIRA fixes | • [HIVE-17155](https://issues.apache.org/jira/browse/HIVE-17155 "https://issues.apache.org/jira/browse/HIVE-17155"): findConfFile() in HiveConf.java has some issues with the conf path<br>• [HIVE-24797](https://issues.apache.org/jira/browse/HIVE-24797 "https://issues.apache.org/jira/browse/HIVE-24797"): Disable validate default values when parsing Avro schemas<br>• [HIVE-21563](https://issues.apache.org/jira/browse/HIVE-21563 "https://issues.apache.org/jira/browse/HIVE-21563"): Improve Table#getEmptyTable performance by disable registerAllFunctionsOnce<br>• [HIVE-18147](https://issues.apache.org/jira/browse/HIVE-18147 "https://issues.apache.org/jira/browse/HIVE-18147"): Tests can fail with java.net.BindException: Address already in use<br>• [HIVE-24608](https://issues.apache.org/jira/browse/HIVE-24608 "https://issues.apache.org/jira/browse/HIVE-24608"): Switch back to get_table in HMS client for Hive 2.3.x<br>• [HIVE-21200](https://issues.apache.org/jira/browse/HIVE-21200 "https://issues.apache.org/jira/browse/HIVE-21200"): Vectorization - date column throwing java.lang.UnsupportedOperationException for parquet<br>• [HIVE-19228](https://issues.apache.org/jira/browse/HIVE-19228 "https://issues.apache.org/jira/browse/HIVE-19228"): Remove commons-httpclient 3.x usage |
| Hive open source backports since EMR 5.34.0                                                                                                                                                                 | • [HIVE-19990](https://issues.apache.org/jira/browse/HIVE-19990 "https://issues.apache.org/jira/browse/HIVE-19990"): Query with interval literal in join condition fails<br>• [HIVE-25824](https://issues.apache.org/jira/browse/HIVE-25824 "https://issues.apache.org/jira/browse/HIVE-25824"): Upgrade branch-2.3 to log4j 2.17.0<br>• [TEZ-4062](https://issues.apache.org/jira/browse/TEZ-4062 "https://issues.apache.org/jira/browse/TEZ-4062"): Speculative attempt scheduling should be aborted when Task has completed<br>• [TEZ-4108](https://issues.apache.org/jira/browse/TEZ-4108 "https://issues.apache.org/jira/browse/TEZ-4108"): NullPointerException during speculative execution race condition<br>• [TEZ-3918](https://issues.apache.org/jira/browse/TEZ-3918 "https://issues.apache.org/jira/browse/TEZ-3918"): Setting tez.task.log.level does not work                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Hive upgrades and fixes                                                                                                                                                                                     | • Upgrade Log4j version to 2.17.1<br>• Upgrade ORC version to 1.4.3<br>• FixED deadlock due to penalty thread in ShuffleScheduler                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| New features                                                                                                                                                                                                | • Added feature to print Hive Query in AM logs. This is disabled by default. Flag/Conf: `tez.am.emr.print.hive.query.in.log`. Status (default): FALSE.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

| Oozie changes                                | Change type                                                                                                                                                                                        | Description |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Oozie open source backports since EMR 5.34.0 | • [OOZIE-3652](https://issues.apache.org/jira/browse/OOZIE-3652 "https://issues.apache.org/jira/browse/OOZIE-3652"): Oozie launcher should retry directory listing when NoSuchFileException occurs |

| Pig changes | Change type                 | Description |
| ----------- | --------------------------- | ----------- |
| Upgrades    | • log4j upgraded to 1.2.17. |

###### Known issues

- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

## Release 5.34.0

The following release notes include information for Amazon EMR release 5.34.0. Changes
are relative to 5.33.1.

Initial release date: January 20, 2022

Updated release date: March 21, 2022

###### New Features

- **[Managed scaling] Spark shuffle data managed scaling optimization** - For Amazon EMR versions 5.34.0 and
  later, and EMR versions 6.4.0 and later, managed scaling is now Spark shuffle data aware
  (data that Spark redistributes across partitions to perform specific operations). For more information
  on shuffle operations, see [Using EMR managed scaling in Amazon EMR](../ManagementGuide/emr-managed-scaling.md "../ManagementGuide/emr-managed-scaling.md") in the _Amazon EMR Management Guide_ and [Spark Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations "https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations").
- [Hudi] Improvements to simplify Hudi configuration. Disabled optimistic concurrency control by default.

###### Changes, Enhancements, and Resolved Issues

- This is a release to fix issues with Amazon EMR Scaling when it fails to scale up/scale down a cluster successfully or causes application failures.
- Previously, manual restart of the resource manager on a multi-master cluster caused Amazon EMR on-cluster daemons, like Zookeeper, to reload all previously decommissioned or lost nodes in the Zookeeper znode file. This caused default limits to be exceeded in certain situations. Amazon EMR now removes the decommissioned or lost node records older than one hour from the Zookeeper file and the internal limits have been increased.
- Fixed an issue where scaling requests failed for a large, highly utilized cluster when Amazon EMR on-cluster daemons were running health checking activities, such as gathering YARN node state and HDFS node state. This was happening because on-cluster daemons were not able to communicate the health status data of a node to internal Amazon EMR components.
- Improved EMR on-cluster daemons to correctly track the node states when IP addresses are reused to improve reliability during scaling operations.
- [SPARK-29683](https://issues.apache.org/jira/browse/SPARK-29683 "https://issues.apache.org/jira/browse/SPARK-29683"). Fixed an issue where job failures occurred during cluster scale-down as Spark was assuming all available nodes were deny-listed.
- [YARN-9011](https://issues.apache.org/jira/browse/YARN-9011 "https://issues.apache.org/jira/browse/YARN-9011"). Fixed an issue where job failures occurred due to a race condition in YARN decommissioning when cluster tried to scale up or down.
- Fixed issue with step or job failures during cluster scaling by ensuring that the node states are always consistent between the Amazon EMR on-cluster daemons and YARN/HDFS.
- Fixed an issue where cluster operations such as scale down and step submission failed for Amazon EMR clusters enabled with Kerberos authentication. This was because the Amazon EMR on-cluster daemon did not renew the Kerberos ticket, which is required to securely communicate with HDFS/YARN running on the primary node.
- Zeppelin upgraded to version 0.10.0.
- Livy Fix - upgraded to 0.7.1
- Spark performance improvement - heterogeneous executors are disabled when certain Spark configuration values are overridden in EMR 5.34.0.
- WebHDFS and HttpFS server are disabled by default. You can re-enable WebHDFS using the Hadoop configuration, `dfs.webhdfs.enabled`. HttpFS server can be started by using `sudo systemctl start hadoop-httpfs`.

###### Known Issues

- The Amazon EMR Notebooks feature used with Livy user impersonation does not work because HttpFS is disabled by default. In this case, the EMR notebook cannot connect to the cluster that has Livy impersonation enabled. The workaround is to start HttpFS server before connecting the EMR notebook to the cluster using `sudo systemctl start hadoop-httpfs`.
- Hue queries do not work in Amazon EMR 6.4.0 because Apache Hadoop HttpFS server is disabled by default. To use Hue on Amazon EMR 6.4.0, either manually start HttpFS server on the Amazon EMR primary node using `sudo systemctl start hadoop-httpfs`, or [use an Amazon EMR step](../ManagementGuide/add-step-cli.md "../ManagementGuide/add-step-cli.md").
- The Amazon EMR Notebooks feature used with Livy user impersonation does not work because HttpFS is disabled by default. In this case, the EMR notebook cannot connect to the cluster that has Livy impersonation enabled. The workaround is to start HttpFS server before connecting the EMR notebook to the cluster using `sudo systemctl start hadoop-httpfs`.
- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

## Release 6.5.0

The following release notes include information for Amazon EMR release 6.5.0. Changes
are relative to 6.4.0.

Initial release date: January 20, 2022

Updated release date: March 21, 2022

###### New Features

- **[Managed scaling] Spark shuffle data managed scaling optimization** - For Amazon EMR versions 5.34.0 and
  later, and EMR versions 6.4.0 and later, managed scaling is now Spark shuffle data aware
  (data that Spark redistributes across partitions to perform specific operations). For more information
  on shuffle operations, see [Using EMR managed scaling in Amazon EMR](../ManagementGuide/emr-managed-scaling.md "../ManagementGuide/emr-managed-scaling.md") in the _Amazon EMR Management Guide_ and [Spark Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations "https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations").
- Starting with Amazon EMR 5.32.0 and 6.5.0, dynamic executor sizing for Apache Spark is enabled by default. To turn this feature on or off, you can use the `spark.yarn.heterogeneousExecutors.enabled` configuration parameter.
- Support for Apache Iceberg open table format for huge analytic datasets.
- Support for ranger-trino-plugin 2.0.1-amzn-1
- Support for toree 0.5.0

###### Changes, Enhancements, and Resolved Issues

- Amazon EMR 6.5 release version now supports Apache Iceberg 0.12.0, and provides runtime improvements with Amazon EMR Runtime for Apache Spark, Amazon EMR Runtime for Presto, and Amazon EMR Runtime for Apache Hive.
- [Apache Iceberg](https://iceberg.apache.org/ "https://iceberg.apache.org/") is an open table format for large data sets in Amazon S3 and provides fast query performance over large tables, atomic commits, concurrent writes, and SQL-compatible table evolution. With EMR 6.5, you can use Apache Spark 3.1.2 with the Iceberg table format.
- Apache Hudi 0.9 adds Spark SQL DDL and DML support. This allows you to create, upsert Hudi tables using just SQL statements. Apache Hudi 0.9 also includes query side and writer side performance improvements.
- Amazon EMR Runtime for Apache Hive improves Apache Hive performance on Amazon S3 by removing rename operations during staging operations, and improves performance for metastore check (MSCK) commands used for repairing tables.

###### Known Issues

- When Amazon EMR release 6.5.0, 6.6.0, or 6.7.0 read Apache Phoenix tables through the Apache Spark shell, a `NoSuchMethodError` occurs because Amazon EMR uses an incorrect `Hbase.compat.version`. Amazon EMR release 6.8.0 fixes this issue.
- Hbase bundle clusters in high availability (HA) fail to provision with the default volume size and instance type. The workaround for this issue is to increase the root volume size.
- To use Spark actions with Apache Oozie, you must add the following configuration to your Oozie `workflow.xml` file. Otherwise, several critical libraries such as Hadoop and EMRFS will be missing from the classpath of the Spark executors that Oozie launches.

```
<spark-opts>--conf spark.yarn.populateHadoopClasspath=true</spark-opts>
```

- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

## Release 6.4.0

The following release notes include information for Amazon EMR release 6.4.0. Changes
are relative to 6.3.0.

Initial release date: Sept 20, 2021

Updated release date: March 21, 2022

###### Supported applications

- AWS SDK for Java version 1.12.31
- CloudWatch Sink version 2.2.0
- DynamoDB Connector version 4.16.0
- EMRFS version 2.47.0
- Amazon EMR Goodies version 3.2.0
- Amazon EMR Kinesis Connector version 3.5.0
- Amazon EMR Record Server version 2.1.0
- Amazon EMR Scripts version 2.5.0
- Flink version 1.13.1
- Ganglia version 3.7.2
- AWS Glue Hive Metastore Client version 3.3.0
- Hadoop version 3.2.1-amzn-4
- HBase version 2.4.4-amzn-0
- HBase-operator-tools 1.1.0
- HCatalog version 3.1.2-amzn-5
- Hive version 3.1.2-amzn-5
- Hudi version 0.8.0-amzn-0
- Hue version 4.9.0
- Java JDK version Corretto-8.302.08.1 (build 1.8.0_302-b08)
- JupyterHub version 1.4.1
- Livy version 0.7.1-incubating
- MXNet version 1.8.0
- Oozie version 5.2.1
- Phoenix version 5.1.2
- Pig version 0.17.0
- Presto version 0.254.1-amzn-0
- Trino version 359
- Apache Ranger KMS (multi-master transparent encryption) version 2.0.0
- ranger-plugins 2.0.1-amzn-0
- ranger-s3-plugin 1.2.0
- SageMaker Spark SDK version 1.4.1
- Scala version 2.12.10 (OpenJDK 64-Bit Server VM, Java 1.8.0_282)
- Spark version 3.1.2-amzn-0
- spark-rapids 0.4.1
- Sqoop version 1.4.7
- TensorFlow version 2.4.1
- tez version 0.9.2
- Zeppelin version 0.9.0
- Zookeeper version 3.5.7
- Connectors and drivers: DynamoDB Connector 4.16.0

###### New features

- **[Managed scaling] Spark shuffle data managed scaling optimization** - For Amazon EMR versions 5.34.0 and
  later, and EMR versions 6.4.0 and later, managed scaling is now Spark shuffle data aware
  (data that Spark redistributes across partitions to perform specific operations). For more information
  on shuffle operations, see [Using EMR managed scaling in Amazon EMR](../ManagementGuide/emr-managed-scaling.md "../ManagementGuide/emr-managed-scaling.md") in the _Amazon EMR Management Guide_ and [Spark Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations "https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations").
- On Apache Ranger-enabled Amazon EMR clusters, you can use Apache Spark SQL to insert data into or update the Apache Hive metastore tables using `INSERT INTO`, `INSERT OVERWRITE`, and `ALTER TABLE`.
  When using ALTER TABLE with Spark SQL, a partition location must be the child directory of a table location. Amazon EMR does not currently support inserting data into a partition where the partition location is different from the table location.
- PrestoSQL has been
  [renamed to Trino.](https://trino.io/blog/2020/12/27/announcing-trino.html "https://trino.io/blog/2020/12/27/announcing-trino.html")
- Hive: Execution of simple SELECT queries with LIMIT clause are accelerated by stopping the query execution as soon as the number of records mentioned in LIMIT clause is fetched.
  Simple SELECT queries are queries that do not have GROUP BY / ORDER by clause or queries that do not have a reducer stage. For example,
  `SELECT * from <TABLE> WHERE <Condition> LIMIT <Number>`.

###### Hudi Concurrency Control

- Hudi now supports Optimistic Concurrency Control (OCC), which can be leveraged with write operations like UPSERT and INSERT to allow changes from multiple writers to the same Hudi table. This is file-level OCC, so any two commits (or writers) can write to the same table, if their changes do not conflict.
  For more information, see the
  [Hudi concurrency control](https://hudi.apache.org/docs/concurrency_control/ "https://hudi.apache.org/docs/concurrency_control/").
- Amazon EMR clusters have Zookeeper installed, which can be leveraged as the lock provider for OCC. To make it easier to use this feature, Amazon EMR clusters have the following properties pre-configured:

```
hoodie.write.lock.provider=org.apache.hudi.client.transaction.lock.ZookeeperBasedLockProvider
hoodie.write.lock.zookeeper.url=<`EMR Zookeeper URL`>
hoodie.write.lock.zookeeper.port=<`EMR Zookeeper Port`>
hoodie.write.lock.zookeeper.base_path=/hudi
```

To enable OCC, you need to configure the following properties either with their Hudi job options or at the cluster-level using the Amazon EMR configurations API:

```
hoodie.write.concurrency.mode=optimistic_concurrency_control
hoodie.cleaner.policy.failed.writes=LAZY (Performs cleaning of failed writes lazily instead of inline with every write)
hoodie.write.lock.zookeeper.lock_key=`<Key to uniquely identify the Hudi table>` (Table Name is a good option)
```

###### Hudi Monitoring: Amazon CloudWatch integration to report Hudi Metrics

- Amazon EMR supports publishing Hudi Metrics to Amazon CloudWatch. It is enabled by setting the following required configurations:

```
hoodie.metrics.on=true
hoodie.metrics.reporter.type=CLOUDWATCH
```

- The following are optional Hudi configurations that you can change:

| Setting                                         | Description                                                                 | Value                                                                                                  |
| ----------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| hoodie.metrics.cloudwatch.report.period.seconds | Frequency (in seconds) at which to report metrics to Amazon CloudWatch      | Default value is 60s, which is fine for the default one minute resolution offered by Amazon CloudWatch |
| hoodie.metrics.cloudwatch.metric.prefix         | Prefix to be added to each metric name                                      | Default value is empty (no prefix)                                                                     |
| hoodie.metrics.cloudwatch.namespace             | Amazon CloudWatch namespace under which metrics are published               | Default value is Hudi                                                                                  |
| hoodie.metrics.cloudwatch.maxDatumsPerRequest   | Maximum number of datums to be included in one request to Amazon CloudWatch | Default value is 20, which is same as Amazon CloudWatch default                                        |

###### Amazon EMR Hudi configurations support and improvements

- Customers can now leverage EMR Configurations API and Reconfiguration feature to configure Hudi configurations at cluster level. A new file based configuration support has been introduced via /etc/hudi/conf/hudi-defaults.conf along the lines of other applications like Spark, Hive etc. EMR configures few defaults to improve user experience:

—
`hoodie.datasource.hive_sync.jdbcurl` is configured to the cluster Hive server URL and no longer needs to be specified. This is particularly useful when running a job in Spark cluster mode, where you previously had to specify the Amazon EMR master IP.

— HBase specific configurations, which are useful for using HBase index with Hudi.

— Zookeeper lock provider specific configuration, as discussed under concurrency control, which makes it easier to use Optimistic Concurrency Control (OCC).

- Additional changes have been introduced to reduce the number of configurations that you need to pass, and to infer automatically where possible:

— The
`partitionBy` keyword can be used to specify the partition column.

— When enabling Hive Sync, it is no longer mandatory to pass
`HIVE_TABLE_OPT_KEY, HIVE_PARTITION_FIELDS_OPT_KEY, HIVE_PARTITION_EXTRACTOR_CLASS_OPT_KEY`. Those values can be inferred from the Hudi table name and partition field.

—
`KEYGENERATOR_CLASS_OPT_KEY` is not mandatory to pass, and can be inferred from simpler cases of
`SimpleKeyGenerator` and
`ComplexKeyGenerator`.

###### Hudi Caveats

- Hudi does not support vectorized execution in Hive for Merge on Read (MoR) and Bootstrap tables. For example,
  `count(*)` fails with Hudi realtime table when
  `hive.vectorized.execution.enabled` is set to true.
  As a workaround, you can disable vectorized reading by setting
  `hive.vectorized.execution.enabled` to
  `false`.
- Multi-writer support is not compatible with the Hudi bootstrap feature.
- Flink Streamer and Flink SQL are experimental features in this release. These features are not recommended for use in production deployments.

###### Changes, enhancements, and resolved issues

This is a release to fix issues with Amazon EMR Scaling when it fails to scale up/scale down a cluster successfully or causes application failures.

- Previously, manual restart of the resource manager on a multi-master cluster caused Amazon EMR on-cluster daemons, like Zookeeper, to reload all previously decommissioned or lost nodes in the Zookeeper znode file. This caused default limits to be exceeded in certain situations. Amazon EMR now removes the decommissioned or lost node records older than one hour from the Zookeeper file and the internal limits have been increased.
- Fixed an issue where scaling requests failed for a large, highly utilized cluster when Amazon EMR on-cluster daemons were running health checking activities, such as gathering YARN node state and HDFS node state. This was happening because on-cluster daemons were not able to communicate the health status data of a node to internal Amazon EMR components.
- Improved EMR on-cluster daemons to correctly track the node states when IP addresses are reused to improve reliability during scaling operations.
- [SPARK-29683](https://issues.apache.org/jira/browse/SPARK-29683 "https://issues.apache.org/jira/browse/SPARK-29683"). Fixed an issue where job failures occurred during cluster scale-down as Spark was assuming all available nodes were deny-listed.
- [YARN-9011](https://issues.apache.org/jira/browse/YARN-9011 "https://issues.apache.org/jira/browse/YARN-9011"). Fixed an issue where job failures occurred due to a race condition in YARN decommissioning when cluster tried to scale up or down.
- Fixed issue with step or job failures during cluster scaling by ensuring that the node states are always consistent between the Amazon EMR on-cluster daemons and YARN/HDFS.
- Fixed an issue where cluster operations such as scale down and step submission failed for Amazon EMR clusters enabled with Kerberos authentication. This was because the Amazon EMR on-cluster daemon did not renew the Kerberos ticket, which is required to securely communicate with HDFS/YARN running on the primary node.
- **Configuring a cluster to fix Apache YARN Timeline Server version 1 and 1.5 performance issues**

Apache YARN Timeline Server version 1 and 1.5 can cause performance issues with very active, large EMR clusters, particularly with `yarn.resourcemanager.system-metrics-publisher.enabled=true`, which is the default setting in Amazon EMR.
An open source YARN Timeline Server v2 solves the performance issue related to YARN Timeline Server scalability.

Other workarounds for this issue include:

    + Configuring yarn.resourcemanager.system-metrics-publisher.enabled=false in yarn-site.xml.
    + Enabling the fix for this issue when creating a cluster, as described below.

The following Amazon EMR releases contain a fix for this YARN Timeline Server performance issue.

EMR 5.30.2, 5.31.1, 5.32.1, 5.33.1, 5.34.x, 6.0.1, 6.1.1, 6.2.1, 6.3.1, 6.4.x

To enable the fix on any of the above specified Amazon EMR releases, set these properties to `true` in a configurations JSON file that is passed in using the [`aws emr create-cluster` command parameter](emr-configure-apps-create-cluster.md "emr-configure-apps-create-cluster.md"): `--configurations file://./configurations.json`. Or enable the fix using the [reconfiguration console UI](emr-configure-apps-running-cluster.md "emr-configure-apps-running-cluster.md").

Example of the configurations.json file contents:

```
[
{
"Classification": "yarn-site",
"Properties": {
"yarn.resourcemanager.system-metrics-publisher.timeline-server-v1.enable-batch": "true",
"yarn.resourcemanager.system-metrics-publisher.enabled": "true"
},
"Configurations": []
}
]
```

- WebHDFS and HttpFS server are disabled by default. You can re-enable WebHDFS using the Hadoop configuration, `dfs.webhdfs.enabled`. HttpFS server can be started by using `sudo systemctl start hadoop-httpfs`.
- HTTPS is now enabled by default for Amazon Linux repositories. If you are using an Amazon S3 VPCE policy to restrict access to specific buckets, you must add the new Amazon Linux bucket ARN
  `arn:aws:s3:::amazonlinux-2-repos-$region/*` to your policy (replace
  `$region` with the region where the endpoint is).
  For more information, see this topic in the AWS discussion forums.
  [Announcement: Amazon Linux 2 now supports the ability to use HTTPS while connecting to package repositories](https://forums.aws.amazon.com/ann.jspa?annID=8528 "https://forums.aws.amazon.com/ann.jspa?annID=8528") .
- Hive: Write query performance is improved by enabling the use of a scratch directory on HDFS for the last job. The temporary data for final job is written to HDFS instead of Amazon S3 and performance is improved because the data is moved from HDFS to the final table location (Amazon S3) instead of between Amazon S3 devices.
- Hive: Query compilation time improvement up to 2.5x with Glue metastore Partition Pruning.
- By default, when built-in UDFs are passed by Hive to the Hive Metastore Server, only a subset of those built-in UDFs are passed to the Glue Metastore since Glue supports only limited expression
  operators. If you set
  `hive.glue.partition.pruning.client=true`, then all partition pruning happens on the client side. If the you set
  `hive.glue.partition.pruning.server=true`, then all partition pruning happens on the server side.

###### Known issues

- Hue queries do not work in Amazon EMR 6.4.0 because Apache Hadoop HttpFS server is disabled by default. To use Hue on Amazon EMR 6.4.0, either manually start HttpFS server on the Amazon EMR primary node using `sudo systemctl start hadoop-httpfs`, or [use an Amazon EMR step](../ManagementGuide/add-step-cli.md "../ManagementGuide/add-step-cli.md").
- The Amazon EMR Notebooks feature used with Livy user impersonation does not work because HttpFS is disabled by default. In this case, the EMR notebook cannot connect to the cluster that has Livy impersonation enabled. The workaround is to start HttpFS server before connecting the EMR notebook to the cluster using `sudo systemctl start hadoop-httpfs`.
- In Amazon EMR version 6.4.0, Phoenix does not support the Phoenix connectors component.
- To use Spark actions with Apache Oozie, you must add the following configuration to your Oozie `workflow.xml` file. Otherwise, several critical libraries such as Hadoop and EMRFS will be missing from the classpath of the Spark executors that Oozie launches.

```
<spark-opts>--conf spark.yarn.populateHadoopClasspath=true</spark-opts>
```

- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

## Release 5.32.0

The following release notes include information for Amazon EMR release 5.32.0. Changes
are relative to 5.31.0.

Initial release date: Jan 8, 2021

###### Upgrades

- Upgraded Amazon Glue connector to version 1.14.0
- Upgraded Amazon SageMaker Spark SDK to version 1.4.1
- Upgraded AWS SDK for Java to version 1.11.890
- Upgraded EMR DynamoDB Connector version 4.16.0
- Upgraded EMRFS to version 2.45.0
- Upgraded EMR Log Analytics Metrics to version 1.18.0
- Upgraded EMR MetricsAndEventsApiGateway Client to version 1.5.0
- Upgraded EMR Record Server to version 1.8.0
- Upgraded EMR S3 Dist CP to version 2.17.0
- Upgraded EMR Secret Agent to version 1.7.0
- Upgraded Flink to version 1.11.2
- Upgraded Hadoop to version 2.10.1-amzn-0
- Upgraded Hive to version 2.3.7-amzn-3
- Upgraded Hue to version 4.8.0
- Upgraded Mxnet to version 1.7.0
- Upgraded OpenCV to version 4.4.0
- Upgraded Presto to version 0.240.1-amzn-0
- Upgraded Spark to version 2.4.7-amzn-0
- Upgraded TensorFlow to version 2.3.1

###### Changes, enhancements, and resolved issues

- This is a release to fix issues with Amazon EMR Scaling when it fails to scale up/scale down a cluster successfully or causes application failures.
- Fixed an issue where scaling requests failed for a large, highly utilized cluster when Amazon EMR on-cluster daemons were running health checking activities, such as gathering YARN node state and HDFS node state. This was happening because on-cluster daemons were not able to communicate the health status data of a node to internal Amazon EMR components.
- Improved EMR on-cluster daemons to correctly track the node states when IP addresses are reused to improve reliability during scaling operations.
- [SPARK-29683](https://issues.apache.org/jira/browse/SPARK-29683 "https://issues.apache.org/jira/browse/SPARK-29683"). Fixed an issue where job failures occurred during cluster scale-down as Spark was assuming all available nodes were deny-listed.
- [YARN-9011](https://issues.apache.org/jira/browse/YARN-9011 "https://issues.apache.org/jira/browse/YARN-9011"). Fixed an issue where job failures occurred due to a race condition in YARN decommissioning when cluster tried to scale up or down.
- Fixed issue with step or job failures during cluster scaling by ensuring that the node states are always consistent between the Amazon EMR on-cluster daemons and YARN/HDFS.
- Fixed an issue where cluster operations such as scale down and step submission failed for Amazon EMR clusters enabled with Kerberos authentication. This was because the Amazon EMR on-cluster daemon did not renew the Kerberos ticket, which is required to securely communicate with HDFS/YARN running on the primary node.
- Newer Amazon EMR releases fix the issue with a lower "Max open files" limit on older AL2 in Amazon EMR. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later now include a permanent fix with a higher "Max open files" setting.
- Upgraded component versions.
- For a list of component versions, see [About Amazon EMR Releases](emr-release-components.md "emr-release-components.md") in this guide.

###### New features

- Starting with Amazon EMR 5.32.0 and 6.5.0, dynamic executor sizing for Apache Spark is enabled by default. To turn this feature on or off, you can use the `spark.yarn.heterogeneousExecutors.enabled` configuration parameter.
- Instance Metadata Service (IMDS) V2 support status: Amazon EMR 5.23.1, 5.27.1 and 5.32 or later components use IMDSv2 for all IMDS calls. For IMDS calls in your application code, you can use both IMDSv1 and IMDSv2, or configure the IMDS to use only IMDSv2 for added security. For other 5.x EMR releases, disabling IMDSv1 causes cluster startup failure.
- Beginning with Amazon EMR 5.32.0, you can launch a cluster that natively integrates with Apache Ranger. Apache Ranger is an open-source framework to enable, monitor, and manage comprehensive data security across the Hadoop platform.
  For more information, see [Apache Ranger](https://ranger.apache.org/ "https://ranger.apache.org/"). With native integration, you can bring your own Apache Ranger to enforce fine-grained data access control on Amazon EMR. See [Integrate Amazon EMR with Apache Ranger](../ManagementGuide/emr-ranger.md "../ManagementGuide/emr-ranger.md") in the _Amazon EMR Release Guide_.
- Amazon EMR Release 5.32.0 supports Amazon EMR on EKS. For more details on getting started with EMR on EKS, see [What is Amazon EMR on EKS](../EMR-on-EKS-DevelopmentGuide/emr-eks.md "../EMR-on-EKS-DevelopmentGuide/emr-eks.md").
- Amazon EMR Release 5.32.0 supports Amazon EMR Studio (Preview). For more details on getting started with EMR Studio, see [Amazon EMR Studio (Preview)](../ManagementGuide/emr-studio.md "../ManagementGuide/emr-studio.md").
- Scoped managed policies: To align with AWS best practices, Amazon EMR has introduced v2 EMR-scoped default managed policies as replacements for policies that will be deprecated. See [Amazon EMR Managed Policies](../ManagementGuide/emr-managed-iam-policies.md "../ManagementGuide/emr-managed-iam-policies.md").

###### Known issues

- For Amazon EMR 6.3.0 and 6.2.0 private subnet clusters, you cannot access the Ganglia web UI. You will get an "access denied (403)" error. Other web UIs, such as Spark, Hue, JupyterHub, Zeppelin, Livy, and Tez are working normally. Ganglia web UI access on public subnet clusters are also working normally. To resolve this issue, restart httpd service on the primary node with `sudo systemctl restart httpd`. This issue is fixed in Amazon EMR 6.4.0.
- **Lower "Max open files" limit on older AL2 [fixed in newer releases].** Amazon EMR releases: emr-5.30.x, emr-5.31.0, emr-5.32.0, emr-6.0.0, emr-6.1.0, and emr-6.2.0 are based on older versions ofAmazon Linux 2 (AL2), which have a lower ulimit setting for "Max open files" when Amazon EMR clusters are created with the default AMI. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later include a permanent fix with a higher "Max open files" setting.
  Releases with the lower open file limit causes a "Too many open files" error when submitting Spark job. In the impacted releases, the Amazon EMR default AMI has a default ulimit setting of 4096 for "Max open files," which is lower than the 65536 file limit in the latestAmazon Linux 2 AMI.
  The lower ulimit setting for "Max open files" causes Spark job failure when the Spark driver and executor try to open more than 4096 files. To fix the issue, Amazon EMR has a bootstrap action (BA) script that adjusts the ulimit setting at cluster creation.

If you are using an older Amazon EMR version that doesn't have the permanent fix for this issue, the following workaround lets you to explicitly set the instance-controller ulimit to a maximum of 65536 files.

###### Explicitly set a ulimit from the command line

    1. Edit `/etc/systemd/system/instance-controller.service` to add the following parameters to Service section.


    `LimitNOFILE=65536`


    `LimitNPROC=65536`
    2. Restart InstanceController


    `$ sudo systemctl daemon-reload`


    `$ sudo systemctl restart instance-controller`

**Set a ulimit using bootstrap action (BA)**

You can also use a bootstrap action (BA) script to configure the instance-controller ulimit to 65536 files at cluster creation.

```
#!/bin/bash
for user in hadoop spark hive; do
sudo tee /etc/security/limits.d/$user.conf << EOF
$user - nofile 65536
$user - nproc 65536
EOF
done
for proc in instancecontroller logpusher; do
sudo mkdir -p /etc/systemd/system/$proc.service.d/
sudo tee /etc/systemd/system/$proc.service.d/override.conf << EOF
[Service]
LimitNOFILE=65536
LimitNPROC=65536
EOF
pid=$(pgrep -f aws157.$proc.Main)
sudo prlimit --pid $pid --nofile=65535:65535 --nproc=65535:65535
done
sudo systemctl daemon-reload
```

- ###### Important

EMR clusters that run Amazon Linux or Amazon Linux 2 Amazon Machine Images (AMIs) use default Amazon Linux behavior, and do not
automatically download and install important and critical kernel updates that require a reboot.
This is the same behavior as other Amazon EC2 instances that run the default Amazon Linux AMI. If new Amazon Linux software updates
that require a reboot (such as kernel, NVIDIA, and CUDA updates) become available after
an Amazon EMR release becomes available, EMR cluster instances that run the default AMI do not automatically
download and install those updates. To get kernel updates, you can [customize your Amazon EMR AMI](../ManagementGuide/emr-custom-ami.md "../ManagementGuide/emr-custom-ami.md") to
[use the latest Amazon Linux AMI](../../../AWSEC2/latest/UserGuide/finding-an-ami.md "../../../AWSEC2/latest/UserGuide/finding-an-ami.md").

- Console support to create a security configuration that specifies the AWS Ranger integration option is currently not supported in the GovCloud Region. Security configuration can be done using the CLI. See [Create the EMR Security Configuration](../ManagementGuide/emr-ranger-security-config.md "../ManagementGuide/emr-ranger-security-config.md") in the _Amazon EMR Management Guide_.
- When AtRestEncryption or HDFS encryption is enabled on a cluster that uses Amazon EMR 5.31.0 or 5.32.0, Hive queries result in the following runtime exception.

```
TaskAttempt 3 failed, info=[Error: Error while running task ( failure ) : attempt_1604112648850_0001_1_01_000000_3:java.lang.RuntimeException: java.lang.RuntimeException: Hive Runtime Error while closing operators: java.io.IOException: java.util.ServiceConfigurationError: org.apache.hadoop.security.token.TokenIdentifier: Provider org.apache.hadoop.hbase.security.token.AuthenticationTokenIdentifier not found
```

- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

## Release 6.2.0

The following release notes include information for Amazon EMR release 6.2.0. Changes
are relative to 6.1.0.

Initial release date: Dec 09, 2020

Last updated date: Oct 04, 2021

###### Supported applications

- AWS SDK for Java version 1.11.828
- emr-record-server version 1.7.0
- Flink version 1.11.2
- Ganglia version 3.7.2
- Hadoop version 3.2.1-amzn-1
- HBase version 2.2.6-amzn-0
- HBase-operator-tools 1.0.0
- HCatalog version 3.1.2-amzn-0
- Hive version 3.1.2-amzn-3
- Hudi version 0.6.0-amzn-1
- Hue version 4.8.0
- JupyterHub version 1.1.0
- Livy version 0.7.0
- MXNet version 1.7.0
- Oozie version 5.2.0
- Phoenix version 5.0.0
- Pig version 0.17.0
- Presto version 0.238.3-amzn-1
- PrestoSQL version 343
- Spark version 3.0.1-amzn-0
- spark-rapids 0.2.0
- TensorFlow version 2.3.1
- Zeppelin version 0.9.0-preview1
- Zookeeper version 3.4.14
- Connectors and drivers: DynamoDB Connector 4.16.0

###### New features

- HBase: Removed rename in commit phase and added persistent HFile tracking. See [Persistent HFile Tracking](emr-hbase-s3.md#emr-hbase-s3-hfile-tracking "emr-hbase-s3.md#emr-hbase-s3-hfile-tracking") in the _Amazon EMR Release Guide_.
- HBase: Backported [Create a config that forces to cache blocks on compaction](https://issues.apache.org/jira/browse/HBASE-23066 "https://issues.apache.org/jira/browse/HBASE-23066").
- PrestoDB: Improvements to Dynamic Partition Pruning. Rule-based Join Reorder works on non-partitioned data.
- Scoped managed policies: To align with AWS best practices, Amazon EMR has introduced v2 EMR-scoped default managed policies as replacements for policies that will be deprecated. See [Amazon EMR Managed Policies](../ManagementGuide/emr-managed-iam-policies.md "../ManagementGuide/emr-managed-iam-policies.md").
- Instance Metadata Service (IMDS) V2 support status: For Amazon EMR 6.2 or later, Amazon EMR components use IMDSv2 for all IMDS calls. For IMDS calls in your application code, you can use both IMDSv1 and IMDSv2, or configure the IMDS to use only IMDSv2 for added security. If you disable IMDSv1 in earlier Amazon EMR 6.x releases, it causes cluster startup failure.

###### Changes, enhancements, and resolved issues

- This is a release to fix issues with Amazon EMR Scaling when it fails to scale up/scale down a cluster successfully or causes application failures.
- Fixed an issue where scaling requests failed for a large, highly utilized cluster when Amazon EMR on-cluster daemons were running health checking activities, such as gathering YARN node state and HDFS node state. This was happening because on-cluster daemons were not able to communicate the health status data of a node to internal Amazon EMR components.
- Improved EMR on-cluster daemons to correctly track the node states when IP addresses are reused to improve reliability during scaling operations.
- [SPARK-29683](https://issues.apache.org/jira/browse/SPARK-29683 "https://issues.apache.org/jira/browse/SPARK-29683"). Fixed an issue where job failures occurred during cluster scale-down as Spark was assuming all available nodes were deny-listed.
- [YARN-9011](https://issues.apache.org/jira/browse/YARN-9011 "https://issues.apache.org/jira/browse/YARN-9011"). Fixed an issue where job failures occurred due to a race condition in YARN decommissioning when cluster tried to scale up or down.
- Fixed issue with step or job failures during cluster scaling by ensuring that the node states are always consistent between the Amazon EMR on-cluster daemons and YARN/HDFS.
- Fixed an issue where cluster operations such as scale down and step submission failed for Amazon EMR clusters enabled with Kerberos authentication. This was because the Amazon EMR on-cluster daemon did not renew the Kerberos ticket, which is required to securely communicate with HDFS/YARN running on the primary node.
- Newer Amazon EMR releases fix the issue with a lower "Max open files" limit on older AL2 in Amazon EMR. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later now include a permanent fix with a higher "Max open files" setting.
- Spark: Performance improvements in Spark runtime.

###### Known issues

- Amazon EMR 6.2 has incorrect permissions set on the /etc/cron.d/libinstance-controller-java file in EMR 6.2.0. Permissions on the file are 645 (-rw-r--r-x), when they should be 644 (-rw-r--r--).
  As a result, Amazon EMR version 6.2 does not log instance-state logs, and the /emr/instance-logs directory is empty. This issue is fixed in Amazon EMR 6.3.0 and later.

To work around this issue, run the following script as a bootstrap action at cluster launch.

```
#!/bin/bash
sudo chmod 644 /etc/cron.d/libinstance-controller-java

```

- For Amazon EMR 6.2.0 and 6.3.0 private subnet clusters, you cannot access the Ganglia web UI. You will get an "access denied (403)" error. Other web UIs, such as Spark, Hue, JupyterHub, Zeppelin, Livy, and Tez are working normally. Ganglia web UI access on public subnet clusters are also working normally. To resolve this issue, restart httpd service on the primary node with `sudo systemctl restart httpd`. This issue is fixed in Amazon EMR 6.4.0.
- There is an issue in Amazon EMR 6.2.0 where httpd continuously fails, causing Ganglia to be unavailable. You get a "cannot connect to the server" error. To fix a cluster that is already running with this issue, SSH to the cluster primary node and add the line `Listen 80` to the file `httpd.conf` located at `/etc/httpd/conf/httpd.conf`. This issue is fixed in Amazon EMR 6.3.0.
- HTTPD fails on EMR 6.2.0 clusters when you use a security configuration. This makes the Ganglia web application user interface unavailable. To access the Ganglia web application user interface, add `Listen 80` to the `/etc/httpd/conf/httpd.conf` file on the primary node of your cluster. For information about connecting to your cluster, see [Connect to the Primary Node Using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md").

EMR Notebooks also fail to establish a connection with EMR 6.2.0 clusters when you use a security configuration. The notebook will fail to list kernels and submit Spark jobs. We recommend that you use EMR Notebooks with another version of Amazon EMR instead.

- **Lower "Max open files" limit on older AL2 [fixed in newer releases].** Amazon EMR releases: emr-5.30.x, emr-5.31.0, emr-5.32.0, emr-6.0.0, emr-6.1.0, and emr-6.2.0 are based on older versions ofAmazon Linux 2 (AL2), which have a lower ulimit setting for "Max open files" when Amazon EMR clusters are created with the default AMI. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later include a permanent fix with a higher "Max open files" setting.
  Releases with the lower open file limit causes a "Too many open files" error when submitting Spark job. In the impacted releases, the Amazon EMR default AMI has a default ulimit setting of 4096 for "Max open files," which is lower than the 65536 file limit in the latestAmazon Linux 2 AMI.
  The lower ulimit setting for "Max open files" causes Spark job failure when the Spark driver and executor try to open more than 4096 files. To fix the issue, Amazon EMR has a bootstrap action (BA) script that adjusts the ulimit setting at cluster creation.

If you are using an older Amazon EMR version that doesn't have the permanent fix for this issue, the following workaround lets you to explicitly set the instance-controller ulimit to a maximum of 65536 files.

###### Explicitly set a ulimit from the command line

    1. Edit `/etc/systemd/system/instance-controller.service` to add the following parameters to Service section.


    `LimitNOFILE=65536`


    `LimitNPROC=65536`
    2. Restart InstanceController


    `$ sudo systemctl daemon-reload`


    `$ sudo systemctl restart instance-controller`

**Set a ulimit using bootstrap action (BA)**

You can also use a bootstrap action (BA) script to configure the instance-controller ulimit to 65536 files at cluster creation.

```
#!/bin/bash
for user in hadoop spark hive; do
sudo tee /etc/security/limits.d/$user.conf << EOF
$user - nofile 65536
$user - nproc 65536
EOF
done
for proc in instancecontroller logpusher; do
sudo mkdir -p /etc/systemd/system/$proc.service.d/
sudo tee /etc/systemd/system/$proc.service.d/override.conf << EOF
[Service]
LimitNOFILE=65536
LimitNPROC=65536
EOF
pid=$(pgrep -f aws157.$proc.Main)
sudo prlimit --pid $pid --nofile=65535:65535 --nproc=65535:65535
done
sudo systemctl daemon-reload
```

- ###### Important

Amazon EMR 6.1.0 and 6.2.0 include a performance issue that can critically affect all Hudi insert, upsert, and delete operations. If you plan to use Hudi with Amazon EMR 6.1.0 or 6.2.0, you should contact AWS support to obtain a patched Hudi RPM.

- ###### Important

EMR clusters that run Amazon Linux or Amazon Linux 2 Amazon Machine Images (AMIs) use default Amazon Linux behavior, and do not
automatically download and install important and critical kernel updates that require a reboot.
This is the same behavior as other Amazon EC2 instances that run the default Amazon Linux AMI. If new Amazon Linux software updates
that require a reboot (such as kernel, NVIDIA, and CUDA updates) become available after
an Amazon EMR release becomes available, EMR cluster instances that run the default AMI do not automatically
download and install those updates. To get kernel updates, you can [customize your Amazon EMR AMI](../ManagementGuide/emr-custom-ami.md "../ManagementGuide/emr-custom-ami.md") to
[use the latest Amazon Linux AMI](../../../AWSEC2/latest/UserGuide/finding-an-ami.md "../../../AWSEC2/latest/UserGuide/finding-an-ami.md").

- Amazon EMR 6.2.0 Maven artifacts are not published. They will be published with a future release of Amazon EMR.
- Persistent HFile tracking using the HBase storefile system table does not support the HBase region replication feature. For more information about HBase region replication, see [Timeline-consistent High Available Reads](http://hbase.apache.org/book.html#arch.timelineconsistent.reads "http://hbase.apache.org/book.html#arch.timelineconsistent.reads").
- Amazon EMR 6.x and EMR 5.x Hive bucketing version differences

EMR 5.x uses OOS Apache Hive 2, while in EMR 6.x uses OOS Apache Hive 3. The open source Hive2 uses Bucketing version 1, while open source Hive3 uses Bucketing version 2.
This bucketing version difference between Hive 2 (EMR 5.x) and Hive 3 (EMR 6.x) means Hive bucketing hashing functions differently. See the example below.

The following table is an example created in EMR 6.x and EMR 5.x, respectively.

```
-- Using following LOCATION in EMR 6.x
CREATE TABLE test_bucketing (id INT, desc STRING)
PARTITIONED BY (day STRING)
CLUSTERED BY(id) INTO 128 BUCKETS
LOCATION 's3://your-own-s3-bucket/emr-6-bucketing/';

-- Using following LOCATION in EMR 5.x
LOCATION 's3://your-own-s3-bucket/emr-5-bucketing/';
```

Inserting the same data in both EMR 6.x and EMR 5.x.

```
INSERT INTO test_bucketing PARTITION (day='01') VALUES(66, 'some_data');
INSERT INTO test_bucketing PARTITION (day='01') VALUES(200, 'some_data');
```

Checking the S3 location, shows the bucketing file name is different, because the hashing function is different between EMR 6.x (Hive 3) and EMR 5.x (Hive 2).

```
[hadoop@ip-10-0-0-122 ~]$ aws s3 ls s3://your-own-s3-bucket/emr-6-bucketing/day=01/
2020-10-21 20:35:16         13 000025_0
2020-10-21 20:35:22         14 000121_0
[hadoop@ip-10-0-0-122 ~]$ aws s3 ls s3://your-own-s3-bucket/emr-5-bucketing/day=01/
2020-10-21 20:32:07         13 000066_0
2020-10-21 20:32:51         14 000072_0

```

You can also see the version difference by running the following command in Hive CLI in EMR 6.x. Note that it returns bucketing version 2.

```
hive> DESCRIBE FORMATTED test_bucketing;
...
Table Parameters:
    bucketing_version       2
...
```

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

## Release 5.31.0

The following release notes include information for Amazon EMR release 5.31.0. Changes
are relative to 5.30.1.

Initial release date: Oct 9, 2020

Last updated date: Oct 15, 2020

###### Upgrades

- Upgraded Amazon Glue connector to version 1.13.0
- Upgraded Amazon SageMaker Spark SDK to version 1.4.0
- Upgraded Amazon Kinesis connector to version 3.5.9
- Upgraded AWS SDK for Java to version 1.11.852
- Upgraded Bigtop-tomcat to version 8.5.56
- Upgraded EMR FS to version 2.43.0
- Upgraded EMR MetricsAndEventsApiGateway Client to version 1.4.0
- Upgraded EMR S3 Dist CP to version 2.15.0
- Upgraded EMR S3 Select to version 1.6.0
- Upgraded Flink to version 1.11.0
- Upgraded Hadoop to version 2.10.0
- Upgraded Hive to version 2.3.7
- Upgraded Hudi to version 0.6.0
- Upgraded Hue to version 4.7.1
- Upgraded JupyterHub to version 1.1.0
- Upgraded Mxnet to version 1.6.0
- Upgraded OpenCV to version 4.3.0
- Upgraded Presto to version 0.238.3
- Upgraded TensorFlow to version 2.1.0

###### Changes, enhancements, and resolved issues

- This is a release to fix issues with Amazon EMR Scaling when it fails to scale up/scale down a cluster successfully or causes application failures.
- Fixed an issue where scaling requests failed for a large, highly utilized cluster when Amazon EMR on-cluster daemons were running health checking activities, such as gathering YARN node state and HDFS node state. This was happening because on-cluster daemons were not able to communicate the health status data of a node to internal Amazon EMR components.
- Improved EMR on-cluster daemons to correctly track the node states when IP addresses are reused to improve reliability during scaling operations.
- [SPARK-29683](https://issues.apache.org/jira/browse/SPARK-29683 "https://issues.apache.org/jira/browse/SPARK-29683"). Fixed an issue where job failures occurred during cluster scale-down as Spark was assuming all available nodes were deny-listed.
- [YARN-9011](https://issues.apache.org/jira/browse/YARN-9011 "https://issues.apache.org/jira/browse/YARN-9011"). Fixed an issue where job failures occurred due to a race condition in YARN decommissioning when cluster tried to scale up or down.
- Fixed issue with step or job failures during cluster scaling by ensuring that the node states are always consistent between the Amazon EMR on-cluster daemons and YARN/HDFS.
- Fixed an issue where cluster operations such as scale down and step submission failed for Amazon EMR clusters enabled with Kerberos authentication. This was because the Amazon EMR on-cluster daemon did not renew the Kerberos ticket, which is required to securely communicate with HDFS/YARN running on the primary node.
- Newer Amazon EMR releases fix the issue with a lower "Max open files" limit on older AL2 in Amazon EMR. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later now include a permanent fix with a higher "Max open files" setting.
- [Hive column statistics](https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ColumnStatistics "https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ColumnStatistics") are supported for Amazon EMR versions 5.31.0 and later.
- Upgraded component versions.
- EMRFS S3EC V2 Support in Amazon EMR 5.31.0. In S3 Java SDK releases 1.11.837 and later, encryption client Version 2 (S3EC V2) has been introduced with various security enhancements.
  For more information, see the following:

      + S3 blog post: [Updates to the Amazon S3 encryption client](https://aws.amazon.com/blogs/developer/updates-to-the-amazon-s3-encryption-client/ "https://aws.amazon.com/blogs/developer/updates-to-the-amazon-s3-encryption-client/").
      + AWS SDK for Java Developer Guide: [Migrate encryption and decryption clients to V2](../../../sdk-for-java/v1/developer-guide/s3-encryption-migration.md#s3-cse-update-code "../../../sdk-for-java/v1/developer-guide/s3-encryption-migration.md#s3-cse-update-code").
      + EMR Management Guide: [Amazon S3 client-side encryption](emr-emrfs-encryption-cse.md "emr-emrfs-encryption-cse.md").

  Encryption Client V1 is still available in the SDK for backward compatibility.

###### New features

- **Lower "Max open files" limit on older AL2 [fixed in newer releases].** Amazon EMR releases: emr-5.30.x, emr-5.31.0, emr-5.32.0, emr-6.0.0, emr-6.1.0, and emr-6.2.0 are based on older versions ofAmazon Linux 2 (AL2), which have a lower ulimit setting for "Max open files" when Amazon EMR clusters are created with the default AMI. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later include a permanent fix with a higher "Max open files" setting.
  Releases with the lower open file limit causes a "Too many open files" error when submitting Spark job. In the impacted releases, the Amazon EMR default AMI has a default ulimit setting of 4096 for "Max open files," which is lower than the 65536 file limit in the latestAmazon Linux 2 AMI.
  The lower ulimit setting for "Max open files" causes Spark job failure when the Spark driver and executor try to open more than 4096 files. To fix the issue, Amazon EMR has a bootstrap action (BA) script that adjusts the ulimit setting at cluster creation.

If you are using an older Amazon EMR version that doesn't have the permanent fix for this issue, the following workaround lets you to explicitly set the instance-controller ulimit to a maximum of 65536 files.

###### Explicitly set a ulimit from the command line

    1. Edit `/etc/systemd/system/instance-controller.service` to add the following parameters to Service section.


    `LimitNOFILE=65536`


    `LimitNPROC=65536`
    2. Restart InstanceController


    `$ sudo systemctl daemon-reload`


    `$ sudo systemctl restart instance-controller`

**Set a ulimit using bootstrap action (BA)**

You can also use a bootstrap action (BA) script to configure the instance-controller ulimit to 65536 files at cluster creation.

```
#!/bin/bash
for user in hadoop spark hive; do
sudo tee /etc/security/limits.d/$user.conf << EOF
$user - nofile 65536
$user - nproc 65536
EOF
done
for proc in instancecontroller logpusher; do
sudo mkdir -p /etc/systemd/system/$proc.service.d/
sudo tee /etc/systemd/system/$proc.service.d/override.conf << EOF
[Service]
LimitNOFILE=65536
LimitNPROC=65536
EOF
pid=$(pgrep -f aws157.$proc.Main)
sudo prlimit --pid $pid --nofile=65535:65535 --nproc=65535:65535
done
sudo systemctl daemon-reload
```

- With Amazon EMR 5.31.0, you can launch a cluster that integrates with Lake Formation. This integration provides fine-grained, column-level data filtering to databases and tables in the AWS Glue Data Catalog.
  It also enables federated single sign-on to EMR Notebooks or Apache Zeppelin from an enterprise identity system.
  For more information, see [Integrating Amazon EMR with AWS Lake Formation](../ManagementGuide/emr-lake-formation.md "../ManagementGuide/emr-lake-formation.md") in the _Amazon EMR Management Guide_.

Amazon EMR with Lake Formation is currently available in 16 AWS Regions: US East (Ohio and N. Virginia), US West (N. California and Oregon), Asia Pacific (Mumbai, Seoul, Singapore, Sydney, and Tokyo), Canada (Central), Europe (Frankfurt, Ireland, London, Paris, and Stockholm), South America (São Paulo).

###### Known issues

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

- When AtRestEncryption or HDFS encryption is enabled on a cluster that uses Amazon EMR 5.31.0 or 5.32.0, Hive queries result in the following runtime exception.

```
TaskAttempt 3 failed, info=[Error: Error while running task ( failure ) : attempt_1604112648850_0001_1_01_000000_3:java.lang.RuntimeException: java.lang.RuntimeException: Hive Runtime Error while closing operators: java.io.IOException: java.util.ServiceConfigurationError: org.apache.hadoop.security.token.TokenIdentifier: Provider org.apache.hadoop.hbase.security.token.AuthenticationTokenIdentifier not found
```

- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

## Release 6.1.0

The following release notes include information for Amazon EMR release 6.1.0. Changes
are relative to 6.0.0.

Initial release date: Sept 04, 2020

Last updated date: Oct 15, 2020

###### Supported applications

- AWS SDK for Java version 1.11.828
- Flink version 1.11.0
- Ganglia version 3.7.2
- Hadoop version 3.2.1-amzn-1
- HBase version 2.2.5
- HBase-operator-tools 1.0.0
- HCatalog version 3.1.2-amzn-0
- Hive version 3.1.2-amzn-1
- Hudi version 0.5.2-incubating
- Hue version 4.7.1
- JupyterHub version 1.1.0
- Livy version 0.7.0
- MXNet version 1.6.0
- Oozie version 5.2.0
- Phoenix version 5.0.0
- Presto version 0.232
- PrestoSQL version 338
- Spark version 3.0.0-amzn-0
- TensorFlow version 2.1.0
- Zeppelin version 0.9.0-preview1
- Zookeeper version 3.4.14
- Connectors and drivers: DynamoDB Connector 4.14.0

###### New features

- ARM instance types are supported starting with Amazon EMR version 5.30.0 and Amazon EMR version 6.1.0.
- M6g general purpose instance types are supported starting with Amazon EMR versions 6.1.0 and 5.30.0. For more information, see [Supported Instance Types](../ManagementGuide/emr-supported-instance-types.md "../ManagementGuide/emr-supported-instance-types.md") in the _Amazon EMR Management Guide_.
- The EC2 placement group feature is supported starting with Amazon EMR version 5.23.0 as an option for multiple primary node clusters. Currently, only primary node types are supported by the placement group feature, and the `SPREAD` strategy is applied to those primary nodes.
  The `SPREAD` strategy places a small group of instances across separate underlying hardware to guard against the loss of multiple primary nodes in the event of a hardware failure. For more information, see [EMR Integration with EC2 Placement Group](../ManagementGuide/emr-plan-ha-placementgroup.md "../ManagementGuide/emr-plan-ha-placementgroup.md") in the _Amazon EMR Management Guide_.
- Managed Scaling – With Amazon EMR version 6.1.0,
  you can enable Amazon EMR managed scaling to automatically increase or decrease the number
  of instances or units in your cluster based on workload. Amazon EMR continuously evaluates
  cluster metrics to make scaling decisions that optimize your clusters for cost and
  speed. Managed Scaling is also available on Amazon EMR version 5.30.0 and later, except 6.0.0. For more information, see [Scaling Cluster Resources](../ManagementGuide/emr-scale-on-demand.md "../ManagementGuide/emr-scale-on-demand.md") in the
  _Amazon EMR Management Guide_.
- PrestoSQL version 338 is supported with EMR 6.1.0.
  For more information, see [Presto](emr-presto.md "emr-presto.md").
  - PrestoSQL is supported on EMR 6.1.0 and later versions only, not on EMR 6.0.0 or EMR 5.x.
  - The application name, `Presto` continues to be used to install PrestoDB on clusters. To install PrestoSQL on clusters, use the application name `PrestoSQL`.
  - You can install either PrestoDB or PrestoSQL, but you cannot install both on a single cluster. If both PrestoDB and PrestoSQL are specified when attempting to create a cluster, a validation error occurs and the cluster creation request fails.
  - PrestoSQL is supported on both single-master and muti-master clusters. On multi-master clusters, an external Hive metastore is required to run PrestoSQL or PrestoDB. See [Supported applications in an EMR cluster with multiple primary nodes](../ManagementGuide/emr-plan-ha-applications.md#emr-plan-ha-applications-list "../ManagementGuide/emr-plan-ha-applications.md#emr-plan-ha-applications-list").

- ECR auto authentication support on Apache Hadoop and Apache Spark with Docker: Spark users can use Docker images from Docker Hub and Amazon Elastic Container Registry (Amazon ECR) to define environment and library dependencies.

[Configure Docker](../ManagementGuide/emr-plan-docker.md "../ManagementGuide/emr-plan-docker.md") and [Run Spark Applications with Docker Using Amazon EMR 6.x](emr-spark-docker.md "emr-spark-docker.md").

- EMR supports Apache Hive ACID transactions: Amazon EMR 6.1.0 adds support for Hive ACID transactions so it complies with the ACID properties of a database. With this feature, you can run `INSERT, UPDATE, DELETE,` and `MERGE` operations in Hive managed tables with data in Amazon Simple Storage Service (Amazon S3). This is a key feature for use cases like streaming ingestion, data restatement, bulk updates using MERGE, and slowly changing dimensions.
  For more information, including configuration examples and use cases, see [Amazon EMR supports Apache Hive ACID transactions](https://aws.amazon.com/blogs/big-data/amazon-emr-supports-apache-hive-acid-transactions "https://aws.amazon.com/blogs/big-data/amazon-emr-supports-apache-hive-acid-transactions").

###### Changes, enhancements, and resolved issues

- This is a release to fix issues with Amazon EMR Scaling when it fails to scale up/scale down a cluster successfully or causes application failures.
- Fixed an issue where scaling requests failed for a large, highly utilized cluster when Amazon EMR on-cluster daemons were running health checking activities, such as gathering YARN node state and HDFS node state. This was happening because on-cluster daemons were not able to communicate the health status data of a node to internal Amazon EMR components.
- Improved EMR on-cluster daemons to correctly track the node states when IP addresses are reused to improve reliability during scaling operations.
- [SPARK-29683](https://issues.apache.org/jira/browse/SPARK-29683 "https://issues.apache.org/jira/browse/SPARK-29683"). Fixed an issue where job failures occurred during cluster scale-down as Spark was assuming all available nodes were deny-listed.
- [YARN-9011](https://issues.apache.org/jira/browse/YARN-9011 "https://issues.apache.org/jira/browse/YARN-9011"). Fixed an issue where job failures occurred due to a race condition in YARN decommissioning when cluster tried to scale up or down.
- Fixed issue with step or job failures during cluster scaling by ensuring that the node states are always consistent between the Amazon EMR on-cluster daemons and YARN/HDFS.
- Fixed an issue where cluster operations such as scale down and step submission failed for Amazon EMR clusters enabled with Kerberos authentication. This was because the Amazon EMR on-cluster daemon did not renew the Kerberos ticket, which is required to securely communicate with HDFS/YARN running on the primary node.
- Newer Amazon EMR releases fix the issue with a lower "Max open files" limit on older AL2 in Amazon EMR. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later now include a permanent fix with a higher "Max open files" setting.
- Apache Flink is not supported on EMR 6.0.0, but it is supported on EMR 6.1.0 with Flink 1.11.0. This is the first version of Flink to officially support Hadoop 3. See [Apache Flink 1.11.0 Release Announcement](https://flink.apache.org/news/2020/07/06/release-1.11.0.html "https://flink.apache.org/news/2020/07/06/release-1.11.0.html").
- Ganglia has been removed from default EMR 6.1.0 package bundles.

###### Known issues

- **Lower "Max open files" limit on older AL2 [fixed in newer releases].** Amazon EMR releases: emr-5.30.x, emr-5.31.0, emr-5.32.0, emr-6.0.0, emr-6.1.0, and emr-6.2.0 are based on older versions ofAmazon Linux 2 (AL2), which have a lower ulimit setting for "Max open files" when Amazon EMR clusters are created with the default AMI. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later include a permanent fix with a higher "Max open files" setting.
  Releases with the lower open file limit causes a "Too many open files" error when submitting Spark job. In the impacted releases, the Amazon EMR default AMI has a default ulimit setting of 4096 for "Max open files," which is lower than the 65536 file limit in the latestAmazon Linux 2 AMI.
  The lower ulimit setting for "Max open files" causes Spark job failure when the Spark driver and executor try to open more than 4096 files. To fix the issue, Amazon EMR has a bootstrap action (BA) script that adjusts the ulimit setting at cluster creation.

If you are using an older Amazon EMR version that doesn't have the permanent fix for this issue, the following workaround lets you to explicitly set the instance-controller ulimit to a maximum of 65536 files.

###### Explicitly set a ulimit from the command line

    1. Edit `/etc/systemd/system/instance-controller.service` to add the following parameters to Service section.


    `LimitNOFILE=65536`


    `LimitNPROC=65536`
    2. Restart InstanceController


    `$ sudo systemctl daemon-reload`


    `$ sudo systemctl restart instance-controller`

**Set a ulimit using bootstrap action (BA)**

You can also use a bootstrap action (BA) script to configure the instance-controller ulimit to 65536 files at cluster creation.

```
#!/bin/bash
for user in hadoop spark hive; do
sudo tee /etc/security/limits.d/$user.conf << EOF
$user - nofile 65536
$user - nproc 65536
EOF
done
for proc in instancecontroller logpusher; do
sudo mkdir -p /etc/systemd/system/$proc.service.d/
sudo tee /etc/systemd/system/$proc.service.d/override.conf << EOF
[Service]
LimitNOFILE=65536
LimitNPROC=65536
EOF
pid=$(pgrep -f aws157.$proc.Main)
sudo prlimit --pid $pid --nofile=65535:65535 --nproc=65535:65535
done
sudo systemctl daemon-reload
```

- ###### Important

Amazon EMR 6.1.0 and 6.2.0 include a performance issue that can critically affect all Hudi insert, upsert, and delete operations. If you plan to use Hudi with Amazon EMR 6.1.0 or 6.2.0, you should contact AWS support to obtain a patched Hudi RPM.

- If you set custom garbage collection configuration with `spark.driver.extraJavaOptions` and `spark.executor.extraJavaOptions`, this will result in driver/executor launch failure with EMR 6.1 due to conflicting garbage collection configuration. With EMR Release 6.1.0, you should specify custom Spark garbage collection configuration for drivers and executors with the properties `spark.driver.defaultJavaOptions` and `spark.executor.defaultJavaOptions` instead. Read more in [Apache Spark Runtime Environment](https://spark.apache.org/docs/latest/configuration.html#runtime-environment "https://spark.apache.org/docs/latest/configuration.html#runtime-environment") and [Configuring Spark Garbage Collection on Amazon EMR 6.1.0](emr-spark-configure.md#spark-gc-config "emr-spark-configure.md#spark-gc-config").
- Using Pig with Oozie (and within Hue, since Hue uses Oozie actions to run Pig scripts), generates an error that a native-lzo library cannot be loaded. This error message is informational and does not block Pig from running.
- Hudi Concurrency Support: Currently Hudi doesn't support concurrent writes to a single Hudi table. In addition, Hudi rolls back any changes being done by in-progress writers before allowing a new writer to start. Concurrent writes can interfere with this mechanism and introduce race conditions, which can lead to data corruption. You should ensure that as part of your data processing workflow, there is only a single Hudi writer operating against a Hudi table at any time. Hudi does support multiple concurrent readers operating against the same Hudi table.
- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

- There is an issue in Amazon EMR 6.1.0 that affects clusters running Presto. After an extended period of time (days), the cluster may throw errors such as, "su: failed to execute /bin/bash: Resource temporarily unavailable" or "shell request failed on channel 0".
  This issue is caused by an internal Amazon EMR process (InstanceController) that is spawning too many Light Weight Processes (LWP), which eventually causes the Hadoop user to exceed their nproc limit.
  This prevents the user from opening additional processes. The solution for this issue is to upgrade to EMR 6.2.0.

## Release 6.0.0

The following release notes include information for Amazon EMR release 6.0.0.

Initial release date: March 10, 2020

###### Supported applications

- AWS SDK for Java version 1.11.711
- Ganglia version 3.7.2
- Hadoop version 3.2.1
- HBase version 2.2.3
- HCatalog version 3.1.2
- Hive version 3.1.2
- Hudi version 0.5.0-incubating
- Hue version 4.4.0
- JupyterHub version 1.0.0
- Livy version 0.6.0
- MXNet version 1.5.1
- Oozie version 5.1.0
- Phoenix version 5.0.0
- Presto version 0.230
- Spark version 2.4.4
- TensorFlow version 1.14.0
- Zeppelin version 0.9.0-SNAPSHOT
- Zookeeper version 3.4.14
- Connectors and drivers: DynamoDB Connector 4.14.0

###### Note

Flink, Sqoop, Pig, and Mahout are not available in Amazon EMR version 6.0.0.

###### New features

- YARN Docker Runtime Support - YARN applications, such as Spark jobs, can now run in the
  context of a Docker container. This allows you to easily define dependencies in
  a Docker image without the need to install custom libraries on your Amazon EMR cluster.
  For more information, see [Configure Docker Integration](../ManagementGuide/emr-plan-docker.md "../ManagementGuide/emr-plan-docker.md") and [Run Spark applications with Docker using Amazon EMR 6.0.0](emr-spark-docker.md "emr-spark-docker.md").
- Hive LLAP Support - Hive now supports the LLAP execution mode for improved query performance. For more information, see [Using Hive LLAP](emr-hive-llap.md "emr-hive-llap.md").

###### Changes, enhancements, and resolved issues

- This is a release to fix issues with Amazon EMR Scaling when it fails to scale up/scale down a cluster successfully or causes application failures.
- Fixed an issue where scaling requests failed for a large, highly utilized cluster when Amazon EMR on-cluster daemons were running health checking activities, such as gathering YARN node state and HDFS node state. This was happening because on-cluster daemons were not able to communicate the health status data of a node to internal Amazon EMR components.
- Improved EMR on-cluster daemons to correctly track the node states when IP addresses are reused to improve reliability during scaling operations.
- [SPARK-29683](https://issues.apache.org/jira/browse/SPARK-29683 "https://issues.apache.org/jira/browse/SPARK-29683"). Fixed an issue where job failures occurred during cluster scale-down as Spark was assuming all available nodes were deny-listed.
- [YARN-9011](https://issues.apache.org/jira/browse/YARN-9011 "https://issues.apache.org/jira/browse/YARN-9011"). Fixed an issue where job failures occurred due to a race condition in YARN decommissioning when cluster tried to scale up or down.
- Fixed issue with step or job failures during cluster scaling by ensuring that the node states are always consistent between the Amazon EMR on-cluster daemons and YARN/HDFS.
- Fixed an issue where cluster operations such as scale down and step submission failed for Amazon EMR clusters enabled with Kerberos authentication. This was because the Amazon EMR on-cluster daemon did not renew the Kerberos ticket, which is required to securely communicate with HDFS/YARN running on the primary node.
- Newer Amazon EMR releases fix the issue with a lower "Max open files" limit on older AL2 in Amazon EMR. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later now include a permanent fix with a higher "Max open files" setting.
- Amazon Linux
  - Amazon Linux 2 is the operating system for the EMR 6.x release series.
  - `systemd` is used for service management instead of `upstart` used inAmazon Linux 1.

- Java Development Kit (JDK)
  - Corretto JDK 8 is the default JDK for the EMR 6.x release series.

- Scala
  - Scala 2.12 is used with Apache Spark and Apache Livy.

- Python 3
  - Python 3 is now the default version of Python in EMR.

- YARN node labels
  - Beginning with Amazon EMR 6.x release series, the YARN node labels feature is disabled by default. The application
    master processes can run on both core and task nodes by default. You can enable the
    YARN node labels feature by configuring following properties: `yarn.node-labels.enabled` and `yarn.node-labels.am.default-node-label-expression`. For more information, see [Understanding Primary, Core, and Task Nodes](../ManagementGuide/emr-master-core-task-nodes.md "../ManagementGuide/emr-master-core-task-nodes.md").

###### Known issues

- **Lower "Max open files" limit on older AL2 [fixed in newer releases].** Amazon EMR releases: emr-5.30.x, emr-5.31.0, emr-5.32.0, emr-6.0.0, emr-6.1.0, and emr-6.2.0 are based on older versions ofAmazon Linux 2 (AL2), which have a lower ulimit setting for "Max open files" when Amazon EMR clusters are created with the default AMI. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later include a permanent fix with a higher "Max open files" setting.
  Releases with the lower open file limit causes a "Too many open files" error when submitting Spark job. In the impacted releases, the Amazon EMR default AMI has a default ulimit setting of 4096 for "Max open files," which is lower than the 65536 file limit in the latestAmazon Linux 2 AMI.
  The lower ulimit setting for "Max open files" causes Spark job failure when the Spark driver and executor try to open more than 4096 files. To fix the issue, Amazon EMR has a bootstrap action (BA) script that adjusts the ulimit setting at cluster creation.

If you are using an older Amazon EMR version that doesn't have the permanent fix for this issue, the following workaround lets you to explicitly set the instance-controller ulimit to a maximum of 65536 files.

###### Explicitly set a ulimit from the command line

    1. Edit `/etc/systemd/system/instance-controller.service` to add the following parameters to Service section.


    `LimitNOFILE=65536`


    `LimitNPROC=65536`
    2. Restart InstanceController


    `$ sudo systemctl daemon-reload`


    `$ sudo systemctl restart instance-controller`

**Set a ulimit using bootstrap action (BA)**

You can also use a bootstrap action (BA) script to configure the instance-controller ulimit to 65536 files at cluster creation.

```
#!/bin/bash
for user in hadoop spark hive; do
sudo tee /etc/security/limits.d/$user.conf << EOF
$user - nofile 65536
$user - nproc 65536
EOF
done
for proc in instancecontroller logpusher; do
sudo mkdir -p /etc/systemd/system/$proc.service.d/
sudo tee /etc/systemd/system/$proc.service.d/override.conf << EOF
[Service]
LimitNOFILE=65536
LimitNPROC=65536
EOF
pid=$(pgrep -f aws157.$proc.Main)
sudo prlimit --pid $pid --nofile=65535:65535 --nproc=65535:65535
done
sudo systemctl daemon-reload
```

- Spark interactive shell, including PySpark, SparkR, and spark-shell, does not
  support using Docker with additional libraries.
- To use Python 3 with Amazon EMR version 6.0.0, you must add `PATH` to `yarn.nodemanager.env-whitelist`.
- The Live Long and Process (LLAP) functionality is not supported when you use the AWS Glue Data Catalog as the metastore for Hive.
- When using Amazon EMR 6.0.0 with Spark and Docker integration, you need to configure the instances in your cluster with the same instance type and the same amount of EBS volumes to avoid failure when submitting a Spark job with Docker runtime.
- In Amazon EMR 6.0.0, HBase on Amazon S3 storage mode is impacted by the [HBASE-24286](https://issues.apache.org/jira/browse/HBASE-24286 "https://issues.apache.org/jira/browse/HBASE-24286"). issue. HBase master cannot initialize when the cluster is created using existing S3 data.
- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.30.1

The following release notes include information for Amazon EMR release 5.30.1. Changes
are relative to 5.30.0.

Initial release date: June 30, 2020

Last updated date: August 24, 2020

###### Changes, enhancements, and resolved issues

- Newer Amazon EMR releases fix the issue with a lower "Max open files" limit on older AL2 in Amazon EMR. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later now include a permanent fix with a higher "Max open files" setting.
- Fixed issue where instance controller process spawned infinite number of processes.
- Fixed issue where Hue was unable to run an Hive query, showing a "database is locked" message and preventing the execution of queries.
- Fixed a Spark issue to enable more tasks to run concurrently on the EMR cluster.
- Fixed a Jupyter notebook issue causing a "too many files open error" in the Jupyter server.
- Fixed an issue with cluster start times.

###### New features

- Tez UI and YARN timeline server persistent application interfaces are available with Amazon EMR versions 6.x, and EMR version 5.30.1 and later. One-click link access to persistent application history lets you quickly access job history without setting up a web proxy through an SSH connection. Logs for active and terminated clusters are available for 30 days after the application ends. For more information, see [View Persistent Application User Interfaces](../ManagementGuide/app-history-spark-UI.md "../ManagementGuide/app-history-spark-UI.md") in the _Amazon EMR Management Guide_.
- EMR Notebook execution APIs are available to execute EMR notebooks via a script or command line. The ability to start, stop, list, and describe EMR notebook executions without the AWS console enables you programmatically control an EMR notebook.
  Using a parameterized notebook cell, you can pass different parameter values to a notebook without having to create a copy of the notebook for each new set of paramter values. See [EMR API Actions.](../APIReference/API_Operations.md "../APIReference/API_Operations.md") For sample code, see [Sample commands to execute EMR Notebooks
  programmatically.](../ManagementGuide/emr-managed-notebooks-headless.md "../ManagementGuide/emr-managed-notebooks-headless.md")

###### Known issues

- **Lower "Max open files" limit on older AL2 [fixed in newer releases].** Amazon EMR releases: emr-5.30.x, emr-5.31.0, emr-5.32.0, emr-6.0.0, emr-6.1.0, and emr-6.2.0 are based on older versions ofAmazon Linux 2 (AL2), which have a lower ulimit setting for "Max open files" when Amazon EMR clusters are created with the default AMI. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later include a permanent fix with a higher "Max open files" setting.
  Releases with the lower open file limit causes a "Too many open files" error when submitting Spark job. In the impacted releases, the Amazon EMR default AMI has a default ulimit setting of 4096 for "Max open files," which is lower than the 65536 file limit in the latestAmazon Linux 2 AMI.
  The lower ulimit setting for "Max open files" causes Spark job failure when the Spark driver and executor try to open more than 4096 files. To fix the issue, Amazon EMR has a bootstrap action (BA) script that adjusts the ulimit setting at cluster creation.

If you are using an older Amazon EMR version that doesn't have the permanent fix for this issue, the following workaround lets you to explicitly set the instance-controller ulimit to a maximum of 65536 files.

###### Explicitly set a ulimit from the command line

    1. Edit `/etc/systemd/system/instance-controller.service` to add the following parameters to Service section.


    `LimitNOFILE=65536`


    `LimitNPROC=65536`
    2. Restart InstanceController


    `$ sudo systemctl daemon-reload`


    `$ sudo systemctl restart instance-controller`

**Set a ulimit using bootstrap action (BA)**

You can also use a bootstrap action (BA) script to configure the instance-controller ulimit to 65536 files at cluster creation.

```
#!/bin/bash
for user in hadoop spark hive; do
sudo tee /etc/security/limits.d/$user.conf << EOF
$user - nofile 65536
$user - nproc 65536
EOF
done
for proc in instancecontroller logpusher; do
sudo mkdir -p /etc/systemd/system/$proc.service.d/
sudo tee /etc/systemd/system/$proc.service.d/override.conf << EOF
[Service]
LimitNOFILE=65536
LimitNPROC=65536
EOF
pid=$(pgrep -f aws157.$proc.Main)
sudo prlimit --pid $pid --nofile=65535:65535 --nproc=65535:65535
done
sudo systemctl daemon-reload
```

- **EMR Notebooks**

The feature that allows you to install kernels and additional Python libraries on the cluster primary node is disabled by default on EMR version 5.30.1. For more information about this feature, see [Installing Kernels and Python Libraries on a Cluster Primary Node](../ManagementGuide/emr-managed-notebooks-installing-libraries-and-kernels.md "../ManagementGuide/emr-managed-notebooks-installing-libraries-and-kernels.md").

To enable the feature, do the following:

    1. Make sure that the permissions policy attached to the service role for EMR Notebooks allows the following action:


    `elasticmapreduce:ListSteps`


    For more information, see [Service Role for EMR Notebooks](../ManagementGuide/emr-managed-notebooks-service-role.md "../ManagementGuide/emr-managed-notebooks-service-role.md").
    2. Use the AWS CLI to run a step on the cluster that sets up EMR Notebooks as shown in the following example. Replace `us-east-1` with the Region in which your cluster resides. For more information, see [Adding Steps to a Cluster Using the AWS CLI](../ManagementGuide/add-step-cli.md "../ManagementGuide/add-step-cli.md").



    ```
    `aws emr add-steps --cluster-id `MyClusterID` --steps Type=CUSTOM_JAR,Name=EMRNotebooksSetup,ActionOnFailure=CONTINUE,Jar=s3://`us-east-1`.elasticmapreduce/libs/script-runner/script-runner.jar,Args=["s3://awssupportdatasvcs.com/bootstrap-actions/EMRNotebooksSetup/emr-notebooks-setup.sh"]`
    ```

- **Managed scaling**

Managed scaling operations on 5.30.0 and 5.30.1 clusters without Presto installed may cause application failures or cause a uniform instance group or instance fleet to stay in the `ARRESTED` state, particularly when a scale down operation is followed quickly by a scale up operation.

As a workaround, choose Presto as an application to install when you create a cluster with Amazon EMR releases 5.30.0 and 5.30.1, even if your job does not require Presto.

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

## Release 5.30.0

The following release notes include information for Amazon EMR release 5.30.0. Changes
are relative to 5.29.0.

Initial release date: May 13, 2020

Last updated date: June 25, 2020

###### Upgrades

- Upgraded AWS SDK for Java to version 1.11.759
- Upgraded Amazon SageMaker Spark SDK to version 1.3.0
- Upgraded EMR Record Server to version 1.6.0
- Upgraded Flink to version 1.10.0
- Upgraded Ganglia to version 3.7.2
- Upgraded HBase to version 1.4.13
- Upgraded Hudi to version 0.5.2-incubating
- Upgraded Hue to version 4.6.0
- Upgraded JupyterHub to version 1.1.0
- Upgraded Livy to version 0.7.0-incubating
- Upgraded Oozie to version 5.2.0
- Upgraded Presto to version 0.232
- Upgraded Spark to version 2.4.5
- Upgraded Connectors and drivers: Amazon Glue Connector 1.12.0; Amazon Kinesis Connector 3.5.0; EMR DynamoDB Connector 4.14.0

###### New features

- **EMR Notebooks** – When used with EMR clusters created using 5.30.0, EMR notebook kernels run on cluster. This improves notebook performance and allows you to install and customize kernels. You can also install Python libraries on the cluster primary node. For more information, see [Installing and Using Kernels and Libraries](../ManagementGuide/emr-managed-notebooks-installing-libraries-and-kernels.md "../ManagementGuide/emr-managed-notebooks-installing-libraries-and-kernels.md") in the _EMR Management Guide_.
- **Managed Scaling** – With Amazon EMR version 5.30.0 and later,
  you can enable EMR managed scaling to automatically increase or decrease the number
  of instances or units in your cluster based on workload. Amazon EMR continuously evaluates
  cluster metrics to make scaling decisions that optimize your clusters for cost and
  speed. For more information, see [Scaling Cluster Resources](../ManagementGuide/emr-scale-on-demand.md "../ManagementGuide/emr-scale-on-demand.md") in the
  _Amazon EMR Management Guide_.
- **Encrypt log files stored in Amazon S3** – With Amazon EMR version 5.30.0 and later, you can encrypt log files stored
  in Amazon S3 with an AWS KMS customer managed key. For more information, see [Encrypt log files stored in Amazon S3](../ManagementGuide/emr-plan-debugging.md#emr-log-encryption "../ManagementGuide/emr-plan-debugging.md#emr-log-encryption") in the
  _Amazon EMR Management Guide_.
- **Amazon Linux 2 support** – In EMR version 5.30.0 and later, EMR usesAmazon Linux 2 OS. New custom AMIs (Amazon Machine Image) must be based on theAmazon Linux 2 AMI. For more information, see [Using a Custom AMI](../ManagementGuide/emr-custom-ami.md "../ManagementGuide/emr-custom-ami.md").
- **Presto Graceful Auto Scale** – EMR clusters using 5.30.0 can be set with an auto scaling timeout period that gives Presto tasks time to finish running before their node is decommissioned. For more information, see [Using Presto automatic scaling with Graceful
  Decommission](presto-graceful-autoscale.md "presto-graceful-autoscale.md").
- **Fleet Instance creation with new allocation strategy option** – A new allocation strategy option is available in EMR version 5.12.1 and later. It offers faster cluster provisioning, more accurate spot allocation, and less spot instance interruption. Updates to non-default EMR service roles are required. See [Configure Instance Fleets](../ManagementGuide/emr-instance-fleet.md "../ManagementGuide/emr-instance-fleet.md").
- **sudo systemctl stop and sudo systemctl start commands** – In EMR version 5.30.0 and later, which useAmazon Linux 2 OS, EMR uses `sudo systemctl stop` and `sudo systemctl start` commands to restart services. For more information, see [How do I restart a service in Amazon EMR?](https://aws.amazon.com/premiumsupport/knowledge-center/restart-service-emr/ "https://aws.amazon.com/premiumsupport/knowledge-center/restart-service-emr/").

###### Changes, enhancements, and resolved issues

- EMR version 5.30.0 doesn't install Ganglia by default. You can explicitly select Ganglia to install when you create a cluster.
- Spark performance optimizations.
- Presto performance optimizations.
- Python 3 is the default for Amazon EMR version 5.30.0 and later.
- The default managed security group for service access in private subnets has been
  updated with new rules. If you use a custom
  security group for service access, you must include the same rules as the default managed security group. For more information, see [Amazon EMR-Managed Security Group for Service Access (Private Subnets)](../ManagementGuide/emr-man-sec-groups.md#emr-sg-elasticmapreduce-sa-private "../ManagementGuide/emr-man-sec-groups.md#emr-sg-elasticmapreduce-sa-private"). If you use a custom service role for Amazon EMR, you must grant permission to `ec2:describeSecurityGroups` so that EMR can validate if the security groups are correctly created. If you use the `EMR_DefaultRole`, this permission is already included in the default managed policy.

###### Known issues

- **Lower "Max open files" limit on older AL2 [fixed in newer releases].** Amazon EMR releases: emr-5.30.x, emr-5.31.0, emr-5.32.0, emr-6.0.0, emr-6.1.0, and emr-6.2.0 are based on older versions ofAmazon Linux 2 (AL2), which have a lower ulimit setting for "Max open files" when Amazon EMR clusters are created with the default AMI. Amazon EMR releases 5.30.1, 5.30.2, 5.31.1, 5.32.1, 6.0.1, 6.1.1, 6.2.1, 5.33.0, 6.3.0 and later include a permanent fix with a higher "Max open files" setting.
  Releases with the lower open file limit causes a "Too many open files" error when submitting Spark job. In the impacted releases, the Amazon EMR default AMI has a default ulimit setting of 4096 for "Max open files," which is lower than the 65536 file limit in the latestAmazon Linux 2 AMI.
  The lower ulimit setting for "Max open files" causes Spark job failure when the Spark driver and executor try to open more than 4096 files. To fix the issue, Amazon EMR has a bootstrap action (BA) script that adjusts the ulimit setting at cluster creation.

If you are using an older Amazon EMR version that doesn't have the permanent fix for this issue, the following workaround lets you to explicitly set the instance-controller ulimit to a maximum of 65536 files.

###### Explicitly set a ulimit from the command line

    1. Edit `/etc/systemd/system/instance-controller.service` to add the following parameters to Service section.


    `LimitNOFILE=65536`


    `LimitNPROC=65536`
    2. Restart InstanceController


    `$ sudo systemctl daemon-reload`


    `$ sudo systemctl restart instance-controller`

**Set a ulimit using bootstrap action (BA)**

You can also use a bootstrap action (BA) script to configure the instance-controller ulimit to 65536 files at cluster creation.

```
#!/bin/bash
for user in hadoop spark hive; do
sudo tee /etc/security/limits.d/$user.conf << EOF
$user - nofile 65536
$user - nproc 65536
EOF
done
for proc in instancecontroller logpusher; do
sudo mkdir -p /etc/systemd/system/$proc.service.d/
sudo tee /etc/systemd/system/$proc.service.d/override.conf << EOF
[Service]
LimitNOFILE=65536
LimitNPROC=65536
EOF
pid=$(pgrep -f aws157.$proc.Main)
sudo prlimit --pid $pid --nofile=65535:65535 --nproc=65535:65535
done
sudo systemctl daemon-reload
```

- **Managed scaling**

Managed scaling operations on 5.30.0 and 5.30.1 clusters without Presto installed may cause application failures or cause a uniform instance group or instance fleet to stay in the `ARRESTED` state, particularly when a scale down operation is followed quickly by a scale up operation.

As a workaround, choose Presto as an application to install when you create a cluster with Amazon EMR releases 5.30.0 and 5.30.1, even if your job does not require Presto.

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

- The default database engine for Hue 4.6.0 is SQLite, which causes issues when you try to use Hue with an external database. To fix this, set `engine` in your `hue-ini` configuration classification to `mysql`. This issue has been fixed in Amazon EMR version 5.30.1.
- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

## Release 5.29.0

The following release notes include information for Amazon EMR release 5.29.0. Changes
are relative to 5.28.1.

Initial release date: Jan 17, 2020

###### Upgrades

- Upgraded AWS SDK for Java to version 1.11.682
- Upgraded Hive to version 2.3.6
- Upgraded Flink to version 1.9.1
- Upgraded EmrFS to version 2.38.0
- Upgraded EMR DynamoDB Connector to version 4.13.0

###### Changes, enhancements, and resolved issues

- Spark
  - Spark performance optimizations.

- EMRFS
  - Management Guide updates to emrfs-site.xml default settings for consistent view.

###### Known issues

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.28.1

The following release notes include information for Amazon EMR release 5.28.1. Changes
are relative to 5.28.0.

Initial release date: Jan 10, 2020

###### Changes, enhancements, and resolved issues

- Spark
  - Fixed Spark compatibility issues.

- CloudWatch Metrics
  - Fixed Amazon CloudWatch Metrics publishing on an EMR cluster with multiple primary nodes.

- Disabled log message
  - Disabled false log message, "...using old version (<4.5.8) of Apache http client."

###### Known issues

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.28.0

The following release notes include information for Amazon EMR release 5.28.0. Changes
are relative to 5.27.0.

Initial release date: Nov 12, 2019

###### Upgrades

- Upgraded Flink to version 1.9.0
- Upgraded Hive to version 2.3.6
- Upgraded MXNet to version 1.5.1
- Upgraded Phoenix to version 4.14.3
- Upgraded Presto to version 0.227
- Upgraded Zeppelin to version 0.8.2

###### New features

- [Apache Hudi](https://hudi.apache.org/ "https://hudi.apache.org/") is now available for Amazon EMR to install when you create a cluster. For more information, see [Hudi](emr-hudi.md "emr-hudi.md").
- (Nov 25, 2019) You can now choose to run
  multiple steps in parallel to improve cluster utilization and save cost. You can also cancel both pending and running steps. For
  more information, see [Work with Steps Using the AWS CLI and Console](../ManagementGuide/emr-work-with-steps.md "../ManagementGuide/emr-work-with-steps.md").
- (Dec 3, 2019) You can now create and run EMR clusters on AWS Outposts. AWS Outposts enables native AWS services, infrastructure, and operating models in on-premises facilities. In AWS Outposts environments, you can use the same AWS APIs, tools, and infrastructure that you use in the AWS cloud. For
  more information, see [EMR clusters on AWS Outposts](../ManagementGuide/emr-plan-outposts.md "../ManagementGuide/emr-plan-outposts.md").
- (Mar 11, 2020) Beginning with Amazon EMR version 5.28.0, you can create and run Amazon EMR clusters on an AWS Local Zones subnet as a logical extension of an AWS Region that supports Local Zones. A Local Zone enables Amazon EMR features and a subset of AWS services, like compute and storage services, to be located closer to users, providing very low latency access to applications running locally. For a list of available Local Zones, see [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/"). For information about accessing available AWS Local Zones, see [Regions, Availability Zones, and Local Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md").

Local Zones do not currently support Amazon EMR Notebooks and do not support connections directly to Amazon EMR using interface VPC endpoint (AWS PrivateLink).

###### Changes, enhancements, and resolved issues

- Expanded Application Support for High Availability Clusters
  - For more information, see [Supported applications in an EMR cluster with Multiple Primary Nodes](../ManagementGuide/emr-plan-ha-applications.md#emr-plan-ha-applications-list "../ManagementGuide/emr-plan-ha-applications.md#emr-plan-ha-applications-list") in the _Amazon EMR Management Guide_.

- Spark
  - Performance optimizations

- Hive
  - Performance optimizations

- Presto
  - Performance optimizations

###### Known issues

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.27.0

The following release notes include information for Amazon EMR release 5.27.0. Changes
are relative to 5.26.0.

Initial release date: Sep 23, 2019

###### Upgrades

- AWS SDK for Java 1.11.615
- Flink 1.8.1
- JupyterHub 1.0.0
- Spark 2.4.4
- Tensorflow 1.14.0
- Connectors and drivers:
  - DynamoDB Connector 4.12.0

###### New features

- (Oct 24, 2019) The following New features in EMR notebooks
  are available with all Amazon EMR releases.
  - You can now associate Git repositories with EMR notebooks to store your
    notebooks in a version controlled environment. You can share code with peers and
    reuse existing Jupyter notebooks through remote Git repositories. For more information, see [Associate Git Repositories with Amazon EMR Notebooks](../ManagementGuide/emr-git-repo.md "../ManagementGuide/emr-git-repo.md") in the
    _Amazon EMR Management Guide_.
  - The [nbdime utility](https://github.com/jupyter/nbdime "https://github.com/jupyter/nbdime") is now available in EMR notebooks to simplify comparing and merging notebooks.
  - EMR notebooks now support JupyterLab. JupyterLab is a web-based interactive
    development environment fully compatible with Jupyter notebooks. You can now choose
    to open your notebook in either JupyterLab or Jupyter notebook editor.

- (Oct 30, 2019) With Amazon EMR versions 5.25.0 and later, you can connect to Spark history server
  UI from the cluster **Summary** page or the
  **Application history** tab in the console. Instead of
  setting up a web proxy through an SSH connection, you can quickly access the
  Spark history server UI to view application metrics and access relevant log
  files for active and terminated clusters. For more information, see [Off-cluster access to persistent application user interfaces](../ManagementGuide/app-history-spark-UI.md "../ManagementGuide/app-history-spark-UI.md") in the _Amazon EMR Management Guide_.

###### Changes, enhancements, and resolved issues

- Amazon EMR cluster with multiple primary nodes
  - You can install and run Flink on an Amazon EMR cluster with multiple primary nodes. For more information, see [Supported applications and features](../ManagementGuide/emr-plan-ha-applications.md "../ManagementGuide/emr-plan-ha-applications.md").
  - You can configure HDFS transparent encryption on an Amazon EMR cluster with multiple primary nodes. For more information, see [HDFS Transparent Encryption on EMR clusters with
    Multiple Primary Nodes](emr-encryption-tdehdfs.md#emr-hadoop-kms-multi-master "emr-encryption-tdehdfs.md#emr-hadoop-kms-multi-master").
  - You can now modify the configuration of applications running on an Amazon EMR cluster with multiple primary nodes. For more information, see [Supplying a Configuration for an Instance Group in a Running Cluster](emr-configure-apps-running-cluster.md "emr-configure-apps-running-cluster.md").

- Amazon EMR-DynamoDB Connector
  - Amazon EMR-DynamoDB Connector now supports the following DynamoDB data types: boolean, list, map, item, null. For more information, see [Set Up a Hive Table to Run Hive Commands](EMR_Interactive_Hive.md "EMR_Interactive_Hive.md").

###### Known issues

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.26.0

The following release notes include information for Amazon EMR release 5.26.0. Changes
are relative to 5.25.0.

Initial release date: Aug 8, 2019

Last updated date: Aug 19, 2019

###### Upgrades

- AWS SDK for Java 1.11.595
- HBase 1.4.10
- Phoenix 4.14.2
- Connectors and drivers:
  - DynamoDB Connector 4.11.0
  - MariaDB Connector 2.4.2
  - Amazon Redshift JDBC Driver 1.2.32.1056

###### New features

- (Beta) With Amazon EMR 5.26.0, you can launch a cluster that integrates with Lake Formation. This integration
  provides fine-grained, column-level access to databases and tables in the AWS Glue Data Catalog. It also enables federated single sign-on to EMR Notebooks or
  Apache Zeppelin from an enterprise identity system. For more information, see [Integrating Amazon EMR with AWS Lake Formation (Beta)](../ManagementGuide/emr-lake-formation.md "../ManagementGuide/emr-lake-formation.md").
- (Aug 19, 2019) Amazon EMR block public access is now available with all Amazon EMR releases that support security groups. Block public access is an account-wide setting applied to each AWS Region. Block public access prevents a cluster from launching when any
  security group associated with the cluster has a rule that allows inbound traffic from
  IPv4 0.0.0.0/0 or IPv6 ::/0 (public access) on a port, unless a port is specified as an exception. Port 22 is an exception by default. For more information, see [Using Amazon EMR Block Public Access](../ManagementGuide/emr-block-public-access.md "../ManagementGuide/emr-block-public-access.md") in the _Amazon EMR Management Guide_.

###### Changes, enhancements, and resolved issues

- EMR Notebooks
  - With EMR 5.26.0 and later, EMR Notebooks supports notebook-scoped Python libraries in addition to the default Python libraries. You can install notebook-scoped libraries from within the notebook editor without having to re-create a cluster or re-attach a notebook to a cluster. Notebook-scoped libraries are created in a Python virtual environment, so they apply only to the current notebook session. This allows you to isolate notebook dependencies. For more information, see [Using Notebook Scoped Libraries](../ManagementGuide/emr-managed-notebooks-custom-libraries-limitations.md "../ManagementGuide/emr-managed-notebooks-custom-libraries-limitations.md") in the _Amazon EMR Management Guide_.

- EMRFS
  - You can enable an ETag verification feature (Beta) by setting
    `fs.s3.consistent.metadata.etag.verification.enabled` to
    `true`. With this feature, EMRFS uses Amazon S3 ETags to
    verify that objects being read are the latest available version. This
    feature is helpful for read-after-update use cases in which files on
    Amazon S3 are overwritten while retaining the same name. This
    ETag verification capability currently does not work with S3 Select. For
    more information, see [Configure Consistent View](../ManagementGuide/emrfs-configure-consistent-view.md "../ManagementGuide/emrfs-configure-consistent-view.md").

- Spark
  - The following optimizations are now enabled by default: dynamic partition pruning, DISTINCT before INTERSECT, improvements in SQL plan statistics inference for JOIN followed by DISTINCT queries, flattening scalar subqueries, optimized join reorder, and bloom filter join. For more information, see [Optimizing Spark Performance](emr-spark-performance.md "emr-spark-performance.md").
  - Improved whole stage code generation for Sort Merge Join.
  - Improved query fragment and subquery reuse.
  - Improvements to pre-allocate executors on Spark start up.
  - Bloom filter joins are no longer applied when the smaller side of the join includes a broadcast hint.

- Tez
  - Resolved an issue with Tez. Tez UI now works on an Amazon EMR cluster with multiple primary nodes.

###### Known issues

- The improved whole stage code generation capabilities for Sort Merge Join can increase memory pressure when enabled. This optimization improves performance, but may result in job retries or failures if the `spark.yarn.executor.memoryOverheadFactor` is not tuned to provide enough memory. To disable this feature, set `spark.sql.sortMergeJoinExec.extendedCodegen.enabled` to false.
- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.25.0

The following release notes include information for Amazon EMR release 5.25.0. Changes
are relative to 5.24.1.

Initial release date: July 17, 2019

Last updated date: Oct 30, 2019

**Amazon EMR 5.25.0**

###### Upgrades

- AWS SDK for Java 1.11.566
- Hive 2.3.5
- Presto 0.220
- Spark 2.4.3
- TensorFlow 1.13.1
- Tez 0.9.2
- Zookeeper 3.4.14

###### New features

- (Oct 30, 2019) Beginning with Amazon EMR version 5.25.0, you can connect to Spark history server UI from the
  cluster **Summary** page or the **Application
  history** tab in the console. Instead of setting up a web proxy through an
  SSH connection, you can quickly access the Spark history server UI to view application
  metrics and access relevant log files for active and terminated clusters. For more information, see [Off-cluster access to persistent application user interfaces](../ManagementGuide/app-history-spark-UI.md "../ManagementGuide/app-history-spark-UI.md") in the _Amazon EMR Management Guide_.

###### Changes, enhancements, and resolved issues

- Spark

      + Improved the performance of some joins by using Bloom filters to pre-filter inputs. The optimization is disabled by default and can be enabled by setting the Spark configuration parameter `spark.sql.bloomFilterJoin.enabled` to `true`.
      + Improved the performance of grouping by string type columns.
      + Improved the default Spark executor memory and cores configuration of
       R4 instance types for clusters without HBase installed.
      + Resolved a previous issue with the dynamic partition pruning feature where the pruned table
       has to be on the left side of the join.
      + Improved DISTINCT before INTERSECT optimization to apply to additional cases involving aliases.
      + Improved SQL plan statistics inference for JOIN followed by DISTINCT queries. This
       improvement is disabled by default and can be enabled by setting the
       Spark configuration parameter `spark.sql.statsImprovements.enabled` to
       `true`. This optimization is required by the Distinct before Intersect
       feature and will be enabled automatically when
       `spark.sql.optimizer.distinctBeforeIntersect.enabled` is set to
       `true`.
      + Optimized join order based on table size and filters. This optimization is disabled by default
       and can be enabled by setting the Spark configuration parameter
       `spark.sql.optimizer.sizeBasedJoinReorder.enabled` to `true`.

  For more information, see [Optimizing Spark Performance](emr-spark-performance.md "emr-spark-performance.md").

- EMRFS
  - The EMRFS setting, `fs.s3.buckets.create.enabled`, is now disabled by
    default. With testing, we found that disabling this setting improves
    performance and prevents unintentional creation of S3 buckets. If your
    application relies on this functionality, you can enable it by setting
    the property `fs.s3.buckets.create.enabled` to
    `true` in the `emrfs-site` configuration
    classification. For information, see [Supplying
    a Configuration when Creating a Cluster](emr-configure-apps-create-cluster.md "emr-configure-apps-create-cluster.md").

- Local Disk Encryption and S3 Encryption Improvements in Security Configurations (August 5, 2019)
  - Separated Amazon S3 encryption settings from local disk encryption settings in security configuration setup.
  - Added an option to enable EBS encryption with release 5.24.0 and later. Selecting this option encrypts the root device volume in addition to storage volumes. Previous versions required using a custom AMI to encrypt the root device volume.
  - For more information, see [Encryption Options](../ManagementGuide/emr-data-encryption-options.md "../ManagementGuide/emr-data-encryption-options.md") in the _Amazon EMR Management Guide_.

###### Known issues

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.24.1

The following release notes include information for Amazon EMR release 5.24.1. Changes
are relative to 5.24.0.

Initial release date: June 26, 2019

###### Changes, enhancements, and resolved issues

- Updated the default Amazon Linux AMI for Amazon EMR to include important Linux kernel security updates, including the TCP SACK Denial of Service Issue ([AWS-2019-005](https://aws.amazon.com/security/security-bulletins/AWS-2019-005/ "https://aws.amazon.com/security/security-bulletins/AWS-2019-005/")).

###### Known issues

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.24.0

The following release notes include information for Amazon EMR release 5.24.0. Changes
are relative to 5.23.0.

Initial release date: June 11, 2019

Last updated date: August 5, 2019

###### Upgrades

- Flink 1.8.0
- Hue 4.4.0
- JupyterHub 0.9.6
- Livy 0.6.0
- MxNet 1.4.0
- Presto 0.219
- Spark 2.4.2
- AWS SDK for Java 1.11.546
- Connectors and drivers:
  - DynamoDB Connector 4.9.0
  - MariaDB Connector 2.4.1
  - Amazon Redshift JDBC Driver 1.2.27.1051

###### Changes, enhancements, and resolved issues

- Spark

      + Added optimization to dynamically prune partitions. The optimization is disabled by default. To enable it, set the Spark configuration parameter `spark.sql.dynamicPartitionPruning.enabled` to `true`.
      + Improved performance of `INTERSECT` queries. This optimization is disabled by default. To enable it, set the Spark configuration parameter `spark.sql.optimizer.distinctBeforeIntersect.enabled` to `true`.
      + Added optimization to flatten scalar subqueries with aggregates that use the same relation. The optimization is disabled by default. To enable it, set the Spark configuration parameter `spark.sql.optimizer.flattenScalarSubqueriesWithAggregates.enabled` to `true`.
      + Improved whole stage code generation.

  For more information, see [Optimizing Spark Performance](emr-spark-performance.md "emr-spark-performance.md").

- Local Disk Encryption and S3 Encryption Improvements in Security Configurations (August 5, 2019)
  - Separated Amazon S3 encryption settings from local disk encryption settings in security configuration setup.
  - Added an option to enable EBS encryption. Selecting this option encrypts the root device volume in addition to storage volumes. Previous versions required using a custom AMI to encrypt the root device volume.
  - For more information, see [Encryption Options](../ManagementGuide/emr-data-encryption-options.md "../ManagementGuide/emr-data-encryption-options.md") in the _Amazon EMR Management Guide_.

###### Known issues

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.23.0

The following release notes include information for Amazon EMR release 5.23.0. Changes
are relative to 5.22.0.

Initial release date: April 01, 2019

Last updated date: April 30, 2019

###### Upgrades

- AWS SDK for Java 1.11.519

###### New features

- (April 30, 2019) With Amazon EMR 5.23.0 and later, you can launch a cluster with three primary nodes to support high availability of applications like YARN Resource Manager, HDFS NameNode, Spark, Hive, and Ganglia. The primary node is no longer a potential single point of failure with this feature. If one of the primary nodes fails, Amazon EMR automatically fails over to a standby primary node and replaces the failed primary node with a new one with the same configuration and bootstrap actions. For more information, see [Plan and Configure Primary Nodes](../ManagementGuide/emr-plan-ha.md "../ManagementGuide/emr-plan-ha.md").

###### Known issues

- Tez UI (Fixed in Amazon EMR release 5.26.0)

Tez UI does not work on an EMR cluster with multiple primary nodes.

- Hue (Fixed in Amazon EMR release 5.24.0)
  - Hue running on Amazon EMR does not support Solr. Beginning with Amazon EMR release 5.20.0, a misconfiguration issue causes Solr to be enabled and a harmless error message to appear similar to the following:

  `Solr server could not be contacted properly: HTTPConnectionPool('host=ip-xx-xx-xx-xx.ec2.internal', port=1978): Max retries exceeded with url: /solr/admin/info/system?user.name=hue&doAs=administrator&wt=json (Caused by NewConnectionError(': Failed to establish a new connection: [Errno 111] Connection refused',))`

  **To prevent the Solr error message from appearing:**

      1. Connect to the primary node command line using SSH.
      2. Use a text editor to open the `hue.ini` file. For example:


      `sudo vim /etc/hue/conf/hue.ini`
      3. Search for the term `appblacklist` and modify the line to the following:



      ```
      appblacklist = search
      ```
      4. Save your changes and restart Hue as shown in the following example:



      ```
      sudo stop hue; sudo start hue
      ```

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.22.0

The following release notes include information for Amazon EMR release 5.22.0. Changes
are relative to 5.21.0.

###### Important

Beginning with Amazon EMR release 5.22.0, Amazon EMR uses AWS Signature Version 4 exclusively to authenticate requests to Amazon S3. Earlier Amazon EMR releases use AWS Signature Version 2 in some cases, unless the release notes indicate that Signature Version 4 is used exclusively. For more information, see [Authenticating Requests (AWS Signature Version 4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md") and [Authenticating Requests (AWS Signature Version 2)](../../../AmazonS3/latest/API/auth-request-sig-v2.md "../../../AmazonS3/latest/API/auth-request-sig-v2.md") in the _Amazon Simple Storage Service Developer Guide_.

Initial release date: March 20, 2019

###### Upgrades

- Flink 1.7.1
- HBase 1.4.9
- Oozie 5.1.0
- Phoenix 4.14.1
- Zeppelin 0.8.1
- Connectors and drivers:
  - DynamoDB Connector 4.8.0
  - MariaDB Connector 2.2.6
  - Amazon Redshift JDBC Driver 1.2.20.1043

###### New features

- Modified the default EBS configuration for EC2 instance types with EBS-only storage. When you create a cluster using Amazon EMR release 5.22.0 and later, the default amount of EBS storage increases based on the size of the instance. In addition, we split increased storage across multiple volumes, giving increased IOPS performance. If you want to use a different EBS instance storage configuration, you can specify it when you create an EMR cluster or add nodes to an existing cluster. For more information about the amount of storage and number of volumes allocated by default for each instance type, see [Default EBS Storage for Instances](../ManagementGuide/emr-plan-storage.md#emr-plan-storage-ebs-storage-default "../ManagementGuide/emr-plan-storage.md#emr-plan-storage-ebs-storage-default") in the _Amazon EMR Management Guide_.

###### Changes, enhancements, and resolved issues

- Spark
  - Introduced a new configuration property for Spark on YARN, `spark.yarn.executor.memoryOverheadFactor`. The value of this property is a scale factor that sets the value of memory overhead to a percentage of executor memory, with a minimum of 384 MB. If memory overhead is set explicitly using `spark.yarn.executor.memoryOverhead`, this property has no effect. The default value is `0.1875`, representing 18.75%. This default for Amazon EMR leaves more space in YARN containers for executor memory overhead than the 10% default set internally by Spark. The Amazon EMR default of 18.75% empirically showed fewer memory-related failures in TPC-DS benchmarks.
  - Backported [SPARK-26316](https://issues.apache.org/jira/browse/SPARK-26316 "https://issues.apache.org/jira/browse/SPARK-26316") to improve performance.

- In Amazon EMR version 5.19.0, 5.20.0, and 5.21.0, YARN node labels are stored in
  an HDFS directory. In some situations, this leads to core node startup delays and then
  causes cluster time-out and launch failure. Beginning with Amazon EMR 5.22.0, this issue
  is resolved. YARN node labels are stored on the local disk of each cluster node,
  avoiding dependencies on HDFS.

###### Known issues

- Hue (Fixed in Amazon EMR release 5.24.0)
  - Hue running on Amazon EMR does not support Solr. Beginning with Amazon EMR release 5.20.0, a misconfiguration issue causes Solr to be enabled and a harmless error message to appear similar to the following:

  `Solr server could not be contacted properly: HTTPConnectionPool('host=ip-xx-xx-xx-xx.ec2.internal', port=1978): Max retries exceeded with url: /solr/admin/info/system?user.name=hue&doAs=administrator&wt=json (Caused by NewConnectionError(': Failed to establish a new connection: [Errno 111] Connection refused',))`

  **To prevent the Solr error message from appearing:**

      1. Connect to the primary node command line using SSH.
      2. Use a text editor to open the `hue.ini` file. For example:


      `sudo vim /etc/hue/conf/hue.ini`
      3. Search for the term `appblacklist` and modify the line to the following:



      ```
      appblacklist = search
      ```
      4. Save your changes and restart Hue as shown in the following example:



      ```
      sudo stop hue; sudo start hue
      ```

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.21.1

The following release notes include information for Amazon EMR release 5.21.1. Changes
are relative to 5.21.0.

Initial release date: July 18, 2019

###### Changes, enhancements, and resolved issues

- Updated the default Amazon Linux AMI for Amazon EMR to include important Linux kernel security updates, including the TCP SACK Denial of Service Issue ([AWS-2019-005](https://aws.amazon.com/security/security-bulletins/AWS-2019-005/ "https://aws.amazon.com/security/security-bulletins/AWS-2019-005/")).

###### Known issues

- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.21.0

The following release notes include information for Amazon EMR release 5.21.0. Changes
are relative to 5.20.0.

Initial release date: February 18, 2019

Last updated date: April 3, 2019

###### Upgrades

- Flink 1.7.0
- Presto 0.215
- AWS SDK for Java 1.11.479

###### New features

- (April 3, 2019) With Amazon EMR version 5.21.0 and later, you can override cluster configurations and specify additional configuration classifications for each instance group in a running cluster. You do this by using the Amazon EMR console, the AWS Command Line Interface (AWS CLI), or the AWS SDK. For more information, see [Supplying a Configuration for an Instance Group in a Running Cluster](emr-configure-apps-running-cluster.md "emr-configure-apps-running-cluster.md").

###### Changes, enhancements, and resolved issues

- Zeppelin
  - Backported [ZEPPELIN-3878](https://issues.apache.org/jira/browse/ZEPPELIN-3878 "https://issues.apache.org/jira/browse/ZEPPELIN-3878").

###### Known issues

- Hue (Fixed in Amazon EMR release 5.24.0)
  - Hue running on Amazon EMR does not support Solr. Beginning with Amazon EMR release 5.20.0, a misconfiguration issue causes Solr to be enabled and a harmless error message to appear similar to the following:

  `Solr server could not be contacted properly: HTTPConnectionPool('host=ip-xx-xx-xx-xx.ec2.internal', port=1978): Max retries exceeded with url: /solr/admin/info/system?user.name=hue&doAs=administrator&wt=json (Caused by NewConnectionError(': Failed to establish a new connection: [Errno 111] Connection refused',))`

  **To prevent the Solr error message from appearing:**

      1. Connect to the primary node command line using SSH.
      2. Use a text editor to open the `hue.ini` file. For example:


      `sudo vim /etc/hue/conf/hue.ini`
      3. Search for the term `appblacklist` and modify the line to the following:



      ```
      appblacklist = search
      ```
      4. Save your changes and restart Hue as shown in the following example:



      ```
      sudo stop hue; sudo start hue
      ```

- Tez
  - This issue was fixed in Amazon EMR 5.22.0.

  When you connect to the Tez UI at http://`MasterDNS`:8080/tez-ui through an SSH connection to the cluster primary node, the error "Adapter operation failed - Timeline server (ATS) is out of reach. Either it is down, or CORS is not enabled" appears, or tasks unexpectedly show N/A.

  This is caused by the Tez UI making requests to the YARN Timeline Server using `localhost` rather than the host name of the primary node. As a workaround, a script is available to run as a bootstrap action or step. The script updates the host name in the Tez `configs.env` file. For more information and the location of the script, see the [Bootstrap Instructions](http://awssupportdatasvcs.com/bootstrap-actions/fix_tez_ui_0-9-1/ "http://awssupportdatasvcs.com/bootstrap-actions/fix_tez_ui_0-9-1/").

- In Amazon EMR version 5.19.0, 5.20.0, and 5.21.0, YARN node labels are stored in
  an HDFS directory. In some situations, this leads to core node startup delays and then
  causes cluster time-out and launch failure. Beginning with Amazon EMR 5.22.0, this issue
  is resolved. YARN node labels are stored on the local disk of each cluster node,
  avoiding dependencies on HDFS.
- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.20.0

The following release notes include information for Amazon EMR release 5.20.0. Changes
are relative to 5.19.0.

Initial release date: December 18, 2018

Last updated date: January 22, 2019

###### Upgrades

- Flink 1.6.2
- HBase 1.4.8
- Hive 2.3.4
- Hue 4.3.0
- MXNet 1.3.1
- Presto 0.214
- Spark 2.4.0
- TensorFlow 1.12.0
- Tez 0.9.1
- AWS SDK for Java 1.11.461

###### New features

- (January 22, 2019) Kerberos in Amazon EMR has been improved to support authenticating principals from an external KDC. This centralizes principal management because multiple clusters can share a single, external KDC. In addition, the external KDC can have a cross-realm trust with an Active Directory domain. This allows all clusters to authenticate principals from Active Directory. For more information, see [Use Kerberos Authentication](../ManagementGuide/emr-kerberos.md "../ManagementGuide/emr-kerberos.md") in the _Amazon EMR Management Guide_.

###### Changes, enhancements, and resolved issues

- Default Amazon Linux AMI for Amazon EMR
  - Python3 package was upgraded from python 3.4 to 3.6.

- The EMRFS S3-optimized committer
  - The EMRFS S3-optimized committer is now enabled by default, which improves write performance. For more information, see [Use the EMRFS S3-optimized
    committer](emr-spark-s3-optimized-committer.md "emr-spark-s3-optimized-committer.md").

- Hive
  - Backported [HIVE-16686](https://issues.apache.org/jira/browse/HIVE-16686 "https://issues.apache.org/jira/browse/HIVE-16686").

- Glue with Spark and Hive
  - In EMR 5.20.0 or later, parallel partition pruning is enabled automatically for Spark and Hive when AWS Glue Data Catalog is used as the metastore. This change significantly reduces query planning time by executing multiple requests in parallel to retrieve partitions. The total number of segments that can be executed concurrently range between 1 and 10. The default value is 5, which is a recommended setting. You can change it by specifying the property `aws.glue.partition.num.segments` in `hive-site` configuration classification. If throttling occurs, you can turn off the feature by changing the value to 1. For more information, see [AWS Glue Segment Structure](../../../glue/latest/dg/aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-Segment "../../../glue/latest/dg/aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-Segment").

###### Known issues

- Hue (Fixed in Amazon EMR release 5.24.0)
  - Hue running on Amazon EMR does not support Solr. Beginning with Amazon EMR release 5.20.0, a misconfiguration issue causes Solr to be enabled and a harmless error message to appear similar to the following:

  `Solr server could not be contacted properly: HTTPConnectionPool('host=ip-xx-xx-xx-xx.ec2.internal', port=1978): Max retries exceeded with url: /solr/admin/info/system?user.name=hue&doAs=administrator&wt=json (Caused by NewConnectionError(': Failed to establish a new connection: [Errno 111] Connection refused',))`

  **To prevent the Solr error message from appearing:**

      1. Connect to the primary node command line using SSH.
      2. Use a text editor to open the `hue.ini` file. For example:


      `sudo vim /etc/hue/conf/hue.ini`
      3. Search for the term `appblacklist` and modify the line to the following:



      ```
      appblacklist = search
      ```
      4. Save your changes and restart Hue as shown in the following example:



      ```
      sudo stop hue; sudo start hue
      ```

- Tez
  - This issue was fixed in Amazon EMR 5.22.0.

  When you connect to the Tez UI at http://`MasterDNS`:8080/tez-ui through an SSH connection to the cluster primary node, the error "Adapter operation failed - Timeline server (ATS) is out of reach. Either it is down, or CORS is not enabled" appears, or tasks unexpectedly show N/A.

  This is caused by the Tez UI making requests to the YARN Timeline Server using `localhost` rather than the host name of the primary node. As a workaround, a script is available to run as a bootstrap action or step. The script updates the host name in the Tez `configs.env` file. For more information and the location of the script, see the [Bootstrap Instructions](http://awssupportdatasvcs.com/bootstrap-actions/fix_tez_ui_0-9-1/ "http://awssupportdatasvcs.com/bootstrap-actions/fix_tez_ui_0-9-1/").

- In Amazon EMR version 5.19.0, 5.20.0, and 5.21.0, YARN node labels are stored in
  an HDFS directory. In some situations, this leads to core node startup delays and then
  causes cluster time-out and launch failure. Beginning with Amazon EMR 5.22.0, this issue
  is resolved. YARN node labels are stored on the local disk of each cluster node,
  avoiding dependencies on HDFS.
- Known issue in clusters with multiple primary nodes and Kerberos authentication

If you run clusters with multiple primary nodes and Kerberos authentication in Amazon EMR releases
5.20.0 and later, you may encounter problems with cluster operations such as
scale down or step submission, after the cluster has been running for some time.
The time period depends on the Kerberos ticket validity period that you defined.
The scale-down problem impacts both automatic scale-down and explicit scale down
requests that you submitted. Additional cluster operations can also be impacted.

Workaround:

    + SSH as `hadoop` user to the lead primary node of the EMR cluster with multiple primary nodes.
    + Run the following command to renew Kerberos ticket for `hadoop` user.



    ```
    kinit -kt <keytab_file> <principal>
    ```

    Typically, the keytab file is located at `/etc/hadoop.keytab` and the
     principal is in the form of
     `hadoop/<hostname>@<REALM>`.

###### Note

This workaround will be effective for the time period the Kerberos ticket is valid. This
duration is 10 hours by default, but can configured by your Kerberos
settings. You must re-run the above command once the Kerberos ticket
expires.

## Release 5.19.0

The following release notes include information for Amazon EMR release 5.19.0. Changes
are relative to 5.18.0.

Initial release date: November 7, 2018

Last updated date: November 19, 2018

###### Upgrades

- Hadoop 2.8.5
- Flink 1.6.1
- JupyterHub 0.9.4
- MXNet 1.3.0
- Presto 0.212
- TensorFlow 1.11.0
- Zookeeper 3.4.13
- AWS SDK for Java 1.11.433

###### New features

- (Nov. 19, 2018) EMR Notebooks is a managed environment based on Jupyter Notebook. It supports Spark magic kernels for PySpark, Spark SQL, Spark R, and Scala. EMR Notebooks can be used with clusters created using Amazon EMR release 5.18.0 and later. For more information, see [Using EMR Notebooks](../ManagementGuide/emr-managed-notebooks.md "../ManagementGuide/emr-managed-notebooks.md") in the _Amazon EMR Management Guide_.
- The EMRFS S3-optimized committer is available when writing Parquet files using Spark and EMRFS. This committer improves write performance. For more information, see [Use the EMRFS S3-optimized
  committer](emr-spark-s3-optimized-committer.md "emr-spark-s3-optimized-committer.md").

###### Changes, enhancements, and resolved issues

- YARN
  - Modified the logic that limits the application master process to running on core nodes. This functionality now uses the YARN node labels feature and properties in the `yarn-site` and `capacity-scheduler` configuration classifications. For information, see [https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-instances-guidelines.html#emr-plan-spot-YARN.](../ManagementGuide/emr-plan-instances-guidelines.md#emr-plan-spot-YARN. "../ManagementGuide/emr-plan-instances-guidelines.md#emr-plan-spot-YARN.")

- Default Amazon Linux AMI for Amazon EMR
  - `ruby18`, `php56`, and `gcc48` are no longer installed by default. These can be installed if desired using `yum`.
  - The aws-sdk ruby gem is no longer installed by default. It can be installed using `gem install aws-sdk`, if desired. Specific components can also be installed. For example, `gem install aws-sdk-s3`.

###### Known issues

- **EMR Notebooks**—In some circumstances, with multiple notebook editors open, the notebook editor may appear unable to connect to the cluster. If this happens, clear browser cookies and then reopen notebook editors.
- **CloudWatch ContainerPending Metric and Automatic Scaling**—(Fixed in 5.20.0)Amazon EMR may emit a negative value for `ContainerPending`. If `ContainerPending` is used in an automatic scaling rule, automatic scaling does not behave as expected. Avoid using `ContainerPending` with automatic scaling.
- In Amazon EMR version 5.19.0, 5.20.0, and 5.21.0, YARN node labels are stored in
  an HDFS directory. In some situations, this leads to core node startup delays and then
  causes cluster time-out and launch failure. Beginning with Amazon EMR 5.22.0, this issue
  is resolved. YARN node labels are stored on the local disk of each cluster node,
  avoiding dependencies on HDFS.

## Release 5.18.0

The following release notes include information for Amazon EMR release 5.18.0. Changes
are relative to 5.17.0.

Initial release date: October 24, 2018

###### Upgrades

- Flink 1.6.0
- HBase 1.4.7
- Presto 0.210
- Spark 2.3.2
- Zeppelin 0.8.0

###### New features

- Beginning with Amazon EMR 5.18.0, you can use the Amazon EMR artifact repository to build your job code against the exact versions of libraries and dependencies that are available with specific Amazon EMR releases. For more information, see [Checking dependencies using the Amazon EMR artifact repository](emr-artifact-repository.md "emr-artifact-repository.md").

###### Changes, enhancements, and resolved issues

- Hive
  - Added support for S3 Select. For more information, see [Using S3 Select with Hive to improve
    performance](emr-hive-s3select.md "emr-hive-s3select.md").

- Presto
  - Added support for [S3 Select](https://aws.amazon.com/blogs/aws/s3-glacier-select/ "https://aws.amazon.com/blogs/aws/s3-glacier-select/") Pushdown. For more information, see [Using S3 Select Pushdown with Presto to improve
    performance](emr-presto-s3select.md "emr-presto-s3select.md").

- Spark
  - The default log4j configuration for Spark has been changed to roll container logs hourly for Spark streaming jobs. This helps prevent the deletion of logs for long-running Spark streaming jobs.

## Release 5.17.1

The following release notes include information for Amazon EMR release 5.17.1. Changes
are relative to 5.17.0.

Initial release date: July 18, 2019

###### Changes, enhancements, and resolved issues

- Updated the default Amazon Linux AMI for Amazon EMR to include important Linux kernel security updates, including the TCP SACK Denial of Service Issue ([AWS-2019-005](https://aws.amazon.com/security/security-bulletins/AWS-2019-005/ "https://aws.amazon.com/security/security-bulletins/AWS-2019-005/")).

## Release 5.17.0

The following release notes include information for Amazon EMR release 5.17.0. Changes
are relative to 5.16.0.

Initial release date: August 30, 2018

###### Upgrades

- Flink 1.5.2
- HBase 1.4.6
- Presto 0.206

###### New features

- Added support for Tensorflow. For more information, see [TensorFlow](emr-tensorflow.md "emr-tensorflow.md").

###### Changes, enhancements, and resolved issues

- JupyterHub
  - Added support for notebook persistence in Amazon S3. For more information, see [Configuring persistence for notebooks in Amazon S3](emr-jupyterhub-s3.md "emr-jupyterhub-s3.md").

- Spark
  - Added support for [S3 Select](https://aws.amazon.com/blogs/aws/s3-glacier-select/ "https://aws.amazon.com/blogs/aws/s3-glacier-select/"). For more information, see [Use S3 Select with Spark to improve query
    performance](emr-spark-s3select.md "emr-spark-s3select.md").

- Resolved the issues with the Cloudwatch metrics and the automatic scaling feature in Amazon EMR version 5.14.0, 5.15.0, or 5.16.0.

###### Known issues

- When you create a kerberized cluster with Livy installed, Livy fails with an error that simple authentication is not enabled. Rebooting the Livy server resolves the issue. As a workaround, add a step during cluster creation that runs `sudo restart livy-server` on the primary node.
- If you use a custom Amazon Linux AMI based on an Amazon Linux AMI with a creation date of 2018-08-11, the Oozie server fails to start. If you use Oozie, create a custom AMI based on an Amazon Linux AMI ID with a different creation date. You can use the following AWS CLI command to return a list of Image IDs for all HVM Amazon Linux AMIs with a 2018.03 version, along with the release date, so that you can choose an appropriate Amazon Linux AMI as your base. Replace MyRegion with your Region identifier, such as us-west-2.

```
aws ec2 --region `MyRegion` describe-images --owner amazon --query 'Images[?Name!=`null`]|[?starts_with(Name, `amzn-ami-hvm-2018.03`) == `true`].[CreationDate,ImageId,Name]' --output text | sort -rk1

```

## Release 5.16.0

The following release notes include information for Amazon EMR release 5.16.0. Changes
are relative to 5.15.0.

Initial release date: July 19, 2018

###### Upgrades

- Hadoop 2.8.4
- Flink 1.5.0
- Livy 0.5.0
- MXNet 1.2.0
- Phoenix 4.14.0
- Presto 0.203
- Spark 2.3.1
- AWS SDK for Java 1.11.336
- CUDA 9.2
- Redshift JDBC Driver 1.2.15.1025

###### Changes, enhancements, and resolved issues

- HBase
  - Backported [HBASE-20723](https://issues.apache.org/jira/browse/HBASE-20723 "https://issues.apache.org/jira/browse/HBASE-20723")

- Presto
  - Configuration changes to support LDAP authentication. For more information, see [Using LDAP authentication for Presto on
    Amazon EMR](emr-presto-ldap.md "emr-presto-ldap.md").

- Spark
  - Apache Spark version 2.3.1, available beginning with Amazon EMR release 5.16.0, addresses [CVE-2018-8024](https://nvd.nist.gov/vuln/detail/CVE-2018-8024 "https://nvd.nist.gov/vuln/detail/CVE-2018-8024") and [CVE-2018-1334](https://nvd.nist.gov/vuln/detail/CVE-2018-1334 "https://nvd.nist.gov/vuln/detail/CVE-2018-1334"). We recommend that you migrate earlier versions of Spark to Spark version 2.3.1 or later.

###### Known issues

- This release version does not support the c1.medium or m1.small instance types. Clusters using either of these instance types fail to start. As a workaround, specify a different instance type or use a different release version.
- When you create a kerberized cluster with Livy installed, Livy fails with an error that simple authentication is not enabled. Rebooting the Livy server resolves the issue. As a workaround, add a step during cluster creation that runs `sudo restart livy-server` on the primary node.
- After the primary node reboots or the instance controller restarts, the CloudWatch metrics will not be collected and the automatic scaling feature will not be available in Amazon EMR version 5.14.0, 5.15.0, or 5.16.0. This issue is fixed in Amazon EMR 5.17.0.

## Release 5.15.0

The following release notes include information for Amazon EMR release 5.15.0. Changes
are relative to 5.14.0.

Initial release date: June 21, 2018

###### Upgrades

- Upgraded HBase to 1.4.4
- Upgraded Hive to 2.3.3
- Upgraded Hue to 4.2.0
- Upgraded Oozie to 5.0.0
- Upgraded Zookeeper to 3.4.12
- Upgraded AWS SDK to 1.11.333

###### Changes, enhancements, and resolved issues

- Hive
  - Backported [HIVE-18069](https://issues.apache.org/jira/browse/HIVE-18069 "https://issues.apache.org/jira/browse/HIVE-18069")

- Hue
  - Updated Hue to correctly authenticate with Livy when Kerberos is enabled. Livy is now supported when using Kerberos with Amazon EMR.

- JupyterHub
  - Updated JupyterHub so that Amazon EMR installs LDAP client libraries by default.
  - Fixed an error in the script that generates self-signed certificates.

###### Known issues

- This release version does not support the c1.medium or m1.small instance types. Clusters using either of these instance types fail to start. As a workaround, specify a different instance type or use a different release version.
- After the primary node reboots or the instance controller restarts, the CloudWatch metrics will not be collected and the automatic scaling feature will not be available in Amazon EMR version 5.14.0, 5.15.0, or 5.16.0. This issue is fixed in Amazon EMR 5.17.0.

## Release 5.14.1

The following release notes include information for Amazon EMR release 5.14.1. Changes
are relative to 5.14.0.

Initial release date: October 17, 2018

Updated the default AMI for Amazon EMR to address potential security vulnerabilities.

## Release 5.14.0

The following release notes include information for Amazon EMR release 5.14.0. Changes
are relative to 5.13.0.

Initial release date:
June 4, 2018

###### Upgrades

- Upgraded Apache Flink to 1.4.2
- Upgraded Apache MXnet to 1.1.0
- Upgraded Apache Sqoop to 1.4.7

###### New features

- Added JupyterHub support. For more information, see [JupyterHub](emr-jupyterhub.md "emr-jupyterhub.md").

###### Changes, enhancements, and resolved issues

- EMRFS
  - The userAgent string in requests to Amazon S3 has been updated to contain the user and group
    information of the invoking principal. This can be
    used with AWS CloudTrail logs for more comprehensive
    request tracking.

- HBase
  - Included [HBASE-20447](https://issues.apache.org/jira/browse/HBASE-20447 "https://issues.apache.org/jira/browse/HBASE-20447"), which addresses an issue that could cause cache issues, especially with split Regions.

- MXnet
  - Added OpenCV libraries.

- Spark
  - When Spark writes Parquet files to an Amazon S3 location
    using EMRFS, the FileOutputCommitter algorithm has
    been updated to use version 2 instead of version 1.
    This reduces the number of renames, which improves
    application performance. This change does not
    affect:
    - Applications other than Spark.
    - Applications that write to other file
      systems, such as HDFS (which still use version 1
      of FileOutputCommitter).
    - Applications that use other output formats,
      such as text or csv, that already use EMRFS direct
      write.

###### Known issues

- JupyterHub
  - Using configuration classifications to set up JupyterHub and
    individual Jupyter notebooks when you create a cluster is not
    supported. Edit the jupyterhub_config.py file and
    jupyter_notebook_config.py files for each user manually. For more
    information, see [Configuring JupyterHub](emr-jupyterhub-configure.md "emr-jupyterhub-configure.md").
  - JupyterHub fails to start on clusters within a private subnet, failing with the message `Error: ENOENT: no such file or directory, open '/etc/jupyter/conf/server.crt'` . This is caused by an error in the script that generates self-signed certificates. Use the following workaround to generate self-signed certificates. All commands are executed while connected to the primary node.

        1. Copy the certificate generation script from the container to the primary node:



        ```
        sudo docker cp jupyterhub:/tmp/gen_self_signed_cert.sh ./
        ```
        2. Use a text editor to change line 23 to change public hostname to local hostname as shown below:



        ```
        `local` hostname=$(curl -s $EC2_METADATA_SERVICE_URI/`local`-hostname)
        ```
        3. Run the script to generate self-signed certificates:



        ```
        sudo bash ./gen_self_signed_cert.sh
        ```
        4. Move the certificate files that the script generates to the `/etc/jupyter/conf/` directory:



        ```
        sudo mv /tmp/server.crt /tmp/server.key /etc/jupyter/conf/
        ```

    You can `tail` the `jupyter.log` file to verify that JupyterHub restarted and is returning a 200 response code. For example:

  ```
  tail -f /var/log/jupyter/jupyter.log
  ```

  This should return a response similar to the following:

  ```
  # [I 2018-06-14 18:56:51.356 JupyterHub app:1581] JupyterHub is now running at https://:9443/
  # 19:01:51.359 - info: [ConfigProxy] 200 GET /api/routes

  ```

- After the primary node reboots or the instance controller restarts, the CloudWatch metrics will not be collected and the automatic scaling feature will not be available in Amazon EMR version 5.14.0, 5.15.0, or 5.16.0. This issue is fixed in Amazon EMR 5.17.0.

## Release 5.13.0

The following release notes include information for the Amazon EMR release 5.13.0. Changes
are relative to 5.12.0.

###### Upgrades

- Upgraded Spark to 2.3.0
- Upgraded HBase to 1.4.2
- Upgraded Presto to 0.194
- Upgraded AWS SDK for Java to 1.11.297

###### Changes, enhancements, and resolved issues

- Hive
  - Backported [HIVE-15436](https://issues.apache.org/jira/browse/HIVE-15436 "https://issues.apache.org/jira/browse/HIVE-15436"). Enhanced Hive APIs to return only views.

###### Known issues

- MXNet does not currently have OpenCV libraries.

## Release 5.12.2

The following release notes include information for Amazon EMR release 5.12.2. Changes
are relative to 5.12.1.

Initial release date: August 29, 2018

###### Changes, enhancements, and resolved issues

- This release addresses a potential security vulnerability.

## Release 5.12.1

The following release notes include information for Amazon EMR release 5.12.1. Changes
are relative to 5.12.0.

Initial release date: March 29, 2018

###### Changes, enhancements, and resolved issues

- Updated the Amazon Linux kernel of the defaultAmazon Linux AMI for Amazon EMR to address potential vulnerabilities.

## Release 5.12.0

The following release notes include information for the Amazon EMR release 5.12.0. Changes
are relative to 5.11.1.

###### Upgrades

- AWS SDK for Java 1.11.238 ⇒ 1.11.267. For more information, see the [AWS SDK for Java Change Log](https://github.com/aws/aws-sdk-java/blob/master/CHANGELOG.md "https://github.com/aws/aws-sdk-java/blob/master/CHANGELOG.md") on GitHub.
- Hadoop 2.7.3 ⇒ 2.8.3. For more information, see [Apache Hadoop Releases](http://hadoop.apache.org/releases.html "http://hadoop.apache.org/releases.html").
- Flink 1.3.2 ⇒ 1.4.0. For more information, see the [Apache Flink 1.4.0 Release Announcement](https://flink.apache.org/news/2017/12/12/release-1.4.0.html "https://flink.apache.org/news/2017/12/12/release-1.4.0.html").
- HBase 1.3.1 ⇒ 1.4.0. For more information, see the [HBase Release Announcement](http://mail-archives.apache.org/mod_mbox/www-announce/201712.mbox/%3CCA+RK=_AU+tB=7SU1HRbeKVEd-sKA5WcJo3oa43vQ6PMB3L9pgQ@mail.gmail.com%3E "http://mail-archives.apache.org/mod_mbox/www-announce/201712.mbox/%3CCA+RK=_AU+tB=7SU1HRbeKVEd-sKA5WcJo3oa43vQ6PMB3L9pgQ@mail.gmail.com%3E").
- Hue 4.0.1 ⇒ 4.1.0. For more information, see the [Release Notes](https://docs.gethue.com/releases/release-notes-4.10.0/ "https://docs.gethue.com/releases/release-notes-4.10.0/").
- MxNet 0.12.0 ⇒ 1.0.0. For more information, see the [MXNet Change Log](https://github.com/apache/incubator-mxnet/releases/tag/1.0.0 "https://github.com/apache/incubator-mxnet/releases/tag/1.0.0") on GitHub.
- Presto 0.187 ⇒ 0.188. For more information, see the [Release Notes](https://prestodb.io/docs/current/release/release-0.188.html "https://prestodb.io/docs/current/release/release-0.188.html").

###### Changes, enhancements, and resolved issues

- **Hadoop**
  - The `yarn.resourcemanager.decommissioning.timeout` property has changed to
    `yarn.resourcemanager.nodemanager-graceful-decommission-timeout-secs`. You can use this property to customize cluster scale-down. For more information, see [Cluster Scale-Down](../ManagementGuide/emr-scaledown-behavior.md "../ManagementGuide/emr-scaledown-behavior.md") in the _Amazon EMR Management Guide_.
  - The Hadoop CLI added the `-d` option to the `cp` (copy) command, which specifies direct copy. You can use this to avoid creating an intermediary `.COPYING` file, which makes copying data between Amazon S3 faster. For more information, see [HADOOP-12384](https://issues.apache.org/jira/browse/HADOOP-12384 "https://issues.apache.org/jira/browse/HADOOP-12384").

- **Pig**
  - Added the `pig-env` configuration classification, which simplifies the configuration of Pig environment properties. For more information, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

- **Presto**
  - Added the `presto-connector-redshift` configuration classification, which you can use to configure values in the Presto `redshift.properties` configuration file. For more information, see [Redshift Connector](https://prestodb.io/docs/current/connector/redshift.html "https://prestodb.io/docs/current/connector/redshift.html") in Presto documentation, and [Configure applications](emr-configure-apps.md "emr-configure-apps.md").
  - Presto support for EMRFS has been added and is the default configuration. Earlier Amazon EMR releases used PrestoS3FileSystem, which was the only option. For more information, see [EMRFS and PrestoS3FileSystem
    configuration](emr-presto-considerations.md#emr-presto-prestos3 "emr-presto-considerations.md#emr-presto-prestos3").

  ###### Note

  If you query underlying data in Amazon S3 with Amazon EMR version 5.12.0, Presto errors
  can occur. This is because Presto fails to pick up configuration classification
  values from `emrfs-site.xml`. As a workaround, create an
  `emrfs` subdirectory under
  `usr/lib/presto/plugin/hive-hadoop2/` and create a symlink in
  `usr/lib/presto/plugin/hive-hadoop2/emrfs` to the existing
  `/usr/share/aws/emr/emrfs/conf/emrfs-site.xml` file. Then restart
  the presto-server process (`sudo presto-server stop` followed by
  `sudo presto-server start`).

- **Spark**
  - Backported [SPARK-22036: BigDecimal multiplication sometimes returns null](https://issues.apache.org/jira/browse/SPARK-22036 "https://issues.apache.org/jira/browse/SPARK-22036").

###### Known issues

- MXNet does not include OpenCV libraries.
- SparkR is not available for clusters created using a custom AMI because R is not installed by default on cluster nodes.

## Release 5.11.3

The following release notes include information for Amazon EMR release 5.11.3. Changes
are relative to 5.11.2.

Initial release date: July 18, 2019

###### Changes, enhancements, and resolved issues

- Updated the default Amazon Linux AMI for Amazon EMR to include important Linux kernel security updates, including the TCP SACK Denial of Service Issue ([AWS-2019-005](https://aws.amazon.com/security/security-bulletins/AWS-2019-005/ "https://aws.amazon.com/security/security-bulletins/AWS-2019-005/")).

## Release 5.11.2

The following release notes include information for Amazon EMR release 5.11.2. Changes
are relative to 5.11.1.

Initial release date: August 29, 2018

###### Changes, enhancements, and resolved issues

- This release addresses a potential security vulnerability.

## Release 5.11.1

The following release notes include information for the Amazon EMR version 5.11.1
release. Changes are relative to the Amazon EMR 5.11.0 release.

Initial release date: January 22, 2018

### Changes, enhancements, and resolved

issues

- Updated the Amazon Linux kernel of the defaultAmazon Linux AMI for Amazon EMR to address vulnerabilities associated with speculative execution (CVE-2017-5715, CVE-2017-5753, and CVE-2017-5754). For more information, see [https://aws.amazon.com/security/security-bulletins/AWS-2018-013/](https://aws.amazon.com/security/security-bulletins/AWS-2018-013/ "https://aws.amazon.com/security/security-bulletins/AWS-2018-013/").

### Known issues

- MXNet does not include OpenCV libraries.
- Hive 2.3.2 sets `hive.compute.query.using.stats=true` by
  default. This causes queries to get data from existing statistics rather
  than directly from data, which could be confusing. For example, if you
  have a table with `hive.compute.query.using.stats=true` and
  upload new files to the table `LOCATION`, running a
  `SELECT COUNT(*)` query on the table returns the count
  from the statistics, rather than picking up the added rows.

As a workaround, use the `ANALYZE TABLE` command to gather
new statistics, or set
`hive.compute.query.using.stats=false`. For more information,
see [Statistics in Hive](https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ExistingTables%E2%80%93ANALYZE "https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ExistingTables%E2%80%93ANALYZE") in the Apache Hive documentation.

## Release 5.11.0

The following release notes include information for the Amazon EMR version 5.11.0
release. Changes are relative to the Amazon EMR 5.10.0 release.

### Upgrades

The following applications and components have been upgraded in this release
to include the following versions.

- Hive 2.3.2
- Spark 2.2.1
- SDK for Java 1.11.238

### New features

- **Spark**
  - Added `spark.decommissioning.timeout.threshold`
    setting, which improves Spark decommissioning behavior when
    using Spot instances. For more information, see [Configuring node decommissioning
    behavior](emr-spark-configure.md#spark-decommissioning "emr-spark-configure.md#spark-decommissioning").
  - Added the `aws-sagemaker-spark-sdk` component to
    Spark, which installs Amazon SageMaker Spark and associated
    dependencies for Spark integration with [Amazon SageMaker](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/").
    You can use Amazon SageMaker Spark to construct Spark machine
    learning (ML) pipelines using Amazon SageMaker stages. For more
    information, see the [SageMaker Spark readme](https://github.com/aws/sagemaker-spark/blob/master/README.md "https://github.com/aws/sagemaker-spark/blob/master/README.md") on GitHub and [Using Apache Spark with Amazon SageMaker](../../../sagemaker/latest/dg/apache-spark.md "../../../sagemaker/latest/dg/apache-spark.md") in the
    _Amazon SageMaker Developer
    Guide_.

### Known issues

- MXNet does not include OpenCV libraries.
- Hive 2.3.2 sets `hive.compute.query.using.stats=true` by
  default. This causes queries to get data from existing statistics rather
  than directly from data, which could be confusing. For example, if you
  have a table with `hive.compute.query.using.stats=true` and
  upload new files to the table `LOCATION`, running a
  `SELECT COUNT(*)` query on the table returns the count
  from the statistics, rather than picking up the added rows.

As a workaround, use the `ANALYZE TABLE` command to gather
new statistics, or set
`hive.compute.query.using.stats=false`. For more information,
see [Statistics in Hive](https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ExistingTables%E2%80%93ANALYZE "https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ExistingTables%E2%80%93ANALYZE") in the Apache Hive documentation.

## Release 5.10.0

The following release notes include information for the Amazon EMR version 5.10.0
release. Changes are relative to the Amazon EMR 5.9.0 release.

### Upgrades

The following applications and components have been upgraded in this release
to include the following versions.

- AWS SDK for Java 1.11.221
- Hive 2.3.1
- Presto 0.187

### New features

- Added support for Kerberos authentication. For more information, see
  [Use Kerberos
  authentication](../ManagementGuide/emr-kerberos.md "../ManagementGuide/emr-kerberos.md") in the
  _Amazon EMR Management Guide_
- Added support for IAM roles for EMRFS requests to Amazon S3. For more
  information, see [Configure IAM roles for EMRFS requests to Amazon S3](../ManagementGuide/emr-emrfs-iam-roles.md "../ManagementGuide/emr-emrfs-iam-roles.md") in the
  _Amazon EMR Management Guide_.
- Added support for GPU-based P2 and P3 instance types. For more
  information, see [Amazon EC2 P2 instances](https://aws.amazon.com/ec2/instance-types/p2/ "https://aws.amazon.com/ec2/instance-types/p2/") and [Amazon EC2 P3
  instances](https://aws.amazon.com/ec2/instance-types/p3/ "https://aws.amazon.com/ec2/instance-types/p3/"). NVIDIA driver 384.81 and CUDA driver 9.0.176 are
  installed on these instance types by default.
- Added support for [Apache MXNet](emr-mxnet.md "emr-mxnet.md").

### Changes, enhancements, and resolved

issues

- Presto
  - Added support for using the AWS Glue Data Catalog as the default Hive
    metastore. For more information, see [Using
    Presto with the AWS Glue Data Catalog](emr-presto.md#emr-presto-glue "emr-presto.md#emr-presto-glue").
  - Added support for [geospatial functions](https://prestodb.io/docs/current/functions/geospatial.html "https://prestodb.io/docs/current/functions/geospatial.html").
  - Added [spill to disk](https://prestodb.io/docs/current/admin/spill.html "https://prestodb.io/docs/current/admin/spill.html") support for joins.
  - Added support for the [Redshift connector](https://prestodb.io/docs/current/connector/redshift.html "https://prestodb.io/docs/current/connector/redshift.html").

- Spark
  - Backported [SPARK-20640](https://issues.apache.org/jira/browse/SPARK-20640 "https://issues.apache.org/jira/browse/SPARK-20640"), which makes the rpc timeout and the
    retries for shuffle registration values configurable using
    `spark.shuffle.registration.timeout` and
    `spark.shuffle.registration.maxAttempts`
    properties.
  - Backported [SPARK-21549](https://issues.apache.org/jira/browse/SPARK-21549 "https://issues.apache.org/jira/browse/SPARK-21549"), which corrects an error that occurs
    when writing custom OutputFormat to non-HDFS locations.

- Backported [Hadoop-13270](https://issues.apache.org/jira/browse/HADOOP-13270 "https://issues.apache.org/jira/browse/HADOOP-13270")
- The Numpy, Scipy, and Matplotlib libraries have been removed from the
  base Amazon EMR AMI. If these libraries are required for your application,
  they are available in the application repository, so you can use a
  bootstrap action to install them on all nodes using `yum
install`.
- The Amazon EMR base AMI no longer has application RPM packages included, so
  the RPM packages are no longer present on cluster nodes. Custom AMIs and
  the Amazon EMR base AMI now reference the RPM package repository in
  Amazon S3.
- Because of the introduction of per-second billing in Amazon EC2, the
  default **Scale down behavior** is now
  **Terminate at task completion** rather than
  **Terminate at instance hour**. For more
  information, see [Configure cluster scale-down](../ManagementGuide/emr-scaledown-behavior.md "../ManagementGuide/emr-scaledown-behavior.md").

### Known issues

- MXNet does not include OpenCV libraries.
- Hive 2.3.1 sets `hive.compute.query.using.stats=true` by
  default. This causes queries to get data from existing statistics rather
  than directly from data, which could be confusing. For example, if you
  have a table with `hive.compute.query.using.stats=true` and
  upload new files to the table `LOCATION`, running a
  `SELECT COUNT(*)` query on the table returns the count
  from the statistics, rather than picking up the added rows.

As a workaround, use the `ANALYZE TABLE` command to gather
new statistics, or set
`hive.compute.query.using.stats=false`. For more information,
see [Statistics in Hive](https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ExistingTables%E2%80%93ANALYZE "https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ExistingTables%E2%80%93ANALYZE") in the Apache Hive documentation.

## Release 5.9.0

The following release notes include information for the Amazon EMR version 5.9.0
release. Changes are relative to the Amazon EMR 5.8.0 release.

Release date: October 5, 2017

Latest feature update: October 12, 2017

### Upgrades

The following applications and components have been upgraded in this release
to include the following versions.

- AWS SDK for Java version 1.11.183
- Flink 1.3.2
- Hue 4.0.1
- Pig 0.17.0
- Presto 0.184

### New features

- Added Livy support (version 0.4.0-incubating). For more information,
  see [Apache Livy](emr-livy.md "emr-livy.md").
- Added support for Hue Notebook for Spark.
- Added support for i3-series Amazon EC2 instances (October 12, 2017).

### Changes, enhancements, and resolved

issues

- Spark
  - Added a new set of features that help ensure Spark handles
    node termination because of a manual resize or an automatic
    scaling policy request more gracefully. For more information,
    see [Configuring node decommissioning
    behavior](emr-spark-configure.md#spark-decommissioning "emr-spark-configure.md#spark-decommissioning").
  - SSL is used instead of 3DES for in-transit encryption for the
    block transfer service, which enhances performance when using
    Amazon EC2 instance types with AES-NI.
  - Backported [SPARK-21494](https://issues.apache.org/jira/browse/SPARK-21494 "https://issues.apache.org/jira/browse/SPARK-21494").

- Zeppelin
  - Backported [ZEPPELIN-2377](https://issues.apache.org/jira/browse/ZEPPELIN-2377 "https://issues.apache.org/jira/browse/ZEPPELIN-2377").

- HBase
  - Added patch [HBASE-18533](https://issues.apache.org/jira/browse/HBASE-18533 "https://issues.apache.org/jira/browse/HBASE-18533"), which allows additional values for
    HBase BucketCache configuration using the
    `hbase-site` configuration classification.

- Hue
  - Added AWS Glue Data Catalog support for the Hive query editor in
    Hue.
  - By default, superusers in Hue can access all files that Amazon EMR
    IAM roles are allowed to access. Newly created users do not
    automatically have permissions to access the Amazon S3 filebrowser
    and must have the `filebrowser.s3_access` permissions
    enabled for their group.

- Resolved an issue that caused underlying JSON data created using
  AWS Glue Data Catalog to be inaccessible.

### Known issues

- Cluster launch fails when all applications are installed and the
  default Amazon EBS root volume size is not changed. As a workaround, use the
  `aws emr create-cluster` command from the AWS CLI and
  specify a larger `--ebs-root-volume-size` parameter.
- Hive 2.3.0 sets `hive.compute.query.using.stats=true` by
  default. This causes queries to get data from existing statistics rather
  than directly from data, which could be confusing. For example, if you
  have a table with `hive.compute.query.using.stats=true` and
  upload new files to the table `LOCATION`, running a
  `SELECT COUNT(*)` query on the table returns the count
  from the statistics, rather than picking up the added rows.

As a workaround, use the `ANALYZE TABLE` command to gather
new statistics, or set
`hive.compute.query.using.stats=false`. For more information,
see [Statistics in Hive](https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ExistingTables%E2%80%93ANALYZE "https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ExistingTables%E2%80%93ANALYZE") in the Apache Hive documentation.

## Release 5.8.2

The following release notes include information for Amazon EMR release 5.8.2. Changes
are relative to 5.8.1.

Initial release date: March 29, 2018

###### Changes, enhancements, and resolved issues

- Updated the Amazon Linux kernel of the defaultAmazon Linux AMI for Amazon EMR to address potential vulnerabilities.

## Release 5.8.1

The following release notes include information for the Amazon EMR version 5.8.1
release. Changes are relative to the Amazon EMR 5.8.0 release.

Initial release date: January 22, 2018

### Changes, enhancements, and resolved

issues

- Updated the Amazon Linux kernel of the defaultAmazon Linux AMI for Amazon EMR to address vulnerabilities associated with speculative execution (CVE-2017-5715, CVE-2017-5753, and CVE-2017-5754). For more information, see [https://aws.amazon.com/security/security-bulletins/AWS-2018-013/](https://aws.amazon.com/security/security-bulletins/AWS-2018-013/ "https://aws.amazon.com/security/security-bulletins/AWS-2018-013/").

## Release 5.8.0

The following release notes include information for the Amazon EMR version 5.8.0
release. Changes are relative to the Amazon EMR 5.7.0 release.

Initial release date: August 10, 2017

Latest feature update: September 25, 2017

### Upgrades

The following applications and components have been upgraded in this release
to include the following versions:

- AWS SDK 1.11.160
- Flink 1.3.1
- Hive 2.3.0. For more information, see [Release notes](https://issues.apache.org/jira/secure/ConfigureReleaseNote.jspa?projectId=12310843&version=12340269 "https://issues.apache.org/jira/secure/ConfigureReleaseNote.jspa?projectId=12310843&version=12340269") on the Apache Hive site.
- Spark 2.2.0. For more information, see [Release notes](https://spark.apache.org/releases/spark-release-2-2-0.html "https://spark.apache.org/releases/spark-release-2-2-0.html") on the Apache Spark site.

### New features

- Added support for viewing application history (September 25, 2017).
  For more information, see [Viewing
  application history](../ManagementGuide/emr-cluster-application-history.md "../ManagementGuide/emr-cluster-application-history.md") in the
  _Amazon EMR Management Guide_.

### Changes, enhancements, and resolved

issues

- **Integration with AWS Glue Data Catalog**
  - Added ability for Hive and Spark SQL to use AWS Glue Data Catalog as the
    Hive metadata store. For more information, see [Using the AWS Glue Data Catalog as the metastore for
    Hive](emr-hive-metastore-glue.md "emr-hive-metastore-glue.md") and [Use AWS Glue Data Catalog catalog with Spark on Amazon EMR](emr-spark-glue.md "emr-spark-glue.md").

- Added **Application history** to cluster details,
  which allows you to view historical data for YARN applications and
  additional details for Spark applications. For more information, see
  [View
  application history](../ManagementGuide/emr-cluster-application-history.md "../ManagementGuide/emr-cluster-application-history.md") in the
  _Amazon EMR Management Guide_.
- **Oozie**
  - Backported [OOZIE-2748](https://issues.apache.org/jira/browse/OOZIE-2748 "https://issues.apache.org/jira/browse/OOZIE-2748").

- **Hue**
  - Backported [HUE-5859](https://issues.cloudera.org/browse/HUE-5859 "https://issues.cloudera.org/browse/HUE-5859")

- **HBase**
  - Added patch to expose the HBase master server start time
    through Java Management Extensions (JMX) using
    `getMasterInitializedTime`.
  - Added patch that improves cluster start time.

### Known issues

- Cluster launch fails when all applications are installed and the
  default Amazon EBS root volume size is not changed. As a workaround, use the
  `aws emr create-cluster` command from the AWS CLI and
  specify a larger `--ebs-root-volume-size` parameter.
- Hive 2.3.0 sets `hive.compute.query.using.stats=true` by
  default. This causes queries to get data from existing statistics rather
  than directly from data, which could be confusing. For example, if you
  have a table with `hive.compute.query.using.stats=true` and
  upload new files to the table `LOCATION`, running a
  `SELECT COUNT(*)` query on the table returns the count
  from the statistics, rather than picking up the added rows.

As a workaround, use the `ANALYZE TABLE` command to gather
new statistics, or set
`hive.compute.query.using.stats=false`. For more information,
see [Statistics in Hive](https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ExistingTables%E2%80%93ANALYZE "https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ExistingTables%E2%80%93ANALYZE") in the Apache Hive documentation.

- **Spark**—When using Spark, there
  is a file handler leak issue with the apppusher daemon, which can appear
  for a long-running Spark job after several hours or days. To fix the
  issue, connect to the master node and type `sudo
/etc/init.d/apppusher stop`. This stops that apppusher daemon,
  which Amazon EMR will restart automatically.
- **Application history**
  - Historical data for dead Spark executors is not
    available.
  - Application history is not available for clusters that use a
    security configuration to enable in-flight encryption.

## Release 5.7.0

The following release notes include information for the Amazon EMR 5.7.0 release.
Changes are relative to the Amazon EMR 5.6.0 release.

Release date: July 13, 2017

### Upgrades

- Flink 1.3.0
- Phoenix 4.11.0
- Zeppelin 0.7.2

### New features

- Added the ability to specify a custom Amazon Linux AMI when you create
  a cluster. For more information, see [Using a custom
  AMI](../ManagementGuide/emr-custom-ami.md "../ManagementGuide/emr-custom-ami.md").

### Changes, enhancements, and resolved issues

- **HBase**
  - Added capability to configure HBase read-replica clusters. See
    [Using a read-replica cluster.](emr-hbase-s3.md#emr-hbase-s3-read-replica "emr-hbase-s3.md#emr-hbase-s3-read-replica")
  - Multiple bug fixes and enhancements

- **Presto** - added ability to configure
  `node.properties`.
- **YARN** - added ability to configure
  `container-log4j.properties`
- **Sqoop** - backported [SQOOP-2880](https://issues.apache.org/jira/browse/SQOOP-2880 "https://issues.apache.org/jira/browse/SQOOP-2880"), which introduces an argument that allows you to
  set the Sqoop temporary directory.

## Release 5.6.0

The following release notes include information for the Amazon EMR 5.6.0 release.
Changes are relative to the Amazon EMR 5.5.0 release.

Release date: June 5, 2017

### Upgrades

- Flink 1.2.1
- HBase 1.3.1
- Mahout 0.13.0. This is the first version of Mahout to support Spark
  2.x in Amazon EMR version 5.0 and later.
- Spark 2.1.1

### Changes, enhancements, and resolved issues

- **Presto**
  - Added the ability to enable SSL/TLS secured communication
    between Presto nodes by enabling in-transit encryption using a
    security configuration. For more information, see [In-transit data encryption](emr-data-encryption-options.md#emr-encryption-intransit "emr-data-encryption-options.md#emr-encryption-intransit").
  - Backported [Presto 7661](https://github.com/prestodb/presto/pull/7661/commits "https://github.com/prestodb/presto/pull/7661/commits"), which adds the `VERBOSE`
    option to the `EXPLAIN ANALYZE` statement to report
    more detailed, low level statistics about a query plan.

## Release 5.5.3

The following release notes include information for Amazon EMR release 5.5.3. Changes
are relative to 5.5.2.

Initial release date: August 29, 2018

###### Changes, enhancements, and resolved issues

- This release addresses a potential security vulnerability.

## Release 5.5.2

The following release notes include information for Amazon EMR release 5.5.2. Changes
are relative to 5.5.1.

Initial release date: March 29, 2018

###### Changes, enhancements, and resolved issues

- Updated the Amazon Linux kernel of the defaultAmazon Linux AMI for Amazon EMR to address potential vulnerabilities.

## Release 5.5.1

The following release notes include information for the Amazon EMR 5.5.1 release.
Changes are relative to the Amazon EMR 5.5.0 release.

Initial release date: January 22, 2018

### Changes, enhancements, and resolved

issues

- Updated the Amazon Linux kernel of the defaultAmazon Linux AMI for Amazon EMR to address vulnerabilities associated with speculative execution (CVE-2017-5715, CVE-2017-5753, and CVE-2017-5754). For more information, see [https://aws.amazon.com/security/security-bulletins/AWS-2018-013/](https://aws.amazon.com/security/security-bulletins/AWS-2018-013/ "https://aws.amazon.com/security/security-bulletins/AWS-2018-013/").

## Release 5.5.0

The following release notes include information for the Amazon EMR 5.5.0 release.
Changes are relative to the Amazon EMR 5.4.0 release.

Release date: April 26, 2017

### Upgrades

- Hue 3.12
- Presto 0.170
- Zeppelin 0.7.1
- ZooKeeper 3.4.10

### Changes, enhancements, and resolved issues

- **Spark**
  - Backported Spark Patch [(SPARK-20115) fix DAGScheduler to recompute all the lost
    shuffle blocks when external shuffle service is
    unavailable](https://issues.apache.org/jira/browse/SPARK-20115 "https://issues.apache.org/jira/browse/SPARK-20115") to version 2.1.0 of Spark, which is
    included in this release.

- **Flink**
  - Flink is now built with Scala 2.11. If you use the Scala API
    and libraries, we recommend that you use Scala 2.11 in your
    projects.
  - Addressed an issue where `HADOOP_CONF_DIR` and
    `YARN_CONF_DIR` defaults were not properly set,
    so `start-scala-shell.sh` failed to work. Also added
    the ability to set these values using
    `env.hadoop.conf.dir` and
    `env.yarn.conf.dir` in
    `/etc/flink/conf/flink-conf.yaml` or the
    `flink-conf` configuration classification.
  - Introduced a new EMR-specific command,
    `flink-scala-shell` as a wrapper for
    `start-scala-shell.sh`. We recommend using this
    command instead of `start-scala-shell`. The new
    command simplifies execution. For example,
    `flink-scala-shell -n 2` starts a Flink Scala
    shell with a task parallelism of 2.
  - Introduced a new EMR-specific command,
    `flink-yarn-session` as a wrapper for
    `yarn-session.sh`. We recommend using this
    command instead of `yarn-session`. The new command
    simplifies execution. For example, `flink-yarn-session -d
-n 2` starts a long-running Flink session in a
    detached state with two task managers.
  - Addressed [(FLINK-6125) commons httpclient is not shaded anymore in
    Flink 1.2](https://issues.apache.org/jira/browse/FLINK-6125 "https://issues.apache.org/jira/browse/FLINK-6125").

- **Presto**
  - Added support for LDAP authentication. Using LDAP with Presto
    on Amazon EMR requires that you enable HTTPS access for the Presto
    coordinator (`http-server.https.enabled=true` in
    `config.properties`). For configuration details,
    see [LDAP authentication](https://prestodb.io/docs/current/security/ldap.html "https://prestodb.io/docs/current/security/ldap.html") in Presto documentation.
  - Added support for `SHOW GRANTS`.

- **Amazon EMR Base Linux AMI**
  - Amazon EMR releases are now based on Amazon Linux 2017.03. For more
    information, see [Amazon Linux AMI 2017.03 release notes](https://aws.amazon.com/amazon-linux-ami/2017.03-release-notes/ "https://aws.amazon.com/amazon-linux-ami/2017.03-release-notes/").
  - Removed Python 2.6 from the Amazon EMR base Linux image. Python 2.7
    and 3.4 are installed by default. You can install Python 2.6
    manually if necessary.

## Release 5.4.0

The following release notes include information for the Amazon EMR 5.4.0 release.
Changes are relative to the Amazon EMR 5.3.0 release.

Release date: March 08, 2017

### Upgrades

The following upgrades are available in this release:

- Upgraded to Flink 1.2.0
- Upgraded to Hbase 1.3.0
- Upgraded to Phoenix 4.9.0

###### Note

If you upgrade from an earlier version of Amazon EMR to Amazon EMR version
5.4.0 or later and use secondary indexing, upgrade local indexes as
described in the [Apache Phoenix documentation](https://phoenix.apache.org/secondary_indexing.html#Upgrading_Local_Indexes_created_before_4.8.0 "https://phoenix.apache.org/secondary_indexing.html#Upgrading_Local_Indexes_created_before_4.8.0"). Amazon EMR removes the
required configurations from the `hbase-site`
classification, but indexes need to be repopulated. Online and
offline upgrade of indexes are supported. Online upgrades are the
default, which means indexes are repopulated while initializing from
Phoenix clients of version 4.8.0 or greater. To specify offline
upgrades, set the `phoenix.client.localIndexUpgrade`
configuration to false in the `phoenix-site`
classification, and then SSH to the master node to run `psql
 [zookeeper] -1`.

- Upgraded to Presto 0.166
- Upgraded to Zeppelin 0.7.0

### Changes and enhancements

The following are changes made to Amazon EMR releases for release label
emr-5.4.0:

- Added support for r4 instances. See [Amazon EC2 instance
  types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

## Release 5.3.1

The following release notes include information for the Amazon EMR 5.3.1 release. Changes
are relative to the Amazon EMR 5.3.0 release.

Release date: February 7, 2017

Minor changes to backport Zeppelin patches and update the default AMI for Amazon EMR.

## Release 5.3.0

The following release notes include information for the Amazon EMR 5.3.0 release.
Changes are relative to the Amazon EMR 5.2.1 release.

Release date: January 26, 2017

### Upgrades

The following upgrades are available in this release:

- Upgraded to Hive 2.1.1
- Upgraded to Hue 3.11.0
- Upgraded to Spark 2.1.0
- Upgraded to Oozie 4.3.0
- Upgraded to Flink 1.1.4

### Changes and enhancements

The following are changes made to Amazon EMR releases for release label
emr-5.3.0:

- Added a patch to Hue that allows you to use the
  `interpreters_shown_on_wheel` setting to configure what
  interpreters to show first on the Notebook selection wheel, regardless
  of their ordering in the `hue.ini` file.
- Added the `hive-parquet-logging` configuration
  classification, which you can use to configure values in Hive's
  `parquet-logging.properties` file.

## Release 5.2.2

The following release notes include information for the Amazon EMR 5.2.2 release.
Changes are relative to the Amazon EMR 5.2.1 release.

Release date: May 2, 2017

### Known issues resolved from the previous releases

- Backported [SPARK-194459](https://issues.apache.org/jira/browse/SPARK-19459 "https://issues.apache.org/jira/browse/SPARK-19459"), which addresses an issue where reading from
  an ORC table with char/varchar columns can fail.

## Release 5.2.1

The following release notes include information for the Amazon EMR 5.2.1 release.
Changes are relative to the Amazon EMR 5.2.0 release.

Release date: December 29, 2016

### Upgrades

The following upgrades are available in this release:

- Upgraded to Presto 0.157.1. For more information, see [Presto release notes](https://prestodb.io/docs/current/release/release-0.157.1.html "https://prestodb.io/docs/current/release/release-0.157.1.html") in the Presto documentation.
- Upgraded to Zookeeper 3.4.9. For more information, see [ZooKeeper release notes](https://zookeeper.apache.org/doc/r3.4.9/releasenotes.html "https://zookeeper.apache.org/doc/r3.4.9/releasenotes.html") in the Apache ZooKeeper
  documentation.

### Changes and enhancements

The following are changes made to Amazon EMR releases for release label
emr-5.2.1:

- Added support for the Amazon EC2 m4.16xlarge instance type in Amazon EMR version
  4.8.3 and later, excluding 5.0.0, 5.0.3, and 5.2.0.
- Amazon EMR releases are now based on Amazon Linux 2016.09. For more information,
  see [https://aws.amazon.com/amazon-linux-ami/2016.09-release-notes/](https://aws.amazon.com/amazon-linux-ami/2016.09-release-notes/ "https://aws.amazon.com/amazon-linux-ami/2016.09-release-notes/").
- The location of Flink and YARN configuration paths are now set by
  default in `/etc/default/flink` that you don't need to set
  the environment variables `FLINK_CONF_DIR` and
  `HADOOP_CONF_DIR` when running the `flink` or
  `yarn-session.sh` driver scripts to launch Flink
  jobs.
- Added support for FlinkKinesisConsumer class.

### Known issues resolved from the previous releases

- Fixed an issue in Hadoop where the ReplicationMonitor thread could get
  stuck for a long time because of a race between replication and deletion
  of the same file in a large cluster.
- Fixed an issue where ControlledJob#toString failed with a null pointer
  exception (NPE) when job status was not successfully updated.

## Release 5.2.0

The following release notes include information for the Amazon EMR 5.2.0 release.
Changes are relative to the Amazon EMR 5.1.0 release.

Release date: November 21, 2016

### Changes and enhancements

The following changes and enhancements are available in this release:

- Added Amazon S3 storage mode for HBase.
- Enables you to specify an Amazon S3 location for the HBase rootdir. For
  more information, see [HBase
  on Amazon S3](emr-hbase-s3.md "emr-hbase-s3.md").

### Upgrades

The following upgrades are available in this release:

- Upgraded to Spark 2.0.2

### Known issues resolved from the previous releases

- Fixed an issue with /mnt being constrained to 2 TB on EBS-only
  instance types.
- Fixed an issue with instance-controller and logpusher logs being
  output to their corresponding .out files instead of to their normal
  log4j-configured .log files, which rotate hourly. The .out files don't
  rotate, so this would eventually fill up the /emr partition. This issue
  only affects hardware virtual machine (HVM) instance types.

## Release 5.1.0

The following release notes include information for the Amazon EMR 5.1.0 release.
Changes are relative to the Amazon EMR 5.0.0 release.

Release date: November 03, 2016

### Changes and enhancements

The following changes and enhancements are available in this release:

- Added support for Flink 1.1.3.
- Presto has been added as an option in the notebook section of
  Hue.

### Upgrades

The following upgrades are available in this release:

- Upgraded to HBase 1.2.3
- Upgraded to Zeppelin 0.6.2

### Known issues resolved from the previous releases

- Fixed an issue with Tez queries on Amazon S3 with ORC files did not perform
  as well as earlier Amazon EMR 4.x versions.

## Release 5.0.3

The following release notes include information for the Amazon EMR 5.0.3 release.
Changes are relative to the Amazon EMR 5.0.0 release.

Release date: October 24, 2016

### Upgrades

The following upgrades are available in this release:

- Upgraded to Hadoop 2.7.3
- Upgraded to Presto 0.152.3, which includes support for the Presto web
  interface. You can access the Presto web interface on the Presto
  coordinator using port 8889. For more information about the Presto web
  interface, see [Web
  interface](https://prestodb.io/docs/current/admin/web-interface.html "https://prestodb.io/docs/current/admin/web-interface.html") in the Presto documentation.
- Upgraded to Spark 2.0.1
- Amazon EMR releases are now based on Amazon Linux 2016.09. For more information,
  see [https://aws.amazon.com/amazon-linux-ami/2016.09-release-notes/](https://aws.amazon.com/amazon-linux-ami/2016.09-release-notes/ "https://aws.amazon.com/amazon-linux-ami/2016.09-release-notes/").

## Release 5.0.0

Release date: July 27, 2016

### Upgrades

The following upgrades are available in this release:

- Upgraded to Hive 2.1
- Upgraded to Presto 0.150
- Upgraded to Spark 2.0
- Upgraded to Hue 3.10.0
- Upgraded to Pig 0.16.0
- Upgraded to Tez 0.8.4
- Upgraded to Zeppelin 0.6.1

### Changes and enhancements

The following are changes made to Amazon EMR releases for release label emr-5.0.0
or greater:

- Amazon EMR supports the latest open-source versions of Hive (version 2.1)
  and Pig (version 0.16.0). If you have used Hive or Pig on Amazon EMR in the
  past, this may affect some use cases. For more information, see [Hive](emr-hive.md "emr-hive.md") and [Pig](emr-pig.md "emr-pig.md").
- The default execution engine for Hive and Pig is now Tez. To change
  this, you would edit the appropriate values in the
  `hive-site` and `pig-properties` configuration
  classifications, respectively.
- An enhanced step debugging feature was added, which allows you to see
  the root cause of step failures if the service can determine the cause.
  For more information, see [Enhanced step
  debugging](../ManagementGuide/emr-enhanced-step-debugging.md "../ManagementGuide/emr-enhanced-step-debugging.md") in the Amazon EMR Management Guide.
- Applications that previously ended with "-Sandbox" no longer have that
  suffix. This may break your automation, for example, if you are using
  scripts to launch clusters with these applications. The following table
  shows application names in Amazon EMR 4.7.2 versus Amazon EMR 5.0.0.

| Application name changes | Amazon EMR 4.7.2 | Amazon EMR 5.0.0 |
| ------------------------ | ---------------- | ---------------- |
| Oozie-Sandbox            | Oozie            |
| Presto-Sandbox           | Presto           |
| Sqoop-Sandbox            | Sqoop            |
| Zeppelin-Sandbox         | Zeppelin         |
| ZooKeeper-Sandbox        | ZooKeeper        |

- Spark is now compiled for Scala 2.11.
- Java 8 is now the default JVM. All applications run using the Java 8
  runtime. There are no changes to any application's byte code target.
  Most applications continue to target Java 7.
- Zeppelin now includes authentication features. For more information,
  see [Zeppelin](emr-zeppelin.md "emr-zeppelin.md").
- Added support for security configurations, which allow you to create
  and apply encryption options more easily. For more information, see
  [Data
  encryption](emr-data-encryption.md "emr-data-encryption.md").

## Release 4.9.5

The following release notes include information for Amazon EMR release 4.9.5. Changes
are relative to 4.9.4.

Initial release date: August 29, 2018

###### Changes, enhancements, and resolved issues

- HBase
  - This release addresses a potential security vulnerability.

## Release 4.9.4

The following release notes include information for Amazon EMR release 4.9.4. Changes
are relative to 4.9.3.

Initial release date: March 29, 2018

###### Changes, enhancements, and resolved issues

- Updated the Amazon Linux kernel of the defaultAmazon Linux AMI for Amazon EMR to address potential vulnerabilities.

## Release 4.9.3

The following release notes include information for the Amazon EMR 4.9.3 release.
Changes are relative to the Amazon EMR 4.9.2 release.

Initial release date: January 22, 2018

### Changes, enhancements, and resolved

issues

- Updated the Amazon Linux kernel of the defaultAmazon Linux AMI for Amazon EMR to address vulnerabilities associated with speculative execution (CVE-2017-5715, CVE-2017-5753, and CVE-2017-5754). For more information, see [https://aws.amazon.com/security/security-bulletins/AWS-2018-013/](https://aws.amazon.com/security/security-bulletins/AWS-2018-013/ "https://aws.amazon.com/security/security-bulletins/AWS-2018-013/").

## Release 4.9.2

The following release notes include information for the Amazon EMR 4.9.2 release.
Changes are relative to the Amazon EMR 4.9.1 release.

Release date: July 13, 2017

Minor changes, bug fixes, and enhancements were made in this release.

## Release 4.9.1

The following release notes include information for the Amazon EMR 4.9.1 release.
Changes are relative to the Amazon EMR 4.8.4 release.

Release date: April 10, 2017

### Known issues resolved from the previous releases

- Backports of [HIVE-9976](https://issues.apache.org/jira/browse/HIVE-9976 "https://issues.apache.org/jira/browse/HIVE-9976") and [HIVE-10106](https://issues.apache.org/jira/browse/HIVE-10106 "https://issues.apache.org/jira/browse/HIVE-10106")
- Fixed an issue in YARN where a large number of nodes (greater than
  2,000) and containers (greater than 5,000) would cause an out of memory
  error, for example: `"Exception in thread 'main'
java.lang.OutOfMemoryError"`.

### Changes and enhancements

The following are changes made to Amazon EMR releases for release label
emr-4.9.1:

- Amazon EMR releases are now based on Amazon Linux 2017.03. For more information,
  see [https://aws.amazon.com/amazon-linux-ami/2017.03-release-notes/](https://aws.amazon.com/amazon-linux-ami/2017.03-release-notes/ "https://aws.amazon.com/amazon-linux-ami/2017.03-release-notes/").
- Removed Python 2.6 from the Amazon EMR base Linux image. You can install
  Python 2.6 manually if necessary.

## Release 4.8.4

The following release notes include information for the Amazon EMR 4.8.4 release.
Changes are relative to the Amazon EMR 4.8.3 release.

Release date: Feb 7, 2017

Minor changes, bug fixes, and enhancements were made in this release.

## Release 4.8.3

The following release notes include information for the Amazon EMR 4.8.3 release.
Changes are relative to the Amazon EMR 4.8.2 release.

Release date: December 29, 2016

### Upgrades

The following upgrades are available in this release:

- Upgraded to Presto 0.157.1. For more information, see [Presto release notes](https://prestodb.io/docs/current/release/release-0.157.1.html "https://prestodb.io/docs/current/release/release-0.157.1.html") in the Presto documentation.
- Upgraded to Spark 1.6.3. For more information, see [Spark release notes](http://spark.apache.org/releases/spark-release-1-6-3.html "http://spark.apache.org/releases/spark-release-1-6-3.html") in the Apache Spark
  documentation.
- Upgraded to ZooKeeper 3.4.9. For more information, see [ZooKeeper release notes](https://zookeeper.apache.org/doc/r3.4.9/releasenotes.html "https://zookeeper.apache.org/doc/r3.4.9/releasenotes.html") in the Apache ZooKeeper
  documentation.

### Changes and enhancements

The following are changes made to Amazon EMR releases for release label
emr-4.8.3:

- Added support for the Amazon EC2 m4.16xlarge instance type in Amazon EMR version
  4.8.3 and later, excluding 5.0.0, 5.0.3, and 5.2.0.
- Amazon EMR releases are now based on Amazon Linux 2016.09. For more information,
  see [https://aws.amazon.com/amazon-linux-ami/2016.09-release-notes/](https://aws.amazon.com/amazon-linux-ami/2016.09-release-notes/ "https://aws.amazon.com/amazon-linux-ami/2016.09-release-notes/").

### Known issues resolved from the previous releases

- Fixed an issue in Hadoop where the ReplicationMonitor thread could get
  stuck for a long time because of a race between replication and deletion
  of the same file in a large cluster.
- Fixed an issue where ControlledJob#toString failed with a null pointer
  exception (NPE) when job status was not successfully updated.

## Release 4.8.2

The following release notes include information for the Amazon EMR 4.8.2 release.
Changes are relative to the Amazon EMR 4.8.0 release.

Release date: October 24, 2016

### Upgrades

The following upgrades are available in this release:

- Upgraded to Hadoop 2.7.3
- Upgraded to Presto 0.152.3, which includes support for the Presto web
  interface. You can access the Presto web interface on the Presto
  coordinator using port 8889. For more information about the Presto web
  interface, see [Web
  interface](https://prestodb.io/docs/current/admin/web-interface.html "https://prestodb.io/docs/current/admin/web-interface.html") in the Presto documentation.
- Amazon EMR releases are now based on Amazon Linux 2016.09. For more information,
  see [https://aws.amazon.com/amazon-linux-ami/2016.09-release-notes/](https://aws.amazon.com/amazon-linux-ami/2016.09-release-notes/ "https://aws.amazon.com/amazon-linux-ami/2016.09-release-notes/").

## Release 4.8.0

Release date: September 7, 2016

### Upgrades

The following upgrades are available in this release:

- Upgraded to HBase 1.2.2
- Upgraded to Presto-Sandbox 0.151
- Upgraded to Tez 0.8.4
- Upgraded to Zeppelin-Sandbox 0.6.1

### Changes and enhancements

The following are changes made to Amazon EMR releases for release label
emr-4.8.0:

- Fixed an issue in YARN where the ApplicationMaster would attempt to
  clean up containers that no longer exist because their instances have
  been terminated.
- Corrected the hive-server2 URL for Hive2 actions in the Oozie
  examples.
- Added support for additional Presto catalogs.
- Backported patches: [HIVE-8948](https://issues.apache.org/jira/browse/HIVE-8948 "https://issues.apache.org/jira/browse/HIVE-8948"), [HIVE-12679](https://issues.apache.org/jira/browse/HIVE-12679 "https://issues.apache.org/jira/browse/HIVE-12679"), [HIVE-13405](https://issues.apache.org/jira/browse/HIVE-13405 "https://issues.apache.org/jira/browse/HIVE-13405"), [PHOENIX-3116](https://issues.apache.org/jira/browse/PHOENIX-3116 "https://issues.apache.org/jira/browse/PHOENIX-3116"), [HADOOP-12689](https://issues.apache.org/jira/browse/HADOOP-12689 "https://issues.apache.org/jira/browse/HADOOP-12689")
- Added support for security configurations, which allow you to create
  and apply encryption options more easily. For more information, see
  [Data
  encryption](emr-data-encryption.md "emr-data-encryption.md").

## Release 4.7.2

The following release notes include information for Amazon EMR 4.7.2.

Release date: July 15, 2016

### Features

The following features are available in this release:

- Upgraded to Mahout 0.12.2
- Upgraded to Presto 0.148
- Upgraded to Spark 1.6.2
- You can now create an AWSCredentialsProvider for use with EMRFS using
  a URI as a parameter. For more information, see [Create an
  AWSCredentialsProvider for EMRFS](emr-plan-credentialsprovider.md "emr-plan-credentialsprovider.md").
- EMRFS now allows users to configure a custom DynamoDB endpoint for their
  Consistent View metadata using the
  `fs.s3.consistent.dynamodb.endpoint` property in
  `emrfs-site.xml`.
- Added a script in `/usr/bin` called
  `spark-example`, which wraps
  `/usr/lib/spark/spark/bin/run-example` so you can
  run examples directly. For instance, to run the SparkPi example that
  comes with the Spark distribution, you can run `spark-example
SparkPi 100` from the command line or using
  `command-runner.jar` as a step in the API.

### Known issues resolved from previous releases

- Fixed an issue where Oozie had the
  `spark-assembly.jar` was not in the correct
  location when Spark was also installed, which resulted in failure to
  launch Spark applications with Oozie.
- Fixed an issue with Spark Log4j-based logging in YARN
  containers.

## Release 4.7.1

Release date: June 10, 2016

### Known issues resolved from previous releases

- Fixed an issue that extended the startup time of clusters launched in
  a VPC with private subnets. The bug only impacted clusters launched with
  the Amazon EMR 4.7.0 release.
- Fixed an issue that improperly handled listing of files in Amazon EMR for
  clusters launched with the Amazon EMR 4.7.0 release.

## Release 4.7.0

###### Important

Amazon EMR 4.7.0 is deprecated. Use Amazon EMR 4.7.1 or later instead.

Release date: June 2, 2016

### Features

The following features are available in this release:

- Added Apache Phoenix 4.7.0
- Added Apache Tez 0.8.3
- Upgraded to HBase 1.2.1
- Upgraded to Mahout 0.12.0
- Upgraded to Presto 0.147
- Upgraded the AWS SDK for Java to 1.10.75
- The final flag was removed from the
  `mapreduce.cluster.local.dir` property in
  `mapred-site.xml` to allow users to run Pig in
  local mode.

### Amazon Redshift JDBC drivers available on cluster

Amazon Redshift JDBC drivers are now included at
`/usr/share/aws/redshift/jdbc`.
`/usr/share/aws/redshift/jdbc/RedshiftJDBC41.jar` is the
JDBC 4.1-compatible Amazon Redshift driver and
`/usr/share/aws/redshift/jdbc/RedshiftJDBC4.jar` is the
JDBC 4.0-compatible Amazon Redshift driver. For more information, see [Configure a JDBC
connection](../../../redshift/latest/mgmt/configure-jdbc-connection.md "../../../redshift/latest/mgmt/configure-jdbc-connection.md") in the _Amazon Redshift Management Guide_.

### Java 8

Except for Presto, OpenJDK 1.7 is the default JDK used for all applications.
However, both OpenJDK 1.7 and 1.8 are installed. For information about how to
set `JAVA_HOME` for applications, see [Configuring
applications to use Java 8](emr-configure-apps.md#configuring-java8 "emr-configure-apps.md#configuring-java8").

### Known issues resolved from previous releases

- Fixed a kernel issue that significantly affected performance on
  Throughput Optimized HDD (st1) EBS volumes for Amazon EMR in
  emr-4.6.0.
- Fixed an issue where a cluster would fail if any HDFS encryption zone
  were specified without choosing Hadoop as an application.
- Changed the default HDFS write policy from `RoundRobin` to
  `AvailableSpaceVolumeChoosingPolicy`. Some volumes were
  not properly utilized with the RoundRobin configuration, which resulted
  in failed core nodes and an unreliable HDFS.
- Fixed an issue with the EMRFS CLI, which would cause an exception when
  creating the default DynamoDB metadata table for consistent views.
- Fixed a deadlock issue in EMRFS that potentially occurred during
  multipart rename and copy operations.
- Fixed an issue with EMRFS that caused the CopyPart size default to be
  5 MB. The default is now properly set at 128 MB.
- Fixed an issue with the Zeppelin upstart configuration that
  potentially prevented you from stopping the service.
- Fixed an issue with Spark and Zeppelin, which prevented you from using
  the `s3a://` URI scheme because
  `/usr/lib/hadoop/hadoop-aws.jar` was not properly
  loaded in their respective classpath.
- Backported [HUE-2484](https://issues.cloudera.org/browse/HUE-2484 "https://issues.cloudera.org/browse/HUE-2484").
- Backported a [commit](https://github.com/cloudera/hue/commit/c3c89f085e7a29c9fac7de016d881142d90af3eb "https://github.com/cloudera/hue/commit/c3c89f085e7a29c9fac7de016d881142d90af3eb") from Hue 3.9.0 (no JIRA exists) to fix an issue with
  the HBase browser sample.
- Backported [HIVE-9073](https://issues.apache.org/jira/browse/HIVE-9073 "https://issues.apache.org/jira/browse/HIVE-9073").

## Release 4.6.0

Release date: April 21, 2016

### Features

The following features are available in this release:

- Added HBase 1.2.0
- Added Zookeeper-Sandbox 3.4.8
- Upgraded to Presto-Sandbox 0.143
- Amazon EMR releases are now based on Amazon Linux 2016.03.0. For more information,
  see [https://aws.amazon.com/amazon-linux-ami/2016.03-release-notes/](https://aws.amazon.com/amazon-linux-ami/2016.03-release-notes/ "https://aws.amazon.com/amazon-linux-ami/2016.03-release-notes/").

### Issue affecting Throughput Optimized HDD (st1) EBS volume types

An issue in the Linux kernel versions 4.2 and above significantly affects
performance on Throughput Optimized HDD (st1) EBS volumes for EMR. This release
(emr-4.6.0) uses kernel version 4.4.5 and hence is impacted. Therefore, we
recommend not using emr-4.6.0 if you want to use st1 EBS volumes. You can use
emr-4.5.0 or prior Amazon EMR releases with st1 without impact. In addition, we
provide the fix with future releases.

### Python defaults

Python 3.4 is now installed by default, but Python 2.7 remains the system
default. You may configure Python 3.4 as the system default using either a
bootstrap action; you can use the configuration API to set PYSPARK_PYTHON export
to `/usr/bin/python3.4` in the `spark-env`
classification to affect the Python version used by PySpark.

### Java 8

Except for Presto, OpenJDK 1.7 is the default JDK used for all applications.
However, both OpenJDK 1.7 and 1.8 are installed. For information about how to
set `JAVA_HOME` for applications, see [Configuring
applications to use Java 8](emr-configure-apps.md#configuring-java8 "emr-configure-apps.md#configuring-java8").

### Known issues resolved from previous releases

- Fixed an issue where application provisioning would sometimes randomly
  fail due to a generated password.
- Previously, `mysqld` was installed on all nodes. Now, it is
  only installed on the master instance and only if the chosen application
  includes `mysql-server` as a component. Currently, the
  following applications include the `mysql-server` component:
  HCatalog, Hive, Hue, Presto-Sandbox, and Sqoop-Sandbox.
- Changed `yarn.scheduler.maximum-allocation-vcores` to 80
  from the default of 32, which fixes an issue introduced in emr-4.4.0
  that mainly occurs with Spark while using the
  `maximizeResourceAllocation` option in a cluster whose
  core instance type is one of a few large instance types that have the
  YARN vcores set higher than 32; namely c4.8xlarge, cc2.8xlarge,
  hs1.8xlarge, i2.8xlarge, m2.4xlarge, r3.8xlarge, d2.8xlarge, or
  m4.10xlarge were affected by this issue.
- s3-dist-cp now uses EMRFS for all Amazon S3 nominations and no longer
  stages to a temporary HDFS directory.
- Fixed an issue with exception handling for client-side encryption
  multipart uploads.
- Added an option to allow users to change the Amazon S3 storage class. By
  default this setting is `STANDARD`. The
  `emrfs-site` configuration classification setting
  is `fs.s3.storageClass` and the possible values are
  `STANDARD`, `STANDARD_IA`, and
  `REDUCED_REDUNDANCY`. For more information about storage
  classes, see [Storage
  classes](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md") in the Amazon Simple Storage Service User Guide.

## Release 4.5.0

Release date: April 4, 2016

### Features

The following features are available in this release:

- Upgraded to Spark 1.6.1
- Upgraded to Hadoop 2.7.2
- Upgraded to Presto 0.140
- Added AWS KMS support for Amazon S3 server-side encryption.

### Known issues resolved from previous releases

- Fixed an issue where MySQL and Apache servers would not start after a
  node was rebooted.
- Fixed an issue where IMPORT did not work correctly with
  non-partitioned tables stored in Amazon S3
- Fixed an issue with Presto where it requires the staging directory to
  be `/mnt/tmp` rather than `/tmp`
  when writing to Hive tables.

## Release 4.4.0

Release date: March 14, 2016

### Features

The following features are available in this release:

- Added HCatalog 1.0.0
- Added Sqoop-Sandbox 1.4.6
- Upgraded to Presto 0.136
- Upgraded to Zeppelin 0.5.6
- Upgraded to Mahout 0.11.1
- Enabled `dynamicResourceAllocation` by default.
- Added a table of all configuration classifications for the release.
  For more information, see the Configuration Classifications table in
  [Configuring
  applications](emr-configure-apps.md "emr-configure-apps.md").

### Known issues resolved from previous releases

- Fixed an issue where the `maximizeResourceAllocation`
  setting would not reserve enough memory for YARN ApplicationMaster
  daemons.
- Fixed an issue encountered with a custom DNS. If any entries in
  `resolve.conf` precede the custom entries
  provided, then the custom entries are not resolvable. This behavior was
  affected by clusters in a VPC where the default VPC name server is
  inserted as the top entry in `resolve.conf`.
- Fixed an issue where the default Python moved to version 2.7 and boto
  was not installed for that version.
- Fixed an issue where YARN containers and Spark applications would
  generate a unique Ganglia round robin database (rrd) file, which
  resulted in the first disk attached to the instance filling up. Because
  of this fix, YARN container level metrics have been disabled and Spark
  application level metrics have been disabled.
- Fixed an issue in log pusher where it would delete all empty log
  folders. The effect was that the Hive CLI was not able to log because
  log pusher was removing the empty `user` folder under
  `/var/log/hive`.
- Fixed an issue affecting Hive imports, which affected partitioning and
  resulted in an error during import.
- Fixed an issue where EMRFS and s3-dist-cp did not properly handle
  bucket names that contain periods.
- Changed a behavior in EMRFS so that in versioning-enabled buckets the
  `_$folder$` marker file is not continuously created,
  which may contribute to improved performance for versioning-enabled
  buckets.
- Changed the behavior in EMRFS such that it does not use instruction
  files except for cases where client-side encryption is enabled. If you
  want to delete instruction files while using client-side encryption, you
  can set the emrfs-site.xml property,
  `fs.s3.cse.cryptoStorageMode.deleteInstructionFiles.enabled`,
  to true.
- Changed YARN log aggregation to retain logs at the aggregation
  destination for two days. The default destination is your cluster's HDFS
  storage. If you want to change this duration, change the value of
  `yarn.log-aggregation.retain-seconds` using the
  `yarn-site` configuration classification when you create
  your cluster. As always, you can save your application logs to Amazon S3
  using the `log-uri` parameter when you create your
  cluster.

### Patches applied

The following patches from open source projects were included in this
release:

- [HIVE-9655](https://issues.apache.org/jira/browse/HIVE-9655 "https://issues.apache.org/jira/browse/HIVE-9655")
- [HIVE-9183](https://issues.apache.org/jira/browse/HIVE-9183 "https://issues.apache.org/jira/browse/HIVE-9183")
- [HADOOP-12810](https://issues.apache.org/jira/browse/HADOOP-12810 "https://issues.apache.org/jira/browse/HADOOP-12810")

## Release 4.3.0

Release date: January 19, 2016

### Features

The following features are available in this release:

- Upgraded to Hadoop 2.7.1
- Upgraded to Spark 1.6.0
- Upgraded Ganglia to 3.7.2
- Upgraded Presto to 0.130

Amazon EMR made some changes to `spark.dynamicAllocation.enabled` when
it is set to true; it is false by default. When set to true, this affects the
defaults set by the `maximizeResourceAllocation` setting:

- If `spark.dynamicAllocation.enabled` is set to true,
  `spark.executor.instances` is not set by
  `maximizeResourceAllocation`.
- The `spark.driver.memory` setting is now configured based
  on the instance types in the cluster in a similar way to how
  `spark.executors.memory` is set. However, because the
  Spark driver application may run on either the master or one of the core
  instances (for example, in YARN client and cluster modes, respectively),
  the `spark.driver.memory` setting is set based on the
  instance type of the smaller instance type between these two instance
  groups.
- The `spark.default.parallelism` setting is now set at twice
  the number of CPU cores available for YARN containers. In previous
  releases, this was half that value.
- The calculations for the memory overhead reserved for Spark YARN
  processes was adjusted to be more accurate, resulting in a small
  increase in the total amount of memory available to Spark (that is,
  `spark.executor.memory`).

### Known issues resolved from the previous releases

- YARN log aggregation is now enabled by default.
- Fixed an issue where logs would not be pushed to a cluster's Amazon S3 logs
  bucket when YARN log aggregation was enabled.
- YARN container sizes now have a new minimum of 32 across all node
  types.
- Fixed an issue with Ganglia that caused excessive disk I/O on the
  master node in large clusters.
- Fixed an issue that prevented applications logs from being pushed to
  Amazon S3 when a cluster is shutting down.
- Fixed an issue in EMRFS CLI that caused certain commands to
  fail.
- Fixed an issue with Zeppelin that prevented dependencies from being
  loaded in the underlying SparkContext.
- Fixed an issue that resulted from issuing a resize attempting to add
  instances.
- Fixed an issue in Hive where CREATE TABLE AS SELECT makes excessive
  list calls to Amazon S3.
- Fixed an issue where large clusters would not provision properly when
  Hue, Oozie, and Ganglia are installed.
- Fixed an issue in s3-dist-cp where it would return a zero exit code
  even if it failed with an error.

### Patches applied

The following patches from open source projects were included in this
release:

- [OOZIE-2402](https://issues.apache.org/jira/browse/OOZIE-2402 "https://issues.apache.org/jira/browse/OOZIE-2402")
- [HIVE-12502](https://issues.apache.org/jira/browse/HIVE-12502 "https://issues.apache.org/jira/browse/HIVE-12502")
- [HIVE-10631](https://issues.apache.org/jira/browse/HIVE-10631 "https://issues.apache.org/jira/browse/HIVE-10631")
- [HIVE-12213](https://issues.apache.org/jira/browse/HIVE-12213 "https://issues.apache.org/jira/browse/HIVE-12213")
- [HIVE-10559](https://issues.apache.org/jira/browse/HIVE-10559 "https://issues.apache.org/jira/browse/HIVE-10559")
- [HIVE-12715](https://issues.apache.org/jira/browse/HIVE-12715 "https://issues.apache.org/jira/browse/HIVE-12715")
- [HIVE-10685](https://issues.apache.org/jira/browse/HIVE-10685 "https://issues.apache.org/jira/browse/HIVE-10685")

## Release 4.2.0

Release date: November 18, 2015

### Features

The following features are available in this release:

- Added Ganglia support
- Upgraded to Spark 1.5.2
- Upgraded to Presto 0.125
- Upgraded Oozie to 4.2.0
- Upgraded Zeppelin to 0.5.5
- Upgraded the AWS SDK for Java to 1.10.27

### Known issues resolved from the previous releases

- Fixed an issue with the EMRFS CLI where it did not use the default
  metadata table name.
- Fixed an issue encountered when using ORC-backed tables in
  Amazon S3.
- Fixed an issue encountered with a Python version mismatch in the Spark
  configuration.
- Fixed an issue when a YARN node status fails to report because of DNS
  issues for clusters in a VPC.
- Fixed an issue encountered when YARN decommissioned nodes, resulting
  in hanged applications or the inability to schedule new
  applications.
- Fixed an issue encountered when clusters terminated with status
  TIMED_OUT_STARTING.
- Fixed an issue encountered when including the EMRFS Scala dependency
  in other builds. The Scala dependency has been removed.
