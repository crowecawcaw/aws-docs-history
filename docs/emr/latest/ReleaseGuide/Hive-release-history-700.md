# Amazon EMR 7.0.0 - Hive

release notes

## Amazon EMR 7.0.0 -

Hive changes

| Type     | Description                                                                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Upgrade  | Hive Runtime now uses Java 17 by default. Please refer [EMR 7.0.0 Release Guide](emr-700-release.md "emr-700-release.md") for more details.           |
| Backport | [HIVE-17709](https://issues.apache.org/jira/browse/HIVE-17709 "https://issues.apache.org/jira/browse/HIVE-17709"): remove sun.misc.Cleaner references |
| Bug Fix  | Disable Tez Async Init RR when LLAP or ACID is enabled                                                                                                |
