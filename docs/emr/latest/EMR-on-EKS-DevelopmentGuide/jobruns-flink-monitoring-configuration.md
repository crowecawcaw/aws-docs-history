# Use monitoring configuration

to monitor Flink Kubernetes operator and Flink jobs

Monitoring configuration lets you easily set up log archiving of your Flink application and
operator logs to S3 and/or CloudWatch (you can choose either one or both). Doing so adds a FluentD sidecar
to your JobManager and TaskManager pods and subsequently
forwards these components' logs to your configured sinks.

###### Note

You must set up IAM Roles for the service account for your Flink operator and your Flink job (Service Accounts)
to be able to use this feature, as it requires interacting with other AWS services. You must set this up using IRSA in
[Setting up the Flink Kubernetes
operator for Amazon EMR on EKS](jobruns-flink-kubernetes-operator-setup.md "jobruns-flink-kubernetes-operator-setup.md").

## Flink application logs

You can define this configuration in the following way.

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: basic-example
spec:
  image: `FLINK IMAGE TAG`
  imagePullPolicy: Always
  flinkVersion: v1_17
  flinkConfiguration:
    taskmanager.numberOfTaskSlots: "2"
  executionRoleArn: `JOB EXECUTION ROLE`
  jobManager:
    resource:
      memory: "2048m"
      cpu: 1
  taskManager:
    resource:
      memory: "2048m"
      cpu: 1
  job:
    jarURI: local:///opt/flink/examples/streaming/StateMachineExample.jar
  monitoringConfiguration:
    s3MonitoringConfiguration:
      logUri: `S3 BUCKET`
    cloudWatchMonitoringConfiguration:
      logGroupName: `LOG GROUP NAME`
      logStreamNamePrefix: `LOG GROUP STREAM PREFIX`
    sideCarResources:
      limits:
        cpuLimit: 500m
        memoryLimit: 250Mi
    containerLogRotationConfiguration:
        rotationSize: 2GB
        maxFilesToKeep: 10
```

The following are configuration options.

- `s3MonitoringConfiguration` – configuration key to set up
  forwarding to S3
  - `logUri` (required) – the S3 bucket path of where you want to store your logs.
  - The path on S3 once the logs are uploaded will look like the following.
    - No log rotation enabled:

    ```
    s3://${`logUri`}/${`POD NAME`}/`STDOUT or STDERR`.gz
    ```

    - Log rotation is enabled. You can use both a rotated file and a current file (one without the date stamp).

    ```
    s3://${`logUri`}/${`POD NAME`}/`STDOUT or STDERR`.gz
    ```

    The following format is an incrementing number.

    ```
    s3://${`logUri`}/${`POD NAME`}/stdout_`YYYYMMDD`_index.gz
    ```

  - The following IAM permissions are required to use this forwarder.

  ```
  {
      "Effect": "Allow",
      "Action": [
          "s3:PutObject"
      ],
      "Resource": [
         "`S3_BUCKET_URI`/*",
         "`S3_BUCKET_URI`"
      ]
  }
  ```

- `cloudWatchMonitoringConfiguration` – configuration key to set up
  forwarding to CloudWatch.
  - `logGroupName` (required) – nameof the CloudWatch log group that you
    want to send logs to (automatically creates the group if it doesn't exist).
  - `logStreamNamePrefix` (optional) – name of the log
    stream that you want to send logs into. Default value is an empty string. The format
    is as follows:

  ```
  ${logStreamNamePrefix}/${`POD NAME`}/`STDOUT or STDERR`
  ```

  - The following IAM permissions are required to use this forwarder.

  ```
  {
      "Effect": "Allow",
      "Action": [
          "logs:CreateLogStream",
          "logs:CreateLogGroup",
          "logs:PutLogEvents"
      ],
      "Resource": [
          "arn:aws:logs:`REGION`:`ACCOUNT-ID`:log-group:{`YOUR_LOG_GROUP_NAME`}:*",
          "arn:aws:logs:`REGION`:`ACCOUNT-ID`:log-group:{`YOUR_LOG_GROUP_NAME`}"
      ]
  }
  ```

- `sideCarResources` (optional) – the configuration key to set
  resource limits on the launched Fluentbit sidecar container.
  - `memoryLimit` (optional) – the default value is 512Mi. Adjust according to your needs.
  - `cpuLimit` (optional) – this option doesn't have a default. Adjust according to your needs.

- `containerLogRotationConfiguration` (optional) – controls the
  container log rotation behavior. It is enabled by default.
  - `rotationSize` (required) – specifies the file size for the log rotation.
    The range of possible values is from 2KB to 2GB.
    The numeric unit portion of the rotationSize parameter is passed as an integer.
    Since decimal values aren't supported, you can specify a rotation size of 1.5GB,
    for example, with the value 1500MB. The default is 2GB.
  - `maxFilesToKeep` (required) – specifies the maximum number of
    files to retain in container after rotation has taken place.
    The minimum value is 1, and the maximum value is 50. The default is 10.

## Flink operator logs

We can also enable log archiving for the operator by using the following options in the `values.yaml`
file in your helm chart installation. You can enable S3, CloudWatch, or both.

```
monitoringConfiguration:
  s3MonitoringConfiguration:
    logUri: "`S3-BUCKET`"
    totalFileSize: "1G"
    uploadTimeout: "1m"
  cloudWatchMonitoringConfiguration:
    logGroupName: "flink-log-group"
    logStreamNamePrefix: "example-job-prefix-test-2"
  sideCarResources:
    limits:
      cpuLimit: 1
      memoryLimit: 800Mi
  memoryBufferLimit: 700M
