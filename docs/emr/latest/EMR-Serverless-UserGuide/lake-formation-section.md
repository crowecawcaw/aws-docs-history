# Using Lake Formation with EMR Serverless

You can configure EMR Serverless applications to use Lake Formation with either full table
access or fine-grained access control. For details on supported features in each access
mode, review the the following table.

## Feature availability

| Feature                                                                | Available from |
| ---------------------------------------------------------------------- | -------------- |
| Read operations (SELECT, DESCRIBE) for Hive, Iceberg tables            | EMR 7.2+       |
| Multi-dialect views                                                    | EMR 7.6+       |
| Read operations (SELECT, DESCRIBE) for Delta Lake and Hudi<br>tables   | EMR 7.6+       |
| Full table access for Hive, Iceberg                                    | EMR 7.9+       |
| Full table access for Delta Lake                                       | EMR 7.11+      |
| Write operations (DDL, DML) for Hive, Iceberg and Delta Lake<br>tables | EMR 7.12+      |
| Full table access for Hudi                                             | EMR 7.12+      |
