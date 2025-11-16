# View persistent application user

interfaces in Amazon EMR

Starting with Amazon EMR version 5.25.0, you can connect to the persistent Spark History
Server application details hosted off-cluster using the cluster
**Summary** page or the **Application user
interfaces** tab in the console. Tez UI and YARN timeline server persistent
application interfaces are available starting with Amazon EMR version 5.30.1. One-click link
access to persistent application history provides the following benefits:

- You can quickly analyze and troubleshoot active jobs and job history without
  setting up a web proxy through an SSH connection.
- You can access application history and relevant log files for active and
  terminated clusters. The logs are available for 30 days after the application
  ends.
  Navigate to your cluster details in the console, and select the
  **Applications** tab. Select the application UI that you want once
  your cluster has launched. The application UI opens in a new browser tab. For more
  information, see [Monitoring and instrumentation](https://spark.apache.org/docs/latest/monitoring.html "https://spark.apache.org/docs/latest/monitoring.html").

You can view YARN container logs through the links on the Spark history server, YARN
timeline server, and Tez UI.

###### Note

To access YARN container logs from the Spark history server, YARN timeline server,
and Tez UI, you must enable logging to Amazon S3 for your cluster. If you don't enable
logging, the links to YARN container logs won't work.

## Logs collection

To enable one-click access to persistent application user interfaces, Amazon EMR
collects two types of logs:

- **Application event logs** are collected into
  an EMR system bucket. The event logs are encrypted at rest using Server-Side
  Encryption with Amazon S3 Managed Keys (SSE-S3). If you use a private subnet
  for your cluster, make sure to include the correct system bucket ARNs in the resource list of the Amazon S3 policy for the private subnet.
  For more information,
  see [Minimum Amazon
  S3 policy for private subnet](private-subnet-iampolicy.md "private-subnet-iampolicy.md").
- **YARN container logs** are collected into an
  Amazon S3 bucket that you own. You must enable logging for your cluster to access
  YARN container logs. For more information, see [Configure cluster logging
  and debugging](emr-plan-debugging.md "emr-plan-debugging.md").

If you need to disable this feature for privacy reasons, you can stop the daemon
by using a bootstrap script when you create a cluster, as the following example
demonstrates.

```
aws emr create-cluster --name "Stop Application UI Support" --release-label emr-7.11.0 \
--applications Name=Hadoop Name=Spark --ec2-attributes KeyName=`<myEMRKeyPairName>` \
--instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m3.xlarge InstanceGroupType=CORE,InstanceCount=1,InstanceType=m3.xlarge InstanceGroupType=TASK,InstanceCount=1,InstanceType=m3.xlarge \
--use-default-roles --bootstrap-actions Path=s3://`region`.elasticmapreduce/bootstrap-actions/run-if,Args=["instance.isMaster=true","echo Stop Application UI | sudo tee /etc/apppusher/run-apppusher; sudo systemctl stop apppusher || exit 0"]
```

After you run this bootstrap script, Amazon EMR will not collect any Spark History
Server or YARN timeline server event logs into the EMR system bucket. No application
history information will be available on the **Application user
interfaces** tab, and you will lose access to all application user
interfaces from the console.

## Large Spark event log

files

In some cases, long-running Spark jobs, such as Spark streaming, and large jobs,
such as Spark SQL queries, can generate large event logs. With large events logs,
you can quickly use up disk space on compute instances and encounter
`OutOfMemory` errors when you load Persistent UIs. To avoid
these issues, we recommend that you turn on the Spark event log rolling and
compaction feature. This feature is available on Amazon EMR versions emr-6.1.0 and later.
For more details about rolling and compaction, see [Applying compaction on rolling event log files](https://spark.apache.org/docs/latest/monitoring.html#applying-compaction-on-rolling-event-log-files "https://spark.apache.org/docs/latest/monitoring.html#applying-compaction-on-rolling-event-log-files") in the Spark
documentation.

To activate the Spark event log rolling and compaction feature, turn on the
following Spark configuration settings.

- `spark.eventLog.rolling.enabled` – Turns on event log
  rolling based on size. This setting is deactivated by default.
- `spark.eventLog.rolling.maxFileSize` – When rolling is
  activated, specifies the maximum size of the event log file before it rolls
  over. The default is 128 MB.
- `spark.history.fs.eventLog.rolling.maxFilesToRetain` –
  Specifies the maximum number of non-compacted event log files to retain. By
  default, all event log files are retained. Set to a lower number to compact
  older event logs. The lowest value is 1.

Note that compaction attempts to exclude events with outdated event log files,
such as the following. If it does discard events, you no longer see them on the
Spark History Server UI.

- Events for finished jobs and related stage or task events.
- Events for terminated executors.
- Events for completed SQL inquiries, and related job, stage, and tasks
  events.

###### To launch a cluster with rolling and compaction enabled

1. Create a `spark-configuration.json` file with the following
   configuration.

```
[
   {
     "Classification": "spark-defaults",
        "Properties": {
           "spark.eventLog.rolling.enabled": true,
           "spark.history.fs.eventLog.rolling.maxFilesToRetain": 1
        }
   }
]
```

2. Create your cluster with the Spark rolling compaction configuration as
   follows.

```
aws emr create-cluster \
--release-label emr-6.6.0 \
--instance-type m4.large \
--instance-count 2 \
--use-default-roles \
--configurations file://spark-configuration.json
```

## Permissions for viewing persistent application user interfaces

The following sample shows the role permissions required for access to persistent application user interfaces. For clusters with runtime role enabled, this
will only allow users to access applications submitted by the same user identity and runtime role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:CreatePersistentAppUI",
 "elasticmapreduce:DescribePersistentAppUI"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:*:123456789012:cluster/clusterId"
 ],
 "Sid": "AllowELASTICMAPREDUCECreatepersistentappui"
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:GetPersistentAppUIPresignedURL"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:*:123456789012:cluster/clusterId",
 "arn:aws:elasticmapreduce:*:123456789012:persistent-app-ui/*"
 ],
 "Condition": {
 "StringEqualsIfExists": {
 "elasticmapreduce:ExecutionRoleArn": [
 "arn:aws:iam::123456789012:role/executionRoleArn"
 ]
 }
 },
 "Sid": "AllowELASTICMAPREDUCEGetpersistentappuipresignedurl"
 }
 ]
}`

```

