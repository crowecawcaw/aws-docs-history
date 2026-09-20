

# EMR Serverless 6.6.0
<a name="release-version-660"></a>

The following table lists the application versions available with EMR Serverless 6.6.0.


| Application | Version | 
| --- | --- | 
| Apache Spark | 3.2.0 | 
| Apache Hive | 3.1.2 | 
| Apache Tez | 0.9.2 | 

**EMR Serverless initial release notes**
+ EMR Serverless supports the Spark configuration classification `spark-defaults`. This classification changes values in Spark's `spark-defaults.conf` XML file. Configuration classifications allow you to customize applications. For more information, refer to [Configure applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).
+ EMR Serverless supports the Hive configuration classifications `hive-site`, `tez-site`, `emrfs-site`, and `core-site`. This classification can change the values in Hive's `hive-site.xml` file, Tez's `tez-site.xml` file, Amazon EMR's EMRFS settings, or Hadoop's `core-site.xml` file, respectively. Configuration classifications allow you to customize applications. For more information, refer to [Configure applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

**Engine-specific changes, enhancements, and resolved issues**
+ The following table lists Hive and Tez backports.


**Hive and Tez changes**  
<a name="table-hive-tez-660"></a>
<table>
<thead>
  <tr><th>Change</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Backport</td><td><a href="https://issues.apache.org/jira/browse/TEZ-4430">TEZ-4430</a>: Fixed issue with <code>tez.task.launch.cmd-opts</code> property</td></tr>
  <tr><td>Backport</td><td><a href="https://issues.apache.org/jira/browse/HIVE-25971">HIVE-25971</a>: Fixed Tez task shutdown delays due to open cached thread pool</td></tr>
</tbody>
</table>
