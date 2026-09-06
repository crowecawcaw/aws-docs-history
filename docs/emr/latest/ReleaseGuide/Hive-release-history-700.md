

# Amazon EMR 7.0.0 - Hive release notes
<a name="Hive-release-history-700"></a>

## Amazon EMR 7.0.0 - Hive changes
<a name="Hive-release-history-changes-700"></a>



| Type | Description | 
| --- | --- | 
| Upgrade | Hive Runtime now uses Java 17 by default. Please refer [EMR 7.0.0 Release Guide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-700-release.html) for more details. | 
| Backport | [HIVE-17709](https://issues.apache.org/jira/browse/HIVE-17709): remove sun.misc.Cleaner references | 
| Bug Fix | Disable Tez Async Init RR when LLAP or ACID is enabled  | 