# Using Amazon EMR container defaults classification

## Overview

The following settings are available under the `emr-containers-defaults`
classification:

**`job-start-timeout`**

By default, a job will time out if it cannot start and it waits in the `SUBMITTED` state for 15 minutes. This configuration changes the number of seconds
to wait before the job times out.

**`executor.logging`**

Enables or disables logging on the executor pods. When this is set to `DISABLED` the logging container is removed from the executor pods, which will
disable any logging for these pods specified in the `monitoringConfiguration`,
such as `s3MonitoringConfiguration` or `cloudWatchMonitoringConfiguration`.
When this setting is not set or is set to any other value, logging on the executor pods is enabled.

**`logging.image`**

Sets a custom image to be used for the logging container on the driver and executor
pods.

**`logging.request.cores`**

Sets a custom value for the number of CPUs, in CPU units, for the logging container
on the driver and executor pods. By default, this is not set.

**`logging.request.memory`**

Sets a custom value for the amount of memory, in bytes, for the logging container on
the driver and executor pods. By default, this is set to **512Mi**.
A mebibyte is a unit of measure that's similar to a megabyte.

## Job submitter classification examples

###### In this section

- [StartJobRun request with custom job timeout](#emr-eks-job-submitter-container-custom-timeout "#emr-eks-job-submitter-container-custom-timeout")
- [StartJobRun request with logging disabled for executor pods](#emr-eks-executor-logging-disabled "#emr-eks-executor-logging-disabled")
- [StartJobRun request with custom logging container image, CPU, and memory for the driver and executor pods](#emr-eks-job-submitter-container-custom-image-cpu "#emr-eks-job-submitter-container-custom-image-cpu")

### `StartJobRun` request with custom job timeout

```
{
  "name": "spark-python",
  "virtualClusterId": "`virtual-cluster-id`",
  "executionRoleArn": "`execution-role-arn`",
  "releaseLabel": "`emr-6.11.0-latest`",
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "s3://`S3-prefix`/trip-count.py"
    }
  },
  "configurationOverrides": {
    "applicationConfiguration": [
      {
        "classification": "emr-containers-defaults",
        "properties": {
          "job-start-timeout": "1800"
        }
      }
    ],
    "monitoringConfiguration": {
      "cloudWatchMonitoringConfiguration": {
        "logGroupName": "/emr-containers/jobs",
        "logStreamNamePrefix": "demo"
      },
      "s3MonitoringConfiguration": {
        "logUri": "s3://joblogs"
      }
    }
  }
}
```

### `StartJobRun` request with logging disabled for executor pods

```
"configurationOverrides": {
  "applicationConfiguration": [
    {
      "classification": "emr-containers-defaults",
      "properties": {
        "executor.logging": "DISABLED"
      }
    }
  ],
  "monitoringConfiguration": {
    "cloudWatchMonitoringConfiguration": {
      "logGroupName": "/emr-containers/jobs",
      "logStreamNamePrefix": "demo"
    },
    "s3MonitoringConfiguration": {
      "logUri": "s3://joblogs"
    }
  }
}
```

### `StartJobRun` request with custom logging container image, CPU, and memory for the driver and executor pods

```
"configurationOverrides": {
  "applicationConfiguration": [
    {
      "classification": "emr-containers-defaults",
      "properties": {
        "logging.image": "`YOUR_ECR_IMAGE_URL`",
        "logging.request.memory": "200Mi",
        "logging.request.cores": "0.5"
      }
    }
  ],
  "monitoringConfiguration": {
    "cloudWatchMonitoringConfiguration": {
      "logGroupName": "/emr-containers/jobs",
      "logStreamNamePrefix": "demo"
    },
    "s3MonitoringConfiguration": {
      "logUri": "s3://joblogs"
    }
  }
}
```

###### Note

If the Fluentd logging container encounters an out-of-memory (OOM) error, increase the
`logging.request.memory` value. For example, set it to `1Gi` to
allocate more memory to the logging container and prevent OOM issues.
