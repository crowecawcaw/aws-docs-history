# Spark Operator Logs

You can define monitoring configuration in the following way when doing `helm install`:

```
helm install spark-operator spark-operator \
--namespace `namespace` \
--set emrContainers.awsRegion=`aws_region` \
--set emrContainers.monitoringConfiguration.image=`log_agent_image_url` \
--set emrContainers.monitoringConfiguration.s3MonitoringConfiguration.logUri=`S3_bucket_uri` \
--set emrContainers.monitoringConfiguration.cloudWatchMonitoringConfiguration.logGroupName=`log_group_name` \
--set emrContainers.monitoringConfiguration.cloudWatchMonitoringConfiguration.logStreamNamePrefix=`log_stream_prefix` \
--set emrContainers.monitoringConfiguration.sideCarResources.limits.cpuLimit=500m \
--set emrContainers.monitoringConfiguration.sideCarResources.limits.memoryLimit=512Mi \
--set emrContainers.monitoringConfiguration.containerLogRotationConfiguration.rotationSize=2GB \
--set emrContainers.monitoringConfiguration.containerLogRotationConfiguration.maxFilesToKeep=10 \
--set webhook.enable=true \
--set emrContainers.operatorExecutionRoleArn=`operator_execution_role_arn`

```

**Monitoring configuration**

The following are the available configuration options under **monitoringConfiguration**.

- **Image** (optional) – Log agent image url. Will fetch by emrReleaseLabel if not provided.
- **s3MonitoringConfiguration** – Set this option to archive to Amazon S3.
  - **logUri** – (required) – The Amazon S3 bucket path where you want to store your logs.
  - The following are sample formats for the Amazon S3 bucket paths, after the logs are uploaded. The first example shows no log rotation enabled.

  ```
  s3://${logUri}/${POD NAME}/operator/stdout.gz
  s3://${logUri}/${POD NAME}/operator/stderr.gz
  ```

  Log rotation enabled by default. You can see both a rotated file, with an incrementing index, and a current file, which is the same as the previous sample.

  ```
  s3://${logUri}/${POD NAME}/operator/stdout_YYYYMMDD_index.gz
  s3://${logUri}/${POD NAME}/operator/stderr_YYYYMMDD_index.gz
  ```

- **cloudWatchMonitoringConfiguration** – The configuration key to set up forwarding to Amazon CloudWatch.
  - **logGroupName** (required) – Name of the Amazon CloudWatch log group that you want to send logs to. The group
    automatically gets created if it doesn't exist.
  - **logStreamNamePrefix** (optional) – Name of the log stream that you want to send logs into. The default value is an
    empty string. The format in Amazon CloudWatch is as follows:

  ```
  ${logStreamNamePrefix}/${POD NAME}/STDOUT or STDERR
  ```

- **sideCarResources** (optional) – The configuration key to set resource limits on the launched Fluentd sidecar container.
  - **memoryLimit** (optional) – The memory limit. Adjust according to your needs. The default is 512Mi.
  - **cpuLimit** (optional) – The CPU limit. Adjust according to your needs. The default is 500m.

- **containerLogRotationConfiguration** (optional) – Controls the container log rotation behavior. It is enabled by default.

      + **rotationSize** (required) – Specifies file size for the log rotation. The range of possible values is from 2KB to 2GB. The
       numeric unit portion of the rotationSize parameter is passed as an integer. Since decimal values aren't supported, you can specify a rotation size of 1.5GB, for example, with the value 1500MB. The
       default is 2GB.
      + **maxFilesToKeep** (required) – Specifies the maximum number of files to retain in the container after rotation
       has taken place. The minimum value is 1, and the maximum value is 50. The default is 10.

  After configured _monitoringConfiguration_, you should be able to check spark operator pod logs on an Amazon S3 bucket or Amazon CloudWatch or both. For an Amazon S3 bucket, you need to
  wait 2 minutes for the first log file to get flushed.

To find the logs in Amazon CloudWatch, you can navigate to the following: **CloudWatch** > **Log groups** > **`Log group name`** >
`Pod name`**/operator/stderr**

Or you can navigate to: **CloudWatch** > **Log groups** > **`Log group name`** >
`Pod name`**/operator/stdout**
