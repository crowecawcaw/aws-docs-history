# Spark Application Logs

You can define this configuration in the following way.

```
apiVersion: "sparkoperator.k8s.io/v1beta2"
kind: SparkApplication
metadata:
  name: spark-pi
  namespace: `namespace`
spec:
  type: Scala
  mode: cluster
  imagePullPolicy: Always
  mainClass: org.apache.spark.examples.SparkPi
  mainApplicationFile: "local:///usr/lib/spark/examples/jars/spark-examples.jar"
  sparkVersion: "3.3.1"
  emrReleaseLabel: `emr_release_label`
  executionRoleArn: `job_execution_role_arn`
  restartPolicy:
    type: Never
  volumes:
    - name: "test-volume"
      hostPath:
        path: "/tmp"
        type: Directory
  driver:
    cores: 1
    coreLimit: "1200m"
    memory: "512m"
    labels:
      version: 3.3.1
    volumeMounts:
      - name: "test-volume"
        mountPath: "/tmp"
  executor:
    cores: 1
    instances: 1
    memory: "512m"
    labels:
      version: 3.3.1
    volumeMounts:
      - name: "test-volume"
        mountPath: "/tmp"
  monitoringConfiguration:
    image: "`log_agent_image`"
    s3MonitoringConfiguration:
      logUri: "`S3_bucket_uri`"
    cloudWatchMonitoringConfiguration:
      logGroupName: "`log_group_name`"
      logStreamNamePrefix: "`log_stream_prefix`"
    sideCarResources:
      limits:
        cpuLimit: "500m"
        memoryLimit: "250Mi"
    containerLogRotationConfiguration:
      rotationSize: "2GB"
      maxFilesToKeep: "10"
```

The following are the available configuration options under **monitoringConfiguration**.

- **Image** (optional) – Log agent image url. Will fetch by emrReleaseLabel if not provided.
- **s3MonitoringConfiguration** – Set this option to archive to Amazon S3.
  - **logUri** (required) – The Amazon S3 bucket path where you want to store your logs. The first example shows no log rotation enabled:

  ```
  s3://${`logUri`}/${`APPLICATION NAME`}-${`APPLICATION UID`}/${`POD NAME`}/stdout.gz
  s3://${`logUri`}/${`APPLICATION NAME`}-${`APPLICATION UID`}/${`POD NAME`}/stderr.gz
  ```

  Log rotation is enabled by default. You can use both a rotated file (with incrementing index) and a current file (one without the date stamp).

  ```
  s3://${`logUri`}/${`APPLICATION NAME`}-${`APPLICATION UID`}/${`POD NAME`}/stdout_YYYYMMDD_index.gz
  s3://${`logUri`}/${`APPLICATION NAME`}-${`APPLICATION UID`}/${`POD NAME`}/stderr_YYYYMMDD_index.gz
  ```

- **cloudWatchMonitoringConfiguration** – The configuration key to set up forwarding to Amazon CloudWatch.
  - **logGroupName** (required) – The name of the Cloudwatch log group that you want to send logs to. The group automatically is
    created if it doesn't exist.
  - **logStreamNamePrefix** (optional) – The Name of the log stream that you want to send logs into. The default value is an
    empty string. The format in CloudWatch is as follows:

  ```
  ${`logStreamNamePrefix`}/${`APPLICATION NAME`}-${`APPLICATION UID`}/${`POD NAME`}/stdout
  ${`logStreamNamePrefix`}/${`APPLICATION NAME`}-${`APPLICATION UID`}/${`POD NAME`}/stderr
  ```

- **sideCarResources** (optional) – The configuration key to set resource limits on the launched Fluentd sidecar container.
  - **memoryLimit** (optional) – The memory limit. Adjust according to your needs. The default is 250Mi.
  - **cpuLimit** – The CPU limit. Adjust according to your needs. The default is 500m.

- **containerLogRotationConfiguration** (optional) – Controls the container log rotation behavior. It is enabled by default.

      + **rotationSize** (required) – Specifies file size for the log rotation. The range of possible values is from 2KB to 2GB. The numeric
       unit portion of the rotationSize parameter is passed as an integer. Since decimal values aren't supported, you can specify a rotation size of 1.5GB, for example, with the value
       1500MB. The default is 2GB.
      + **maxFilesToKeep** (required) – Specifies the maximum number of files to retain in the container after rotation has taken place. The
       minimum value is 1. The maximum value is 50. The default is 10.

  After configuring monitoringConfiguration, you should be able to check your spark application driver and executor logs on an Amazon S3 bucket or CloudWatch or both. For an Amazon S3 bucket, you need to wait 2 minutes
  for the first log file to be flushed. For example, in Amazon S3, the bucket path appears like the following:

**Amazon S3** > **Buckets** > **`Bucket name`** >
`Spark application name - UUID` > `Pod Name` > **stderr.gz**

Or:

**Amazon S3** > **Buckets** > **`Bucket name`** >
`Spark application name - UUID` > `Pod Name` > **stdout.gz**

In CloudWatch, the path appears like the following:

**CloudWatch** > **Log groups** > **`Log group name`** > `Spark application name - UUID`/
`Pod name`**/stderr**

Or:

**CloudWatch** > **Log groups** > **`Log group name`** > `Spark application name - UUID`/
`Pod name`**/stdout**
