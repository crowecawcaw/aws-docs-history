# Queries are unexpectedly

failing for Ranger integration with Amazon EMR

**Check Apache Ranger plugin logs (Apache Hive, EMR
RecordServer, EMR SecretAgent, etc., logs)**

This section is common across all applications that integrate with the Ranger
plugin, such as Apache Hive, EMR Record Server, and EMR SecretAgent.

**Common Error Messages**

| Error message                                                                                                                                                       | Cause                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`ERROR PolicyRefresher:272<br>• []<br>PolicyRefresher(serviceName=policy-repository): failed to<br>find service. Will clean up local cache of policies<br>(-1)`** | This error messages means that the service name you provided<br>in the EMR security configuration does not match a service<br>policy repository in the Ranger Admin server. |

If within Ranger Admin server your AMAZON-EMR-SPARK service looks like the
following, then you should enter `amazonemrspark` as the
service name.

![Ranger Admin server showing AMAZON-EMR-SPARK troubleshooting.](images/ranger-amazon-emr-spark-troubleshooting.png)
