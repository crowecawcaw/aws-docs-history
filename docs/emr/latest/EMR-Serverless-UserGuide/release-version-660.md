# EMR Serverless 6.6.0

The following table lists the application versions available with
EMR Serverless 6.6.0.

| Application  | Version |
| ------------ | ------- |
| Apache Spark | 3.2.0   |
| Apache Hive  | 3.1.2   |
| Apache Tez   | 0.9.2   |

###### EMR Serverless initial release notes

- EMR Serverless supports the Spark configuration classification
  `spark-defaults`. This classification changes values in Spark's
  `spark-defaults.conf` XML file. Configuration classifications allow you to
  customize applications. For more information, refer to [Configure applications](../ReleaseGuide/emr-configure-apps.md "../ReleaseGuide/emr-configure-apps.md").
- EMR Serverless supports the Hive configuration classifications `hive-site`,
  `tez-site`, `emrfs-site`, and `core-site`. This
  classification can change the values in Hive's `hive-site.xml` file, Tez's
  `tez-site.xml` file, Amazon EMR's EMRFS settings, or Hadoop's `core-site.xml`
  file, respectively. Configuration classifications allow you to customize applications. For more
  information, refer to [Configure
  applications](../ReleaseGuide/emr-configure-apps.md "../ReleaseGuide/emr-configure-apps.md").

###### Engine-specific changes, enhancements, and resolved

issues

- The following table lists Hive and Tez backports.

| Hive and Tez changes | Change                                                                                                                                                                              | Description |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Backport             | [TEZ-4430](https://issues.apache.org/jira/browse/TEZ-4430 "https://issues.apache.org/jira/browse/TEZ-4430"): Fixed<br>issue with `tez.task.launch.cmd-opts` property                |
| Backport             | [HIVE-25971](https://issues.apache.org/jira/browse/HIVE-25971 "https://issues.apache.org/jira/browse/HIVE-25971"):<br>Fixed Tez task shutdown delays due to open cached thread pool |
