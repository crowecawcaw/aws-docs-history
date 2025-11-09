# Amazon EMR 7.4.0 - Hive

release notes

## Amazon EMR 7.4.0 -

Hive changes

| Type        | Description                                                                                                                                                                                                    |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Upgrade     | [HIVE-28191](https://issues.apache.org/jira/browse/HIVE-28191 "https://issues.apache.org/jira/browse/HIVE-28191"): Upgrade Hadoop Version to 3.4.0                                                             |
| Upgrade     | Upgrade hadoop shaded protobuf to 3.21                                                                                                                                                                         |
| Upgrade     | Upgrade commons-cli to 1.5.0                                                                                                                                                                                   |
| Upgrade     | Upgrade commons-compress to 1.24.0                                                                                                                                                                             |
| Upgrade     | Upgrade commons-io to 2.14.0                                                                                                                                                                                   |
| Upgrade     | Upgrade commons-lang3 to 3.21.0                                                                                                                                                                                |
| Improvement | Change time to wait for Tez session to be opened while trying to use the existing session in HiveCLI to 10s                                                                                                    |
| Improvement | Enable short circuit mechanism in Tez DAG for simple select queries with LIMIT                                                                                                                                 |
| Improvement | [HIVE-21100](https://issues.apache.org/jira/browse/HIVE-21100 "https://issues.apache.org/jira/browse/HIVE-21100"): Allow flattening of table subdirectories<br>resulted when using TEZ engine and UNION clause |
| Bug Fix     | [HIVE-25095](https://issues.apache.org/jira/browse/HIVE-25095 "https://issues.apache.org/jira/browse/HIVE-25095"): Beeline/hive -e command can't deal with query with trailing quote                           |
| Bug Fix     | [HIVE-13781](https://issues.apache.org/jira/browse/HIVE-13781 "https://issues.apache.org/jira/browse/HIVE-13781"): Tez Job failed with FileNotFoundException when partition dir doesnt exists                  |
| Bug Fix     | [HIVE-28480](https://issues.apache.org/jira/browse/HIVE-28480 "https://issues.apache.org/jira/browse/HIVE-28480"): Disable SMB on partition hash generator mismatch across join branches in previous RS        |

### Amazon EMR 7.4.0 -

New configurations

| Classification | Name                                        | Default | Description                                                                                                                                                                                                                                                                                                                                                       |
| -------------- | ------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hive-site      | hive.ignore.failure.partition.dir.not.found | false   | Ignores failure if the table partition exists but the actual object storage path does not exist.                                                                                                                                                                                                                                                                  |
| hive-site      | hive.tez.union.flatten.subdirectories       | false   | When writing data into a table and UNION ALL is the last step of the query, Hive on Tez creates a subdirectory for each branch of the UNION ALL. When this property is enabled,<br>the subdirectories are removed, and the files are renamed and moved to the parent directory. Note that this has no effect when hive.blobstore.use.output-committer is enabled. |