```

The following are the available configuration options under `monitoringConfiguration`.

- `s3MonitoringConfiguration` – set this option to archive to S3.
- `logUri` (required) – The S3 bucket path where you want to store your logs.
- The following are formats of what the S3 bucket paths might look like once the logs are uploaded.
  - No log rotation enabled.

  ```
  s3://${`logUri`}/${`POD NAME`}/`OPERATOR or WEBHOOK`/`STDOUT or STDERR`.gz
  ```

  - Log rotation is enabled. You can use both a rotated file and a current file (one without the date stamp).

  ```
  s3://${`logUri`}/${`POD NAME`}/`OPERATOR or WEBHOOK`/`STDOUT or STDERR`.gz
  ```

  The following format index is an incrementing number.

  ```
  s3://${`logUri`}/${`POD NAME`}/`OPERATOR or WEBHOOK`/stdout_`YYYYMMDD`_index.gz
  ```

- `cloudWatchMonitoringConfiguration` – the configuration key to set up forwarding to CloudWatch.
  - `logGroupName` (required) – name of the CloudWatch log group
    that you want to send logs to. The group automatically gets created if it doesn't exist.
  - `logStreamNamePrefix` (optional) – name of the log stream that
    you want to send logs into. The default value is an empty string.
    The format in CloudWatch is as follows:

  ```
  ${logStreamNamePrefix}/${`POD NAME`}/`STDOUT or STDERR`
  ```

- `sideCarResources` (optional) – the configuration key to set resource limits
  on the launched Fluentbit sidecar container.
  - `memoryLimit` (optional) – the memory limit. Adjust according to your needs.
    The default is 512Mi.
  - `cpuLimit` – the CPU limit. Adjust according to your needs. No default value.

- `containerLogRotationConfiguration` (optional): – controls the container log rotation behavior.
  It is enabled by default.
  - `rotationSize` (required) – specifies file size for the log rotation.
    The range of possible values is from 2KB to 2GB. The numeric unit portion of
    the rotationSize parameter is passed as an integer. Since decimal values aren't supported,
    you can specify a rotation size of 1.5GB, for example, with the value 1500MB. The default is 2GB.
  - `maxFilesToKeep` (required) – specifies the maximum number of files to
    retain in container after rotation has taken place. The minimum value is 1, and the maximum value is 50.
    The default is 10.