The following sample shows the role permissions required for removing the restrictions on viewing applications in the persistent
application user interfaces for runtime role enabled clusters.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:CreatePersistentAppUI",
 "elasticmapreduce:DescribePersistentAppUI",
 "elasticmapreduce:AccessAllEventLogs"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:us-east-1:123456789012:cluster/j-XXXXXXXXXXXXX"
 ],
 "Sid": "AllowELASTICMAPREDUCECreatepersistentappui"
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:GetPersistentAppUIPresignedURL"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:us-east-1:123456789012:cluster/j-XXXXXXXXXXXXX",
 "arn:aws:elasticmapreduce:us-east-1:123456789012:persistent-app-ui/*"
 ],
 "Condition": {
 "StringEqualsIfExists": {
 "elasticmapreduce:ExecutionRoleArn": [
 "arn:aws:iam::123456789012:role/YourExecutionRoleName"
 ]
 }
 },
 "Sid": "AllowELASTICMAPREDUCEGetpersistentappuipresignedurl"
 }
 ]
}`

```

## Considerations and

limitations

One-click access to persistent application user interfaces currently has the
following limitations.

- There will be at least a two-minute delay when the application details
  show up on the Spark History Server UI.
- This feature works only when the event log directory for the application
  is in HDFS. By default, Amazon EMR stores event logs in a directory of HDFS. If
  you change the default directory to a different file system, such as Amazon S3,
  this feature will not work.
- This feature is currently not available for EMR clusters with multiple
  master nodes or for EMR clusters integrated with AWS Lake Formation.
- To enable one-click access to persistent application user interfaces, you
  must have permission to the `CreatePersistentAppUI`, `DescribePersistentAppUI` and `GetPersistentAppUIPresignedURL` actions for Amazon EMR.
  If you deny an IAM principal's permission to these actions, it takes
  approximately five minutes for the permission change to propagate.
- If a cluster is a runtime role enabled cluster, when accessing the Spark History Server from the Persistent App UI, the user will only be able to access a Spark job
  if the Spark job is submitted by a runtime role.
- If a cluster is a runtime role enabled cluster, each user can access only an application submitted by the same user identity
  and runtime role.
- The `AccessAllEventLogs` action for Amazon EMR is necessary to view all applications in persistent application user interfaces
  for runtime role enabled clusters.
- If you reconfigure applications in a running cluster, the application
  history will be not available through the application UI.
- For each AWS account, the default limit for active application UIs is

200.

- In the following AWS Regions, you can access application UIs from the console with Amazon EMR 6.14.0 and higher:
  - Asia Pacific (Jakarta) (ap-southeast-3)
  - Europe (Spain) (eu-south-2)
  - Asia Pacific (Melbourne) (ap-southeast-4)
  - Israel (Tel Aviv) (il-central-1)
  - Middle East (UAE) (me-central-1)

- In the following AWS Regions, you can access application UIs from the console with Amazon EMR 5.25.0 and higher:
  - US East (N. Virginia) (us-east-1)
  - US West (Oregon) (us-west-2)
  - Asia Pacific (Mumbai) (ap-south-1)
  - Asia Pacific (Seoul) (ap-northeast-2)
  - Asia Pacific (Singapore) (ap-southeast-1)
  - Asia Pacific (Sydney) (ap-southeast-2)
  - Asia Pacific (Tokyo) (ap-northeast-1)
  - Canada (Central) (ca-central-1)
  - South America (São Paulo) (sa-east-1)
  - Europe (Frankfurt) (eu-central-1)
  - Europe (Ireland) (eu-west-1)
  - Europe (London) (eu-west-2)
  - Europe (Paris) (eu-west-3)
  - Europe (Stockholm) (eu-north-1)
  - China (Beijing) (cn-north-1)
  - China (Ningxia) (cn-northwest-1)
